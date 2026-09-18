"""Load OSM 1.3.0 catalog/ and posture/ YAML with source locations."""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

from tools.osm_common.models import (
    Catalog,
    Characteristic,
    Location,
    Offering,
    OfferingPosture,
    Provenance,
    Provider,
    Service,
    ServicePosture,
    Stack,
)

LINE_KEY = "__osm_line__"


class CatalogLoadError(RuntimeError):
    """Catalog YAML is missing or not OSM-shaped enough to load."""


class LocationLoader(yaml.SafeLoader):
    """SafeLoader that stamps mapping start lines onto each dict."""


def _construct_mapping(loader: yaml.SafeLoader, node: yaml.MappingNode) -> dict[str, Any]:
    loader.flatten_mapping(node)
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=False)
        value = loader.construct_object(value_node, deep=False)
        mapping[key] = value
    mapping[LINE_KEY] = node.start_mark.line + 1
    return mapping


LocationLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


def _iso(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    return value


def _location(path: Path, record: dict[str, Any] | None) -> Location | None:
    if not record:
        return None
    line = record.get(LINE_KEY)
    if not isinstance(line, int):
        return Location(path, 1)
    return Location(path, line)


def _clean(record: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in record.items() if key != LINE_KEY}


def _load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return yaml.load(handle, Loader=LocationLoader)


def _parse_characteristics(path: Path, rows: Any) -> list[Characteristic]:
    if not isinstance(rows, list):
        return []
    result: list[Characteristic] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        name = row.get("name")
        if not isinstance(name, str):
            continue
        result.append(
            Characteristic(
                name=name,
                value_type=row.get("value_type") if isinstance(row.get("value_type"), str) else None,
                value=_iso(row.get("value")),
                location=_location(path, row),
                raw=_clean(row),
            )
        )
    return result


def _parse_provenance(path: Path, row: Any) -> Provenance | None:
    if not isinstance(row, dict):
        return None
    return Provenance(
        authoritative_source=_iso(row.get("authoritative_source")),
        source_system=_iso(row.get("source_system")),
        source_record_id=_iso(row.get("source_record_id")),
        last_verified=_iso(row.get("last_verified")),
        evidence_reference=_iso(row.get("evidence_reference")),
        confidence=row.get("confidence") if isinstance(row.get("confidence"), str) else None,
        discovery_method=row.get("discovery_method")
        if isinstance(row.get("discovery_method"), str)
        else None,
        location=_location(path, row),
        raw=_clean(row),
    )


def _parse_offering(path: Path, row: dict[str, Any]) -> Offering:
    providers = row.get("providers") if isinstance(row.get("providers"), list) else []
    return Offering(
        id=str(row.get("id") or ""),
        name=str(row.get("name") or ""),
        description=row.get("description") if isinstance(row.get("description"), str) else None,
        providers=[str(item) for item in providers],
        characteristics=_parse_characteristics(path, row.get("characteristics")),
        provenance=_parse_provenance(path, row.get("provenance")),
        location=_location(path, row),
        raw=_clean(row),
    )


def _parse_service(path: Path, row: dict[str, Any]) -> Service:
    offerings_raw = row.get("service_offerings")
    offerings: list[Offering] = []
    if isinstance(offerings_raw, list):
        for item in offerings_raw:
            if isinstance(item, dict):
                offerings.append(_parse_offering(path, item))
    providers = row.get("providers") if isinstance(row.get("providers"), list) else []
    accountable = row.get("accountable")
    return Service(
        id=str(row.get("id") or ""),
        name=str(row.get("name") or ""),
        description=row.get("description") if isinstance(row.get("description"), str) else None,
        accountable=str(accountable).strip() if accountable not in (None, "") else None,
        technology_stack=row.get("technology_stack")
        if isinstance(row.get("technology_stack"), str)
        else None,
        version=_iso(row.get("version")),
        valid_from=_iso(row.get("valid_from")),
        valid_to=_iso(row.get("valid_to")),
        lifecycle_state=row.get("lifecycle_state")
        if isinstance(row.get("lifecycle_state"), str)
        else None,
        providers=[str(item) for item in providers],
        characteristics=_parse_characteristics(path, row.get("characteristics")),
        offerings=offerings,
        provenance=_parse_provenance(path, row.get("provenance")),
        location=_location(path, row),
        raw=_clean(row),
    )


def _parse_stack(path: Path, row: dict[str, Any]) -> Stack:
    mappings = row.get("mappings")
    return Stack(
        id=str(row.get("id") or ""),
        name=str(row.get("name") or ""),
        description=row.get("description") if isinstance(row.get("description"), str) else None,
        mappings=mappings if isinstance(mappings, dict) else {},
        location=_location(path, row),
        raw=_clean(row),
    )


def _parse_provider(path: Path, row: dict[str, Any]) -> Provider:
    certs = row.get("certifications") if isinstance(row.get("certifications"), list) else []
    return Provider(
        id=str(row.get("id") or ""),
        name=str(row.get("name") or ""),
        type=row.get("type") if isinstance(row.get("type"), str) else None,
        substitutability=row.get("substitutability")
        if isinstance(row.get("substitutability"), str)
        else None,
        gdpr_dpa_signed=row.get("gdpr_dpa_signed"),
        dora_notification_clause=row.get("dora_notification_clause"),
        certifications=[str(item) for item in certs],
        risk_level=row.get("risk_level") if isinstance(row.get("risk_level"), str) else None,
        location=_location(path, row),
        raw=_clean(row),
    )


def _parse_offering_posture(path: Path, row: dict[str, Any]) -> OfferingPosture:
    controls = row.get("iso27001_controls") if isinstance(row.get("iso27001_controls"), list) else []
    functions = row.get("nist_functions") if isinstance(row.get("nist_functions"), list) else []
    return OfferingPosture(
        offering_id=str(row.get("offering_id") or ""),
        rto=_iso(row.get("rto")),
        rpo=_iso(row.get("rpo")),
        resilience_tested=row.get("resilience_tested"),
        last_resilience_test=_iso(row.get("last_resilience_test")),
        resilience_evidence=row.get("resilience_evidence"),
        cost_pool=row.get("cost_pool"),
        chargeback_model=row.get("chargeback_model"),
        unit_cost=row.get("unit_cost"),
        automation_coverage=row.get("automation_coverage"),
        provisioning_automation=row.get("provisioning_automation"),
        self_service=row.get("self_service"),
        manual_hours_week=row.get("manual_hours_week"),
        last_security_review=_iso(row.get("last_security_review")),
        asset_coverage=row.get("asset_coverage"),
        iso27001_controls=list(controls),
        iso27701_pii_role=row.get("iso27701_pii_role"),
        nist_functions=list(functions),
        nist_control_status=row.get("nist_control_status"),
        gdpr_processing_activity=row.get("gdpr_processing_activity"),
        provenance=_parse_provenance(path, row.get("provenance")),
        location=_location(path, row),
        raw=_clean(row),
    )


def _parse_service_posture(path: Path, row: dict[str, Any]) -> ServicePosture:
    offering_rows = row.get("offering_posture")
    offerings: list[OfferingPosture] = []
    if isinstance(offering_rows, list):
        for item in offering_rows:
            if isinstance(item, dict):
                offerings.append(_parse_offering_posture(path, item))
    return ServicePosture(
        service_id=str(row.get("service_id") or ""),
        operational_criticality=row.get("operational_criticality")
        if isinstance(row.get("operational_criticality"), str)
        else None,
        resilience_tier=row.get("resilience_tier")
        if isinstance(row.get("resilience_tier"), str)
        else None,
        availability_target=_iso(row.get("availability_target")),
        response_target=_iso(row.get("response_target")),
        resolution_target=_iso(row.get("resolution_target")),
        data_classification=row.get("data_classification")
        if isinstance(row.get("data_classification"), str)
        else None,
        security_classification=row.get("security_classification")
        if isinstance(row.get("security_classification"), str)
        else None,
        privacy_classification=row.get("privacy_classification")
        if isinstance(row.get("privacy_classification"), str)
        else None,
        tech_debt_score=row.get("tech_debt_score"),
        vendor_support_status=row.get("vendor_support_status")
        if isinstance(row.get("vendor_support_status"), str)
        else None,
        financial_owner=row.get("financial_owner")
        if isinstance(row.get("financial_owner"), str)
        else None,
        ai_act_applicable=row.get("ai_act_applicable"),
        ai_act_risk_class=row.get("ai_act_risk_class")
        if isinstance(row.get("ai_act_risk_class"), str)
        else None,
        offering_posture=offerings,
        provenance=_parse_provenance(path, row.get("provenance")),
        location=_location(path, row),
        raw=_clean(row),
    )


def load_catalog(root: str | Path) -> Catalog:
    """Load catalog/ YAML. Posture file is optional and may be empty."""
    catalog_root = Path(root).resolve()
    files = {
        "stacks": catalog_root / "catalog" / "technology-stacks.yaml",
        "services": catalog_root / "catalog" / "services.yaml",
        "providers": catalog_root / "catalog" / "ict-providers.yaml",
        "posture": catalog_root / "posture" / "service-posture.yaml",
    }
    missing = [str(path) for key, path in files.items() if key != "posture" and not path.is_file()]
    if missing:
        raise CatalogLoadError("missing required catalog files:\n  " + "\n  ".join(missing))

    stacks_doc = _load_yaml(files["stacks"]) or {}
    services_doc = _load_yaml(files["services"]) or {}
    providers_doc = _load_yaml(files["providers"]) or {}
    if files["posture"].is_file():
        posture_doc = _load_yaml(files["posture"]) or {}
    else:
        posture_doc = {}

    if not isinstance(stacks_doc, dict) or not isinstance(services_doc, dict) or not isinstance(
        providers_doc, dict
    ):
        raise CatalogLoadError(f"{catalog_root} does not contain OSM mapping documents")

    stacks_raw = stacks_doc.get("technology_stacks")
    services_raw = services_doc.get("services")
    providers_raw = providers_doc.get("ict_providers")
    posture_raw = posture_doc.get("service_posture") if isinstance(posture_doc, dict) else None

    if not isinstance(stacks_raw, list):
        raise CatalogLoadError("catalog/technology-stacks.yaml must contain a technology_stacks list")
    if not isinstance(services_raw, list):
        raise CatalogLoadError("catalog/services.yaml must contain a services list")
    if not isinstance(providers_raw, list):
        raise CatalogLoadError("catalog/ict-providers.yaml must contain an ict_providers list")
    if posture_raw is None:
        posture_raw = []
    if not isinstance(posture_raw, list):
        raise CatalogLoadError("posture/service-posture.yaml must contain a service_posture list")

    stacks = [_parse_stack(files["stacks"], row) for row in stacks_raw if isinstance(row, dict)]
    services = [_parse_service(files["services"], row) for row in services_raw if isinstance(row, dict)]
    providers = [
        _parse_provider(files["providers"], row) for row in providers_raw if isinstance(row, dict)
    ]
    posture = [
        _parse_service_posture(files["posture"], row)
        for row in posture_raw
        if isinstance(row, dict)
    ]

    return Catalog(
        root=catalog_root,
        stacks=stacks,
        services=services,
        providers=providers,
        posture=posture,
        files=files,
    )
