# 02 — Model / architecture mapping matrix

**Object:** frozen OSM 1.3.0  
**Classifications:** MAP | MAP + DOCUMENT | EXTERNAL | GAP CANDIDATE | AMBIGUOUS / DECISION REQUIRED  
**Do not map by name.** Semantic equivalence is in the Rationale column.

Existing public files under `models/` were **revalidated**. Several are version-stale (see 06).

---

## 1. TM Forum TMF633 v4.0.0

### Version used

Production **TMF633 Service Catalog Management API v4.0.0**. v5 exists only in preproduction; not mapped.

### Out of scope (justified)

TMF **product catalog (TMF620)**, **resource catalog (TMF634)**, **service inventory (TMF638)** are adjacent ODA APIs. They matter as *boundaries*: TMF633 is the catalog of **specifications**; instances live in TMF638. OSM already draws that same catalog-vs-instance line. Mapping TMF620/TMF638 classes into OSM would violate OSM-M-004.

### A–N extract (service-catalog relevant only)

| Lens | TMF633 v4.0 concept | Material to OSM? |
|------|---------------------|------------------|
| A Core | ServiceCatalog, ServiceCategory, ServiceCandidate, ServiceSpecification | Yes — catalog shape |
| B Catalog | Catalog is a container of candidates; candidate publishes a specification into 0..n catalogs | Yes — OSM has no Catalog/Candidate entities |
| C Definition | ServiceSpecification = template from which Services are instantiated; `specCharacteristic`, `validFor`, `lifecycleStatus`, `version` | Yes |
| D Offering/variant | No first-class “offering”. Variation via characteristics, bundled specs, or product-side TMF620 ProductOffering | Yes — OSM Offering is an OSM invention relative to TMF633 |
| E Ownership | `relatedParty` on specification | Partial |
| F Provider | Not a TMF633 resource. Parties via relatedParty / TMF632 | Partial |
| G Lifecycle | Full `lifecycleStatus` machine + `validFor` on catalog, candidate, spec | Yes |
| H Relationships | `serviceSpecRelationship` (migration, substitution, dependency, exclusivity); spec ↔ resource spec refs | Yes |
| I Operational/posture | Not in TMF633 (inventory / quality APIs) | Boundary |
| J Financial | Not in TMF633 | No |
| K Architecture | CFS vs RFS is SID, not a TMF633 resource pair OSM must copy | Boundary |
| L Dependency | Spec relationships; resource specification refs | Yes |
| M Instance | Explicitly TMF638, not TMF633 | Boundary — EXTERNAL |
| N Machine-readable | Rich characteristic metamodel, `@type`/`@schemaLocation`, JSON schema targetEntitySchema | Yes |

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| ServiceSpecification | Template describing a type of service; instances share its characteristics | Specification | OSM **Service** *is* the definition (OSM-M-003) | Service | **MAP** | Same semantic job: stable definition. OSM refuses a separate spec entity. |
| Service (instance) | Instantiated service in inventory | Instance | — | — | **EXTERNAL** | TMF638. OSM Service is never an instance. |
| ServiceCatalog | Container exposing candidates | Catalog | OSM catalog files | Dataset | **EXTERNAL** | OSM does not reify a Catalog entity; the dataset *is* the catalog (same pattern as ITIL). |
| ServiceCandidate | Publication of a spec into a catalog | Publication | — | — | **EXTERNAL** | Publication/visibility, not a technological variant. |
| ServiceCategory | Grouping of candidates | Taxonomy | Technology Stack is **not** a category | Stack | **EXTERNAL** | Stack is operational ownership, not a catalog taxonomy. |
| CharacteristicSpecification | Named typed configurable property with cardinality/constraints | Spec / candidate | Characteristic | Service/Offering | **MAP + DOCUMENT** | OSM is a small nested structure, not a characteristic catalog, no `@type`/`@schemaLocation`, no shared registry. Semantics overlap; metamodel does not. |
| `version` / `validFor` | Spec may evolve; validity window | Spec | `version`, `valid_from`, `valid_to` | Service | **MAP** | Adopted subset (OSM-M-002). |
| `lifecycleStatus` | Full TMF state machine | Spec/catalog/candidate | `lifecycle_state` enum of 5 | Service | **MAP + DOCUMENT** | Same *kind* of fact (definition lifecycle), reduced enum. Do not import TMF states. |
| Offering / ProductOffering | TMF620 commercial offering | Product | Service Offering | Offering | **EXTERNAL** (product) / OSM Offering is **not** TMF633 | OSM Offering ≈ requestable technological variant. TMF puts commercial packaging in the product catalog. |
| `relatedParty` | Parties with interest/management | Spec | `accountable`; `providers` | Service / Provider | **MAP** (subset) | Only Service Owner + ICT Provider. Other parties stay outside. |
| `serviceSpecRelationship` | Dependency, substitution, exclusivity, migration | Spec–Spec | Forbidden Service→Service | — | **GAP CANDIDATE** / currently **EXTERNAL by OSM-C-004** | Recurs in TMF, CSDM, ArchiMate, DORA. See GAP-002. Do not add because TMF has it. |
| ResourceSpecificationRef | Spec depends on resource specs | Spec–resource | — | — | **EXTERNAL** | Resource catalog / CMDB. |
| CFS / RFS | SID customer- vs resource-facing | Architecture | — | — | **EXTERNAL** | OSM Service is technological only; CFS would be a business/customer service. |
| `@type` / `@schemaLocation` | Polymorphic JSON-LD style extension | API | — | — | **EXTERNAL** | API concern. |
| Identifier schemes | TMF ids | Entity | 2-/3-segment OSM ids | Service/Offering | **EXTERNAL** | OSM-C/M already keep OSM ids. |
| In-catalog version history | Multiple spec versions as rows | Spec | One row per `id` | Service | **EXTERNAL** | History out of band (git). |
| Offering-level version | TMF can version candidates/specs separately | Candidate | None on Offering | — | **EXTERNAL** | OSM-M-002: offerings belong to the parent definition. |

