# 7lens Open Services Data Model — Specification

Version: 1.0.0

This is the normative specification of the **7lens Open Services Data
Model**: a small, opinionated way to describe *what* a technology
organization delivers as technological services, who runs them, how
healthy they are, and which third parties they depend on.

The specification is vendor-neutral and framework-neutral. Nothing
here requires a particular product, cloud, or methodology.

**Service** always means a **technological service**.

---

## 1. Scope and philosophy

The model answers one question:

> What technological services does the technology organization
> deliver, and in what operational state?

It is deliberately a catalog of technological capabilities. It does
not model:

- business capabilities or business services
- applications
- CMDB configuration items or running-system inventory
- organizational hierarchy
- geographic or legal-entity hierarchy
- enterprise-wide ontology
- stakeholder lenses
- enterprise decision intelligence

Consumers of a technological service are outside the scope of this
model.

### Design principles

1. **Catalog vs. health record.** The catalog of services is stable.
   Operational state changes constantly. Keep them in separate files
   with separate owners and cadences.
2. **Two tiers, no deeper.** A service has service offerings. That is
   the only nesting. Offerings are the atomic requestable unit.
3. **Immutable IDs.** An ID never changes once assigned, even if
   ownership moves.
4. **Every service has exactly one operational owner** (a technology
   stack).
5. **Framework mappings, not framework lock-in.** Optional mappings
   to TBM, TOGAF, ISO, NIST, GDPR, DORA and the EU AI Act let
   different readers translate the catalog. The model is not an
   implementation of those frameworks.

---

## 2. Files and how they relate

| File | Concept | Nature | Typical owner |
|------|---------|--------|---------------|
| `examples/technology-stacks.yaml` | Operational competency domains | Stable | Platform leadership |
| `examples/services.yaml` | The catalog (services → offerings) | Stable | Stack + Service Owners |
| `examples/service-attributes.yaml` | Operational and compliance state | Dynamic | Multiple teams |
| `examples/ict-providers.yaml` | Third-party provider register | Semi-dynamic | Vendor management / risk |

```
technology-stacks.yaml
        │  1 stack : many services
        v
services.yaml                 ← the catalog
        │
        │ service_id
        v
service-attributes.yaml  ───► ict-providers.yaml
```

JSON Schema for each entity is in `schema/`.

---

## 3. Identifiers

IDs use dot-separated segments:

```
{stack_prefix}.{service_slug}.{offering_slug}
```

- **Service ID** = 2 segments, e.g. `compute.kubernetes`
- **Offering ID** = 3 segments, e.g. `compute.kubernetes.shared-cluster`
- Each segment is a lowercase, hyphen-delimited slug matching
  `^[a-z0-9]+(?:-[a-z0-9]+)*$`

**Prefixes are stable; stack assignment is mutable.** The prefix
records the stack a service was originally created under. A service
may later be reassigned to a different `technology_stack` without
changing its ID. Therefore the prefix does not always equal the
current stack.

Do not invent additional identity schemes.

---

## 4. Technology Stack

A **technology stack** is an operational competency domain that runs
a group of services day to day. It is not a financial taxonomy.

Adopting organizations typically define 8–20 stacks. The examples
in this repository are a starter set.

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | Short stable identifier (also used as the default service prefix). |
| `name` | yes | Human-readable stack name. |
| `description` | yes | Plain-language description of the stack's scope. |
| `mappings` | no | Optional reference mappings (see below). |

### `mappings` sub-fields (all optional)

| Mapping | Purpose |
|---------|---------|
| `tbm_tower` | TBM IT Tower (L1) — finance cost allocation |
| `tbm_sub_tower` | TBM Sub-Tower (L2) |
| `togaf_domain` | TOGAF architecture domain |
| `iso27001` | Free-text ISO/IEC 27001:2022 Annex A control references |
| `iso27701` | Free-text ISO/IEC 27701 references, or `not-applicable` |
| `nist_csf` | List of NIST CSF 2.0 functions: `govern`, `identify`, `protect`, `detect`, `respond`, `recover` |
| `gdpr` | Free-text GDPR article references, or `not-applicable` |
| `dora` | `pillar` and `criticality` (see enums below) |
| `ai_act` | `contains_ai_systems`, `max_risk_class`, optional `reference` |

