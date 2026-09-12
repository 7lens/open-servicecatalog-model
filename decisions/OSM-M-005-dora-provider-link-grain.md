# OSM-M-005 — DORA provider-link grain (offering vs service)

- **Status:** SUPERSEDED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](../DECISIONS.md)
- **Superseded by:** [`OSM-M-010`](OSM-M-010-canonical-providers-relationship.md)

## Decision

Originally not decided. Two open questions were recorded:

1. Grain: `dora_third_party_deps` is offering-level;
   `services_consumed` is service-level.
2. Relationship: whether `dora_third_party_deps` and canonical
   `providers` represent genuinely different relationships, or the
   same association under two names.

**OSM-M-010** closes both questions. `providers` is the single
canonical Service / Offering → ICT Provider relationship. DORA uses
that field. `dora_third_party_deps` and `services_consumed` are
removed. Reverse Provider → Service links are derived from
`providers`.

## What this is not

An independent accepted model. See OSM-M-010.

## Surfaces to update

Named on OSM-M-010.

## Notes

Logged during P0 as `OSM-M-001`. Renumbered to `OSM-M-005` when
7lens assigned OSM-M-001–OSM-M-004 to the TM Forum follow-up
decisions. Superseded by OSM-M-010 under OSM-M-008.
