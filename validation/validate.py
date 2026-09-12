#!/usr/bin/env python3
"""Validate an Open Services Data Model catalog.

Checks identifiers, required fields, parent-child offering IDs,
cross-file references and a small set of enums. This is a catalog
integrity tool, not a product platform.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("PyYAML is required. Install with: pip install -r validation/requirements.txt\n")
    sys.exit(2)

SEGMENT = r"[a-z0-9]+(?:-[a-z0-9]+)*"
SERVICE_ID = re.compile(rf"^{SEGMENT}\.{SEGMENT}$")
OFFERING_ID = re.compile(rf"^{SEGMENT}\.{SEGMENT}\.{SEGMENT}$")
STACK_ID = re.compile(rf"^{SEGMENT}$")
PROVIDER_ID = re.compile(rf"^{SEGMENT}$")

AI_ACT_OFFERING_FIELDS = {
    "ai_act_intended_purpose",
    "ai_act_human_oversight",
    "ai_act_transparency_level",
    "ai_act_conformity_assessment",
    "ai_act_training_data_doc",
}

LIFECYCLE = {"draft", "pilot", "production", "sunset", "retired"}
CRITICALITY = {"critical", "important", "standard"}
CLASSIFICATION = {"public", "internal", "confidential", "restricted"}
VENDOR_SUPPORT = {"active", "extended", "end-of-life"}
AI_RISK = {"unacceptable", "high-risk", "limited-risk", "minimal-risk", "not-applicable"}
CHARGEBACK = {"shared", "dedicated", "consumption"}
AUTOMATION = {"none", "partial", "full"}
ASSET_COVERAGE = {"complete", "partial", "unknown"}
PII_ROLE = {"controller", "processor", "joint-controller", "none"}
PII_CATEGORY = {
    "identity",
    "financial",
    "health",
    "behavioral",
    "location",
    "biometric",
    "communications",
    "none",
}
NIST = {"govern", "identify", "protect", "detect", "respond", "recover"}
NIST_STATUS = {"implemented", "partially-implemented", "planned", "not-applicable"}
ERASURE = {True, False, "partial", "not-applicable"}
PROVIDER_TYPE = {
    "cloud-infrastructure",
    "cloud-platform",
    "managed-service",
    "software-vendor",
    "network-provider",
    "data-center",
}
SUBSTITUTABILITY = {"low", "medium", "high"}
RISK_LEVEL = {"low", "medium", "high", "critical"}
VALUE_TYPES = {"string", "number", "boolean", "date"}
NAME_KEY = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
CONFIDENCE = {"high", "medium", "low", "unknown"}
DISCOVERY = {"declared", "imported", "discovered", "manual"}
PRIVACY_CLASS = {"none", "pii", "sensitive", "not-assessed"}
PROVENANCE_KEYS = {
    "authoritative_source",
    "source_system",
    "source_record_id",
    "last_verified",
    "evidence_reference",
    "confidence",
    "discovery_method",
}
PROHIBITED_REL = {
    "depends_on",
    "consumes",
    "provides_to",
    "related_service",
    "related_services",
}
REMOVED_CANONICAL_COPIES = {
    "dora_rto",
    "dora_rpo",
    "dora_resilience_tested",
    "dora_criticality",
    "cloud_providers",
    "dora_third_party_deps",
    "services_consumed",
}
REMOVED_PROVIDER_FIELDS = {
    "criticality",
    "services_consumed",
}


class Reporter:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def ok(self) -> bool:
        return not self.errors


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def parse_iso_date(value: Any) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def validate_characteristics(parent_id: str, rows: Any, reporter: Reporter) -> None:
    if rows is None:
        return
    if not isinstance(rows, list):
        reporter.error(f"{parent_id} characteristics must be a list")
        return
    seen: set[str] = set()
    for item in rows:
        if not isinstance(item, dict):
            reporter.error(f"{parent_id} characteristic must be a mapping")
            continue
        name = item.get("name")
        if not isinstance(name, str) or not NAME_KEY.match(name):
            reporter.error(f"{parent_id} has invalid characteristic name {name!r}")
            continue
        if name in seen:
            reporter.error(f"{parent_id} has duplicate characteristic name {name}")
        seen.add(name)
        value_type = item.get("value_type")
        if value_type not in VALUE_TYPES:
            reporter.error(f"{parent_id}.{name} has invalid value_type {value_type!r}")
        allowed = item.get("allowed_values")
        if allowed is not None and not isinstance(allowed, list):
            reporter.error(f"{parent_id}.{name} allowed_values must be a list")
            allowed = None
        value = item.get("value", None)
        if value is not None and allowed and value not in allowed:
            reporter.error(f"{parent_id}.{name} value {value!r} is not in allowed_values")
        default = item.get("default_value", None)
        if default is not None and allowed and default not in allowed:
            reporter.error(
                f"{parent_id}.{name} default_value {default!r} is not in allowed_values"
            )
        min_card = item.get("min_cardinality", 0)
        max_card = item.get("max_cardinality", None)
        if min_card is not None and not (isinstance(min_card, int) and min_card >= 0):
            reporter.error(f"{parent_id}.{name} has invalid min_cardinality")
            min_card = 0
        if max_card is not None and not (isinstance(max_card, int) and max_card >= 1):
            reporter.error(f"{parent_id}.{name} has invalid max_cardinality")
        elif isinstance(max_card, int) and isinstance(min_card, int) and max_card < min_card:
            reporter.error(f"{parent_id}.{name} max_cardinality is less than min_cardinality")
        if "configurable" in item and not isinstance(item.get("configurable"), bool):
            reporter.error(f"{parent_id}.{name} configurable must be a boolean")
        constraints = item.get("constraints")
        if constraints is not None:
            if not isinstance(constraints, dict):
                reporter.error(f"{parent_id}.{name} constraints must be a mapping")
            else:
                extra = set(constraints) - {"min", "max", "pattern"}
                if extra:
                    reporter.error(f"{parent_id}.{name} has unknown constraint keys {sorted(extra)}")


def parent_service_id(offering_id: str) -> str:
    return ".".join(offering_id.split(".")[:2])


def reject_service_relationships(owner_id: str, record: dict[str, Any], reporter: Reporter) -> None:
    present = sorted(PROHIBITED_REL.intersection(record))
    if present:
        reporter.error(
            f"{owner_id} must not declare Service-to-Service relationship fields {present}"
        )


def validate_provenance(owner_id: str, row: Any, reporter: Reporter) -> None:
    if row is None:
        return
    if not isinstance(row, dict):
        reporter.error(f"{owner_id} provenance must be a mapping")
        return
    extra = set(row) - PROVENANCE_KEYS
    if extra:
        reporter.error(f"{owner_id} provenance has unknown keys {sorted(extra)}")
    if "confidence" in row and row["confidence"] not in CONFIDENCE:
        reporter.error(f"{owner_id} provenance has invalid confidence {row['confidence']!r}")
    if "discovery_method" in row and row["discovery_method"] not in DISCOVERY:
        reporter.error(
            f"{owner_id} provenance has invalid discovery_method {row['discovery_method']!r}"
        )
    if row.get("last_verified") is not None and parse_iso_date(row.get("last_verified")) is None:
        reporter.error(f"{owner_id} provenance has invalid last_verified")
    for key in ("authoritative_source", "source_system", "source_record_id", "evidence_reference"):
        value = row.get(key)
        if value is not None and not (isinstance(value, str) and value.strip()):
            reporter.error(f"{owner_id} provenance {key} must be a non-empty string")


def validate_provider_refs(owner_id: str, refs: Any, provider_ids: set[str], reporter: Reporter) -> None:
    if refs is None:
        return
    if not isinstance(refs, list):
        reporter.error(f"{owner_id} providers must be a list of ICT Provider ids")
        return
    seen: set[str] = set()
    for ref in refs:
        if not isinstance(ref, str) or not PROVIDER_ID.match(ref):
            reporter.error(f"{owner_id} has invalid provider id {ref!r}")
            continue
        if ref in seen:
            reporter.error(f"{owner_id} has duplicate provider id {ref}")
        seen.add(ref)
        if ref not in provider_ids:
            reporter.error(
                f"{owner_id} providers references unknown ICT Provider {ref}"
            )


def validate_catalog(catalog_dir: Path) -> list[str]:
    reporter = Reporter()
    files = {
        "stacks": catalog_dir / "technology-stacks.yaml",
        "services": catalog_dir / "services.yaml",
        "attributes": catalog_dir / "service-attributes.yaml",
        "providers": catalog_dir / "ict-providers.yaml",
    }
    for label, path in files.items():
        if not path.is_file():
            reporter.error(f"missing file: {path}")
    if reporter.errors:
        return reporter.errors

    stacks_doc = load_yaml(files["stacks"]) or {}
    services_doc = load_yaml(files["services"]) or {}
    attributes_doc = load_yaml(files["attributes"]) or {}
    providers_doc = load_yaml(files["providers"]) or {}

    stacks = stacks_doc.get("technology_stacks")
    services = services_doc.get("services")
    attributes = attributes_doc.get("service_attributes")
    providers = providers_doc.get("ict_providers")

    if not isinstance(stacks, list):
        reporter.error("technology-stacks.yaml must contain a technology_stacks list")
        stacks = []
    if not isinstance(services, list):
        reporter.error("services.yaml must contain a services list")
        services = []
    if not isinstance(attributes, list):
        reporter.error("service-attributes.yaml must contain a service_attributes list")
        attributes = []
    if not isinstance(providers, list):
        reporter.error("ict-providers.yaml must contain an ict_providers list")
        providers = []

    provider_ids: set[str] = set()
    for provider in providers:
        if not isinstance(provider, dict):
            reporter.error("ict provider entry must be a mapping")
            continue
        provider_id = provider.get("id")
        if not isinstance(provider_id, str) or not PROVIDER_ID.match(provider_id):
            reporter.error(f"invalid provider id: {provider_id!r}")
        elif provider_id in provider_ids:
            reporter.error(f"duplicate provider id: {provider_id}")
        else:
            provider_ids.add(provider_id)
        if not provider.get("name"):
            reporter.error(f"provider {provider_id!r} is missing name")
        provider_type = provider.get("type")
        if provider_type not in PROVIDER_TYPE:
            reporter.error(f"provider {provider_id!r} has invalid type {provider_type!r}")
        if provider.get("substitutability") not in SUBSTITUTABILITY:
            reporter.error(f"provider {provider_id!r} has invalid substitutability")
        extra_provider = sorted(REMOVED_PROVIDER_FIELDS.intersection(provider))
        if extra_provider:
            reporter.error(
                f"provider {provider_id!r} uses removed fields {extra_provider}; "
                "use risk_level for severity (OSM-M-009) and derive reverse "
                "links from providers (OSM-M-010)"
            )
        if "risk_level" in provider and provider["risk_level"] not in RISK_LEVEL | {None}:
            reporter.error(f"provider {provider_id!r} has invalid risk_level")

    stack_ids: set[str] = set()
    stack_names: set[str] = set()
    for stack in stacks:
        if not isinstance(stack, dict):
            reporter.error("technology stack entry must be a mapping")
            continue
        stack_id = stack.get("id")
        name = stack.get("name")
        if not stack.get("description"):
            reporter.error(f"stack {stack_id!r} is missing description")
        if not isinstance(stack_id, str) or not STACK_ID.match(stack_id):
            reporter.error(f"invalid stack id: {stack_id!r}")
        elif stack_id in stack_ids:
            reporter.error(f"duplicate stack id: {stack_id}")
        else:
            stack_ids.add(stack_id)
        if not isinstance(name, str) or not name.strip():
            reporter.error(f"stack {stack_id!r} is missing name")
        elif name in stack_names:
            reporter.error(f"duplicate stack name: {name}")
        else:
            stack_names.add(name)

    service_ids: set[str] = set()
    offering_ids: set[str] = set()
    offerings_by_service: dict[str, set[str]] = {}

    for service in services:
        if not isinstance(service, dict):
            reporter.error("service entry must be a mapping")
            continue
        service_id = service.get("id")
        for field in ("name", "description", "accountable", "technology_stack", "version", "valid_from", "lifecycle_state"):
            if not service.get(field):
                reporter.error(f"service {service_id!r} is missing {field}")
        if service.get("lifecycle_state") not in LIFECYCLE:
            reporter.error(f"service {service_id!r} has invalid lifecycle_state")
        valid_from = parse_iso_date(service.get("valid_from"))
        if service.get("valid_from") is not None and valid_from is None:
            reporter.error(f"service {service_id!r} has invalid valid_from")
        valid_to_raw = service.get("valid_to", None)
        if valid_to_raw is not None:
            valid_to = parse_iso_date(valid_to_raw)
            if valid_to is None:
                reporter.error(f"service {service_id!r} has invalid valid_to")
            elif valid_from is not None and valid_to < valid_from:
                reporter.error(f"service {service_id!r} valid_to is before valid_from")
        validate_characteristics(str(service_id), service.get("characteristics"), reporter)
        validate_provider_refs(str(service_id), service.get("providers"), provider_ids, reporter)
        validate_provenance(str(service_id), service.get("provenance"), reporter)
        if isinstance(service, dict):
            reject_service_relationships(str(service_id), service, reporter)
        if not isinstance(service_id, str) or not SERVICE_ID.match(service_id):
            reporter.error(f"invalid service id (need 2 segments): {service_id!r}")
        elif service_id in service_ids:
            reporter.error(f"duplicate service id: {service_id}")
        else:
            service_ids.add(service_id)

        stack_name = service.get("technology_stack")
        if isinstance(stack_name, str) and stack_name not in stack_names:
            reporter.error(
                f"service {service_id!r} references unknown technology_stack {stack_name!r}"
            )

        offerings = service.get("service_offerings")
        if not isinstance(offerings, list) or not offerings:
            reporter.error(f"service {service_id!r} must have at least one offering")
            continue
        offerings_by_service[service_id] = set()
        for offering in offerings:
            if not isinstance(offering, dict):
                reporter.error(f"offering under {service_id!r} must be a mapping")
                continue
            offering_id = offering.get("id")
            if not offering.get("name"):
                reporter.error(f"offering {offering_id!r} is missing name")
            if not isinstance(offering_id, str) or not OFFERING_ID.match(offering_id):
                reporter.error(f"invalid offering id (need 3 segments): {offering_id!r}")
                continue
            if offering_id in offering_ids:
                reporter.error(f"duplicate offering id: {offering_id}")
            offering_ids.add(offering_id)
            if parent_service_id(offering_id) != service_id:
                reporter.error(
                    f"offering {offering_id} is not a child of service {service_id}"
                )
            offerings_by_service[service_id].add(offering_id)
            validate_characteristics(str(offering_id), offering.get("characteristics"), reporter)
            validate_provider_refs(str(offering_id), offering.get("providers"), provider_ids, reporter)
            validate_provenance(str(offering_id), offering.get("provenance"), reporter)
            reject_service_relationships(str(offering_id), offering, reporter)

    seen_attribute_services: set[str] = set()
    for record in attributes:
        if not isinstance(record, dict):
            reporter.error("service_attributes entry must be a mapping")
            continue
        service_id = record.get("service_id")
        if service_id not in service_ids:
            reporter.error(f"service_attributes references unknown service_id {service_id!r}")
            continue
        if service_id in seen_attribute_services:
            reporter.error(f"duplicate service_attributes for {service_id}")
        seen_attribute_services.add(service_id)
        if "lifecycle_state" in record:
            reporter.error(
                f"{service_id} service_attributes must not include lifecycle_state; it belongs on Service"
            )
        extra_copies = sorted(REMOVED_CANONICAL_COPIES.intersection(record))
        if extra_copies:
            reporter.error(
                f"{service_id} service_attributes uses removed duplicate fields {extra_copies}; "
                "use the canonical OSM field (OSM-M-008)"
            )
        score = record.get("tech_debt_score", None)
        if score is not None and not (isinstance(score, int) and 0 <= score <= 100):
            reporter.error(f"{service_id} has invalid tech_debt_score")
        if "data_classification" in record and record["data_classification"] not in CLASSIFICATION:
            reporter.error(f"{service_id} has invalid data_classification")
        if "vendor_support_status" in record and record["vendor_support_status"] not in VENDOR_SUPPORT:
            reporter.error(f"{service_id} has invalid vendor_support_status")
        if "ai_act_risk_class" in record and record["ai_act_risk_class"] not in AI_RISK:
            reporter.error(f"{service_id} has invalid ai_act_risk_class")
        if "operational_criticality" in record and record["operational_criticality"] not in CRITICALITY:
            reporter.error(f"{service_id} has invalid operational_criticality")
        if "security_classification" in record and record["security_classification"] not in CLASSIFICATION:
            reporter.error(f"{service_id} has invalid security_classification")
        if "privacy_classification" in record and record["privacy_classification"] not in PRIVACY_CLASS:
            reporter.error(f"{service_id} has invalid privacy_classification")
        validate_provenance(str(service_id), record.get("provenance"), reporter)

        ai_applicable = bool(record.get("ai_act_applicable"))
        offering_rows = record.get("offering_attributes")
        if not isinstance(offering_rows, list):
            reporter.error(f"{service_id} offering_attributes must be a list")
            continue
        seen_offerings: set[str] = set()
        known_offerings = offerings_by_service.get(service_id, set())
        for row in offering_rows:
            if not isinstance(row, dict):
                reporter.error(f"{service_id} offering_attributes row must be a mapping")
                continue
            offering_id = row.get("offering_id")
            if offering_id not in known_offerings:
                reporter.error(
                    f"{service_id} offering_attributes references unknown offering {offering_id!r}"
                )
            if offering_id in seen_offerings:
                reporter.error(f"duplicate offering_attributes for {offering_id}")
            seen_offerings.add(offering_id)
            extra_copies = sorted(REMOVED_CANONICAL_COPIES.intersection(row))
            if extra_copies:
                reporter.error(
                    f"{offering_id} offering_attributes uses removed duplicate fields {extra_copies}; "
                    "use the canonical OSM field (OSM-M-008)"
                )

            extra_ai = AI_ACT_OFFERING_FIELDS.intersection(row)
            if extra_ai and not ai_applicable:
                reporter.error(
                    f"{offering_id} has AI Act fields but service ai_act_applicable is not true"
                )

            if "chargeback_model" in row and row["chargeback_model"] not in CHARGEBACK:
                reporter.error(f"{offering_id} has invalid chargeback_model")
            coverage = row.get("automation_coverage", None)
            if coverage is not None and coverage not in AUTOMATION:
                reporter.error(f"{offering_id} has invalid automation_coverage")
            provisioning = row.get("provisioning_automation", None)
            if provisioning is not None and provisioning not in AUTOMATION:
                reporter.error(f"{offering_id} has invalid provisioning_automation")
            if "self_service" in row and row["self_service"] not in {True, False, None}:
                reporter.error(f"{offering_id} has invalid self_service")
            unit_cost = row.get("unit_cost", None)
            if unit_cost is not None and not (
                isinstance(unit_cost, (int, float)) and not isinstance(unit_cost, bool) and unit_cost >= 0
            ):
                reporter.error(f"{offering_id} has invalid unit_cost")
            if row.get("last_resilience_test") is not None and parse_iso_date(
                row.get("last_resilience_test")
            ) is None:
                reporter.error(f"{offering_id} has invalid last_resilience_test")
            if "resilience_tested" in row and row["resilience_tested"] not in {True, False, None}:
                reporter.error(f"{offering_id} has invalid resilience_tested")
            validate_provenance(str(offering_id), row.get("provenance"), reporter)
            asset = row.get("asset_coverage", None)
            if asset is not None and asset not in ASSET_COVERAGE:
                reporter.error(f"{offering_id} has invalid asset_coverage")
            if "iso27701_pii_role" in row and row["iso27701_pii_role"] not in PII_ROLE:
                reporter.error(f"{offering_id} has invalid iso27701_pii_role")
            for category in row.get("iso27701_pii_categories") or []:
                if category not in PII_CATEGORY:
                    reporter.error(f"{offering_id} has invalid iso27701_pii_category {category!r}")
            for function in row.get("nist_functions") or []:
                if function not in NIST:
                    reporter.error(f"{offering_id} has invalid nist function {function!r}")
            status = row.get("nist_control_status", None)
            if status is not None and status not in NIST_STATUS:
                reporter.error(f"{offering_id} has invalid nist_control_status")
            if "gdpr_erasure_capable" in row and row["gdpr_erasure_capable"] not in ERASURE:
                reporter.error(f"{offering_id} has invalid gdpr_erasure_capable")

    return reporter.errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate an Open Services Data Model catalog")
    parser.add_argument(
        "--catalog",
        default=str(Path(__file__).resolve().parents[1] / "examples"),
        help="Directory containing catalog YAML files (default: examples/)",
    )
    args = parser.parse_args(argv)
    catalog_dir = Path(args.catalog)
    errors = validate_catalog(catalog_dir)
    if errors:
        sys.stderr.write(f"{len(errors)} validation error(s) in {catalog_dir}:\n")
        for message in errors:
            sys.stderr.write(f"  - {message}\n")
        return 1
    sys.stdout.write(f"OK: {catalog_dir} is valid\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