### TMF633 conclusion

Selective compatibility of OSM-M-001–004 **still holds against v4.0**. The public `models/service-management/TMFORUM-TMF633.md` is directionally correct but should cite v4.0.0 and state that v5 is preproduction. No new OSM field is justified by TMF633 v4.

---

## 2. ITIL (Version 5) — distinguish from ITIL 4

### Version used

**ITIL (Version 5)**, GA 12 Feb 2026. ITIL 4 remains valid in parallel. OSM-C-004 already targeted “ITIL v5”; this revalidation checks whether Version 5 **changed** the service-catalog subset.

### What Version 5 changes (material)

- **Digital product and service are one lifecycle**, eight activities: Discover, Design, Acquire, Build, Transition, Operate, Deliver, Support.
- AI-native / complexity-ready practice guidance.
- Continuity of SVS, guiding principles, practices, service/offering/catalogue language.

What Version 5 does **not** change: a technological-service catalog still needs a service, requestable offerings, ownership, suppliers, and a distinction between definition and operation.

### Out of scope (justified)

ITIL practices, value streams, governance boards, workforce, experience journeys, AI-practice guidance — management system, not catalog semantics. OSM-C-004 already excluded them. Version 5’s *stronger* product emphasis **reinforces** that Digital Product stays outside OSM rather than pulling it in.

### A–N extract

| Lens | ITIL v5 concept | Material? |
|------|-----------------|-----------|
| A | Service, digital product, practice, SVS | Service yes; product/SVS no |
| B | Service catalogue (request + technical views in practice) | Yes |
| C | Service as value co-creation; ITIL service is broader than technology | Yes — OSM narrower by design |
| D | Service offering (one or more services + terms, for a consumer group) | Yes |
| E | Service owner and many other roles | Accountability yes; role taxonomy no |
| F | Supplier / service provider | Yes |
| G | Product & service lifecycle activities vs definition state | Yes — different concerns |
| H | Service relationships, CI relationships | Yes as boundary |
| I | SLAs, OLAs, SLIs, event/incident | Targets yes; SLA objects no |
| J | Cost/value, charging | Characterization only |
| K | Architecture practices | No |
| L | Dependencies in the value stream | Boundary |
| M | Configuration items / live services | EXTERNAL |
| N | ITIL is not a schema | Mapping only |

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| Service | Means of enabling value; may be business, customer, or technology | Service | OSM Service | Service | **MAP** | Conceptual compatibility, **deliberately narrower** (OSM-C-004). |
| Digital Product | Version 5 first-class counterpart of service | Product | — | — | **EXTERNAL** | OSM-C-004. v5 increased product weight; that is a reason to keep OSM technological, not to add Product. |
| Service offering | Package of one+ services with terms for a consumer group | Offering + commercial + consumer | Service Offering | Offering | **MAP + DOCUMENT** | OSM keeps the atomic requestable variant; consumer groups and commercial packaging stay in ITIL/commercial systems. |
| Service catalogue | Management view of live/requestable services | Catalog | OSM catalog dataset | Dataset | **MAP** | No ServiceCatalogue entity needed. |
| Product & Service Lifecycle (8 activities) | How work is done | Activity | `lifecycle_state` + version/validity | Service definition | **MAP + DOCUMENT** | **Different facts.** OSM = definition state. ITIL = management activity. Do not rename OSM enum to Discover/Design/… |
| Service owner | Accountability | Role | `accountable` | Service | **MAP** | Stack Owner is documented, not a schema field. |
| Supplier / provider | Third party supplying services | Supplier | ICT Provider + `providers` | Provider | **MAP** | Do not import supplier-management practice. |
| SLA / service level | Negotiated agreement + measures | Contract | `availability_target`, `response_target`, `resolution_target`; hours as characteristics | Posture / characteristic | **MAP + DOCUMENT** | Expectations only. SLA objects EXTERNAL (OSM-C-004). Vendor SLA ≠ enterprise target (estate D-011). |
| CI / asset | Inventory | Item | `asset_coverage` signal only | Offering posture | **EXTERNAL** (+ weak signal MAP) | Completeness flag is not a CI. |
| Service→Service | Supporting/depending services | Rel | forbidden | — | **GAP CANDIDATE** (see GAP-002) | Same as TMF/CSDM. Currently EXTERNAL by OSM-C-004. |
| Consumers / user experience | Who consumes, how it feels | Person/group | — | — | **EXTERNAL** | OSM-C-004. |
| AI governance practices | How to manage AI in SM | Practice | AI Act flags if the *service* is an AI system | Posture | **EXTERNAL** | Practice ≠ catalog fact. |

