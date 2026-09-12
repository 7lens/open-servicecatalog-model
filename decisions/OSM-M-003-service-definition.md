# OSM-M-003 — Service is the stable definition

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](../DECISIONS.md)

This record is extracted from the repository decision log. No
architectural content has been added beyond what was already
accepted.

## Decision

An OSM Service is the stable definition of a technological service —
the useful semantic role of TMF ServiceSpecification — without
introducing that entity. A Service is not merely a catalog entry or
availability record, and it is not a running instance.

Hierarchy remains:

**Technology Stack → Service → Service Offering**

## What this is not

A new entity; a TMF catalog tree; an instance or inventory object.

## Surfaces updated

- `SPECIFICATION.md`
- `MODEL.md`
- `README.md`
- `schema/service.yaml` (comments)
- `compatibility/TMFORUM-TMF633.md`
- `DECISIONS.md`

## Notes

Documentation and comments only, plus the fields from OSM-M-001 and
OSM-M-002.

OSM-M-007 (PROPOSED) builds on this decision: it does not replace
the “Service is the stable definition” architecture; it completes
the definition. Schema implementation of OSM-M-007 has not been
performed.
