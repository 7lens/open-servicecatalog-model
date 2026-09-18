"""Governance queries over a loaded OSM catalog. No inferred compliance."""

from __future__ import annotations

from collections import defaultdict
from typing import Any

from tools.osm_common.models import Catalog, OfferingPosture, Service, ServicePosture


def _present(value: Any) -> bool:
    return value not in (None, "", [])


def query_gaps(catalog: Catalog) -> dict[str, list[dict[str, Any]]]:
    """Owner, critical RTO/RPO, and posture-provenance gaps. Sparse is valid."""
    missing_accountable: list[dict[str, Any]] = []
    for service in catalog.services:
        if service.accountable:
            continue
        missing_accountable.append(
            {
                "service_id": service.id,
                "name": service.name,
                "technology_stack": service.technology_stack or "",
                "location": str(service.location) if service.location else "",
            }
        )

    critical_missing: list[dict[str, Any]] = []
    for posture in catalog.posture:
        if posture.operational_criticality != "critical":
            continue
        service = catalog.service_by_id().get(posture.service_id)
        rows = posture.offering_posture
        if not rows:
            critical_missing.append(
                {
                    "service_id": posture.service_id,
                    "offering_id": "",
                    "operational_criticality": "critical",
                    "rto": "",
                    "rpo": "",
                    "reason": "critical service has no offering_posture rows",
                    "location": str(posture.location) if posture.location else "",
                    "stack": service.technology_stack if service else "",
                }
            )
            continue
        for row in rows:
            if _present(row.rto) and _present(row.rpo):
                continue
            missing = []
            if not _present(row.rto):
                missing.append("rto")
            if not _present(row.rpo):
                missing.append("rpo")
            critical_missing.append(
                {
                    "service_id": posture.service_id,
                    "offering_id": row.offering_id,
                    "operational_criticality": "critical",
                    "rto": row.rto if _present(row.rto) else "",
                    "rpo": row.rpo if _present(row.rpo) else "",
                    "reason": "missing " + " and ".join(missing),
                    "location": str(row.location or posture.location or ""),
                    "stack": service.technology_stack if service else "",
                }
            )

    posture_missing_provenance: list[dict[str, Any]] = []
    for posture in catalog.posture:
        if posture.provenance is None:
            posture_missing_provenance.append(
                {
                    "grain": "service_posture",
                    "service_id": posture.service_id,
                    "offering_id": "",
                    "location": str(posture.location) if posture.location else "",
                }
            )
        for row in posture.offering_posture:
            if row.provenance is None:
                posture_missing_provenance.append(
                    {
                        "grain": "offering_posture",
                        "service_id": posture.service_id,
                        "offering_id": row.offering_id,
                        "location": str(row.location or posture.location or ""),
                    }
                )

    missing_accountable.sort(key=lambda item: item["service_id"])
    critical_missing.sort(key=lambda item: (item["service_id"], item["offering_id"]))
    posture_missing_provenance.sort(
        key=lambda item: (item["service_id"], item["grain"], item["offering_id"])
    )
    return {
        "missing_accountable": missing_accountable,
        "critical_missing_rto_rpo": critical_missing,
        "posture_missing_provenance": posture_missing_provenance,
    }


def query_providers(catalog: Catalog) -> list[dict[str, Any]]:
    """Offerings grouped by legal ICT Provider. Derived from providers[] only."""
    provider_meta = catalog.provider_by_id()
    offerings_by_provider: dict[str, set[str]] = defaultdict(set)
    stacks_by_provider: dict[str, set[str]] = defaultdict(set)
    services_by_provider: dict[str, set[str]] = defaultdict(set)

    for service in catalog.services:
        stack = service.technology_stack or ""
        for offering in service.offerings:
            sellers = catalog.offering_providers(service, offering)
            for provider_id in sellers:
                offerings_by_provider[provider_id].add(offering.id)
                if stack:
                    stacks_by_provider[provider_id].add(stack)
                services_by_provider[provider_id].add(service.id)

    rows: list[dict[str, Any]] = []
    for provider_id, offering_ids in offerings_by_provider.items():
        meta = provider_meta.get(provider_id)
        stacks = sorted(stacks_by_provider[provider_id])
        rows.append(
            {
                "provider_id": provider_id,
                "provider_name": meta.name if meta else provider_id,
                "provider_type": meta.type if meta else "",
                "offering_count": len(offering_ids),
                "stacks_affected": stacks,
                "stack_count": len(stacks),
                "service_count": len(services_by_provider[provider_id]),
                "offerings": sorted(offering_ids),
            }
        )
    rows.sort(key=lambda item: (-item["offering_count"], item["provider_id"]))
    return rows


