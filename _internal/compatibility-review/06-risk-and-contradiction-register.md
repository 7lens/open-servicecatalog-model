# 06 — Risk and contradiction register

Recorded, not fixed. IDs are investigation-local (`C-*`).

---

## C-VER — Incorrect current-version mappings

| ID | Surface | Issue |
|----|---------|-------|
| C-VER-1 | `models/architecture/ARCHIMATE.md` | Maps OSM Service to ArchiMate **Technology Service**. Current spec is **ArchiMate 4** (27 Apr 2026); that class is merged into generic **Service**. Internal notes still say NOT ANALYZED. |
| C-VER-2 | `models/architecture/TBM.md`, `SPECIFICATION.md` `tbm_tower` | Language is “TBM IT Tower (L1)”. Current: **Technology Resource Towers**, taxonomy **5.0.1** (18 Jul 2025). |
| C-VER-3 | `models/service-management/ITIL.md` | Does not distinguish ITIL 4 vs **Version 5** (12 Feb 2026) eight-activity product/service lifecycle vs OSM definition lifecycle. |
| C-VER-4 | `models/service-management/CSDM.md` | Does not cite **CSDM 5** Service Instance siblings or TMS rename evidence. Mapping is still *directionally* right. |
| C-VER-5 | `models/architecture/TOGAF.md` | No 10th Edition / Corrigendum 1 (May 2025). |
| C-VER-6 | `models/service-management/TMFORUM-TMF633.md` | Does not state production **v4.0.0** or that v5 is preproduction. |
| C-VER-7 | `compliance/ISO-27701.md` | Describes 27701 as an **extension** of 27001/27002. **2025 is standalone.** |
| C-VER-8 | `compliance/ISO-27001.md` | Mentions 27001:2022 Annex A; omits **Amd 1:2024** (harmless for catalog, incomplete for currentness). |
| C-VER-9 | `compliance/EU-AI-ACT.md` | No 2026 Omnibus postponements, GPAI enforcement 2 Aug 2026, or draft high-risk guidelines (19 May 2026). Enum presented as if it were the Act. |
| C-VER-10 | `compliance/DORA.md` | Canonical-field mapping is good; omits RTS 2024/1773 and ITS 2024/2956; does not warn about arrangement grain. |
| C-VER-11 | `_internal/notes/COMPATIBILITY.md` | Architecture freeze copies **NOT ANALYZED** for ArchiMate/TOGAF/TBM and all six compliance items, while public `models/` already contain assertive mappings. Status vocabulary is internally inconsistent. |

---

## C-DUP — Duplicate or overlapping semantics (OSM-M-008 stress)

| ID | Fields | Same concept? | Note |
|----|--------|---------------|------|
| C-DUP-1 | stack `iso27001` (free text) vs offering `iso27001_controls` (list) | **Yes, different grain and type** | One concept, two parameters. Flag, do not auto-merge. |
| C-DUP-2 | stack `nist_csf` vs offering `nist_functions` | **Yes (Functions)** | Dual grain. Document or pick one default. |
| C-DUP-3 | stack `ai_act.max_risk_class` vs service `ai_act_risk_class` | Roll-up vs fact | Acceptable if documented as derived vs authoritative. Not documented as derived. |
| C-DUP-4 | stack `dora.criticality` vs `operational_criticality` | **No** (stack label vs service criticality) | Documented as different grains. Risk: adopters copy the same token into both. |
| C-DUP-5 | `iso27701_pii_role` vs GDPR controller/processor | **Yes** | Only one field exists (good). **Wrong name** for dual-standard concept. |
| C-DUP-6 | `privacy_classification` vs `gdpr_processing_activity` vs `iso27701_pii_role` vs `iso27701_pii_categories` | **Overlapping locators** | Four ways to say “this handles personal data”. |
| C-DUP-7 | `ai_act_intended_purpose` vs missing generic purpose vs `description` | Purpose vs description | AI-prefixed subset of GAP-003. |
| C-DUP-8 | `resilience_evidence` vs `provenance.evidence_reference` | Evidence pointer | Different objects; easy to double-store the same URI. |
| C-DUP-9 | `last_security_review` vs provenance.`last_verified` | Dates of trust | Related, not identical. |
| C-DUP-10 | Provider `risk_level` vs service `operational_criticality` vs stack DORA criticality | **No** (OSM-M-009) | Correctly distinct; still a training hazard. |

