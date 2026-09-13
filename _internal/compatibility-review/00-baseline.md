# 00 — Repository and OSM baseline

**Investigation date:** 2026-09-13  
**OSM version under test:** Specification 1.3.0 (frozen architecture)  
**Normative sources:** `schema/`, `SPECIFICATION.md`, `MODEL.md`  
**This file is not a model change.**

---

## 1. Actual repository layout (as inspected)

Do not rely on older path names in decision records. The live tree is:

```text
schema/
  catalog/     technology-stack.yaml, service.yaml, service-offering.yaml, ict-provider.yaml
  posture/     service-posture.yaml
  shared/      characteristic.yaml, provenance.yaml

models/
  README.md
  service-management/  TMFORUM-TMF633.md, ITIL.md, CSDM.md
  architecture/        ARCHIMATE.md, TOGAF.md, TBM.md

compliance/
  README.md, ISO-27001.md, ISO-27701.md, NIST-CSF.md, GDPR.md, DORA.md, EU-AI-ACT.md

examples/
  catalog/   technology-stacks.yaml, services.yaml, ict-providers.yaml
  posture/   service-posture.yaml
  reference-enterprise/
  reference-estate/

validation/validate.py

_internal/
  decisions/     DECISIONS.md, OSM-M-*, OSM-ARCHITECTURE-FREEZE.md
  notes/         COMPATIBILITY.md + historical compatibility/ and compliance/ notes
  investigation/ reference-estate stress test (2026-09-13)
```

### Path drift (record only)

| Older name still cited | Current location |
|------------------------|------------------|
| `COMPATIBILITY.md` at repo root | `_internal/notes/COMPATIBILITY.md` |
| `compatibility/*.md` | public: `models/`; archive: `_internal/notes/compatibility/` |
| `schema/service.yaml` etc. | `schema/catalog/`, `schema/posture/`, `schema/shared/` |
| YAML keys `service_attributes` / `offering_attributes` | files/keys now `service_posture` / `offering_posture` |
| `DECISIONS.md` at repo root | `_internal/decisions/DECISIONS.md` |

`SPECIFICATION.md` §2 still says JSON Schema lives in those nested folders (correct) but DECISIONS.md surface lists still name pre-move paths.

---

## 2. Frozen OSM entities

| Entity | Role | Identity | Required core fields |
|--------|------|----------|----------------------|
| **Technology Stack** | Operational competency / ownership domain. Not a cost centre, org box, or infrastructure inventory. | `id` (slug; default service prefix) | `id`, `name`, `description` |
| **Service** | Stable **definition** of a technological service. Not a listing, availability record, or instance. | 2-segment `id`, immutable | `id`, `name`, `description`, `accountable`, `technology_stack` (stack **name**), `version`, `valid_from`, `lifecycle_state`, `service_offerings` (≥1) |
| **Service Offering** | Atomic requestable / deliverable **variant**. No independent version/validity/lifecycle. | 3-segment `id`; first two = parent service | `id`, `name` |
| **ICT Provider** | Canonical third-party technology organisation | `id` (slug) | `id`, `name`, `type`, `substitutability` |

### Reusable structures (not catalog entities)

| Structure | Attaches to | Role |
|-----------|-------------|------|
| **Characteristic** | Service or Offering (nested) | Named, typed property. No OSM id. Inspired by TMF; not a TMF characteristic catalog. |
| **Provenance** | Service, Offering, service posture, offering posture | Why a fact can be trusted. Seven non-interchangeable fields. |
| **Service Posture** | Service via `service_id` | How the service currently stands. |
| **Offering Posture** | Nested under service posture via `offering_id` | Variant-level operations, cost, security, resilience, optional mappings. |

Empty `offering_posture: []` is valid.

---

## 3. Canonical relationships

```text
Technology Stack      1 : many   Service                 (service.technology_stack = stack name)
Service               1 : many   Service Offering        (offering id prefix = service id)
Service               0 : many   Characteristic          nested
Service Offering      0 : many   Characteristic          nested
Service               0 : many   ICT Provider            providers[] ids
Service Offering      0 : many   ICT Provider            providers[] ids
Service / Offering / posture  0 : 1  Provenance          nested
Service               1 : 0..1   Service Posture         service_id
Service Posture       1 : many   Offering Posture        offering_id
```

**`providers` is the single canonical who-provides relationship** (OSM-M-006, OSM-M-010). Reverse Provider → Service is derived. `providers` is not Service → Service.

