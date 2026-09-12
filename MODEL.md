# Conceptual model

This document describes **7lens OSM** (7lens Open Service Catalog
Model) as a standalone conceptual structure. The normative field
definitions are in [`SPECIFICATION.md`](SPECIFICATION.md). Accepted
model decisions are indexed in [`DECISIONS.md`](DECISIONS.md) and
detailed under [`decisions/`](decisions/).

OSM-M-007 is **ACCEPTED** and implemented. The model distinguishes:

```text
SERVICE DEFINITION     what the service is
SERVICE POSTURE        how the service currently stands
PROVENANCE             why the information can be trusted
EXTERNAL CONTEXT       information owned elsewhere
```

The YAML keys `service_attributes` / `offering_attributes` are the
Service Posture and Offering Posture records. File names were kept
for compatibility; they are not a second catalog entity.

## One concept, one canonical parameter

OSM MUST NOT represent the same semantic concept through multiple
canonical parameters (OSM-M-008). Before adding a field, search
schemas, examples, this file, `SPECIFICATION.md` and existing
decisions. If the concept already exists, reuse it and map frameworks
to that field. Duplication is justified only for genuinely different
concepts or different grains — not different names.

Genuinely different concepts may coexist even when they use similar
names, the same enum values, or appear related.

Canonical examples of **one concept, reused**:

```text
rto / rpo          recovery objectives (DORA maps here)
providers          ICT Provider association (a cloud provider is still an ICT Provider)
operational_criticality   service criticality (DORA maps here)
```

Canonical examples of **different concepts that may share tokens**:

```text
data_classification vs security_classification
automation_coverage vs provisioning_automation
resilience_tier vs rto / rpo
accountable vs financial_owner
availability_target vs service_hours
```

## Purpose

The model describes **technological services**: what a technology or
platform organization delivers, who operates those deliveries, the
current operational state, and which third parties the deliveries
depend on.

It does not describe the rest of an enterprise.

## Core entities

```
┌─────────────────────┐
│  Technology Stack   │  operational competency / ownership domain
└──────────┬──────────┘
           │ 1 : many
           v
┌─────────────────────┐
│      Service        │  stable definition of a technological service
└──────────┬──────────┘
           │ 1 : many
           v
┌─────────────────────┐
│  Service Offering   │  atomic requestable / deliverable unit
└─────────────────────┘
```

Each service also has:

- an **accountable** Service Owner (service-definition
  accountability; distinct from posture `financial_owner`)
- **version**, **validity period** and **lifecycle_state**
- optional **characteristics** (generic machine-readable properties)
- optional **providers** (ICT Provider ids; OSM-M-006)
- optional **provenance** (reusable trust metadata; OSM-M-007)
- optional **service posture** (`service_attributes`)
- optional **offering posture** (`offering_attributes`)

## Technology Stack

A Technology Stack is a stable operational domain. It answers
"which competency runs this group of services?"

Stacks are not:

- cost centers (finance may *map* to them)
- org-chart boxes that must mirror HR structure
- infrastructure inventories

A service belongs to exactly one current stack. The stack on a
service may change; the service ID does not.

## Service

A Service is the **stable definition** of a technological capability
(OSM-M-003). It is not only a catalog row, not an availability
record, and not a running instance. OSM does not add a separate
ServiceSpecification entity; the Service *is* that definition.

A Service has:

- an immutable identifier (2 segments)
- a name and description
- a Service Owner
- a current Technology Stack
- a definition `version`
- a validity window (`valid_from`, optional `valid_to`)
- a `lifecycle_state`
- one or more Service Offerings
- optional characteristics
- optional `providers` (ICT Provider ids)
- optional `provenance`

**Immutable identity ≠ immutable definition** (OSM-M-002). The `id`
never changes. The definition (name, description, lifecycle, offerings,
characteristics, providers, provenance, version, validity) may change.
One catalog record exists per service `id`; that record is the current
definition.

OSM Service is the canonical **definition**. A deployed Service
Instance is outside the OSM core (OSM-C-005).

## Service Offering

A Service Offering is the canonical requestable/deliverable **variant**
of a Service. It may differ in environment, location, availability,
packaging, operating model, provider, or other meaningful
characteristics. Do not hard-code every dimension as a core field;
use Characteristics (OSM-M-001) and optional `providers` (OSM-M-006).

The offering identifier has 3 segments. The first two segments must
equal the parent service ID. Offerings belong to the parent Service
definition and do not carry a separate version or validity window.

