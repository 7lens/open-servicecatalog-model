# 05 — Gap register

Investigation-time candidates (2026-09-13). The findings below remain
as evidence. **Disposition after accepted decisions** is authoritative
for what OSM will do.

## Classification (A–E)

| Class | Meaning |
|-------|---------|
| **A** | Current OSM capability (already representable) |
| **B** | Documentation / characteristic-convention gap (now closed in spec) |
| **C** | Mapping gap (framework docs, not schema) |
| **D** | Future optional schema evolution |
| **E** | Intentionally external — no schema change |

| ID | Concept | Class | Disposition (ACCEPTED 2026-09-13) |
|----|---------|-------|-----------------------------------|
| GAP-001 | Storage location vs processing location | **B** | Characteristic convention (`processing_location` ≠ `storage_location`). No immediate schema change. OSM-D-001. |
| GAP-002 | Service→Service dependency | **E** | Intentionally excluded. No `depends_on` etc. OSM-C-008. |
| GAP-003 | Canonical purpose | **B** (+ **D** only if proven load-bearing) | Characteristic `name: purpose` now. No top-level field. OSM-D-002. |
| GAP-004 | Provider legal parent | **E** | External (legal-entity / RoI). No schema change. |
| GAP-005 | ICT Provider provenance | **D** | Reuse existing `provenance` object. Schema does not currently allow it on ICT Provider. OSM-M-011 principle ACCEPTED; **not implemented**. No per-field provenance. |
| GAP-006 | Actual offering residency vs provider capability | **B** | Characteristic semantics. Provider `data_processing_locations` = capability. OSM-D-001. |
| GAP-007 | Contractual Arrangement entity | **E** | Rejected as OSM core. DORA RoI/arrangement remains external. OSM-C-007. |

Nothing in the original write-up below was an accepted decision at
investigation time. Do not re-open A/B/E items as schema work without
a new OSM-M.

---

## GAP-001

**Concept:** Distinct **data-storage location** vs **data-processing location**

**External terminology:** DORA RTS 2024/1773 “location where the data is processed and stored”; GDPR Ch. V (transfers often care about where data *rests*); ISO 27701 transfer/storage; cloud “data at rest vs in use”

**Frameworks:** DORA (primary), GDPR, ISO 27701, ISO 27001 (A.8.10/A.8.13), CSDM location on offerings

**Underlying semantic meaning:** Processing and storage can be in different countries/regions for the same ICT service (e.g. compute in `ie`, backups in `de`). Collapsing them loses a resilience and transfer fact.

**Why existing OSM is insufficient:** ICT Provider.`data_processing_locations` is a single list, at **provider** grain, documented as a capability map. It cannot say “this offering stores in X and processes in Y”.

**Candidate grain:** Offering characteristic **or** Offering Posture **or** Provider (two lists). Prefer **Offering** for actual residency; keep Provider list as capability.

**Existing fields considered:** `data_processing_locations`; offering characteristics `location`; stack mappings — insufficient because processing≠storage and provider≠offering.

**Cross-framework evidence:** HIGH (04)

**Enterprise universality:** HIGH (any multi-region SaaS/cloud estate)

**Machine-readability value:** HIGH (residency, transfer, concentration reasoning)

**Complexity cost:** LOW if two characteristics or one posture pair of lists; MEDIUM if a location object with purpose=process|store

**Eight tests:** 1 yes (Provider/Offering/Posture). 2 yes (useful without DORA). 3 yes. 4 yes. 5 no adequate existing split. 6 Offering for actual, Provider for capability. 7 yes if not a new entity. 8 yes.

**Recommendation:** **ACCEPT CANDIDATE** as a *documentation + characteristic convention* now; **schema pair of fields** only if maintainers want a canonical name.

**Human decision required:** **YES** (D5)

---

## GAP-002

**Concept:** First-class **Service → Service** (or Service → Offering) **dependency**

**External terminology:** TMF `serviceSpecRelationship`; CSDM service relationships; ArchiMate Serving/Realization; ITIL supporting services; DORA “ICT services supporting a critical or important function” (function is external, ICT-to-ICT still appears)

