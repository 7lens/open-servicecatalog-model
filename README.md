# 7lens OSM

**7lens Open Service-Catalog Model**

> **ONE ENTERPRISE. ONE ONTOLOGY. SEVEN LENSES.**
> **SAME DATA. DIFFERENT QUESTIONS. BETTER DECISIONS.**

A small, vendor-neutral, machine-readable **canonical model** for
technological services.

OSM lets an enterprise **own** the description of its technological
services — instead of letting a vendor, platform or framework become
the canonical representation of that landscape.

It is published by [7lens](https://7lens.io) as a standalone open
model. It does not require a particular product, cloud or method.

7lens OSM is a semantic **data model**. It is not an AI model.

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



## How OSM relates to 7lens

OSM is **not** the complete 7lens ontology.

It is the canonical **technological-service** model. 7lens provides enterprise-grade capability to implement and operate OSM, and to connect it with organization and business-application models.

OSM was opened so companies can prepare IT governance for an AI-operated future — whether or not they use 7lens.

```
Enterprise technology context
        ↓
      OSM
        ↓
     7lens
        ↓
  decision perspectives
```

7lens uses OSM as a foundation for richer contextual intelligence
across:

- CIO
- CTO
- CFO
- CISO
- Automation
- AI Agents
- Operations

Those lenses are **not** part of OSM. OSM stays a small technology core that 7lens — and other systems — can build on.

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



## Start here


| If you want to…                        | Read                                                                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| Understand the idea                    | this README                                                                                |
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