### ITIL v5 conclusion

OSM-C-004 **survives Version 5**. The new product/service lifecycle is the main documentation debt: public `models/service-management/ITIL.md` does not say that OSM `lifecycle_state` is **not** the eight-activity model. No schema change is required to remain selectively compatible.

---

## 3. ServiceNow CSDM 5 — Service vs Service Instance

### Version used

**CSDM 5** official white paper. Platform labels: Technology Management Service / Offering; Service Instance (was Application Service).

### Service vs Service Instance (required analysis)

| CSDM 5 class | Meaning | OSM |
|--------------|---------|-----|
| **Business Service** | Outcome-facing service with Business Service Offerings | **EXTERNAL** (OSM-C-005) |
| **Technology Management Service** (was Technical Service) | Who **manages** a technology service; published to the technical catalog; mapped to `cmdb_ci_service_technical` | **MAP** → OSM Service (narrower, vendor-neutral definition — not a CMDB CI) |
| **Technology Management Service Offering** | Technical offering with **service commitments**; requestable; related to CIs via Dynamic CI Group | **MAP** → OSM Offering (OSM has no commitment/SLA object) |
| **Service Instance** (was Application Service) | **Instantiation** of a service: deployed operational stack. Designated by environment, region, LoB. Operational CI used for IPC impact. Siblings: Data (incl. genAI), Network, Connection, Facility, Operational Process | **EXTERNAL** — this is the runtime OSM refuses |
| **Application Service** | Now a *classification* of Service Instance (application stack), not a separate abstract service type | **EXTERNAL** |

CSDM 5 **clarifies** a confusion OSM already encoded: people mixed “technical service” with “application service/instance”. TMS is the management/catalog definition. Service Instance is the deployed thing. OSM Service ≠ Service Instance remains correct and is **stronger** under CSDM 5.

### Out of scope (justified)

CMDB class hierarchy, Product Models (including new Service Offering Model), Value Streams, Teams, DevOps change model, Dynamic CI Groups, IPC impact — ServiceNow operating model. OSM-C-003 keeps CSDM in the universe as a **projection target**, not a metamodel.

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| Technology Management Service | Catalogued technical service, who manages the technology | Service CI | Service | Service | **MAP** | Closest class. OSM is not a CI. |
| Technology Management Service Offering | Requestable technical variant + commitments | Offering CI | Service Offering + optional characteristics | Offering | **MAP + DOCUMENT** | Commitments/SLA stay outside OSM. Variation dimensions via characteristics/`providers`. |
| Business Service / Offering | Sell/consume / SPM | Business | — | — | **EXTERNAL** | OSM-C-005. |
| Service Instance (+ siblings) | Deployed instantiation | Instance CI | — | — | **EXTERNAL** | Explicit OSM out-of-scope. CSDM 5 rename makes this safer to explain. |
| Service Offering Model | Product model for offerings | Product model | — | — | **EXTERNAL** | Product Models out of OSM. |
| Service Owner | CSDM contact | Role | `accountable` | Service | **MAP** | Do not copy CSDM contact graph. |
| Technology Provider | Company/CI providing technology | Provider | ICT Provider + `providers` | Provider | **MAP** | OSM-M-006/010. |
| Life Cycle Stage & Status | New CSDM 5 stage model on CIs | CI | `lifecycle_state` | Service definition | **MAP + DOCUMENT** | Different state machine; do not import CSDM stages. |
| Dynamic CI Group / CI rel | Inventory grouping | CI | `asset_coverage` | Offering posture | **EXTERNAL** | Signal only. |
| Service→Service / depends on | CMDB rel | Rel | forbidden | — | **GAP CANDIDATE** (GAP-002) | CSDM graphs this; OSM does not. |
| Value Stream | CSDM 5 capability | Business | — | — | **EXTERNAL** | |

