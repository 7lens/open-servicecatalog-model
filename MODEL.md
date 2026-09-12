# Conceptual model

This document describes **7lens OSM** (7lens Open Service Catalog
Model) as a standalone conceptual structure. The normative field
definitions are in [`SPECIFICATION.md`](SPECIFICATION.md). Accepted
model decisions are indexed in [`DECISIONS.md`](DECISIONS.md) and
detailed under [`decisions/`](decisions/).

**OSM-M-007** (Complete Service Definition) is **PROPOSED**. It
distinguishes Service Definition, Service Posture and External
Context. That architecture is recorded; this file still describes
the **currently implemented** model. Current names `service_attributes`
/ `offering_attributes` (health record) correspond to what OSM-M-007
calls Service Posture. They have not been renamed here.

## Purpose

The model describes **technological services**: what a technology or
platform organization delivers, who operates those deliveries, the
current operational state, and which third parties the deliveries
depend on.

It does not describe the rest of an enterprise.

## Core entities

```
┌─────────────────────┐
│  Technology Stack   │  operational competency / ownership domain
└──────────┬──────────┘
           │ 1 : many
           v
┌─────────────────────┐
│      Service        │  stable definition of a technological service
└──────────┬──────────┘
           │ 1 : many
           v
┌─────────────────────┐
│  Service Offering   │  atomic requestable / deliverable unit
└─────────────────────┘
```

Each service also has:

- an **accountable** Service Owner
- **version**, **validity period** and **lifecycle_state**
- optional **characteristics** (generic machine-readable properties)
- optional **providers** (ICT Provider ids; OSM-M-006)
- optional **service attributes** (health / governance posture)
- optional **offering attributes** (variant-level operational data)

## Technology Stack

A Technology Stack is a stable operational domain. It answers
"which competency runs this group of services?"

Stacks are not:

- cost centers (finance may *map* to them)
- org-chart boxes that must mirror HR structure
- infrastructure inventories

A service belongs to exactly one current stack. The stack on a
service may change; the service ID does not.

## Service

A Service is the **stable definition** of a technological capability
(OSM-M-003). It is not only a catalog row, not an availability
record, and not a running instance. OSM does not add a separate
ServiceSpecification entity; the Service *is* that definition.

A Service has:

- an immutable identifier (2 segments)
- a name and description
- a Service Owner
- a current Technology Stack
- a definition `version`
- a validity window (`valid_from`, optional `valid_to`)
- a `lifecycle_state`
- one or more Service Offerings
- optional characteristics
- optional `providers` (ICT Provider ids)

**Immutable identity ≠ immutable definition** (OSM-M-002). The `id`
never changes. The definition (name, description, lifecycle, offerings,
characteristics, providers, version, validity) may change. One catalog
record exists per service `id`; that record is the current definition.

OSM Service is the canonical **definition**. A deployed Service
Instance is outside the OSM core (OSM-C-005).

## Service Offering

A Service Offering is the canonical requestable/deliverable **variant**
of a Service. It may differ in environment, location, availability,
packaging, operating model, provider, or other meaningful
characteristics. Do not hard-code every dimension as a core field;
use Characteristics (OSM-M-001) and optional `providers` (OSM-M-006).

The offering identifier has 3 segments. The first two segments must
equal the parent service ID. Offerings belong to the parent Service
definition and do not carry a separate version or validity window.

## Characteristics

Services and Service Offerings may declare nested **characteristics**
(OSM-M-001): named, typed properties with optional value, defaults,
allowed values, cardinality, constraints and a configurable flag.

Characteristics are a reuse of one small structure, not a new catalog
entity and not a TM Forum characteristic model.

## Attributes

Attributes are separated from identity on purpose.

| Layer | Holds | Changes when |
|-------|--------|--------------|
| Service / offering catalog | The **definition** of what is delivered, including `lifecycle_state` | Definition version, validity, lifecycle, offerings or characteristics change. `id` does not. |
| Service attributes | Shared operational / compliance posture | Criticality, classification, automation, resilience evidence change |
| Offering attributes | Variant-level operations, cost, security, resilience | Day-to-day operational reality changes |

Empty offering attributes are allowed. Populate them as evidence
becomes available.

## ICT providers

An ICT Provider is the canonical record of a third-party technology
organization. Service and Offering point at it by id:

```
Service / Offering  →  providers[]  →  ICT Provider
```

Use Service-level `providers` when the provider is intrinsic to the
capability (for example Enterprise DNS → Infoblox). Use Offering-level
`providers` when provider choice distinguishes the variant (for
example Kubernetes AWS vs Azure). Association is optional. Multiple
ids are allowed. Do not copy provider master data onto Service or
Offering.

Separate, existing fields:

- `dora_third_party_deps` on offering attributes — DORA-oriented
  third-party listing, not the canonical provider association
- `services_consumed` on ICT Provider — reverse list of service ids
  in the vendor register

`providers` is not a generic Service → Service relationship.

Those fields are ordinary references. Using DORA-named fields does not
make a catalog a regulatory filing.

## Optional framework mappings

Stacks, services and offerings may carry mappings to TBM, TOGAF,
ISO/IEC 27001, ISO/IEC 27701, NIST CSF, GDPR, DORA and the EU AI Act.

Mappings are optional, illustrative and non-normative for those
frameworks. 7lens OSM is not an implementation of any of them.
Compatibility does not mean copying (OSM-M-004).
See [`COMPATIBILITY.md`](COMPATIBILITY.md).

## What is deliberately excluded

The model stops at technological services. It does not define
business capabilities, business services, digital products,
business outcomes, value streams, applications, Application Services,
Service Instances, infrastructure configuration items, Product Models,
organization or geography, enterprise-wide ontologies, stakeholder
lenses, decision intelligence, detailed service-level / SLA objects,
or first-class Service → Service relationships.

Service → Service relationships are deliberately outside the
**current** OSM core (OSM-C-004, OSM-C-005), not a permanent rejection.

Consumers of a technological service are outside the scope of this
model.
