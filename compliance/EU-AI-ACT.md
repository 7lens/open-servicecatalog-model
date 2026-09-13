# EU AI Act

OSM is **not** an EU AI Act conformity assessment, technical file,
or claim of compliance with Regulation (EU) 2024/1689.

7lens OSM is a **data model** for technological services. It is not
an AI model.

The EU AI Act classifies AI systems by risk and imposes obligations
that vary by class. OSM can flag technological services that
contain AI systems and carry a small set of governance facts —
without becoming an AI-system technical file.

## What maps

| OSM field | Where | Role |
|-----------|--------|------|
| `mappings.ai_act.contains_ai_systems` | Technology Stack | Whether the stack includes AI systems |
| `mappings.ai_act.max_risk_class` | Technology Stack | Highest labelled class in the stack |
| `mappings.ai_act.reference` | Technology Stack | Optional free-text reference |
| `ai_act_applicable` | Service posture | Whether offering-level AI Act fields apply |
| `ai_act_risk_class` | Service posture | Risk class |
| `ai_act_intended_purpose` | Offering posture | Present only when applicable |
| `ai_act_human_oversight` | Offering posture | Present only when applicable |
| `ai_act_transparency_level` | Offering posture | Present only when applicable |
| `ai_act_conformity_assessment` | Offering posture | Present only when applicable |
| `ai_act_training_data_doc` | Offering posture | Present only when applicable |

Offering-level AI Act fields are valid only when
`ai_act_applicable` is true.

## What stays in AI Act operations

- provider / deployer / manufacturer roles
- Annex III taxonomy
- technical documentation packs
- quality-management records

Example `max_risk_class` values are illustrative, not legal
classifications. Completing OSM fields is not a conformity
assessment. These fields describe optional catalog metadata about
technological services; they are not a 7lens agent architecture.

Exact field definitions are in
[`SPECIFICATION.md`](../SPECIFICATION.md).
