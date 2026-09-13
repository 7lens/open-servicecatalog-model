# 01 — Source register

**Investigation date:** 2026-09-13  
**Rule:** Priority 1 = official owner; Priority 2 = official guidance; Priority 3 = reputable secondary only when primary is inaccessible or to clarify interpretation. Vendor blogs are not used as architectural authority.

Every version claim below was checked against current official pages on this date. Do not silently fall back to older editions.

---

## A. Models / architecture frameworks

### A1. TM Forum TMF633 Service Catalog

| Item | Value |
|------|-------|
| **Current production version** | **TMF633 Service Catalog API v4.0.0** (user guide / production) |
| **Status** | TM Forum Approved production. ODA component TMFC006 Service Catalog Management v1.2.0 (published 2024-11-12) lists TMF633 as a mandatory exposed API with **conformance testing for v4 APIs only**. |
| **v5** | A v5 preproduction asset exists. TMF620 Product Catalog and TMF638 Service Inventory already have production v5. TMF633 v5 is **not** production. This investigation maps **v4.0**. |
| **Superseded** | Older REST specification R18.5.1 is archived; TM Forum points to Production version 4.0.0. |
| **Primary sources** | [TMF633 v4.0.0 user guide](https://www.tmforum.org/resources/specification/tmf633-service-catalog-api-user-guide-v4-0-0/); [ODA TMFC006](https://www.tmforum.org/oda/directory/components-map/production/TMFC006); [TMF633 v4.0.0 specification PDF](https://tmf-open-api-table-documents.s3.eu-west-1.amazonaws.com/OpenApiTable/TMF633_Service_Catalog/4.0.0/user_guides/TMF633_Service_Catalog_Management_API_v4.0.0_specification.pdf) |
| **Secondary** | TM Forum community threads on v5 timing (not used as version authority). |

### A2. ITIL (PeopleCert)

| Item | Value |
|------|-------|
| **Current version** | **ITIL (Version 5)**, general availability **12 February 2026** |
| **Relationship to ITIL 4** | Evolution, not a wipe. ITIL 4 and Version 5 run in parallel (minimum ~12 months). ITIL 4 Foundation remains a valid prerequisite for Version 5 advanced modules. |
| **Material change for OSM** | Unified **digital product and service** management; eight-activity Product and Service Lifecycle (Discover, Design, Acquire, Build, Transition, Operate, Deliver, Support); AI-native guidance; stronger experience/product emphasis. |
| **Primary sources** | [ITIL Version 5 explained](https://www.itil.com/Itil-News-and-Announcements/itil-version-5-explained); [Transition from ITIL 4](https://www.itil.com/Itil-News-and-Announcements/itil-version-5-transition-from-itil-4); [Foundation what’s new](https://itil.com/Itil-News-and-Announcements/itil-version-5-foundation-whats-new-guide); [Product and Service Lifecycle Model](https://www.itil.com/Itil-News-and-Announcements/itil-version-5-service-lifecycle-model) |
| **Limitation** | Full paid syllabi/books were not purchased. Mapping uses official PeopleCert/ITIL.com conceptual material. Service / offering / catalogue language is continuous with ITIL 4; product integration is new emphasis. |

### A3. ServiceNow CSDM 5

| Item | Value |
|------|-------|
| **Current version** | **CSDM 5** (white paper at Knowledge 2025; platform changes rolling through family/store releases including Yokohama / CMDB CI Class Models 1.64.0 Nov 2024) |
| **Material change vs CSDM 4** | Technical Service → **Technology Management Service**; Technical Service Offering → **Technology Management Service Offering**; Application Service → **Service Instance** with new siblings (Data/AI, Network, Connection, Operational Process, Facility); Product Models include Service Offering Model; Life Cycle Stage & Stage Status. |
| **Primary sources** | [CSDM 5.0 white paper PDF](https://www.servicenow.com/community/s/cgfwn76974/attachments/cgfwn76974/common-service-data-model-kb/744/2/CSDM%205.pdf) (ServiceNow community attachment of the official white paper); ServiceNow CSDM product documentation on Service Instance rename |
| **Secondary** | ServiceNow community explainer on v4→v5 terminology (used only to confirm rename mapping). |

### A4. ArchiMate (The Open Group)

| Item | Value |
|------|-------|
| **Current version** | **ArchiMate 4 Specification**, announced **27 April 2026** (document C260) |
| **Previous** | ArchiMate 3.2 (C226, 19 Oct 2022) — **superseded as latest**. Task prompt expected 3.2; currentness rule requires **4**. |
| **Material change for OSM** | ~30% fewer concepts. Per-layer Business/Application/Technology **Service** merged into a generic Common Domain **Service**. Layers restyled as domains. |
| **Primary sources** | [ArchiMate 4 announcement](https://www.opengroup.org/The-Open-Group-Announces-ArchiMate%C2%AE-4-Specification); [Licensed downloads (latest = 4)](https://www.opengroup.org/archimate-licensed-downloads); [Motivation white paper W262, 27 Apr 2026](https://publications.opengroup.org/w262); [ArchiMate 3.2 C226](https://publications.opengroup.org/c226) (historical) |
| **Limitation** | Full paid ArchiMate 4 PDF was not downloaded under evaluation licence. Structural claims use The Open Group announcement + W262 + Open Group blog (20 May 2026). |

### A5. TOGAF (The Open Group)

| Item | Value |
|------|-------|
| **Current version** | **TOGAF Standard, 10th Edition**, with **Technical Corrigendum 1** applied **19 May 2025** (corrigendum published 15 May 2025, U254) |
| **Previous** | TOGAF 9.2 remains in some certification paths; 10th Edition is the current standard. |
| **Primary sources** | [TOGAF 10th Edition C220](https://publications.opengroup.org/c220); [Technical Corrigendum 1 U254](https://publications.opengroup.org/u254); [Downloads](https://www.opengroup.org/togaf-standard-10th-edition-downloads) |
| **Domains used** | Architecture content still organised around Business, Data, Application, Technology (plus strategy/security as practice concerns — Security is **not** a fifth core domain in the standard’s four-domain set). |

### A6. TBM (TBM Council)

| Item | Value |
|------|-------|
| **Current taxonomy** | **TBM Taxonomy v5.0.1**, released **18 July 2025** (v5.0 originally 6 June 2025) |
| **Material change** | “Towers” renamed **Technology Resource Towers**; Cost Pools modernised (Cloud Services, Staffing); Security split from Risk & Compliance; Solutions layer adds AI and Sustainability & ESG; Consumer Layer (was Business Layer). Platform tower retired. |
| **Primary sources** | [Taxonomy page v5.0.1](https://www.tbmcouncil.org/taxonomy/); [Taxonomy 5.0.1 resource](https://www.tbmcouncil.org/learn-tbm/resource-center/the-tbm-taxonomy-5/); [Migration guide](https://www.tbmcouncil.org/learn-tbm/tbm-modeling/taxonomy-migration/); CIO/Practice Lead guides updated May 2026 still referring to Taxonomy 5.0 |

---

## B. Compliance / governance frameworks

### B1. ISO/IEC 27001

| Item | Value |
|------|-------|
| **Current** | **ISO/IEC 27001:2022** (Edition 3, Oct 2022) **+ Amendment 1:2024** “Climate action changes” (published 23 Feb 2024) |
| **Amd 1 content** | Climate-change wording in clauses 4.1 / 4.2. **No Annex A change.** |
| **Annex A** | 93 controls in four themes: Organizational (5.1–5.37), People (6.1–6.8), Physical (7.1–7.14), Technological (8.1–8.34). Reference set for the Statement of Applicability; not a mandatory checklist. |
| **Primary** | [ISO 27001:2022](https://www.iso.org/standard/27001); [Amd 1:2024](https://www.iso.org/standard/88435.html) |
| **Superseded** | ISO/IEC 27001:2013 (and its 14-domain Annex A). |

### B2. ISO/IEC 27701

| Item | Value |
|------|-------|
| **Current** | **ISO/IEC 27701:2025** (Edition 2, published **14 October 2025**) |
| **Structural change** | **Standalone PIMS**, not an extension of ISO 27001/27002. Own Clauses 4–10. Annex A: Table A.1 controllers (31), A.2 processors (18), A.3 shared security (29). Annex D informative GDPR mapping. Annex F 2019→2025 control map. |
| **Transition** | 2019 certificates commonly described as remaining valid until October 2028 (certification-scheme practice; confirm with the adopter’s certification body). |
| **Primary** | [ISO 27701:2025](https://www.iso.org/standard/27701); IEC webstore history (2019 = Revised) |
| **Do not use** | ISO/IEC 27701:2019 as if current. Public OSM `compliance/ISO-27701.md` still reads as the 2019 extension model. |

### B3. NIST CSF

| Item | Value |
|------|-------|
| **Current framework** | **NIST CSF 2.0** (26 February 2024) — Govern, Identify, Protect, Detect, Respond, Recover |
| **Implementation guidance** | CSF 2.0 Quick-Start Guides (Organizational Profiles, Community Profiles, SCRM, Tiers, Informative References). Updated 25 Aug 2026 listing. |
| **AI-related (current)** | **NIST IR 8596** Cyber AI Profile — initial preliminary draft 16 Dec 2025 (comment closed 30 Jan 2026). **NIST SP 1353** ipd Quick-Start Guide for Using AI *for CSF analysis and reporting* — 19 Aug 2026, comments due 15 Oct 2026. SP 1353 is about **using AI to implement CSF**, not classifying AI systems. |
| **Primary** | [CSF 2.0](https://www.nist.gov/cyberframework); [Quick-Start Guides](https://www.nist.gov/cyberframework/quick-start-guides); [SP 1353](https://csrc.nist.gov/pubs/sp/1353/ipd); [IR 8596](https://csrc.nist.gov/pubs/ir/8596/iprd) |

### B4. GDPR

| Item | Value |
|------|-------|
| **Current text** | Regulation **(EU) 2016/679**. EUR-Lex current consolidated version **04/05/2016**, corrected by OJ L 127, 23.5.2018. **No later consolidated amendment** as of this investigation. |
| **2025–2026 official guidance (selected, service-relevant)** | EDPB Guidelines 01/2025 Pseudonymisation (adopted 16 Jan 2025); EDPB Guidelines 3/2025 DSA–GDPR interplay v1.1 (11/12 Sep 2025). Broader 2025–2026 EDPB work on research/anonymisation exists; not all of it attaches to a service catalog. |
| **Primary** | [CELEX 32016R0679](https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX%3A32016R0679); [consolidated 02016R0679-20160504](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02016R0679-20160504); [EDPB Guidelines 01/2025](https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf) |

### B5. DORA

| Item | Value |
|------|-------|
| **Regulation** | **(EU) 2022/2554**, applicable **17 January 2025** |
| **Key RTS/ITS used** | **Delegated Regulation (EU) 2024/1773** (13 Mar 2024) — RTS on policy for contractual arrangements on ICT services supporting critical or important functions. **Implementing Regulation (EU) 2024/2956** (29 Nov 2024) — ITS standard templates for the **register of information** (Art. 28(3)). |
| **2026 reporting** | Competent authorities collect RoI; ESAs use it for CTPP designation. 2026 RoI reference date commonly **31 December 2025**; national windows (e.g. CSSF 11 Feb–31 Mar 2026; CBI 2–31 Mar 2026). EBA RoI FAQ updated 28 Mar 2025; data model DPM 4.0. |
| **Primary** | [RTS 2024/1773](https://eur-lex.europa.eu/eli/reg_del/2024/1773); [ITS 2024/2956](https://www.eba.europa.eu/sites/default/files/2026-02/4ba5c76d-7d54-4fc4-9747-ababfff9c4e6/OJ_L_202402956_EN_TXT.pdf); [EBA DORA RoI preparation](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act/preparation-dora-application); [EBA RoI FAQ](https://eba.europa.eu/sites/default/files/2025-03/31bb6e60-7d10-4405-a8c5-9f04934630ac/20250328%20-%20DORA%20RoI%20reporting%20FAQ%20%28updated%29.pdf) |
| **Also in force (noted, not fully templated here)** | Other DORA RTS/ITS (ICT risk management, incident reporting, TLPT, etc.). OSM is not an ICT risk-management framework; those stay EXTERNAL unless a concept already maps to canonical posture. |

### B6. EU AI Act

| Item | Value |
|------|-------|
| **Regulation** | **(EU) 2024/1689**, in force **1 August 2024** |
| **Timeline (current, including Omnibus postponements)** | Prohibited practices + AI literacy: **2 Feb 2025**. GPAI obligations: **2 Aug 2025**. Commission GPAI enforcement/fines: **2 Aug 2026**. GPAI models on market before 2 Aug 2025: comply by **2 Aug 2027**. High-risk Annex III obligations postponed to **2 Dec 2027**; Annex I product-safety route to **2 Aug 2028** (Digital Omnibus / Regulation (EU) 2026/1744 as reported in Commission digital-strategy pages). |
| **2025–2026 Commission guidance** | Guidelines on prohibited AI practices, C(2025) 5052, 29 Jul 2025. GPAI provider obligation guidelines (content approved 18 Jul 2025; formal adoption 19 Nov 2025, C(2025) 7719). **Draft** high-risk classification guidelines under Art. 6(5), published **19 May 2026** (consultation; not yet final). Guidelines on AI system definition. |
| **Primary** | [Commission AI Act policy page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai); [GPAI guidelines](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers); [Draft high-risk classification guidelines](https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems); prohibited-practices guidelines PDF via AI Act Service Desk |

---

## C. OSM sources used as the object under test

| Source | Role |
|--------|------|
| `SPECIFICATION.md` 1.3.0 | Normative fields |
| `MODEL.md` | Conceptual model |
| `schema/catalog/*`, `schema/posture/*`, `schema/shared/*` | JSON Schema |
| `validation/validate.py` | Enforced rules |
| `_internal/decisions/*` | Accepted / superseded / freeze |
| `models/*`, `compliance/*` | Current public mapping text (revalidated, not trusted) |
| `_internal/notes/*` | Historical notes (status mostly NOT ANALYZED) |
| `_internal/investigation/*` | Estate stress-test OPEN items (evidence, not decisions) |
| `examples/**` | How mappings are taught (not modified) |

---

## D. Access limitations (honest)

| Gap | Impact |
|-----|--------|
| Paid TMF / ArchiMate / TOGAF / ISO full texts | Structural mapping used official tables, user guides, ISO catalogue pages, and Open Group announcements. Fine-grained attribute lists for ArchiMate 4 elements rely on Open Group public summaries. |
| PeopleCert ITIL Version 5 official books | Product/service lifecycle and positioning from itil.com; practice-level detail not exhaustively mapped (correctly EXTERNAL anyway). |
| CSDM 5 is a ServiceNow white paper + platform model | Class names and Service vs Instance boundary are clear from the official PDF. Table internals may lag documentation. |
| Draft AI Act high-risk guidelines | Recorded as draft. Classification examples may change before year-end 2026 adoption. |

None of these limitations prevent classifying OSM sufficiency at the **technological-service** grain. They do prevent claiming a complete attribute-by-attribute clone of any paid standard.
