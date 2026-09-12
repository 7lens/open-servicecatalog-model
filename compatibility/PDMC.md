# PDMC

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (model / taxonomy / architectural framework)
- **OSM schema fields today:** none dedicated to PDMC
- **Working identification:** Practical Data Model for CMDB (public
  CMDB reference model, Services Tier). Confirm this is the intended
  reference; see decisions below.

Do not treat this file as a mapping.

## 1. Model overview

**Working identification (unconfirmed):** PDMC here is treated as the
**Practical Data Model for CMDB**, a public CMDB information model
with tiers such as Business, Services, and Service Configuration.
The Services Tier distinguishes customer-facing services and backend
services, and links them to configuration items.

If maintainers intended a different public service-model reference
(for example CPSV-AP for public-administration services), this file
must be retargeted before analysis starts.

## 2. Scope

In scope for a later OSM comparison: the PDMC **Services Tier**, to
the extent it describes provider capabilities rather than CMDB
instances.

Out of scope for OSM: CMDB configuration items, the Service
Configuration Tier, and the Business Tier. OSM already excludes
infrastructure inventory / CMDB CIs.

## 3. OSM concepts potentially corresponding to the model

NOT YET ANALYZED.

Candidates to compare later (not mappings):

| OSM (current) | PDMC concept to inspect (if PDMC = Practical Data Model for CMDB) |
|---------------|---------------------------------------------------------------------|
| Service | Backend service / capability (possible) |
| Service Offering | Service product / package / offering (uncertain) |
| Technology Stack | Uncertain |
| ICT Provider | External backend provider (uncertain) |

## 4. Attribute compatibility

NOT YET ANALYZED.

## 5. Relationship compatibility

NOT YET ANALYZED.

## 6. Terminology differences

NOT YET ANALYZED.

Likely tension: PDMC is a CMDB model. OSM is a service catalog model
that refuses to be a CMDB.

## 7. Gaps

NOT YET ANALYZED.

If PDMC is confirmed as a CMDB model, large parts may be
**NOT APPLICABLE** rather than gaps inside OSM. That judgment is not
made here.

## 8. Potential extensions

None proposed. No attributes are added in this baseline.

## 9. Decisions still required

- **Confirm PDMC identity** (Practical Data Model for CMDB vs another
  public reference)
- Whether any CMDB-oriented model belongs in the compatibility
  universe given OSM's CI exclusion
- If CPSV-AP or another catalog vocabulary was intended, add or
  replace this file by a later `OSM-C-*` decision

## 10. Compatibility status

**NOT ANALYZED**
