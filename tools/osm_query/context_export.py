"""Deterministic OSM context JSON for AI agents. No inferred facts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from tools.osm_common.models import Catalog, OfferingPosture, ServicePosture

OSM_VERSION = "1.3.0"
UNKNOWN = "UNKNOWN"

SERVICE_POSTURE_KEYS = (
    "operational_criticality",
    "availability_target",
    "response_target",
    "resolution_target",
    "data_classification",
    "security_classification",
    "privacy_classification",
    "vendor_support_status",
    "financial_owner",
    "ai_act_applicable",
)

OFFERING_POSTURE_KEYS = (
    "rto",
    "rpo",
    "resilience_tested",
    "automation_coverage",
    "provisioning_automation",
    "self_service",
    "chargeback_model",
    "unit_cost",
)


def _unknown(value: Any) -> str | bool | int | float:
    if value is None or value == "":
        return UNKNOWN
    if isinstance(value, str) and value.strip().lower() in {"not-assessed", "unknown"}:
        return UNKNOWN
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value
    return str(value)


def _service_boundary(posture: ServicePosture | None) -> dict[str, Any]:
    if posture is None:
        return {key: UNKNOWN for key in SERVICE_POSTURE_KEYS}
    raw = {
        "operational_criticality": posture.operational_criticality,
        "availability_target": posture.availability_target,
        "response_target": posture.response_target,
        "resolution_target": posture.resolution_target,
        "data_classification": posture.data_classification,
        "security_classification": posture.security_classification,
        "privacy_classification": posture.privacy_classification,
        "vendor_support_status": posture.vendor_support_status,
        "financial_owner": posture.financial_owner,
        "ai_act_applicable": posture.ai_act_applicable,
    }
    return {key: _unknown(raw[key]) for key in SERVICE_POSTURE_KEYS}


def _offering_boundary(row: OfferingPosture | None) -> dict[str, Any]:
    if row is None:
        return {key: UNKNOWN for key in OFFERING_POSTURE_KEYS}
    raw = {
        "rto": row.rto,
        "rpo": row.rpo,
        "resilience_tested": row.resilience_tested,
        "automation_coverage": row.automation_coverage,
        "provisioning_automation": row.provisioning_automation,
        "self_service": row.self_service,
        "chargeback_model": row.chargeback_model,
        "unit_cost": row.unit_cost,
    }
    return {key: _unknown(raw[key]) for key in OFFERING_POSTURE_KEYS}


def _offering_posture_row(
    posture: ServicePosture | None, offering_id: str
) -> OfferingPosture | None:
    if posture is None:
        return None
    for row in posture.offering_posture:
        if row.offering_id == offering_id:
            return row
    return None


def build_agent_context(catalog: Catalog) -> dict[str, Any]:
    """Single JSON object. Unassessed mapping fields are stripped."""
    posture_by_service = catalog.posture_by_service_id()
    services_out: list[dict[str, Any]] = []
    for service in sorted(catalog.services, key=lambda item: item.id):
        posture = posture_by_service.get(service.id)
        offerings_out: list[dict[str, Any]] = []
        for offering in sorted(service.offerings, key=lambda item: item.id):
            row = _offering_posture_row(posture, offering.id)
            offerings_out.append(
                {
                    "id": offering.id,
                    "name": offering.name,
                    "providers": list(catalog.offering_providers(service, offering)),
                    "operational_boundary": _offering_boundary(row),
                }
            )
        services_out.append(
            {
                "id": service.id,
                "name": service.name,
                "technology_stack": service.technology_stack or UNKNOWN,
                "lifecycle_state": service.lifecycle_state or UNKNOWN,
                "accountable": service.accountable or UNKNOWN,
                "providers": list(service.providers),
                "operational_boundary": _service_boundary(posture),
                "offerings": offerings_out,
            }
        )

    providers_out = [
        {
            "id": provider.id,
            "name": provider.name,
            "type": provider.type or UNKNOWN,
            "substitutability": provider.substitutability or UNKNOWN,
        }
        for provider in sorted(catalog.providers, key=lambda item: item.id)
    ]

    return {
        "osm_version": OSM_VERSION,
        "catalog": str(catalog.root),
        "unknown_token": UNKNOWN,
        "notes": [
            "UNKNOWN means the fact is unset or not assessed. Do not infer a value.",
            "Framework mapping fields (ISO, NIST, GDPR, DORA locators, AI Act labels) "
            "are stripped so they cannot be over-read as certification.",
            "Vendor SLAs are not copied into availability_target.",
        ],
        "providers": providers_out,
        "services": services_out,
    }


def dumps_agent_context(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def write_agent_context(catalog: Catalog, output: str | Path) -> Path:
    path = Path(output)
    path.write_text(dumps_agent_context(build_agent_context(catalog)), encoding="utf-8")
    return path
