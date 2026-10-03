# DORA

**Mapped version:** Regulation **(EU) 2022/2554** (applicable
17 January 2025), plus **Delegated Regulation (EU) 2024/1773** (RTS
on contractual arrangements for ICT services supporting critical or
important functions) and **Implementing Regulation (EU) 2024/2956**
(ITS templates for the **register of information**, Art. 28(3)).
Other DORA RTS/ITS (ICT risk management, incident reporting, TLPT)
exist; they stay **EXTERNAL** unless a fact already maps to
canonical OSM posture.

> **Mapping basis (2026-06-11):** the three regulation identifiers
> are confirmed against EUR-Lex. The base act is Regulation (EU)
> 2022/2554 (DORA)
> ([EUR-Lex ELI](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)).
> The RTS on contractual arrangements for ICT services supporting
> critical or important functions is Commission Delegated Regulation
> (EU) 2024/1773
> ([EUR-Lex ELI](https://eur-lex.europa.eu/eli/reg_del/2024/1773/oj)).
> The ITS on standard templates for the register of information
> (Art. 28(3)) is Commission Implementing Regulation (EU) 2024/2956
> of 29 November 2024
> ([EUR-Lex ELI](https://eur-lex.europa.eu/eli/reg_impl/2024/2956/oj)).
> Source wording was rephrased for licensing compliance.

**Status:** **PARTIAL**

OSM is **not** a DORA register of information, an ICT
risk-management framework, or a claim of compliance with
2022/2554.

**OSM provider linkage is not a DORA RoI or contractual-arrangement
model.**

Three different objects:

| Object | Where it lives |
|--------|----------------|
| OSM **ICT Provider** + `providers` | OSM core. Canonical technology-service-to-provider relationship. |
| DORA **contractual arrangement** | **EXTERNAL**. RTS 2024/1773. Not an OSM Arrangement entity (**OSM-C-007**). |
| DORA **register of information (RoI)** | **EXTERNAL**. ITS 2024/2956 templates. Supervisory reporting may *consume* OSM `providers`; OSM is not the RoI. |

`providers` is **not** `dora_third_party_deps`. That prefixed field
must remain removed. The canonical relationship is simply
`providers`, with DORA interpretation around it.

Where DORA talks about recovery, criticality, testing or third
parties, it **maps onto canonical OSM fields**. OSM does not
redefine those fields for DORA, and it does not duplicate them
under DORA-prefixed names (`dora_rto`, `dora_rpo`,
`dora_criticality` as a copy of service criticality,
`dora_resilience_tested`, `cloud_providers`, `services_consumed`
are forbidden).

```text
rto, rpo                     →  recovery objectives (framework interpretation around OSM)
operational_criticality      →  service criticality (map DORA CIF criticality *onto* this; do not copy)
resilience_tested            →  resilience-test posture
providers                    →  ICT third-party association (feeds RoI; is not RoI)
```

## Mapping table

The rows below walk DORA's own top-level structure — its five
pillars (ICT risk management, incident management/reporting,
digital-operational-resilience testing, ICT third-party risk,
information/intelligence sharing) plus the register-of-information
and contractual machinery — and give each a status from the index
vocabulary (MAPPED / PARTIAL / EXTERNAL / NOT IN SCOPE / FUTURE /
OPTIONAL), so no top-level DORA concept is silently missing. OSM is
narrow by design: it maps the third-party and resilience-posture
facts that already have canonical homes and marks the rest EXTERNAL.

| External concept (DORA) | OSM target | Grain | Status + kind | Outside OSM |
|-------------------------|------------|-------|---------------|-------------|
| ICT third-party provider of an ICT service (Chapter V) | `providers` → ICT Provider | Service and/or Offering | **MAPPED** — canonical OSM relationship. Operator/deliverer/underpinning party (**OSM-C-006**). | LEI, legal parent, CIF register |
| Contractual arrangement / RoI row (Art. 28–30) | — | Arrangement | **EXTERNAL** (**OSM-C-007**). Provider `contract_*` fields are **characterization**, not an Arrangement model. | RTS 2024/1773 structure; ITS 2024/2956 templates |
| Recovery time / point (business continuity, Art. 11–12) | `rto`, `rpo` | Offering posture | **MAPPED** — canonical OSM; DORA *interprets* them. | DORA-prefixed copies |
| Service / function criticality (critical or important function) | `operational_criticality` | Service posture | **PARTIAL** — canonical OSM. DORA CIF criticality maps **onto** this where applicable. | Function register |
| Stack DORA labels | `mappings.dora.pillar`, `mappings.dora.criticality` | Stack | **MAPPED** — informal **stack** labels. `standard` is an OSM enum token, **not** a DORA CIF class. Different grain from service criticality and provider `risk_level`. | Supervisory criticality of a CIF |
| Provider risk | `risk_level` | ICT Provider | **MAPPED** — canonical provider risk/severity. | Concentration models beyond the flag |
| Notification clause | `dora_notification_clause` | ICT Provider | **PARTIAL** — contract **flag** specific to DORA wording. | Full contract |
| Process vs store location (RTS “processed and stored”) | characteristics `processing_location` / `storage_location` | Offering (actual) vs Provider `data_processing_locations` (capability) | **MAPPED** — convention (**OSM-D-001**). No new schema fields. | RoI location columns |
| Resilience / threat-led penetration testing (Chapter IV, TLPT) | `resilience_tested` | Offering posture | **PARTIAL** — a boolean resilience-test posture flag only; OSM does not model TLPT scope, scenarios or results. | TLPT programme, test reports |
| ICT risk-management framework (Chapter II) | — | — | **EXTERNAL** — governance/control framework, not a catalog object. | ICT risk-management framework |
| ICT-related incident management & reporting (Chapter III) | — | — | **EXTERNAL** — incident classification/notification process. | Incident feed, major-incident reports |
| Information & intelligence sharing (Art. 45) | — | — | **NOT IN SCOPE** — threat-intel exchange arrangement, outside OSM's catalog boundary. | Threat-intel sharing |
| Legal Entity Identifier | — | — | **EXTERNAL** | LEI model |

Reverse Provider → Service links are derived from `providers`.

## ICT Provider contract fields

Existing fields such as `contract_ref`, `contract_start`,
`contract_end`, `notice_period_days`, `audit_rights`,
`subcontracting_allowed`, `subcontractors`,
`exit_strategy_documented` remain **characterization** of the
provider record. They are **not** a DORA Arrangement model.

## What stays in DORA / supervisory reporting (**EXTERNAL**)

- RoI
- LEI
- CIF register
- contractual Arrangement entity
- incident reporting model / incident feed
- RTS/ITS filing formats

A field name that includes `dora_` does not make a catalog DORA
compliant. Canonical `rto` and `rpo` keep their OSM meaning.

Exact field definitions are in
[`SPECIFICATION.md`](../SPECIFICATION.md).
