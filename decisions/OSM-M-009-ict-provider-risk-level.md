# OSM-M-009 — ICT Provider risk_level

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](../DECISIONS.md)

## Decision

ICT Provider has **`risk_level`**, not `criticality`.

`risk_level` is the canonical assessment of ICT Provider
risk/severity (`low` \| `medium` \| `high` \| `critical`, or `null`
if not assessed). Do not introduce another provider criticality
field.

`operational_criticality` on Service Posture remains the canonical
service criticality. Stack `mappings.dora.criticality` remains a
stack-level DORA label at a different grain. Those fields are not
provider risk and are unchanged.

OSM-M-008 (One Concept, One Canonical Parameter) is the governing
principle. Provider importance/severity is one concept; it has one
canonical parameter: `risk_level`.

Removed:

```text
ICT Provider criticality
```

No replacement field is introduced.

## What this is not

Permission to add `dora_criticality`, `provider_criticality`, or any
other provider severity field. A change to service
`operational_criticality` or stack `mappings.dora.criticality`.

## Surfaces to update

- `schema/ict-provider.yaml`
- `examples/ict-providers.yaml`
- `validation/validate.py`
- `validation/README.md`
- `SPECIFICATION.md`
- `MODEL.md`
- `README.md`
- `CONTRIBUTING.md`
- `compliance/DORA.md`
- `DECISIONS.md`

## Notes

Final model correction before the current OSM architecture is
frozen. Complements OSM-M-008.
