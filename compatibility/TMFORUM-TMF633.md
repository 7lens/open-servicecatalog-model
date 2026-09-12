# TM Forum TMF633 — Service Catalog

- **Status:** PARTIALLY COMPATIBLE
- **Universe:** OSM-C-001 (model / taxonomy / architectural framework)
- **Decisions applied:** OSM-M-001, OSM-M-002, OSM-M-003, OSM-M-004

This file records the first TM Forum analysis as implemented in OSM.
It is **not** a claim that OSM implements TMF633, SID, or TMF
certification. Compatibility does not mean copying (OSM-M-004).

## 1. Model overview

TM Forum TMF633 is the REST API and information model for **Service
Catalog Management**. Related TMF / SID ideas include service
specification vs service instance, catalog vs inventory, and
customer-facing vs resource-facing services.

## 2. Scope

In scope for OSM: catalog-level **definition** of technological
services and requestable offerings, with optional characteristics
and definition version, validity and `lifecycle_state`.

Out of scope for OSM: TMF service instances, resource inventory,
product catalog, CFS/RFS as OSM entities, TMF API resources, and
the full characteristic/lifecycle metamodel.

## 3. OSM concepts corresponding to the model

| OSM | TMF / SID role | Status |
|-----|----------------|--------|
| Service | Semantic role of **ServiceSpecification** (stable definition). OSM does **not** add a ServiceSpecification entity (OSM-M-003). | MAPPED (selective) |
| Service Offering | Requestable catalog variant. Not imported as TMF ServiceCandidate / catalog hierarchy. | PARTIAL — grain kept as OSM offering |
| Characteristic (nested) | Inspired by TMF characteristics; small OSM structure only (OSM-M-001). | MAPPED (selective) |
| `version`, `valid_from`, `valid_to`, `lifecycle_state` | Definition may evolve while `id` stays (OSM-M-002). OSM lifecycle enum on Service; not TMF's full lifecycleStatus machine. | MAPPED (selective) |
| Technology Stack | No TMF633 counterpart adopted. | NOT APPLICABLE |
| ICT Provider | Not mapped in this analysis. | NOT ANALYZED |
| Service instance / inventory | Out of OSM scope. | NOT APPLICABLE |

## 4. Attribute compatibility

Adopted into OSM (small subset):

- nested characteristic fields listed in `SPECIFICATION.md` §5.1
- Service `version`, `valid_from`, `valid_to`, `lifecycle_state`

Not adopted: TMF characteristic specification catalog, `@type` /
`@schemaLocation`, full lifecycleStatus state machines, bundled
offering graphs, ServiceCandidate, ServiceCategory, CFS/RFS, TMF
API resource structures, or TMF identifier schemes.

## 5. Relationship compatibility

OSM keeps **Technology Stack → Service → Service Offering**.
No TMF catalog/category/candidate tree was added.

## 6. Terminology differences

- OSM **Service** = technological service **definition** (TMF
  specification role), never a running instance.
- OSM **Service** is not TMF's broader "service" (including CFS).
- OSM characteristic `name` is a key on the parent; it is not a
  TMF entity id.

## 7. Gaps

Deliberate (OSM-M-004), not accidental omission:

- no ServiceSpecification entity
- no service instance
- no CFS/RFS split
- no TMF catalog API resources
- no ServiceCandidate / ServiceCategory
- no in-catalog history of prior definition versions (one row per `id`)
- no offering-level version/validity

## 8. Potential extensions

None proposed here. Further TMF structures need a new `OSM-M-*`
decision. Do not add them because TMF has them.

## 9. Decisions still required

- CFS/RFS remains out of OSM unless a later decision says otherwise
- TMF identifier schemes will not replace OSM 2-/3-segment IDs
- Offering-level version/validity was not part of OSM-M-002

## 10. Compatibility status

**PARTIALLY COMPATIBLE**

OSM adopts a small set of useful TMF *semantics* (definition vs
identity, nested characteristics, version/validity, Service
`lifecycle_state`). OSM is not a TMF633 implementation.
