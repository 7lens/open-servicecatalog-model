# 03 — Compliance / governance mapping matrix

**Object:** frozen OSM 1.3.0  
**Classifications:** MAP | MAP + DOCUMENT | EXTERNAL | GAP CANDIDATE | AMBIGUOUS / DECISION REQUIRED  

OSM may *represent information relevant to* these frameworks. Completing a field is **not** compliance, certification, or legal advice.

---

## 1. ISO/IEC 27001:2022 + Amd 1:2024

### Version / currentness

ISO/IEC 27001:2022 (Ed. 3) + **Amd 1:2024** climate-action wording in 4.1/4.2. Annex A unchanged (93 controls, four themes). Amd 1 is **organizational ISMS context**, not a service-catalog attribute.

### Service vs organisation

| 27001 concern | Describes the service? | OSM |
|---------------|------------------------|-----|
| Clauses 4–10 ISMS (scope, leadership, planning, support, operation, performance, improvement) | No — organisation | **EXTERNAL** |
| Statement of Applicability | No — ISMS artefact | **EXTERNAL** |
| Risk treatment | No — ISMS | **EXTERNAL** |
| Annex A **organizational** (policies, roles, supplier relationships, asset mgmt, incident, continuity, classification) | Mixed: some controls *apply to* a service | Control **IDs** can hang off a service; the control system stays in GRC |
| Annex A **people** | Rarely a service property | **EXTERNAL** (HR) |
| Annex A **physical** | Facility services maybe | Usually **EXTERNAL**; data-center provider may be ICT Provider |
| Annex A **technological** (access, crypto, logging, backup, coding, cloud, …) | Often **about** how a technological service is built/run | Best OSM join: offering `iso27001_controls` as **references**, plus canonical classification / review / RTO |

### Are control IDs sufficient?

**As a join key: yes. As a security model: no.**

- IDs (`A.5.23`, `A.8.13`) are the internationally stable handle.
- They do not record applicability justification, implementation status, evidence, or owner.
- OSM `iso27001_controls` is a list of strings with **no schema for “implemented vs applicable vs inherited from ISMS”**.
- Stack `mappings.iso27001` is **free text**, offering field is a **list** — same concept, two shapes (**contradiction C-ISO-1**).

A stronger semantic mapping mechanism (control object with status, evidence, SoA pointer) would turn OSM into a GRC module. That fails Tests 4, 7, 8 as a *canonical catalog* concern. **Recommendation: keep IDs; document that GRC owns status/evidence.** Provenance on the posture row can point at the SoA.

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| ISMS / SoA / risk treatment | Management system | Organisation | — | — | **EXTERNAL** | Not a service definition. |
| Annex A control | Reference control | Control | `iso27001_controls` / stack `iso27001` | Offering / Stack | **MAP + DOCUMENT** | IDs only. Dual grain/type is a documentation/schema smell, not a new concept. |
| Information classification | Classify information | Asset/info | `data_classification` | Service posture | **MAP** | Same idea. OSM enum is enterprise-generic, not 27002’s scheme. |
| Asset inventory completeness | Know your assets | Asset | `asset_coverage` | Offering posture | **MAP** | Weak signal, not the inventory. |
| Supplier security (A.5.19–A.5.23) | Third-party IS | Supplier | ICT Provider fields + `providers` | Provider | **MAP** | Due-diligence dates, certs, audit flags — characterization. |
| ICT continuity (A.5.30) | Readiness | Service | `rto`/`rpo`/`resilience_*` / `resilience_tier` | Offering / Service | **MAP** | Canonical recovery. |
| Security review | Periodic review | Control ops | `last_security_review` | Offering posture | **MAP** | Date only. |
| Climate change (Amd 1) | Context of the org | Organisation | — | — | **EXTERNAL** | Not a service parameter. |
| Evidence of implementation | Audit evidence | Control | `provenance`, `resilience_evidence` | Posture | **MAP** (pointer) | Not a control library. |

---

## 2. ISO/IEC 27701:2025 (not 2019)

### Version / currentness

**ISO/IEC 27701:2025** (14 Oct 2025) is a **standalone PIMS**. 2019 was an extension of 27001/27002. OSM public text still describes the 2019 shape.

### 2025 semantics vs OSM fields

