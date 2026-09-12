# OSM-M-007 — Complete Service Definition

**Status:** ACCEPTED  
**Date:** 2026-09-12  
**Type:** Model  
**Scope:** Core OSM semantic model

> **Repository record.** This file is the canonical architectural
> document for OSM-M-007. Schema, examples and validation implement
> it. See the register: [`DECISIONS.md`](../DECISIONS.md).
>
> OSM-M-008 (One Concept, One Canonical Parameter) applies to this
> implementation. Framework-specific information is expressed through
> mappings when the underlying concept is already represented
> canonically. Canonical resilience and provider fields are `rto`,
> `rpo`, and `providers`. `dora_rto`, `dora_rpo`,
> `dora_third_party_deps`, `cloud_providers`, `services_consumed`,
> and ICT Provider `criticality` are not OSM fields (OSM-M-008,
> OSM-M-009, OSM-M-010).

---

## 1. Decision

7lens OSM defines a **Complete Service Definition** as the minimum set of information required to unambiguously describe a technological service as a deliverable capability, its accountability, its available variants, its delivery characteristics, its expected service levels, its technology/provider context, and the governance characteristics necessary to understand and operate that service.

A complete definition must be rich enough to support:

- human understanding
- machine interpretation
- interoperability
- governance
- service comparison
- service consumption
- future AI-driven analysis

without turning OSM into:

- a CMDB
- an ITSM system
- a GRC system
- a FinOps system
- an application inventory
- an organizational model
- an enterprise ontology.

The model therefore separates information into four semantic layers:

```text
SERVICE DEFINITION
        │
        ├── Service
        ├── Service Offering
        └── Characteristics
        │
SERVICE POSTURE
        │
        └── Current operational / governance state
        │
PROVENANCE & EVIDENCE
        │
        └── Where the information came from and how trusted it is
        │
EXTERNAL CONTEXT
        │
        └── Applications, assets, CMDB, contracts, ITSM, etc.
```

Framework mappings remain a cross-cutting translation layer.

---

## 2. The definition of "complete"

> **A technological Service Definition is complete when it can unambiguously describe what the service is, who is accountable for it, how it is delivered, what variants are available, who provides it, what service-level expectations and resilience requirements apply, what security, data and compliance constraints apply, how it is financially characterized, and how its authoritative information can be verified — without requiring OSM to represent consuming applications, underlying assets, business hierarchy, organizational hierarchy, or operational workflows.**

This deliberately expands the current OSM definition.

The current model correctly establishes Service as the stable definition and separates it from operational attributes. M-007 does **not** replace that architecture; it completes it.

---

## 3. Fundamental semantic distinction

OSM formally distinguishes three concepts.

### 3.1 Service Definition

**What the service is.**

It changes relatively slowly and is governed as catalog information.

Examples:

- Managed Kubernetes
- Enterprise DNS
- Object Storage
- API Gateway
- Database Platform

### 3.2 Service Posture

**How the service currently stands.**

Examples:

- criticality
- technical debt
- security review status
- automation coverage
- resilience test status
- current cost characteristics
- vendor support status

The existing `service_attributes` and `offering_attributes` patterns support this distinction. M-007 formally establishes it as a semantic principle rather than merely a file organization convention.

### 3.3 External Context

**Information about things around the service that OSM does not own.**

Examples:

- applications consuming the service
- assets implementing it
- CMDB CIs
- business capabilities
- organizations
- contracts
- incidents
- monitoring
- detailed financial transactions

OSM may be integrated with these systems, but does not model them.

---

## 4. Classification of OSM information

Every candidate concept must belong to one of these classifications.

| Classification | Meaning |
|---|---|
| **CORE FIELD** | Canonical semantic property of the OSM model |
| **CHARACTERISTIC** | Valid service/offering property that does not justify a dedicated core field |
| **SERVICE POSTURE** | Current operational, financial, security, resilience or governance state |
| **EXTERNAL CONTEXT** | Information owned by another model/system |
| **FRAMEWORK MAPPING** | Translation into an external framework |
| **OUT OF SCOPE** | Explicitly not represented by OSM |

This prevents future contributors from turning every useful piece of information into a new OSM field.

---

## 5. Service — canonical definition

A Service remains the central entity.

M-007 confirms the following as **CORE**.

### Core Service fields

| Field | Classification | Required |
|---|---|---:|
| `id` | **CORE** | Yes |
| `name` | **CORE** | Yes |
| `description` | **CORE** | Yes |
| `accountable` | **CORE** | Yes — service-definition / overall accountability; distinct from `financial_owner` |
| `technology_stack` | **CORE** | Yes |
| `version` | **CORE** | Yes |
| `valid_from` | **CORE** | Yes |
| `valid_to` | **CORE** | No |
| `lifecycle_state` | **CORE** | Yes |
| `characteristics` | **CORE mechanism** | No |
| `providers` | **CORE relationship** | No |
| `service_offerings` | **CORE relationship** | Yes |

