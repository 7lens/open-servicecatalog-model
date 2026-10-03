# TOGAF

**Mapped version:** **TOGAF Standard, 10th Edition**, with
**Technical Corrigendum 1**.

> **Mapping basis (2026-06-11):** The TOGAF Standard, 10th Edition is
> confirmed by The Open Group as
> [introduced in April 2022 and since expanded with additional TOGAF
> Series Guides](https://blog.opengroup.org/2025/07/01/navigating-the-togaf-standard-10th-edition-updates-and-insights/),
> and is
> [available to download free for non-commercial use](https://www.opengroup.org/togaf-standard-10th-edition-downloads).
> The exact publication date of **Technical Corrigendum 1** could not
> be confirmed from an openly accessible Open Group source — the
> TOGAF Standard publications area requires sign-in — so the previous
> "(May 2025)" qualifier is treated as **unverified at 2026-06-11
> (sources consulted: The Open Group TOGAF Standard, 10th Edition
> downloads and specifications pages, which are gated)** and is
> dropped rather than asserted. The 10th-Edition four-domain
> structure used below is stable across the corrigendum. Source
> wording was rephrased for licensing compliance.

**Status:** **MAPPED** (stack-level domain label only)

OSM is **not** a TOGAF method, ADM implementation, or architecture
content metamodel. OSM does **not** represent the entire TOGAF
architecture model.

TOGAF’s core architecture domains (Business, Data, Application,
Technology) are **broader** than OSM. OSM is a technological-service
catalog. Mapping stays at **Technology Stack** unless a future
concrete interoperability requirement proves a Service-level field
is necessary. Do **not** add TOGAF domain fields to Service now.

Security is an architecture *practice* concern in TOGAF. It is
**not** a fifth core domain in the standard’s four-domain set.
Example `togaf_domain` values should use those four names, not
“Security Architecture”.

## Concept walk (TOGAF Standard, 10th Edition top-level structure)

Every top-level TOGAF area below carries a status from the index
vocabulary (MAPPED / PARTIAL / EXTERNAL / NOT IN SCOPE / FUTURE /
OPTIONAL), so none is silently missing.

| TOGAF top-level area | OSM target | Status + kind | Outside OSM |
|----------------------|------------|---------------|-------------|
| Technology Architecture (one of four core domains) | `mappings.togaf_domain` on Technology Stack | **MAPPED** — partial label. A free-text reference hint, not a TOGAF building block. | ADM, content metamodel |
| Business / Data / Application Architecture (the other three domains) | Same optional stack label | **PARTIAL** — conceptual only if a stack is discussed in that domain. OSM stays technological. | Those domains as OSM entities |
| Architecture Development Method (ADM) phases A–H + Preliminary | — | **EXTERNAL** — OSM is a catalog, not a method. | The ADM cycle |
| Architecture Content Framework / content metamodel | — | **EXTERNAL** — OSM is not a TOGAF content metamodel. | Deliverables, artifacts, building blocks |
| Enterprise Continuum & Tools / Architecture Repository | — | **EXTERNAL** — OSM is one catalog, not the TOGAF repository classification. | Continuum, reference libraries |
| Architecture Capability (governance, board, contracts, maturity) | — | **EXTERNAL** — capability/governance machinery is outside OSM. | Governance framework |
| Applying the TOGAF Standard (adaptation, security/risk practice) | — | **NOT IN SCOPE** — practice guidance, including security as a practice concern, is outside OSM's boundary. | Practitioner guidance |

## Mapping table

| External concept | OSM target | Grain | Status + kind | Outside OSM |
|------------------|------------|-------|---------------|-------------|
| Technology Architecture (one of four core domains) | `mappings.togaf_domain` | **Technology Stack only** | **MAPPED** — partial label. Free-text reference hint, not a TOGAF building block. | ADM, content metamodel |
| Data / Application / Business Architecture | Same optional stack label | Stack | **PARTIAL** — conceptual only if a stack is discussed in that domain. OSM stays technological. | Those domains as OSM entities |
| Technology service / building block | Service | Service | **PARTIAL** — conceptual. OSM Service is the stable technological definition. TOGAF “service” is broader. | Application and business building blocks |
| Service Offering | — | Offering | **PARTIAL** — variant grain stays in OSM. | TOGAF catalog hierarchy |
| ADM, capabilities, governance | — | — | **EXTERNAL** | Method and governance |

## What stays in TOGAF (**EXTERNAL**)

- ADM phases and architecture governance
- capability models
- application architecture as OSM entities
- the TOGAF content metamodel
- a claim that OSM covers Business + Data + Application + Technology

The `togaf_domain` mapping sits on Technology Stack, not on Service
or Offering. Exact field definitions are in
[`SPECIFICATION.md`](../../SPECIFICATION.md).