| 27701:2025 | OSM today | Valid? |
|------------|-----------|--------|
| PII controller / processor determined **per processing activity** (Clause 4.1) | `iso27701_pii_role` on **Offering** | **Partially.** Offering is a proxy for an activity, not the activity. Dual-role SaaS (controller for telemetry, processor for customer PII) cannot be expressed as one enum. |
| Joint controller | `joint-controller` | Still a recognised role (GDPR Art. 26). **MAP** if grain is accepted. |
| PII categories | `iso27701_pii_categories` closed enum | **Weak MAP.** Enum is a home-grown list, not 2025 Annex language and not GDPR Art. 9. |
| Retention | `iso27701_retention_days` | Characterization only. Real retention is purpose-specific (multiple periods). |
| Annex A.1/A.2/A.3 control IDs | No 27701 control-ID field (only free-text stack mapping) | **EXTERNAL** — PIMS SoA, or reuse 27001 pattern. Do not add a second control list without OSM-M-008 review. |
| Standalone PIMS (no 27001 required) | OSM still pairs 27001+27701 fields | Documentation: 27701 can apply without 27001. **Does not invalidate** the OSM fields. |

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| PIMS | Management system | Organisation | — | — | **EXTERNAL** | |
| Controller / processor / joint | Role for a processing | **Activity** | `iso27701_pii_role` | **Offering** | **MAP + DOCUMENT** + **AMBIGUOUS grain** | Same legal idea as GDPR Art. 4(7)(8). OSM has **no GDPR role field** — this *is* the role field (OSM-M-008). Grain mismatch vs activity/RoPA. |
| PII | Personal data | Data | `privacy_classification`, PII categories | Service / Offering | **MAP + DOCUMENT** | Overlap of three fields (privacy class, categories, gdpr_processing_activity). |
| Processing purpose | Why PII is processed | Activity | `ai_act_intended_purpose` only if AI | Offering | **GAP CANDIDATE** (GAP-003) | Purpose is cross-framework (GDPR, 27701, AI Act). Only AI-prefixed purpose exists. |
| PII principal rights operations | Access, erasure workflows | Process | `gdpr_erasure_capable` (capability only) | Offering | **EXTERNAL** (+ weak capability MAP) | |
| Retention | Storage limitation | Activity/purpose | `iso27701_retention_days` | Offering | **MAP + DOCUMENT** | Single integer cannot express purpose-based retention. |
| Privacy risk | PIMS risk process | Org/activity | — | — | **EXTERNAL** | |
| Evidence | PIMS evidence | Org | provenance | Posture | **MAP** pointer | |
| Relationship to 27001 | 2019: extension. 2025: standalone, A.3 security controls | Standard | 27001 fields remain separately useful | — | **MAP + DOCUMENT** | Update public text. Do not merge 27001 and 27701 fields. |

---

## 3. NIST CSF 2.0 + 2026 implementation / AI guidance

### Do not reduce to six Functions

CSF 2.0 structure:

| Layer | What it is | OSM today |
|-------|------------|-----------|
| **Functions** (6) | Govern, Identify, Protect, Detect, Respond, Recover | Stack `nist_csf` + offering `nist_functions` |
| **Categories** | Outcome groups (e.g. GV.OC, PR.DS) | not stored |
| **Subcategories** | Specific outcomes | not stored |
| **Organizational Profile** | Current vs target state | not stored |
| **Tiers** | Implementation sophistication (org) | not stored |
| **Informative references** | Mappings to 27001, etc. | not stored |
| **Community Profiles** | Sector overlays | not stored |

### Which layer belongs in OSM?

**Functions as optional tags are the only layer that survives Tests 4 and 7.** Categories/Subcategories are a control catalog. Profiles/Tiers are an assessment programme.

### AI-related CSF guidance (current)

- **IR 8596 Cyber AI Profile** (draft): how to *secure AI / use AI for cyber / thwart AI attacks* using CSF outcomes. This is a **community profile**, not a service attribute. **EXTERNAL.** OSM AI Act flags already mark “this service involves AI”.
- **SP 1353** (Aug 2026 draft): using generative AI to *produce CSF artefacts*. Irrelevant to OSM fields. **EXTERNAL.**

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| Function | Highest CSF outcome group | Org / system | `nist_csf` / `nist_functions` | Stack / Offering | **MAP + DOCUMENT** | Duplicate grain/fields (C-NIST-1). Function tags are not “implemented CSF”. |
| Category / Subcategory | Outcomes | Org/system | — | — | **EXTERNAL** | GRC/profile tool. |
| Organizational Profile | Current/target | Org | — | — | **EXTERNAL** | |
| Tiers | Maturity-like | Org | — | — | **EXTERNAL** | |
| `nist_control_status` | OSM invention | Offering | — | Offering | **MAP + DOCUMENT** / **reconsider** | **Not a CSF object.** Looks like certification. Estate D-028. Options in 07-D8. |
| Supply chain (CSF GV.SC) | SCRM outcomes | Org/supply | ICT Provider fields | Provider | **MAP** (partial) | Due diligence / concentration / subcontractors. Not a SCRM programme. |
| Cyber AI Profile | Profile overlay | Org/AI | `ai_act_applicable` as a *locator* | Service | **EXTERNAL** | Do not store IR 8596 subcategory lists. |