---

## C-TERM — Conflicting terminology

| ID | Clash |
|----|-------|
| C-TERM-1 | OSM **Service** vs ITIL/TOGAF/TBM/ArchiMate 4 generic **service** (broader). |
| C-TERM-2 | OSM **Service Offering** vs ITIL/CSDM offering (often includes consumer + SLA commitments). |
| C-TERM-3 | OSM `lifecycle_state` vs ITIL v5 Product & Service Lifecycle vs CSDM 5 Life Cycle Stage vs TMF lifecycleStatus. |
| C-TERM-4 | OSM `cost_pool` vs TBM 5 **Cost Pool** (GL what-was-bought). |
| C-TERM-5 | OSM `mappings.dora.pillar` — DORA does not name “pillars”; five areas if information-sharing is counted. |
| C-TERM-6 | OSM `ai_act_risk_class` `limited-risk` / `minimal-risk` / `unacceptable` vs Act: prohibited, high-risk, Art. 50, GPAI. |
| C-TERM-7 | YAML/`SPECIFICATION` **Service Posture** vs freeze text still mentioning `service_attributes` as the implemented name (partially healed by file rename). |
| C-TERM-8 | `nist_control_status` implies NIST *controls*; CSF 2.0 has outcomes, not a control catalog. |

---

## C-GRAIN — Wrong or unstable grain

| ID | Issue |
|----|-------|
| C-GRAIN-1 | **OSM-M-005 remainder:** DORA association is arrangement×ICT service×function; OSM `providers` is Service and/or Offering. OSM-M-010 closed duplication, not this mismatch. |
| C-GRAIN-2 | Contract, exit, audit, DPA, notification **on Provider** vs per-arrangement / per-service. |
| C-GRAIN-3 | `data_processing_locations` on Provider (capability) vs actual offering residency. |
| C-GRAIN-4 | `iso27701_pii_role` on Offering vs 27701:2025 / GDPR **per processing activity**. |
| C-GRAIN-5 | `iso27701_retention_days` single integer vs purpose-based multiple retentions. |
| C-GRAIN-6 | `togaf_domain` stack-only; services cannot be labelled. |
| C-GRAIN-7 | TBM Resource Tower labels on **Stack** vs TBM 5 **Solutions** closer to OSM Service. |
| C-GRAIN-8 | `concentration_risk` as a provider boolean vs firm-level concentration vs function-level. |
| C-GRAIN-9 | `certifications[]` provider-wide vs scoped to product/region/edition (D-001). |
| C-GRAIN-10 | ISO 27001 controls on **Offering** vs many controls that are organisational (A.5.*) or people/physical. |

---

## C-SPEC — Framework-specific fields that look canonical

| ID | Field | Risk |
|----|-------|------|
| C-SPEC-1 | `dora_notification_clause` | Only DORA-prefixed leftover; implies DORA applicability. |
| C-SPEC-2 | Entire `ai_act_*` cluster | Useful locators; enum looks like a legal classification. |
| C-SPEC-3 | `nist_control_status` | Invented CSF control status. |
| C-SPEC-4 | `gdpr_*` booleans | Fine as locators; `gdpr_dpa_signed=true` on a public provider row is an overclaim. |
| C-SPEC-5 | `iso27701_*` names | Hide that they are also GDPR semantics. |
| C-SPEC-6 | stack `dora.pillar` | Finance-only taxonomy on a general catalog. |

---

## C-COMPLY — Mappings that imply compliance

| ID | Mechanism |
|----|-----------|
| C-COMPLY-1 | Listing `iso27001_controls` without status/evidence reads as “these controls are in place”. Public files warn; schema descriptions are weaker. |
| C-COMPLY-2 | `nist_control_status: implemented` plus Function tags reads as CSF certification. NIST does not certify. |
| C-COMPLY-3 | `ai_act_conformity_assessment: <date>` reads as “assessed/conformant”. It is a date field. |
| C-COMPLY-4 | `gdpr_dpia_required: false` reads as a completed Art. 35 decision. |
| C-COMPLY-5 | `certifications: [iso27001]` on AWS/Microsoft-class providers reads as all services/regions certified. |
| C-COMPLY-6 | Examples populate article numbers and Annex A IDs as if they were interpretations. |