**Frameworks:** TMF633, CSDM 5, ArchiMate 4, ITIL v5, DORA (partial)

**Underlying semantic meaning:** One technological service requires another (identity, network, logging, KMS). Distinct from `providers` (who sells/operates).

**Why existing OSM is insufficient:** Validation **forbids** `depends_on` / `consumes` / etc. `providers` must not be misused for Entra→Teams (estate D-014, OSM-M-010).

**Candidate grain:** Relationship (new, not a new *entity*). Ends: Service and/or Offering.

**Existing fields considered:** `providers` — wrong semantic. Characteristics — not graph-queryable. Provenance — not a dependency.

**Cross-framework evidence:** HIGH

**Enterprise universality:** HIGH

**Machine-readability value:** HIGH (blast radius, concentration, automation)

**Complexity cost:** HIGH (graph, cycles, versioning, offering-level deps, freeze + OSM-C-004/005)

**Eight tests:** 1 yes (relationship involving Service). 2 yes. 3 yes. 4 yes. 5 no. 6 Relationship. 7 **tension** — smallness vs usefulness. 8 yes.

**Recommendation:** **DEFER**. Do not add during freeze. Reopen only with a concrete interoperability requirement (already OSM-C-004). If reopened, a **minimal directed `depends_on: [service_id]`** on Service is the smallest option; offering-level and typed relationships (migration/exclusivity) should stay out.

**Human decision required:** **YES** (D4) — even to confirm continued exclusion.

---

## GAP-003

**Concept:** Canonical **purpose** of the service’s data/AI processing (not only AI Act)

**External terminology:** GDPR purpose; ISO 27701 processing purpose; AI Act intended purpose; TMF specification description (weaker)

**Frameworks:** GDPR, ISO 27701:2025, EU AI Act

**Underlying semantic meaning:** Why the technological service processes data / exists as an automated system. Distinct from `description` (what it is) and from legal basis (why processing is lawful).

**Why existing OSM is insufficient:** Only `ai_act_intended_purpose` (offering, gated on AI applicability). Non-AI personal-data services have no purpose field. Adding more `gdpr_purpose` would violate OSM-M-008.

**Candidate grain:** Service or Offering. Offering if purpose varies by variant (EU vs US processing). Characteristic `purpose` is a valid non-schema path.

**Existing fields considered:** `description` — not a typed purpose. `ai_act_intended_purpose` — AI-only, wrong name for the generic concept.

**Cross-framework evidence:** HIGH

**Enterprise universality:** HIGH

**Machine-readability value:** MEDIUM–HIGH (RoPA join, AI classification, minimization)

**Complexity cost:** LOW (one optional string) to MEDIUM (purpose vs legal basis confusion)

**Eight tests:** 1 yes. 2 yes. 3 yes. 4 yes. 5 AI field is a **subset**, not coverage. 6 Service default, Offering if variants differ. 7 yes if unprefixed and optional. 8 yes.

**Recommendation:** **ACCEPT CANDIDATE**. Prefer **one unprefixed optional `purpose`** (or mandated characteristic name) and map AI Act / GDPR / 27701 onto it. Do **not** add `gdpr_purpose`.

**Human decision required:** **YES** (D11)

---

## GAP-004

**Concept:** **Legal parent** (name and/or location) of an ICT Provider, distinct from the contracting/HQ entity

**External terminology:** DORA RTS “location of the ICT TPP or … parent company”; ITS RoI “ultimate parent undertaking”; corporate groups (Microsoft/GitHub, IBM/Red Hat)

**Frameworks:** DORA (strong); general vendor-risk / concentration (weaker but real)

**Underlying semantic meaning:** The seller you contract with is not always the parent that creates concentration or sanctions exposure.

**Why existing OSM is insufficient:** Single `name` + `headquarters`. No parent id, no parent country, no LEI.

**Candidate grain:** Provider (optional parent_id referencing another ICT Provider) **or** EXTERNAL legal-entity register.

