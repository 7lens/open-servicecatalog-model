# 08 — Investigation summary

**Date:** 2026-09-13  
**Object tested:** frozen OSM 1.3.0  
**Universe:** OSM-C-001 (six models + six compliance frameworks), revalidated against current official versions  
**Model changes in this investigation:** none

> **Later the same day:** maintainers accepted OSM-C-006–C-009,
> OSM-D-001–D-003, OSM-M-011 (principle only). Public mapping
> documents were rewritten. GAP dispositions are in
> [05-gap-register.md](05-gap-register.md). This summary remains
> the investigation-time conclusion.

---

## Executive conclusion

**The current OSM core is semantically sufficient to act as the canonical technological-service core across this universe — with important caveats.**

It already holds, once each, the facts that independently recur: a stable technological-service **definition**, a requestable **variant**, **accountability**, **who provides**, **definition lifecycle**, **service-level expectations**, **recovery objectives**, **posture vs definition**, **trust metadata**, and **optional translation tags**.

It is **not** sufficient as a substitute for any of the twelve external systems (TMF catalog API, ITIL operating model, CSDM/CMDB, EA repository, TBM engine, ISMS, PIMS, CSF profile, RoPA, DORA register of information, AI Act technical file). Several **mapping documents are version-stale or too thin**, and a small set of **candidate canonical semantics** should be reviewed before anyone treats the freeze as “mapping-complete”.

The investigation identified **seven gap candidates**. Only **GAP-005 (provenance on ICT Provider)** and **GAP-003 (unprefixed purpose)** plus **GAP-001 (storage vs processing location)** are serious as *canonical* holes. **GAP-002 (Service→Service)** is the serious *relationship* hole and should stay closed unless an interoperability project reopens OSM-C-004. **DORA arrangement grain (OSM-M-005 remainder)** is the serious *unresolved question* and must not be mistaken for a solved decision.

This is not a finding that “no changes are required”. It is a finding that **the core should not be grown to match frameworks**, and that **documentation and a short decision queue matter more than new entities**.

---

### Strongly covered

- Technology Stack → Service → Service Offering as the only catalog nesting
- Service as **definition** (TMF spec role, CSDM TMS, not an instance)
- Offering as requestable **variant** (ITIL/CSDM offering core; dimensions via characteristics)
- `providers` as the single who-provides relationship (ITIL supplier, CSDM Technology Provider, DORA ICT TPP join, ArchiMate actor)
- Temporal identity (TMF version/validity; not ITIL activity lifecycle)
- Canonical resilience and criticality (`rto`/`rpo`/`resilience_*`/`operational_criticality`) with DORA/ISO/NIST mapping **onto** them (OSM-M-008)
- Data vs security classification as distinct facts
- Provenance on catalog and posture records
- Deliberate exclusion of instance, business service, digital product, consumers, CMDB, SLA objects

### Covered but mapping/documentation needs work

- ArchiMate 4 (public file still says Technology Service)
- ITIL Version 5 product/service lifecycle vs OSM `lifecycle_state`
- CSDM 5 Service Instance rename
- TBM Taxonomy 5.0.1 Resource Tower names and Solutions vs Stack grain
- TOGAF 10th Edition + example “Security Architecture”
- ISO 27701:2025 standalone PIMS vs 2019 extension story
- ISO 27001 dual grain/type control fields
- NIST Functions duplicated on stack and offering; invented `nist_control_status`
- GDPR locators overlapping privacy_classification / 27701 role
- DORA RTS/ITS, arrangement grain, `pillar`/`standard` tokens
- AI Act enum vs legal taxonomy; 2026 guidance and Omnibus dates
- When to use Service-level vs Offering-level `providers`

### Correctly external

- Runtime / Service Instance / TMF638
- Digital Product, Business Service, value streams, consumers
- TMF Catalog/Candidate/Category, CFS/RFS
- EA viewpoints and ArchiMate relationship graphs
- TBM allocation / Consumer Layer
- ISMS, PIMS, CSF profiles, RoPA, DORA RoI, AI Act conformity file/GPAI regime
- Service→Service **for now** (confirmed exclusion, not “missing because we forgot”)

### Potential OSM gaps

See [05-gap-register.md](05-gap-register.md). Headline:

