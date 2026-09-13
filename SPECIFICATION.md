# Specification

Version: 1.3.0

This is the normative specification of 7lens OSM (7lens Open Service-Catalog Model): a small, opinionated, machine-readable model for describing an enterprise's technological services, their ownership and delivery, their current posture, and their dependencies on third-party providers.

The specification is vendor-neutral and framework-neutral. Nothing here requires a particular product, cloud or methodology.

**Service** always means a **technological service**. An OSM Service is the **stable definition** of that service, not merely a catalog listing, an availability record, or a running instance.

OSM is a canonical technological-service core. It does not replace ITIL, TM Forum, CSDM, or other enterprise frameworks. It provides a common, vendor-neutral foundation that can be mapped to and extended by specialized frameworks, incorporating useful semantics where they improve interoperability, governance, and machine readability.

The implemented model separates:

```text
SERVICE DEFINITION     what the service is (catalog, including characteristics)
SERVICE POSTURE        how the service currently stands (`service_posture`)
OFFERING POSTURE       how each offering currently stands (`offering_posture`)
PROVENANCE             why the information can be trusted
EXTERNAL CONTEXT       owned by other systems — not modelled here
```

This specification is the implemented field model. Conceptual
explanation is in `[MODEL.md](MODEL.md)`.

---



## 1. Scope and philosophy

The model answers one question:

> What technological services does the enterprise deliver, and in
> what operational state?

It is deliberately a catalog of technological services. It does
not model:

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
- first-class Service → Service relationships
- DORA register of information or contractual Arrangement
- GDPR Record of Processing Activities
- ISO ISMS / PIMS control-implementation objects
- NIST CSF Profiles, Categories, or Tiers
- EU AI Act technical-file or GPAI structures

Consumers of a technological service are outside the scope of this
model. See §10 for the full **External Concepts** list.

OSM is a vendor-neutral technological service model: machine-readable,
intentionally small, designed for interoperability, suitable as a
canonical technology-service layer. It is **not** a CMDB, a complete
enterprise ontology, a DORA RoI, a GDPR RoPA, a ServiceNow CSDM
implementation, an ITIL implementation, a full TM Forum model, an
NIST implementation model, an ISO control system, or an EU AI Act
technical-file system.

### Design principles

1. **Catalog vs. posture.** The catalog holds the **service
  definition** (`id`, version, validity, `lifecycle_state`,
   offerings, characteristics, optional `providers`, optional
   `provenance`). Identity (`id`) is immutable. The definition may
   evolve. Current operational/governance **posture** lives in
   `service_posture` and changes on a different cadence.
2. **Two tiers, no deeper.** A service has service offerings. That is
  the only nesting. Offerings are the atomic requestable unit. OSM
   does not add a ServiceSpecification entity or extra catalog
   hierarchy.
3. **Immutable IDs.** An ID never changes once assigned, even if
  ownership moves or the definition is versioned.
4. **Every service has exactly one operational owner** (a technology
  stack).
5. **Generic characteristics where a dedicated field is not justified.**
  Delivery, service-experience, capacity, commercial and technology
   variant dimensions belong on characteristics unless they are
   classified as posture. Do not grow the core schema for every
   possible property. `service_type` is not a core field; Technology
   Stack remains the classification axis.
6. **Selective compatibility.** Optional mappings to TBM, TOGAF, ISO,
  NIST, GDPR, DORA and the EU AI Act let different readers translate
   the catalog. OSM is not an implementation of those frameworks.
   Compatibility does not mean copying. See `[models/](models/)`
   and `[compliance/](compliance/)`.
7. **One concept, one canonical parameter.** OSM does not represent
  the same semantic concept through multiple canonical parameters.
   Before introducing any new field, parameter, characteristic, or
   mapping field:
  1. Search the entire model for an existing representation of the
    concept.
  2. Check schemas.
  3. Check examples.
  4. Check `MODEL.md`.
  5. Check `SPECIFICATION.md`.
  6. Determine whether the apparent difference is actually semantic
    or merely terminology / framework-specific.
  7. Only add a new field if there is a genuine semantic distinction.
    If an existing OSM field already represents the concept, reuse it
    and express framework-specific semantics through mappings. The
    existence of a field in another standard is not sufficient
    justification for adding it to OSM. Genuinely different concepts
    may coexist even when they use similar names, the same enum
    values, or appear related.