DORA `pillar` ∈ {`ICT Risk Management`, `ICT-related Incident Management`, `Digital Operational Resilience Testing`, `ICT Third-Party Risk Management`}

DORA `criticality` ∈ {`critical`, `important`, `standard`}

EU AI Act `max_risk_class` ∈ {`unacceptable`, `high-risk`, `limited-risk`, `minimal-risk`, `not-applicable`}

These mappings are **optional reference mappings**. They are not a
claim of compliance, certification, or legal interpretation.

---

## 5. Service

### Service fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | 2-segment service ID. Immutable. |
| `name` | yes | Capability name. |
| `description` | yes | Plain-language capability description. |
| `accountable` | yes | The Service Owner (role name, team, or named individual). |
| `technology_stack` | yes | The `name` of the owning stack. Exactly one. |
| `service_offerings` | yes | List of offerings. |

### Offering fields

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | 3-segment offering ID. Immutable. |
| `name` | yes | What a consumer can request. |
| `description` | no | Optional clarification of the variant. |

An **offering** is the atomic requestable unit. A service that offers
the same capability across clouds typically has one offering per
cloud or operating model.

---

## 6. Service attributes

Organized **by service**. Each block has service-level posture fields
plus a list of `offering_attributes`. Service-level fields are not
duplicated per offering — an offering inherits them from its parent.

An empty `offering_attributes: []` is a valid state.

### Service-level fields

| Field | Values |
|-------|--------|
| `service_id` | Must exist in the services catalog. |
| `lifecycle_state` | `draft` \| `pilot` \| `production` \| `sunset` \| `retired` |
| `tech_debt_score` | `0`–`100`, or `null` if not assessed. |
| `dora_criticality` | `critical` \| `important` \| `standard` |
| `data_classification` | `public` \| `internal` \| `confidential` \| `restricted` |
| `vendor_support_status` | `active` \| `extended` \| `end-of-life` |
| `ai_act_applicable` | `true` \| `false` |
| `ai_act_risk_class` | `unacceptable` \| `high-risk` \| `limited-risk` \| `minimal-risk` \| `not-applicable` |

`dora_criticality` and `ai_act_*` are named for the frameworks they
optionally map to. Using them does not constitute a DORA or AI Act
assessment.

### Offering-level fields

**Finance**

| Field | Values |
|-------|--------|
| `cloud_providers` | list of `aws`, `azure`, `gcp`, `on-prem` |
| `cost_pool` | free-text cost pool, or `null` |
| `chargeback_model` | `shared` \| `dedicated` \| `consumption` |

**Operations**

| Field | Values |
|-------|--------|
| `automation_coverage` | `none` \| `partial` \| `full` \| `null` |
| `manual_hours_week` | number, or `null` |

**Security operations**

| Field | Values |
|-------|--------|
| `last_security_review` | ISO 8601 date, or `null` |
| `asset_coverage` | `complete` \| `partial` \| `unknown` \| `null` |

**ISO 27001 / 27701 (reference mappings)**

| Field | Values |
|-------|--------|
| `iso27001_controls` | list of Annex A control IDs |
| `iso27701_pii_role` | `controller` \| `processor` \| `joint-controller` \| `none` |
| `iso27701_pii_categories` | list of `identity`, `financial`, `health`, `behavioral`, `location`, `biometric`, `communications`, `none` |
| `iso27701_retention_days` | number, or `null` |

**NIST CSF 2.0 (reference mappings)**

| Field | Values |
|-------|--------|
| `nist_functions` | list of `govern`, `identify`, `protect`, `detect`, `respond`, `recover` |
| `nist_control_status` | `implemented` \| `partially-implemented` \| `planned` \| `not-applicable` \| `null` |

**GDPR (reference mappings)**

| Field | Values |
|-------|--------|
| `gdpr_processing_activity` | `true` \| `false` |
| `gdpr_dpia_required` | `true` \| `false` |
| `gdpr_erasure_capable` | `true` \| `false` \| `partial` \| `not-applicable` |