Public compliance preambles are generally honest (“OSM is not a claim of compliance”). The **field names and examples** undo some of that honesty.

---

## C-EX — Examples teaching the wrong semantic model

Examples were **not modified**. Observations:

| ID | Where | Teaching error |
|----|-------|----------------|
| C-EX-1 | `examples/reference-enterprise/catalog/technology-stacks.yaml` | `togaf_domain: Security Architecture` — not one of TOGAF’s four standard domains. |
| C-EX-2 | same | `tbm_tower: Infrastructure` / `Management` / `Applications` — not aligned to TBM 5.0.1 Resource Tower names (Compute, Storage, Application, …). “Applications” happens to exist in 5.x; Infrastructure/Management do not as tower names. |
| C-EX-3 | same | GDPR **article numbers** on stacks invite legal interpretation. |
| C-EX-4 | same | `dora.criticality` and service criticality can be copied mechanically. |
| C-EX-5 | posture examples | AI Act `not-applicable` everywhere in some golden files — fine, but does not exercise the gated offering fields (under-teaching). |

---

## C-WEAK — One framework exposing another mapping’s weakness

| ID | Exposure |
|----|----------|
| C-WEAK-1 | **CSDM 5 Service Instance** makes any future temptation to encode environment as a *service* obviously wrong; environment is offering characteristic **or** instance (external). |
| C-WEAK-2 | **ITIL v5 Digital Product** pressure tests OSM-C-004: if OSM ever added Product, it would stop being a technological-service core. |
| C-WEAK-3 | **ArchiMate 4 generic Service** weakens “OSM = Technology Service” as a slogan; OSM must say *technological* in prose, not by ArchiMate class name. |
| C-WEAK-4 | **TBM 5 Solutions vs Resource Towers** weakens stack-level `tbm_tower` as the natural join to “service”. |
| C-WEAK-5 | **ISO 27701:2025 per-activity role** weakens offering-level `iso27701_pii_role` as a PIMS substitute. |
| C-WEAK-6 | **DORA ITS ranked supply chain** weakens `subcontractors[]` names as adequate TPRM. |
| C-WEAK-7 | **AI Act provider/deployer + Annex III use-case** weakens service-level `ai_act_risk_class` as a classification engine (use case ≠ technology offering). |
| C-WEAK-8 | **GDPR Art. 30 RoPA** weakens `gdpr_processing_activity: true` as privacy compliance. |

---

## C-PATH — Repository contradictions (process, not model)

| ID | Issue |
|----|-------|
| C-PATH-1 | Decision records still name `compatibility/`, root `COMPATIBILITY.md`, `schema/service.yaml`. Live tree is `models/`, `_internal/notes/COMPATIBILITY.md`, `schema/catalog/`. |
| C-PATH-2 | Freeze says public compatibility status is NOT ANALYZED for six frameworks that already have public mapping pages. |
| C-PATH-3 | OSM-M-005 status SUPERSEDED is easy to misread as “grain question gone”. It is not. |
| C-PATH-4 | Public `models/` and `_internal/notes/compatibility/` can diverge; notes are richer for TMF/ITIL/CSDM, poorer/outdated for ArchiMate. |

---

## Field-by-field mapping audit (required §12)

Compact form. Full meaning is in 00 and 03.