---



## 2. Files and how they relate


| File | Concept | Nature | Typical owner |
|------|---------|--------|---------------|
| `examples/catalog/technology-stacks.yaml` | Operational competency domains | Stable | Platform leadership |
| `examples/catalog/services.yaml` | The catalog (services, with nested offerings) | Stable | Stack + Service Owners |
| `examples/catalog/ict-providers.yaml` | Third-party provider register | Semi-dynamic | Vendor management / risk |
| `examples/posture/service-posture.yaml` | Service / offering **posture** | Dynamic | Multiple teams |

The schema defines Service Offering as its own concept. In catalog
data, offerings are nested under their parent Service. See
`[examples/README.md](examples/README.md)`.

```
catalog/technology-stacks.yaml
        │  1 stack : many services
        v
catalog/services.yaml          ← the catalog
        │                       providers[] → catalog/ict-providers.yaml
        │ service_id
        v
posture/service-posture.yaml
```

JSON Schema is in `schema/catalog/`, `schema/posture/` and
`schema/shared/`.

---



## 3. Identifiers

IDs use dot-separated segments:

```
{stack_prefix}.{service_slug}.{offering_slug}
```

- **Service ID** = 2 segments, e.g. `compute.kubernetes`
- **Offering ID** = 3 segments, e.g. `compute.kubernetes.aws`
- Each segment is a lowercase, hyphen-delimited slug matching
`^[a-z0-9]+(?:-[a-z0-9]+)*$`

**Prefixes are stable; stack assignment is mutable.** The prefix
records the stack a service was originally created under. A service
may later be reassigned to a different `technology_stack` without
changing its ID. Therefore the prefix does not always equal the
current stack.

**Immutable identity ≠ immutable definition.** Changing `version` or
the definition body does not change `id`. Do not invent additional
identity schemes (no `id`+`version` composite key; one catalog
record per service `id`).

---



## 4. Technology Stack

A **technology stack** is an operational competency domain that runs
a group of services day to day. It is not a financial taxonomy.

Adopting organizations typically define 8–20 stacks. The examples
in this repository are a starter set.

### Fields


| Field         | Required | Description                                                        |
| ------------- | -------- | ------------------------------------------------------------------ |
| `id`          | yes      | Short stable identifier (also used as the default service prefix). |
| `name`        | yes      | Human-readable stack name.                                         |
| `description` | yes      | Plain-language description of the stack's scope.                   |
| `mappings`    | no       | Optional reference mappings (see below).                           |




### `mappings` sub-fields (all optional)


| Mapping         | Purpose                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------- |
| `tbm_tower`     | TBM Taxonomy 5.0.1 **Technology Resource Tower** label — finance mapping, not a TBM catalog     |
| `tbm_sub_tower` | TBM Sub-Tower label                                                                             |
| `togaf_domain`  | TOGAF 10th Edition architecture domain label (Business, Data, Application, or Technology)       |
| `iso27001`      | Free-text ISO/IEC 27001:2022 Annex A control references                                         |
| `iso27701`      | Free-text ISO/IEC 27701:2025 references, or `not-applicable`                                    |
| `nist_csf`      | List of NIST CSF 2.0 functions: `govern`, `identify`, `protect`, `detect`, `respond`, `recover` |
| `gdpr`          | Free-text GDPR article references, or `not-applicable`                                          |
| `dora`          | `pillar` and `criticality` (see enums below)                                                    |
| `ai_act`        | `contains_ai_systems`, `max_risk_class`, optional `reference`                                   |


DORA `pillar` ∈ {`ICT Risk Management`, `ICT-related Incident Management`, `Digital Operational Resilience Testing`, `ICT Third-Party Risk Management`}

