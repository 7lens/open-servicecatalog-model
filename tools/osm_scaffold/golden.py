"""Propose Stacks/Services/Offerings from OSM golden examples. Capability names only."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from tools.osm_common.loader import load_catalog
from tools.osm_common.models import Catalog, Offering, Provider, Service, Stack


@dataclass(frozen=True)
class Domain:
    id: str
    name: str
    stack_ids: tuple[str, ...]
    summary: str


DOMAINS: tuple[Domain, ...] = (
    Domain(
        "cloud-infrastructure",
        "Cloud Infrastructure",
        ("compute", "storage", "db"),
        "Compute, storage and managed database as technological services.",
    ),
    Domain(
        "identity-access",
        "Identity & Access",
        ("identity", "sec"),
        "Workforce IdP, cloud authorization, secrets — not a vendor IAM suite.",
    ),
    Domain(
        "devops-automation",
        "DevOps & Automation",
        ("auto",),
        "Configuration automation and AIOps as technological services.",
    ),
    Domain(
        "data-analytics",
        "Data & Analytics",
        ("data",),
        "Analytical warehouse and vendor-operated data-platform AI.",
    ),
    Domain(
        "collaboration",
        "Collaboration",
        ("collaboration",),
        "Issue tracking, email and team chat — not a Microsoft 365 SKU.",
    ),
)

GOLDEN_RELATIVE = (
    Path("examples") / "reference-enterprise" / "golden-example",
    Path("examples") / "reference-estate" / "golden-example",
)


def _char_draft(raw: dict[str, Any]) -> dict[str, Any]:
    allowed = {
        "name",
        "value_type",
        "description",
        "value",
        "default_value",
        "allowed_values",
        "min_cardinality",
        "max_cardinality",
        "configurable",
        "constraints",
    }
    return {key: raw[key] for key in allowed if key in raw}


def _offering_draft(offering: Offering) -> dict[str, Any]:
    row: dict[str, Any] = {
        "id": offering.id,
        "name": offering.name,
        "providers": list(offering.providers),
        "characteristics": [_char_draft(char.raw) for char in offering.characteristics],
    }
    if offering.description:
        row["description"] = offering.description
    return row


def _service_draft(service: Service) -> dict[str, Any]:
    return {
        "id": service.id,
        "name": service.name,
        "description": service.description or service.name,
        "technology_stack": service.technology_stack,
        "accountable": None,
        "version": service.version or "1.0.0",
        "valid_from": None,
        "valid_to": None,
        "lifecycle_state": "draft",
        "providers": [],
        "characteristics": [_char_draft(char.raw) for char in service.characteristics],
        "offerings": [_offering_draft(offering) for offering in service.offerings],
    }


def _stack_draft(stack: Stack) -> dict[str, Any]:
    return {
        "id": stack.id,
        "name": stack.name,
        "description": stack.description or stack.name,
        "mappings": {},
    }


def _provider_draft(provider: Provider) -> dict[str, Any]:
    return {
        "id": provider.id,
        "name": provider.name,
        "type": provider.type or "cloud-infrastructure",
        "substitutability": provider.substitutability or "medium",
        "gdpr_dpa_signed": None,
        "dora_notification_clause": None,
        "certifications": [],
        "risk_level": None,
    }


def load_goldens(repo_root: Path) -> list[Catalog]:
    catalogs: list[Catalog] = []
    for relative in GOLDEN_RELATIVE:
        path = repo_root / relative
        if (path / "catalog" / "services.yaml").is_file():
            catalogs.append(load_catalog(path))
    return catalogs


def merge_goldens(
    catalogs: list[Catalog],
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    stacks: dict[str, dict[str, Any]] = {}
    services: dict[str, dict[str, Any]] = {}
    providers: dict[str, dict[str, Any]] = {}
    for catalog in catalogs:
        for stack in catalog.stacks:
            stacks.setdefault(stack.id, _stack_draft(stack))
        for provider in catalog.providers:
            providers.setdefault(provider.id, _provider_draft(provider))
        for service in catalog.services:
            incoming = _service_draft(service)
            existing = services.get(service.id)
            if existing is None:
                services[service.id] = incoming
                continue
            seen = {row["id"] for row in existing["offerings"]}
            for offering in incoming["offerings"]:
                if offering["id"] not in seen:
                    existing["offerings"].append(offering)
                    seen.add(offering["id"])
    return stacks, services, providers


def propose_draft(
    repo_root: Path,
    domain_ids: list[str],
    catalogs: list[Catalog] | None = None,
) -> dict[str, Any]:
    """Stacks/services/offerings for the selected capability domains."""
    selected = [domain for domain in DOMAINS if domain.id in domain_ids]
    stack_ids: list[str] = []
    for domain in selected:
        for stack_id in domain.stack_ids:
            if stack_id not in stack_ids:
                stack_ids.append(stack_id)
    catalogs = catalogs if catalogs is not None else load_goldens(repo_root)
    stacks, services, providers = merge_goldens(catalogs)

    draft_stacks = [stacks[stack_id] for stack_id in stack_ids if stack_id in stacks]
    stack_names = {row["name"] for row in draft_stacks}
    draft_services = [
        service
        for service in services.values()
        if service.get("technology_stack") in stack_names
        or service["id"].split(".")[0] in stack_ids
    ]
    used_provider_ids: set[str] = set()
    for service in draft_services:
        for offering in service["offerings"]:
            used_provider_ids.update(offering.get("providers") or [])
    draft_providers = [providers[pid] for pid in sorted(used_provider_ids) if pid in providers]
    return {
        "domains": [domain.id for domain in selected],
        "stacks": draft_stacks,
        "services": draft_services,
        "providers": draft_providers,
    }
