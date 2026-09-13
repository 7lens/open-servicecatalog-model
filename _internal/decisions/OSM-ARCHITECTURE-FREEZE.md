# 7lens Open Service Catalog Model — Architecture Freeze

- **Status:** FROZEN
- **Date:** 2026-09-12
- **Type:** Documentation / Governance
- **Register:** [`DECISIONS.md`](DECISIONS.md)
- **Normative field model:** [`SPECIFICATION.md`](../../SPECIFICATION.md)
- **Conceptual model:** [`MODEL.md`](../../MODEL.md)

This is the authoritative Architecture Freeze Record for **7lens OSM**
(7lens Open Service Catalog Model). It records the architecture as
implemented in this repository. It does not add, remove, rename or
reinterpret entities, fields, relationships or decisions.

**The current OSM architecture is frozen.** Future architectural
changes require an explicit new architectural decision before
implementation.

The current repository is the only source of truth for this record.

---

## Frozen conceptual structure

```text
Technology Stack
        │  1 : N
        v
     Service
        │  1 : N
        v
 Service Offering
```

A Technology Stack is an operational competency / ownership domain.
A Service is the stable definition of a technological service.
A Service Offering is the atomic requestable / deliverable variant
of that Service.

Supporting concepts already in the model:

| Concept | Role |
|---------|------|
| Characteristics | Nested, reusable properties on Service or Offering (OSM-M-001). Not a catalog entity. |
| Service Posture | How the service currently stands (`service_attributes`; OSM-M-007). |
| Offering Posture | Variant-level operational state (`offering_attributes`; OSM-M-007). |
| Provenance | Reusable trust metadata: why an enterprise fact can be believed (OSM-M-007). |
| ICT Provider | Canonical third-party technology provider (OSM-M-006). |
| Framework mappings | Optional, illustrative, non-normative translations (OSM-M-004, OSM-M-008). |

The YAML keys `service_attributes` / `offering_attributes` are the
Service Posture and Offering Posture records. File names were kept
for compatibility; they are not a second catalog entity.

### Semantic layers (OSM-M-007)

```text
SERVICE DEFINITION     what the service is (catalog)
SERVICE POSTURE        how it currently stands (service_attributes)
PROVENANCE             why the information can be trusted
EXTERNAL CONTEXT       owned by other systems — not modelled here
```

These layers are distinct. Posture is not a second catalog. Provenance
is not an AI interpretation or recommendation. External context is
not an OSM entity.

---

## Frozen entities

### Technology Stack

A Technology Stack is a stable operational domain. It answers "which
competency runs this group of services?" It is not a financial
taxonomy, not a cost center, not an org-chart box, and not an
infrastructure inventory. A service belongs to exactly one current
stack. The stack on a service may change; the service ID does not.

### Service

A Service is the **stable definition** of a technological capability
(OSM-M-003). It is not only a catalog row, not an availability
record, and not a running instance. OSM does not add a separate
ServiceSpecification entity; the Service *is* that definition.

A Service has an immutable 2-segment identifier, a name and
description, a Service Owner (`accountable`), a current Technology
Stack, a definition `version`, a validity window (`valid_from`,
optional `valid_to`), a `lifecycle_state`, one or more Service
Offerings, and optionally characteristics, `providers` and
`provenance`.

### Service Offering

A Service Offering is the canonical requestable/deliverable
**variant** of a Service. It may differ in environment, location,
availability, packaging, operating model, provider, or other
meaningful characteristics. Variation dimensions are not hard-coded
as core fields; use Characteristics (OSM-M-001) and optional
`providers` (OSM-M-006). Offerings belong to the parent Service
definition.

### Characteristic

A nested property on a Service or a Service Offering (OSM-M-001).
It is not a catalog entity, has no OSM identifier, and is not a copy
of the TM Forum characteristic model. The same structure is reused
on Service and Offering. There is no shared characteristic registry.

### Provenance

A reusable object that may attach to a Service, a Service Offering,
a service posture record, or an offering posture row. It records why
an enterprise fact can be trusted. The seven provenance fields are
not interchangeable: who is authoritative, which system, which
record, when verified, where evidence lives, how much to trust, how
it was discovered.

### ICT Provider

The canonical record of a third-party technology organization.
Service and Offering associate with it by listing its `id` in
`providers`. Do not copy provider master data onto Service or
Offering. `risk_level` is the canonical assessment of ICT Provider
risk/severity (OSM-M-009). There is no provider `criticality` field.
A cloud provider is an ICT Provider.

### Service Posture (`service_attributes`)

How the service currently stands: shared operational / governance
state, including service-level expectations. It is not the service
definition. `lifecycle_state` does not live here.

### Offering Posture (`offering_attributes`)

Variant-level operations, cost, security and resilience. An empty
`offering_attributes: []` is a valid incremental state.

---

## Frozen relationships

