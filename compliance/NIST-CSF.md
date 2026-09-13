# NIST CSF

**Mapped version:** **NIST CSF 2.0** (26 February 2024) — Functions
Govern, Identify, Protect, Detect, Respond, Recover.

**Status:** **MAPPED** (Functions + OSM assessment signal)

OSM is **not** a NIST CSF profile and not a claim that an adopter
complies with the Cybersecurity Framework. OSM does **not**
introduce NIST Profiles, Categories, Subcategories, Tiers, or
control-implementation structures.

OSM stores CSF **Functions** as a translation layer on stacks and
offerings. `nist_control_status` is an **OSM/framework assessment
mapping signal**. It is **not** a native NIST CSF object, not a
Subcategory, and not a control from a NIST catalogue.

## Mapping table

| External concept (CSF 2.0) | OSM target | Grain | Kind | Outside OSM |
|----------------------------|------------|-------|------|-------------|
| Functions (GV, ID, PR, DE, RS, RC) | `mappings.nist_csf`; `nist_functions` | Stack; Offering posture | Partial labels | Categories, Subcategories |
| Organizational / Community Profiles | — | Organization | **EXTERNAL** | Profiles |
| Tiers | — | Organization | **EXTERNAL** | Tiers |
| Implementation / assessment status | `nist_control_status` | Offering posture | OSM **signal** (`implemented` / `partially-implemented` / `planned` / `not-applicable`). **Not** a CSF object. Do not present examples as if OSM implements the NIST control catalogue. | Control catalogues, informative references |
| Review cadence | `last_security_review` | Offering posture | Operations signal | Assessments |

## `nist_control_status`

This field already exists in the frozen schema. It is **not**
redesigned here. Treat it as: “how far has this offering been
assessed against the mapped CSF Functions in *this* catalog?” — an
OSM mapping signal, not a NIST artefact.

A function tag is not an implemented control. Completing OSM fields
is not a CSF profile.

## What stays in NIST CSF (**EXTERNAL**)

- Profiles
- Categories and Subcategories
- Tiers
- control implementation structures
- a security assessment or certification

Exact field definitions are in
[`SPECIFICATION.md`](../SPECIFICATION.md).
