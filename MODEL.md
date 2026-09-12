# Conceptual model

This document describes the 7lens Open Services Data Model as a
standalone conceptual structure. The normative field definitions are
in [`SPECIFICATION.md`](SPECIFICATION.md).

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
│      Service        │  technological capability being delivered
└──────────┬──────────┘
           │ 1 : many
           v
┌─────────────────────┐
│  Service Offering   │  atomic requestable / deliverable unit
└─────────────────────┘
```

Each service also has:

- an **accountable** Service Owner
- optional **service attributes** (health / governance posture)
- optional **offering attributes** (variant-level operational data)
- optional **ICT provider** dependencies

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

A Service is a technological capability with:

- an immutable identifier (2 segments)
- a name and description
- a Service Owner
- a current Technology Stack
- one or more Service Offerings

The catalog of services is intended to be stable. Treat it as the
identity record of what you deliver.

## Service Offering

A Service Offering is the atomic unit associated with a Service.
Offerings distinguish requestable or deliverable variants of the
same capability: different grades, hosting locations, or operating
models.

The offering identifier has 3 segments. The first two segments must
equal the parent service ID.

## Attributes

Attributes are separated from identity on purpose.

| Layer | Holds | Changes when |
|-------|--------|--------------|
| Service / offering catalog | What exists | A capability is introduced or withdrawn |
| Service attributes | Shared posture of the service | Lifecycle, criticality or classification changes |
| Offering attributes | Variant-level operations, cost, security, resilience | Day-to-day operational reality changes |

Empty offering attributes are allowed. Populate them as evidence
becomes available.

## ICT providers

An ICT provider is a third-party technology organization that
underpins one or more services. The relationship is recorded in two
directions:

- a provider lists `services_consumed`
- an offering may list `dora_third_party_deps`

Those fields are ordinary references. Using the field names does not
make a catalog a regulatory filing.

## Optional framework mappings

Stacks, services and offerings may carry mappings to TBM, TOGAF,
ISO/IEC 27001, ISO/IEC 27701, NIST CSF, GDPR, DORA and the EU AI Act.

Mappings are optional, illustrative and non-normative for those
frameworks. The Services Data Model is not an implementation of any
of them.

## What is deliberately excluded

The model stops at technological services. It does not define
business capabilities, business services, applications,
infrastructure configuration items, organization or geography,
enterprise-wide ontologies, stakeholder lenses, or decision
intelligence.

Consumers of a technological service are outside the scope of this
model.