---

## 4. GDPR (2016/679 + EDPB 2025–2026)

### Do not reduce to article numbers

Stack `mappings.gdpr` as free-text article refs is the **weakest** GDPR mapping OSM has. The regulation’s service-relevant *concepts* are below.

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| Controller / processor / joint | Art. 4(7)(8), 26 | **Processing activity** | `iso27701_pii_role` | Offering | **MAP + DOCUMENT** | Same concept as 27701. Named ISO not GDPR (C-PRIV-1). |
| Processing activity / RoPA Art. 30 | Record of processing | Activity | `gdpr_processing_activity` bool | Offering | **MAP + DOCUMENT** | Boolean locator, **not** a RoPA. Overlaps privacy_classification. |
| Purpose | Art. 5(1)(b), 30(1)(b) | Activity | missing (except AI purpose) | — | **GAP CANDIDATE** (GAP-003) | |
| Data-subject categories | Art. 30(1)(c) | Activity | — | — | **EXTERNAL** | RoPA. |
| Personal-data categories | Art. 30(1)(c), Art. 9 | Activity | `iso27701_pii_categories` + `privacy_classification` | Offering / Service | **MAP + DOCUMENT** | Enum ≠ Art. 9. |
| Recipients | Art. 30(1)(d) | Activity | `providers` (subset: processors) | Service/Offering | **MAP** (partial) | Recipients include internal parties; OSM only ICT providers. |
| Third countries / transfers | Ch. V | Transfer | `data_processing_locations`, `headquarters` | Provider | **MAP** (weak) | Locations ≠ transfer mechanism (SCCs, adequacy). Mechanism is **EXTERNAL**. |
| Retention | Art. 5(1)(e), 30(1)(f) | Activity | `iso27701_retention_days` | Offering | **MAP** (weak) | See 27701. |
| Security measures Art. 32 | TOMs | Activity/system | classification, 27001 IDs, review date | mixed | **MAP** (locator) | Not the TOM library. |
| DPIA Art. 35 | Assessment | Activity | `gdpr_dpia_required` | Offering | **MAP + DOCUMENT** | Signal only. |
| Privacy by design/default Art. 25 | Obligation | Org/system | — | — | **EXTERNAL** | Process/architecture, not a catalog flag. |
| Processors / subprocessors Art. 28 | Contract + chain | Arrangement | `gdpr_dpa_signed`, `subcontractors` | Provider | **MAP + DOCUMENT** | DPA boolean overclaims (D-006). Subprocessors names-only. |
| Accountability / evidence Art. 5(2), 24 | Demonstrate compliance | Org | provenance | Posture | **MAP** pointer | |
| Pseudonymisation (EDPB 01/2025) | Safeguard | Processing | — | — | **EXTERNAL** | Technique; could be a characteristic if needed. Do not add a GDPR-prefixed field. |
| Erasure Art. 17 | Right | Activity | `gdpr_erasure_capable` | Offering | **MAP** | Capability of the **technological service**, useful for machines. Workflow EXTERNAL. |

**RoPA vs OSM:** purpose, data-subject categories, legal basis, recipients beyond ICT providers, transfer tools, DPO — **EXTERNAL**. OSM should remain a locator into a privacy system.

---

## 5. DORA — priority (Regulation + RTS 2024/1773 + ITS 2024/2956)

### Version / currentness

DORA applicable 17 Jan 2025. This mapping uses the Regulation plus **RTS 2024/1773** (contractual-arrangement policy) and **ITS 2024/2956** (RoI templates). 2026 RoI submissions use 31 Dec 2025 as reference date.

OSM is usable outside finance; DORA does not apply to every adopter. Fields must remain meaningful as **generic ICT third-party / resilience** facts (OSM-M-008).

### OSM-M-005 grain — evidence, not a decision

**Closed by OSM-M-010:** there is one who-provides relationship (`providers`). `dora_third_party_deps` must not return.

**Still open:** what *grain* that relationship represents versus DORA.