**Existing fields considered:** `headquarters`, `name`, `concentration_risk` — collapse the distinction.

**Cross-framework evidence:** MEDIUM (DORA + common vendor practice; not in ITIL/TMF/ArchiMate as a field)

**Enterprise universality:** MEDIUM (high in regulated finance; medium elsewhere)

**Machine-readability value:** MEDIUM

**Complexity cost:** MEDIUM (graph of legal entities; LEI; CTPP)

**Eight tests:** 1 Provider yes. 2 **weak** — much weaker if DORA disappears (Test 2 stress). 3 partial. 4 medium. 5 no. 6 Provider or EXTERNAL. 7 adding full legal-entity model **fails smallness**. 8 medium.

**Recommendation:** **DEFER / likely EXTERNAL**. Document the collapse. Optional `parent_provider_id` is the smallest *if* finance adopters must stay inside OSM. LEI/CTPP stay out (estate D-003/D-004).

**Human decision required:** **YES** (D12)

---

## GAP-005

**Concept:** **Provenance on ICT Provider** (reuse existing structure)

**External terminology:** evidence, source system, last verified — ISO, DORA due diligence, GDPR accountability, AI Act documentation pointers

**Frameworks:** ISO 27001/27701, DORA, GDPR, EU AI Act, OSM-M-007 (structure already exists)

**Underlying semantic meaning:** Provider master data (locations, certs, DPA, risk_level) needs the same trust metadata as services.

**Why existing OSM is insufficient:** Provenance may attach to Service, Offering, postures — **not** ICT Provider. Estate D-025.

**Candidate grain:** Provenance nested on Provider (no new entity)

**Existing fields considered:** `last_risk_assessment` — only a date. `certifications` — unscoped claims without source.

**Cross-framework evidence:** HIGH (auditability convergence)

**Enterprise universality:** HIGH

**Machine-readability value:** HIGH

**Complexity cost:** LOW

**Eight tests:** 1 yes. 2 yes. 3 yes. 4 yes. 5 provenance exists but **cannot attach**. 6 Provenance. 7 yes — reuse. 8 yes.

**Recommendation:** **ACCEPT CANDIDATE**. Smallest freeze-compatible model change later: allow existing `provenance` on ICT Provider.

**Human decision required:** **YES** (D13) — schema change, so explicit OSM-M after freeze.

---

## GAP-006

**Concept:** **Actual residency / region of an Offering** as distinct from provider *capability* locations

**External terminology:** DORA “location from where the ICT services are provided”; GDPR transfer; cloud region; CSDM offering location

**Frameworks:** DORA, GDPR, CSDM, ITIL offering dimensions

**Underlying semantic meaning:** AWS *can* process in many countries; *this offering* is `eu-west-1`.

**Why existing OSM is insufficient:** Locations live on Provider. Characteristics *can* already hold `region` / `location` (OSM-M-001). The gap is **canonical convention**, not a missing type.

**Candidate grain:** Offering Characteristic (preferred) vs new posture fields

**Existing fields considered:** characteristics — **sufficient if documented**. Provider list — wrong grain.

**Cross-framework evidence:** HIGH

**Enterprise universality:** HIGH

**Machine-readability value:** HIGH **if** a reserved characteristic name exists; LOW if every adopter invents `region` vs `location` vs `data_residency`

**Complexity cost:** LOW (documentation) / MEDIUM (reserved names)

**Eight tests:** 1 yes. 2 yes. 3 yes. 4 yes. 5 **yes, via characteristics** — Test 5 says reuse. 6 Offering. 7 documentation preserves smallness. 8 yes with reserved names.

**Recommendation:** **REJECT as schema gap; ACCEPT as documentation convention** (MAP + DOCUMENT). Pair with GAP-001 for process vs store.

**Human decision required:** **YES** (D5 covers both)

---

## GAP-007

**Concept:** **Contractual arrangement** (or arrangement-scoped attributes) between the enterprise and an ICT Provider for a Service/Offering

