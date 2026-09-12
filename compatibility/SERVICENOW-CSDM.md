# ServiceNow CSDM

- **Status:** PARTIALLY COMPATIBLE (selective compatibility)
- **Universe:** OSM-C-001 (model / taxonomy / architectural framework)
- **Decisions:** OSM-C-003 (universe retained), OSM-C-005 (this analysis),
  OSM-M-006 (canonical ICT Provider references)
- **OSM schema fields today:** none dedicated to CSDM. Provider
  association uses existing ICT Provider ids (`providers` on Service
  and Service Offering).

OSM is **not** a CSDM implementation. OSM provides a small canonical
core of technological Services and Service Offerings. CSDM is a much
broader service-management / CMDB model. OSM should map cleanly into
CSDM without reproducing CSDM runtime, business, application or CMDB
structures.

```
OSM core definition
        ↓
semantic mapping
        ↓
CSDM / ITIL / ArchiMate / other frameworks
        ↓
customer tools and systems
```

## 1. Model overview

The ServiceNow **Common Service Data Model (CSDM)** prescribes CMDB
classes for services, applications, offerings, instances, products,
value streams and related objects. It is vendor-specific. OSM is
vendor-neutral. Compatibility means an adopter can *project* OSM
records into relevant CSDM classes — not that OSM is a ServiceNow
product model (**OSM-C-003**).

## 2. Scope

In scope: conceptual alignment of OSM Service, Service Offering,
ownership, and ICT Provider with CSDM Technology Management Service,
Service Offering, Service Owner, and Technology Provider ideas.

Out of OSM core (deliberate, not a gap to fill here): Service
Instance, Business Service, Application Service, CMDB/CIs, Product
Models, Value Streams, and first-class Service → Service
relationships.

## 3. OSM concepts corresponding to the model

| OSM | CSDM | Conclusion |
|-----|------|------------|
| Service | Technology Management Service | **Conceptually maps.** OSM remains narrower and technology-focused. OSM Service is the canonical **definition** of a technological service, not a runtime object. |
| Service Offering | Service Offering | **Conceptually maps.** OSM Offering is an atomic requestable/deliverable technological variant. Variation may include environment, location, availability, packaging, operating model, provider, and other meaningful characteristics. Do not hard-code every dimension; use generic Characteristics (OSM-M-001) plus optional `providers`. |
| — | Service Instance | **Outside OSM.** Operational/deployed/runtime context. Do not add it. |
| — | Business Service | **Outside OSM.** Broader 7lens/customer context. |
| — | Application Service | **Outside OSM.** |
| — | CMDB / Configuration Item | **Outside OSM.** |
| — | Product Models | **Outside OSM.** Map/interoperate where required; do not reproduce them. |
| `accountable`; Technology Stack Owner | Service Owner | **Existing OSM accountability remains valid.** Do not reproduce CSDM role taxonomies. |
| ICT Provider + `providers` | Technology Provider | **Explicitly supported.** Canonical ICT Provider entity; Service and/or Offering hold id references (OSM-M-006). |
| Technology Stack | (no required CSDM class) | Operational ownership domain. |

## 4. Attribute compatibility

No CSDM-specific fields were added. Offering variation uses existing
Characteristics and optional `providers` ids. CSDM CMDB attributes,
instance attributes, and business-service attributes stay outside OSM.

## 5. Relationship compatibility

OSM keeps **Technology Stack → Service → Service Offering**.

Canonical provider association:

```
Service / Offering  →  providers (ids)  →  ICT Provider
```

That is not a generic Service → Service relationship. It is also
not automatically the same as `dora_third_party_deps`. Whether those
two fields represent genuinely different relationships is unresolved
(**OSM-M-005**, **PROPOSED**).

Service → Service relationships remain **deliberately outside the
current OSM core**. Not a permanent rejection; reopen only if a
concrete interoperability requirement appears.

CI / asset relationships are outside OSM.

## 6. Terminology differences

- CSDM **service** spans business, application and technical layers.
  OSM **Service** means technological service definition only.
- CSDM **Service Instance** is deployed/runtime. OSM has no instance
  entity.
- CSDM **Service Offering** often sits in a sell/consume or CMDB
  graph. OSM Offering is a catalog variant of a technological Service.
- CSDM **Technology Provider** may be a CI or company record. OSM
  ICT Provider is the catalog's canonical provider entity.

## 7. Deliberate boundaries (not missing OSM capabilities)

These may matter in the broader 7lens model or in customer CSDM
implementations. OSM does not reproduce them to claim CSDM
compatibility:

- Service Instance / deployed implementation
- Business Service
- Application Service
- CMDB / Configuration Items
- Product Models
- Value Streams
- broader service relationships (including Service → Service)
- CSDM domain tables and prescribed class hierarchy

## 8. Potential extensions

None in this task. Further CSDM structures need an explicit `OSM-M-*`
or `OSM-C-*` decision. Do not add them because CSDM has them
(OSM-M-004).

## 9. Decisions still required

- Service → Service relationships: outside current OSM core; reopen
  only if a concrete interoperability requirement appears.
- Whether `ict_providers[].services_consumed` should stay an
  independent reverse listing or be derived from canonical `providers`
  (does not block this analysis).

## 10. Compatibility status

**PARTIALLY COMPATIBLE / SELECTIVE COMPATIBILITY**

OSM aligns with the CSDM concepts that are useful for a small
technological service catalog. OSM is substantially smaller and
narrower than CSDM. OSM does not implement CSDM.
