# ITIL v5

- **Status:** PARTIALLY COMPATIBLE (selective compatibility)
- **Universe:** OSM-C-001 (model / taxonomy / architectural framework)
- **Decision:** OSM-C-004
- **OSM schema fields today:** none dedicated to ITIL

OSM is **not** an alternative implementation of ITIL. OSM provides a
small canonical core definition of technological services and
offerings that can be **mapped** to ITIL (and other frameworks) and
integrated with customer systems. Compatibility is semantic
interoperability, not reproduction.

```
OSM core definition
        ↓
semantic mapping
        ↓
ITIL / CSDM / ArchiMate / other frameworks
        ↓
customer tools and systems
```

## 1. Model overview

ITIL v5 (PeopleCert) is a service-management practice framework. It
describes services, service offerings, a service catalogue, service
lifecycle activities, roles, suppliers, and a wide operating model
(practices, value streams, products, consumers, service levels).

ITIL is a management framework, not a machine-readable schema. OSM
aligns with a **narrow technological-service subset** of ITIL
language.

## 2. Scope

In scope for this analysis: conceptual alignment of OSM Service,
Service Offering, catalog shape, definition lifecycle, ownership,
and ICT Provider with the corresponding ITIL ideas.

Out of OSM core (deliberate, not a gap to fill here): ITIL practices,
process structures, business/customer services, digital products,
consumers, value streams, CMDB/CI links, and detailed SLA models.

## 3. OSM concepts corresponding to the model

| OSM | ITIL v5 | Conclusion |
|-----|---------|------------|
| Service | Service | **Compatible at conceptual level, deliberately narrower.** OSM Service is a **technological service** definition. Not expanded to business services, customer services, outcomes, or broader ITIL service semantics. |
| Service Offering | Service offering | **Compatible with the useful core.** OSM offering is an atomic requestable/deliverable variant of a technological Service. No consumer/group/commercial semantics in OSM. |
| Service + Service Offering records | Service catalogue | **Naturally compatible.** No separate ServiceCatalogue entity. The OSM catalog *is* the machine-readable technological service catalog. |
| `version`, `valid_from`, `valid_to`, `lifecycle_state` | ITIL lifecycle activities/stages | **Different concerns.** OSM lifecycle is definition validity/state. Do not import ITIL lifecycle activities as OSM states. |
| `accountable`; Technology Stack Owner | ITIL roles | **Core accountability only.** Do not reproduce ITIL role taxonomies. |
| ICT Provider | Supplier / provider | **Compatible with relevant supplier/provider semantics.** Do not reproduce ITIL supplier-management structures. |
| Technology Stack | (no required ITIL class) | Operational ownership domain; not an ITIL catalogue category. |

## 4. Attribute compatibility

No ITIL-specific fields were added. Existing OSM fields are enough
for the alignments above. ITIL practice attributes, SLA metrics, and
consumer-facing commercial attributes stay outside OSM.

## 5. Relationship compatibility

OSM keeps **Technology Stack → Service → Service Offering**.

Service → Service relationships are **deliberately outside the
current OSM core**. That is not a permanent rejection; they are not
justified in the minimal technological-service definition unless a
later interoperability requirement says otherwise.

Asset/CI relationships are likewise outside OSM.

## 6. Terminology differences

- ITIL **service** is broader (business, customer, outcome). OSM
  **Service** means technological service only.
- ITIL **service offering** often includes consumer and commercial
  packaging. OSM **Service Offering** is a requestable/deliverable
  variant of a technological service.
- ITIL **lifecycle** is management activity. OSM **lifecycle_state**
  plus version/validity describe the current **definition**.
- ITIL **service catalogue** is a management concept. OSM does not
  reify it as an entity.

## 7. Deliberate boundaries (not missing OSM capabilities)

These may matter in the broader 7lens model or in customer systems
and frameworks. OSM does not reproduce them to claim ITIL
compatibility:

- Digital Product
- Business Service
- Business outcomes
- Consumers / consumer groups
- Value Streams
- broader service relationships (including Service → Service)
- Asset / Configuration Item relationships
- detailed Service Level / SLA modelling
- ITIL practices and process structures

## 8. Potential extensions

None in this task. Further ITIL structures need an explicit `OSM-M-*`
or `OSM-C-*` decision. Do not add them because ITIL has them
(OSM-M-004).

## 9. Decisions still required

- Service → Service relationships: outside current OSM core; reopen
  only if a concrete interoperability requirement appears.
- Request-catalog vs technical-catalog split: not adopted.
- SLA objects: remain outside OSM.

## 10. Compatibility status

**PARTIALLY COMPATIBLE / SELECTIVE COMPATIBILITY**

OSM aligns with the ITIL v5 concepts that are useful for a small
technological service catalog. OSM is substantially smaller and
narrower than ITIL. OSM does not implement ITIL.
