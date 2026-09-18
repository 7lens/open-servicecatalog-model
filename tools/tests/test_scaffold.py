from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.osm_lint.engine import lint_path
from tools.osm_scaffold.frameworks import discover_frameworks
from tools.osm_scaffold.golden import propose_draft
from tools.osm_scaffold.state import load_state, render_tree, save_state, state_path
from tools.osm_scaffold.wizard import (
    OnboardingWizard,
    SaveAndExit,
    ScaffoldError,
    build_records,
    refuse_vendor_label,
    write_catalog_from_state,
)
from tools.tests.support import REPO_ROOT


VALID_CONFIG = {
    "stack": {
        "id": "compute",
        "name": "Compute",
        "description": "Compute technological services.",
    },
    "service": {
        "slug": "kubernetes",
        "name": "Managed Kubernetes",
        "description": "Kubernetes clusters as a technological service.",
        "accountable": "Service Owner",
    },
    "offerings": [
        {"slug": "aws-eks", "name": "Amazon EKS", "provider_id": "aws"},
    ],
    "providers": [
        {
            "id": "aws",
            "name": "Amazon Web Services, Inc.",
            "type": "cloud-infrastructure",
            "substitutability": "low",
        }
    ],
}


class ScaffoldValidationTests(unittest.TestCase):
    def test_emits_canonical_ids(self) -> None:
        records = build_records(VALID_CONFIG)
        self.assertEqual(records["service"]["id"], "compute.kubernetes")
        self.assertEqual(records["service"]["service_offerings"][0]["id"], "compute.kubernetes.aws-eks")
        self.assertEqual(records["service"]["technology_stack"], "Compute")

    def test_refuses_product_service_slug(self) -> None:
        config = {
            **VALID_CONFIG,
            "service": {**VALID_CONFIG["service"], "slug": "eks", "name": "EKS"},
        }
        with self.assertRaises(ScaffoldError) as ctx:
            build_records(config)
        self.assertIn("compute.kubernetes", str(ctx.exception))

    def test_refuses_request_offering_slug(self) -> None:
        config = {
            **VALID_CONFIG,
            "offerings": [{"slug": "password-reset", "name": "Reset", "provider_id": "aws"}],
        }
        with self.assertRaises(ScaffoldError):
            build_records(config)

    def test_refuses_vendor_stack(self) -> None:
        config = {
            **VALID_CONFIG,
            "stack": {"id": "aws", "name": "AWS", "description": "AWS"},
        }
        with self.assertRaises(ScaffoldError):
            build_records(config)

    def test_refuses_zero_offerings(self) -> None:
        config = {**VALID_CONFIG, "offerings": []}
        with self.assertRaises(ScaffoldError):
            build_records(config)


class ScaffoldCliTests(unittest.TestCase):
    def test_writes_catalog_that_passes_structural_validation(self) -> None:
        with TemporaryDirectory() as tmp:
            config_path = Path(tmp) / "config.yaml"
            config_path.write_text(
                "\n".join(
                    [
                        "stack:",
                        "  id: compute",
                        "  name: Compute",
                        "  description: Compute technological services.",
                        "service:",
                        "  slug: kubernetes",
                        "  name: Managed Kubernetes",
                        "  description: Kubernetes as a service.",
                        "  accountable: Service Owner",
                        "offerings:",
                        "  - slug: aws-eks",
                        "    name: Amazon EKS",
                        "    provider_id: aws",
                        "providers:",
                        "  - id: aws",
                        "    name: Amazon Web Services, Inc.",
                        "    type: cloud-infrastructure",
                        "    substitutability: low",
                    ]
                ),
                encoding="utf-8",
            )
            out = Path(tmp) / "catalog-out"
            cli = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "tools.osm_scaffold.cli",
                    "--config",
                    str(config_path),
                    "--output",
                    str(out),
                ],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(cli.returncode, 0, cli.stderr)
            validate = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "validation" / "validate.py"),
                    "--catalog",
                    str(out),
                ],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)

    def test_cli_refuses_eks_slug(self) -> None:
        with TemporaryDirectory() as tmp:
            config_path = Path(tmp) / "config.yaml"
            config_path.write_text(
                "stack:\n  id: compute\n  name: Compute\n"
                "service:\n  slug: eks\n  name: EKS\n"
                "offerings:\n  - slug: managed\n    name: Managed\n",
                encoding="utf-8",
            )
            cli = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "tools.osm_scaffold.cli",
                    "--config",
                    str(config_path),
                ],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(cli.returncode, 1)
            self.assertIn("product token", cli.stderr)


