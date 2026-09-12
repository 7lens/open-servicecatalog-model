# 7lens OSM — Decision register

**Canonical name:** 7lens OSM  
**Expanded:** 7lens Open Service Catalog Model

This file is the **decision register** (index). Detailed model
decision documents live in [`decisions/`](decisions/).

```text
DECISIONS.md     Decision register / index
decisions/       Detailed architectural decisions
```

**Agents and contributors do not make architectural or model
decisions here.** They may only apply decisions whose status is
`ACCEPTED`. A `PROPOSED` decision is recorded, not implemented.

There was no prior numbering scheme in this repository. New IDs use:

| Prefix | Use |
|--------|-----|
| `OSM-C-nnn` | Compatibility universe and mapping decisions |
| `OSM-M-nnn` | Model / schema decisions |
| `OSM-D-nnn` | Documentation / naming decisions (none yet) |

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

---

## Model decisions

| ID | Decision | Status | Date | Document |
|----|----------|--------|------|----------|
| OSM-M-001 | Generic characteristics | ACCEPTED | 2026-09-12 | [`decisions/OSM-M-001-generic-characteristics.md`](decisions/OSM-M-001-generic-characteristics.md) |
| OSM-M-002 | Temporal semantics | ACCEPTED | 2026-09-12 | [`decisions/OSM-M-002-temporal-semantics.md`](decisions/OSM-M-002-temporal-semantics.md) |
| OSM-M-003 | Service is the stable definition | ACCEPTED | 2026-09-12 | [`decisions/OSM-M-003-service-definition.md`](decisions/OSM-M-003-service-definition.md) |
| OSM-M-004 | Best-of, not standards accumulation | ACCEPTED | 2026-09-12 | [`decisions/OSM-M-004-best-of-not-standards-accumulation.md`](decisions/OSM-M-004-best-of-not-standards-accumulation.md) |
| OSM-M-005 | DORA provider-link grain | PROPOSED | 2026-09-12 | [`decisions/OSM-M-005-dora-provider-link-grain.md`](decisions/OSM-M-005-dora-provider-link-grain.md) |
| OSM-M-006 | Canonical ICT Provider references | ACCEPTED | 2026-09-12 | [`decisions/OSM-M-006-ict-provider-references.md`](decisions/OSM-M-006-ict-provider-references.md) |
| OSM-M-007 | Complete Service Definition | PROPOSED | 2026-09-12 | [`decisions/OSM-M-007-complete-service-definition.md`](decisions/OSM-M-007-complete-service-definition.md) |

**OSM-M-007** is established as an architectural decision. Its
schema/model implementation has **not** been performed. Status
remains `PROPOSED` until maintainers accept it.

OSM-M-007 does not change the status of OSM-M-001–OSM-M-006.

---

## Terminology note (OSM-M-007 vs current repository)

OSM-M-007 formally distinguishes:

```text
SERVICE DEFINITION     What the service is
SERVICE POSTURE        How the service currently stands
EXTERNAL CONTEXT       Information owned by other models or systems
```

The **implemented** repository still uses older names for the same
separation of files:

| Current repository term | OSM-M-007 term |
|-------------------------|----------------|
| Catalog (`services.yaml`) | Service Definition |
| Health record / `service_attributes` / `offering_attributes` | Service Posture |
| Out of scope / other systems | External Context |

OSM-M-007 states that the existing attributes pattern supports the
distinction and that M-007 establishes it as a semantic principle
rather than merely a file-organization convention.

This register **does not rename** `service_attributes` or rewrite
`MODEL.md` / `SPECIFICATION.md` field tables. That is implementation
work after OSM-M-007 is accepted.

Provenance & evidence is a layer in OSM-M-007. It is not in the
current schema.

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
