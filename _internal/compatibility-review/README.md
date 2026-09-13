# Compatibility and semantic sufficiency investigation

**Date:** 2026-09-13  
**Object under test:** frozen OSM 1.3.0 as implemented in this repository  
**Investigation constraint:** no schema, specification, MODEL, validation, example, or accepted-decision changes *during the investigation*

This folder is **research**. It is not public OSM documentation.
Version findings in [01-source-register.md](01-source-register.md)
remain the source of truth for framework editions.

A later documentation pass (same date) applied the accepted
decisions OSM-C-006–C-009, OSM-D-001–D-003, OSM-M-011 (principle
only) to public `models/`, `compliance/`, specification, and
examples. Schema remains frozen. ICT Provider `provenance` is a
recorded schema-change **candidate**, not implemented.

Public mapping files under `models/` and `compliance/` were
**rewritten after** this investigation. Quality findings in 06 that
refer to pre-pass public wording are **historical**.

| File | Purpose |
|------|---------|
| [00-baseline.md](00-baseline.md) | Repository and OSM model inventory |
| [01-source-register.md](01-source-register.md) | Authoritative versions and sources used |
| [02-model-mapping-matrix.md](02-model-mapping-matrix.md) | TMF633, ITIL v5, CSDM 5, ArchiMate 4, TOGAF 10, TBM 5.0.1 |
| [03-compliance-mapping-matrix.md](03-compliance-mapping-matrix.md) | ISO 27001, ISO 27701:2025, NIST CSF 2.0, GDPR, DORA, EU AI Act |
| [04-cross-framework-convergence.md](04-cross-framework-convergence.md) | Concepts that independently recur |
| [05-gap-register.md](05-gap-register.md) | Gap candidates that passed the eight-test filter |
| [06-risk-and-contradiction-register.md](06-risk-and-contradiction-register.md) | Duplications, outdated mappings, wrong grains |
| [07-recommendations.md](07-recommendations.md) | Decision queue with trade-offs — start here for human review |
| [08-investigation-summary.md](08-investigation-summary.md) | Executive conclusion |

Public mapping files under `models/` and `compliance/` were **revalidated**, not rewritten. Quality findings are in 06 and recommended documentation updates are in 07.
