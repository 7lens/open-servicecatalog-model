"""Test helpers for OSM tools. Writes temporary catalogs; does not touch examples/."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
GOLDEN_ENTERPRISE = REPO_ROOT / "examples" / "reference-enterprise" / "golden-example"
GOLDEN_ESTATE = REPO_ROOT / "examples" / "reference-estate" / "golden-example"


def write_catalog(
    root: Path,
    *,
    stacks: list[dict[str, Any]] | None = None,
    services: list[dict[str, Any]] | None = None,
    providers: list[dict[str, Any]] | None = None,
    posture: list[dict[str, Any]] | None = None,
) -> Path:
    catalog_dir = root / "catalog"
    posture_dir = root / "posture"
    catalog_dir.mkdir(parents=True, exist_ok=True)
    posture_dir.mkdir(parents=True, exist_ok=True)
    (catalog_dir / "technology-stacks.yaml").write_text(
        yaml.safe_dump({"technology_stacks": stacks or []}, sort_keys=False),
        encoding="utf-8",
    )
    (catalog_dir / "services.yaml").write_text(
        yaml.safe_dump({"services": services or []}, sort_keys=False),
        encoding="utf-8",
    )
    (catalog_dir / "ict-providers.yaml").write_text(
        yaml.safe_dump({"ict_providers": providers or []}, sort_keys=False),
        encoding="utf-8",
    )
    (posture_dir / "service-posture.yaml").write_text(
        yaml.safe_dump({"service_posture": posture if posture is not None else []}, sort_keys=False),
        encoding="utf-8",
    )
    return root


def stack(stack_id: str = "compute", name: str = "Compute") -> dict[str, Any]:
    return {
        "id": stack_id,
        "name": name,
        "description": f"{name} services",
    }


def provider(provider_id: str = "aws", name: str = "Amazon Web Services, Inc.") -> dict[str, Any]:
    return {
        "id": provider_id,
        "name": name,
        "type": "cloud-infrastructure",
        "substitutability": "low",
        "gdpr_dpa_signed": None,
    }


def service(
    service_id: str,
    *,
    name: str | None = None,
    stack_name: str = "Compute",
    offerings: list[dict[str, Any]] | None = None,
    providers: list[str] | None = None,
    accountable: str | None = "Service Owner",
    characteristics: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "id": service_id,
        "name": name or service_id,
        "description": name or service_id,
        "accountable": accountable,
        "technology_stack": stack_name,
        "version": "1.0.0",
        "valid_from": "2026-01-01",
        "valid_to": None,
        "lifecycle_state": "draft",
        "service_offerings": offerings
        or [{"id": f"{service_id}.default", "name": "Default"}],
    }
    if providers:
        row["providers"] = providers
    if characteristics:
        row["characteristics"] = characteristics
    return row