def _offering_row(
    service: Service,
    posture: ServicePosture | None,
    offering_id: str,
) -> OfferingPosture | None:
    if posture is None:
        return None
    for row in posture.offering_posture:
        if row.offering_id == offering_id:
            return row
    return None


def query_compliance(catalog: Catalog, framework: str) -> dict[str, Any]:
    """Surface locators. Does not attest compliance."""
    key = framework.lower()
    posture_by_service = catalog.posture_by_service_id()
    provider_meta = catalog.provider_by_id()
    rows: list[dict[str, Any]] = []

    for service in catalog.services:
        posture = posture_by_service.get(service.id)
        for offering in service.offerings:
            sellers = catalog.offering_providers(service, offering)
            offering_posture = _offering_row(service, posture, offering.id)
            row: dict[str, Any] = {
                "service_id": service.id,
                "offering_id": offering.id,
                "stack": service.technology_stack or "",
                "providers": sellers,
                "provider_names": [
                    provider_meta[item].name if item in provider_meta else item for item in sellers
                ],
            }
            if key == "dora":
                row.update(
                    {
                        "operational_criticality": (
                            posture.operational_criticality if posture else None
                        ),
                        "rto": offering_posture.rto if offering_posture else None,
                        "rpo": offering_posture.rpo if offering_posture else None,
                        "resilience_tested": (
                            offering_posture.resilience_tested if offering_posture else None
                        ),
                        "note": (
                            "OSM provider linkage and recovery signals only. "
                            "OSM is not the DORA Register of Information."
                        ),
                    }
                )
            elif key == "iso27001":
                stack = catalog.stack_by_name().get(service.technology_stack or "")
                stack_iso = None
                if stack and isinstance(stack.mappings, dict):
                    stack_iso = stack.mappings.get("iso27001")
                row.update(
                    {
                        "stack_iso27001_locator": stack_iso,
                        "offering_iso27001_controls": (
                            offering_posture.iso27001_controls if offering_posture else []
                        ),
                        "note": (
                            "Control ID locators only. Not a Statement of Applicability "
                            "and not evidence that controls are implemented."
                        ),
                    }
                )
            elif key == "nist":
                row.update(
                    {
                        "nist_functions": (
                            offering_posture.nist_functions if offering_posture else []
                        ),
                        "nist_control_status": (
                            offering_posture.nist_control_status if offering_posture else None
                        ),
                        "note": (
                            "nist_control_status is an OSM assessment signal, not a "
                            "NIST CSF Profile, Category, or control-catalogue entry."
                        ),
                    }
                )
            rows.append(row)

    rows.sort(key=lambda item: (item["service_id"], item["offering_id"]))
    disclaimer = {
        "dora": (
            "These are OSM locators that may feed a DORA conversation. "
            "This report is not a Register of Information, not an Arrangement "
            "register, and not a claim of DORA compliance."
        ),
        "iso27001": (
            "These are optional ISO/IEC 27001:2022 Annex A locators. "
            "This report is not an ISMS, SoA, or certification."
        ),
        "nist": (
            "These are optional NIST CSF 2.0 Function locators plus an OSM "
            "assessment signal. This report is not a CSF Profile and not certification."
        ),
    }[key]
    return {
        "framework": key,
        "disclaimer": disclaimer,
        "rows": rows,
    }
