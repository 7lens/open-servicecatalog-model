# DORA

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (compliance / governance)
- **OSM schema fields today:** canonical OSM posture and provider
  fields that a DORA conversation can use. DORA-specific remaining
  fields are not copies of those canonical facts.

DORA-oriented information in OSM is a **mapping onto canonical OSM
concepts** where the concept already exists (OSM-M-008). Named DORA
fields that remain are not copies of `rto`, `rpo`, service
criticality or provider association. They are **not** a DORA register
of information, not an ICT risk-management framework, and not a claim
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

The same pattern applies to operational criticality, resilience
testing and provider association:

```text
operational_criticality  →  DORA mapping
resilience_tested        →  DORA mapping
providers                →  DORA ICT third-party association
```

## 3. OSM concepts/attributes relevant to the framework

Present in the current schema (not yet analyzed as a mapping):

| OSM field | Where | Role |
|-----------|--------|------|
| `mappings.dora.pillar` | Technology Stack | Stack-level DORA label (mapping object) |
| `mappings.dora.criticality` | Technology Stack | Stack-level DORA label; **not** a copy of service criticality and **not** ICT Provider risk |
| `operational_criticality` | Service posture | Canonical service criticality; DORA maps here |
| `rto`, `rpo` | Offering posture | Canonical recovery objectives; DORA maps here |
| `resilience_tested`, `last_resilience_test`, `resilience_evidence` | Offering posture | Canonical resilience-test posture; DORA maps here |
| `providers` | Service and Service Offering | Canonical ICT Provider association; DORA maps here (OSM-M-010) |
| `risk_level` | ICT Provider | Canonical provider risk/severity (OSM-M-009); not service criticality |
| ICT Provider contract / risk / resilience fields | ICT Provider | Provider master data |
| `dora_notification_clause` | ICT Provider | DORA-specific contract flag; not a copy of another OSM fact |

There are no OSM fields named `dora_rto`, `dora_rpo`,
`dora_criticality`, `dora_resilience_tested` or
`dora_third_party_deps`. There is no ICT Provider `criticality`
field and no `services_consumed` reverse list.

## 4. Mapping opportunities

NOT YET ANALYZED.

The compatibility layer should continue to point DORA readers at
canonical `rto` / `rpo` / `operational_criticality` /
`resilience_tested` / `providers` rather than introducing parallel
fields.

## 5. Missing information

NOT YET ANALYZED.

DORA RTS register-of-information fields, entity identifiers, and
supervisory reporting layouts are not in OSM.

Canonical Service/Offering `providers` (**OSM-M-006**, **OSM-M-010**)
is who delivers or underpins the technological Service/Offering.
DORA uses that relationship. Reverse Provider → Service links are
derived from `providers`.

## 6. Potential extensions

None proposed. No attributes are added in this baseline. Do not add
DORA-prefixed copies of canonical OSM fields (OSM-M-008). Do not add
another provider relationship.

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
