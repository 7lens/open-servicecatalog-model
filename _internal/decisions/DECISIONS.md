# 7lens OSM — Decision register

> **Maintainer archive.** This register lives under
> `_internal/decisions/`. It is not public OSM documentation.
> The current model is defined by `schema/`, `SPECIFICATION.md` and
> `MODEL.md` at the repository root.

This file is the **decision register** (index). Detailed model
decision documents live in this directory.

```text
DECISIONS.md     Decision register / index
decisions/       Detailed architectural decisions
```

The current architecture is frozen. Authoritative freeze record:
[`OSM-ARCHITECTURE-FREEZE.md`](OSM-ARCHITECTURE-FREEZE.md).

**Agents and contributors do not make architectural or model
decisions here.** They may only apply decisions whose status is
`ACCEPTED`.

There was no prior numbering scheme in this repository. New IDs use:

| Prefix | Use |
|--------|-----|
| `OSM-C-nnn` | Compatibility universe and mapping decisions |
| `OSM-M-nnn` | Model / schema decisions |
| `OSM-D-nnn` | Documentation / naming decisions |

---

## Decision record template

```
### OSM-X-nnn — Title

- Status: PROPOSED | ACCEPTED | SUPERSEDED | REJECTED
- Date:
- Type: Compatibility | Model | Documentation
- Decision:
- What this is not:
- Surfaces to update:
- Notes:
```

Accepted **model** decisions also have a file under `decisions/`.

---

## Decision propagation

When a decision becomes `ACCEPTED`, update **every surface it names**.
Leave unnamed surfaces unchanged.

Propagation rules:

1. Do not add, remove or rename entities, attributes or relationships
   unless the accepted decision says to.
2. Keep `SPECIFICATION.md` normative for fields and rules.
3. Keep `MODEL.md` conceptual; do not let it drift from the spec.
4. Keep README user-facing and aligned with accepted names and scope.
5. Keep examples synthetic and valid against `validation/validate.py`.
6. Update the matching file under `compatibility/` or `compliance/`
   and the status table in `COMPATIBILITY.md`.
7. If identifiers or enums change, update `validation/validate.py`.
8. Record the commit or PR on the decision once applied.
9. Detailed `OSM-M-*` text lives in `decisions/`; keep this register
   in sync (status, date, link).

---

## Compatibility decisions

Compatibility decision records remain in this file (no `decisions/`
extraction was requested for `OSM-C-*`).

