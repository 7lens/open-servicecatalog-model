# DORA

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (compliance / governance)
- **OSM schema fields today:** several DORA-*named* fields on stacks,
  service attributes, offering attributes and ICT providers

DORA-named fields let a catalog **represent information that a DORA
conversation might use**. They are **not** a DORA register of
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

## 3. OSM concepts/attributes relevant to the framework

Present in the current schema (not yet analyzed as a mapping):

| OSM field | Where |
|-----------|--------|
| `mappings.dora.pillar` | Technology Stack |
| `mappings.dora.criticality` | Technology Stack |
| `dora_criticality` | Service attributes |
| `dora_rto`, `dora_rpo` | Offering attributes |
| `dora_third_party_deps` | Offering attributes |
| `dora_resilience_tested` | Offering attributes |
| ICT Provider contract / risk / resilience fields | ICT Provider |
| `dora_notification_clause` | ICT Provider |
| `services_consumed` | ICT Provider |

## 4. Mapping opportunities

NOT YET ANALYZED.

## 5. Missing information

NOT YET ANALYZED.

DORA RTS register-of-information fields, entity identifiers, and
supervisory reporting layouts are not in OSM.

There is a grain mismatch already visible and **not yet decided**:
`dora_third_party_deps` is offering-level; `services_consumed` is
service-level.

## 6. Potential extensions

None proposed. No attributes are added in this baseline.

## 7. Important caveats

- Field names that include `dora_` do not make a catalog DORA
  compliant.
- OSM is usable outside the financial sector; DORA does not apply
  to every adopter.
- This file is not legal advice, not an RTS mapping, and not a
  claim of compliance.

## 8. Status

**NOT ANALYZED**
