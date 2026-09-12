# ServiceNow CSDM

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (model / taxonomy / architectural framework)
- **OSM schema fields today:** none dedicated to CSDM

Do not treat this file as a mapping.

## 1. Model overview

The ServiceNow **Common Service Data Model (CSDM)** is a prescribed
way to use ServiceNow CMDB classes for services, applications and
related objects. It typically spans foundation data, design objects,
technical services, application services, and sell/consume (business)
services.

CSDM is vendor-specific. OSM is vendor-neutral. Compatibility, if
later established, would mean an adopter can *project* OSM records
into CSDM classes — not that OSM is a ServiceNow product model.

## 2. Scope

In scope for a later OSM comparison: CSDM classes that describe
**technical services** and **technical service offerings**.

Out of scope for OSM: business services, business applications,
application services, and CMDB configuration items. OSM already
excludes those domains.

## 3. OSM concepts potentially corresponding to the model

NOT YET ANALYZED.

Candidates to compare later (not mappings):

| OSM (current) | CSDM concept to inspect |
|---------------|-------------------------|
| Service | Technical Service (possible) |
| Service Offering | Technical Service Offering (possible) |
| Technology Stack | Uncertain (not a standard CSDM class) |
| ICT Provider | Vendor / company / service provider CI (uncertain) |

Business Service, Business Application and Application Service are
**not** OSM entities.

## 4. Attribute compatibility

NOT YET ANALYZED.

## 5. Relationship compatibility

NOT YET ANALYZED.

CSDM is relationship-heavy (depends on, provided by, consumes). OSM
currently has a small relationship set only.

## 6. Terminology differences

NOT YET ANALYZED.

Likely tension: CSDM "service" includes business and application
layers that OSM refuses to model.

## 7. Gaps

NOT YET ANALYZED.

## 8. Potential extensions

None proposed. No attributes are added in this baseline.

## 9. Decisions still required

- Whether any OSM concept should ever be documented as a CSDM class
  mapping, or only as an integration example
- How to talk about CSDM without implying OSM models applications

## 10. Compatibility status

**NOT ANALYZED**
