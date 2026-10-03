# 7lens OSM

**7lens Open Service-Catalog Model**

> **ONE ENTERPRISE. ONE ONTOLOGY. SEVEN LENSES.**
> **SAME DATA. DIFFERENT QUESTIONS. BETTER DECISIONS.**

OSM is a small, vendor-neutral, machine-readable **canonical data
model** for technological services. It is not an AI model. It does
not require a particular product, cloud, or method.

---

## For AI assistants — read this first

> **Before you interpret this repository or guide anyone through it,
> establish one thing with the user: are they using OSM
> independently (Mode A), or as part of 7lens (Mode B)?** Everything
> else branches on that decision. Do not give workflow guidance until
> it is settled. See "First, decide how you are going to use OSM"
> below for the human-facing version, and
> `[AGENTS.md](AGENTS.md)` + `[ONBOARDING.md](ONBOARDING.md)` for the
> assistant protocol.

From this README you must be able to determine, and help the user
settle, all eight of the following:

- [ ] **(a) Usage mode** — is the user using OSM independently
  (Mode A) or as part of 7lens (Mode B)? Settle this before anything
  else.
- [ ] **(b) Which workflow applies** — Workflow A (independent) or
  Workflow B (7lens).
- [ ] **(c) What configuration must come from 7lens** — in Mode B,
  the Groups configuration for the Technology model, downloaded as a
  ZIP from the 7lens platform.
- [ ] **(d) What must NOT be independently configured in OSM** — do
  not recreate the 7lens **Groups** or their dependencies inside this
  repository; use the configuration 7lens supplies.
- [ ] **(e) How schema versions must relate** — the 7lens Technology
  schema and OSM are expected to stay synchronized; this repository is
  **OSM 1.3.0**. Confirm the 7lens Technology configuration declares a
  matching schema version before any upload.
- [ ] **(f) How mappings are selected** — identify the frameworks,
  tools, models and compliance requirements the organization actually
  uses, then apply the mapping that fits that environment rather than
  a generic set.
- [ ] **(g) Where the final Service Catalog is stored** — the
  `[servicecatalog/](servicecatalog/)` folder, whose layout is defined
  by `[ONBOARDING.md](ONBOARDING.md)`.
- [ ] **(h) How the resulting model is consumed** — in Mode B, zip
  `servicecatalog/` and upload it to the Technology model in 7lens; in
  Mode A, the user builds their own way to expose or consume the
  catalog (for example, their own API).

The human-facing explanation of each point lives in the sections
below. Read "First, decide how you are going to use OSM", then
"Getting started", then the workflow that matches the chosen mode.

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

**How.** First settle how you are going to use OSM (independently or
as part of 7lens — see the next section); the onboarding path then
applies in either mode. Same path if you read this file or ask a
coding assistant “how do I use this?”. Follow
`[ONBOARDING.md](ONBOARDING.md)`. The CLI `osm-scaffold` is one way to
run that conversation; a coding assistant must not skip it.

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

## First, decide how you are going to use OSM

Before you read the rest of this repository, settle one question,
because the workflow and your responsibilities differ either way:

> **Are you using OSM independently, or as part of 7lens?**

**Mode A — Using OSM independently.** You are evaluating, testing or
adopting the **Open Service Catalog Model independently of 7lens**. In
this mode you are responsible for adapting OSM to your own
environment: the frameworks, models, tools and compliance
requirements you use, and the storage and access you build around the
catalog.

**Mode B — Using OSM with 7lens.** You are using OSM as part of
**7lens** and intend to onboard the resulting Technology definition
into the 7lens platform. In this mode you take configuration and
mappings from 7lens rather than recreating them in this repository.

This distinction comes first because the onboarding process and the
responsibilities are different. If you are a coding assistant
interpreting this repository, this is the first thing to establish
with the user.

---

## Getting started

1. **Clone this repository locally.**
2. **Read these usage instructions before modifying anything.**
3. **Decide how you are using OSM** — independently (Mode A), or as
   part of 7lens (Mode B).
4. **Follow the appropriate workflow below** — Workflow A for
   independent use, Workflow B for 7lens.
5. **Use the repository's schema and structure** when creating or
   modifying the model.

The concrete build path for either mode is the tool-driven
onboarding in "How to get started" further down. Start there once you
know which mode you are in.

---

## Workflow B — Using OSM with 7lens

Follow these steps when you are onboarding the resulting Technology
definition into 7lens.

