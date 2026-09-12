# OSM-M-005 — DORA provider-link grain (offering vs service)

- **Status:** PROPOSED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](../DECISIONS.md)

This record is extracted from the repository decision log. No
architectural content has been added beyond what was already
recorded. Status remains **PROPOSED**.

## Decision

Not decided. Observed mismatch: `dora_third_party_deps` is
offering-level; `services_consumed` is service-level. Maintainers
will address this during DORA compliance analysis.

**Do not change schema, examples or validation for this decision
until it is ACCEPTED.**

Canonical Service/Offering `providers` (**OSM-M-006**) is a separate
association and does not resolve this DORA grain question.

## What this is not

An accepted model change.

## Surfaces to update

None until this decision is ACCEPTED.

## Notes

Logged during P0 as `OSM-M-001`. Renumbered to `OSM-M-005` when
7lens assigned OSM-M-001–OSM-M-004 to the TM Forum follow-up
decisions.
