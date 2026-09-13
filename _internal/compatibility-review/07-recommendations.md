# 07 — Recommendations and human decision queue

> **Disposition (2026-09-13 implementation pass):** The eight
> architectural decisions in the follow-up instruction were
> **ACCEPTED** as OSM-C-006–C-009, OSM-D-001–D-003, and OSM-M-011
> (principle; schema not implemented). DOC-1–DOC-12 documentation
> items were applied to public `models/`, `compliance/`,
> `SPECIFICATION.md`, `MODEL.md`, and examples. This file remains
> the **investigation-time** queue. Do not treat D1–D5 / D11–D13
> “suggested defaults” as still open for those accepted items.

**This file did not make architectural decisions at investigation
time.** It ordered the questions so maintainers could.

Default if no decision is taken: **the frozen OSM 1.3.0 core stays as-is**; only documentation of mappings is overdue.

---

## How to use this queue

1. Decide **documentation-only** items first (no freeze break).
2. Decide **explicit non-additions** (confirm EXTERNAL) so the next cycle does not re-litigate them.
3. Only then consider **schema candidates** (each needs a new OSM-M after unfreezing).

Trade-offs are written as A / B / C. **Bold** is the investigation’s *suggested default*, not an accepted decision.

---

# Part A — Do not decide these as model changes yet

These look like gaps but should remain **outside the canonical model** unless a later OSM-C/M says otherwise.

| Topic | Why not now | If ignored, what happens |
|-------|-------------|--------------------------|
| CSDM Service Instance (+ siblings) | Runtime/CMDB; OSM-C-005 | Adopters try to catalog prod/test as services |
| ITIL Digital Product / consumers / value streams | OSM-C-004; v5 made this *more* ITIL, not more OSM | OSM stops being a small technology core |
| TMF Candidate/Category/CFS/RFS / TMF638 instances | OSM-M-003/004 | Catalog hierarchy explosion |
| NIST Categories, Profiles, Tiers | GRC | OSM becomes CSF |
| ISO 27001 SoA / control implementation objects | GRC | OSM becomes ISMS |
| GDPR RoPA (legal basis, data subjects, SCCs, DPO) | Privacy system | OSM becomes RoPA |
| DORA RoI templates, LEI, CIF register, incident feed | Supervisory reporting | OSM becomes the register of information |
| AI Act GPAI, deployer/provider roles, EU database, technical file | AI governance | OSM becomes an AI Act file |
| Arrangement **entity** | GAP-007 failed smallness | OSM becomes a contract register |

**Suggested default:** record as **confirmed EXTERNAL** in a future documentation pass of `models/` and `compliance/` — still not a schema change.

---

# Part B — Documentation decisions (no schema)

Do these without unfreezing. They fix C-VER-* and teaching errors without pretending OSM “implements” anything.

| Doc ID | Change | Trade-off |
|--------|--------|-----------|
| DOC-1 | Cite **current versions** in every `models/` and `compliance/` file (see 01) | Accuracy vs. maintenance cost when standards move |
| DOC-2 | Rewrite ArchiMate mapping to **ArchiMate 4 generic Service** in technology-domain context | Correctness vs. 3.2 adopters still using TechnologyService |
| DOC-3 | ITIL: OSM `lifecycle_state` ≠ Version 5 eight-activity lifecycle; Digital Product remains EXTERNAL | Prevents enum pollution vs. ITIL-purist disappointment |
| DOC-4 | CSDM 5: TMS vs **Service Instance** table in `CSDM.md` | Clears the #1 implementation confusion |
| DOC-5 | TBM: “IT Tower” → Technology Resource Tower 5.0.1; examples’ Infrastructure/Management names are illustrative only | Honesty vs. breaking example aesthetics later |
| DOC-6 | ISO 27701:2025 standalone PIMS; role is per **activity**; OSM field is a proxy | Prevents PIMS-substitution |
| DOC-7 | DORA: `providers` feeds RoI, is not RoI; list RTS/ITS; OSM-M-005 grain still open | Prevents false DORA completeness |
| DOC-8 | AI Act: enum is a **label**, not Art. 6; no GPAI; Omnibus dates | Prevents fake classification |
| DOC-9 | One-pager: **when to put `providers` on Service vs Offering** (without resolving D1) | Operational clarity vs. prematurely closing arrangement grain |
| DOC-10 | Reserved **characteristic names** for `location` / `region` / `data_residency` / process-vs-store | Closes GAP-006 without schema vs. appearing to standardise characteristics |
| DOC-11 | Align COMPATIBILITY status table with reality (MAPPED / PARTIALLY COMPATIBLE vs NOT ANALYZED) | Process honesty; freeze text currently stale |
| DOC-12 | Privacy locator overlap: which of `privacy_classification`, `gdpr_processing_activity`, `iso27701_pii_*` is authoritative for “handles PII?” | Machine clarity vs. keeping all locators |

