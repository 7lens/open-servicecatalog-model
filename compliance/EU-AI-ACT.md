# EU AI Act

**Mapped version:** Regulation **(EU) 2024/1689** (published in the
Official Journal 12 July 2024, in force 1 August 2024), with the
**current implementation timeline** including the "Digital Omnibus
on AI" postponement of the high-risk dates.

> **Mapping basis (2026-06-11):** the base act is Regulation (EU)
> 2024/1689 (the AI Act), published in the OJ on 12 July 2024 and in
> force 1 August 2024
> ([EUR-Lex ELI](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)).
> The high-risk obligations were deferred by the "Digital Omnibus on
> AI" amending regulation — standalone Annex III systems to
> 2 December 2027 and Annex I product-embedded systems to
> 2 August 2028 — while enforcement powers (the AI Office and
> national authorities, GPAI penalties, Article 50 transparency)
> took effect 2 August 2026
> ([Council AI Act timeline](https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/timeline-artificial-intelligence/),
> [Commission guidelines for high-risk AI systems](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-high-risk-systems),
> [amending Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng)).
> The timeline is volatile; re-verify against the authoritative EU
> sources before relying on a date. Source wording was rephrased for
> licensing compliance.

**Status:** **PARTIAL**

OSM is **not** an EU AI Act conformity assessment, technical file,
or claim of compliance with 2024/1689.

7lens OSM is a **data model** for technological services. It is not
an AI model.

OSM can flag technological services that contain AI systems and
carry a small set of **compatibility** facts. It does not become an
AI-system technical file.

## Timeline (re-verified 2026-06-11)

| Milestone | Date |
|-----------|------|
| Prohibited practices + AI literacy | 2 February 2025 |
| GPAI obligations | 2 August 2025 |
| Enforcement powers + Article 50 transparency (AI Office / national authorities / GPAI penalties) | 2 August 2026 |
| GPAI models on market before 2 Aug 2025: comply by | 2 August 2027 |
| High-risk **Annex III** obligations | **2 December 2027** (postponed) |
| Annex I product-safety route | **2 August 2028** (postponed) |

Dates re-verified against the
[Council AI Act timeline](https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/timeline-artificial-intelligence/)
and the
[Commission guidelines for high-risk AI systems](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-high-risk-systems);
the high-risk deferral is set by the Digital Omnibus on AI amending
regulation. Draft Commission guidelines on high-risk classification
under Article 6 existed as consultation text; they are **not** an
OSM enum. This timeline is volatile — treat these dates as the
latest known and re-check against the EU sources above.

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

The rows below walk the AI Act's own top-level structure — the
risk tiers (prohibited / high-risk / limited-risk-transparency /
minimal-risk), the GPAI-model regime, the provider and deployer
roles, and the conformity/registration machinery — and give each a
status from the index vocabulary (MAPPED / PARTIAL / EXTERNAL /
NOT IN SCOPE / FUTURE / OPTIONAL), so no top-level AI Act concept is
silently missing. OSM carries only compatibility locators and
labels; the legal classification and conformity structures stay
EXTERNAL.

| External concept (AI Act) | OSM target | Grain | Status + kind | Outside OSM |
|---------------------------|------------|-------|---------------|-------------|
| Whether the service involves an AI system (locator) | `ai_act_applicable`; stack `contains_ai_systems` | Service posture; Stack | **PARTIAL** — presence flag only. | Legal provider/deployer determination |
| Risk class **label** (prohibited / high / limited / minimal) | `ai_act_risk_class`; `max_risk_class` | Service posture; Stack | **PARTIAL** — OSM label, **not** Art. 6 / Annex III classification. | Legal classification, Annex III taxonomy |
| Intended purpose (AI Act mapping) | `ai_act_intended_purpose` | Offering posture (when applicable) | **MAPPED** — mapping field. | Technical-file purpose statement |
| Human oversight (AI Act mapping) | `ai_act_human_oversight` | Offering posture | **MAPPED** — keep prefixed name (**OSM-C-009**); not a generic `human_oversight`. | Oversight procedures |
| Transparency / conformity date / training-data doc flags | corresponding `ai_act_*` fields | Offering posture | **PARTIAL** — signals only. | Technical documentation pack |
| General-purpose AI (GPAI) model obligations | — | — | **EXTERNAL** — GPAI model entities and systemic-risk duties. | GPAI entities |
| Provider / deployer legal roles | — | — | **EXTERNAL** — role determination is a legal assessment. | Role model |
| Conformity assessment / technical file / CE marking | — | — | **EXTERNAL** — conformity structures. | Those structures |
| EU database registration (Art. 71) | — | — | **EXTERNAL** — registration system. | Registration |
| Post-market monitoring / incident reporting | — | — | **NOT IN SCOPE** — operational process outside OSM's catalog boundary. | Monitoring, serious-incident reports |
| AI regulatory sandboxes | — | — | **NOT IN SCOPE** — supervisory arrangement, not a catalog object. | Sandbox programmes |

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
