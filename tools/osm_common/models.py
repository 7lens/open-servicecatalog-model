"""Read-only Python representation of a loaded OSM 1.3.0 catalog."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Location:
    path: Path
    line: int

    def __str__(self) -> str:
        return f"{self.path}:{self.line}"


@dataclass
class Characteristic:
    name: str
    value_type: str | None
    value: Any
    location: Location | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)


@dataclass
class Provenance:
    authoritative_source: str | None = None
    source_system: str | None = None
    source_record_id: str | None = None
    last_verified: str | None = None
    evidence_reference: str | None = None
    confidence: str | None = None
    discovery_method: str | None = None
    location: Location | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)

    def has_high_confidence_evidence(self) -> bool:
        evidence = (self.evidence_reference or "").strip()
        return self.confidence == "high" and bool(evidence)


@dataclass
class Stack:
    id: str
    name: str
    description: str | None = None
    mappings: dict[str, Any] = field(default_factory=dict)
    location: Location | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)


@dataclass
class Offering:
    id: str
    name: str
    description: str | None = None
    providers: list[str] = field(default_factory=list)
    characteristics: list[Characteristic] = field(default_factory=list)
    provenance: Provenance | None = None
    location: Location | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)


@dataclass
class Service:
    id: str
    name: str
    description: str | None = None
    accountable: str | None = None
    technology_stack: str | None = None
    version: str | None = None
    valid_from: str | None = None
    valid_to: str | None = None
    lifecycle_state: str | None = None
    providers: list[str] = field(default_factory=list)
    characteristics: list[Characteristic] = field(default_factory=list)
    offerings: list[Offering] = field(default_factory=list)
    provenance: Provenance | None = None
    location: Location | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)

    @property
    def slug(self) -> str:
        parts = self.id.split(".")
        return parts[-1] if parts else self.id


@dataclass
class Provider:
    id: str
    name: str
    type: str | None = None
    substitutability: str | None = None
    gdpr_dpa_signed: Any = None
    dora_notification_clause: Any = None
    certifications: list[str] = field(default_factory=list)
    risk_level: str | None = None
    location: Location | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)


@dataclass
class OfferingPosture:
    offering_id: str
    rto: Any = None
    rpo: Any = None
    resilience_tested: Any = None
    last_resilience_test: Any = None
    resilience_evidence: Any = None
    cost_pool: Any = None
    chargeback_model: Any = None
    unit_cost: Any = None
    automation_coverage: Any = None
    provisioning_automation: Any = None
    self_service: Any = None
    manual_hours_week: Any = None
    last_security_review: Any = None
    asset_coverage: Any = None
    iso27001_controls: list[Any] = field(default_factory=list)
    iso27701_pii_role: Any = None
    nist_functions: list[Any] = field(default_factory=list)
    nist_control_status: Any = None
    gdpr_processing_activity: Any = None
    provenance: Provenance | None = None
    location: Location | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)


@dataclass
class ServicePosture:
    service_id: str
    operational_criticality: str | None = None
    resilience_tier: str | None = None
    availability_target: Any = None
    response_target: Any = None
    resolution_target: Any = None
    data_classification: str | None = None
    security_classification: str | None = None
    privacy_classification: str | None = None
    tech_debt_score: Any = None
    vendor_support_status: str | None = None
    financial_owner: str | None = None
    ai_act_applicable: Any = None
    ai_act_risk_class: str | None = None
    offering_posture: list[OfferingPosture] = field(default_factory=list)
    provenance: Provenance | None = None
    location: Location | None = None
    raw: dict[str, Any] = field(default_factory=dict, repr=False)


@dataclass
class Catalog:
    root: Path
    stacks: list[Stack] = field(default_factory=list)
    services: list[Service] = field(default_factory=list)
    providers: list[Provider] = field(default_factory=list)
    posture: list[ServicePosture] = field(default_factory=list)
    files: dict[str, Path] = field(default_factory=dict)

    def stack_by_id(self) -> dict[str, Stack]:
        return {stack.id: stack for stack in self.stacks}

    def stack_by_name(self) -> dict[str, Stack]:
        return {stack.name: stack for stack in self.stacks}

    def service_by_id(self) -> dict[str, Service]:
        return {service.id: service for service in self.services}

    def offering_by_id(self) -> dict[str, Offering]:
        found: dict[str, Offering] = {}
        for service in self.services:
            for offering in service.offerings:
                found[offering.id] = offering
        return found

    def provider_by_id(self) -> dict[str, Provider]:
        return {provider.id: provider for provider in self.providers}

    def posture_by_service_id(self) -> dict[str, ServicePosture]:
        return {row.service_id: row for row in self.posture}

    def offering_providers(self, service: Service, offering: Offering) -> list[str]:
        """Legal sellers that underpin an offering (offering list, else service list)."""
        if offering.providers:
            return list(offering.providers)
        return list(service.providers)