DORA `criticality` ∈ {`critical`, `important`, `standard`}

EU AI Act `max_risk_class` ∈ {`unacceptable`, `high-risk`, `limited-risk`, `minimal-risk`, `not-applicable`}

These mappings are **optional reference mappings**. They are not a
claim of compliance, certification, or legal interpretation. OSM can
**map to** / **support integration with** the named frameworks; it
does not implement them.

Stack `mappings.dora.criticality` is a **stack-level** DORA-oriented
label. Service criticality is canonical `operational_criticality`.
Those are different grains. Stack `standard` is an OSM enum token,
not a DORA CIF class.

`togaf_domain` sits on Technology Stack only. Do not add TOGAF
domain fields to Service.

`tbm_tower` / `tbm_sub_tower` sit on Technology Stack only. Do not
add Service-level TBM Solutions-layer fields unless a future
mapping extension requires them.

EU AI Act `max_risk_class` is an **OSM compatibility label**. It
does not reproduce Article 6 / Annex III legal classification.

---



## 5. Service

A **Service** is the stable **definition** of a technological service.
Conceptually this is the role a service specification plays in a
service catalog. OSM does **not** introduce a separate
ServiceSpecification entity. A Service is not merely a catalog entry
or an availability record, and it is not a running instance.


| Concept                                    | Where                                                         |
| ------------------------------------------ | ------------------------------------------------------------- |
| OSM Service                                | Canonical **definition** of a technological service           |
| Service Offering                           | Canonical requestable/deliverable **variant** of that service |
| Service Instance / deployed implementation | Operational/runtime representation **outside** the OSM core   |




### Service fields


| Field               | Required | Description                                                                                                                                            |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                | yes      | 2-segment service ID. Immutable.                                                                                                                       |
| `name`              | yes      | Service name.                                                                                                                                          |
| `description`       | yes      | Plain-language service description.                                                                                                                    |
| `accountable`       | yes      | Person or role accountable for the service definition and overall service accountability (the Service Owner). Distinct from posture `financial_owner`. |
| `technology_stack`  | yes      | The `name` of the owning stack. Exactly one.                                                                                                           |
| `version`           | yes      | Definition version (opaque string). Does not change `id`.                                                                                              |
| `valid_from`        | yes      | Inclusive ISO 8601 date this definition takes effect.                                                                                                  |
| `valid_to`          | no       | Inclusive ISO 8601 date this definition ends, or `null` if still in force.                                                                             |
| `lifecycle_state`   | yes      | `draft` | `pilot` | `production` | `sunset` | `retired`. Authoritative definition lifecycle.                                                           |
| `characteristics`   | no       | Generic characteristics (see §5.1).                                                                                                                    |
| `providers`         | no       | ICT Provider ids when the provider is intrinsic to this Service.                                                                                       |
| `provenance`        | no       | Reusable provenance for this definition.                                                                                                               |
| `service_offerings` | yes      | List of offerings.                                                                                                                                     |


This catalog record is the **current** definition for that `id`.
Prior definitions are not stored as extra rows; validity tells a
machine the period this definition covers. `valid_to: null` means
still in force. `lifecycle_state` lives on the Service, not on
`service_posture`. Offerings have no independent version,
validity, or lifecycle fields.

### Offering fields


| Field             | Required | Description                                                        |
| ----------------- | -------- | ------------------------------------------------------------------ |
| `id`              | yes      | 3-segment offering ID. Immutable.                                  |
| `name`            | yes      | What a consumer can request.                                       |
| `description`     | no       | Optional clarification of the variant.                             |
| `characteristics` | no       | Generic characteristics (see §5.1).                                |
| `providers`       | no       | ICT Provider ids when provider choice distinguishes this offering. |
| `provenance`      | no       | Reusable provenance for this offering.                             |


An **offering** is the atomic requestable/deliverable variant of a
Service. It may differ in delivery characteristics such as
environment, location, availability, packaging, operating model,
provider, or other meaningful dimensions. Do not turn each dimension
into a mandatory core field; use characteristics and optional
`providers` instead.

