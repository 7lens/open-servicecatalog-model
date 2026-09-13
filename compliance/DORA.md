# DORA

OSM is **not** a DORA register of information, an ICT risk-management
framework, or a claim of compliance with Regulation (EU) 2022/2554.

The Digital Operational Resilience Act sets operational-resilience
obligations for certain financial entities and their ICT providers.
OSM is usable outside the financial sector; DORA does not apply to
every adopter.

Where DORA talks about recovery, criticality, testing or third
parties, it maps onto **canonical OSM fields**. OSM does not
redefine those fields for DORA, and it does not duplicate them
under DORA-prefixed names.

```text
rto, rpo                     →  recovery objectives
operational_criticality      →  service criticality
resilience_tested            →  resilience-test posture
providers                    →  ICT third-party association
```

## What maps

| OSM field | Where | Role |
|-----------|--------|------|
| `rto` | Offering posture | Recovery Time Objective |
| `rpo` | Offering posture | Recovery Point Objective |
| `resilience_tested`, `last_resilience_test`, `resilience_evidence` | Offering posture | Resilience-test posture |
| `operational_criticality` | Service posture | Canonical service criticality |
| `providers` | Service / Offering | Canonical ICT Provider association |
| `risk_level` | ICT Provider | Canonical provider risk/severity — not service criticality |
| `mappings.dora.pillar` | Technology Stack | Stack-level DORA pillar label |
| `mappings.dora.criticality` | Technology Stack | Stack-level DORA label — **not** a copy of service criticality, **not** ICT Provider `risk_level` |
| `dora_notification_clause` | ICT Provider | Contract flag specific to DORA notification |
| ICT Provider contract / risk / exit fields | ICT Provider | Provider master data |

`mappings.dora.criticality` and `operational_criticality` are
different grains: stack label versus service criticality.

Reverse Provider → Service links are derived from `providers`.

## What stays in DORA / supervisory reporting

- RTS register-of-information layouts
- entity identifiers and filing formats
- a complete ICT risk-management framework

A field name that includes `dora_` does not make a catalog DORA
compliant. Canonical `rto` and `rpo` keep their OSM meaning.

Exact field definitions are in
[`SPECIFICATION.md`](../SPECIFICATION.md).
