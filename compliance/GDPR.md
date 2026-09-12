# GDPR

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (compliance / governance)
- **OSM schema fields today:** optional stack `mappings.gdpr`;
  optional offering `gdpr_processing_activity`, `gdpr_dpia_required`,
  `gdpr_erasure_capable`; optional provider `gdpr_dpa_signed`

These fields are reference mappings. They are **not** a GDPR
compliance programme and not legal advice. OSM does not "comply
with GDPR".

## 1. Framework overview

The EU General Data Protection Regulation (Regulation (EU) 2016/679)
governs processing of personal data. Obligations depend on role
(controller / processor), purpose, legal basis, and many operational
facts OSM does not currently model.

## 2. Relevant scope for technological services

Later analysis should ask which **catalog-level** facts help a
privacy team locate technological services that process personal
data — without OSM becoming a Record of Processing Activities.

## 3. OSM concepts/attributes relevant to the framework

Present in the current schema (not yet analyzed as a mapping):

| OSM field | Where |
|-----------|--------|
| `mappings.gdpr` | Technology Stack (free text) |
| `gdpr_processing_activity` | Offering attributes |
| `gdpr_dpia_required` | Offering attributes |
| `gdpr_erasure_capable` | Offering attributes |
| `iso27701_pii_*` | Offering attributes (privacy-adjacent) |
| `gdpr_dpa_signed` | ICT Provider |
| `data_processing_locations` | ICT Provider |

## 4. Mapping opportunities

NOT YET ANALYZED.

## 5. Missing information

NOT YET ANALYZED.

Legal basis, data-subject rights workflows, international transfers,
DPO identity and RoPA entries are not OSM entities.

## 6. Potential extensions

None proposed. No attributes are added in this baseline.

## 7. Important caveats

- Boolean flags such as `gdpr_processing_activity` are not a lawful
  assessment.
- Illustrative article references in examples are not interpretations
  of the regulation.
- This file is not legal advice and not evidence of compliance.

## 8. Status

**NOT ANALYZED**
