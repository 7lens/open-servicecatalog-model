# ArchiMate

**Mapped version:** **ArchiMate 4** (The Open Group, published
April 2026). ArchiMate 3.2 is **not** the current mapping target.
Do not describe 3.2 as current.

> **Mapping basis (2026-06-11):** The release of the ArchiMate 4
> Specification is confirmed by The Open Group — it was
> [discussed at The Open Group Summit in Oslo on 28 April 2026 as a
> "landmark release"](https://blog.opengroup.org/2026/05/20/discussing-the-release-of-the-archimate-4-specification/),
> and an independent practitioner analysis records that
> [Version 4 is the first major update in a decade and merges the
> previously per-layer behavior concepts into a single set in a
> "Common Domain"](https://bizzdesign.com/blog/archimate-4-changes).
> The file previously asserted "announced 27 April 2026"; the
> authoritative sources date the public discussion to 28 April 2026
> and the blog publication to 20 May 2026, so the exact day of first
> announcement is not independently confirmable — the version string
> is corrected to the confirmable "published April 2026". Source
> wording was rephrased for licensing compliance.

**Status:** **MAPPED** (conceptual, technology-service grain)

OSM is **not** an ArchiMate model, viewpoint set, or architecture
repository.

ArchiMate 4 merges the former per-layer Business / Application /
Technology **Service** elements (together with Process, Function and
Event) into a single generic behavior set in the **Common Domain**.
Layers are restyled as domains. The relevant compatibility **anchor**
for OSM is that generic Service, used in a **technology-domain**
context.

OSM remains **technology-service focused**. It does not create a
layer-specific ArchiMate entity hierarchy.

## Concept walk (ArchiMate 4 top-level structure)

Every top-level ArchiMate 4 grouping below carries a status from the
index vocabulary (MAPPED / PARTIAL / EXTERNAL / NOT IN SCOPE /
FUTURE / OPTIONAL), so none is silently missing.

| ArchiMate 4 top-level area | OSM target | Status + kind | Outside OSM |
|----------------------------|------------|---------------|-------------|
| Common Domain generic **Service** (technology-domain use) | OSM Service | **MAPPED** — conceptual. Closest element. OSM Service is a **definition**, not a runtime object and not a layered architecture element. | Business-domain and application-domain uses of the same generic Service |
| Common Domain behavior set (Process, Function, Event, Collaboration, Role) | — | **EXTERNAL** — OSM models catalog definitions, not behavior/collaboration elements. | ArchiMate behavior modeling |
| Technology domain (Node, Device, System Software, Artifact, etc.) | — | **EXTERNAL** — OSM does not model infrastructure elements or deployment. | Technology-layer structure elements |
| Application domain (Application Component, Application Service) | — | **EXTERNAL** — those architecture elements stay in ArchiMate. | Application-domain structure |
| Business domain (Business Service, Actor, Product, Contract) | — | **EXTERNAL** — Contract is now a kind of Business Object in v4; none is an OSM entity. | Business-domain structure |
| Motivation elements (Stakeholder, Driver, Goal, Requirement) | — | **NOT IN SCOPE** — motivation modeling is outside OSM's technological-service boundary. | ArchiMate motivation extension |
| Strategy elements (Resource, Capability, Course of Action) | — | **NOT IN SCOPE** — strategy modeling is outside OSM. | ArchiMate strategy extension |
| Implementation & Migration elements (Work Package, Plateau) | — | **NOT IN SCOPE** — transformation planning is outside OSM. | ArchiMate implementation extension |
| Relationships (serving, realization, composition, assignment) | ICT Provider via `providers` (who provides) only | **EXTERNAL** — OSM `providers` is not an ArchiMate relationship type; architecture views of serving/realization live in ArchiMate. | Serving, realization, composition, assignment |
| Views / viewpoints | — | **EXTERNAL** — OSM is not a modeling/diagramming repository. | ArchiMate views |

## Mapping table

| External concept (ArchiMate 4) | OSM target | Grain | Status + kind | Outside OSM |
|--------------------------------|------------|-------|---------------|-------------|
| Generic **Service** (technology-domain use) | OSM Service | Service | **MAPPED** — conceptual. Closest element. OSM Service is a **definition**, not a runtime object and not a layered architecture element. | Business-domain and application-domain uses of Service |
| ArchiMate 3.2 Technology Service (historical) | OSM Service | Service | **MAPPED** — historical alias only. Current mapping is the ArchiMate 4 generic Service. | 3.2 metamodel |
| Service Offering | — | Offering | **PARTIAL** — no required ArchiMate twin. Variation stays in OSM. | — |
| Technology Stack | — | Stack | **PARTIAL** — operational ownership domain. Not absorbed as grouping, capability or device. | ArchiMate grouping / device |
| Serving / realization | ICT Provider via `providers` (who provides) | Service/Offering | **EXTERNAL** — OSM `providers` is not an ArchiMate relationship type. Architecture views of serving live in ArchiMate. | Serving, realization, composition |
| Application / Application Service | — | — | **EXTERNAL** | Those architecture elements |
| Service Instance / running inventory | — | — | **EXTERNAL** | Runtime |

There are no ArchiMate-specific schema fields.

## What stays in ArchiMate (**EXTERNAL**)

- Business-domain and application-domain Service uses
- the Common Domain behavior set beyond the generic Service anchor
- serving and realization relationships
- architecture views and viewpoints
- a layer-specific entity hierarchy inside OSM (forbidden)
- operational attributes that ArchiMate does not model (OSM
  `lifecycle_state`, RTO/RPO, cost characterization)

In ArchiMate 4, “service” is generic across domains. In OSM, Service
always means **technological** service. Join OSM records to an
architecture repository when you need the other domains.

Exact field definitions are in
[`SPECIFICATION.md`](../../SPECIFICATION.md).