class FrameworkAndGoldenTests(unittest.TestCase):
    def test_discovers_togaf_and_dora(self) -> None:
        found = {item.id: item for item in discover_frameworks(REPO_ROOT)}
        self.assertIn("togaf", found)
        self.assertIn("dora", found)
        self.assertIn("togaf_domain", found["togaf"].stack_fields)

    def test_golden_proposal_for_devops(self) -> None:
        draft = propose_draft(REPO_ROOT, ["devops-automation"])
        stack_ids = [row["id"] for row in draft["stacks"]]
        service_ids = [row["id"] for row in draft["services"]]
        self.assertIn("auto", stack_ids)
        self.assertTrue(any(item.startswith("auto.") for item in service_ids))
        self.assertTrue(all(service.get("offerings") for service in draft["services"]))

    def test_rejects_vendor_domain_label(self) -> None:
        with self.assertRaises(ScaffoldError):
            refuse_vendor_label("AWS")
        with self.assertRaises(ScaffoldError):
            refuse_vendor_label("Microsoft")


class QueueAsk:
    def __init__(self, answers: list[str]) -> None:
        self.answers = list(answers)
        self.prompts: list[str] = []

    def __call__(self, prompt: str) -> str:
        self.prompts.append(prompt)
        if not self.answers:
            raise AssertionError(f"no scripted answer left for: {prompt}")
        return self.answers.pop(0)


def _keep_defaults_for_draft(draft: dict) -> list[str]:
    answers = ["none", "3", ""]
    for _stack in draft["stacks"]:
        answers.append("")
    answers.append("n")
    for _service in draft["services"]:
        answers.append("")
    answers.append("n")
    for service in draft["services"]:
        for _offering in service["offerings"]:
            answers.append("")
        answers.append("n")
    for _stack in draft["stacks"]:
        answers.append("")
    for _service in draft["services"]:
        answers.extend(["", "", ""])
    for service in draft["services"]:
        for _offering in service["offerings"]:
            answers.extend(["", "n"])
    return answers


class OnboardingWizardTests(unittest.TestCase):
    def test_view_and_save_checkpoint(self) -> None:
        with TemporaryDirectory() as tmp:
            catalog_dir = Path(tmp) / "servicecatalog"
            ask = QueueAsk([":view", ":save"])
            wizard = OnboardingWizard(REPO_ROOT, catalog_dir, ask=ask, echo=lambda _msg: None)
            with self.assertRaises(SaveAndExit):
                wizard.run(resume=False)
            self.assertTrue(state_path(catalog_dir).is_file())
            saved = load_state(catalog_dir)
            assert saved is not None
            self.assertEqual(saved["step"], "frameworks")
            tree = render_tree(saved)
            self.assertIn("step:", tree)

    def test_resume_compile_writes_yaml_and_clears_checkpoint(self) -> None:
        with TemporaryDirectory() as tmp:
            catalog_dir = Path(tmp) / "servicecatalog"
            draft = propose_draft(REPO_ROOT, ["devops-automation"])
            state = {
                "step": "compile",
                "cursor": 0,
                "frameworks": [],
                "domains": ["devops-automation"],
                "stacks": draft["stacks"],
                "services": draft["services"],
                "providers": draft["providers"],
            }
            for service in state["services"]:
                service["accountable"] = "Service Owner"
                service["lifecycle_state"] = "draft"
                service["version"] = "1.0.0"
                service["valid_from"] = "2026-01-01"
            save_state(catalog_dir, state)
            wizard = OnboardingWizard(REPO_ROOT, catalog_dir, ask=QueueAsk([]), echo=lambda _msg: None)
            wizard.run(resume=True)
            self.assertFalse(state_path(catalog_dir).is_file())
            self.assertTrue((catalog_dir / "catalog" / "services.yaml").is_file())
            validate = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "validation" / "validate.py"),
                    "--catalog",
                    str(catalog_dir),
                ],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(validate.returncode, 0, validate.stderr + validate.stdout)
            _, findings = lint_path(catalog_dir)
            self.assertEqual(findings, [], msg=[item.format_text() for item in findings])

    def test_scripted_wizard_keep_defaults(self) -> None:
        draft = propose_draft(REPO_ROOT, ["devops-automation"])
        answers = _keep_defaults_for_draft(draft)
        with TemporaryDirectory() as tmp:
            catalog_dir = Path(tmp) / "servicecatalog"
            ask = QueueAsk(answers)
            wizard = OnboardingWizard(REPO_ROOT, catalog_dir, ask=ask, echo=lambda _msg: None)
            wizard.run(resume=False)
            self.assertEqual(ask.answers, [])
            self.assertTrue((catalog_dir / "catalog" / "technology-stacks.yaml").is_file())
            self.assertFalse(state_path(catalog_dir).is_file())

    def test_write_catalog_from_state_helper(self) -> None:
        with TemporaryDirectory() as tmp:
            catalog_dir = Path(tmp)
            draft = propose_draft(REPO_ROOT, ["devops-automation"])
            for service in draft["services"]:
                service["accountable"] = "Platform Lead"
            write_catalog_from_state(catalog_dir, draft)
            text = (catalog_dir / "catalog" / "services.yaml").read_text(encoding="utf-8")
            self.assertIn("auto.", text)


if __name__ == "__main__":
    unittest.main()
