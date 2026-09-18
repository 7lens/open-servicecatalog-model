"""Semantic OSM lint. Complements structural validation/validate.py."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable

from tools.osm_common.loader import CatalogLoadError, load_catalog
from tools.osm_common.models import (
    Catalog,
    Characteristic,
    Location,
    Offering,
    Provenance,
    Service,
    ServicePosture,
)
from tools.osm_common.semantics import (
    CLOUD_AUTHORIZATION_TOKENS,
    ITSM_OFFERING_TOKENS,
    NON_INTRINSIC_SERVICE_SLUGS,
    PRODUCT_SERVICE_TOKENS,
    PROVIDER_DUPLICATE_CHAR_NAMES,
    PROVIDER_VALUE_ALIASES,
    VENDOR_SLA_CHAR_NAMES,
    VENDOR_STACK_TOKENS,
    WORKFORCE_IDP_TOKENS,
    normalised_name,
    tokenize,
)


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    path: str
    line: int
    entity_id: str
    message: str
    advice: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def format_text(self) -> str:
        header = (
            f"{self.severity} {self.rule_id}  {self.path}:{self.line}  {self.entity_id}"
        )
        return f"{header}\n  {self.message}\n  Advice: {self.advice}"


def _loc(entity_location: Location | None, fallback: Path) -> tuple[str, int]:
    if entity_location is None:
        return (str(fallback), 1)
    return (str(entity_location.path), entity_location.line)


def _haystack(*parts: str | None) -> str:
    chunks = [normalised_name(part) for part in parts if part]
    return "-" + "-".join(chunks) + "-"


def _contains_token(haystack: str, token: str) -> bool:
    needle = f"-{normalised_name(token)}-"
    return needle in haystack


def _product_hits(service: Service) -> list[str]:
    hits: list[str] = []
    segments = service.id.split(".")
    slug_tokens: list[str] = []
    if len(segments) >= 2:
        slug_tokens.extend(tokenize(segments[1]))
    slug_tokens.extend(tokenize(service.name))
    seen: set[str] = set()
    for token in slug_tokens:
        if token in PRODUCT_SERVICE_TOKENS and token not in seen:
            seen.add(token)
            hits.append(token)
    return hits


def _itsm_hits(offering: Offering) -> list[str]:
    # Slugs only. Names like "VM provisioning and lifecycle" are valid variant labels.
    third = offering.id.split(".")[-1] if offering.id else ""
    haystack = _haystack(offering.id, third)
    return [token for token in ITSM_OFFERING_TOKENS if _contains_token(haystack, token)]


def _identity_bucket(offering: Offering) -> set[str]:
    haystack = _haystack(offering.id, offering.name)
    buckets: set[str] = set()
    if any(_contains_token(haystack, token) for token in CLOUD_AUTHORIZATION_TOKENS):
        buckets.add("cloud-authorization")
    if any(_contains_token(haystack, token) for token in WORKFORCE_IDP_TOKENS):
        buckets.add("workforce-idp")
    return buckets


def _char_provider_overlap(
    characteristics: Iterable[Characteristic],
    provider_ids: list[str],
) -> list[tuple[Characteristic, str]]:
    known = set(provider_ids)
    aliases = {alias: canonical for alias, canonical in PROVIDER_VALUE_ALIASES.items()}
    hits: list[tuple[Characteristic, str]] = []
    for char in characteristics:
        if char.name not in PROVIDER_DUPLICATE_CHAR_NAMES:
            continue
        if char.value is None:
            continue
        raw = normalised_name(str(char.value))
        canonical = aliases.get(raw, raw)
        if canonical in known or raw in known:
            hits.append((char, str(char.value)))
    return hits


def _vendor_sla_values(service: Service) -> list[str]:
    values: list[str] = []
    for char in service.characteristics:
        if char.name in VENDOR_SLA_CHAR_NAMES and char.value not in (None, ""):
            values.append(str(char.value).strip())
    for offering in service.offerings:
        for char in offering.characteristics:
            if char.name in VENDOR_SLA_CHAR_NAMES and char.value not in (None, ""):
                values.append(str(char.value).strip())
    return values


def _effective_provenance(
    posture: ServicePosture,
    offering_provenance: Provenance | None,
) -> Provenance | None:
    if offering_provenance is not None:
        return offering_provenance
    return posture.provenance


def _rule_10_1(catalog: Catalog) -> list[Finding]:
    findings: list[Finding] = []
    fallback = catalog.files["services"]
    for service in catalog.services:
        for token in _product_hits(service):
            capability, product = PRODUCT_SERVICE_TOKENS[token]
            path, line = _loc(service.location, fallback)
            findings.append(
                Finding(
                    rule_id="OSM-LINT-10.1",
                    severity="error",
                    path=path,
                    line=line,
                    entity_id=service.id,
                    message=(
                        f"Product token {token!r} used as a Service "
                        f"(id {service.id!r}, name {service.name!r})."
                    ),
                    advice=(
                        f"Name the technological capability {capability} and move "
                        f"{product} to an Offering."
                    ),
                )
            )
    return findings


def _rule_10_2(catalog: Catalog) -> list[Finding]:
    findings: list[Finding] = []
    fallback = catalog.files["services"]
    for service in catalog.services:
        for offering in service.offerings:
            hits = _itsm_hits(offering)
            if not hits:
                continue
            path, line = _loc(offering.location, fallback)
            findings.append(
                Finding(
                    rule_id="OSM-LINT-10.2",
                    severity="error",
                    path=path,
                    line=line,
                    entity_id=offering.id,
                    message=(
                        f"Offering looks like an ITSM/request-catalog item "
                        f"(tokens: {', '.join(hits)})."
                    ),
                    advice=(
                        "Offerings are technological variants (provider, operating "
                        "model, packaging). Request types such as MFA or password "
                        "reset stay in ITSM."
                    ),
                )
            )
    return findings


def _rule_10_3(catalog: Catalog) -> list[Finding]:
    findings: list[Finding] = []
    fallback = catalog.files["services"]
    for service in catalog.services:
        buckets: set[str] = set()
        for offering in service.offerings:
            buckets.update(_identity_bucket(offering))
        if buckets != {"cloud-authorization", "workforce-idp"}:
            continue
        path, line = _loc(service.location, fallback)
        findings.append(
            Finding(
                rule_id="OSM-LINT-10.3",
                severity="error",
                path=path,
                line=line,
                entity_id=service.id,
                message=(
                    "Service mixes cloud resource authorization (e.g. AWS IAM) "
                    "and workforce IdP (e.g. Entra / Okta) on one Service."
                ),
                advice=(
                    "Split into distinct Services (e.g. identity.cloud-authorization "
                    "and identity.directory-idp). Unifying them produces false "
                    "substitutability."
                ),
            )
        )
    return findings


def _rule_10_4(catalog: Catalog) -> list[Finding]:
    findings: list[Finding] = []
    fallback = catalog.files["stacks"]
    for stack in catalog.stacks:
        tokens = set(tokenize(stack.id)) | {normalised_name(stack.id), normalised_name(stack.name)}
        hit = sorted(token for token in tokens if token in VENDOR_STACK_TOKENS)
        if not hit:
            continue
        path, line = _loc(stack.location, fallback)
        findings.append(
            Finding(
                rule_id="OSM-LINT-10.4",
                severity="error",
                path=path,
                line=line,
                entity_id=stack.id,
                message=(
                    f"Technology Stack {stack.id!r} / {stack.name!r} is a vendor "
                    f"tower (tokens: {', '.join(hit)})."
                ),
                advice=(
                    "Stacks are operational competency domains of the adopting "
                    "organisation (Compute, Identity, Data), not AWS / Azure / M365."
                ),
            )
        )
    return findings


def _rule_10_7(catalog: Catalog) -> list[Finding]:
    findings: list[Finding] = []
    fallback = catalog.files["services"]
    for service in catalog.services:
        for char, value in _char_provider_overlap(service.characteristics, service.providers):
            path, line = _loc(char.location or service.location, fallback)
            findings.append(
                Finding(
                    rule_id="OSM-LINT-10.7",
                    severity="warning",
                    path=path,
                    line=line,
                    entity_id=service.id,
                    message=(
                        f"Characteristic {char.name}={value!r} duplicates Service "
                        f"providers {service.providers}."
                    ),
                    advice="Use providers[] as the seller dimension; do not restated it as a characteristic.",
                )
            )
        for offering in service.offerings:
            providers = catalog.offering_providers(service, offering)
            for char, value in _char_provider_overlap(offering.characteristics, providers):
                path, line = _loc(char.location or offering.location, fallback)
                findings.append(
                    Finding(
                        rule_id="OSM-LINT-10.7",
                        severity="warning",
                        path=path,
                        line=line,
                        entity_id=offering.id,
                        message=(
                            f"Characteristic {char.name}={value!r} duplicates "
                            f"providers {providers}."
                        ),
                        advice=(
                            "Use providers[] as the cloud/seller dimension. "
                            "Characteristics hold other variant facts (engine, OS, hours)."
                        ),
                    )
                )
    return findings


def _rule_10_8(catalog: Catalog) -> list[Finding]:
    findings: list[Finding] = []
    fallback = catalog.files["services"]
    for service in catalog.services:
        if not service.providers:
            continue
        offering_providers: set[str] = set()
        for offering in service.offerings:
            offering_providers.update(offering.providers)
        distinguishes_by_provider = len(offering_providers) > 1
        non_intrinsic = service.slug in NON_INTRINSIC_SERVICE_SLUGS
        if not distinguishes_by_provider and not non_intrinsic:
            continue
        path, line = _loc(service.location, fallback)
        if non_intrinsic:
            reason = (
                f"capability {service.slug!r} is not intrinsically bound to one seller"
            )
        else:
            reason = "offerings already distinguish sellers"
        findings.append(
            Finding(
                rule_id="OSM-LINT-10.8",
                severity="warning",
                path=path,
                line=line,
                entity_id=service.id,
                message=(
                    f"Service-level providers {service.providers} look misplaced "
                    f"({reason})."
                ),
                advice=(
                    "Use Service-level providers only when the seller is intrinsic "
                    "to the capability. Put distinguishing sellers on Offerings."
                ),
            )
        )
    return findings


def _rule_10_10(catalog: Catalog) -> list[Finding]:
    findings: list[Finding] = []
    fallback = catalog.files.get("posture") or catalog.root / "posture" / "service-posture.yaml"
    services = catalog.service_by_id()
    for posture in catalog.posture:
        target = posture.availability_target
        if target in (None, ""):
            continue
        service = services.get(posture.service_id)
        if service is None:
            continue
        target_s = str(target).strip()
        slas = _vendor_sla_values(service)
        exact = [sla for sla in slas if sla == target_s]
        evidenced = (
            posture.provenance is not None and posture.provenance.has_high_confidence_evidence()
        )
        if exact:
            path, line = _loc(posture.location, fallback)
            findings.append(
                Finding(
                    rule_id="OSM-LINT-10.10",
                    severity="error",
                    path=path,
                    line=line,
                    entity_id=posture.service_id,
                    message=(
                        f"availability_target {target_s!r} equals a "
                        "vendor_availability_sla characteristic."
                    ),
                    advice=(
                        "Vendor SLA belongs on a characteristic. availability_target "
                        "is the enterprise expectation and must not copy the vendor string."
                    ),
                )
            )
            continue
        if slas and not evidenced:
            path, line = _loc(posture.location, fallback)
            findings.append(
                Finding(
                    rule_id="OSM-LINT-10.10",
                    severity="warning",
                    path=path,
                    line=line,
                    entity_id=posture.service_id,
                    message=(
                        f"availability_target {target_s!r} is set alongside vendor "
                        "SLA characteristics without high-confidence enterprise provenance."
                    ),
                    advice=(
                        "Record the enterprise target with provenance "
                        "(confidence: high and evidence_reference). Do not copy a vendor SLA."
                    ),
                )
            )
    return findings


def _rule_10_12(catalog: Catalog) -> list[Finding]:
    findings: list[Finding] = []
    providers_file = catalog.files["providers"]
    for provider in catalog.providers:
        if provider.gdpr_dpa_signed is not True:
            continue
        path, line = _loc(provider.location, providers_file)
        findings.append(
            Finding(
                rule_id="OSM-LINT-10.12",
                severity="error",
                path=path,
                line=line,
                entity_id=provider.id,
                message=(
                    "gdpr_dpa_signed is true. ICT Provider has no provenance field, "
                    "so this cannot carry high-confidence evidence in OSM 1.3.0."
                ),
                advice=(
                    "Set gdpr_dpa_signed only when this customer executed the DPA. "
                    "Vendor-published DPAs are not that fact. Leave null if unevidenced."
                ),
            )
        )

    posture_file = catalog.files.get("posture") or catalog.root / "posture" / "service-posture.yaml"
    for posture in catalog.posture:
        if posture.raw.get("gdpr_dpa_signed") is True:
            path, line = _loc(posture.location, posture_file)
            findings.append(
                Finding(
                    rule_id="OSM-LINT-10.12",
                    severity="error",
                    path=path,
                    line=line,
                    entity_id=posture.service_id,
                    message="gdpr_dpa_signed: true on posture without OSM provider evidence.",
                    advice="gdpr_dpa_signed lives on ICT Provider and requires customer execution evidence.",
                )
            )
        for row in posture.offering_posture:
            if row.nist_control_status != "implemented":
                continue
            provenance = _effective_provenance(posture, row.provenance)
            if provenance is not None and provenance.has_high_confidence_evidence():
                continue
            path, line = _loc(row.location or posture.location, posture_file)
            findings.append(
                Finding(
                    rule_id="OSM-LINT-10.12",
                    severity="error",
                    path=path,
                    line=line,
                    entity_id=row.offering_id or posture.service_id,
                    message=(
                        "nist_control_status is implemented without high-confidence "
                        "provenance and evidence_reference."
                    ),
                    advice=(
                        "This is an OSM assessment signal, not a NIST CSF object. "
                        "Leave it unset unless the estate assessed it and recorded evidence. "
                        "Do not copy vendor marketing."
                    ),
                )
            )
    return findings


RULES = (
    _rule_10_1,
    _rule_10_2,
    _rule_10_3,
    _rule_10_4,
    _rule_10_7,
    _rule_10_8,
    _rule_10_10,
    _rule_10_12,
)


def lint_catalog(catalog: Catalog) -> list[Finding]:
    findings: list[Finding] = []
    for rule in RULES:
        findings.extend(rule(catalog))
    findings.sort(key=lambda item: (item.path, item.line, item.rule_id, item.entity_id, item.message))
    return findings


def lint_path(root: str | Path) -> tuple[Catalog, list[Finding]]:
    catalog = load_catalog(root)
    return catalog, lint_catalog(catalog)


def exit_code(findings: Iterable[Finding]) -> int:
    items = list(findings)
    if any(item.severity == "error" for item in items):
        return 1
    if any(item.severity == "warning" for item in items):
        return 2
    return 0


__all__ = [
    "CatalogLoadError",
    "Finding",
    "exit_code",
    "lint_catalog",
    "lint_path",
]