Use Service-level `providers` when the provider is intrinsic to the service. Use Offering-level `providers` when provider choice distinguishes the variant.

**Not defined (deliberate, frozen):** Service → Service; consumers; applications; Service Instance; CMDB/CI; Product Models; org/geo hierarchy; SLA objects.

Ownership: `accountable` = Service Owner. Technology Stack Owner is documented in `GOVERNANCE.md` but is **not** a stack schema field. `financial_owner` is posture, not definition accountability.

---

## 4. Layers (OSM-M-007)

```text
SERVICE DEFINITION     what the service is (catalog, including characteristics)
POSTURE                how it currently stands
PROVENANCE             why the information can be trusted
EXTERNAL CONTEXT       owned elsewhere
FRAMEWORK MAPPINGS     translation layer, not a second copy of OSM facts
```

Identity is immutable. Definition may evolve (`version`, `valid_from`/`valid_to`, `lifecycle_state` on Service). One catalog row per service `id`. History of prior definitions is out of band.

---

## 5. Complete mapping-field inventory

Principle under test: **ONE CONCEPT → ONE CANONICAL PARAMETER** (OSM-M-008).

### 5.1 Technology Stack `mappings` (all optional, non-normative)

| Field | Semantic meaning | Grain | Type / enum | Normative? | Originating framework | Already represented elsewhere? |
|-------|------------------|-------|-------------|------------|----------------------|--------------------------------|
| `tbm_tower` | TBM IT Tower (L1) / Resource Tower label | Stack | free-text string | optional mapping | TBM | Possibly OSM Service (TBM Solutions) or Stack (operational domain). **Duplication risk vs TBM Solutions / OSM Service.** |
| `tbm_sub_tower` | TBM Sub-Tower (L2) | Stack | free-text string | optional mapping | TBM | Same grain question as tower. |
| `togaf_domain` | TOGAF architecture domain label | Stack | free-text string | optional mapping | TOGAF | No other TOGAF field. Grain: stack-only. |
| `iso27001` | Annex A control references | Stack | free-text string | optional mapping | ISO 27001 | **Same concept as offering `iso27001_controls` at different grain and type.** |
| `iso27701` | ISO 27701 references or `not-applicable` | Stack | free-text string | optional mapping | ISO 27701 | Offering `iso27701_pii_*` are different facts (role/categories/retention), not a duplicate of this label. |
| `nist_csf` | CSF 2.0 Functions | Stack | enum list: govern, identify, protect, detect, respond, recover | optional mapping | NIST CSF 2.0 | **Same enum as offering `nist_functions`.** |
| `gdpr` | GDPR article references or `not-applicable` | Stack | free-text string | optional mapping | GDPR | Offering GDPR booleans are different facts. Article numbers vs processing flags. |
| `dora.pillar` | Informal DORA “pillar” | Stack | enum of 4 titles | optional mapping | DORA | DORA does not officially call these “pillars”; information-sharing is omitted. Not a duplicate of a canonical field. |
| `dora.criticality` | Stack-level DORA label | Stack | critical / important / **standard** | optional mapping | DORA | **Not** service `operational_criticality` (different grain, documented). Enum token `standard` is **not** a DORA legal term. |
| `ai_act.contains_ai_systems` | Whether the stack includes AI systems | Stack | boolean | optional mapping | EU AI Act | Related to, not identical with, service `ai_act_applicable`. |
| `ai_act.max_risk_class` | Highest labelled class in the stack | Stack | same enum as service risk class | optional mapping | EU AI Act | **Roll-up of `ai_act_risk_class`.** Same concept, different grain. |
| `ai_act.reference` | Free-text reference | Stack | string | optional mapping | EU AI Act | No other field. |

### 5.2 Service definition fields that participate in mappings

| Field | Meaning | Grain | Type | Normative? | Frameworks | Duplication flag |
|-------|---------|-------|------|------------|------------|------------------|
| `accountable` | Service Owner | Service | string | required | ITIL, CSDM, ISO roles | Distinct from `financial_owner`. |
| `lifecycle_state` | Definition lifecycle | Service | draft/pilot/production/sunset/retired | required | TMF, ITIL, CSDM | Distinct from ITIL/CSDM *management* lifecycle. |
| `version`, `valid_from`, `valid_to` | Definition version/validity | Service | string / date | required except valid_to | TMF | Distinct from offering (none) and posture. |
| `providers` | Who provides | Service or Offering | id list | optional | DORA, CSDM, ITIL supplier, ArchiMate actor | Canonical. Do not duplicate. |
| `characteristics` | Variant/definition properties | Service or Offering | nested | optional | TMF, CSDM offering dimensions | Extension mechanism, not a mapping field. |

