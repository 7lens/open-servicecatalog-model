# EU AI Act

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (compliance / governance)
- **OSM schema fields today:** optional stack `mappings.ai_act`;
  service `ai_act_applicable`, `ai_act_risk_class`; offering
  `ai_act_*` fields when applicable

These fields are reference mappings. They are **not** an EU AI Act
conformity assessment and not a claim that OSM, 7lens, or any
adopter complies with Regulation (EU) 2024/1689.

7lens OSM is a **data model** for technological services. It is not
an AI model.

## 1. Framework overview

The EU AI Act classifies AI systems by risk and imposes obligations
that vary by class (including transparency and, for high-risk
systems, conformity assessment and quality-management duties).

## 2. Relevant scope for technological services

Later analysis should ask how a technological-service catalog can
flag services that contain AI systems and carry a small set of
governance facts — without OSM becoming an AI-system technical file.

## 3. OSM concepts/attributes relevant to the framework

Present in the current schema (not yet analyzed as a mapping):

| OSM field | Where |
|-----------|--------|
| `mappings.ai_act.contains_ai_systems` | Technology Stack |
| `mappings.ai_act.max_risk_class` | Technology Stack |
| `mappings.ai_act.reference` | Technology Stack |
| `ai_act_applicable` | Service attributes |
| `ai_act_risk_class` | Service attributes |
| `ai_act_intended_purpose` | Offering attributes (only if applicable) |
| `ai_act_human_oversight` | Offering attributes |
| `ai_act_transparency_level` | Offering attributes |
| `ai_act_conformity_assessment` | Offering attributes |
| `ai_act_training_data_doc` | Offering attributes |

Validation currently requires offering-level AI Act fields only when
`ai_act_applicable` is true.

## 4. Mapping opportunities

NOT YET ANALYZED.

## 5. Missing information

NOT YET ANALYZED.

Provider, deployer vs. manufacturer roles, Annex III taxonomy,
technical documentation packs and QMS records are not OSM entities.

## 6. Potential extensions

None proposed. No attributes are added in this baseline.

## 7. Important caveats

- Example `max_risk_class` values are illustrative, not legal
  classifications.
- Completing OSM fields is not a conformity assessment.
- This file is not legal advice.
- Do not read these fields as a 7lens agent architecture. They
  describe optional catalog metadata about technological services.

## 8. Status

**NOT ANALYZED**
