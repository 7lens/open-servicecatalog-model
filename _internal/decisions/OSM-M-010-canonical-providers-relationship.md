# OSM-M-010 — Canonical providers relationship

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](DECISIONS.md)

## Decision

`providers` is the **single canonical** Service / Service Offering →
ICT Provider relationship.

Remove:

```text
services_consumed
dora_third_party_deps
```

`services_consumed` is unnecessary reverse storage. Provider-to-Service
relationships are derived from canonical `providers` references. Do
not replace it with another reverse relationship.

`dora_third_party_deps` is removed because DORA does not justify
duplicating the canonical provider relationship. DORA-relevant
provider associations are expressed through `providers`. Do not
create another DORA-specific provider relationship.

OSM-M-008 (One Concept, One Canonical Parameter) is the governing
principle. Who provides a Service or Offering is one concept; it has
one canonical parameter: `providers`.

This decision **supersedes OSM-M-005**.

```text
Service / Offering
      ↓  providers (ids, optional, 0..n)
ICT Provider
```

Use Service-level `providers` when the provider is intrinsic to the
capability. Use Offering-level `providers` when provider choice
distinguishes the variant. Association remains optional. Multiple
ids remain allowed.

## What this is not

A new provider entity; a generic Service → Service relationship; a
DORA register of information; permission to add a reverse listing or
a DORA-prefixed copy of `providers`.

## Surfaces to update

- `schema/ict-provider.yaml`
- `schema/service.yaml`
- `schema/service-offering.yaml`
- `schema/service-attributes.yaml`
- `examples/ict-providers.yaml`
- `examples/services.yaml`
- `examples/service-attributes.yaml`
- `validation/validate.py`
- `validation/README.md`
- `SPECIFICATION.md`
- `MODEL.md`
- `README.md`
- `CONTRIBUTING.md`
- `COMPATIBILITY.md`
- `compatibility/SERVICENOW-CSDM.md`
- `compliance/DORA.md`
- `decisions/OSM-M-005-dora-provider-link-grain.md`
- `decisions/OSM-M-006-ict-provider-references.md`
- `decisions/OSM-M-008-one-concept-one-canonical-parameter.md`
- `DECISIONS.md`

## Notes

Final model correction before the current OSM architecture is
frozen. Complements OSM-M-006 (canonical ICT Provider references)
and OSM-M-008 (one concept, one canonical parameter).
