from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.osm_lint.engine import exit_code, lint_path
from tools.tests.support import (
    GOLDEN_ENTERPRISE,
    GOLDEN_ESTATE,
    provider,
    service,
    stack,
    write_catalog,
)


class GoldenRegressionTests(unittest.TestCase):
    def test_enterprise_golden_is_clean(self) -> None:
        _, findings = lint_path(GOLDEN_ENTERPRISE)
        self.assertEqual(findings, [], msg=[item.format_text() for item in findings])
        self.assertEqual(exit_code(findings), 0)

    def test_estate_golden_is_clean(self) -> None:
        _, findings = lint_path(GOLDEN_ESTATE)
        self.assertEqual(findings, [], msg=[item.format_text() for item in findings])
        self.assertEqual(exit_code(findings), 0)


class ProductServiceTests(unittest.TestCase):
    def test_product_named_service_is_error(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack()],
                providers=[provider()],
                services=[
                    service(
                        "compute.eks",
                        name="Amazon EKS",
                        offerings=[
                            {
                                "id": "compute.eks.managed",
                                "name": "Managed EKS",
                                "providers": ["aws"],
                            }
                        ],
                    )
                ],
            )
            _, findings = lint_path(root)
            rules = [item.rule_id for item in findings]
            self.assertIn("OSM-LINT-10.1", rules)
            self.assertEqual(exit_code(findings), 1)
            eks = next(item for item in findings if item.rule_id == "OSM-LINT-10.1")
            self.assertIn("compute.kubernetes", eks.advice)
            self.assertGreaterEqual(eks.line, 1)


class RequestCatalogTests(unittest.TestCase):
    def test_password_reset_offering_is_error(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack("sec", "Security")],
                providers=[provider("microsoft", "Microsoft")],
                services=[
                    service(
                        "sec.iam",
                        name="Workforce Identity",
                        stack_name="Security",
                        offerings=[
                            {
                                "id": "sec.iam.password-reset",
                                "name": "Password reset",
                                "providers": ["microsoft"],
                            }
                        ],
                    )
                ],
            )
            _, findings = lint_path(root)
            self.assertTrue(any(item.rule_id == "OSM-LINT-10.2" for item in findings))


class IdentityConflationTests(unittest.TestCase):
    def test_mixed_identity_service_is_error(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack("identity", "Identity")],
                providers=[provider(), provider("microsoft", "Microsoft"), provider("okta", "Okta")],
                services=[
                    service(
                        "identity.iam",
                        name="IAM",
                        stack_name="Identity",
                        offerings=[
                            {
                                "id": "identity.iam.aws-iam",
                                "name": "AWS IAM",
                                "providers": ["aws"],
                            },
                            {
                                "id": "identity.iam.entra-id",
                                "name": "Entra ID",
                                "providers": ["microsoft"],
                            },
                        ],
                    )
                ],
            )
            _, findings = lint_path(root)
            self.assertTrue(any(item.rule_id == "OSM-LINT-10.3" for item in findings))

    def test_split_identity_services_are_clean(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack("identity", "Identity")],
                providers=[provider(), provider("microsoft", "Microsoft")],
                services=[
                    service(
                        "identity.cloud-authorization",
                        name="Cloud Platform Authorization",
                        stack_name="Identity",
                        offerings=[
                            {
                                "id": "identity.cloud-authorization.aws-iam",
                                "name": "AWS IAM",
                                "providers": ["aws"],
                            }
                        ],
                    ),
                    service(
                        "identity.directory-idp",
                        name="Workforce Directory",
                        stack_name="Identity",
                        offerings=[
                            {
                                "id": "identity.directory-idp.entra-id",
                                "name": "Entra ID",
                                "providers": ["microsoft"],
                            }
                        ],
                    ),
                ],
            )
            _, findings = lint_path(root)
            self.assertFalse(any(item.rule_id == "OSM-LINT-10.3" for item in findings))