No additional mandatory Service fields are introduced merely because another framework has them.

---

## 6. Technology Stack vs Service Type

Technology Stack already provides a strong technological classification axis.

### Technology Stack answers:

> **Which technological competency owns and operates this service?**

### Service Type would answer:

> **What kind of service is this from a service-definition perspective?**

However, introducing a second taxonomy risks duplication and ambiguity.

Therefore:

> **`service_type` is not a core OSM concept.**

If an adopting organization needs such a classification, it may be represented through the generic Characteristics mechanism, provided it expresses a semantic distinction not already covered by Technology Stack.

OSM must not create parallel taxonomies such as Stack, Service Type, Service Category, Service Class and Service Taxonomy unless a future decision establishes a clear need.

---

## 7. Service Offering

M-007 confirms:

> A Service Offering is a specific requestable/deliverable variant of a Service.

An Offering can represent both:

1. a specific functionality; and/or
2. a configured variant of that functionality.

For example:

```text
Service
Managed Kubernetes
│
├── Offering
│   Managed Kubernetes — Production
│
├── Offering
│   Managed Kubernetes — Development
│
└── Offering
    Managed Kubernetes — Production AWS
```

The Offering may expose configurable dimensions without creating a new Offering for every possible combination.

---

## 8. Offering characteristics

The following are **CHARACTERISTICS**, not mandatory schema fields.

### Delivery

- environment
- location
- region
- deployment model
- operating model
- provisioning model
- delivery channel
- packaging

### Service experience

- availability class
- support level
- service hours
- support hours
- requestability
- approval requirements

### Capacity

- capacity tier
- performance tier
- scalability characteristics

### Commercial

- pricing model
- unit of consumption
- consumption model

`chargeback_model` is offering **posture**, not a second characteristic
of the same fact (see §13).

### Technology

- platform variant
- technology variant

Provider / cloud association is **not** a characteristic and not a
parallel `cloud_providers` field. Use canonical `providers` → ICT
Provider (OSM-M-006). A cloud provider is still an ICT Provider.

The generic Characteristics mechanism should be used instead of creating dozens of dedicated Offering fields.

---

## 9. Service Levels

OSM should represent **service-level expectations**, but not full SLA management.

### OSM may represent

| Concept | Classification |
|---|---|
| Availability target | **SERVICE POSTURE / Service Level** |
| Service hours | **CHARACTERISTIC / Service Level** |
| Support hours | **CHARACTERISTIC / Service Level** |
| Response target | **SERVICE POSTURE / Service Level** |
| Resolution target | **SERVICE POSTURE / Service Level** |
| RTO | **SERVICE POSTURE** |
| RPO | **SERVICE POSTURE** |
| Resilience tier | **CHARACTERISTIC / POSTURE** |

The distinction is:

> **OSM defines service-level expectations; it does not manage SLAs.**

**Targets** (`availability_target`, `response_target`,
`resolution_target`) describe expected service performance.

**Hours** (`service_hours`, `support_hours` characteristics) describe
when the service or support is available.

They are not the same concept. Do not treat hours as a substitute for
targets, or targets as a substitute for hours.

### Explicitly excluded

- SLA entities
- contracts
- penalties
- service credits
- SLA workflow
- escalation workflow
- measurement history

---

## 10. Resilience and criticality

The complete service picture includes:

### Service-level posture

- operational criticality (canonical; DORA maps to this field)
- resilience tier — qualitative resilience classification

Do not add a separate DORA-prefixed criticality field. Stack-level
`mappings.dora.criticality` remains a stack mapping at a different
grain.

### Offering-level posture

- RTO — Recovery Time Objective (explicit)
- RPO — Recovery Point Objective (explicit)
- resilience tested
- last resilience test
- resilience-related evidence

`resilience_tier` and `rto` / `rpo` are different concepts. A tier
MAY be associated with expected recovery characteristics; it is not
a replacement for explicit RTO/RPO values.

---

## 11. Security, data and privacy

OSM should describe enough security/data posture to make a technological service understandable and governable.

### Service-level

| Concept | Classification |
|---|---|
| Data classification | **SERVICE POSTURE** — data handled, processed, stored, or exposed |
| Security classification | **SERVICE POSTURE** — security sensitivity of the service itself |
| Privacy classification | **SERVICE POSTURE / CHARACTERISTIC** |
| AI applicability | **FRAMEWORK / POSTURE** |
| Criticality | **SERVICE POSTURE** |

