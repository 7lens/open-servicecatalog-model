# TM Forum TMF633

**Mapped version:** TMF633 Service Catalog API **v4.0.0**
(TM Forum Approved production). TMF633 v5 is preproduction and is
**not** the mapping target.

**Status:** **PARTIAL**

OSM is **not** a TMF633 implementation, SID implementation, or TMF
certification. TMF633 is the REST API and information model for
Service Catalog Management. OSM adopts a small set of useful catalog
**semantics**. It does not reproduce the complete TMF information
model, the API, or the product/resource catalogs.

## Mapping table

| External concept (TMF633 v4.0.0) | OSM target | Grain | Kind | Outside OSM |
|----------------------------------|------------|-------|------|-------------|
| **ServiceSpecification** (stable catalog definition) | OSM **Service** | Service | Conceptual / partial. OSM Service *plays this role*. OSM does **not** add a ServiceSpecification entity. | Full TMF specification metamodel, `@type`, identifier schemes |
| Requestable catalog variant | Service Offering | Offering | Partial. Grain kept as OSM offering. | ServiceCandidate, bundled offering graphs |
| Characteristic | Nested `characteristics` | Service or Offering | Partial. Inspired by TMF; a small OSM structure, not a characteristic-specification catalog. | TMF characteristic specification catalog |
| `lifecycleStatus` / version / validity | `version`, `valid_from`, `valid_to`, `lifecycle_state` | Service | Partial. OSM uses a **compact** lifecycle enum on Service only. | TMF full state machine; offering-level version |
| ServiceCandidate | — | — | **EXTERNAL** | Candidate catalog objects |
| ServiceCategory | — | — | **EXTERNAL** | Category tree |
| Customer Facing Service (CFS) / Resource Facing Service (RFS) | — | — | **EXTERNAL**. OSM stays technology-service focused. | CFS/RFS as entities |
| TMF638 Service Inventory / Service Instance | — | — | **EXTERNAL** | Inventory |
| `serviceSpecRelationship` (spec-to-spec) | — | — | **EXTERNAL** (**OSM-C-008**) | Dependency graph |

## ServiceSpecification and OSM Service

TMF633 separates specification (what can be delivered) from instance
(what is running). OSM Service is the **definition** — the same *job*
as ServiceSpecification for a technological catalog.

OSM intentionally keeps a smaller model:

- no extra ServiceSpecification entity
- no Candidate / Category tree
- no CFS / RFS split inside OSM
- Technology Stack → Service → Service Offering remains the only
  catalog nesting

Join OSM to TMF633 when an adopter needs the full TMF catalog API.

## What OSM takes from TMF semantics

- nested characteristic fields ([`SPECIFICATION.md`](../../SPECIFICATION.md) §5.1)
- Service `version`, `valid_from`, `valid_to`, `lifecycle_state`

## What stays in TM Forum (**EXTERNAL**)

- Candidate
- Category
- Customer Facing Service (CFS)
- Resource Facing Service (RFS)
- Service Inventory / Service Instance (TMF638 and related)
- TMF characteristic specification catalog
- `@type` / `@schemaLocation`
- full `lifecycleStatus` state machines
- bundled offering graphs
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
