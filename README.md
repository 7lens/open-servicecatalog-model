# 7lens OSM

**7lens Open Service Catalog Model**

A small, vendor-neutral, machine-readable **data model** for describing
technological services, their offerings, ownership, operational
state and third-party dependencies.

7lens OSM is maintained by [7lens](https://7lens.io). It is published
as a standalone open-source Service Catalog Model. It does not require
a particular vendor, product, or enterprise architecture method.

**Service**, in 7lens OSM, always means a **technological service**
delivered by a technology or platform organization.

7lens OSM is a data model. It is not an AI model.

---

## Why 7lens OSM exists

Two ideas sit underneath this project.

### 1. A small model that can sit with existing languages

Organizations already describe technology through several service
models, architecture models and governance frameworks. 7lens OSM is
**designed** to bring together the useful characteristics of that
landscape into one deliberately small, vendor-neutral Service Catalog
Model.

7lens OSM incorporates useful semantics from existing models where
they materially improve interoperability, governance or
machine-readability. It does **not** copy those models wholesale.
Compatibility does not mean copying. One semantic concept has one
canonical OSM parameter (OSM-M-008); frameworks map to that
parameter rather than adding a second copy.

The [initial compatibility universe](COMPATIBILITY.md) is the map
against which that goal will be validated. 7lens OSM is **designed
to be compatible** with those languages. That is not a claim that
it already is.

### 2. Prepared for a world where AI operates technology

7lens OSM is designed from the ground up for a future in which AI
manages an increasing — and eventually dominant — portion of
enterprise technology systems. That is not an afterthought.

The 7lens line that names the problem is:

> Your Corporate Surface Has Outgrown Human Governance.

When the estate is larger than human-only governance can hold,
catalog information has to be explicit enough for both people and
machines. 7lens OSM is meant to help organizations prepare for a
world where:

- AI agents increasingly operate technology
- systems need machine-readable semantics
- services need explicit ownership and relationships
- operational state needs to be represented consistently
- governance needs to be understandable by both humans and machines
- technology estates increasingly exceed the practical limits of
  human-only governance

The model should support a future in which AI agents can reason over
enterprise technological services because the underlying information
is explicit, structured, consistent, machine-readable, governed and
traceable.

That is why OSM is a **data model** for technological services — not
an AI product, and not a description of any proprietary 7lens agent
architecture.

---

## What 7lens OSM is

7lens OSM is a compact YAML catalog for describing:

- **Technology Stacks** — operational competency domains
- **Services** — stable definitions of technological capabilities
- **Service Offerings** — atomic requestable or deliverable variants
- **Characteristics** — optional generic properties on services and offerings
- **Provenance** — reusable source, evidence, verification and confidence
- **Ownership** — who is accountable for a stack or a service
- **Temporal semantics** — definition version, validity period and lifecycle
- **Operational posture** — criticality, automation, security
  and resilience evidence in the service posture record
- **Governance attributes** — optional mappings to common frameworks
- **ICT providers** — canonical third-party technology providers;
  Services and Offerings may reference them

It is designed to be read by humans and validated by machines.

## What problem it solves

Technology organizations repeatedly rebuild service catalogs in
spreadsheets, wiki pages, CMDB extensions and proprietary tools.
Those catalogs often mix business language, application inventories
and infrastructure records until nobody can answer a simple question:

> What technological services do we actually deliver, who owns them,
> and in what operational state are they?

Most catalogs fail in one of two ways:

1. They are too thin — a list of names with no ownership, offerings
   or operational signal.
2. They are too broad — an attempt to model the entire enterprise
   in one schema, which becomes slow to adopt and hard to keep true.

7lens OSM sits in between. It is opinionated about a few things and
silent about everything else.

A small common model makes it easier to:

- describe technological services consistently
- exchange service information between teams and tools
- automate validation of identifiers and references
- connect a service catalog with operational tooling
- map services to governance frameworks when needed
- improve transparency between technology teams and stakeholders
- give humans and machines the same structured picture of what is
  delivered

The purpose is community utility and interoperability.

---

## Compatibility

7lens OSM is **designed to be compatible with** a defined set of
existing service models, architecture models and
compliance/governance frameworks. That set is the initial
compatibility baseline. It is **not** a list of completed mappings
and **not** a list of regulations OSM complies with.

See [`COMPATIBILITY.md`](COMPATIBILITY.md) and the register
[`DECISIONS.md`](DECISIONS.md) (`OSM-C-001`, `OSM-C-004`, `OSM-C-005`,
`OSM-M-001`–`OSM-M-004`, `OSM-M-006`, `OSM-M-007`). Detailed model
decisions are in [`decisions/`](decisions/).

Until an analysis is accepted, an entry is **NOT ANALYZED**. TM Forum
TMF633, ITIL v5 and ServiceNow CSDM are **PARTIALLY COMPATIBLE**
(selective compatibility; OSM is not a TMF, ITIL or CSDM
implementation).

---

## Conceptual structure

7lens OSM stays inside this boundary:

```
Technology Stack
      |
      v
   Service
      |
      v
Service Offering
```

Associated records:

- Optional characteristics on services and offerings
- Optional `providers` (ICT Provider ids) on services and offerings
- Optional `provenance` on definitions and posture records
- Service posture and offering posture (`service_attributes`)
- ICT Provider register
- Governance / ownership

Two files, two cadences:

| Record | Nature | Typical cadence |
|--------|--------|-----------------|
| Catalog (`services`) | Current **definition** of what is delivered | Changes when version, validity, lifecycle, offerings, characteristics or providers change. `id` does not change. |
| Service posture (`service_attributes`) | Current operational and governance state | Changes as operations, risk and governance teams update posture |

Identifiers never change once assigned. The **definition** may evolve
(`version`, `valid_from`, `valid_to`, `lifecycle_state`). Ownership and
operational posture may change freely. Immutable identity is not an
immutable definition.

## Service vs Service Offering

A **Service** is the stable **definition** of a technological
capability (not merely a catalog listing, and not a running
instance). Examples: managed Kubernetes, object storage, identity
and access management, CI/CD.

A **Service Offering** is the atomic requestable/deliverable variant
of that service. Variants may differ in environment, location,
availability, packaging, operating model, provider, or other
meaningful characteristics — without turning each dimension into a
mandatory field.

A **Service Instance** / deployed implementation is operational
runtime context. It is **outside** the OSM core.

```
service     compute.kubernetes
  └── offering  compute.kubernetes.aws
  └── offering  compute.kubernetes.azure
```

That is the only nesting in 7lens OSM. There is no deeper tree.

### Identity

```
{stack_prefix}.{service_slug}.{offering_slug}
```

- **Service ID** = 2 segments, for example `compute.kubernetes`
- **Offering ID** = 3 segments, for example `compute.kubernetes.aws`
- Segments are lowercase, hyphen-delimited slugs

The prefix records the stack under which the service was originally
created. A service may later move to another technology stack
**without changing its ID**. IDs are permanent references; ownership
evolves. A new `version` of the same service also keeps the same ID.
`lifecycle_state` is part of that Service definition.

## Characteristics

Services and offerings may declare optional **characteristics**:
named, typed properties (value, type, allowed values, default,
cardinality, constraints, configurable). Use them instead of growing
the core schema for every property. They are not a separate catalog
entity.

## Technology Stacks

A **Technology Stack** is an operational ownership domain: the
competency that runs a group of services day to day. It is not a
financial taxonomy, an org-chart dump, or a list of servers.

Typical generic domains include:

- Compute
- Database
- Network
- Storage
- Security
- DevOps
- Automation
- Data
- Operations
- FinOps

Adopting organizations usually define between 8 and 20 stacks.
The examples in this repository are a starter set, not a required
taxonomy.

Every service has exactly one current technology stack.

## Ownership and governance

Two roles are defined in [`GOVERNANCE.md`](GOVERNANCE.md):

- **Technology Stack Owner** — accountable for the completeness and
  coherence of a stack, and for every service in that stack having a
  Service Owner.
- **Service Owner** — accountable for a technological service, its
  lifecycle, correct use, and applicable security and operational
  obligations.

The `accountable` field on a service names the Service Owner
(service-definition and overall service accountability). Use a role
title, a named individual, or a team alias according to local
convention. Posture `financial_owner` is a different concept:
financial ownership of the service.

## Service posture

[`schema/service-attributes.yaml`](schema/service-attributes.yaml)
holds **Service Posture** — how the service currently stands — not
its definition lifecycle:

- operational criticality and qualitative `resilience_tier` (not a
  substitute for offering `rto` / `rpo`)
- service-level **targets** (availability / response / resolution) —
  expected performance, not hours windows
- data classification (data handled) and security classification
  (the service itself); shared enum tokens, different subjects
- technical debt and vendor support
- `automation_coverage` (overall delivery/operation) and
  `provisioning_automation` (provisioning process)
- financial characterization (cost pool, chargeback, unit cost,
  `financial_owner` — distinct from Service `accountable`)
- offering-level RTO/RPO and resilience evidence (`rto`, `rpo`; DORA
  maps to these canonical fields)
- optional regulatory or framework mappings (not copies of canonical
  fields)
- optional provenance

Service-level fields apply to the whole service. Offering-level
fields capture differences between requestable variants. An empty
`offering_attributes` list is valid: posture is filled in over time.

## Third-party providers

ICT Provider is the canonical provider entity.
[`schema/ict-provider.yaml`](schema/ict-provider.yaml) holds provider
identity, criticality, substitutability, contract and risk fields,
and certifications.

A Service or Offering may list `providers` — ids into that register —
when a provider delivers or underpins the capability (OSM-M-006).
Use Service-level association when the provider is intrinsic to the
Service; use Offering-level association when provider choice is the
variant. Association is optional. Multiple providers are allowed.
Do not copy provider master data onto Service or Offering.
There is no separate `cloud_providers` field; a cloud provider is an
ICT Provider.

`dora_third_party_deps` on offering attributes is a DORA-oriented
listing. Whether it is a genuinely different relationship from
canonical `providers` is unresolved (**OSM-M-005**, **PROPOSED**).
Do not collapse the two fields yet.

The examples contain a **small fictional register** of well-known
public providers. They are not a recommended vendor list and not an
organization's real third-party register.

## Framework mappings

7lens OSM can carry **optional reference mappings**. Some mapping
fields already exist in the schema (for example TBM, TOGAF, ISO,
NIST, GDPR, DORA and the EU AI Act). Other models in the
[compatibility universe](COMPATIBILITY.md) have no OSM fields yet.

These mappings exist so different stakeholders can read the same
catalog in their own language. They do **not** make 7lens OSM an
implementation, certification, or legal interpretation of any of
those frameworks. If OSM already represents the concept, the
framework maps to that field (OSM-M-008).

Illustrative mappings in the examples are reference material only.
They are not legal advice, not evidence of regulatory compliance,
and not a certification of any organization or product.

## Examples

Synthetic examples live in [`examples/`](examples/):

| File | What it demonstrates |
|------|----------------------|
| `technology-stacks.yaml` | Generic operational domains and optional mappings |
| `services.yaml` | A small catalog of services, offerings and optional providers |
| `service-attributes.yaml` | Compliance and offering-level posture |
| `ict-providers.yaml` | Canonical ICT Provider register for the example catalog |

The examples are deliberately small and fictional. Replace them with
your own catalog. Do not treat them as a recommended technology
estate.

## How to adopt it

1. Read [`SPECIFICATION.md`](SPECIFICATION.md) and [`MODEL.md`](MODEL.md).
2. Copy `examples/` and replace the records with your stacks, services
   and offerings.
3. Keep IDs stable. Assign them carefully; they are immutable.
4. Populate `service_attributes` incrementally. Start with criticality
   and data classification.
5. Add ICT providers as part of vendor management, not as a one-off
   documentation exercise.
6. Run the checks in [`validation/`](validation/) in review or CI.

7lens OSM is YAML. You can store it in git, generate documentation
from it, or load it into whatever operational tooling you already use.

---

## What 7lens OSM does NOT try to model

The following are **out of scope**:

- business capabilities
- business services
- Application Services
- Service Instances / deployed implementations
- applications
- infrastructure inventory / CMDB configuration items
- Product Models
- organizational hierarchy
- geographic hierarchy
- enterprise-wide ontology
- stakeholder lenses
- enterprise decision intelligence

Consumers of a technological service are outside the scope of this
model. Adopters may join this catalog to other records in their own
systems; this repository does not define those other records.

---

## Repository layout

```
.
├── README.md
├── LICENSE
├── NOTICE
├── SPECIFICATION.md
├── GOVERNANCE.md
├── MODEL.md
├── CONTRIBUTING.md
├── COMPATIBILITY.md
├── DECISIONS.md
├── decisions/
├── schema/
│   ├── technology-stack.yaml
│   ├── service.yaml
│   ├── service-offering.yaml
│   ├── characteristic.yaml
│   ├── provenance.yaml
│   ├── service-attributes.yaml
│   └── ict-provider.yaml
├── examples/
│   ├── technology-stacks.yaml
│   ├── services.yaml
│   ├── service-attributes.yaml
│   └── ict-providers.yaml
├── compatibility/
├── compliance/
└── validation/
    ├── README.md
    ├── requirements.txt
    └── validate.py
```

## Contribution approach

Contributions are welcome when they keep 7lens OSM:

- small
- opinionated
- vendor-neutral
- focused on technological services
- understandable
- machine-readable
- extensible without copying other models wholesale

Model changes need an accepted decision in [`DECISIONS.md`](DECISIONS.md).
See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`decisions/`](decisions/).

## License

Copyright 2026 7lens Technologies S.L.

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).
