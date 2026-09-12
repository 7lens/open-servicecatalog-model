# 7lens OSM — Compatibility

**Canonical name:** 7lens OSM  
**Expanded:** 7lens Open Service Catalog Model

This document is the index for the **initial compatibility universe** of
7lens OSM. It records *what we intend to evaluate*, not what has already
been proven.

Compatibility analysis has **not** been completed. No model in this
baseline is marked compatible.

Related decision: [`DECISIONS.md`](DECISIONS.md) — **OSM-C-001**.

---

## Why compatibility matters

Technology organizations already live with several service, architecture
and governance languages: TM Forum catalogs, ITIL, CSDM, ArchiMate,
TOGAF, TBM, CMDB reference models, and a set of security, privacy and
operational-resilience frameworks.

7lens OSM is being designed to bring together the **useful
characteristics** of those languages in one deliberately small,
vendor-neutral Service Catalog Model. Compatibility work is how that
design goal will be validated. Until a mapping is written and reviewed,
OSM is only **designed to be compatible** with the universe below.

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

Until analysis is finished, the honest status is **NOT ANALYZED**.

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
| Service | Technological capability delivered by the technology organization |
| Service Offering | Atomic requestable / deliverable variant |
| Service Attributes | Health / governance posture of a service |
| Offering Attributes | Variant-level operational data |
| ICT Provider | Third-party technology dependency |
| Roles (documentation) | Technology Stack Owner, Service Owner |

### Relationships already defined

- Technology Stack `1 : many` Service (`service.technology_stack` = stack `name`)
- Service `1 : many` Service Offering (offering ID prefix = service ID)
- Service `1 : 0..1` Service Attributes (`service_id`)
- Service Attributes `1 : many` Offering Attributes (`offering_id`)
- Offering → ICT Provider (`dora_third_party_deps`)
- ICT Provider → Service (`services_consumed`)

Consumers of a technological service are out of scope. No application,
business-service or CMDB-CI relationship is defined.

### Mapping fields already present

Optional reference mappings already exist on **Technology Stack**
(`tbm_tower`, `tbm_sub_tower`, `togaf_domain`, `iso27001`, `iso27701`,
`nist_csf`, `gdpr`, `dora`, `ai_act`) and on **service / offering
attributes** (ISO, NIST, GDPR, DORA-named and EU AI Act fields).

No mapping fields currently exist for TM Forum TMF633, ITIL,
ServiceNow CSDM, ArchiMate or PDMC.

The presence of a field is **not** a completed compatibility analysis.

### What this repository does not contain

- dedicated compatibility files (this directory tree is new)
- a decision log (see `DECISIONS.md`, new)
- proven mappings
- regulatory compliance claims that should be treated as fact

---

## Initial compatibility universe

The following models and frameworks form the **initial compatibility
baseline** for 7lens OSM (OSM-C-001). OSM is designed to be compatible
with this universe. That design intent is not yet validated.

### A. Models / taxonomies / architectural frameworks

| Model | File | Status |
|-------|------|--------|
| TM Forum TMF633 Service Catalog | [compatibility/TMFORUM-TMF633.md](compatibility/TMFORUM-TMF633.md) | NOT ANALYZED |
| ITIL | [compatibility/ITIL.md](compatibility/ITIL.md) | NOT ANALYZED |
| ServiceNow CSDM | [compatibility/SERVICENOW-CSDM.md](compatibility/SERVICENOW-CSDM.md) | NOT ANALYZED |
| ArchiMate | [compatibility/ARCHIMATE.md](compatibility/ARCHIMATE.md) | NOT ANALYZED |
| TOGAF | [compatibility/TOGAF.md](compatibility/TOGAF.md) | NOT ANALYZED |
| TBM | [compatibility/TBM.md](compatibility/TBM.md) | NOT ANALYZED |
| PDMC (Practical Data Model for CMDB) | [compatibility/PDMC.md](compatibility/PDMC.md) | NOT ANALYZED |

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
| PARTIALLY COMPATIBLE | Some required correspondences work; gaps remain |
| COMPATIBLE | Reviewed mapping covers the service-catalog-relevant subset |
| REQUIRES EXTENSION | OSM cannot represent a needed concept without a model change |
| NOT APPLICABLE | Outside OSM's technological-service boundary |

Do not mark a row **COMPATIBLE** until maintainers complete and accept
the analysis.

---

## How later decisions will be applied

Maintainers record accepted changes in [`DECISIONS.md`](DECISIONS.md).
A future propagation pass must update every listed surface and must
**not** invent model changes. See *Decision propagation* in that file.
