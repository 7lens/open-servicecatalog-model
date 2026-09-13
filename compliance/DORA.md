# DORA

**Mapped version:** Regulation **(EU) 2022/2554** (applicable
17 January 2025), plus **Delegated Regulation (EU) 2024/1773** (RTS
on contractual arrangements for ICT services supporting critical or
important functions) and **Implementing Regulation (EU) 2024/2956**
(ITS templates for the **register of information**, Art. 28(3)).
Other DORA RTS/ITS (ICT risk management, incident reporting, TLPT)
exist; they stay **EXTERNAL** unless a fact already maps to
canonical OSM posture.

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

| External concept | OSM target | Grain | Kind | Outside OSM |
|------------------|------------|-------|------|-------------|
| ICT third-party provider of an ICT service | `providers` → ICT Provider | Service and/or Offering | Canonical OSM relationship. Operator/deliverer/underpinning party (**OSM-C-006**). | LEI, legal parent, CIF register |
| Contractual arrangement / RoI row | — | Arrangement | **EXTERNAL** (**OSM-C-007**). Provider `contract_*` fields are **characterization**, not an Arrangement model. | RTS 2024/1773 structure; ITS 2024/2956 templates |
| Recovery time / point | `rto`, `rpo` | Offering posture | Canonical OSM; DORA *interprets* them | DORA-prefixed copies |
| Service / function criticality | `operational_criticality` | Service posture | Canonical OSM. DORA CIF criticality maps **onto** this where applicable. | Function register |
| Stack DORA labels | `mappings.dora.pillar`, `mappings.dora.criticality` | Stack | Informal **stack** labels. `standard` is an OSM enum token, **not** a DORA CIF class. Different grain from service criticality and provider `risk_level`. | Supervisory criticality of a CIF |
| Provider risk | `risk_level` | ICT Provider | Canonical provider risk/severity | Concentration models beyond the flag |
| Notification clause | `dora_notification_clause` | ICT Provider | Contract **flag** specific to DORA wording | Full contract |
| Process vs store location (RTS “processed and stored”) | characteristics `processing_location` / `storage_location` | Offering (actual) vs Provider `data_processing_locations` (capability) | Convention (**OSM-D-001**). No new schema fields. | RoI location columns |
| Incident reporting | — | — | **EXTERNAL** | Incident feed |
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
