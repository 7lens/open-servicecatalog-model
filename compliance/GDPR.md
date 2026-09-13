# GDPR

**Mapped version:** Regulation **(EU) 2016/679** (consolidated text
as of the compatibility investigation; no later consolidated
amendment identified).

**Status:** **PARTIAL**

OSM is **not** a GDPR compliance programme, a Record of Processing
Activities, or legal advice. OSM does not “comply with GDPR”.
Do **not** turn OSM into a RoPA.

OSM may carry high-level privacy classification and compatibility
characteristics/mappings so a privacy team can **locate**
technological services that process personal data.

## Mapping table

| External concept | OSM target | Grain | Kind | Outside OSM |
|------------------|------------|-------|------|-------------|
| High-level privacy sensitivity | `privacy_classification` | Service posture | **Canonical OSM** (**OSM-D-003**) | `gdpr_privacy_classification` (forbidden) |
| Whether processing of personal data occurs (locator) | `gdpr_processing_activity` | Offering posture | Mapping boolean — **not** a lawful assessment | Processing-activity entity |
| DPIA / erasure locators | `gdpr_dpia_required`, `gdpr_erasure_capable` | Offering posture | Signals | DPIA files, rights workflows |
| Article references | `mappings.gdpr` | Stack | Illustrative free-text, or `not-applicable`. **Not** a legal interpretation. | Legal analysis |
| DPA signed with provider | `gdpr_dpa_signed` | ICT Provider | Flag | Contract repository |
| Provider possible processing countries | `data_processing_locations` | ICT Provider | **Capability / possible locations**, not actual offering residency (**OSM-D-001**) | Transfer mechanisms, SCCs |
| Purpose of processing | characteristic `name: purpose` | Service or Offering | Generic characteristic (**OSM-D-002**). **Not** `gdpr_purpose`. | Purpose register in RoPA |
| Processing vs storage location | characteristics `processing_location` / `storage_location` | Offering (actual) vs Provider (capability) | Convention, no new schema fields | RoPA location columns |
| Legal basis, data subjects, recipients, transfers, retention, DPO, SCCs, full RoPA | — | — | **EXTERNAL** | Those objects |

## Precedence

1. `privacy_classification` — canonical OSM class.
2. GDPR-named fields — compatibility locators.

## What stays in GDPR / privacy operations (**EXTERNAL**)

- processing activities (no GDPR processing-activity entity in OSM)
- legal basis
- data-subject categories
- recipient categories
- transfer mechanisms
- retention schedules
- DPO
- SCCs
- full RoPA

Boolean flags such as `gdpr_processing_activity` are not a lawful
assessment. Illustrative article references in examples are not
interpretations of the regulation.

Exact field definitions are in
[`SPECIFICATION.md`](../SPECIFICATION.md).
