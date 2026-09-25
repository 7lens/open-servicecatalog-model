# 7lens OSM

**7lens Open Service-Catalog Model**

> **ONE ENTERPRISE. ONE ONTOLOGY. SEVEN LENSES.**
> **SAME DATA. DIFFERENT QUESTIONS. BETTER DECISIONS.**

OSM is a small, vendor-neutral, machine-readable **canonical data
model** for technological services. It is not an AI model. It does
not require a particular product, cloud, or method.

---

## What it is, why it matters, how to start

**What.** OSM is the place where your organization records *what a
technological service is* — once, in its own vocabulary. Stacks,
Services, and Offerings are the canonical core.

**Why.** You own the **semantics**. That is the hard asset. Owned
semantics are what let you grow a **lock-in-free ontology**: your
enterprise picture of technological services, mapped to clouds, ITSM,
GRC, and frameworks, instead of any of those becoming the source of
truth.

In an AI-driven organization that is not optional. If you do not own
the semantics — and make them available to the whole enterprise —
every team, tool, and agent keeps translating between incompatible
pictures.

**Who.** The ideal first user is a Principal Manager, Platform Lead,
Head of Architecture, or Enterprise Architect. It can be **anyone**
who sees the problem: not owning the semantics, and not making them
available organization-wide, is a strategic failure in an AI future.

**How.** Same path if you read this file or ask a coding assistant
“how do I use this?”. Follow `[ONBOARDING.md](ONBOARDING.md)`. The
CLI `osm-scaffold` is one way to run that conversation; a coding
assistant must not skip it.

Phase 1 is a **draft** of Technology Stacks and Services you are
comfortable starting with. Your model lives in
`[servicecatalog/](servicecatalog/)`. After every change you should
see a simple board: this is what we currently have. Pause at any
time; continue later from the same draft.

1. What capabilities do you operate? (Technology Stacks — competencies,
   not vendor towers.)
2. Which regimes apply as locators, not claims? (compliance mappings.)
3. Stop when the draft is honest enough to start.

**Scope.** OSM is a **model definition**, and only for technological
**services**. It is not a platform. You own the semantics, and you
build what sits around the model: where the catalog is stored, how
other sources are reconciled into it, and how people and agents read
and write it.

