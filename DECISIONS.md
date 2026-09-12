# 7lens OSM — Decision log

**Canonical name:** 7lens OSM  
**Expanded:** 7lens Open Service Catalog Model

This log records maintainer decisions. It is the input to any later
propagation across schema, specification, README, examples,
compatibility files, compliance files and validation.

**Agents and contributors do not make architectural or model
decisions here.** They may only apply decisions whose status is
`ACCEPTED`.

There was no prior numbering scheme in this repository. New IDs use:

| Prefix | Use |
|--------|-----|
| `OSM-C-nnn` | Compatibility universe and mapping decisions |
| `OSM-M-nnn` | Model / schema decisions (none yet) |
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
  - [ ] schema/
  - [ ] SPECIFICATION.md
  - [ ] MODEL.md
  - [ ] README.md
  - [ ] examples/
  - [ ] compatibility/
  - [ ] compliance/
  - [ ] validation/
  - [ ] DECISIONS.md (this file)
- Notes:
```

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

The next human-led step after OSM-C-001 is comparison and decision
making (P1+). That work is not started here.

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
  - PDMC (working identification: Practical Data Model for CMDB;
    confirm if another public service-model reference was intended)

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
