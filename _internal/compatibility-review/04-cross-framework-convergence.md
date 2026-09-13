# 04 — Cross-framework convergence

Concepts below appear **independently** in multiple frameworks. Those are the strongest candidates for canonical OSM semantics (OSM-M-004 / OSM-M-008). Single-framework leftovers belong in mappings or outside OSM.

**Evidence strength:** HIGH = 4+ independent families; MEDIUM = 2–3; LOW = mostly one family plus echo.

| Canonical concept candidate | Frameworks supporting it | Existing OSM representation | Strength | Recommendation |
| --------------------------- | ------------------------ | --------------------------- | -------- | -------------- |
| Stable **service definition** vs **runtime instance** | TMF633 spec vs TMF638; CSDM 5 TMS vs Service Instance; ITIL catalogue vs live CI; OSM-M-003 | OSM Service = definition; instance out of scope | HIGH | **Keep.** Document CSDM 5 rename. Do not add Instance. |
| **Requestable variant** of a service | ITIL offering; CSDM TMSO; TMF characteristics / product offering; OSM Offering | Service Offering + characteristics | HIGH | **Keep.** Do not hard-code dimensions. |
| **Who is accountable** for the service | ITIL service owner; CSDM Service Owner; ISO 27001 roles; GDPR/27701 accountability (different: processing) | `accountable` | HIGH | **Keep.** Do not merge with `financial_owner` or AI Act deployer. |
| **Who provides** the technology (third party) | ITIL supplier; CSDM Technology Provider; ArchiMate Actor; DORA ICT TPP; GDPR processor; TMF relatedParty | `providers` → ICT Provider | HIGH | **Keep one relationship.** Arrangement grain is a separate question (D1). |
| **Definition lifecycle / validity** | TMF lifecycleStatus+validFor; CSDM 5 Life Cycle Stage; OSM-M-002 | `lifecycle_state`, `version`, `valid_from`/`valid_to` | HIGH | **Keep on Service only.** Do not import ITIL 8-activity or CSDM stage enums. |
| **Service-level expectations** (availability, response, resolution) | ITIL SLM; CSDM commitments; ISO 27001 continuity; DORA resilience | posture targets; hours as characteristics | HIGH | **Keep split:** targets vs hours. SLA objects stay EXTERNAL. |
| **Recovery objectives** RTO/RPO | DORA; ISO 27001 A.5.30; NIST Recover; TBM storage offerings mention RPO; ITIL continuity | `rto`, `rpo` + `resilience_tier` | HIGH | **Keep canonical.** No framework-prefixed copies. |
| **Resilience testing / evidence** | DORA Ch. IV; ISO 27001; NIST Recover | `resilience_tested`, dates, evidence | HIGH | **Keep as posture signals.** Test programmes EXTERNAL. |
| **Operational / functional criticality** | DORA CIF (function); OSM service criticality; ISO business continuity; ITIL priority | `operational_criticality`; stack `dora.criticality` | MEDIUM–HIGH | **Keep service criticality.** Do not treat it as DORA CIF. Reconsider stack DORA criticality token `standard` (D9). |
| **Data classification** vs **system security classification** | ISO 27001; GDPR; DORA data; NIST PR.DS | `data_classification` + `security_classification` | HIGH | **Keep both** (genuinely different subjects, same enum by design). |
| **Privacy / PII presence** | GDPR; ISO 27701; ISO 27001 classification; DORA data | `privacy_classification` + PII categories + `gdpr_processing_activity` | HIGH | **Convergence is real; OSM has three overlapping locators.** Decision D3 (consolidate vs keep). |
| **Controller / processor role** | GDPR Art. 4; ISO 27701:2025 per activity; DORA/processor contracts | `iso27701_pii_role` only | HIGH | **Keep one field** (OSM-M-008). Rename-or-alias is documentation (D2). Grain vs RoPA is D2. |
| **Processing / intended purpose** | GDPR Art. 5/30; ISO 27701; AI Act intended purpose; TMF spec description | only `ai_act_intended_purpose` | HIGH | **GAP-003.** Strongest *missing canonical* after location split. Prefer generic purpose over more AI-prefixed fields. |
| **Retention** | GDPR storage limitation; ISO 27701; ISO 27001 deletion A.8.10 | `iso27701_retention_days` | MEDIUM | **Keep as characterization.** Full retention schedule EXTERNAL. Name is ISO-specific. |
| **Geographic / data location** | DORA RTS (provider, parent, process, store, provision); GDPR transfers; ISO 27701 transfers; CSDM location on offerings | `headquarters` + `data_processing_locations` | HIGH | **Partial.** GAP-001 storage vs process; parent location GAP-004; actual vs capability D-009. |
| **Substitutability / exit** | DORA RTS transferability + exit; ISO supplier; ITIL supplier strategy | `substitutability`, exit flags | MEDIUM | **Keep** as provider characterization. Arrangement grain documented. |
| **Concentration** | DORA; operational risk; TBM vendor | `concentration_risk` | MEDIUM | **Keep** with documentation that it is often firm-level. |
| **Auditability / assurance evidence** | DORA audit rights; GDPR Art. 28; ISO 27001/27701 evidence; AI Act technical file | `audit_rights`, `certifications`, provenance, `resilience_evidence` | HIGH | **Keep pointers.** Do not store certificates as proof (D-001). **GAP-005:** provenance not attachable to ICT Provider. |
| **Subcontractor chain** | DORA ITS B_05.02; GDPR Art. 28(2); ISO 27701 processor controls | names list + allowed flag | MEDIUM | **Keep coarse flags.** Ranked chain EXTERNAL (RoI/DPA). |
| **Security control join keys** | ISO 27001 Annex A; NIST informative refs; sometimes TBM Risk & Compliance | `iso27001_controls`, NIST Functions | MEDIUM | **Keep IDs/Functions as joins.** Status/SoA EXTERNAL. Reconsider `nist_control_status`. |
| **AI-system applicability** | EU AI Act; NIST IR 8596; ITIL v5 AI-native ops; TBM AI solution type; CSDM Data/AI Service Instance | `ai_act_applicable` + stack contains_ai | MEDIUM–HIGH | **Keep locator.** Do not import GPAI/deployer/Annex III taxonomy. |
| **Human oversight of automated systems** | AI Act Art. 14; GDPR Art. 22; ISO 27701 automated decision notes | `ai_act_human_oversight` | MEDIUM | **Framework-named.** Useful beyond AI Act (automated decisions). Decision D10: keep prefixed vs generalize. |
| **Financial characterization** (cost pool, chargeback) | TBM 5; ITIL charging; OSM posture | `cost_pool`, `chargeback_model`, `unit_cost`, `financial_owner` | MEDIUM | **Keep characterization.** TBM engine EXTERNAL. Fix TBM 5 names/grain (D7). |
| **Automation / self-service of the offering** | ITIL request; CSDM request catalog; TMF configurable characteristics | `self_service`, automation fields, `configurable` on characteristics | MEDIUM | **Keep.** |
| **Service-to-service dependency** | TMF specRelationship; CSDM rel; ArchiMate Serving; ITIL supporting services; DORA ICT service supporting a function | **forbidden** | HIGH | **GAP-002.** Strongest *relationship* candidate. Conflicts with OSM-C-004/005 freeze. Human decision D4. |
| **Consumers / business service / digital product / value stream** | ITIL v5 product; CSDM Business Service; TBM Consumer Layer; ArchiMate business domain; TOGAF Business Architecture | out of scope | HIGH | **Correctly EXTERNAL.** v5/CSDM 5/TBM 5 all *increased* this layer — that strengthens OSM’s technological boundary, it does not weaken it. |
| **Contractual arrangement as an entity** | DORA RoI; GDPR Art. 28 contract; ISO supplier agreements | contract fields **on Provider** | MEDIUM | **AMBIGUOUS D1.** Not a technological-service entity per Test 1 unless scoped as “link attributes”. Prefer EXTERNAL contract system. |

### What did *not* converge enough to be canonical

| Idea | Why it stays mapping/external |
|------|-------------------------------|
| TMF ServiceCandidate / Category / Catalog entities | One ecosystem (plus product catalog). OSM dataset is enough. |
| CSDM Service Instance siblings | Runtime/CMDB. |
| ArchiMate generic Service *element id* | EA repository join via provenance. |
| TOGAF ADM / ABB ids | Method. |
| TBM Consumer Layer, Cost Pool engine | Finance system. |
| NIST Categories, Profiles, Tiers | Assessment programme. |
| GDPR legal basis, DPO, SCCs | Privacy system. |
| DORA RoI templates, LEI, licensed activities | Supervisory reporting. |
| AI Act GPAI, registration, conformity file | AI governance system. |
| ISO 27001 Amd 1 climate | ISMS context. |
