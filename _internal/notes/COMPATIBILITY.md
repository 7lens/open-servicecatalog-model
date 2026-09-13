# 7lens OSM — Compatibility

**Canonical name:** 7lens OSM  
**Expanded:** 7lens Open Service Catalog Model

This document is the index for the **initial compatibility universe** of
7lens OSM. It records *what we intend to evaluate*, and the status of
each analysis.

Most entries remain **NOT ANALYZED**. TM Forum TMF633, ITIL v5 and
ServiceNow CSDM are **PARTIALLY COMPATIBLE** (selective compatibility).
No entry is marked fully **COMPATIBLE**. OSM does not implement ITIL,
TMF or CSDM.

Related decisions: [`DECISIONS.md`](../decisions/DECISIONS.md) — **OSM-C-001**
(as amended by **OSM-C-002**, **OSM-C-003**); TM Forum follow-up
**OSM-M-001**–**OSM-M-004**; ITIL v5 **OSM-C-004**; CSDM **OSM-C-005**
and provider references **OSM-M-006**; Complete Service Definition
**OSM-M-007**; One concept, one canonical parameter **OSM-M-008**;
ICT Provider `risk_level` **OSM-M-009**; canonical `providers`
relationship **OSM-M-010** (supersedes **OSM-M-005**).

---

## Canonical core, not a framework clone

OSM is **not** an alternative implementation of ITIL (or of TMF,
CSDM, ArchiMate, TOGAF, or TBM).

OSM provides a small canonical core definition of technological
services and service offerings that can be mapped to those frameworks
and integrated with customer systems and tools.

```
OSM core definition
        ↓
semantic mapping
        ↓
ITIL / CSDM / ArchiMate / other frameworks
        ↓
customer tools and systems
```

The objective is compatibility and semantic interoperability, not
reproduction. OSM holds the minimum canonical semantics needed to
define its concepts. Contextual concepts and richer relationships
can exist in the broader 7lens model or in customer systems and
frameworks without being duplicated in OSM.

A framework must not drive a new OSM field simply because it has a
field with a different name (OSM-M-008). Reuse the canonical OSM
concept and document the mapping.

---

## Why compatibility matters

Technology organizations already live with several service, architecture
and governance languages: TM Forum catalogs, ITIL, CSDM, ArchiMate,
TOGAF, TBM, and a set of security, privacy and operational-resilience
frameworks.

7lens OSM incorporates useful semantics from existing models where
they materially improve interoperability, governance or
machine-readability, and deliberately avoids wholesale reproduction
of those models (OSM-M-004). Compatibility does not mean copying.

## What "compatible" means here

For 7lens OSM, **compatible** means:

- an adopter can relate OSM records to the other model or framework
  without inventing a private translation layer for every field
- OSM concepts, attributes and relationships can represent the
  *service-catalog-relevant* subset of the other model
- differences in terminology are documented
- gaps are explicit, including cases where OSM should stay silent

Compatible does **not** mean:

- OSM implements the other model
- OSM replaces the other model
- an organization using OSM complies with a regulation
- every class in the other model has an OSM twin

Until analysis is finished, the honest status is **NOT ANALYZED**,
except where maintainers have accepted a mapping decision (currently
TM Forum TMF633, ITIL v5 and ServiceNow CSDM are **PARTIALLY
COMPATIBLE**).

## Model compatibility vs compliance / governance mapping

These are different jobs.

| | A. Models / taxonomies / architectural frameworks | B. Compliance / governance frameworks |
|--|--|--|
| Question | Can OSM describe technological services in a way that lines up with this catalog or architecture model? | Can OSM *represent information relevant to* this framework for a technological service? |
| Success looks like | Concept, attribute and relationship mapping, with terminology notes | Optional fields or mappings that a governance team can use as a reference |
| Failure mode | Pretending OSM is ITIL, CSDM or TMF633 | Writing "OSM complies with GDPR / DORA / ISO 27001" |

OSM may carry optional reference mappings to group B. Those fields are
not a certification, a legal interpretation, or a completed audit.

---

## Current repository snapshot (audit)

This baseline starts from the public repository as it exists, not from
any private source catalog.

### Entities already defined

| Entity | Role |
|--------|------|
| Technology Stack | Operational competency / ownership domain |
| Service | Stable **definition** of a technological service (OSM-M-003), including `version`, validity and `lifecycle_state` |
| Service Offering | Atomic requestable / deliverable variant |
| Characteristic | Nested property on Service or Offering (OSM-M-001); not a catalog entity |
| Provenance | Reusable source/evidence/confidence object (OSM-M-007); not a catalog entity |
| Service Posture | Current operational / governance state (`service_attributes`) |
| Offering Posture | Variant-level operational state (`offering_attributes`) |
| ICT Provider | Canonical third-party technology provider (OSM-M-006) |
| Roles (documentation) | Technology Stack Owner, Service Owner |

### Relationships already defined

- Technology Stack `1 : many` Service (`service.technology_stack` = stack `name`)
- Service `1 : many` Service Offering (offering ID prefix = service ID)
- Service / Offering `0 : many` Characteristic (nested; no characteristic id)
- Service / Offering / posture `0 : 1` Provenance (nested; OSM-M-007)
- Service `1 : 0..1` Service Attributes (`service_id`)
- Service Attributes `1 : many` Offering Attributes (`offering_id`)
- Service / Offering `0 : many` ICT Provider (`providers` ids; OSM-M-006, OSM-M-010)

