# ArchiMate

**Mapped version:** **ArchiMate 4** (The Open Group, announced
27 April 2026). ArchiMate 3.2 is **not** the current mapping target.
Do not describe 3.2 as current.

**Status:** **MAPPED** (conceptual, technology-service grain)

OSM is **not** an ArchiMate model, viewpoint set, or architecture
repository.

ArchiMate 4 merges the former per-layer Business / Application /
Technology **Service** elements into a generic Common Domain
**Service**. Layers are restyled as domains. The relevant
compatibility **anchor** for OSM is that generic Service, used in a
**technology-domain** context.

OSM remains **technology-service focused**. It does not create a
layer-specific ArchiMate entity hierarchy.

## Mapping table

| External concept (ArchiMate 4) | OSM target | Grain | Kind | Outside OSM |
|--------------------------------|------------|-------|------|-------------|
| Generic **Service** (technology-domain use) | OSM Service | Service | Conceptual. Closest element. OSM Service is a **definition**, not a runtime object and not a layered architecture element. | Business-domain and application-domain uses of Service |
| ArchiMate 3.2 Technology Service (historical) | OSM Service | Service | Historical alias only. Current mapping is ArchiMate 4 generic Service. | 3.2 metamodel |
| Service Offering | — | Offering | No required ArchiMate twin. Variation stays in OSM. | — |
| Technology Stack | — | Stack | Operational ownership domain. Not absorbed as grouping, capability or device. | ArchiMate grouping / device |
| Serving / realization | ICT Provider via `providers` (who provides) | Service/Offering | OSM `providers` is not an ArchiMate relationship type. Architecture views of serving live in ArchiMate. | Serving, realization, composition |
| Application / Application Service | — | — | **EXTERNAL** | Those architecture elements |
| Service Instance / running inventory | — | — | **EXTERNAL** | Runtime |

There are no ArchiMate-specific schema fields.

## What stays in ArchiMate (**EXTERNAL**)

- Business-domain and application-domain Service uses
- serving and realization relationships
- architecture views and viewpoints
- a layer-specific entity hierarchy inside OSM (forbidden)
- operational attributes that ArchiMate does not model (OSM
  `lifecycle_state`, RTO/RPO, cost characterization)

In ArchiMate 4, “service” is generic across domains. In OSM, Service
always means **technological** service. Join OSM records to an
architecture repository when you need the other domains.
