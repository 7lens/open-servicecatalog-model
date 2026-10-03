# ITIL

**Mapped version:** ITIL **Version 5** (released by PeopleCert as
"ITIL (Version 5)"; Foundation availability in early 2026). ITIL 4
remains a valid parallel path and prerequisite for some Version 5
modules; OSM does not require an adopter to have moved.

> **Mapping basis (2026-06-11):** Version 5 is the current ITIL
> designation, branded simply "ITIL (Version 5)" and delivered by
> PeopleCert/AXELOS; see the
> [PeopleCert "ITIL (Version 5) explained" announcement](https://www.peoplecert.org/news-and-announcements/itil-version-5-explained).
> Published sources disagree on the exact Foundation general-availability
> day (variously reported in late January and February 2026), so OSM
> states "early 2026" rather than a single calendar date
> (exact GA day unverified at 2026-06-11; sources consulted:
> [PeopleCert](https://www.peoplecert.org/news-and-announcements/itil-version-5-explained),
> [TeamDynamix overview](https://www.teamdynamix.com/blog/an-introduction-to-the-itil-framework/)).
> This mapping is unaffected by the exact day: it targets ITIL's
> stable service/catalogue concepts, not any lifecycle date. Source
> wording was rephrased for licensing compliance.

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

Every top-level ITIL concept below carries a status from the index
vocabulary (MAPPED / PARTIAL / EXTERNAL / NOT IN SCOPE / FUTURE /
OPTIONAL), so none is silently missing.

| External concept | OSM target | Grain | Status + kind | Outside OSM |
|------------------|------------|-------|---------------|-------------|
| ITIL technological / IT service (the catalogued capability) | Service | Service | **PARTIAL** — conceptual. OSM is narrower: technological definition only, not business service or customer outcome. | Business Service, Digital Product |
| ITIL service offering | Service Offering | Offering | **PARTIAL**. OSM offering is an atomic requestable **technological** variant, not consumer/commercial packaging. | Consumers, consumer groups, commercial bundles |
| Service catalogue | The OSM catalog files themselves | Catalog | **PARTIAL** — conceptual. No `ServiceCatalogue` entity. | ITIL catalogue practices, request workflows |
| Product and Service Lifecycle (Discover, Design, Acquire, Build, Transition, Operate, Deliver, Support) | — | — | **NOT IN SCOPE** as an OSM enum. Do **not** map these eight activities onto `lifecycle_state`. | The whole Version 5 lifecycle |
| OSM `lifecycle_state` (`draft` \| `pilot` \| `production` \| `sunset` \| `retired`) | Compact **definition** state | Service | **MAPPED** for OSM's own definition state; **not** the ITIL lifecycle | ITIL management activities |
| Supplier / provider | ICT Provider via `providers` | Service and/or Offering | **PARTIAL**. Operator / deliverer / technology provider only (**OSM-C-006**). | Supplier-management practices |
| Service Owner | `accountable` | Service | **PARTIAL** | Full ITIL role taxonomies |
| ITIL practices (service management, operating-model activities) | — | — | **EXTERNAL**. OSM maps catalogue/service definition, not practices. | ITIL practice library |
| Supporting-service / service–service dependency | — | — | **EXTERNAL** (**OSM-C-008**) | Service→Service graph |
| Digital Product, consumers, value streams | — | — | **EXTERNAL** | Those ITIL objects |
| SLA / contract models | — | — | **EXTERNAL**. OSM carries no SLA/contract object. | ITIL service-level and supplier management |

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