```text
Technology Stack  1 : many  Service
Service           1 : many  Service Offering
Service           0 : many  ICT Provider     via providers
Service Offering  0 : many  ICT Provider     via providers
Service           0 : many  Characteristic   (nested)
Service Offering  0 : many  Characteristic   (nested)
Service / Offering / posture  0 : 1  Provenance  (nested)
Service           1 : 0..1  Service Posture  (service_id)
Service Posture   1 : many  Offering Posture (offering_id)
```

Use Service-level `providers` when the provider is intrinsic to the
capability. Use Offering-level `providers` when provider choice
distinguishes the variant. Association is optional. Multiple ids are
allowed.

**`providers` is the single canonical Service / Offering → ICT
Provider relationship** (OSM-M-006, OSM-M-010). DORA uses this field.
Reverse Provider → Service links are derived from `providers`.

`providers` is not a generic Service → Service relationship.

Do not reintroduce `services_consumed` or `dora_third_party_deps`.

---

## Frozen identity and versioning

IDs use dot-separated segments:

```text
{stack_prefix}.{service_slug}.{offering_slug}
```

- Service ID = 2 segments, e.g. `compute.kubernetes`
- Offering ID = 3 segments, e.g. `compute.kubernetes.aws`
- Each segment is a lowercase, hyphen-delimited slug matching
  `^[a-z0-9]+(?:-[a-z0-9]+)*$`
- The first two segments of an offering ID must equal the parent
  service ID
- An ID never changes once assigned, even if ownership moves or the
  definition is versioned

**Prefixes are stable; stack assignment is mutable.** The prefix
records the stack a service was originally created under. A service
may later be reassigned to a different `technology_stack` without
changing its ID. Therefore the prefix does not always equal the
current stack.

**Immutable identity ≠ immutable definition** (OSM-M-002). Changing
`version` or the definition body does not change `id`. Do not invent
additional identity schemes (no `id`+`version` composite key; one
catalog record per service `id`). That record is the current
definition.

Each Service has `version`, `valid_from`, and optional `valid_to`.
`valid_to: null` means still in force. If `valid_to` is set, it must
not be before `valid_from`. `lifecycle_state` is a required field on
**Service** (not on `service_attributes`): `draft` \| `pilot` \|
`production` \| `sunset` \| `retired`. Prior definitions are not
stored as extra rows; history of prior definitions is out of band
(for example git).

Offerings have no independent version, validity, or lifecycle
fields. They belong to the parent Service definition.

Characteristics have a `name`, not an OSM identifier.

---

## Core architectural principle: OSM-M-008

**OSM-M-008 — One Concept, One Canonical Parameter** is **ACCEPTED**
and is a **core architectural principle** of the frozen model.

OSM MUST NOT represent the same semantic concept through multiple
canonical parameters.

Before introducing any new field, parameter, characteristic,
relationship, or mapping, the entire model must be searched for an
existing representation of the same semantic concept (schemas,
examples, `MODEL.md`, `SPECIFICATION.md`, existing decisions).

The default response to an existing concept is:

**REUSE THE EXISTING CANONICAL REPRESENTATION.**

Express framework-specific semantics through mappings. The existence
of a field in DORA, ISO 27001, ISO 27701, NIST, GDPR, the EU AI Act,
ITIL, CSDM, or TM Forum is not sufficient justification for adding it
to OSM. Framework-specific terminology must not automatically result
in another canonical field.

Duplication is justified only for genuinely different concepts or
different grains — not different names. The default when two fields
appear equivalent is **consolidation, not duplication**. Genuinely
different concepts may coexist even when they use similar names, the
same enum values, or appear related.

---

## Accepted architectural decisions (frozen)

These accepted model decisions form part of the frozen architecture.
OSM-M-005 is superseded and is listed only for the record.

| ID | Title | Status | Meaning in this repository |
|----|-------|--------|----------------------------|
| OSM-M-001 | Generic characteristics | ACCEPTED | Nested characteristic structure on Service and Offering; not a catalog entity and not a TMF characteristic model. |
| OSM-M-002 | Temporal semantics | ACCEPTED | Immutable identity ≠ immutable definition. Service has `version`, `valid_from`, optional `valid_to`, and `lifecycle_state`. Offerings have no version or validity fields. |
| OSM-M-003 | Service is the stable definition | ACCEPTED | An OSM Service is the stable definition of a technological service, without a separate ServiceSpecification entity. |
| OSM-M-004 | Best-of, not standards accumulation | ACCEPTED | Compatibility does not mean copying. OSM incorporates useful semantics and avoids wholesale reproduction. |
| OSM-M-005 | DORA provider-link grain | SUPERSEDED | Superseded by OSM-M-010. |
| OSM-M-006 | Canonical ICT Provider references | ACCEPTED | Service and Offering may list `providers` (ICT Provider ids). Do not embed provider master data. |
| OSM-M-007 | Complete Service Definition | ACCEPTED | Definition, posture, provenance and external context are distinct layers. |
| OSM-M-008 | One concept, one canonical parameter | ACCEPTED | Core principle. One semantic concept, one canonical parameter. Frameworks map; they do not duplicate. |
| OSM-M-009 | ICT Provider risk_level | ACCEPTED | ICT Provider uses `risk_level` as the provider risk/severity concept. ICT Provider does **not** have `criticality`. Service `operational_criticality` and stack `mappings.dora.criticality` remain at their grains. |
| OSM-M-010 | Canonical providers relationship | ACCEPTED | `providers` is the sole canonical provider relationship. `services_consumed` is removed. `dora_third_party_deps` is removed. DORA uses canonical OSM concepts (`providers`, `rto`, `rpo`, `operational_criticality`, `resilience_tested`) rather than duplicate DORA-specific parameters. |

