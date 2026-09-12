# OSM-M-004 — Best-of, not standards accumulation

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](../DECISIONS.md)

This record is extracted from the repository decision log. No
architectural content has been added beyond what was already
accepted.

## Decision

OSM incorporates useful semantics from existing models where they
materially improve interoperability, governance or
machine-readability, and avoids wholesale reproduction. Compatibility
does not mean copying.

Additions must keep OSM small, understandable, vendor-neutral,
machine-readable, opinionated, extensible and easy to implement.

## What this is not

A mandate to import TMF, ITIL, CSDM, ArchiMate, TOGAF or TBM
structures by default.

## Surfaces updated

- `SPECIFICATION.md`
- `MODEL.md`
- `README.md`
- `COMPATIBILITY.md`
- `compatibility/TMFORUM-TMF633.md`
- `CONTRIBUTING.md`
- `DECISIONS.md`

## Notes

Governing principle for future `OSM-M-*` proposals, including
OSM-M-007. OSM-M-008 adds the field-level rule: one concept, one
canonical parameter.