### 5.3 Service posture (canonical, unprefixed)

| Field | Meaning | Grain | Type / enum | Mapping use | Duplication flag |
|-------|---------|-------|-------------|-------------|------------------|
| `operational_criticality` | Canonical service criticality | Service posture | critical / important / standard | DORA maps here | Distinct from stack `dora.criticality` and provider `risk_level`. |
| `resilience_tier` | Qualitative resilience class | Service posture | free-text | DORA/ISO continuity conversations | Distinct from `rto`/`rpo`. |
| `availability_target` | Performance target | Service posture | string | ITIL/CSDM SLA *expectation* only | Distinct from `service_hours` characteristic and vendor SLA. |
| `response_target` | Incident/request response target | Service posture | ISO 8601 duration | same | Distinct from `support_hours`. |
| `resolution_target` | Resolve target | Service posture | ISO 8601 duration | same | — |
| `data_classification` | Data the service handles | Service posture | public/internal/confidential/restricted | ISO 27001, GDPR, DORA data | **Same enum as `security_classification`; different subject.** |
| `security_classification` | Sensitivity of the service itself | Service posture | same enum | ISO 27001 | Not data classification. |
| `privacy_classification` | Privacy class of the service | Service posture | none/pii/sensitive/not-assessed | GDPR, ISO 27701 | **Overlaps offering PII categories and `gdpr_processing_activity`.** |
| `tech_debt_score` | 0–100 or null | Service posture | int | none | OSM-native. |
| `vendor_support_status` | Vendor support life | Service posture | active/extended/end-of-life | supplier mgmt | Distinct from provider `risk_level`. |
| `financial_owner` | Financial ownership role | Service posture | string | TBM accountability | Distinct from `accountable`. |
| `ai_act_applicable` | Whether offering AI Act fields apply | Service posture | bool | EU AI Act | Related to stack `contains_ai_systems`. |
| `ai_act_risk_class` | Risk class | Service posture | unacceptable/high-risk/limited-risk/minimal-risk/not-applicable | EU AI Act | Related to stack `max_risk_class`. Enum is a **common simplification**, not the Act’s legal taxonomy. |

### 5.4 Offering posture — canonical operations/finance/resilience

| Field | Meaning | Grain | Type | Mapping use | Duplication flag |
|-------|---------|-------|------|-------------|------------------|
| `cost_pool` | Cost-pool characterization | Offering posture | string/null | TBM Cost Pool **name collision** | Not TBM allocation. |
| `chargeback_model` | shared/dedicated/consumption | Offering posture | enum | TBM showback pattern | Not a TBM engine. |
| `unit_cost` | Unit-cost characterization | Offering posture | number/null | TBM | Not accounting. |
| `automation_coverage` | Overall ops automation | Offering posture | none/partial/full/null | ITIL/CSDM operational | Distinct from `provisioning_automation`. |
| `provisioning_automation` | Provisioning process automation | Offering posture | same enum | same | — |
| `self_service` | Requestable without human fulfilment | Offering posture | bool/null | ITIL request catalog | — |
| `manual_hours_week` | Manual effort | Offering posture | number/null | TBM labor signal | — |
| `last_security_review` | Last review date | Offering posture | date/null | ISO 27001, NIST | Evidence *date*, not control implementation. |
| `asset_coverage` | Asset inventory completeness | Offering posture | complete/partial/unknown/null | ISO 27001 assets, CSDM CI coverage | Not a CMDB. |
| `rto` | Recovery Time Objective | Offering posture | duration/null | DORA, ISO 27001 A.5.30, NIST Recover | Canonical. No `dora_rto`. |
| `rpo` | Recovery Point Objective | Offering posture | duration/null | same | Canonical. |
| `resilience_tested` | Whether tested | Offering posture | bool/null | DORA testing | Canonical. |
| `last_resilience_test` | Test date | Offering posture | date/null | DORA | — |
| `resilience_evidence` | Handle/URI | Offering posture | string/null | DORA, ISO evidence | Distinct from provenance.evidence_reference (may overlap in practice). |

### 5.5 Offering posture — framework-named mappings