`data_classification` and `security_classification` may share enum
tokens. They classify different subjects and are not the same fact.

### Offering-level

Potentially:

- PII role
- PII categories
- retention
- security review
- asset coverage
- privacy controls
- security control references

---

## 12. Compliance and frameworks

Frameworks remain **FRAMEWORK MAPPINGS**.

They are never the canonical OSM semantic model.

Current mappings remain:

- TBM
- TOGAF
- ISO 27001
- ISO 27701
- NIST CSF
- GDPR
- DORA
- EU AI Act

Mappings allow OSM information to be translated into external frameworks without making OSM a compliance implementation or certification system.

A framework field with a different name is **not** sufficient justification for a new OSM field (OSM-M-008). If OSM already represents the concept, reuse the canonical field and document the mapping. Do not keep framework-prefixed copies such as `dora_rto` alongside canonical `rto`.

---

## 13. Financial characterization

OSM should answer:

> **How is this service financially characterized?**

It should not answer:

> **How much money did the service actually spend yesterday?**

### Include

| Concept | Classification |
|---|---|
| Cost pool | **SERVICE POSTURE** |
| Chargeback model | **SERVICE POSTURE** |
| Pricing model | **CHARACTERISTIC** |
| Unit of consumption | **CHARACTERISTIC** |
| Financial owner | **SERVICE POSTURE** — financial ownership; distinct from Service `accountable` |
| Unit cost | **SERVICE POSTURE** where useful |

### Exclude

- financial transactions
- budgets
- detailed cost history
- cost trends
- invoices
- accounting records

These remain external FinOps/Finance context.

---

## 14. Automation and operational posture

The complete service picture includes operational maturity signals.

### Include as POSTURE

- automation coverage — overall delivery/operation of the offering
- provisioning automation — the provisioning process specifically
- manual effort
- self-service capability
- technical debt
- vendor support status

`automation_coverage` and `provisioning_automation` share enum tokens
on purpose. They are not the same fact.

### Exclude

- individual automation jobs
- pipelines
- deployment telemetry
- incident history
- MTTR
- monitoring metrics

Those belong to operational systems.

---

## 15. Provenance and evidence

A machine-readable service catalog must be able to answer:

> **"Why should I believe this information?"**

OSM should therefore support provenance for important information.

### Candidate provenance concepts

| Concept | Classification |
|---|---|
| Authoritative source | **CORE METADATA** |
| Source system | **CORE METADATA** |
| Source record ID | **CORE METADATA** |
| Last verified | **CORE METADATA** |
| Evidence reference | **CORE METADATA** |
| Confidence | **CORE METADATA** |
| Discovery method | **POSTURE / METADATA** |

This should be implemented as a **reusable provenance mechanism**, rather than as seven unrelated fields on Service.

The seven fields are not interchangeable:

| Field | Question |
|---|---|
| `authoritative_source` | Who/what is authoritative? |
| `source_system` | Which system did it come from? |
| `source_record_id` | Which record in that system? |
| `last_verified` | When was it last verified? |
| `evidence_reference` | Where is supporting evidence? |
| `confidence` | How much should this fact be trusted? |
| `discovery_method` | How did it enter the catalog? |

The strategic purpose is to distinguish:

```text
ENTERPRISE FACT
      │
      ├── source
      ├── evidence
      ├── verification
      └── confidence
             │
             ▼
       AI interpretation
             │
             ▼
       AI recommendation
```

OSM should make the first layer trustworthy without owning the AI interpretation or recommendation layer.

---

## 16. External context

M-007 explicitly confirms these are **not OSM entities**.

### Enterprise

- Organization
- geography
- legal entity
- business capability
- business service
- business outcome
- value stream

### Technology

- Application
- Application Service
- Asset
- CI
- Service Instance
- infrastructure inventory
- Product Model

### Operations

- Incident
- Problem
- Change
- Request
- workflow
- monitoring
- telemetry

### Commercial / governance

- Contract
- full SLA
- procurement workflow
- detailed GRC controls
- detailed financial transactions

OSM may integrate with these systems, but their models remain external.

---

## 17. Service → Service relationships

**No change in M-007.**

OSM-M-007 does not introduce first-class Service → Service relationships.

This remains a separate future decision because dependency graphs are useful but are not required to establish a complete Service Definition.

---

## 18. Final semantic model