| Model | Grain of “who provides ICT” |
|-------|-----------------------------|
| OSM Service `providers` | Provider is intrinsic to the **service definition** |
| OSM Offering `providers` | Provider **distinguishes the variant** |
| DORA Art. 28 / RTS 2024/1773 | **Contractual arrangement** on the use of ICT services, especially those supporting a **critical or important function** |
| DORA ITS 2024/2956 RoI | Arrangement × ICT service × provider × (ranked) subcontractors × function; plus ultimate **parent undertaking** |

These are **not the same fact**:

1. “AWS underpins our Kubernetes **service definition**” → OSM Service `providers`.
2. “The **aws** offering is the AWS variant” → OSM Offering `providers`.
3. “Contract C-19 with Amazon Web Services EMEA SARL covers EKS + S3, supporting the payments CIF, with subcontractor X ranked 1” → **RoI**. OSM cannot store this without becoming a register of information.

**Evidence for maintainers:**

- OSM `providers` is a valid **feed** into RoI (which services/offerings a provider underpins).
- OSM `providers` is **not** a valid *replacement* for RoI (missing legal entity, LEI, licensed activity, function, arrangement identifiers, ranked supply chain).
- Dual placement (service and offering) is semantically justified inside OSM (intrinsic vs variant) and should not be collapsed.
- Putting DORA arrangement attributes on ICT Provider (contract dates, notification clause, exit flags) **collapses many arrangements onto one vendor row** (estate D-010).

Do **not** resolve whether to add an Arrangement entity. Record as **AMBIGUOUS D1**.

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| Critical or important **function** | DORA CIF | Business function | — | — | **EXTERNAL** | OSM has no business function. `operational_criticality` is **service** criticality, not CIF. Do not rename. |
| ICT services | Services provided by ICT TPP | Service under a contract | OSM Service / Offering | Catalog | **MAP + DOCUMENT** | Closest technological object. RoI ICT-service taxonomy (S01…S19 etc.) is a **reporting code list**, not an OSM enum. |
| ICT third-party provider | Legal person providing ICT | Legal entity | ICT Provider | Provider | **MAP + DOCUMENT** | OSM `name`+`headquarters` collapse legal seller, CTPP designation, parent (estate D-003). |
| Provider location | Where the TPP is located | Entity | `headquarters` | Provider | **MAP** (partial) | One ISO country. Dual HQ / contracting country lost. |
| Parent-company location | RTS 2024/1773 explicit | Parent entity | missing | — | **GAP CANDIDATE** (GAP-004) / often **EXTERNAL** | Recurs as legal-parent identity, not only DORA. See tests in 05. |
| Location from which ICT services are provided | Ops location | Arrangement/service | missing | — | **AMBIGUOUS** | Distinct from HQ and from data location. |
| Data **processing** location | Where data is processed | Arrangement/service | `data_processing_locations` | **Provider** | **MAP + DOCUMENT** + grain issue | Provider list is a **capability map**, not actual residency (D-009). |
| Data **storage** location | RTS/ITS distinguish process vs store | Arrangement/service | collapsed into processing list | Provider | **GAP CANDIDATE** (GAP-001) | Also GDPR/27701 relevant. |
| ICT concentration risk | Over-reliance | Entity / function | `concentration_risk` | Provider | **MAP + DOCUMENT** | Often assessed at *firm* vs provider, not as a provider boolean. |
| Substitutability / transferability | RTS: transfer to another TPP | Arrangement/service | `substitutability` | Provider | **MAP + DOCUMENT** | Market vs customer-specific. |
| Due diligence | Pre-contract assessment | Arrangement | `last_risk_assessment`, `risk_level` | Provider | **MAP** | Dates/severity, not the file. |
| Financial/technical capability | RTS selection criteria | Provider | — | — | **EXTERNAL** | Vendor risk system. |
| Security assurance / certifications | RTS / Art. 28 | Provider/service-scoped | `certifications[]` | Provider | **MAP + DOCUMENT** | Unscoped strings overclaim (D-001). |
| Subcontractors / supply chain | ITS B_05.02 ranked chain | Arrangement × service | `subcontractors[]` names; `subcontracting_allowed` | Provider | **MAP + DOCUMENT** | No rank, LEI, per-service chain. Remainder **EXTERNAL** (RoI). |
| Contractual arrangements | Art. 28 | Arrangement | `contract_*` on Provider | Provider | **AMBIGUOUS** (D1) | Wrong grain vs RoI. |
| Audit / access rights | Art. 28(4) | Arrangement | `audit_rights` | Provider | **MAP + DOCUMENT** | Boolean vs report-based (D-007). |
| Business continuity | Art. 11 etc. | Function/service | `rto`/`rpo`/`resilience_tier` | Offering/Service | **MAP** | Canonical. |
| Resilience testing / TLPT | Ch. IV | Entity programme | `resilience_tested`, dates, evidence | Offering | **MAP** (signal) | TLPT programme **EXTERNAL**. |
| Exit strategy | Art. 28(8) | Arrangement | `exit_strategy_documented` / `_tested` | Provider | **MAP + DOCUMENT** | Grain: provider vs arrangement. |
| Termination | Contract | Arrangement | `contract_end`, `notice_period_days` | Provider | **MAP** (weak) | |
| Incidents | Ch. III | Event | — | — | **EXTERNAL** | Incident system. `response_target` is an expectation, not an incident. |
| Register of information | ITS 2024/2956 | Supervisory dataset | — | — | **EXTERNAL** | OSM is not the RoI (compliance/DORA.md already). |
| Lifecycle of TPP arrangements | Onboarding to exit | Arrangement | definition `lifecycle_state` is **not** this | — | **EXTERNAL** | Do not overload Service lifecycle. |
| `mappings.dora.pillar` | OSM label | Stack | four titles | Stack | **MAP + DOCUMENT** / **reconsider** | Informal; omits information-sharing; DORA does not call them pillars. |
| `mappings.dora.criticality` = standard | OSM enum | Stack | not in DORA | Stack | **contradiction** | DORA: critical or important **functions**. `standard` is OSM. Different grain from `operational_criticality` is OK; the token is not. |
| `dora_notification_clause` | Contract clause flag | Provider | DORA-specific | Provider | **MAP** as framework flag | Only remaining DORA-prefixed field. Keep as mapping, or move to contract system (D9). |
| Who-provides | ICT TPP association | see M-005 | `providers` | Service/Offering | **MAP** | Canonical (OSM-M-010). Grain vs arrangement = D1. |

