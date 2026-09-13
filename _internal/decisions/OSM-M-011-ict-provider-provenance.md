# OSM-M-011 — ICT Provider provenance (principle)

- **Status:** ACCEPTED (principle). Schema **not implemented**.
- **Date:** 2026-09-13
- **Type:** Model
- **Register:** [`DECISIONS.md`](DECISIONS.md)

## Decision

There is **one** OSM provenance mechanism: the reusable `provenance`
object already used on Service, Service Offering, service posture,
and offering posture.

ICT Provider facts (locations, certifications, contract flags,
`risk_level`) should use that same object. Do **not** create a
provider-specific provenance type. Do **not** introduce per-field
provenance.

## Schema status

`schema/catalog/ict-provider.yaml` sets `additionalProperties: false`
and does **not** currently include `provenance`.

This decision does **not** add the field. Adding `provenance` to ICT
Provider is the next small schema-evolution **candidate**.

### SCHEMA CHANGE CANDIDATE

- **Current limitation:** Provider master data cannot carry
  `authoritative_source`, `source_system`, `last_verified`,
  `evidence_reference`, `confidence`, or `discovery_method`.
- **Proposed change:** optional `$ref` to
  `schema/shared/provenance.yaml` on ICT Provider, same shape as
  Service.
- **Why documentation/characteristics are insufficient:** provenance
  is already a typed reusable structure; a free-text note would
  duplicate it (OSM-M-008).
- **Affected files:** `schema/catalog/ict-provider.yaml`,
  `SPECIFICATION.md` §7, `validation/validate.py`, examples.
- **Backwards compatibility:** additive optional field.
- **Example use:** evidence URL for a certification list; last
  verified date for `data_processing_locations`.
- **Recommendation:** implement only after an explicit schema-change
  instruction. Do not treat this file as that instruction.

## What this is not

Permission to add per-field provenance; a second provenance system;
implementation of the schema change in this documentation pass.

## Surfaces to update

- [x] `DECISIONS.md`
- [x] `SPECIFICATION.md` (candidate noted; field not added)
- [ ] `schema/catalog/ict-provider.yaml` — **not in this task**

## Notes

Investigation GAP-005. Complements OSM-M-007.