**Suggested default:** do DOC-1–DOC-11 in a documentation PR. DOC-12 needs D3.

---

# Part C — Human decisions (model or mapping architecture)

## D1 — OSM-M-005 remainder: provider-link grain vs DORA arrangement

**Question:** Is `providers` on Service/Offering the same relationship DORA needs, and is Provider-level contract metadata acceptable?

| Option | What it means | Gains | Loses / costs |
|--------|----------------|-------|----------------|
| **A. Keep frozen design** | Dual grain Service/Offering `providers`; contract fields stay on Provider as hints; RoI EXTERNAL | Smallness; OSM-M-010; works for non-finance | Cannot round-trip RoI; contract collapse (multi-contract vendors) |
| B. Strip contract fields from Provider; keep only `contract_ref` pointer | OSM stops pretending to hold the arrangement | Cleaner OSM-M-008 | Migration; less “vendor risk conversation” in-core |
| C. Add Arrangement entity | OSM can feed RoI more directly | Finance interoperability | Breaks freeze, smallness, vendor-neutrality; Test 7 fail |

**Suggested default: A**, plus DOC-7/DOC-9. Do not choose C in this cycle.

**Do not resolve Service-vs-Offering placement.** Keep both: intrinsic vs variant. That part of OSM-M-010 is sound.

---

## D2 — Controller/processor grain and name

**Question:** Offering-level `iso27701_pii_role` vs per-activity reality; ISO name vs GDPR concept.

| Option | Gains | Costs |
|--------|-------|-------|
| **A. Keep field; document proxy + dual standard** | No freeze break; OSM-M-008 (one role field) | Dual-role SaaS still one enum |
| B. Rename to unprefixed `processing_role` | Honest, framework-neutral | Schema rename; churn |
| C. Move to privacy system only; deprecate field | Purity | Lose a useful locator |

**Suggested default: A** now; B only with a later OSM-M.

---

## D3 — Overlapping PII locators

**Question:** Four fields can assert personal data.

| Option | Gains | Costs |
|--------|-------|-------|
| **A. Document precedence:** `privacy_classification` canonical; GDPR/27701 are mappings | OSM-M-008 in prose | Fields still duplicate in data |
| B. Drop `gdpr_processing_activity` (derive from privacy_classification ≠ none) | Less duplication | Loses explicit “assessed as processing” vs “classified pii” |
| C. Drop PII categories enum; use characteristics | Smaller core | Lose closed enum for machines |

**Suggested default: A.**

---

## D4 — Service → Service dependency (GAP-002)

| Option | Gains | Costs |
|--------|-------|-------|
| **A. Confirm exclusion** (OSM-C-004/005) | Freeze; smallness; no graph | Machines cannot reason blast radius inside OSM |
| B. Minimal `depends_on: [service_id]` on Service | High convergence value | Freeze break; cycles; offering-level still missing |
| C. Typed relationships (TMF-like) | Interoperability with TMF/CSDM | OSM-M-004 failure |

**Suggested default: A** until a named interoperability project exists. If B is ever accepted, forbid using `providers` for it (already true).

---

## D5 — Location: capability vs actual; process vs store (GAP-001, GAP-006)

| Option | Gains | Costs |
|--------|-------|-------|
| **A. Characteristics convention only** (`data_processing_location`, `data_storage_location` on Offering; Provider list = capability) | No schema; Test 5 reuse | Optional names drift |
| B. Add two optional lists on Offering Posture | Canonical, queryable | Freeze; overlap with characteristics |
| C. Split Provider into process + store lists only | Tiny schema | Still wrong grain for actual residency |

**Suggested default: A.** Pair with DOC-10.

---

## D6 — `togaf_domain` grain

| Option | Gains | Costs |
|--------|-------|-------|
| **A. Keep stack-only; constrain examples to B/D/A/T** | No schema | Mixed stacks |
| B. Allow service-level mapping | Accurate labels | Another mapping field (OSM-M-008 caution) |
| C. Remove field; use characteristic | Smaller dedicated mappings | Loses a known join |

**Suggested default: A** + fix C-EX-1.

---

## D7 — TBM join: Stack Resource Tower vs Service Solution

| Option | Gains | Costs |
|--------|-------|-------|
| **A. Keep stack labels; document 5.0.1 names** | No schema | Weak join to OSM Service |
| B. Add optional TBM mapping on Service (Solutions layer) | Better TBM 5 fit | Dual TBM fields; freeze |
| C. Remove TBM fields; finance maps externally | Purity | Lose convenient label |

**Suggested default: A.** Do not add service-level TBM until someone demonstrates reporting need.

---

## D8 — `nist_control_status`

| Option | Gains | Costs |
|--------|-------|-------|
| **A. Keep; document “not a CSF object, not certification”** | No churn | Continues to look like certification |
| B. Remove | Honesty | Data migration |
| C. Rename to `control_implementation_status` unprefixed | OSM-M-008 nicer | Still GRC-ish; freeze |

