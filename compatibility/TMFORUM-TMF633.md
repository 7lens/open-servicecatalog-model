# TM Forum TMF633 — Service Catalog

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (model / taxonomy / architectural framework)
- **OSM schema fields today:** none dedicated to TMF633

Do not treat this file as a mapping.

## 1. Model overview

TM Forum TMF633 is the REST API and information model for **Service
Catalog Management**. It is commonly used with related TM Forum
catalog and inventory APIs (for example service inventory) and with
the SID information framework distinctions such as service
specification vs service instance, and customer-facing vs
resource-facing services.

This overview is public-model context only. It is not a TMF
certification statement.

## 2. Scope

In scope for a later OSM comparison: catalog-level description of
technological services and requestable variants.

Out of scope for OSM itself (already stated in the OSM spec): business
products, applications, resource inventory, and customer instances.

## 3. OSM concepts potentially corresponding to the model

NOT YET ANALYZED.

Candidates to compare later (not mappings):

| OSM (current) | TMF633 / SID concept to inspect |
|---------------|----------------------------------|
| Service | Service specification / catalog service |
| Service Offering | Catalog offering / candidate / variant |
| Technology Stack | No obvious TMF633 class; may have no counterpart |
| ICT Provider | Related party / supporting resource provider (uncertain) |

## 4. Attribute compatibility

NOT YET ANALYZED.

## 5. Relationship compatibility

NOT YET ANALYZED.

## 6. Terminology differences

NOT YET ANALYZED.

Likely tension to inspect later: OSM uses **Service** strictly as a
**technological service**. TM Forum service language is broader.

## 7. Gaps

NOT YET ANALYZED.

## 8. Potential extensions

None proposed. Extensions require a later maintainer decision
(`OSM-M-*`). This baseline does not add attributes.

## 9. Decisions still required

- Whether OSM Service aligns to TMF specification, candidate, or another class
- Whether OSM Offering aligns to TMF offering or a different catalog object
- Whether CFS/RFS is in or out of OSM's boundary
- Whether any TMF identifier scheme should ever influence OSM IDs
  (current OSM IDs must not be changed in this task)

## 10. Compatibility status

**NOT ANALYZED**