### CSDM 5 conclusion

OSM-C-005 still holds. Public `models/service-management/CSDM.md` should cite **CSDM 5** and the Service Instance rename. No CSDM-specific schema fields are justified.

---

## 4. ArchiMate 4 (not 3.2)

### Version used

**ArchiMate 4**, 27 Apr 2026. Public OSM file maps to ArchiMate 3.x **Technology Service** — that element type is **merged**.

### Material change

ArchiMate 4 generic Common Domain **Service** = external behaviour provided to an environment. Layer (business / application / technology) is no longer encoded in the *class*; it is encoded by what realises, serves, and is assigned to the service.

Implication for OSM: the landing is still “this catalog record is a **technological** service”, but the ArchiMate *element type* to project into is **Service** (with technology-domain context), not `TechnologyService`.

### Out of scope (justified)

Motivation, strategy, implementation & migration viewpoints, the 11 relationship types as an OSM graph, architecture views. OSM is not an EA repository.

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| Service (generic, ArchiMate 4) | External behaviour | Architecture element | OSM Service | Service | **MAP + DOCUMENT** | Closest element. OSM Service is a catalog **definition**, not a diagram element. Document that 3.2 Technology Service is gone. |
| Business Service / Application Service (3.2 types; 4 as contextual Services) | Other domains | Element | — | — | **EXTERNAL** | OSM technological only. Join in an EA tool. |
| Serving / Realization | Who serves / what realises | Rel | — | — | **EXTERNAL** | Architecture relationships. |
| Service Offering | No required ArchiMate twin | — | stays in OSM | Offering | **EXTERNAL** (no twin) | Correct. Do not invent an ArchiMate offering. |
| Technology Stack | Operational competency | Stack | not Grouping / Capability / Device | Stack | **EXTERNAL** | Stack is operating-model ownership. |
| Actor (external) | Party | Actor | ICT Provider | Provider | **MAP + DOCUMENT** | Loose. OSM provider master data is richer than an Actor box. |
| Location | ArchiMate Location | Place | offering characteristics / provider locations | mixed | **MAP** via characteristics | No dedicated OSM Location entity (correct). |
| Operational attrs (RTO, cost, lifecycle) | Mostly absent in ArchiMate | — | OSM posture | Posture | **EXTERNAL** to ArchiMate | OSM holds them; ArchiMate does not need copies. |

### ArchiMate conclusion

Conceptual mapping remains valid **if documentation is updated to ArchiMate 4**. Adding `mappings.archimate_element` is **not** justified (OSM-M-004); projection rules belong in `models/architecture/ARCHIMATE.md`.

**AMBIGUOUS:** whether OSM should ever store an optional ArchiMate element id for tool join. Default: no — join keys can live in provenance.`source_record_id`.

---

## 5. TOGAF Standard, 10th Edition + Corrigendum 1 (May 2025)

### Out of scope (justified)

ADM phases, architecture governance, capability-based planning, content metamodel as OSM entities, Architecture Repository. OSM is not a method.

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| Technology Architecture | Domain of the estate’s technology | Domain | Stack `togaf_domain` | Stack | **MAP + DOCUMENT** | Optional free-text label. Not a building block. |
| Business / Data / Application Architecture | Other domains | Domain | same field | Stack | **MAP + DOCUMENT** | Examples also store “Security Architecture”, which is **not** one of the four standard domains — teaching error (06). |
| Architecture Building Block / Solution Building Block | Reusable architecture/solution component | ABB/SBB | OSM Service (loose) | Service | **MAP** (conceptual only) | Do not add `togaf_abb`. Service is a technological definition, not a TOGAF artefact. |
| Service (TOGAF usage) | Broader than technology | Various | OSM Service | Service | **MAP + DOCUMENT** | Terminology clash. |
| Service Offering | Not a TOGAF entity | — | stays OSM | Offering | **EXTERNAL** | |
| Capability | Business/tech capability | Capability | — | — | **EXTERNAL** | OSM-M-004 / out of scope. |
| ADM artefacts | Method | Process | — | — | **EXTERNAL** | |

