# OSM-M-001 — Generic characteristics

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](DECISIONS.md)

This record is extracted from the repository decision log. No
architectural content has been added beyond what was already
accepted.

## Decision

OSM has a small nested characteristic structure on Service and
Service Offering. Characteristics are not a first-class catalog
entity and have no identifier. OSM does not reproduce the TM Forum
characteristic model.

The same schema is reused on Service and Offering. There is no
shared characteristic registry.

### Fields

| Field | Required | Notes |
|-------|----------|-------|
| `name` | yes | Unique within the parent. Lowercase snake_case. |
| `value_type` | yes | `string` \| `number` \| `boolean` \| `date` |
| `value` | no | Current value, when set. |
| `description` | no | |
| `allowed_values` | no | Closed list of permitted values. |
| `default_value` | no | |
| `min_cardinality` | no | Integer ≥ 0. |
| `max_cardinality` | no | Integer, or `null` if unbounded. |
| `constraints` | no | Optional `min`, `max`, and/or `pattern`. |
| `configurable` | no | `true` if a consumer may choose the value when requesting. |

Rules already enforced in the repository:

1. `name` is unique among characteristics of the same parent.
2. If `value` is set and `allowed_values` is non-empty, `value` must
   be a member of `allowed_values`.
3. If `max_cardinality` is set, it must be ≥ `min_cardinality`
   (omitted `min_cardinality` treated as 0).

## What this is not

A CharacteristicSpecification catalog; a TMF port; permission to
add arbitrary core fields.

## Surfaces updated

- `schema/characteristic.yaml`
- `schema/service.yaml`
- `schema/service-offering.yaml`
- `SPECIFICATION.md`
- `MODEL.md`
- `README.md`
- `examples/services.yaml`
- `validation/validate.py`
- `compatibility/TMFORUM-TMF633.md`
- `DECISIONS.md`

## Notes

Prefer a characteristic over a new core field when the property is
not needed by most adopters (also OSM-M-004).
