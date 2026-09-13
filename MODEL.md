# Conceptual model

7lens OSM describes an enterprise’s **technological services**: their definition, accountability, requestable variants, current posture, and third-party providers.

It does not describe the rest of an enterprise.

Exact fields are in `[SPECIFICATION.md](SPECIFICATION.md)`.

---

## Layers

```text
SERVICE DEFINITION     what the service is (including characteristics)
POSTURE                how it currently stands
  SERVICE POSTURE      current state of a Service
  OFFERING POSTURE     current state of a Service Offering
PROVENANCE             why the information can be trusted
EXTERNAL CONTEXT       owned elsewhere — not modelled here
```

Characteristics belong to the Service or Offering **definition**.
`service_posture` and `offering_posture` are the current state of
those definitions. They are not a second catalog entity.

Framework mappings are a translation layer. They are not a second copy of OSM facts.

---



## Core structure

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

That is the only catalog nesting.

Each service may also carry:

- an **accountable** Service Owner
- **version**, **validity period** and **lifecycle_state**
- optional **characteristics**
- optional **providers** (ICT Provider ids)
- optional **provenance**
- optional **service posture** and **offering posture**

---



## Technology Stack

A Technology Stack answers: *which competency runs this group of services?*

It is not a cost center, not an HR org-chart box, and not an infrastructure inventory. Finance may *map* to stacks; stacks do
not become a chart of accounts.

A service belongs to exactly one current stack. The stack assignment may change; the service ID does not.

---



## Service

A Service is the **stable definition** of a technological service. It is not merely a catalog listing, not an availability record, and not a running instance.

Examples: managed Kubernetes, object storage, identity and access, CI/CD.

A Service has:

- an immutable 2-segment identifier
- a name and description
- a Service Owner (`accountable`)
- a current Technology Stack
- a definition `version`
- a validity window (`valid_from`, optional `valid_to`)
- a `lifecycle_state`
- one or more Service Offerings
- optional characteristics, `providers` and `provenance`

**Immutable identity ≠ immutable definition.** The `id` never changes. The definition may evolve. One catalog record exists per service `id`; that record is the current definition.

A deployed Service Instance is outside OSM.

---



## Service Offering

A Service Offering is the requestable or deliverable **variant** of a Service. Variants may differ in environment, location, availability, packaging, operating model, provider, or other meaningful characteristics.

Do not hard-code every dimension as a core field. Use Characteristics and optional `providers`.

The offering identifier has 3 segments. The first two must equal the parent service ID. Offerings have no independent version, validity or lifecycle fields.

```
service     compute.kubernetes
  └── offering  compute.kubernetes.aws
  └── offering  compute.kubernetes.azure
```

---



## Identity

```
{stack_prefix}.{service_slug}.{offering_slug}
```

- Service ID = 2 segments, for example `compute.kubernetes`
- Offering ID = 3 segments, for example `compute.kubernetes.aws`
- Segments are lowercase, hyphen-delimited slugs

The prefix records the stack under which the service was originally created. A service may later move to another stack without changing its ID.

---



## Characteristics

Services and offerings may declare nested **characteristics**: named, typed properties with optional value, defaults, allowed values, cardinality, constraints and a configurable flag.

Characteristics are a small reusable structure, not a catalog entity.

Typical offering dimensions — environment, location, `service_hours`, `support_hours`, pricing model, unit of consumption — belong here rather than on the core schema.

`service_hours` and `support_hours` describe **when** service or support is available. They are not performance targets.

Reserved names (conventions, not new schema fields):

- `purpose` — generic purpose. Not framework-prefixed (`gdpr_purpose`, …).
- `processing_location` vs `storage_location` — different facts.
- `deployment_region`, `service_region`, `data_residency`, `operating_region`, `region`, `geography`.

**Processing location ≠ storage location.** Provider `data_processing_locations` is capability, not actual offering residency. Do not collapse those with headquarters or availability region. Do not duplicate provider/stack identity through characteristics.

---



## Service posture and offering posture

Posture is **how the service currently stands**. It changes on a
different cadence from the definition.


| Layer            | Holds                                                        |
| ---------------- | ------------------------------------------------------------ |
| Catalog          | Definition of what is delivered, including `lifecycle_state` |
| Service posture  | Shared operational / governance state                        |
| Offering posture | Variant-level operations, cost, security, resilience         |


Empty offering posture lists are valid. Populate them as evidence becomes available.

### Service-level posture

