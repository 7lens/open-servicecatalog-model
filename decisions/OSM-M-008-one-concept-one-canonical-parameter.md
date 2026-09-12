# OSM-M-008 — One Concept, One Canonical Parameter

- **Status:** ACCEPTED
- **Date:** 2026-09-12
- **Type:** Model
- **Register:** [`DECISIONS.md`](../DECISIONS.md)

## Decision

OSM MUST NOT represent the same semantic concept through multiple
canonical parameters.

Before introducing any new field, parameter, characteristic, or
mapping field, first verify whether the concept is already represented
elsewhere in the model.

If an existing OSM field already represents the concept, reuse that
field and express framework-specific semantics through mappings
rather than creating another representation of the same information.

Duplication is only justified when two fields represent genuinely
different semantic concepts or different grains — not merely because
a framework, provider, or standard uses a different name.

Genuinely different concepts may coexist even when they use similar
names, the same enum values, or appear related. Shared enum tokens
are not evidence that two fields are the same fact.

The default decision when two fields appear semantically equivalent
is **consolidation, not duplication**.

### Required check before any new field

1. Search the entire model for an existing representation of the concept.
2. Check schemas.
3. Check examples.
4. Check `MODEL.md`.
5. Check `SPECIFICATION.md`.
6. Check existing decisions.
7. Determine whether the apparent difference is actually semantic or
   merely terminology / framework-specific.
8. Only add a new field if there is a genuine semantic distinction.

The existence of a field in DORA, ISO 27001, ISO 27701, NIST, GDPR,
the EU AI Act, ITIL, CSDM, or TM Forum is **not** sufficient
justification for adding it to OSM.

```text
Does OSM already represent this concept?
        │
       YES
        │
        ▼
Reuse canonical OSM field
        │
        ▼
Document framework mapping
```

### Applied in this correction

Canonical:

```text
rto
rpo
providers
operational_criticality
resilience_tested
```

Removed as duplicate representations of those concepts:

```text
dora_rto
dora_rpo
dora_criticality
dora_resilience_tested
cloud_providers
```

DORA maps to canonical `rto` / `rpo` / `operational_criticality` /
`resilience_tested`. A cloud provider is an ICT Provider; association
is `providers`. No replacement fields are introduced.

`dora_third_party_deps` is retained pending **OSM-M-005**
(**PROPOSED**). Whether it is a genuinely different relationship from
canonical `providers` is an unresolved architectural question. Do
not collapse the two fields here.

## What this is not

A new taxonomy, a field-by-field redesign of OSM, permission to
rename `rto`, `rpo`, or `providers`, or a mandate to collapse
genuinely different grains or subjects.

## Surfaces updated

- `SPECIFICATION.md`
- `MODEL.md`
- `CONTRIBUTING.md`
- `COMPATIBILITY.md`
- `compliance/DORA.md`
- `schema/service-attributes.yaml`
- `examples/service-attributes.yaml`
- `validation/validate.py`
- `validation/README.md`
- `README.md`
- `decisions/OSM-M-007-complete-service-definition.md`
- `decisions/OSM-M-006-ict-provider-references.md`
- `DECISIONS.md`

## Notes

Complements OSM-M-004 (compatibility does not mean copying) and
OSM-M-007 (classification of candidate concepts). OSM-M-008 is the
anti-duplication rule: one authoritative fact, then mappings.