A service offered across clouds typically has
one offering per cloud or operating model. Offerings are part of the
parent Service definition; they do not have a separate version or
validity window.

### 5.1 Characteristics

A **characteristic** is a nested property on a Service or a Service
Offering. It is not a catalog entity, has no OSM identifier, and is
not a copy of the TM Forum characteristic model.

The same structure is used on both Service and Offering so properties
can be declared at either grain without dedicated core fields.


| Field             | Required | Description                                                |
| ----------------- | -------- | ---------------------------------------------------------- |
| `name`            | yes      | Key. Unique within the parent. Lowercase snake_case.       |
| `value_type`      | yes      | `string` | `number` | `boolean` | `date`                   |
| `description`     | no       | Human-readable meaning.                                    |
| `value`           | no       | Current value, when set.                                   |
| `default_value`   | no       | Default when `value` is omitted.                           |
| `allowed_values`  | no       | Closed list of permitted values.                           |
| `min_cardinality` | no       | Minimum number of values (integer ≥ 0).                    |
| `max_cardinality` | no       | Maximum number of values, or `null` if unbounded.          |
| `configurable`    | no       | `true` if a consumer may choose the value when requesting. |
| `constraints`     | no       | Optional `min`, `max`, and/or `pattern`.                   |


Rules:

1. `name` is unique among characteristics of the same parent.
2. If `value` is set and `allowed_values` is non-empty, `value` must
  be a member of `allowed_values`.
3. If `max_cardinality` is set, it must be ≥ `min_cardinality`
  (treat omitted `min_cardinality` as 0).
4. Do not add a characteristic to the core schema when this mechanism
  is enough. Offering dimensions such as environment, location,
   service hours, support hours, pricing model and unit of
   consumption are characteristics, not dedicated schema fields.
   `service_hours` is the time window the service is intended to be
   available; `support_hours` is the time window support is
   available. They are not `availability_target`, `response_target`
   or `resolution_target`.

Reserved characteristic **names** (conventions, not schema fields).
Use these rather than inventing duplicates. Distinct names mean
distinct facts (**OSM-D-001**, **OSM-D-002**):

| `name` | Meaning |
|--------|---------|
| `purpose` | Generic purpose of the service or offering. Not `gdpr_purpose`, `iso27701_purpose`, `dora_purpose`, or `ai_act_purpose`. |
| `region` | Coarse region label when a single region applies. |
| `geography` | Broader geography when not a single region code. |
| `deployment_region` | Where the offering is deployed. |
| `service_region` | Where the service is offered / available. Not the same as processing or storage. |
| `data_residency` | Residency constraint or actual residency policy for the offering. |
| `processing_location` | Where data is **processed**. Not storage. |
| `storage_location` | Where data is **stored**. Not processing. |
| `operating_region` | Operating / availability region when that is the intended fact. |

**data processing location ≠ data storage location.**

**provider capability / possible location ≠ actual service or
offering residency.** ICT Provider `data_processing_locations` is a
capability map. Actual residency belongs on Service/Offering
characteristics.

Do not use a characteristic to duplicate identity already expressed
by `providers` or stack assignment (for example
`deployment_environment: aws` when AWS is already the ICT Provider).

Do not add these as new core schema properties.



### 5.2 Provenance

A reusable **provenance** object may be attached to a Service, a
Service Offering, a service posture record, or an offering posture
row. It records why an enterprise fact can be trusted. It is not an
AI interpretation or recommendation.

There is **one** provenance mechanism (**OSM-M-011**). Do not add
per-field provenance. ICT Provider does **not** currently allow
`provenance` in the schema (`additionalProperties: false`). Adding
it is a documented schema-change **candidate**, not an implemented
field. Do not invent a provider-specific provenance type.


