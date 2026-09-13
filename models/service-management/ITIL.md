# ITIL

**Mapped version:** ITIL **Version 5** (general availability
12 February 2026). ITIL 4 remains a valid parallel path and
prerequisite for some Version 5 modules; OSM does not require an
adopter to have moved.

**Status:** **PARTIAL**

OSM is **not** an ITIL implementation. ITIL is a service-management
practice framework. OSM is a small machine-readable catalog of
**technological** services. OSM can **map** to ITIL service and
catalogue concepts; it does not implement ITIL practices, value
streams, or the Product and Service Lifecycle.

```
OSM core definition
        ↓
semantic mapping
        ↓
ITIL practices and operating model
        ↓
customer tools and systems
```

## Mapping table

| External concept | OSM target | Grain | Kind | Outside OSM |
|------------------|------------|-------|------|-------------|
| ITIL technological / IT service (the catalogued capability) | Service | Service | Conceptual / partial. OSM is narrower: technological definition only, not business service or customer outcome. | Business Service, Digital Product |
| ITIL service offering | Service Offering | Offering | Partial. OSM offering is an atomic requestable **technological** variant, not consumer/commercial packaging. | Consumers, consumer groups, commercial bundles |
| Service catalogue | The OSM catalog files themselves | Catalog | Conceptual. No `ServiceCatalogue` entity. | ITIL catalogue practices, request workflows |
| Product and Service Lifecycle (Discover, Design, Acquire, Build, Transition, Operate, Deliver, Support) | — | — | **NOT IN SCOPE** as an OSM enum. Do **not** map these eight activities onto `lifecycle_state`. | The whole Version 5 lifecycle |
| OSM `lifecycle_state` (`draft` \| `pilot` \| `production` \| `sunset` \| `retired`) | Compact **definition** state | Service | Direct for OSM; **not** the ITIL lifecycle | ITIL management activities |
| Supplier / provider | ICT Provider via `providers` | Service and/or Offering | Partial. Operator / deliverer / technology provider only (**OSM-C-006**). | Supplier-management practices |
| Service Owner | `accountable` | Service | Partial | Full ITIL role taxonomies |
| Supporting-service / service–service dependency | — | — | **EXTERNAL** (**OSM-C-008**) | Service→Service graph |
| Digital Product, consumers, value streams | — | — | **EXTERNAL** | Those ITIL objects |

No ITIL-specific schema fields are required.

## ITIL Version 5 lifecycle vs OSM `lifecycle_state`

These are different objects.

| | OSM `lifecycle_state` | ITIL Version 5 Product and Service Lifecycle |
|--|------------------------|-----------------------------------------------|
| What it is | Compact state of the **catalog definition** | Eight **management activities** for products and services |
| Values | `draft`, `pilot`, `production`, `sunset`, `retired` | Discover, Design, Acquire, Build, Transition, Operate, Deliver, Support |
| Where it lives | Required field on Service | ITIL operating model / practices |
| May OSM copy it? | No. Do not extend the enum to ITIL activities. | Stays in ITIL |

OSM provides a compact service-definition lifecycle. ITIL provides a
broader management framework. Mapping is conceptual, not 1:1.

## What stays in ITIL (**EXTERNAL**)

- ITIL practices and process structures
- Digital Product
- Consumers / consumer groups
- Value streams
- Business Service and business outcomes
- Service → Service relationships
- Asset / Configuration Item relationships
- Detailed SLA / contract models
- The eight-activity Product and Service Lifecycle

## Terminology

- ITIL **service** is broader. OSM **Service** means technological
  service definition only.
- ITIL **service offering** often includes consumer and commercial
  packaging. OSM **Service Offering** is a requestable variant of a
  technological service — not an ITSM request type, ticket category,
  or fulfillment workflow.
- ITIL **lifecycle** is management activity. OSM
  `lifecycle_state` describes the current **definition**.

OSM can support integration with ITIL-oriented tools. It does not
implement ITIL.
