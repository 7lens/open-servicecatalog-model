# OSM-M-005 — DORA provider-link grain (offering vs service)

- **Status:** PROPOSED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](../DECISIONS.md)

This record is extracted from the repository decision log. No
architectural content has been added beyond what was already
recorded. Status remains **PROPOSED**.

## Decision

Not decided. Two open questions remain, and neither is resolved here:

1. Grain: `dora_third_party_deps` is offering-level;
   `services_consumed` is service-level.
2. Relationship: whether `dora_third_party_deps` and canonical
   `providers` represent genuinely different relationships, or the
   same association under two names.

Maintainers will address both during DORA compliance analysis.
Until this decision is **ACCEPTED**, keep both fields as they are.

**Do not change schema, examples or validation for this decision
until it is ACCEPTED.** Do not collapse `dora_third_party_deps` into
`providers`, rename it, or add another provider relationship.

Canonical Service/Offering `providers` (**OSM-M-006**) is the
canonical who-delivers association. It does not, by itself, close
this DORA grain/relationship question.

## What this is not

An accepted model change.

## Surfaces to update

None until this decision is ACCEPTED.

## Notes

Logged during P0 as `OSM-M-001`. Renumbered to `OSM-M-005` when
7lens assigned OSM-M-001–OSM-M-004 to the TM Forum follow-up
decisions.
