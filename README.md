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

That is a design goal. It is not a claim that OSM is already the
best of those models, or that it is already compatible with them.
The [initial compatibility universe](COMPATIBILITY.md) is the map
against which that goal will be validated.

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
- **Services** — technological capabilities the organization delivers
- **Service Offerings** — atomic requestable or deliverable variants
- **Ownership** — who is accountable for a stack or a service
- **Operational state** — lifecycle, criticality, automation, security
  and resilience posture
- **Governance attributes** — optional mappings to common frameworks
- **ICT providers** — third-party technology dependencies

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

See [`COMPATIBILITY.md`](COMPATIBILITY.md) and decision **OSM-C-001**
in [`DECISIONS.md`](DECISIONS.md).

Until an analysis is accepted, every entry in that universe is
**NOT ANALYZED**.

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

- Service attributes and offering attributes
- ICT provider relationships
- Governance / ownership

Two files, two cadences:

| Record | Nature | Typical cadence |
|--------|--------|-----------------|
| Catalog (`services`) | Stable identity of what is delivered | Changes when a service or offering is introduced, renamed for humans, or withdrawn |
| Health record (`service_attributes`) | Current operational and compliance state | Changes as operations, risk and governance teams update posture |

Identifiers never change once assigned. Ownership and operational
state may change freely.

## Service vs Service Offering

A **Service** is a technological capability offered by the technology
organization. Examples: managed Kubernetes, object storage, identity
and access management, CI/CD.

A **Service Offering** is the atomic unit a consumer can request or
be given. One service may have several offerings: a shared cluster
and a dedicated cluster; a standard database and a highly available
database; an AWS-hosted variant and an Azure-hosted variant.

```
service     compute.kubernetes
  └── offering  compute.kubernetes.shared-cluster
  └── offering  compute.kubernetes.dedicated-cluster
```

That is the only nesting in 7lens OSM. There is no deeper tree.

### Identity

```
{stack_prefix}.{service_slug}.{offering_slug}
```

- **Service ID** = 2 segments, for example `compute.kubernetes`
- **Offering ID** = 3 segments, for example `compute.kubernetes.shared-cluster`
- Segments are lowercase, hyphen-delimited slugs

The prefix records the stack under which the service was originally
created. A service may later move to another technology stack
**without changing its ID**. IDs are permanent references; ownership
evolves.

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

The `accountable` field on a service names the Service Owner. Use a
role title, a named individual, or a team alias according to local
convention.

## Operational attributes

[`schema/service-attributes.yaml`](schema/service-attributes.yaml)
describes the living health record of a service:

- lifecycle state
- technical debt
- operational criticality
- data classification
- vendor support status
- automation vs manual operation
- security review and asset coverage
- operational resilience (for example RTO/RPO)
- optional regulatory or framework fields

Service-level fields apply to the whole service. Offering-level
fields capture differences between requestable variants. An empty
`offering_attributes` list is valid: attributes are filled in over
time.

## Third-party providers

Technological services often depend on external ICT providers.
[`schema/ict-provider.yaml`](schema/ict-provider.yaml) describes
provider identity, criticality, substitutability, contract and risk
fields, certifications, and the services consumed from that provider.

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
those frameworks.

Illustrative mappings in the examples are reference material only.
They are not legal advice, not evidence of regulatory compliance,
and not a certification of any organization or product.

## Examples

Synthetic examples live in [`examples/`](examples/):

| File | What it demonstrates |
|------|----------------------|
| `technology-stacks.yaml` | Generic operational domains and optional mappings |
| `services.yaml` | A small catalog of services and offerings |
| `service-attributes.yaml` | Lifecycle, compliance and offering-level posture |
| `ict-providers.yaml` | Third-party dependencies for the example catalog |

The examples are deliberately small and fictional. Replace them with
your own catalog. Do not treat them as a recommended technology
estate.

## How to adopt it

1. Read [`SPECIFICATION.md`](SPECIFICATION.md) and [`MODEL.md`](MODEL.md).
2. Copy `examples/` and replace the records with your stacks, services
   and offerings.
3. Keep IDs stable. Assign them carefully; they are immutable.
4. Populate `service_attributes` incrementally. Start with lifecycle
   and criticality.
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
- applications
- infrastructure inventory / CMDB configuration items
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
├── schema/
│   ├── technology-stack.yaml
│   ├── service.yaml
│   ├── service-offering.yaml
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

Model changes need an accepted decision in [`DECISIONS.md`](DECISIONS.md).
See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Copyright 2026 7lens Technologies S.L.

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).