| ID | Concept | Suggested posture |
|----|---------|-------------------|
| GAP-001 | Storage location ≠ processing location | Characteristic convention now; schema later if needed |
| GAP-002 | Service→Service dependency | **Defer / keep forbidden** |
| GAP-003 | Canonical purpose | Characteristic now; unprefixed field later |
| GAP-004 | Provider legal parent | **External**; document collapse |
| GAP-005 | Provenance on ICT Provider | **Best small schema candidate** after unfreeze |
| GAP-006 | Actual offering residency vs provider capability | Characteristics (already possible) |
| GAP-007 | Arrangement entity | **Reject**; contract fields are hints |

### Existing mappings that should be reconsidered

- ArchiMate Technology Service landing
- TBM “IT Tower” wording and example tower names
- Stack DORA `pillar` and `criticality: standard`
- `nist_control_status` as if CSF certified controls
- Stack GDPR article trivia
- `iso27701_*` names for GDPR-shared concepts
- AI Act risk-class enum as legal taxonomy
- ISO 27001 free-text vs list duplication
- Any example that fills mapping fields as if they were assessments

### Frameworks where current **public** analysis is insufficient

All twelve public files are **too thin** for the depth this investigation required. Worst currentness failures: **ArchiMate**, **ISO 27701**, **TBM**, **EU AI Act**, **DORA (RTS/ITS)**. TMF/ITIL/CSDM public files are directionally right and still under-versioned.

This package is the deep analysis. Public `models/` and `compliance/` were **not** rewritten here (to avoid silently accepting mappings).

### Decisions that should NOT yet be made

- Adding Service Instance, Digital Product, Arrangement, RoPA, or RoI entities
- Importing ITIL 8-activity or CSDM stage enums
- Adding TMF relationship types or CFS/RFS
- Adding NIST Categories or ISO control-implementation objects
- Adding AI Act deployer/GPAI/Annex III structures
- Resolving D1 by creating a third provider relationship
- Unfreezing the architecture solely because a framework has a field with a similar name

---

## Confidence table

| Area | Current confidence | Key issue | Human decision |
| --------- | -----------------: | --------- | -------------- |
| TMF633 | High | Production is v4.0.0; v5 preproduction ignored; OSM-M-001–004 still hold | DOC-1 only unless TMF v5 production lands |
| ITIL v5 | High | Product/service lifecycle ≠ OSM definition lifecycle; Digital Product correctly external | Confirm OSM-C-004; DOC-3 |
| CSDM 5 | High | Service vs **Service Instance** is clear and matches OSM; public file under-cites v5 | DOC-4 |
| ArchiMate | Medium | **v4 generic Service**; public mapping outdated | DOC-2; no schema |
| TOGAF | Medium | `togaf_domain` is a weak free-text hint; examples use non-standard domain | D6 |
| TBM | Medium | Taxonomy **5.0.1**; Stack vs Solutions grain | D7 |
| ISO 27001 | High | Control IDs are the right join; dual fields; not an ISMS | Document C-DUP-1; no control objects |
| ISO 27701 | Medium | **2025 standalone**; role grain vs activity | D2 |
| NIST CSF | High | Functions OK; Categories/Profiles correctly out; `nist_control_status` is the weak field | D8 |
| GDPR | Medium | Locators useful; RoPA correctly out; overlap + DPA boolean | D3 |
| DORA | Medium | Canonical rto/rpo/criticality/providers mapping is right; **arrangement grain and RoI remain open** | **D1 (do not resolve as schema now)** |
| EU AI Act | Medium | Applicability locator OK; enum and purpose prefix not the Act; GPAI/deployer correctly out | D10, D11; DOC-8 |

---

## OSM-M-005 (explicit)

OSM-M-010 **superseded** OSM-M-005 on **duplication**. Evidence in 03 §5:

- OSM may attach providers at **Service** (intrinsic) and **Offering** (variant). Both remain valid.
- DORA needs **contractual arrangement × ICT service × (external) function × ranked chain × legal persons**.
- Therefore `providers` is a **necessary join**, not a **sufficient DORA model**.

Maintainers should **minute** that the grain question is **open and accepted as open**, not silently treat SUPERSEDED as “settled”.

---

## Validation of this task

See the following section in the agent report after running validation: no schema/spec/example/decision edits; artefacts isolated under `_internal/compatibility-review/`.