| Field | Meaning | Grain | Type / enum | Origin | Duplication flag |
|-------|---------|-------|-------------|--------|------------------|
| `iso27001_controls` | Annex A control IDs | Offering | string list | ISO 27001 | Duplicate concept vs stack `iso27001` (different grain/type). |
| `iso27701_pii_role` | controller/processor/joint-controller/none | Offering | enum | ISO 27701 / GDPR Art. 4 | **Same legal role as GDPR controller/processor.** No GDPR role field exists; this is the only role field. Grain: offering vs processing activity. |
| `iso27701_pii_categories` | identity/financial/health/behavioral/location/biometric/communications/none | Offering | enum list | ISO 27701 | Overlaps `privacy_classification` and GDPR data categories. Enum is **not** GDPR Art. 9 special categories. |
| `iso27701_retention_days` | Retention characterization | Offering | int/null | ISO 27701 / GDPR storage limitation | No GDPR retention field. This is the only retention field. |
| `nist_functions` | CSF Functions | Offering | same enum as stack | NIST CSF 2.0 | Duplicate of stack `nist_csf`. |
| `nist_control_status` | Implementation status | Offering | implemented/partially-implemented/planned/not-applicable/null | NIST-like | **Not a CSF construct.** CSF uses Profiles, not a single status token. Misleading name. |
| `gdpr_processing_activity` | Whether processing occurs | Offering | bool | GDPR | Overlaps `privacy_classification != none` and PII role ≠ none. |
| `gdpr_dpia_required` | DPIA signal | Offering | bool | GDPR Art. 35 | Not a DPIA record. |
| `gdpr_erasure_capable` | Erasure capability | Offering | true/false/partial/not-applicable | GDPR Art. 17 | Capability, not a rights workflow. |
| `ai_act_intended_purpose` | Intended purpose | Offering | free text | EU AI Act Art. 3/9 | Only purpose field in OSM. GDPR/ISO purpose is absent. |
| `ai_act_human_oversight` | Oversight mode | Offering | HITL/HOTL/HIC/none | EU AI Act Art. 14 | Framework-specific. Valid only if `ai_act_applicable`. |
| `ai_act_transparency_level` | Disclosure mode | Offering | explicit/implicit/none | EU AI Act Art. 50 (loosely) | Framework-specific. |
| `ai_act_conformity_assessment` | Date of assessment | Offering | date/null | EU AI Act Art. 43 | Date, not the assessment. |
| `ai_act_training_data_doc` | Training-data documentation exists | Offering | bool/not-applicable | EU AI Act data governance | Flag, not the documentation. |

### 5.6 ICT Provider fields (canonical + two framework flags)

| Field | Meaning | Grain | Type | Origin / use | Duplication flag |
|-------|---------|-------|------|--------------|------------------|
| `type` | Coarse org class | Provider | closed enum (no `saas`) | OSM | Stressed by estate investigation D-002. |
| `headquarters` | ISO 3166-1 alpha-2 | Provider | country code | DORA provider location (partial) | **Collapses legal seat, contracting party, parent, CTPP.** |
| `data_processing_locations` | Countries/regions list | Provider | string list | DORA/GDPR location | **Collapses processing vs storage; capability vs actual residency.** |
| `substitutability` | low/medium/high | Provider | enum | DORA transferability | Market observation vs customer-specific. |
| `contract_*`, `notice_period_days` | Contract characterization | Provider | mixed | DORA contractual arrangements | **Wrong grain vs arrangement × service.** |
| `audit_rights` | bool/null | Provider | bool | DORA/GDPR audit | Boolean overclaims report-based audit. |
| `subcontracting_allowed` | bool/conditional/null | Provider | mixed | DORA subcontracting | — |
| `subcontractors` | name list | Provider | strings | DORA supply chain | No rank, LEI, or chain. |
| `last_risk_assessment` | date | Provider | date | DORA due diligence | — |
| `risk_level` | Provider risk/severity | Provider | low/medium/high/critical/null | OSM-M-009; DORA provider risk | Distinct from service criticality. |
| `exit_strategy_documented` / `_tested` | Exit plan flags | Provider | bool/null | DORA Art. 28 exit | Arrangement grain would be more accurate. |
| `concentration_risk` | bool/null | Provider | bool | DORA concentration | Often an *entity* observation, not a provider property. |
| `certifications` | free-form badges | Provider | string list | ISO/SOC | Unscoped; overclaims (estate D-001). |
| `gdpr_dpa_signed` | DPA flag | Provider | bool/null | GDPR Art. 28 | “Published DPA” ≠ “this customer signed”. |
| `dora_notification_clause` | Contract flag | Provider | bool/null | DORA | The **only remaining DORA-prefixed field**. Framework-specific. |