## Characteristics

Services and Service Offerings may declare nested **characteristics**
(OSM-M-001): named, typed properties with optional value, defaults,
allowed values, cardinality, constraints and a configurable flag.

Characteristics are a reuse of one small structure, not a new catalog
entity and not a TM Forum characteristic model.

## Service posture

Posture is separated from definition on purpose (OSM-M-007).

| Layer | Holds | Changes when |
|-------|--------|--------------|
| Service / offering catalog | The **definition** of what is delivered, including `lifecycle_state` and optional `provenance` | Definition version, validity, lifecycle, offerings, characteristics or providers change. `id` does not. |
| Service posture (`service_attributes`) | Shared operational / governance state, including service-level expectations | Criticality, classification, automation, resilience and financial characterization change |
| Offering posture (`offering_attributes`) | Variant-level operations, cost, security, resilience | Day-to-day operational reality changes |

Empty offering posture lists are allowed. Populate them as evidence
becomes available.

OSM records **service-level expectations** (availability, response,
resolution **targets**) as posture. Targets describe expected
performance. Offering characteristics `service_hours` and
`support_hours` describe **when** the service or support is available.
Those are not the same concept. OSM does not manage SLAs.

Canonical offering-level recovery objectives are `rto` (Recovery Time
Objective) and `rpo` (Recovery Point Objective). Service-level
`resilience_tier` is a qualitative classification. A tier MAY be
associated with expected recovery characteristics; it is not a
replacement for explicit RTO/RPO values. There is no DORA-prefixed
copy of `rto` / `rpo`.

`data_classification` classifies the data the service handles.
`security_classification` classifies the service itself. They may
share enum tokens; they are not the same fact.

`accountable` on the Service is overall service-definition
accountability. Posture `financial_owner` is financial ownership.
They are not the same role.

`automation_coverage` is overall delivery/operation automation.
`provisioning_automation` is provisioning-process automation. Same
enum; different scope.

## Provenance

A reusable `provenance` object may attach to a Service, Offering, or
posture record. It makes an **enterprise fact** trustworthy. OSM does
not model AI interpretation or AI recommendation. Each provenance
field answers a different question (who is authoritative, which
system, which record, when verified, where evidence lives, how much
to trust, how it was discovered). They are not interchangeable.

## ICT providers

An ICT Provider is the canonical record of a third-party technology
organization. Service and Offering point at it by id:

```
Service / Offering  →  providers[]  →  ICT Provider
```

Use Service-level `providers` when the provider is intrinsic to the
capability (for example Enterprise DNS → Infoblox). Use Offering-level
`providers` when provider choice distinguishes the variant (for
example Kubernetes AWS vs Azure). Association is optional. Multiple
ids are allowed. Do not copy provider master data onto Service or
Offering. Do not maintain a parallel `cloud_providers` list; a cloud
provider is an ICT Provider (OSM-M-008).

Separate, existing fields:

- `dora_third_party_deps` on offering attributes — DORA-oriented
  third-party listing. Whether this is a genuinely different
  relationship from `providers` is unresolved (**OSM-M-005**,
  **PROPOSED**). Do not collapse the two fields yet.
- `services_consumed` on ICT Provider — reverse list of service ids
  in the vendor register

`providers` is not a generic Service → Service relationship.

Those fields are ordinary references. Using DORA-named fields does not
make a catalog a regulatory filing.

## Optional framework mappings

Stacks, services and offerings may carry mappings to TBM, TOGAF,
ISO/IEC 27001, ISO/IEC 27701, NIST CSF, GDPR, DORA and the EU AI Act.

Mappings are optional, illustrative and non-normative for those
frameworks. 7lens OSM is not an implementation of any of them.
Compatibility does not mean copying (OSM-M-004). Frameworks map to
canonical OSM fields when the concept already exists; they do not
get a second copy of the same fact (OSM-M-008).
See [`COMPATIBILITY.md`](COMPATIBILITY.md).

## What is deliberately excluded

The model stops at technological services. It does not define
business capabilities, business services, digital products,
business outcomes, value streams, applications, Application Services,
Service Instances, infrastructure configuration items, Product Models,
organization or geography, enterprise-wide ontologies, stakeholder
lenses, decision intelligence, detailed service-level / SLA objects,
or first-class Service → Service relationships.

Service → Service relationships are deliberately outside the
**current** OSM core (OSM-C-004, OSM-C-005), not a permanent rejection.

Consumers of a technological service are outside the scope of this
model.
