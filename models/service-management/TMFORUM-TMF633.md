# TM Forum

OSM is **not** a TMF633 implementation, SID implementation, or TMF
certification.

TM Forum TMF633 is the REST API and information model for Service
Catalog Management. OSM adopts a small set of useful catalog
**semantics** — not the API, not the full characteristic metamodel,
and not the product or resource catalogs.

## What maps

| OSM | TMF / SID role | How they relate |
|-----|----------------|-----------------|
| Service | ServiceSpecification (stable definition) | OSM Service *is* the definition. OSM does not add a ServiceSpecification entity. |
| Service Offering | Requestable catalog variant | Grain kept as OSM offering. Not imported as ServiceCandidate or a catalog hierarchy. |
| Characteristic (nested) | Characteristic | Inspired by TMF characteristics; a small OSM structure only. |
| `version`, `valid_from`, `valid_to`, `lifecycle_state` | Version / validity / lifecycleStatus | Identity stays; the definition may evolve. OSM uses a small lifecycle enum on Service, not TMF’s full state machine. |
| Technology Stack | — | No TMF633 counterpart adopted. |
| Service instance / inventory | Service instance | Outside OSM. |

## What OSM takes from TMF semantics

- nested characteristic fields ([`SPECIFICATION.md`](../../SPECIFICATION.md) §5.1)
- Service `version`, `valid_from`, `valid_to`, `lifecycle_state`

## What stays in TM Forum

- TMF characteristic specification catalog
- `@type` / `@schemaLocation`
- full `lifecycleStatus` state machines
- bundled offering graphs
- ServiceCandidate, ServiceCategory
- CFS / RFS as OSM entities
- TMF API resource structures
- TMF identifier schemes (OSM keeps 2- and 3-segment IDs)
- in-catalog history of prior definition versions (one row per `id`)
- offering-level version / validity

## Terminology

- OSM **Service** = technological service **definition** (TMF
  specification role), never a running instance.
- OSM **Service** is not TMF’s broader “service” (including CFS).
- OSM characteristic `name` is a key on the parent; it is not a
  TMF entity id.

OSM keeps **Technology Stack → Service → Service Offering**. It
does not add a TMF catalog/category/candidate tree.