ICT Provider has **no `provenance`**. Estate investigation D-025 remains open.

---

## 6. Accepted and proposed decisions

Source: `_internal/decisions/DECISIONS.md` and freeze record.

### Compatibility (all ACCEPTED)

| ID | Decision |
|----|----------|
| OSM-C-001 | Universe = 6 models + 6 compliance frameworks |
| OSM-C-002 | PDMC removed |
| OSM-C-003 | CSDM retained (vendor-specific but important) |
| OSM-C-004 | ITIL v5 **PARTIALLY COMPATIBLE / selective**. Digital Product, Business Service, consumers, value streams, Service→Service, CI, SLA stay outside core |
| OSM-C-005 | CSDM **PARTIALLY COMPATIBLE / selective**. Service Instance, Business/Application Service, CMDB, Product Models outside |

### Model (frozen)

| ID | Status | Meaning |
|----|--------|---------|
| OSM-M-001 | ACCEPTED | Generic characteristics |
| OSM-M-002 | ACCEPTED | Temporal semantics on Service only |
| OSM-M-003 | ACCEPTED | Service *is* the definition (no ServiceSpecification entity) |
| OSM-M-004 | ACCEPTED | Best-of, not standards accumulation |
| OSM-M-005 | **SUPERSEDED** by OSM-M-010 | Originally the DORA provider-link **grain** question |
| OSM-M-006 | ACCEPTED | Canonical ICT Provider references |
| OSM-M-007 | ACCEPTED | Complete Service Definition layers |
| OSM-M-008 | ACCEPTED | One concept, one canonical parameter |
| OSM-M-009 | ACCEPTED | Provider `risk_level` not `criticality` |
| OSM-M-010 | ACCEPTED | `providers` is the only who-provides relationship |

**No PROPOSED model decisions exist.** Architecture is FROZEN (`OSM-ARCHITECTURE-FREEZE.md`, 2026-09-12).

### What OSM-M-005 did *not* settle

OSM-M-010 closed **duplication** (do not keep `dora_third_party_deps` beside `providers`). It did **not** close:

1. When a DORA ICT-service / arrangement link should be stored at **Service** vs **Offering**.
2. Whether DORA’s **contractual-arrangement** grain is the same relationship as OSM `providers`.

Evidence for maintainers is in 03 (DORA) and 07 (decision D1). This investigation does **not** resolve it.

### Related open estate decisions (not accepted)

`_internal/investigation/decision_register.md` has 30 OPEN items (D-001–D-030) from the 2026-09-13 estate stress test. They are not OSM decisions. Several overlap this investigation (certification scope, SaaS type, LEI, DPA flag, audit boolean, subcontractor chain, location grain, contract grain, provenance on provider, Service→Service).

---

## 7. Public mapping-file quality at baseline

| Surface | Stated status in `_internal/notes/COMPATIBILITY.md` | Public file quality |
|---------|------------------------------------------------------|---------------------|
| TMF633 | PARTIALLY COMPATIBLE | Short; does not cite v4.0.0 as production or v5 preproduction |
| ITIL | PARTIALLY COMPATIBLE | Does not distinguish ITIL 4 vs Version 5 (Feb 2026) product/service lifecycle |
| CSDM | PARTIALLY COMPATIBLE | Does not cite CSDM 5 Service Instance siblings or TMS rename evidence |
| ArchiMate | NOT ANALYZED | Public file already maps to **Technology Service** — **outdated vs ArchiMate 4** (Apr 2026) |
| TOGAF | NOT ANALYZED | Mentions `togaf_domain`; no 10th Edition / Corrigendum 1 |
| TBM | NOT ANALYZED | Still “IT Tower (L1)”; current name is Technology Resource Towers 5.0.1 |
| All six compliance files | NOT ANALYZED | Thin; ISO 27701 does not mention 2025 standalone PIMS; DORA does not cite RTS/ITS |

Public `models/` and `compliance/` were **not rewritten** in this task. They remain the object of analysis.

---

## 8. Out of scope (frozen, justified later per framework)

From `MODEL.md` / `SPECIFICATION.md`:

- business capabilities / business services
- digital products, outcomes, value streams
- applications / Application Services
- Service Instances / runtime
- CMDB / CIs
- Product Models
- org / geo / legal-entity hierarchy
- enterprise ontology, stakeholder lenses
- detailed SLA objects
- first-class Service → Service relationships

Consumers of a technological service are outside OSM.
