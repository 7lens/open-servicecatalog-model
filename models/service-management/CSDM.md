# ServiceNow CSDM

OSM is **not** a CSDM implementation and not a ServiceNow product
model.

CSDM (Common Service Data Model) is a vendor-specific CMDB and
service-management class model. OSM is vendor-neutral. Compatibility
means an adopter can **project** OSM records into relevant CSDM
classes — not that OSM reproduces CSDM.

```
OSM core definition
        ↓
semantic mapping
        ↓
CSDM classes in ServiceNow
        ↓
customer tools and systems
```

## What maps

| OSM | CSDM | How they relate |
|-----|------|-----------------|
| Service | Technology Management Service | Conceptually maps. OSM remains narrower and technology-focused. OSM Service is the canonical **definition**, not a runtime object. |
| Service Offering | Service Offering | Conceptually maps. OSM Offering is an atomic requestable/deliverable technological variant. Use Characteristics and optional `providers` rather than hard-coding every dimension. |
| `accountable`; Technology Stack Owner | Service Owner | Existing OSM accountability remains valid. OSM does not reproduce CSDM role taxonomies. |
| ICT Provider + `providers` | Technology Provider | Explicitly supported. Canonical ICT Provider entity; Service and/or Offering hold id references. |
| Technology Stack | — | Operational ownership domain. |

Canonical provider association:

```
Service / Offering  →  providers (ids)  →  ICT Provider
```

That is not a generic Service → Service relationship. Reverse
Provider → Service links are derived from `providers`.

## What stays in CSDM

- Service Instance / deployed implementation
- Business Service
- Application Service
- CMDB / Configuration Items
- Product Models
- Value Streams
- Service → Service relationships
- CSDM domain tables and prescribed class hierarchy

No CSDM-specific schema fields are required.

## Terminology

- CSDM **service** spans business, application and technical layers.
  OSM **Service** means technological service definition only.
- CSDM **Service Instance** is deployed/runtime. OSM has no instance
  entity.
- CSDM **Service Offering** often sits in a sell/consume or CMDB
  graph. OSM Offering is a catalog variant of a technological Service.
- CSDM **Technology Provider** may be a CI or company record. OSM
  ICT Provider is the catalog’s canonical provider entity.
