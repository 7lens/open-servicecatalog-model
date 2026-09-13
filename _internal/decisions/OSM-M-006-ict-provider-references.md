# OSM-M-006 — Canonical ICT Provider references on Service and Offering

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](DECISIONS.md)

This record is extracted from the repository decision log. No
architectural content has been added beyond what was already
accepted.

## Decision

Vendor / cloud / technology provider information is part of the
canonical technological-service definition. Service and Service
Offering may each optionally list `providers`: ICT Provider **ids**
(0..n).

Use Service-level association when the provider is intrinsic to the
Service; use Offering-level association when provider choice
distinguishes the variant. Association is not required. Multiple ids
are allowed.

Do not embed ICT Provider master data on Service or Offering. Do not
add a provider-role taxonomy (primary / secondary / subcontractor /
reseller).

`providers` is not a generic Service → Service relationship.
DORA copies of canonical recovery, criticality or testing fields are
not OSM fields (OSM-M-008). DORA provider association is `providers`
(OSM-M-010). ICT Provider remains the single canonical provider
entity; no new Provider type and no `cloud_providers` list. Provider
risk/severity is `risk_level` (OSM-M-009); there is no provider
`criticality` field.

```text
Service / Offering
      ↓  providers (ids, optional, 0..n)
ICT Provider
```

## What this is not

A CSDM Technology Provider CI; a new entity; a DORA-prefixed copy of
`providers`. Amended by **OSM-M-010** (`dora_third_party_deps` and
`services_consumed` removed) and **OSM-M-009** (provider
`criticality` removed).

## Surfaces updated

- `schema/service.yaml`
- `schema/service-offering.yaml`
- `schema/ict-provider.yaml` (comments)
- `schema/service-attributes.yaml`
- `examples/services.yaml`
- `examples/ict-providers.yaml`
- `examples/service-attributes.yaml`
- `validation/validate.py`
- `validation/README.md`
- `SPECIFICATION.md`
- `MODEL.md`
- `README.md`
- `COMPATIBILITY.md`
- `compatibility/SERVICENOW-CSDM.md`
- `compliance/DORA.md`
- `DECISIONS.md`

## Notes

Accepted with CSDM analysis OSM-C-005. Keep OSM small. OSM-M-010
closes the former OSM-M-005 question: DORA uses `providers`.
