# GDPR

OSM is **not** a GDPR compliance programme, a Record of Processing
Activities, or legal advice. OSM does not “comply with GDPR”.

The EU General Data Protection Regulation (Regulation (EU) 2016/679)
governs processing of personal data. OSM can carry **catalog-level**
signals that help a privacy team locate technological services that
process personal data.

## What maps

| OSM field | Where | Role |
|-----------|--------|------|
| `mappings.gdpr` | Technology Stack | Free-text article references, or `not-applicable` |
| `gdpr_processing_activity` | Offering posture | Whether processing occurs |
| `gdpr_dpia_required` | Offering posture | DPIA signal |
| `gdpr_erasure_capable` | Offering posture | Erasure capability |
| `privacy_classification` | Service posture | Canonical privacy class of the service |
| `iso27701_pii_*` | Offering posture | Adjacent privacy characterization |
| `gdpr_dpa_signed` | ICT Provider | DPA flag on the provider |
| `data_processing_locations` | ICT Provider | Where the provider processes data |

## What stays in GDPR / privacy operations

- legal basis
- data-subject rights workflows
- international transfers
- DPO identity
- Record of Processing Activities

Boolean flags such as `gdpr_processing_activity` are not a lawful
assessment. Illustrative article references in examples are not
interpretations of the regulation.

Exact field definitions are in
[`SPECIFICATION.md`](../SPECIFICATION.md).