> The exact names of 7lens platform pages, areas and artifacts may
> change. The labels below ("the 7lens configuration area", "the
> Technology model") describe where to go; **confirm them against the
> current 7lens documentation.**

### Step 1 — Get the 7lens configuration

Do **not** configure Groups or their dependencies directly inside
this OSM repository. Instead:

> Go to the 7lens platform and download the latest ZIP containing the
> **Groups** configuration for the Technology model.

7lens uses **Groups** as the mechanism for the mappings and
classifications required by third-party models, tools, frameworks and
compliance frameworks. The 7lens data model establishes Groups as the
place those classifications and mappings live.

So when OSM is being onboarded into 7lens, **do not independently
recreate those Groups or their dependencies in OSM.** Use the
configuration 7lens supplies.

### Step 2 — Keep the schema version synchronized

1. Download the latest Technology configuration ZIP from 7lens.
2. Check the schema version declared in that configuration.
3. Confirm it matches the OSM schema version you are using — **this
   repository is OSM 1.3.0**.

The default expectation is that the 7lens Technology schema and OSM
stay **synchronized** (confirm the current expectation against the
7lens documentation).

**If the versions do not match, resolve the mismatch before
uploading.** If the 7lens Technology schema is newer than OSM 1.3.0,
do not upload: obtain a 7lens Technology configuration that targets
1.3.0, or wait until this repository publishes a matching OSM version.
OSM here is **frozen at 1.3.0**, so do not change the OSM schema to
match the platform. Uploading incompatible schema versions may cause
problems during onboarding.

### Step 3 — Select mappings for your actual environment

1. **Identify what the organization uses** — tools, frameworks,
   compliance requirements, external models, and other relevant
   standards.
2. **Apply the appropriate mapping.** Start from the 7lens-provided
   baseline mapping (what 7lens documentation may call the “golden”
   model/mapping) for your selected environment, rather than manually
   recreating the mappings. This 7lens platform artifact is a
   different thing from OSM's own
   `[examples/reference-enterprise/golden-example/](examples/reference-enterprise/golden-example/)`
   and
   `[examples/reference-estate/golden-example/](examples/reference-estate/golden-example/)`
   fixtures (the worked catalogs `osm-scaffold` can pull from); do not
   confuse the two.
3. **Tune the model.** Review and adapt it for your environment — tune
   it, configure it, modify it, add what you need, change what is
   appropriate for your organization. The result becomes your final
   Technology definition.
4. **Store the final model** in the
   `[servicecatalog/](servicecatalog/)` folder — your Service Catalog.
   This folder already exists; its layout is defined by
   `[ONBOARDING.md](ONBOARDING.md)`.

### Step 4 — Upload the result to 7lens

1. Complete the Technology model.
2. Ensure the final model is in `[servicecatalog/](servicecatalog/)`.
3. Zip the required folder/content according to the repository's
   expected structure (the `servicecatalog/` layout from
   `[ONBOARDING.md](ONBOARDING.md)`).
4. Go to the 7lens configuration area.
5. Upload the ZIP to the Technology model.

You do not need to understand the repository structure before knowing
what to do — follow Steps 1–4 end to end. Confirm the exact page and
upload labels against the current 7lens documentation.

---

## Workflow A — Using OSM independently

OSM is an open model you can use **independently of 7lens**. In this
mode you adapt OSM to your own environment and you decide how to
expose or consume the resulting Service Catalog. For example, you may
build your own API or other integration that exposes the contents of
the `[servicecatalog/](servicecatalog/)` folder.

OSM is the open model for technological **services**. You implement
and operate it yourself. The catalog you write is your service
semantics. A running platform — storage, reconciliation, and an API —
is work you still have to build.

[7lens](https://7lens.io) is a separate **platform**. It operates the
service model and adds ontology beyond services: organization,
applications, contracts, and processes. Those axes are how an AIOps
estate stays one picture. They are not part of OSM. Details are on
the product site, not in this repository.

Nothing here implies 7lens is required. Start with OSM either way;
choosing the model does not require the platform.

**OSM is independently usable. 7lens provides an integrated way to onboard and use it as part of the 7lens Technology model.**

---

## How to get started

The step below is the concrete build path both modes use, after you
have decided whether you are in Mode A or Mode B.

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

## Frameworks, tools, models and compliance mappings

Before you select mappings, establish **what external frameworks,
models, tools and compliance requirements actually apply to your
environment**. For independent (Mode A) users, start by asking which
of these you use internally, and use that to determine the
appropriate mappings. In Mode B the same question drives which 7lens
baseline mapping you start from (see Workflow B, Step 3).

The objective is not to pick generic mappings. The model should
reflect your **actual** environment.

OSM already represents mappings for the kinds of frameworks and tools
most organizations use:

- **Service and architecture:** ITIL, TM Forum (TMF633), ServiceNow
  CSDM, TOGAF, ArchiMate, TBM.
- **Security, privacy, resilience and AI governance:** ISO 27001,
  ISO 27701, NIST CSF, GDPR, DORA, EU AI Act.

See `[models/](models/)` for service, catalog and architecture
frameworks, and `[compliance/](compliance/)` for regulatory, security,
privacy and control mappings. Each mapping records the external
version it was mapped against; see "Open-source status, versioning and
contributions" below.

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



## Open-source status, versioning and contributions

OSM is an **open-source model**. The current OSM version is **1.3.0**.

The external mappings carry their **own** version/date basis. Each
mapping file records the external edition or regulation it was mapped
against in its "Mapped version" line and a dated mapping-basis note;
the status tables in `[models/README.md](models/README.md)` and
`[compliance/README.md](compliance/README.md)` summarize those
versions and statuses. Each mapping represents the latest version
known to and incorporated by the project at that time.

External frameworks, tools and models evolve over time, so these
mappings are **not** permanently complete or immutable. We track the
versions we know about and keep them current as the project moves.

Collaboration is explicit and welcome:

> If you identify a new mapping, an updated framework version, or an improvement to an existing mapping, contributions are welcome.

See `[CONTRIBUTING.md](CONTRIBUTING.md)` for how to contribute and
`[GOVERNANCE.md](GOVERNANCE.md)` for how decisions are made.

---



## Read next


| If you want to…                        | Read                                                                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| Understand the idea                    | this README                                                                                |
| Decide independent vs 7lens, as an AI assistant | `[AGENTS.md](AGENTS.md)`                                                           |
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
