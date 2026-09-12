# OSM-M-002 — Temporal semantics

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](../DECISIONS.md)

This record is extracted from the repository decision log. No
architectural content has been added beyond what was already
accepted.

## Decision

Immutable identity ≠ immutable definition. Each Service has
`version`, `valid_from`, and optional `valid_to`. One catalog record
per service `id` is the current definition. OSM does not add
ServiceSpecification or TMF lifecycle/version machinery.

`lifecycle_state` is a required field on **Service** (not on
`service_attributes`). Offerings have no version or validity fields.

`lifecycle_state` enum: `draft` \| `pilot` \| `production` \|
`sunset` \| `retired`.

`valid_to: null` means still in force. If `valid_to` is set, it must
not be before `valid_from`. History of prior definitions is out of
band (for example git).

## What this is not

A composite `id`+`version` key; in-catalog history rows;
offering-level version/validity.

## Surfaces updated

- `schema/service.yaml`
- `schema/service-attributes.yaml` (`lifecycle_state` removed)
- `SPECIFICATION.md`
- `MODEL.md`
- `README.md`
- `examples/services.yaml`
- `examples/service-attributes.yaml`
- `validation/validate.py`
- `compatibility/TMFORUM-TMF633.md`
- `DECISIONS.md`

## Notes

Final 7lens instruction recorded with this decision: move
`lifecycle_state` onto Service and remove the duplicate from service
attributes.
