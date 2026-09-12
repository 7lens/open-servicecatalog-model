# 7lens Open Services Data Model

A small, vendor-neutral, machine-readable model for describing
technological services, their offerings, ownership, operational
state and third-party dependencies.

This project is intentionally focused on the **Service** domain.
It is maintained by [7lens](https://7lens.io), and it is published
as a standalone open-source model that any technology organization
can adopt without depending on a particular vendor, product, or
enterprise architecture method.

**Service**, in this repository, always means a **technological
service** delivered by a technology or platform organization.

---

## What this model is

The 7lens Open Services Data Model is a compact YAML catalog for
describing:

- **Technology Stacks** — operational competency domains
- **Services** — technological capabilities the organization delivers
- **Service Offerings** — atomic requestable or deliverable variants
- **Ownership** — who is accountable for a stack or a service
- **Operational state** — lifecycle, criticality, automation, security
  and resilience posture
- **Governance attributes** — optional mappings to common frameworks
- **ICT providers** — third-party technology dependencies

It is designed to be read by humans and validated by machines.

## Why this exists

Technology organizations repeatedly rebuild service catalogs in
spreadsheets, wiki pages, CMDB extensions and proprietary tools.
Those catalogs often mix business language, application inventories
and infrastructure records until nobody can answer a simple question:

> What technological services do we actually deliver, who owns them,
> and in what operational state are they?

A small common model makes it easier to:

- describe technological services consistently
- exchange service information between teams and tools
- automate validation of identifiers and references
- connect a service catalog with operational tooling
- map services to governance frameworks when needed
- improve transparency between technology teams and stakeholders

The purpose is community utility and interoperability.

## What problem it solves

Most catalogs fail in one of two ways:

1. They are too thin — a list of names with no ownership, offerings
   or operational signal.
2. They are too broad — an attempt to model the entire enterprise
   in one schema, which becomes slow to adopt and hard to keep true.

This model sits in between. It is opinionated about a few things
and silent about everything else.

---

## Conceptual structure

The public model stays inside this boundary:

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

That is the only nesting in the model. There is no deeper tree.

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

The model can carry **optional reference mappings** to established
frameworks, including:

- TBM
- TOGAF
- ISO/IEC 27001
- ISO/IEC 27701
- NIST CSF
- GDPR
- DORA
- EU AI Act

These mappings exist so different stakeholders can read the same
catalog in their own language. They do **not** make this model an
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

The model is YAML. You can store it in git, generate documentation
from it, or load it into whatever operational tooling you already use.

---

## What this model does NOT try to model

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
└── validation/
    ├── README.md
    ├── requirements.txt
    └── validate.py
```

## Contribution approach

Contributions are welcome when they keep the model:

- small
- opinionated
- vendor-neutral
- focused on technological services
- understandable
- machine-readable

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Copyright 2026 7lens Technologies S.L.

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).
