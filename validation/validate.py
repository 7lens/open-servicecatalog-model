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
CLOUD = {"aws", "azure", "gcp", "on-prem"}
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


def parent_service_id(offering_id: str) -> str:
    return ".".join(offering_id.split(".")[:2])


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
        for field in ("name", "description", "accountable", "technology_stack"):
            if not service.get(field):
                reporter.error(f"service {service_id!r} is missing {field}")
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
        if provider.get("criticality") not in CRITICALITY:
            reporter.error(f"provider {provider_id!r} has invalid criticality")
        if provider.get("substitutability") not in SUBSTITUTABILITY:
            reporter.error(f"provider {provider_id!r} has invalid substitutability")
        for consumed in provider.get("services_consumed") or []:
            if consumed not in service_ids:
                reporter.error(
                    f"provider {provider_id!r} services_consumed references unknown service {consumed}"
                )

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
        if record.get("lifecycle_state") not in LIFECYCLE:
            reporter.error(f"{service_id} has invalid lifecycle_state")
        score = record.get("tech_debt_score", None)
        if score is not None and not (isinstance(score, int) and 0 <= score <= 100):
            reporter.error(f"{service_id} has invalid tech_debt_score")
        if "dora_criticality" in record and record["dora_criticality"] not in CRITICALITY:
            reporter.error(f"{service_id} has invalid dora_criticality")
        if "data_classification" in record and record["data_classification"] not in CLASSIFICATION:
            reporter.error(f"{service_id} has invalid data_classification")
        if "vendor_support_status" in record and record["vendor_support_status"] not in VENDOR_SUPPORT:
            reporter.error(f"{service_id} has invalid vendor_support_status")
        if "ai_act_risk_class" in record and record["ai_act_risk_class"] not in AI_RISK:
            reporter.error(f"{service_id} has invalid ai_act_risk_class")

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

            extra_ai = AI_ACT_OFFERING_FIELDS.intersection(row)
            if extra_ai and not ai_applicable:
                reporter.error(
                    f"{offering_id} has AI Act fields but service ai_act_applicable is not true"
                )

            for cloud in row.get("cloud_providers") or []:
                if cloud not in CLOUD:
                    reporter.error(f"{offering_id} has invalid cloud provider {cloud!r}")
            if "chargeback_model" in row and row["chargeback_model"] not in CHARGEBACK:
                reporter.error(f"{offering_id} has invalid chargeback_model")
            coverage = row.get("automation_coverage", None)
            if coverage is not None and coverage not in AUTOMATION:
                reporter.error(f"{offering_id} has invalid automation_coverage")
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
            for dep in row.get("dora_third_party_deps") or []:
                if dep not in provider_ids:
                    reporter.error(
                        f"{offering_id} dora_third_party_deps references unknown provider {dep}"
                    )

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