**External terminology:** DORA contractual arrangement / RoI; GDPR Art. 28 processing agreement; ISO supplier agreement

**Frameworks:** DORA, GDPR, ISO 27001 supplier theme

**Underlying semantic meaning:** Contract C binds provider P to ICT services S supporting (external) function F, with dates, audit, exit, notification.

**Why existing OSM is insufficient:** Contract fields hang on **Provider**, so one row cannot represent two contracts or contract×service differences.

**Candidate grain:** New entity **or** EXTERNAL contract/GRC system with join on `contract_ref` / provider id / service id

**Existing fields considered:** `contract_*`, `dora_notification_clause`, exit flags, `audit_rights` — present but wrong grain.

**Cross-framework evidence:** MEDIUM–HIGH

**Enterprise universality:** HIGH in procurement; OSM Test 7 **fails** if a full arrangement entity is added (OSM becomes a contract register).

**Machine-readability value:** HIGH for DORA RoI feed; otherwise join is enough

**Complexity cost:** HIGH for new entity; LOW for “fields are hints, system of record is external”

**Eight tests:** 1 borderline (arrangement is not Stack/Service/Offering/Provider/Posture/Characteristic/Provenance — only a *relationship involving* them). 2 mixed. 3 yes. 4 yes. 5 partial, wrong grain. 6 Relationship/new entity/EXTERNAL. 7 new entity fails smallness. 8 high only for RoI.

**Recommendation:** **REJECT new entity. DEFER field moves.** Keep OSM-M-010 `providers`. Document that contract attributes are **characterization, not RoI**. Optional later: strip contract fields from Provider and leave only `contract_ref` as a pointer.

**Human decision required:** **YES** (D1)

---

## Rejected as OSM gaps (failed tests)

| Idea | Why not a GAP CANDIDATE |
|------|-------------------------|
| NIST Categories/Subcategories/Profiles/Tiers | Test 7/4 — GRC programme |
| ISO 27001 control *implementation* objects | Test 7 — GRC |
| GDPR legal basis, DPO, SCC type, RoPA rows | Test 1/7 — privacy system |
| DORA RoI templates, LEI, EUID, licensed activities, CIF register | Test 4/7 — supervisory reporting |
| AI Act GPAI, systemic risk, EU database, technical file, deployer role | Test 1/7 — AI governance vs catalog |
| TMF ServiceCandidate/Category/CFS/RFS | Test 2/7 — one ecosystem |
| CSDM Service Instance | Test 1 — runtime; already EXTERNAL |
| ITIL Digital Product / consumers / 8-activity lifecycle as OSM enum | Test 1/7; OSM-C-004 |
| ArchiMate element-type field | Test 2 — mapping documentation |
| TOGAF ABB ids | Test 2 |
| TBM allocation engine / Consumer Layer | Test 1/7 |
| Climate change (27001 Amd 1) | Test 1 |
| Service Catalogue entity | Test 5 — dataset is the catalog |
| Offering-level version/lifecycle | Test 7; OSM-M-002 already decided |
| `saas` provider type | Estate D-002; not required by this universe’s *semantics*; documentation |
| Ranked subcontractor graph | Test 7; RoI |

---

## Missing *parameters* vs missing *relations* (decision queue input)

### Parameters (attributes) worth deciding

| ID | Candidate | Default if freeze holds |
|----|-----------|-------------------------|
| GAP-001 | storage location ≠ processing location | characteristics + docs |
| GAP-003 | unprefixed purpose | keep AI-only field (known hole) |
| GAP-005 | provenance on Provider | leave hole (D-025) |
| GAP-004 | parent provider | document collapse |

### Relations worth deciding

| ID | Candidate | Default if freeze holds |
|----|-----------|-------------------------|
| GAP-002 | Service→Service depends_on | remain forbidden |
| GAP-007 / D1 | Arrangement / providers grain | `providers` only; contract fields stay on Provider as hints |
| OSM-M-005 remainder | Service vs Offering `providers` | keep both; document when to use which; do not add a third |

No other new relationship types survived the tests.