**Operational resilience**

| Field | Values |
|-------|--------|
| `dora_rto` | ISO 8601 duration (e.g. `PT8H`), or `null` |
| `dora_rpo` | ISO 8601 duration (e.g. `PT1H`), or `null` |
| `dora_third_party_deps` | list of provider IDs from the ICT provider file |
| `dora_resilience_tested` | `true` \| `false` \| `null` |

**EU AI Act (present only when `ai_act_applicable: true`)**

| Field | Values |
|-------|--------|
| `ai_act_intended_purpose` | free text |
| `ai_act_human_oversight` | `human-in-the-loop` \| `human-on-the-loop` \| `human-in-command` \| `none` |
| `ai_act_transparency_level` | `explicit-disclosure` \| `implicit-disclosure` \| `none` |
| `ai_act_conformity_assessment` | ISO 8601 date, or `null` |
| `ai_act_training_data_doc` | `true` \| `false` \| `not-applicable` |

Illustrative values in examples are **not legal advice** and are
**not evidence of certification or regulatory compliance**.

---

## 7. ICT providers

A register of third-party technology providers. Fields support
vendor-risk conversations; they do not by themselves satisfy any
regulatory filing.

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | Short identifier referenced by offerings |
| `name` | yes | Provider name |
| `type` | yes | `cloud-infrastructure` \| `cloud-platform` \| `managed-service` \| `software-vendor` \| `network-provider` \| `data-center` |
| `headquarters` | no | ISO 3166-1 alpha-2 country code |
| `data_processing_locations` | no | Countries or regions as a list |
| `criticality` | yes | `critical` \| `important` \| `standard` |
| `substitutability` | yes | `low` \| `medium` \| `high` |
| `contract_ref` | no | Local contract reference, or `null` |
| `contract_start` | no | ISO 8601 date, or `null` |
| `contract_end` | no | ISO 8601 date, or `null` |
| `notice_period_days` | no | number, or `null` |
| `audit_rights` | no | `true` \| `false` \| `null` |
| `subcontracting_allowed` | no | `true` \| `false` \| `conditional` \| `null` |
| `subcontractors` | no | list of names |
| `last_risk_assessment` | no | ISO 8601 date, or `null` |
| `risk_level` | no | `low` \| `medium` \| `high` \| `critical` \| `null` |
| `exit_strategy_documented` | no | `true` \| `false` \| `null` |
| `exit_strategy_tested` | no | `true` \| `false` \| `null` |
| `concentration_risk` | no | `true` \| `false` \| `null` |
| `certifications` | no | free-form list (e.g. `iso27001`, `soc2-type2`) |
| `gdpr_dpa_signed` | no | `true` \| `false` \| `null` |
| `dora_notification_clause` | no | `true` \| `false` \| `null` |
| `services_consumed` | no | Service IDs from the services catalog |

Do not publish a real vendor register as an example.

---

## 8. Governance roles

See [`GOVERNANCE.md`](GOVERNANCE.md).

- **Technology Stack Owner** — accountable for stack completeness
  and that every service has a Service Owner.
- **Service Owner** — accountable for a technological service, its
  lifecycle, and applicable security and operational obligations.

---

## 9. Validation rules

An implementation should enforce:

1. Every `service.technology_stack` matches a `technology_stacks[].name`.
2. Every `service.id` is unique and has exactly 2 segments.
3. Every `offering.id` is unique, has 3 segments, and its first 2
   segments equal its parent `service.id`.
4. Every `service_attributes[].service_id` exists in the services catalog.
5. Every `offering_attributes[].offering_id` exists under its parent
   service in the services catalog.
6. Every provider ID in `dora_third_party_deps` exists in the ICT
   provider file.
7. Every service ID in `ict_providers[].services_consumed` exists in
   the services catalog.
8. EU AI Act offering fields are present only where
   `ai_act_applicable: true`.
9. Duplicate IDs are rejected for stacks, services, offerings and
   providers.

See [`validation/`](validation/) for a lightweight checker.