Compatibility decisions OSM-C-001 through OSM-C-005 remain ACCEPTED
as recorded in [`DECISIONS.md`](DECISIONS.md). They define the
compatibility universe and selective ITIL / CSDM status; they do not
add OSM entities.

---

## Explicitly Removed / Forbidden Duplicates

These are **not** part of the frozen model. They must not be
reintroduced as alternative representations of existing concepts
(OSM-M-008, OSM-M-009, OSM-M-010).

| Removed name | Canonical representation |
|--------------|--------------------------|
| `dora_rto` | `rto` |
| `dora_rpo` | `rpo` |
| `dora_criticality` | `operational_criticality` (service); stack `mappings.dora.criticality` remains a different grain |
| `dora_resilience_tested` | `resilience_tested` |
| `cloud_providers` | `providers` (a cloud provider is an ICT Provider) |
| `services_consumed` | derived from canonical `providers` |
| `dora_third_party_deps` | `providers` (DORA uses the canonical relationship) |
| ICT Provider `criticality` | `risk_level` |

Validation rejects these names if they reappear.

---

## Frozen out of scope

The model stops at technological services. It does not describe the
rest of an enterprise. From [`SPECIFICATION.md`](../../SPECIFICATION.md)
and [`MODEL.md`](../../MODEL.md), OSM does not define:

- business capabilities or business services
- digital products
- business outcomes
- value streams
- applications / Application Services
- Service Instance / deployed implementation (runtime context)
- CMDB configuration items or running-system inventory
- Product Models
- organizational hierarchy
- geographic or legal-entity hierarchy
- enterprise-wide ontology
- stakeholder lenses
- enterprise decision intelligence
- detailed service-level / SLA objects
- first-class Service → Service relationships (outside the current
  OSM core; not a permanent rejection — OSM-C-004, OSM-C-005)

Consumers of a technological service are outside the scope of this
model.

OSM does not manage SLAs, contracts, penalties, credits, workflows or
measurement history. OSM records lightweight service-level
**targets** on posture; hours windows are offering characteristics.

---

## Framework compatibility (as currently recorded)

7lens OSM is vendor-neutral, machine-readable, intentionally small,
and an independent canonical model. It is designed to be compatible
with, and mappable to, external frameworks. It is not an
implementation of those frameworks. Frameworks must not become
additional canonical OSM schemas (OSM-M-004, OSM-M-008).

Status is taken from [`COMPATIBILITY.md`](../notes/COMPATIBILITY.md). This
freeze does not perform new analysis. No entry is marked fully
COMPATIBLE.

**Models / taxonomies / architectural frameworks**

| Model | Status |
|-------|--------|
| TM Forum TMF633 Service Catalog | PARTIALLY COMPATIBLE |
| ITIL v5 | PARTIALLY COMPATIBLE |
| ServiceNow CSDM | PARTIALLY COMPATIBLE |
| ArchiMate | NOT ANALYZED |
| TOGAF | NOT ANALYZED |
| TBM | NOT ANALYZED |

**Compliance / governance frameworks**

| Framework | Status |
|-----------|--------|
| ISO/IEC 27001 | NOT ANALYZED |
| ISO/IEC 27701 | NOT ANALYZED |
| NIST CSF | NOT ANALYZED |
| GDPR | NOT ANALYZED |
| DORA | NOT ANALYZED |
| EU AI Act | NOT ANALYZED |

Optional mapping fields already present in the schema remain
illustrative reference mappings, not certification or legal
interpretation. DORA recovery, criticality, resilience testing and
provider association map to canonical `rto`, `rpo`,
`operational_criticality`, `resilience_tested` and `providers`.

---

## Freeze rule

**The OSM architecture is frozen. Future architectural changes
require a new explicit decision record before implementation.**

A future proposal must:

1. Identify the concept/change.
2. Search the existing model for equivalent semantics (schemas,
   examples, `MODEL.md`, `SPECIFICATION.md`, existing decisions).
3. Explain why the existing model cannot represent it.
4. Identify affected entities, fields, relationships and mappings.
5. Assess compatibility impact.
6. Receive an explicit architectural decision whose status is
   `ACCEPTED`.
7. Only then be implemented, on every surface that decision names.

No architectural change should be introduced merely because:

- a framework uses another name;
- another product models it differently;
- an implementation finds it convenient;
- an AI agent suggests it.

Clarifications of existing documentation, synthetic examples, and
validation of already-accepted rules remain in scope when they do
not change architecture.

Agents and contributors do not make architectural or model decisions
in this repository. They may only apply decisions whose status is
`ACCEPTED`.
