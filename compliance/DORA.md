# DORA

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (compliance / governance)
- **OSM schema fields today:** canonical OSM posture and provider
  fields that a DORA conversation can use, plus a small number of
  DORA-specific listings that are not copies of those fields

DORA-oriented information in OSM is a **mapping onto canonical OSM
concepts** where the concept already exists (OSM-M-008). Named DORA
fields that remain are not copies of `rto`, `rpo`, criticality or
provider association. They are **not** a DORA register of
information, not an ICT risk-management framework, and not a claim
that OSM or any adopter complies with Regulation (EU) 2022/2554.

## 1. Framework overview

The Digital Operational Resilience Act (DORA) sets operational
resilience obligations for certain financial entities and their ICT
providers, including ICT risk management, incident management,
resilience testing and third-party risk.

## 2. Relevant scope for technological services

Later analysis should ask which catalog and provider facts are
useful for DORA-oriented operations (criticality, RTO/RPO, third
parties) while remaining honest that OSM is not a regulatory filing
format.

Canonical OSM recovery objectives (`rto`, `rpo`) are not redefined
to accommodate DORA. DORA maps to those fields.

```text
OSM canonical concept
        │
        ├── rto
        └── rpo
              │
              ▼
        DORA mapping
```

The same pattern applies to operational criticality and resilience
testing:

```text
operational_criticality  →  DORA mapping
resilience_tested        →  DORA mapping
providers                →  canonical ICT Provider association
```

## 3. OSM concepts/attributes relevant to the framework

Present in the current schema (not yet analyzed as a mapping):

| OSM field | Where | Role |
|-----------|--------|------|
| `mappings.dora.pillar` | Technology Stack | Stack-level DORA label (mapping object) |
| `mappings.dora.criticality` | Technology Stack | Stack-level DORA label; **not** a copy of service criticality |
| `operational_criticality` | Service posture | Canonical service criticality; DORA maps here |
| `rto`, `rpo` | Offering posture | Canonical recovery objectives; DORA maps here |
| `resilience_tested`, `last_resilience_test`, `resilience_evidence` | Offering posture | Canonical resilience-test posture; DORA maps here |
| `dora_third_party_deps` | Offering attributes | DORA-oriented listing. Relationship to canonical `providers` is unresolved (OSM-M-005, PROPOSED). |
| ICT Provider contract / risk / resilience fields | ICT Provider | Provider master data |
| `dora_notification_clause` | ICT Provider | DORA-specific contract flag; not a copy of another OSM fact |
| `services_consumed` | ICT Provider | Register reverse list |
| `providers` | Service and Service Offering | Canonical ICT Provider ids |

There are no OSM fields named `dora_rto`, `dora_rpo`,
`dora_criticality` or `dora_resilience_tested`.

## 4. Mapping opportunities

NOT YET ANALYZED.

The compatibility layer should continue to point DORA readers at
canonical `rto` / `rpo` / `operational_criticality` /
`resilience_tested` rather than introducing parallel fields.

## 5. Missing information

NOT YET ANALYZED.

DORA RTS register-of-information fields, entity identifiers, and
supervisory reporting layouts are not in OSM.

There is a grain mismatch already visible and **not yet decided**
(**OSM-M-005**, status **PROPOSED**): `dora_third_party_deps` is
offering-level; `services_consumed` is service-level. It is also
still open whether `dora_third_party_deps` and canonical `providers`
are genuinely different relationships. Do not change, collapse,
rename or replace those fields until OSM-M-005 is accepted.

Canonical Service/Offering `providers` (**OSM-M-006**) is who
delivers or underpins the technological Service/Offering. That
association does not, by itself, close OSM-M-005.

## 6. Potential extensions

None proposed. No attributes are added in this baseline. Do not add
DORA-prefixed copies of canonical OSM fields (OSM-M-008).

## 7. Important caveats

- Field names that include `dora_` do not make a catalog DORA
  compliant.
- OSM is usable outside the financial sector; DORA does not apply
  to every adopter.
- This file is not legal advice, not an RTS mapping, and not a
  claim of compliance.
- Canonical `rto` and `rpo` keep their OSM meaning. DORA does not
  redefine them.

## 8. Status

**NOT ANALYZED**
