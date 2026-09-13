# TOGAF

**Mapped version:** **TOGAF Standard, 10th Edition**, with
**Technical Corrigendum 1** (May 2025).

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

## Mapping table

| External concept | OSM target | Grain | Kind | Outside OSM |
|------------------|------------|-------|------|-------------|
| Technology Architecture (one of four core domains) | `mappings.togaf_domain` | **Technology Stack only** | Partial label. Free-text reference hint, not a TOGAF building block. | ADM, content metamodel |
| Data / Application / Business Architecture | Same optional stack label | Stack | Conceptual only if a stack is discussed in that domain. OSM stays technological. | Those domains as OSM entities |
| Technology service / building block | Service | Service | Conceptual. OSM Service is the stable technological definition. TOGAF “service” is broader. | Application and business building blocks |
| Service Offering | — | Offering | Variant grain stays in OSM. | TOGAF catalog hierarchy |
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