---

## 6. EU AI Act (2024/1689) + 2026 Commission guidance

### Distinguish

```text
AI system governance (provider/deployer, GPAI, conformity, registration, incidents)
        vs
technology service catalog semantics (does this technological service include an AI system, and what class was labelled)
```

OSM may do the second. It must not become the first.

### Act concepts vs OSM enum

The Act’s operative classes are approximately:

- **Prohibited practices** (Art. 5) — in force 2 Feb 2025; Commission guidelines C(2025) 5052.
- **High-risk AI systems** (Art. 6 + Annex I / Annex III) — draft classification guidelines 19 May 2026; application postponed (Annex III → 2 Dec 2027; Annex I → 2 Aug 2028).
- **Transparency obligations** (Art. 50) — certain systems (chatbots, deepfakes, emotion recognition exceptions, etc.).
- **GPAI models** (Ch. V) — obligations 2 Aug 2025; Commission enforcement 2 Aug 2026; systemic-risk subset.
- Residual systems — codes of conduct; Commission language “minimal to no risk”.

OSM enum `unacceptable | high-risk | limited-risk | minimal-risk | not-applicable`:

- `unacceptable` ≈ prohibited — **dangerous if used as a catalog label for a live service** (a prohibited system should not be in production catalog as a managed offering without an explicit non-compliance/exception process).
- `high-risk` ≈ Art. 6 — **MAP** if understood as *labelled class, not a legal determination*.
- `limited-risk` ≈ informal name for Art. 50 transparency systems — **not an Act defined class**.
- `minimal-risk` ≈ residual — **not a defined class**.
- **GPAI / systemic risk** — **missing**, and should probably stay **EXTERNAL** (model governance, not service catalog) unless the OSM Service *is* a GPAI model offering.

