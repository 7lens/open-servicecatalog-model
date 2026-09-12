# ITIL

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (model / taxonomy / architectural framework)
- **OSM schema fields today:** none dedicated to ITIL

Do not treat this file as a mapping.

## 1. Model overview

ITIL (AXELOS / PeopleCert) is a service-management practice framework.
It defines, among other things, **services**, **service offerings**,
a **service catalog**, and a **service portfolio**, plus practices for
request, incident, change and service-level management.

ITIL is a management framework, not a machine-readable schema. OSM
would be compatible with ITIL only in the sense of describing catalog
records that an ITIL-aligned operating model can use.

## 2. Scope

In scope for a later OSM comparison: service catalog and service
offering concepts as they apply to **technological** services.

Out of scope for OSM: the full ITIL practice model, business services
as a first-class OSM entity, and process workflows.

## 3. OSM concepts potentially corresponding to the model

NOT YET ANALYZED.

Candidates to compare later (not mappings):

| OSM (current) | ITIL concept to inspect |
|---------------|-------------------------|
| Service | Service (technical / IT service) |
| Service Offering | Service offering |
| Technology Stack | No direct ITIL class; maybe a catalog category |
| Service Owner | Service owner practice role |
| ICT Provider | Supplier / third party (uncertain) |

## 4. Attribute compatibility

NOT YET ANALYZED.

## 5. Relationship compatibility

NOT YET ANALYZED.

## 6. Terminology differences

NOT YET ANALYZED.

Likely tension: ITIL **service** is often broader than OSM's
technological-service boundary. OSM explicitly does not model
business services.

## 7. Gaps

NOT YET ANALYZED.

## 8. Potential extensions

None proposed. No attributes are added in this baseline.

## 9. Decisions still required

- Whether OSM should ever distinguish request catalog vs technical catalog
- Whether ITIL service offering and OSM Service Offering are the same grain
- Whether SLAs belong in OSM or remain outside

## 10. Compatibility status

**NOT ANALYZED**