class StackAndCharacteristicTests(unittest.TestCase):
    def test_vendor_tower_stack_is_error(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack("aws", "AWS")],
                providers=[provider()],
                services=[
                    service(
                        "aws.compute",
                        name="Compute",
                        stack_name="AWS",
                        offerings=[{"id": "aws.compute.default", "name": "Default"}],
                    )
                ],
            )
            _, findings = lint_path(root)
            self.assertTrue(any(item.rule_id == "OSM-LINT-10.4" for item in findings))

    def test_characteristic_duplicating_provider_is_warning(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack()],
                providers=[provider()],
                services=[
                    service(
                        "compute.virtual-machines",
                        name="Virtual Machines",
                        offerings=[
                            {
                                "id": "compute.virtual-machines.aws",
                                "name": "VMs on AWS",
                                "providers": ["aws"],
                                "characteristics": [
                                    {
                                        "name": "deployment_environment",
                                        "value_type": "string",
                                        "value": "aws",
                                    }
                                ],
                            }
                        ],
                    )
                ],
            )
            _, findings = lint_path(root)
            self.assertTrue(any(item.rule_id == "OSM-LINT-10.7" for item in findings))
            self.assertEqual(exit_code(findings), 2)

    def test_service_level_providers_on_kubernetes_is_warning(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack()],
                providers=[provider(), provider("microsoft", "Microsoft")],
                services=[
                    service(
                        "compute.kubernetes",
                        name="Managed Kubernetes",
                        providers=["aws"],
                        offerings=[
                            {
                                "id": "compute.kubernetes.aws-eks",
                                "name": "EKS",
                                "providers": ["aws"],
                            },
                            {
                                "id": "compute.kubernetes.azure-aks",
                                "name": "AKS",
                                "providers": ["microsoft"],
                            },
                        ],
                    )
                ],
            )
            _, findings = lint_path(root)
            self.assertTrue(any(item.rule_id == "OSM-LINT-10.8" for item in findings))


class PostureTrustTests(unittest.TestCase):
    def test_copied_vendor_sla_is_flagged(self) -> None:
        sla = "99.99%-multi-az"
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack()],
                providers=[provider()],
                services=[
                    service(
                        "compute.virtual-machines",
                        name="Virtual Machines",
                        offerings=[
                            {
                                "id": "compute.virtual-machines.aws",
                                "name": "EC2",
                                "providers": ["aws"],
                                "characteristics": [
                                    {
                                        "name": "vendor_availability_sla",
                                        "value_type": "string",
                                        "value": sla,
                                    }
                                ],
                            }
                        ],
                    )
                ],
                posture=[
                    {
                        "service_id": "compute.virtual-machines",
                        "availability_target": sla,
                        "offering_posture": [],
                    }
                ],
            )
            _, findings = lint_path(root)
            self.assertTrue(any(item.rule_id == "OSM-LINT-10.10" for item in findings))

    def test_gdpr_dpa_signed_true_is_error(self) -> None:
        with TemporaryDirectory() as tmp:
            aws = provider()
            aws["gdpr_dpa_signed"] = True
            root = write_catalog(
                Path(tmp),
                stacks=[stack()],
                providers=[aws],
                services=[
                    service(
                        "compute.virtual-machines",
                        name="Virtual Machines",
                        offerings=[
                            {
                                "id": "compute.virtual-machines.aws",
                                "name": "EC2",
                                "providers": ["aws"],
                            }
                        ],
                    )
                ],
            )
            _, findings = lint_path(root)
            self.assertTrue(any(item.rule_id == "OSM-LINT-10.12" for item in findings))
            self.assertEqual(exit_code(findings), 1)

    def test_nist_implemented_without_evidence_is_error(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack()],
                providers=[provider()],
                services=[
                    service(
                        "compute.virtual-machines",
                        name="Virtual Machines",
                        offerings=[
                            {
                                "id": "compute.virtual-machines.aws",
                                "name": "EC2",
                                "providers": ["aws"],
                            }
                        ],
                    )
                ],
                posture=[
                    {
                        "service_id": "compute.virtual-machines",
                        "offering_posture": [
                            {
                                "offering_id": "compute.virtual-machines.aws",
                                "nist_control_status": "implemented",
                            }
                        ],
                    }
                ],
            )
            _, findings = lint_path(root)
            self.assertTrue(any(item.rule_id == "OSM-LINT-10.12" for item in findings))


if __name__ == "__main__":
    unittest.main()