```text
                    TECHNOLOGY STACK
                           │
                           │ owns
                           ▼
                     ┌─────────────┐
                     │   SERVICE   │
                     │             │
                     │ Identity    │
                     │ Definition  │
                     │ Owner       │
                     │ Lifecycle   │
                     │ Stack       │
                     │ Providers   │
                     │ Character.  │
                     └──────┬──────┘
                            │
                       has variants
                            │
                ┌───────────▼───────────┐
                │   SERVICE OFFERING    │
                │                       │
                │ Functionality         │
                │ Delivery variant      │
                │ Characteristics       │
                │ Provider              │
                └───────────┬───────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │  SERVICE POSTURE  │
                  │                   │
                  │ Criticality       │
                  │ Service Levels    │
                  │ Resilience        │
                  │ Security          │
                  │ Data              │
                  │ Financial         │
                  │ Automation        │
                  │ Technical debt    │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │    PROVENANCE     │
                  │                   │
                  │ Source            │
                  │ Evidence          │
                  │ Verification      │
                  │ Confidence        │
                  └───────────────────┘
```

Framework mappings cross-cut the model:

```text
              ┌─────────────────────┐
              │ FRAMEWORK MAPPINGS  │
              │ TBM / TOGAF / ISO   │
              │ NIST / GDPR / DORA  │
              │ EU AI Act           │
              └─────────────────────┘
```

External context remains outside OSM:

```text
Applications
Assets / CMDB
Business
Organization
Geography
Contracts
ITSM
FinOps
GRC
Observability
```

---

## 19. Evolution rule

M-007 establishes the following rule for future OSM evolution:

> **A concept must not become a CORE field merely because it is useful.**

### CORE FIELD

Only if it is:

- fundamental to the meaning of a technological Service
- broadly applicable
- stable
- machine-queryable
- necessary for interoperability
- not adequately represented by Characteristics

### CHARACTERISTIC

If it is:

- meaningful
- variable
- organization-dependent
- potentially extensible
- not sufficiently universal to justify a core field

### SERVICE POSTURE

If it describes:

- current state
- risk
- health
- operational maturity
- current financial/security/resilience condition

### EXTERNAL CONTEXT

If another system/model should own the information.

### FRAMEWORK MAPPING

If the concept exists primarily because another framework uses it **and** OSM does not already represent that concept.

If OSM already represents the concept, document a mapping instead of adding a second field (OSM-M-008).

This is the primary anti-bloat mechanism for OSM.

---

## 20. Consequences

### Positive

OSM becomes substantially more useful without becoming an enterprise ontology.

It can support questions such as:

- What technological services do we provide?
- Who owns them?
- What variants can be consumed?
- Where/how are they delivered?
- Who provides them?
- What service level is expected?
- How resilient are they?
- What data/security constraints apply?
- How automated are they?
- How are they financially characterized?
- Where did this information come from?

These are appropriate questions for a machine-readable technological service model.

### Trade-off

The model becomes larger than the original "minimal catalog."

That is intentional.

> **Small model** means a small number of concepts and relationships — not a small amount of useful information.

---

## 21. Relationship to existing decisions

M-007 does not invalidate:

- OSM-M-001 — Generic Characteristics
- OSM-M-002 — Temporal semantics
- OSM-M-003 — Service is stable definition
- OSM-M-004 — Best-of, not standards accumulation
- OSM-M-005 — DORA provider-link grain (SUPERSEDED by OSM-M-010)
- OSM-M-006 — Canonical ICT Provider references
- OSM-M-008 — One concept, one canonical parameter
- OSM-M-009 — ICT Provider risk_level
- OSM-M-010 — Canonical providers relationship

Instead, M-007 builds on them.

The two-tier hierarchy remains:

**Technology Stack → Service → Service Offering**

---

## 22. Implementation consequence

OSM-M-007 is the architectural source of truth for subsequent implementation.

Cursor should implement the model from this decision rather than independently deciding which concepts belong in OSM.

Implementation work derived from M-007 is expected to address:

1. Service schema
2. Offering schema
3. Characteristics
4. Service Posture
5. Offering Posture
6. Provenance
7. Service-level expectations
8. Resilience
9. Security/data classification
10. Financial characterization
11. Automation posture
12. Examples
13. Validation
14. Specification
15. MODEL.md
16. README
17. Compatibility documentation
18. DECISIONS.md

Implementation must not introduce concepts explicitly excluded by M-007.

---

## 23. Summary

OSM-M-007 establishes that a complete technological service model is not merely a catalog of names and offerings.

It must provide sufficient semantics to understand:

> **what the service is, who owns it, what can be consumed, how it is delivered, who provides it, what it promises, how resilient and secure it is, how it is financially characterized, and why its information can be trusted.**

At the same time, OSM remains deliberately bounded:

> **OSM describes the technological service. It does not model the enterprise around it.**

That boundary is what allows OSM to become richer without becoming another enterprise platform.