| ID | Decision | Status | Date | Record |
|----|----------|--------|------|--------|
| OSM-C-001 | Initial compatibility universe | ACCEPTED | 2026-09-12 | [below](#osm-c-001--initial-compatibility-universe) |
| OSM-C-002 | Remove PDMC from the universe | ACCEPTED | 2026-09-12 | [below](#osm-c-002--remove-pdmc-from-the-compatibility-universe) |
| OSM-C-003 | Retain ServiceNow CSDM in the universe | ACCEPTED | 2026-09-12 | [below](#osm-c-003--retain-servicenow-csdm-in-the-compatibility-universe) |
| OSM-C-004 | ITIL v5 selective compatibility | ACCEPTED | 2026-09-12 | [below](#osm-c-004--itil-v5-selective-compatibility) |
| OSM-C-005 | CSDM selective compatibility | ACCEPTED | 2026-09-12 | [below](#osm-c-005--csdm-selective-compatibility) |
| OSM-C-006 | ICT Provider semantics | ACCEPTED | 2026-09-13 | [below](#osm-c-006--ict-provider-semantics) |
| OSM-C-007 | DORA arrangements remain external | ACCEPTED | 2026-09-13 | [below](#osm-c-007--dora-arrangements-remain-external) |
| OSM-C-008 | Service→Service remains forbidden | ACCEPTED | 2026-09-13 | [below](#osm-c-008--serviceservice-remains-forbidden) |
| OSM-C-009 | Canonical concept first, framework mapping second | ACCEPTED | 2026-09-13 | [below](#osm-c-009--canonical-concept-first-framework-mapping-second) |

---

## Model decisions

| ID | Decision | Status | Date | Document |
|----|----------|--------|------|----------|
| OSM-M-001 | Generic characteristics | ACCEPTED | 2026-09-12 | [`OSM-M-001-generic-characteristics.md`](OSM-M-001-generic-characteristics.md) |
| OSM-M-002 | Temporal semantics | ACCEPTED | 2026-09-12 | [`OSM-M-002-temporal-semantics.md`](OSM-M-002-temporal-semantics.md) |
| OSM-M-003 | Service is the stable definition | ACCEPTED | 2026-09-12 | [`OSM-M-003-service-definition.md`](OSM-M-003-service-definition.md) |
| OSM-M-004 | Best-of, not standards accumulation | ACCEPTED | 2026-09-12 | [`OSM-M-004-best-of-not-standards-accumulation.md`](OSM-M-004-best-of-not-standards-accumulation.md) |
| OSM-M-005 | DORA provider-link grain | SUPERSEDED | 2026-09-12 | [`OSM-M-005-dora-provider-link-grain.md`](OSM-M-005-dora-provider-link-grain.md) |
| OSM-M-006 | Canonical ICT Provider references | ACCEPTED | 2026-09-12 | [`OSM-M-006-ict-provider-references.md`](OSM-M-006-ict-provider-references.md) |
| OSM-M-007 | Complete Service Definition | ACCEPTED | 2026-09-12 | [`OSM-M-007-complete-service-definition.md`](OSM-M-007-complete-service-definition.md) |
| OSM-M-008 | One concept, one canonical parameter | ACCEPTED | 2026-09-12 | [`OSM-M-008-one-concept-one-canonical-parameter.md`](OSM-M-008-one-concept-one-canonical-parameter.md) |
| OSM-M-009 | ICT Provider risk_level | ACCEPTED | 2026-09-12 | [`OSM-M-009-ict-provider-risk-level.md`](OSM-M-009-ict-provider-risk-level.md) |
| OSM-M-010 | Canonical providers relationship | ACCEPTED | 2026-09-12 | [`OSM-M-010-canonical-providers-relationship.md`](OSM-M-010-canonical-providers-relationship.md) |
| OSM-M-011 | ICT Provider provenance (principle) | ACCEPTED | 2026-09-13 | [`OSM-M-011-ict-provider-provenance.md`](OSM-M-011-ict-provider-provenance.md) |

**OSM-M-011** is ACCEPTED as an architectural *principle*: ICT Provider
must reuse the existing `provenance` object; there is no
provider-specific provenance system and no per-field provenance.
The ICT Provider schema does **not** currently allow `provenance`.
That schema change is **not implemented**. See the decision file.

---

## Documentation decisions

| ID | Decision | Status | Date | Record |
|----|----------|--------|------|--------|
| OSM-D-001 | Location / residency via characteristics | ACCEPTED | 2026-09-13 | [below](#osm-d-001--location--residency-via-characteristics) |
| OSM-D-002 | Purpose as a characteristic | ACCEPTED | 2026-09-13 | [below](#osm-d-002--purpose-as-a-characteristic) |
| OSM-D-003 | Privacy classification precedence | ACCEPTED | 2026-09-13 | [below](#osm-d-003--privacy-classification-precedence) |

**OSM-M-007** is ACCEPTED and implemented. Schema/examples/validation
now include Complete Service Definition semantics (posture fields,
provenance, service-level expectations). OSM-M-007 does not change
the status of OSM-M-001–OSM-M-006.

**OSM-M-008** is ACCEPTED. OSM must not represent the same semantic
concept through multiple canonical parameters. DORA RTO/RPO map to
canonical `rto` / `rpo`. Provider association is `providers`;
`cloud_providers` is not an OSM field. OSM-M-008 is the governing
principle behind OSM-M-009 and OSM-M-010.

**OSM-M-009** is ACCEPTED. ICT Provider has `risk_level`, not
`criticality`. `risk_level` is the canonical assessment of ICT
Provider risk/severity. Do not add another provider criticality
field. Service `operational_criticality` and stack
`mappings.dora.criticality` are different grains and remain.

**OSM-M-010** is ACCEPTED and **supersedes OSM-M-005**. `providers`
is the single canonical Service/Offering → ICT Provider
relationship. `services_consumed` is removed because reverse
relationships can be derived. `dora_third_party_deps` is removed
because DORA does not justify duplicating the canonical provider
relationship. DORA uses `providers`.

OSM-M-009 and OSM-M-010 are the **final model corrections** of the
current OSM architecture.

**The current OSM architecture is frozen.** The authoritative freeze
record is
[`OSM-ARCHITECTURE-FREEZE.md`](OSM-ARCHITECTURE-FREEZE.md).
Future architectural changes require a new explicit decision record
before implementation.

---

## Terminology note (OSM-M-007 vs current repository)

OSM-M-007 formally distinguishes:

```text
SERVICE DEFINITION     What the service is
SERVICE POSTURE        How the service currently stands
EXTERNAL CONTEXT       Information owned by other models or systems
```

The **implemented** repository uses these names for the M-007 layers:

| Repository term | OSM-M-007 term |
|-----------------|----------------|
| Catalog (`services.yaml`) | Service Definition |
| `service_attributes` / `offering_attributes` | Service Posture / Offering Posture |
| `provenance` | Provenance & evidence |
| Out of scope / other systems | External Context |

File and YAML key names `service_attributes` were kept for
compatibility. Semantically they are posture, not a second catalog.

---

## Compatibility Baseline

### OSM-C-001 — Initial Compatibility Universe

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Compatibility
- **Decision:** The initial compatibility universe for 7lens OSM is:

  **A. Models / taxonomies / architectural frameworks**
  - TM Forum / TMF633 Service Catalog
  - ITIL
  - ServiceNow CSDM
  - ArchiMate
  - TOGAF
  - TBM (Technology Business Management)

  **B. Compliance / governance frameworks**
  - ISO/IEC 27001
  - ISO/IEC 27701
  - NIST CSF
  - GDPR
  - DORA
  - EU AI Act

  These items are the baseline **scope** for later analysis. 7lens OSM
  is designed to be compatible with this universe. This decision does
  **not** state that OSM is already compatible with any item, and it
  does **not** state regulatory compliance.

- **What this is not:** a mapping, a redesign, an attribute change, or
  a claim of certification.
- **Surfaces to update:**
  - [x] `COMPATIBILITY.md`
  - [x] `compatibility/` (one file per model)
  - [x] `compliance/` (one file per framework)
  - [x] `README.md` (name, positioning, pointer to this universe)
  - [x] `DECISIONS.md` (this record)
  - [ ] `schema/` — no change (OSM-C-001 is scope only)
  - [ ] `SPECIFICATION.md` — no model change
  - [ ] `examples/` — no model change
  - [ ] `validation/` — no rule change
- **Notes:** Individual analyses start at status `NOT ANALYZED`.
  Optional mapping fields already in the schema (TBM, TOGAF, ISO,
  NIST, GDPR, DORA, EU AI Act) remain illustrative until maintainers
  accept a mapping decision.
  Amended by **OSM-C-002** (PDMC removed) and **OSM-C-003** (CSDM
  retained). P0 accepted as documentation-only.

### OSM-C-002 — Remove PDMC from the compatibility universe

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Compatibility
- **Decision:** PDMC is removed from the 7lens OSM compatibility
  universe. It was introduced prematurely and ambiguously and is not
  an approved OSM compatibility target. It is not replaced by another
  model.
- **What this is not:** a model/schema/example change; a substitute
  mapping target.
- **Surfaces to update:**
  - [x] `compatibility/PDMC.md` — deleted
  - [x] `COMPATIBILITY.md`
  - [x] `DECISIONS.md` (this record)
  - [x] `README.md` — no PDMC references were present
  - [ ] `schema/` — no change
  - [ ] `examples/` — no change
  - [ ] `validation/` — no change
- **Notes:** Amends OSM-C-001.

### OSM-C-003 — Retain ServiceNow CSDM in the compatibility universe

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Compatibility
- **Decision:** ServiceNow CSDM remains in the compatibility universe.
  Although vendor-specific, it is sufficiently important in enterprise
  service management to justify compatibility analysis. OSM remains
  vendor-neutral; a later mapping would be a projection into CSDM,
  not an adoption of ServiceNow as the OSM metamodel.
- **What this is not:** a completed CSDM mapping; a decision to model
  business services or applications in OSM.
- **Surfaces to update:**
  - [x] `compatibility/SERVICENOW-CSDM.md` (universe confirmation only)
  - [x] `COMPATIBILITY.md` (CSDM already listed; retained)
  - [x] `DECISIONS.md` (this record)
  - [ ] `schema/` — no change
- **Notes:** Confirms OSM-C-001 with respect to CSDM. Analysis status
  is recorded in **OSM-C-005** (PARTIALLY COMPATIBLE / selective).

### OSM-C-004 — ITIL v5 selective compatibility

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Compatibility
- **Decision:** OSM is not an alternative implementation of ITIL.
  OSM is a small canonical core of technological services and
  offerings, mapped to ITIL and other frameworks, then to customer
  tools. ITIL v5 status is **PARTIALLY COMPATIBLE / SELECTIVE
  COMPATIBILITY**. OSM Service is conceptually compatible with ITIL
  Service but narrower (technological only). OSM Service Offering is
  compatible with the useful ITIL offering core (atomic
  requestable/deliverable variant). OSM Service and Offering records
  constitute the technological service catalogue; there is no
  ServiceCatalogue entity. OSM lifecycle (`version`, `valid_from`,
  `valid_to`, `lifecycle_state`) remains the definition lifecycle
  and is not ITIL lifecycle activities. Ownership stays
  `accountable` plus Technology Stack owner. ICT Provider remains
  compatible with relevant supplier/provider semantics. Digital
  Product, Business Service, outcomes, consumers, Value Streams,
  Service→Service relationships, CI/asset links, detailed SLA
  modelling, and ITIL practices stay **deliberately outside the
  current OSM core** (not recorded as missing capabilities).
  Service→Service is not a permanent rejection; reopen only if a
  concrete interoperability requirement appears. No OSM schema
  change in this decision.
- **What this is not:** an ITIL implementation; permission to add
  ITIL entities or role/supplier/SLA structures to OSM; a change to
  OSM-M-001–OSM-M-004.
- **Surfaces to update:**
  - [x] `compatibility/ITIL.md`
  - [x] `COMPATIBILITY.md`
  - [x] `README.md` (compatibility status)
  - [x] `SPECIFICATION.md` (canonical-core / boundary consistency)
  - [x] `MODEL.md` (deliberate exclusions consistency)
  - [x] `CONTRIBUTING.md` (out-of-scope boundaries)
  - [x] `DECISIONS.md` (this record)
  - [ ] `schema/` — no change
  - [ ] `examples/` — no change
  - [ ] `validation/` — no change
- **Notes:** Mapping path is OSM core → semantic mapping → ITIL /
  CSDM / ArchiMate / other frameworks → customer tools.

### OSM-C-005 — CSDM selective compatibility

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Compatibility
- **Decision:** OSM is not a CSDM implementation. CSDM status is
  **PARTIALLY COMPATIBLE / SELECTIVE COMPATIBILITY**. OSM Service
  conceptually maps to CSDM Technology Management Service but remains
  narrower and technology-focused. OSM Service Offering conceptually
  maps to CSDM Service Offering as an atomic requestable/deliverable
  technological variant; variation dimensions are not hard-coded.
  Service Instance, Business Service, Application Service, CMDB/CIs,
  Product Models and Value Streams stay **outside OSM**. Service →
  Service relationships stay outside the current OSM core (not a
  permanent rejection). Existing `accountable` / Service Owner
  semantics remain valid. Technology Provider information is supported
  through canonical ICT Provider references on Service and/or Offering
  (**OSM-M-006**). OSM maps into CSDM; it does not reproduce CSDM.
- **What this is not:** a ServiceNow metamodel; permission to add
  CSDM classes to OSM; a change to OSM-M-001–OSM-M-004 or OSM-C-004.
- **Surfaces to update:**
  - [x] `compatibility/SERVICENOW-CSDM.md`
  - [x] `COMPATIBILITY.md`
  - [x] `README.md`
  - [x] `SPECIFICATION.md`
  - [x] `MODEL.md`
  - [x] `CONTRIBUTING.md`
  - [x] `DECISIONS.md` (this record)
- **Notes:** Completes the analysis whose universe membership was
  retained by OSM-C-003.

### OSM-C-006 — ICT Provider semantics

- **Status:** ACCEPTED
- **Date:** 2026-09-13
- **Type:** Compatibility
- **Decision:** `providers` names the ICT Provider that materially
  delivers, operates, or underpins the technological Service or
  Service Offering. Use ICT Provider for that party. Do **not** use
  ICT Provider as a generic vendor, tool, or product inventory.
  A licensor is an ICT Provider only when it materially provides or
  underpins the Service/Offering. Generic software tools, products,
  suppliers, or commercial parties are not automatically ICT
  Providers. Do not introduce provider-role fields
  (`operator_provider`, `licensor_provider`, `vendor_role`,
  `provider_role`). Keep `Service.providers` and
  `ServiceOffering.providers`. If an offering is provider-specific,
  put the id on the Offering. If the provider is intrinsic to the
  whole Service, put it on the Service.
- **What this is not:** a new relationship; a DORA arrangement model;
  permission to list every brand in a technology chain.
- **Surfaces to update:**
  - [x] `SPECIFICATION.md`
  - [x] `MODEL.md`
  - [x] `models/` and `compliance/DORA.md`
  - [x] examples (provider placement; operator vs licensor notes)
  - [x] `DECISIONS.md` (this record)
- **Notes:** Clarifies OSM-M-006 / OSM-M-010. Does not change schema.

### OSM-C-007 — DORA arrangements remain external

- **Status:** ACCEPTED
- **Date:** 2026-09-13
- **Type:** Compatibility
- **Decision:** Do not introduce an Arrangement entity. Do not model
  the DORA register of information or contractual-arrangement
  structure inside OSM. Existing ICT Provider contract-related
  fields remain **characterization** of the provider record, not a
  DORA Arrangement model. DORA RoI remains EXTERNAL. The canonical
  OSM relationship is Service / Offering → ICT Provider. DORA
  reporting may consume or enrich that relationship **outside** OSM.
  OSM provider linkage is **not** a DORA RoI or
  contractual-arrangement model. `providers` is not
  `dora_third_party_deps`.
- **What this is not:** a claim that OSM satisfies DORA; permission
  to add LEI, CIF, RoI templates, or incident feeds.
- **Surfaces to update:**
  - [x] `compliance/DORA.md`
  - [x] `SPECIFICATION.md`
  - [x] `MODEL.md`
  - [x] `_internal/notes/COMPATIBILITY.md`
  - [x] `DECISIONS.md` (this record)
- **Notes:** Closes the OSM-M-005 *arrangement-entity* question as
  **rejected for OSM core**. Dual Service/Offering `providers`
  placement from OSM-M-010 remains. Grain vs RoI stays documented,
  not modelled.

### OSM-C-008 — Service→Service remains forbidden

- **Status:** ACCEPTED
- **Date:** 2026-09-13
- **Type:** Compatibility
- **Decision:** Service→Service dependency remains **forbidden**.
  Do not add `depends_on`, `depends_on_services`, `dependencies`,
  `service_dependencies`, `requires_service`, `consumes_service`, or
  a generic relationship mechanism that circumvents this rule.
  Frameworks that need service dependencies map them in an external
  integration layer. Canonical OSM relationships remain:
  Technology Stack → Service → Service Offering, and
  Service / Offering → ICT Provider.
- **What this is not:** a permanent metaphysical ban forever; a
  change to OSM-C-004 / OSM-C-005 except to **confirm** the
  exclusion after the 2026-09-13 compatibility investigation
  (GAP-002).
- **Surfaces to update:**
  - [x] `SPECIFICATION.md` / `MODEL.md` / `CONTRIBUTING.md`
  - [x] `models/`
  - [x] `DECISIONS.md` (this record)
- **Notes:** Confirms OSM-C-004 and OSM-C-005. No schema change.

### OSM-C-009 — Canonical concept first, framework mapping second

- **Status:** ACCEPTED
- **Date:** 2026-09-13
- **Type:** Compatibility
- **Decision:** Keep useful framework-specific mapping fields. They
  are mappings, not claims that OSM implements the framework.
  Canonical OSM concept first; framework mapping second. Do not
  duplicate canonical concepts under framework prefixes. Forbidden
  copies remain forbidden: `dora_rto`, `dora_rpo`,
  `dora_criticality` (as a *copy* of service criticality),
  `dora_resilience_tested`, `cloud_providers`, `services_consumed`,
  `dora_third_party_deps`. Stack `mappings.dora.criticality` stays a
  **different grain** (OSM-M-009).
- **What this is not:** deletion of existing mapping fields;
  certification or legal interpretation.
- **Surfaces to update:**
  - [x] `models/`, `compliance/`
  - [x] `SPECIFICATION.md`
  - [x] `_internal/notes/COMPATIBILITY.md`
  - [x] `DECISIONS.md` (this record)
- **Notes:** Applies OSM-M-008 to the post-investigation mapping
  documentation. Does not change schema.

### OSM-D-001 — Location / residency via characteristics

- **Status:** ACCEPTED
- **Date:** 2026-09-13
- **Type:** Documentation
- **Decision:** Do not add dedicated location/residency fields to the
  core schema. Represent region, geography, deployment_region,
  service_region, data_residency, processing_location,
  storage_location, and operating_region as **characteristics**.
  Processing location and storage location are **different**
  concepts; use distinct characteristic names. Do not collapse
  processing location, storage location, service availability
  region, and provider `headquarters`. Provider
  `data_processing_locations` is a **capability / possible
  location** list, not actual Service/Offering residency.
- **What this is not:** a Location entity; a schema change.
- **Surfaces to update:**
  - [x] `SPECIFICATION.md` §5.1
  - [x] `MODEL.md`
  - [x] `compliance/DORA.md`, `compliance/GDPR.md`
  - [x] `DECISIONS.md` (this record)
- **Notes:** GAP-001 and GAP-006 closed as documentation /
  characteristic convention.

### OSM-D-002 — Purpose as a characteristic

- **Status:** ACCEPTED
- **Date:** 2026-09-13
- **Type:** Documentation
- **Decision:** When an implementation needs a canonical purpose
  concept, use a characteristic named `purpose`. Do not add a
  top-level Service property. Purpose is generic and must not be
  framework-prefixed (`gdpr_purpose`, `iso27701_purpose`,
  `dora_purpose`, `ai_act_purpose` are not OSM fields). Frameworks
  map their terminology onto `purpose`. Existing
  `ai_act_intended_purpose` remains an EU AI Act **mapping** field
  on offering posture when `ai_act_applicable` is true; it is not a
  second canonical purpose.
- **What this is not:** a new entity or lifecycle object; deletion
  of `ai_act_intended_purpose`.
- **Surfaces to update:**
  - [x] `SPECIFICATION.md` §5.1
  - [x] `compliance/GDPR.md`, `compliance/ISO-27701.md`,
    `compliance/EU-AI-ACT.md`
  - [x] `DECISIONS.md` (this record)
- **Notes:** GAP-003. A first-class `purpose` field is a future
  option only if the characteristic proves load-bearing.

### OSM-D-003 — Privacy classification precedence

- **Status:** ACCEPTED
- **Date:** 2026-09-13
- **Type:** Documentation
- **Decision:** `privacy_classification` remains the canonical OSM
  high-level privacy classification. Keep `iso27701_pii_role` and
  related 27701/GDPR mapping fields as **compatibility
  representations**, not a PIMS or RoPA. Precedence: (1)
  `privacy_classification` = canonical OSM class; (2)
  framework-specific fields = mapping semantics. Do not create
  `gdpr_privacy_classification`, `iso27701_privacy_classification`,
  or `dora_privacy_classification`.
- **What this is not:** removal of mapping fields; a claim that OSM
  models all 27701 processing activities, legal bases, or contracts.
- **Surfaces to update:**
  - [x] `SPECIFICATION.md`
  - [x] `compliance/ISO-27701.md`, `compliance/GDPR.md`
  - [x] `DECISIONS.md` (this record)
- **Notes:** Does not change schema.