**Suggested default: A** short term; **B** if a mapping cleanup OSM-M happens.

---

## D9 — Stack DORA `pillar` / `criticality` (incl. `standard`)

| Option | Gains | Costs |
|--------|-------|-------|
| **A. Keep; document informal + `standard` is OSM not DORA** | No schema | Misleading DORA flavour |
| B. Drop `pillar`; keep nothing DORA on stack | Cleaner | Loss of a rarely useful tag |
| C. Change criticality enum to `{critical, important, not-applicable}` | Closer to DORA CIF language | Still wrong **grain** (stack ≠ function) |

**Suggested default: A** with sharp documentation. C is tempting and still semantically wrong (CIF ≠ stack).

---

## D10 — Human oversight: keep AI-prefixed or generalize

| Option | Gains | Costs |
|--------|-------|-------|
| **A. Keep `ai_act_human_oversight` gated** | Matches validation rule 6 | GDPR Art. 22 automation has no field |
| B. Unprefixed `human_oversight` on posture | Cross-framework (04) | Freeze; AI Act gating logic changes |

**Suggested default: A.**

---

## D11 — Canonical purpose (GAP-003)

| Option | Gains | Costs |
|--------|-------|-------|
| A. Do nothing | Freeze | GDPR/27701 purpose hole remains |
| **B. Document characteristic `purpose`** | No schema; OSM-M-001 | Optional adoption |
| C. Add optional unprefixed `purpose` on Service (and/or Offering); map AI Act onto it | Canonical; OSM-M-008 vs `ai_act_intended_purpose` | Freeze; must deprecate or alias the AI field |

**Suggested default: B** now; **C** only if purpose becomes load-bearing for machines.

If C is chosen later, **do not** add `gdpr_purpose`.

---

## D12 — Legal parent of ICT Provider (GAP-004)

| Option | Gains | Costs |
|--------|-------|-------|
| **A. EXTERNAL + document collapse** | Smallness | DORA parent location not in OSM |
| B. Optional `parent_provider_id` | Group graph without LEI | Freeze; identity policy (D-005) |
| C. Full legal-entity attributes (LEI, CTPP, contracting parties) | RoI-ready | OSM-M-004 failure |

**Suggested default: A.**

---

## D13 — Provenance on ICT Provider (GAP-005)

| Option | Gains | Costs |
|--------|-------|-------|
| A. Leave hole | Freeze | Unsourced certs/locations |
| **B. Allow existing provenance object on Provider** (later OSM-M) | Reuse; Test 7 friendly; high audit value | Small freeze break when unfrozen |
| C. Per-field provenance | Perfect evidence | Complexity (estate D-030 already notes per-record limit) |

**Suggested default: B as the strongest small schema candidate**, but **not in this investigation**. Requires an OSM-M after unfreeze.

---

# Part D — Missing parameters vs missing relations (one page)

### Parameters (attributes)

| Status | Item |
|--------|------|
| Already canonical — do not duplicate | `providers`, `rto`/`rpo`, `operational_criticality`, `risk_level`, `accountable`, `lifecycle_state`, classifications, posture targets |
| Overlapping — decide in D2/D3/D8/D9 | PII locators; NIST status; stack DORA labels; ISO 27001 dual fields |
| Missing but **do not add** without OSM-M | storage≠process location as schema; unprefixed purpose; parent provider; provider provenance |
| Use characteristics instead | region/residency, operating model, vendor SLA, GPAI flag, process/store split |

### Relations

| Status | Item |
|--------|------|
| Canonical | Stack→Service; Service→Offering; Service/Offering→Provider (`providers`); nested posture/characteristic/provenance |
| Forbidden | Service→Service (confirm D4) |
| Derived | Provider→Service |
| Not OSM | Consumer, CI, Instance, Arrangement, CIF, RoPA activity |

---

# Part E — Suggested sequencing (still not a decision)

```text
1. Documentation PR (DOC-1–11)     ← no freeze break
2. Confirm EXTERNAL list (Part A)  ← OSM-C notes only
3. D1 / D4 / D5 as explicit "remain frozen" minutes
4. If unfreeze ever: D13 (provenance on provider) first
5. Only with a real project: D4-B or D11-C
6. Never in core: RoI, RoPA, Instance, Product, CSF profile
```

---

# Part F — Public `models/` and `compliance/` quality

Those files were **fully analysed** (02, 03, 06). They are **not yet** the quality they should be for adopters:

- too short to be mappings
- version-stale
- ArchiMate factually outdated
- ISO 27701 structurally outdated
- status in COMPATIBILITY.md disagrees with their existence

**Recommendation:** a follow-up documentation task should rewrite them from this investigation **without** changing schema. That rewrite *is* a mapping-documentation decision (DOC-1–11), not a model decision.

This investigation did **not** rewrite them, to avoid silently accepting mappings.