| Field                  | Required | Description                                                                                                      |
| ---------------------- | -------- | ---------------------------------------------------------------------------------------------------------------- |
| `authoritative_source` | no       | Who or what is authoritative (person, role, or body). Distinct from `source_system`.                             |
| `source_system`        | no       | System the information came from. Distinct from `authoritative_source` and `source_record_id`.                   |
| `source_record_id`     | no       | Identifier of the originating record in `source_system`. Distinct from `evidence_reference`.                     |
| `last_verified`        | no       | ISO 8601 date last verified.                                                                                     |
| `evidence_reference`   | no       | Handle or URI for supporting evidence. Not the source record.                                                    |
| `confidence`           | no       | Trust in the fact: `high` | `medium` | `low` | `unknown`. Distinct from `discovery_method`.                      |
| `discovery_method`     | no       | How the fact entered the catalog: `declared` | `imported` | `discovered` | `manual`. Distinct from `confidence`. |


These seven fields are not interchangeable. Each answers a different
trust question. Do not collapse them.

---



## 6. Service posture

Organized **by service** in `service_posture`. This is
**Service Posture** (how the service currently stands) plus nested
**Offering Posture**.

Service-level fields are not duplicated per offering — an offering
inherits them from its parent. An empty `offering_posture: []` is
a valid incremental state.

Canonical OSM posture fields are unprefixed. Framework-named fields
remain optional **mappings of concepts OSM does not already
represent**. Do not add a framework-prefixed copy of a canonical
field. DORA recovery and criticality information maps to canonical
`rto`, `rpo`, `operational_criticality` and `resilience_tested`.
DORA provider associations map to canonical `providers`.

OSM records lightweight **service-level expectations**
(`availability_target`, `response_target`, `resolution_target`) on
service posture. **Targets** describe expected service performance.
`service_hours` and `support_hours` are offering **characteristics**
that describe **when** service or support is available. They are not
the same concept as the targets. OSM does not manage SLAs, contracts,
penalties, credits, workflows or measurement history.

### Service-level fields


| Field                     | Values                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `service_id`              | Must exist in the services catalog.                                                                                      |
| `tech_debt_score`         | `0`–`100`, or `null` if not assessed.                                                                                    |
| `operational_criticality` | `critical` | `important` | `standard`                                                                                    |
| `resilience_tier`         | qualitative resilience classification/tier (free-text). Not a replacement for offering `rto` / `rpo`.                    |
| `availability_target`     | expected/target level of service availability (e.g. `99.9%`). A performance target, not `service_hours`.                 |
| `response_target`         | expected target time to respond to an incident/request (ISO 8601 duration). A performance target, not `support_hours`.   |
| `resolution_target`       | expected target time to resolve an incident/request (ISO 8601 duration). A performance target, not hours.                |
| `data_classification`     | classification of the data handled, processed, stored, or exposed: `public` | `internal` | `confidential` | `restricted` |
| `security_classification` | security sensitivity of the service itself: `public` | `internal` | `confidential` | `restricted`                        |
| `privacy_classification`  | `none` | `pii` | `sensitive` | `not-assessed`                                                                            |
| `vendor_support_status`   | `active` | `extended` | `end-of-life`                                                                                    |
| `financial_owner`         | person/role responsible for financial ownership. Distinct from Service `accountable`.                                    |
| `provenance`              | reusable provenance object                                                                                               |
| `ai_act_applicable`       | `true` | `false`                                                                                                         |
| `ai_act_risk_class`       | `unacceptable` | `high-risk` | `limited-risk` | `minimal-risk` | `not-applicable`                                        |


`operational_criticality` is the canonical criticality semantic.

`privacy_classification` is the canonical OSM high-level privacy
classification (**OSM-D-003**). Framework-specific privacy fields
(`iso27701_pii_role`, `gdpr_processing_activity`, …) are
compatibility mappings, not competing canonical classes. Do not
create `gdpr_privacy_classification` or similar.

`ai_act_*` fields are named for the framework they optionally map
to. Using them does not constitute an AI Act assessment.
`ai_act_risk_class` is an **OSM compatibility label**. Its enum does
**not** reproduce Article 6 / Annex III legal classification.
`ai_act_human_oversight` is an EU AI Act compatibility field; do
not rename it to generic `human_oversight`.