- `operational_criticality` — service criticality
- `resilience_tier` — qualitative resilience class (not a substitute
for `rto` / `rpo`)
- `availability_target`, `response_target`, `resolution_target` —
expected performance, not hours windows
- `data_classification` — data the service handles
- `security_classification` — sensitivity of the service itself
- `privacy_classification` — canonical high-level privacy class; ISO/GDPR fields are mappings
- technical debt, vendor support, `financial_owner`
- optional AI Act applicability fields
- optional provenance

`data_classification` and `security_classification` may share enum tokens. They are not the same fact.

### Offering-level posture

- Finance: `cost_pool`, `chargeback_model`, `unit_cost`(characterization, not accounting)
- Operations: `automation_coverage`, `provisioning_automation`, `self_service`, `manual_hours_week`
- Security operations: `last_security_review`, `asset_coverage` 
- Resilience: `rto`, `rpo`, `resilience_tested`, `last_resilience_test`, `resilience_evidence`
- Optional ISO, NIST, GDPR and EU AI Act mappings

`rto` is Recovery Time Objective. `rpo` is Recovery Point Objective. `automation_coverage` is overall delivery/operation automation; `provisioning_automation` is the provisioning process specifically.

OSM records service-level **expectations**. It does not manage SLAs, contracts, penalties or measurement history.

Ownership roles are defined in `[GOVERNANCE.md](GOVERNANCE.md)`.

---



## Provenance

A reusable `provenance` object may attach to a Service, Offering or posture record. It makes an enterprise fact trustworthy.

Each field answers a different question: who is authoritative, which system, which record, when verified, where evidence lives, how much to trust, how it was discovered. They are not interchangeable.

There is one provenance mechanism. ICT Provider does not currently carry `provenance` (schema-change candidate OSM-M-011). Do not add per-field provenance.

OSM does not model AI interpretation or AI recommendation.

---



## ICT providers

An ICT Provider is the party that **materially delivers, operates, or underpins** the technological Service or Offering. It is not a generic vendor/tool/product inventory. A licensor belongs here only when it materially provides or underpins the capability.

```
Service / Offering  →  providers[]  →  ICT Provider
```

`providers` is the **single canonical** who-provides relationship.

Use Service-level `providers` when the provider is intrinsic to the service. Use Offering-level `providers` when provider choice distinguishes the variant. Association is optional. Multiple ids are allowed.

Do not copy provider master data onto Service or Offering. A cloud provider is an ICT Provider.

`risk_level` is the ICT Provider risk/severity assessment. It is not service `operational_criticality`.

Reverse Provider → Service links are derived from `providers`. `providers` is not a generic Service → Service relationship.

**OSM provider linkage is not a DORA RoI or contractual-arrangement model.** Contract fields on ICT Provider are characterization, not an Arrangement entity. `headquarters` is not processing location, storage location, or actual offering residency. `data_processing_locations` is provider **capability**, not actual Service/Offering residency.

---



## Framework mappings

Stacks, services and offerings may carry optional mappings to TBM, TOGAF, ISO/IEC 27001, ISO/IEC 27701, NIST CSF, GDPR, DORA and the EU AI Act.

Mappings are illustrative and non-normative for those frameworks. OSM can map to or support integration with them. It is not an implementation, certification or legal interpretation of any of them.

Current mapping versions and status: `[models/](models/)` and `[compliance/](compliance/)`.

---



## One concept, one parameter

OSM does not represent the same semantic concept through multiple canonical parameters.

Before adding a field, search the schemas, examples, this file and `SPECIFICATION.md`. If the concept already exists, reuse it.

Genuinely different concepts may coexist even when they use similar names or the same enum values — for example data classification vs security classification, or hours windows vs performance targets.

---



## Out of scope

OSM does not define:

- business capabilities or business services
- digital products, business outcomes or value streams
- applications or Application Services
- Service Instances / deployed implementations
- CMDB configuration items or running-system inventory
- Product Models
- organizational or geographic hierarchy
- an enterprise-wide ontology
- stakeholder lenses or enterprise decision intelligence
- detailed SLA objects
- first-class Service → Service relationships
- DORA RoI, LEI, CIF, contractual Arrangement, or incident feed
- GDPR RoPA, legal basis, DPO, SCCs, or processing-activity entities
- ISO SoA, control implementation, or PIMS processing structures
- NIST Profiles, Categories, Tiers, or control catalogues
- EU AI Act GPAI, deployer/provider legal roles, EU database, or technical-file structures
- ITIL Digital Product, consumers, or the Version 5 Product and Service Lifecycle as OSM objects
- TM Forum Candidate, Category, CFS, RFS, or Service Inventory

Consumers of a technological service are outside this model. Adopters may join OSM records to other systems; this repository does not define those other records.

See `SPECIFICATION.md` §10 for the same boundary as **External Concepts — Intentionally Outside OSM**.