**Later, as a platform.** You do not need a product to start. If you
later want this operated as a platform — the service model plus the
other ontology axes an AIOps estate needs (**organization**,
**applications**, **contracts**, **processes**) — that product is
[7lens](https://7lens.io).

```bash
python3 -m pip install -r tools/requirements.txt
python3 -m tools.osm_scaffold.cli
python3 -m tools.osm_scaffold.cli --status
python3 -m tools.osm_scaffold.cli --resume
python3 -m tools.osm_lint.cli --catalog servicecatalog
```

Published by [7lens](https://7lens.io) as a standalone open model.

---

## Why OSM exists

Technology organizations already speak several languages: ITIL,
TM Forum, ServiceNow CSDM, TOGAF, ArchiMate, TBM, and a set of
security, privacy and operational-resilience frameworks.

Those languages are useful. None of them should *own* the enterprise’s source of truth for technological services.

OSM provides a deliberately small **canonical core, that could scale into a full enterprise semantics and ontology**:

- what technological services you deliver
- who is accountable for them
- which variants can be requested
- which third parties they depend on
- how they currently stand
- why that information can be trusted

More detailed models sit **alongside** OSM. They do not compete
with it.


| Specialized model                                      | Typical role beside OSM                         |
| ------------------------------------------------------ | ----------------------------------------------- |
| ITIL                                                   | Service management and operational excellence   |
| TM Forum                                               | Richer catalog, commercial and service concepts |
| ServiceNow CSDM                                        | ServiceNow-oriented service and CMDB modeling   |
| TOGAF / ArchiMate                                      | Enterprise architecture                         |
| TBM                                                    | Technology financial management                 |
| ISO 27001 / ISO 27701, NIST CSF, GDPR, DORA, EU AI Act | Security, privacy, resilience and AI governance |


**OSM holds each concept once. Frameworks map onto those concepts. They do not get a second copy of the same fact under another name.**

See `[models/](models/)` for service, catalog and architecture frameworks. See `[compliance/](compliance/)` for regulatory, security, privacy and control mappings.

---



## Why this matters for an AI-driven enterprise

Enterprise technology is increasingly heterogeneous, automated, API-driven and operated by machines — including AI agents.

Agents need **consistent, machine-readable semantics**. If every organization, vendor and framework describes technology differently, every automation has to translate between incompatible pictures.

OSM is a small canonical semantic layer so an organization can:

1. Own its technology model.
2. Connect existing sources and frameworks — or extend OSM internally.
3. Expose the same semantics to automation and AI.
4. Layer specialized frameworks on top without replacing the core.

OSM is the structured technology context that people and AI systems can consume. It is not an AI product and not a description of any proprietary 7lens agent architecture.

> Your Corporate Surface Has Outgrown Human Governance.

When the estate is larger than human-only governance can hold, the catalog has to be explicit enough for both people and machines.

---



## Model, or platform

OSM is the open model for technological **services**. You implement
and operate it yourself. The catalog you write is your service
semantics. A running platform — storage, reconciliation, and an API —
is work you still have to build.

[7lens](https://7lens.io) is a separate **platform**. It operates the
service model and adds ontology beyond services: organization,
applications, contracts, and processes. Those axes are how an AIOps
estate stays one picture. They are not part of OSM. Details are on
the product site, not in this repository.

Start with OSM either way. Choosing the model does not require the
platform.

---



## The model

```
Technology Stack
      ↓
   Service
      ↓
Service Offering
```


| Concept                | Meaning                                              |
| ---------------------- | ---------------------------------------------------- |
| **Technology Stack**   | Operational competency that runs a group of services |
| **Service**            | Stable **definition** of a technological service     |
| **Service Offering**   | Atomic requestable / deliverable variant             |
| **Characteristics**    | Optional typed properties on a service or offering   |
| **ICT Provider**       | Canonical third-party technology provider            |
| **Service Posture**    | How the service currently stands                     |
| **Offering Posture**   | Variant-level operational state                      |
| **Provenance**         | Why a fact can be trusted, and where it came from    |
| **Framework mappings** | Optional translations into other languages           |


Four layers, kept distinct:

```
SERVICE DEFINITION     what the service is
POSTURE                current assessed state
PROVENANCE             why the information can be trusted
FRAMEWORK MAPPINGS     how OSM relates to other models
```

External context — applications, CMDB, organization, geography, contracts, full SLA management — stays **outside** OSM.

**OSM is:**

- a vendor-neutral technological service model
- machine-readable
- intentionally small
- designed for interoperability
- suitable as a canonical technology-service layer

**OSM is not:**

- a CMDB
- a complete enterprise ontology
- a DORA register of information
- a GDPR Record of Processing Activities
- a ServiceNow CSDM implementation
- an ITIL implementation
- a full TM Forum model
- an NIST implementation model
- an ISO control system
- an EU AI Act technical-file system

The conceptual explanation is in `[MODEL.md](MODEL.md)`.
The exact field model is in `[SPECIFICATION.md](SPECIFICATION.md)`.
Compatibility mappings (current versions, **MAPPED** / **PARTIAL**,
not certification) are in `[models/](models/)` and
`[compliance/](compliance/)`.

---



## How to get started

OSM is the model. The catalog you commit is the source of truth.

Start by **creating that catalog**, not by reading the whole
specification. The tools in `[tools/](tools/)` sit on OSM 1.3.0 YAML.
They do not replace the model, and they do not invent posture or
compliance.

Install once from the repository root:

```bash
python3 -m pip install -r tools/requirements.txt
python3 -m pip install -r validation/requirements.txt
```

### 1. Create the canonical catalog — `osm-scaffold`

**Ideal user:** Principal Manager, Platform Lead, Head of Architecture,
or Enterprise Architect. **Anyone** who sees that not owning enterprise
semantics — and not making them available organization-wide — is a
problem in an AI future can start.

This is the onboarding path. The protocol is
`[ONBOARDING.md](ONBOARDING.md)`: what OSM is (you own the semantics;
that is how you grow a lock-in-free ontology), then **your technology
stacks**, then **compliance locators**, then a draft you are comfortable
starting with. Same conversation if a coding assistant is doing the
implementation.

Your model lives in `[servicecatalog/](servicecatalog/)`. Pause
(`:pause`) and continue (`--resume`) from that folder. On continue you
get a summary of what is already configured, where it is stored, and
how to add stacks, add services, or pull more from the golden examples.

`osm-scaffold` refuses the usual first mistakes (product-named Services
such as “EKS”, request-catalog Offerings such as password-reset, vendor
towers such as a stack called AWS).

```bash
python3 -m tools.osm_scaffold.cli
python3 -m tools.osm_scaffold.cli --status
python3 -m tools.osm_scaffold.cli --resume
python3 validation/validate.py --catalog servicecatalog
python3 -m tools.osm_lint.cli --catalog servicecatalog
```

At any prompt: `:view` (the board) or `:pause` (checkpoint and exit).
A one-service non-interactive path remains available with `--config`
for automation; the onboarding conversation is how humans (and coding
assistants) start.

Unknown facts stay unset. That is correct. A small honest catalog
beats a complete-looking fiction.

Worked catalogs, if you want to read before you write:
`[examples/reference-enterprise/golden-example/](examples/reference-enterprise/golden-example/)`
(onboarded predecessor) and
`[examples/reference-estate/golden-example/](examples/reference-estate/golden-example/)`
(public-provider estate). Full CLI:
`[tools/README.md](tools/README.md)`.

### 2. Keep the catalog semantically true — `osm-lint`

**Persona:** Enterprise Architect / Principal Platform Architect.

`validation/validate.py` checks shape and references. `osm-lint`
catches catalogs that *validate* while still being wrong: S3 as a
Service, MFA as an Offering, Entra mixed with AWS IAM, a vendor SLA
copied into `availability_target`, a DPA flagged without evidence.

```bash
python3 -m tools.osm_lint.cli --catalog servicecatalog
python3 -m tools.osm_lint.cli --catalog examples/reference-estate/golden-example
```

Exit `0` is clean, `1` is semantic errors, `2` is warnings only.

### 3. Ask governance questions — `osm-query`

**Persona:** IT Governance / Compliance & Security Officer
(and the architect who must answer them).

Once you have a catalog, do not grep YAML for “where is AWS
concentration?” or “which critical services have no RTO?”. These
reports are locators, not certification. OSM is not a DORA register,
an ISO SoA, or a NIST profile.

```bash
python3 -m tools.osm_query.cli gaps --catalog servicecatalog
python3 -m tools.osm_query.cli providers --catalog servicecatalog
python3 -m tools.osm_query.cli compliance --framework dora --catalog servicecatalog
```

### 4. Give machines bounded context — `osm-context`

**Persona:** AI Agent Builder / Platform Automation Engineer.

Agents need the same catalog, not a CMDB dump. `export-context`
writes one deterministic JSON file. Unassessed operational fields
are `"UNKNOWN"`. Framework mapping fields are stripped so they
cannot be over-read as compliance.

```bash
python3 -m tools.osm_query.cli export-context \
  --catalog servicecatalog \
  --output osm-agent-context.json
```

### Who uses what

| Persona | Job to be done | Tool |
| ------- | -------------- | ---- |
| Anyone who sees the semantics problem (ideal: Principal Manager / Platform Lead / Architecture) | Establish the canonical OSM catalog — own the semantics | **`osm-scaffold`** |
| Enterprise / Platform Architect | Stop a valid YAML file from becoming a false catalog | **`osm-lint`** |
| Governance / CISO | Concentration, owner gaps, resilience locators — without claiming compliance | **`osm-query`** |
| Agent / automation engineer | Bounded, machine-readable operational context | **`osm-context`** |

Command reference: `[tools/README.md](tools/README.md)`.

---



## Read next


| If you want to…                        | Read                                                                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| Understand the idea                    | this README                                                                                |
| Get started with a catalog             | `[ONBOARDING.md](ONBOARDING.md)`, `[servicecatalog/](servicecatalog/)`, `[tools/](tools/)` |
| Understand the model                   | `[MODEL.md](MODEL.md)`                                                                     |
| Implement or validate                  | `[SPECIFICATION.md](SPECIFICATION.md)`, `[schema/](schema/)`, `[validation/](validation/)` |
| Inspect a catalog                      | `[examples/](examples/)` — start with `[examples/reference-enterprise/](examples/reference-enterprise/)` |
| See how OSM sits with other frameworks | `[models/](models/)`                                                                       |
| See regulatory and control mappings    | `[compliance/](compliance/)`                                                               |
| See ownership roles                    | `[GOVERNANCE.md](GOVERNANCE.md)`                                                           |
| Contribute                             | `[CONTRIBUTING.md](CONTRIBUTING.md)`                                                       |




### Try the examples

```bash
python3 -m pip install -r validation/requirements.txt
python3 validation/validate.py
python3 validation/validate.py --catalog examples/reference-enterprise
python3 validation/validate.py --catalog examples/reference-enterprise/golden-example
python3 validation/validate.py --catalog examples/reference-estate
python3 validation/validate.py --catalog examples/reference-estate/golden-example
```

Basic examples under `examples/catalog/` are synthetic schema tutorials.
`examples/reference-enterprise/` is a real predecessor catalog onboarded
to OSM. `examples/reference-estate/` is a researched public-provider
estate. None is a certification or a vendor recommendation.

---



## License

Copyright 2026 7lens Technologies S.L.

Licensed under the Apache License, Version 2.0. See `[LICENSE](LICENSE)`.