`data_classification` and `security_classification` share enum tokens
on purpose. They are **not** the same fact: one classifies the data
the service handles; the other classifies the service itself.
`resilience_tier` is a qualitative classification; offering `rto` /
`rpo` are explicit Recovery Time / Recovery Point Objectives. A tier
MAY imply expected recovery characteristics, but it does not replace
those values. `accountable` (Service definition) is not
`financial_owner` (posture).

### Offering-level fields

**Finance (characterization, not accounting)**


| Field              | Values                                 |
| ------------------ | -------------------------------------- |
| `cost_pool`        | free-text cost pool, or `null`         |
| `chargeback_model` | `shared` | `dedicated` | `consumption` |
| `unit_cost`        | number ≥ 0, or `null`                  |


Cloud / vendor association is not a finance enum. Use canonical
`providers` on the Service or Offering. A cloud provider is an ICT
Provider.

**Operations**


| Field                     | Values                                                                                                         |
| ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `automation_coverage`     | `none` | `partial` | `full` | `null` — degree to which overall delivery/operation of the offering is automated |
| `provisioning_automation` | `none` | `partial` | `full` | `null` — degree to which the provisioning process specifically is automated      |
| `self_service`            | `true` | `false` | `null`                                                                                      |
| `manual_hours_week`       | number, or `null`                                                                                              |


`automation_coverage` and `provisioning_automation` share enum tokens
on purpose. They are **not** the same fact: overall operational
automation versus the provisioning process.

**Security operations**


| Field                  | Values                                      |
| ---------------------- | ------------------------------------------- |
| `last_security_review` | ISO 8601 date, or `null`                    |
| `asset_coverage`       | `complete` | `partial` | `unknown` | `null` |


**Canonical resilience (offering posture)**


| Field                  | Values                                                               |
| ---------------------- | -------------------------------------------------------------------- |
| `rto`                  | Recovery Time Objective (ISO 8601 duration, e.g. `PT8H`), or `null`  |
| `rpo`                  | Recovery Point Objective (ISO 8601 duration, e.g. `PT1H`), or `null` |
| `resilience_tested`    | `true` | `false` | `null`                                            |
| `last_resilience_test` | ISO 8601 date, or `null`                                             |
| `resilience_evidence`  | handle or URI, or `null`                                             |


`rto` and `rpo` are explicit recovery objectives. Service-level
`resilience_tier` is a qualitative classification of the service.
They coexist; the tier is not a substitute for RTO/RPO.

**ISO 27001 / 27701 (reference mappings)**


| Field                     | Values                                                                                                     |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `iso27001_controls`       | list of Annex A control IDs — locators, not SoA or implemented-control evidence                                |
| `iso27701_pii_role`       | Compatibility mapping to ISO/IEC 27701:2025 controller/processor language: `controller` \| `processor` \| `joint-controller` \| `none`. Per **offering**, not per processing activity. Not a PIMS. Canonical privacy class remains `privacy_classification`. |
| `iso27701_pii_categories` | list of `identity`, `financial`, `health`, `behavioral`, `location`, `biometric`, `communications`, `none` |
| `iso27701_retention_days` | number, or `null` — characterization, not a legal retention schedule                                           |


**NIST CSF 2.0 (reference mappings)**


| Field                 | Values                                                                          |
| --------------------- | ------------------------------------------------------------------------------- |
| `nist_functions`      | list of CSF 2.0 Functions: `govern`, `identify`, `protect`, `detect`, `respond`, `recover` |
| `nist_control_status` | OSM assessment **signal**: `implemented` \| `partially-implemented` \| `planned` \| `not-applicable` \| `null`. **Not** a native NIST CSF object, Profile, Category, or control-catalogue entry. |


**GDPR (reference mappings)**


| Field                      | Values                                          |
| -------------------------- | ----------------------------------------------- |
| `gdpr_processing_activity` | `true` | `false`                                |
| `gdpr_dpia_required`       | `true` | `false`                                |
| `gdpr_erasure_capable`     | `true` | `false` | `partial` | `not-applicable` |