Provider vs **deployer** (Art. 3): OSM `accountable` is Service Owner, not AI Act role. Putting `ai_act_role: provider|deployer` would be framework-specific and often **wrong grain** (the enterprise is deployer of a vendor model *and* provider of an internal system). **EXTERNAL** / estate D-022.

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| AI system definition | Art. 3 + Commission definition guidelines | System | `ai_act_applicable` / stack `contains_ai_systems` | Service / Stack | **MAP + DOCUMENT** | Locator. Dual grain (stack max vs service). |
| Provider / deployer / product manufacturer | Art. 3 roles | Actor | — | — | **EXTERNAL** | AI governance file, not catalog. |
| AI literacy Art. 4 | Org duty | Org | — | — | **EXTERNAL** | |
| Prohibited practices Art. 5 | Bans | Practice/system | `ai_act_risk_class=unacceptable` | Service | **MAP + DOCUMENT** | Token is misleading; prohibited ≠ a “risk class” to operate under. |
| High-risk Art. 6 / Annex I / III | Classification | System + use case | `high-risk` | Service | **MAP + DOCUMENT** | Use case (Annex III) is often **not** a property of the technology service alone (HR screening vs generic LLM platform). |
| GPAI / systemic risk | Model regime | Model | — | — | **EXTERNAL** | Unless maintainers want a characteristic `gpai_model`. Default: out. |
| Transparency Art. 50 | Disclose AI / synthetic content | System | `ai_act_transparency_level` | Offering | **MAP + DOCUMENT** | Enum (explicit/implicit/none) is a simplification of Art. 50. |
| Human oversight Art. 14 | High-risk requirement | System | `ai_act_human_oversight` | Offering | **MAP + DOCUMENT** | HITL/HOTL/HIC is industry jargon, not the Act’s wording. Useful machine signal. |
| Technical documentation Art. 11 / Annex IV | File | System | — | — | **EXTERNAL** | Pointer via provenance. |
| Logging Art. 12 | Record-keeping | System | — | — | **EXTERNAL** | Could be a characteristic; not justified as core. |
| Conformity assessment Art. 43 | Procedure | System | `ai_act_conformity_assessment` **date** | Offering | **MAP + DOCUMENT** | Date ≠ assessment. Easy to read as “certified”. |
| Registration Art. 49 | EU database | System | — | — | **EXTERNAL** | |
| Incident reporting Art. 73 | Event | System | — | — | **EXTERNAL** | |
| Cybersecurity Art. 15 | High-risk requirement | System | 27001 / NIST / classification | mixed | **MAP** via existing security fields | Do not add `ai_act_cybersecurity`. |
| Training/data documentation | Data governance | System | `ai_act_training_data_doc` | Offering | **MAP** | Flag only. |
| Intended purpose | Art. 3 / high-risk | System | `ai_act_intended_purpose` | Offering | **MAP** | Also feeds GAP-003 (generic purpose). |
| Timeline / Omnibus postponements | Application dates | Law | — | — | **EXTERNAL** | Documentation of mappings should not freeze Aug 2026 as *the* high-risk date. |

Offering AI fields gated on `ai_act_applicable` is **correct** (validation rule 6).

---

## Compliance-field audit (compact; full prose in 06)

| Field | Still current? | Still useful? | Too framework-specific? | Remain? |
|-------|----------------|---------------|-------------------------|---------|
| stack `iso27001` free-text | 2022 IDs yes | weak vs list | no | Remain or unify with offering list (documentation) |
| `iso27001_controls` | 2022 yes | yes as join keys | no | Remain |
| stack `iso27701` | text must say 2025 | weak | no | Remain as NA flag |
| `iso27701_pii_*` | roles still valid; categories weak | yes | name is ISO-specific for a GDPR concept | Remain; document dual use; grain D2 |
| `nist_csf` / `nist_functions` | CSF 2.0 Functions yes | locator only | Function names are CSF-specific | Remain one grain or document both |
| `nist_control_status` | not a CSF object | dubious | yes (fake control status) | **Reconsider** (D8) |
| stack `gdpr` articles | articles stable | low | yes | Reconsider vs dropping article trivia |
| `gdpr_processing_activity` / `dpia` / `erasure` | yes | yes as locators | prefixed | Remain; document overlap with privacy_classification |
| `gdpr_dpa_signed` | yes | dangerous if true on public catalogs | prefixed | Remain; document D-006 |
| `rto`/`rpo`/`resilience_*`/`operational_criticality`/`providers` | yes | high | no (canonical) | Remain |
| stack `dora.pillar` / `dora.criticality` | informal | low | yes | **Reconsider** (D9) |
| `dora_notification_clause` | yes | finance-only | yes | Remain as optional mapping or move out |
| Provider contract/exit/concentration | yes as characterization | yes | mixed DORA-flavoured | Remain; document grain |
| `ai_act_*` set | Act current; enum not legal taxonomy | locator useful | yes | Remain with documentation; do not expand to GPAI/deployer |

---

## Cross-compliance recurrence (see 04)

Criticality, recovery objectives, testing evidence, third-party identity, location, substitutability, auditability, classification of data vs system, processing role, purpose, retention, AI applicability.