### Grain question

`togaf_domain` sits only on **Stack**. A Data-classified *service* in a Technology-classified stack cannot be labelled. **AMBIGUOUS / DECISION REQUIRED** (D6): keep stack-only vs allow service-level label vs drop the field and use a characteristic.

### TOGAF conclusion

OSM can sit beside TOGAF without becoming TOGAF. The field is a weak translation hint. No TOGAF entities should be added.

---

## 6. TBM Taxonomy 5.0.1 (18 Jul 2025)

### Material change

| TBM 4.x language in OSM today | TBM 5.0.1 |
|-------------------------------|-----------|
| IT Tower (L1) | **Technology Resource Tower** |
| Sub-Tower (L2) | Resource Sub-Tower (still exists; some splits e.g. LAN/WAN, Security vs Risk & Compliance) |
| Cost pool (finance) | **Technology Cost Pools** (Cloud Services, Staffing, …) |
| TBM “service” | Closer to **Solutions** layer (products/services delivered) than to Resource Towers |
| Platform tower | **Retired** — remap to Application, Data, or Smart Devices |

OSM examples use tower names such as Infrastructure, Security, Applications, Management. In 5.0.1, Resource Towers include Compute, Storage, Network, Data, Security, Risk & Compliance, Smart Devices, Application, etc. **“Infrastructure” and “Management” are not 5.0.1 tower names.** Examples teach a stale taxonomy (06). Not changed in this investigation.

### Mapping table

| External concept | Definition | External grain | OSM mapping | OSM grain | Classification | Rationale |
|------------------|------------|----------------|-------------|-----------|----------------|-----------|
| Technology Resource Tower | Where/how resource cost is consumed (compute, storage, …) | Resource taxonomy | `mappings.tbm_tower` | **Stack** | **MAP + DOCUMENT** + **AMBIGUOUS grain** | OSM Stack is an **operational competency**, not a resource tower. Mapping is a translation layer only if names are current. |
| Sub-Tower | Finer resource class | Sub-tower | `tbm_sub_tower` | Stack | **MAP + DOCUMENT** | Same grain issue. |
| Cost Pool (TBM) | What was purchased (GL view) | Finance | `cost_pool` | Offering posture | **MAP + DOCUMENT** | **Name collision.** OSM field is characterization, not a TBM Cost Pool engine. |
| Solutions (Service/Product) | What technology delivers to consumers | Solution | OSM Service / Offering | Service/Offering | **AMBIGUOUS** | TBM 5 Solutions are closer to OSM Service than Towers are. Labels on Stack may be the wrong join. |
| Consumer Layer | Who consumes (BU, product, value stream) | Consumer | — | — | **EXTERNAL** | OSM has no consumers. |
| Chargeback / showback | Allocation operating model | Finance ops | `chargeback_model` | Offering posture | **MAP** | Pattern only. |
| Allocation math / GL | Engine | Finance system | — | — | **EXTERNAL** | OSM-M-004. |
| AI / ESG solution types | New 5.0.1 solution types | Solution | AI Act flags / characteristics | mixed | **EXTERNAL** / characteristic | Do not add `tbm_ai_solution`. |

### TBM conclusion

Optional labels remain the right *kind* of mapping. They are **version-stale** and possibly **wrong grain** (Stack vs Service/Solutions). Human decision D7. No TBM allocation engine in OSM.

---

## Cross-model notes (detail in 04)

Independent recurrence:

- **Definition vs instance** — TMF spec/inventory, CSDM TMS vs Service Instance, OSM Service vs out-of-scope instance. **Strong MAP.**
- **Requestable variant** — ITIL offering, CSDM TMSO, OSM Offering. TMF puts this partly in characteristics/product. **MAP.**
- **Who provides** — ITIL supplier, CSDM Technology Provider, ArchiMate Actor, TMF relatedParty. **MAP to `providers`.**
- **Definition lifecycle** — TMF, CSDM, OSM. Distinct from ITIL activity lifecycle. **MAP + DOCUMENT.**
- **Service–service dependency** — TMF spec relationship, CSDM, ArchiMate serving, ITIL. **GAP-002.**
- **Financial taxonomy ≠ operational ownership** — TBM vs OSM Stack. **Keep distinct.**