**DORA**

DORA recovery and testing semantics map to canonical `rto`, `rpo`
and `resilience_tested` above. DORA provider associations map to
canonical `providers` on Service or Offering. That linkage is **not**
a DORA RoI or contractual-arrangement model. Do not treat
`providers` as `dora_third_party_deps`.

An offering posture row may also carry `provenance`.

**EU AI Act (present only when** `ai_act_applicable: true`**)**


| Field                          | Values                                                                  |
| ------------------------------ | ----------------------------------------------------------------------- |
| `ai_act_intended_purpose`      | free text                                                               |
| `ai_act_human_oversight`       | `human-in-the-loop` | `human-on-the-loop` | `human-in-command` | `none` |
| `ai_act_transparency_level`    | `explicit-disclosure` | `implicit-disclosure` | `none`                  |
| `ai_act_conformity_assessment` | ISO 8601 date, or `null`                                                |
| `ai_act_training_data_doc`     | `true` | `false` | `not-applicable`                                     |


Illustrative values in examples are **not legal advice** and are
**not evidence of certification or regulatory compliance**.

---



## 7. ICT providers

A register of ICT providers that **materially deliver, operate, or
underpin** a technological Service or Service Offering
(**OSM-C-006**). This entity is the **canonical** provider
definition. It is **not** a generic vendor, tool, or product
inventory.

Use ICT Provider for the party that provides the technology
capability. A **licensor** is an ICT Provider only when it
materially provides or underpins the Service/Offering. Generic
software tools, products, suppliers, or commercial parties are not
automatically ICT Providers. Do not introduce provider-role fields
(`operator_provider`, `licensor_provider`, `vendor_role`,
`provider_role`).

Service and Service Offering associate with a provider by listing
its `id` in `providers`. If an offering is provider-specific, the
id belongs on the Offering. If the provider is intrinsic to the
whole Service, the id belongs on the Service.

Do not copy headquarters, locations, certifications, contracts, risk,
substitutability or other provider attributes onto Service or Offering.

**OSM provider linkage is not a DORA RoI or contractual-arrangement
model** (**OSM-C-007**). Contract-related fields below characterize
the provider record. They are not an Arrangement entity. DORA
supervisory reporting may consume this relationship **outside** OSM.

```
Service / Offering
      ↓  providers (ids, optional, 0..n)
ICT Provider
```

`providers` is the **single canonical** who-provides association.
It means the ICT provider delivering or underpinning that Service or
Offering. It is not a generic Service → Service relationship.
Reverse Provider → Service links are derived from `providers`.

`risk_level` is the canonical ICT Provider risk/severity assessment.
Service `operational_criticality` and stack
`mappings.dora.criticality` are different grains.

Fields support vendor-risk conversations; they do not by themselves
satisfy any regulatory filing.


| Field                       | Required | Description                                                                                                               |
| --------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------- |
| `id`                        | yes      | Short identifier referenced by `providers`                                                                                |
| `name`                      | yes      | Provider name                                                                                                             |
| `type`                      | yes      | `cloud-infrastructure` | `cloud-platform` | `managed-service` | `software-vendor` | `network-provider` | `data-center`    |
| `headquarters`              | no       | ISO 3166-1 alpha-2 country code. **Not** processing location, storage location, or service availability region.           |
| `data_processing_locations` | no       | Countries or regions the provider **can** process in (capability / possible locations). **Not** actual Service/Offering residency, and **not** storage location. |
| `substitutability`          | yes      | `low` | `medium` | `high`                                                                                                 |
| `contract_ref`              | no       | Local contract reference, or `null`                                                                                       |
| `contract_start`            | no       | ISO 8601 date, or `null`                                                                                                  |
| `contract_end`              | no       | ISO 8601 date, or `null`                                                                                                  |
| `notice_period_days`        | no       | number, or `null`                                                                                                         |
| `audit_rights`              | no       | `true` | `false` | `null`                                                                                                 |
| `subcontracting_allowed`    | no       | `true` | `false` | `conditional` | `null`                                                                                 |
| `subcontractors`            | no       | list of names                                                                                                             |
| `last_risk_assessment`      | no       | ISO 8601 date, or `null`                                                                                                  |
| `risk_level`                | no       | Canonical provider risk/severity: `low` | `medium` | `high` | `critical` | `null`. Not service `operational_criticality`. |
| `exit_strategy_documented`  | no       | `true` | `false` | `null`                                                                                                 |
| `exit_strategy_tested`      | no       | `true` | `false` | `null`                                                                                                 |
| `concentration_risk`        | no       | `true` | `false` | `null`                                                                                                 |
| `certifications`            | no       | free-form list (e.g. `iso27001`, `soc2-type2`)                                                                            |
| `gdpr_dpa_signed`           | no       | `true` | `false` | `null`                                                                                                 |
| `dora_notification_clause`  | no       | `true` | `false` | `null`                                                                                                 |


