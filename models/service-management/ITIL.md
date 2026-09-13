# ITIL

OSM is **not** an alternative implementation of ITIL.

ITIL is a service-management practice framework. OSM is a small
machine-readable catalog of **technological** services. The two
work together: OSM holds the canonical definition; ITIL describes
how the organization manages, improves and operates services.

```
OSM core definition
        ↓
semantic mapping
        ↓
ITIL practices and operating model
        ↓
customer tools and systems
```

## What maps

| OSM | ITIL | How they relate |
|-----|------|-----------------|
| Service | Service | Compatible at conceptual level, deliberately narrower. OSM Service is a **technological service** definition — not a business service, customer service, or outcome. |
| Service Offering | Service offering | Compatible with the useful core. OSM offering is an atomic requestable/deliverable variant. Consumer, group and commercial packaging stay in ITIL / commercial systems. |
| Service + Offering records | Service catalogue | Naturally compatible. OSM does not add a ServiceCatalogue entity; the catalog *is* the machine-readable technological service catalog. |
| `version`, `valid_from`, `valid_to`, `lifecycle_state` | Lifecycle activities | Different concerns. OSM lifecycle is definition validity/state. ITIL lifecycle is management activity. |
| `accountable`; Technology Stack Owner | Roles | Core accountability only. OSM does not reproduce ITIL role taxonomies. |
| ICT Provider | Supplier / provider | Compatible with relevant supplier semantics. OSM does not reproduce supplier-management practices. |
| Technology Stack | — | Operational ownership domain; not an ITIL catalogue category. |

No ITIL-specific schema fields are required. Existing OSM fields
are enough for the alignments above.

## What stays in ITIL

These belong in ITIL (or in 7lens / customer systems), not in OSM:

- ITIL practices and process structures
- Digital Product, Business Service, business outcomes
- Consumers / consumer groups
- Value streams
- Service → Service relationships
- Asset / Configuration Item relationships
- Detailed SLA / contract models

## Terminology

- ITIL **service** is broader. OSM **Service** means technological
  service only.
- ITIL **service offering** often includes consumer and commercial
  packaging. OSM **Service Offering** is a requestable variant of a
  technological service.
- ITIL **lifecycle** is management activity. OSM
  `lifecycle_state` plus version/validity describe the current
  **definition**.

OSM aligns with the ITIL concepts that are useful for a small
technological service catalog. It does not implement ITIL.