| Field | Why it exists | Source | Authoritative meaning now | OSM meaning | Grain OK? | Current? | Useful? | Duplicate? | Too specific? | Remain? |
|-------|---------------|--------|------------------------|-------------|-----------|----------|---------|------------|---------------|---------|
| `tbm_tower` | Finance join | TBM | Resource Tower 5.0.1 | L1 label | questionable | names stale | if updated | vs Solutions/Service | no | remain as mapping; update docs |
| `tbm_sub_tower` | Finance join | TBM | Sub-tower | L2 label | same | stale | if updated | same | no | remain |
| `togaf_domain` | EA join | TOGAF | B/D/A/T domain | free text | stack-only | yes | low | no | no | remain or characteristic |
| `iso27001` (stack) | Control hint | 27001 | Annex A | free text | dual with offering | 2022 yes | low | **yes** C-DUP-1 | no | unify or document |
| `iso27701` (stack) | NA/hint | 27701 | PIMS refs | free text | ok | must say 2025 | low | no | no | remain |
| `nist_csf` | Function tags | CSF 2.0 | Functions | enum list | dual | yes | locator | **yes** C-DUP-2 | mild | remain |
| `gdpr` (stack) | Article trivia | GDPR | Articles | free text | weak | yes | **low** | no | yes | reconsider |
| `dora.pillar` | Informal label | DORA | not official | 4 titles | weak | incomplete | low | no | yes | reconsider |
| `dora.criticality` | Stack label | DORA | CIF is not this | enum incl. `standard` | different grain OK | **token wrong** | low | hazard C-DUP-4 | yes | reconsider `standard` |
| `ai_act.contains_ai_systems` | Locator | AI Act | AI system present | bool | stack roll-up | yes | yes | related to service flag | mild | remain |
| `ai_act.max_risk_class` | Roll-up | AI Act | not a legal max | enum | derived? | enum weak | low | C-DUP-3 | yes | remain if derived |
| `ai_act.reference` | Pointer | — | — | string | ok | yes | low | no | no | remain |
| `iso27001_controls` | Join keys | 27001 | Annex A IDs | string list | offering | yes | yes | C-DUP-1 | no | remain |
| `iso27701_pii_role` | Processing role | 27701/GDPR | per activity | offering enum | **off** | 2025 still valid roles | yes | C-DUP-5 | name yes | remain; document |
| `iso27701_pii_categories` | Data types | 27701/GDPR | not this enum | offering list | ok-ish | weak enum | medium | C-DUP-6 | name yes | remain or map to privacy_classification |
| `iso27701_retention_days` | Retention | 27701/GDPR | purpose-based | int | coarse | yes | medium | no GDPR twin | name yes | remain |
| `nist_functions` | Function tags | CSF 2.0 | Functions | list | dual | yes | locator | C-DUP-2 | mild | remain |
| `nist_control_status` | Implementation | **OSM invention** | not CSF | enum | offering | n/a | dubious | no | **yes** | reconsider |
| `gdpr_processing_activity` | Locator | GDPR | RoPA ≠ bool | bool | offering | yes | yes | C-DUP-6 | prefixed | remain |
| `gdpr_dpia_required` | Signal | Art. 35 | DPIA ≠ bool | bool | offering | yes | yes | no | prefixed | remain |
| `gdpr_erasure_capable` | Capability | Art. 17 | right ≠ capability | enum | offering | yes | yes | no | prefixed | remain |
| `rto` `rpo` `resilience_*` | Recovery | many | RTO/RPO | duration/bool | offering | yes | **high** | no | no | remain |
| `operational_criticality` | Service criticality | many | ≠ DORA CIF | enum | service | yes | **high** | hazard with stack DORA | no | remain |
| `providers` | Who provides | many | ≠ arrangement | ids | S/O | yes | **high** | no | no | remain |
| `dora_notification_clause` | Clause flag | DORA | Art. 28 notice | bool | provider | yes | finance | no | **yes** | remain optional |
| `gdpr_dpa_signed` | DPA | Art. 28 | executed vs published | bool | provider | yes | dangerous | no | prefixed | remain; document |
| `ai_act_applicable` / `ai_act_risk_class` | Locator | AI Act | classification | bool/enum | service | enum weak | yes | C-DUP-3 | yes | remain |
| offering `ai_act_*` | Governance crumbs | AI Act | oversight, purpose, docs | mixed | offering | simplified | mixed | purpose vs GAP-003 | yes | remain gated; don’t expand |

**Should become Characteristic?** Location/region, process-vs-store, operating model, SLA strings, GPAI flag if ever needed — **yes, characteristics first**.

**Should be removed?** None without an OSM-M decision. Strongest *reconsider* list: stack `gdpr` articles, `dora.pillar`, `nist_control_status`, `dora.criticality` token `standard`.
