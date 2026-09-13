# EU AI Act

**Mapped version:** Regulation **(EU) 2024/1689** (in force
1 August 2024), with the **current implementation timeline** from
the compatibility investigation (including Omnibus postponements of
high-risk dates).

**Status:** **PARTIAL**

OSM is **not** an EU AI Act conformity assessment, technical file,
or claim of compliance with 2024/1689.

7lens OSM is a **data model** for technological services. It is not
an AI model.

OSM can flag technological services that contain AI systems and
carry a small set of **compatibility** facts. It does not become an
AI-system technical file.

## Timeline (investigation, 2026-09-13)

| Milestone | Date |
|-----------|------|
| Prohibited practices + AI literacy | 2 February 2025 |
| GPAI obligations | 2 August 2025 |
| Commission GPAI enforcement / fines | 2 August 2026 |
| GPAI models on market before 2 Aug 2025: comply by | 2 August 2027 |
| High-risk **Annex III** obligations | **2 December 2027** (postponed) |
| Annex I product-safety route | **2 August 2028** (postponed) |

Draft Commission guidelines on high-risk classification under
Article 6(5) existed as consultation text in May 2026; they are
**not** an OSM enum.

## `ai_act_risk_class` is an OSM label

The existing field `ai_act_risk_class` (and stack
`mappings.ai_act.max_risk_class`) is an **OSM compatibility label**.

It must **not** be presented as though its enum exactly reproduces
the legal classification structure of **Article 6 / Annex III**.

Enum tokens (`unacceptable`, `high-risk`, `limited-risk`,
`minimal-risk`, `not-applicable`) are a compact catalog signal.
Legal classification is a different, external assessment.

## `ai_act_human_oversight`

Keep this field as currently defined. Do **not** rename it to
generic `human_oversight`. It is an **EU AI Act compatibility
field**.

`ai_act_intended_purpose` is likewise an AI Act **mapping** field
on offering posture when `ai_act_applicable` is true. Canonical
generic purpose, when needed, is characteristic `name: purpose`
(**OSM-D-002**) — not `ai_act_purpose` as a second canonical.

## Mapping table

| External concept | OSM target | Grain | Kind | Outside OSM |
|------------------|------------|-------|------|-------------|
| Whether the service involves an AI system (locator) | `ai_act_applicable`; stack `contains_ai_systems` | Service posture; Stack | Partial flag | Legal provider/deployer determination |
| Risk class **label** | `ai_act_risk_class`; `max_risk_class` | Service posture; Stack | OSM label — **not** Art. 6 / Annex III | Legal classification, Annex III taxonomy |
| Intended purpose (AI Act mapping) | `ai_act_intended_purpose` | Offering posture (when applicable) | Mapping field | Technical-file purpose statement |
| Human oversight (AI Act mapping) | `ai_act_human_oversight` | Offering posture | Keep prefixed name | Oversight procedures |
| Transparency / conformity date / training-data doc flags | corresponding `ai_act_*` fields | Offering posture | Signals | Technical documentation pack |
| GPAI model structures | — | — | **EXTERNAL** | GPAI entities |
| Provider / deployer legal roles | — | — | **EXTERNAL** | Role model |
| EU database | — | — | **EXTERNAL** | Registration |
| Technical file / conformity assessment system | — | — | **EXTERNAL** | Those structures |

Offering-level AI Act fields are valid only when
`ai_act_applicable` is true.

## What stays in AI Act operations (**EXTERNAL**)

- GPAI model structures
- legal provider/deployer role structures
- EU database
- technical file / conformity assessment structures
- Annex III taxonomy as OSM entities

Example `max_risk_class` values are illustrative, not legal
classifications. Completing OSM fields is not a conformity
assessment. These fields describe optional catalog metadata about
technological services; they are not a 7lens agent architecture.

Exact field definitions are in
[`SPECIFICATION.md`](../SPECIFICATION.md).