Consumers of a technological service are out of scope. No application,
Application Service, Business Service, Digital Product, Value Stream,
Service Instance or CMDB-CI relationship is defined. Service → Service
relationships are deliberately outside the current OSM core
(OSM-C-004, OSM-C-005).

### Mapping fields already present

Optional reference mappings already exist on **Technology Stack**
(`tbm_tower`, `tbm_sub_tower`, `togaf_domain`, `iso27001`, `iso27701`,
`nist_csf`, `gdpr`, `dora`, `ai_act`) and on **service / offering
attributes** (ISO, NIST, GDPR and EU AI Act fields). DORA recovery,
criticality and resilience testing map to canonical `rto`, `rpo`,
`operational_criticality` and `resilience_tested`; DORA provider
associations map to canonical `providers` (OSM-M-010). There are no
DORA-prefixed copies of those fields (OSM-M-008).

No mapping fields currently exist for ArchiMate. TM Forum analysis is
recorded in
[compatibility/TMFORUM-TMF633.md](compatibility/TMFORUM-TMF633.md)
(OSM-M-001–OSM-M-004). ITIL v5 analysis is recorded in
[compatibility/ITIL.md](compatibility/ITIL.md) (OSM-C-004). CSDM
analysis is recorded in
[compatibility/SERVICENOW-CSDM.md](compatibility/SERVICENOW-CSDM.md)
(OSM-C-005, OSM-M-006). OSM has no CSDM, ITIL-specific or TMF API
resource types. Canonical provider association uses ICT Provider ids.

The presence of a field is **not** a completed compatibility analysis.

### What this repository does not contain

- full implementations of ITIL, TMF, CSDM, ArchiMate, TOGAF or TBM
- proven *complete* mappings (TMF633, ITIL v5 and CSDM are selective /
  partial only)
- regulatory compliance claims that should be treated as fact

---

## Initial compatibility universe

The following models and frameworks form the **initial compatibility
baseline** for 7lens OSM (**OSM-C-001**, amended by **OSM-C-002** and
**OSM-C-003**). OSM is designed to be compatible with this universe.
Except for the TM Forum, ITIL v5 and CSDM decisions below, that design
intent is not yet validated.

### A. Models / taxonomies / architectural frameworks

| Model | File | Status |
|-------|------|--------|
| TM Forum TMF633 Service Catalog | [compatibility/TMFORUM-TMF633.md](compatibility/TMFORUM-TMF633.md) | PARTIALLY COMPATIBLE |
| ITIL v5 | [compatibility/ITIL.md](compatibility/ITIL.md) | PARTIALLY COMPATIBLE |
| ServiceNow CSDM | [compatibility/SERVICENOW-CSDM.md](compatibility/SERVICENOW-CSDM.md) | PARTIALLY COMPATIBLE |
| ArchiMate | [compatibility/ARCHIMATE.md](compatibility/ARCHIMATE.md) | NOT ANALYZED |
| TOGAF | [compatibility/TOGAF.md](compatibility/TOGAF.md) | NOT ANALYZED |
| TBM | [compatibility/TBM.md](compatibility/TBM.md) | NOT ANALYZED |

### B. Compliance / governance frameworks

| Framework | File | Status |
|-----------|------|--------|
| ISO/IEC 27001 | [compliance/ISO-27001.md](compliance/ISO-27001.md) | NOT ANALYZED |
| ISO/IEC 27701 | [compliance/ISO-27701.md](compliance/ISO-27701.md) | NOT ANALYZED |
| NIST CSF | [compliance/NIST-CSF.md](compliance/NIST-CSF.md) | NOT ANALYZED |
| GDPR | [compliance/GDPR.md](compliance/GDPR.md) | NOT ANALYZED |
| DORA | [compliance/DORA.md](compliance/DORA.md) | NOT ANALYZED |
| EU AI Act | [compliance/EU-AI-ACT.md](compliance/EU-AI-ACT.md) | NOT ANALYZED |

---

## Status vocabulary

Use only these values in compatibility and compliance files:

| Status | Meaning |
|--------|---------|
| NOT ANALYZED | Universe member identified; no mapping yet |
| ANALYSIS IN PROGRESS | Comparison started; not reviewable |
| MAPPED | Correspondence documented; compatibility not yet judged |
| PARTIALLY COMPATIBLE | Some required correspondences work; remaining concepts may be gaps or **deliberate OSM-core boundaries** (see ITIL v5 OSM-C-004, CSDM OSM-C-005) |
| COMPATIBLE | Reviewed mapping covers the service-catalog-relevant subset |
| REQUIRES EXTENSION | OSM cannot represent a needed concept without a model change |
| NOT APPLICABLE | Outside OSM's technological-service boundary |

Do not mark a row **COMPATIBLE** until maintainers complete and accept
the analysis.

---

## How later decisions will be applied

Maintainers record accepted changes in [`DECISIONS.md`](../decisions/DECISIONS.md).
Detailed `OSM-M-*` documents are in [`../decisions/`](../decisions/).
A future propagation pass must update every listed surface and must
**not** invent model changes. See *Decision propagation* in the
register. **OSM-M-007** is ACCEPTED; it does not add framework
entities to OSM. **OSM-M-008** is ACCEPTED: frameworks map to
canonical OSM fields rather than creating copies of them.
