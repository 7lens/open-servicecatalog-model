# ServiceNow CSDM

**Mapped version:** **CSDM 5** (Technology Management Service;
Application Service renamed **Service Instance**).

**Status:** **PARTIAL**

OSM is **not** a CSDM implementation and not a ServiceNow product
model. CSDM is a vendor-specific CMDB and service-management class
model. OSM is vendor-neutral. An adopter can **project** OSM records
into relevant CSDM classes. OSM does not reproduce CSDM.

```
OSM core definition
        ↓
semantic mapping
        ↓
CSDM classes in ServiceNow
        ↓
customer tools and systems
```

## Mapping table

| External concept (CSDM 5) | OSM target | Grain | Kind | Outside OSM |
|---------------------------|------------|-------|------|-------------|
| Technology Management Service (was Technical Service) | Service | Service | Conceptual / partial. OSM Service is the canonical **definition**, narrower and technology-focused, not a runtime CI. | Business Service |
| Technology Management Service Offering | Service Offering | Offering | Conceptual / partial. OSM uses Characteristics and optional `providers` rather than CSDM dimension tables. | CSDM prescribed offering dimensions |
| Technology Provider | ICT Provider + `providers` | Service and/or Offering | Partial. OSM ICT Provider is catalog master data, not a CMDB company CI. | CMDB company / vendor CIs |
| Service Owner | `accountable` | Service | Partial | CSDM role taxonomies |
| **Service Instance** (was Application Service) and siblings (Data/AI, Network, Connection, Operational Process, Facility) | — | — | **EXTERNAL**. OSM has no instance entity. | Running/deployed objects |
| CMDB Configuration Items | — | — | **EXTERNAL** | Inventory |
| Business Service, Product Models, Value Streams | — | — | **EXTERNAL** | Those CSDM classes |
| Service → Service relationships | — | — | **EXTERNAL** (**OSM-C-008**) | CSDM relationship graph |

Canonical provider association:

```
Service / Offering  →  providers (ids)  →  ICT Provider
```

That is not a generic Service → Service relationship. Reverse
Provider → Service links are derived from `providers`.

No CSDM-specific schema fields are required.

## Technology Management Service vs Service Instance

| | OSM Service | CSDM 5 Technology Management Service | CSDM 5 Service Instance |
|--|-------------|--------------------------------------|-------------------------|
| What | Canonical **catalog definition** of a technological service | Closest CSDM *catalog/management* landing | Deployed / running implementation (and siblings) |
| Runtime? | No | Typically definition/management, not the instance | Yes — **outside OSM** |
| May OSM add it? | Already present | Map conceptually | **Do not** introduce Service Instance into OSM |

CMDB and running-instance inventory stay **outside** OSM.

## What stays in CSDM (**EXTERNAL**)

- Service Instance and related running-instance concepts
- Business Service
- Application Service (CSDM 4 name; CSDM 5 = Service Instance)
- CMDB / Configuration Items
- Product Models
- Value Streams
- Service → Service relationships
- CSDM domain tables and prescribed class hierarchy

## Terminology

- CSDM **service** spans business, application and technical layers.
  OSM **Service** means technological service definition only.
- CSDM **Service Instance** is deployed/runtime. OSM has no instance
  entity.
- CSDM **Service Offering** often sits in a sell/consume or CMDB
  graph. OSM Offering is a catalog variant of a technological Service.
- CSDM **Technology Provider** may be a CI or company record. OSM
  ICT Provider is the catalog’s canonical provider entity — the party
  that materially delivers, operates, or underpins the Service or
  Offering (**OSM-C-006**).