Do not publish a real vendor register as an example.

Contract-related fields (`contract_ref`, `contract_start`,
`contract_end`, `notice_period_days`, `audit_rights`,
`subcontracting_allowed`, `subcontractors`,
`exit_strategy_documented`, and related flags) characterize the
provider relationship. They are **not** a DORA Arrangement model.

ICT Provider has no `provenance` field in this version. See
**OSM-M-011** (schema-change candidate).

---



## 8. Governance roles

See `[GOVERNANCE.md](GOVERNANCE.md)`.

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
4. Every `service_posture[].service_id` exists in the services catalog.
5. Every `offering_posture[].offering_id` exists under its parent
  service in the services catalog.
6. EU AI Act offering fields are present only where
  `ai_act_applicable: true`.
7. Duplicate IDs are rejected for stacks, services, offerings and
  providers.
8. Characteristic `name` values are unique within a Service and
  within each Offering. `value` must match `allowed_values` when
   that list is present.
9. Each Service has `version`, `valid_from` and `lifecycle_state`.
  If `valid_to` is set, it must not be before `valid_from`.
10. `service_posture` must not contain `lifecycle_state`.
11. Every id in Service or Offering `providers` exists in the ICT
  provider file. The field may be omitted. Duplicate ids in one
    list are rejected.
12. If `provenance` is present, `confidence` and `discovery_method`
  must use the published enums; `last_verified` must be an ISO date.
13. Service and Offering records must not declare Service-to-Service
  relationship fields (`depends_on`, `depends_on_services`,
    `dependencies`, `service_dependencies`, `requires_service`,
    `consumes_service`, `consumes`, `provides_to`, `related_service`,
    `related_services`).
14. Records must not declare properties outside this specification.
  Schemas set `additionalProperties: false`.
15. ICT Provider risk/severity is `risk_level`. Reverse Provider →
  Service links are derived from `providers`.

See `[validation/](validation/)` for a lightweight checker.

---

## 10. External Concepts — Intentionally Outside OSM

OSM is not intended to absorb these concepts. Map or join to them
in an external integration layer. Do not add them as OSM entities.

### CSDM

- Service Instance
- related running-instance concepts (including CSDM 5 siblings)

### TM Forum

- Candidate
- Category
- Customer Facing Service (CFS)
- Resource Facing Service (RFS)
- Service Inventory / Service Instance

### ITIL

- Digital Product
- Consumers
- Value Streams
- Product and Service Lifecycle activities (not OSM `lifecycle_state`)

### NIST CSF

- Profiles
- Categories
- Tiers
- control implementation structures

### ISO

- Statement of Applicability (SoA)
- control implementation objects
- PIMS processing structures

### GDPR

- Record of Processing Activities (RoPA)
- legal basis
- DPO
- SCCs
- processing activities

### DORA

- Register of Information (RoI)
- Legal Entity Identifier (LEI)
- CIF register
- contractual Arrangement
- incident feed

### EU AI Act

- GPAI model structures
- legal provider/deployer role structures
- EU database
- technical file / conformity assessment structures

### Architecture / inventory

- Application
- Application Service
- Service Instance
- running CMDB inventory
