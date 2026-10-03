# NIST CSF

**Mapped version:** **NIST CSF 2.0** (26 February 2024) — Functions
Govern, Identify, Protect, Detect, Respond, Recover.

> **Mapping basis (2026-06-11):** CSF 2.0 is the current version,
> released by NIST in February 2024 and organized around six
> Functions — Govern, Identify, Protect, Detect, Respond, Recover
> ([NIST CSF 2.0 release](https://www.nist.gov/news-events/news/2024/02/nist-releases-version-20-landmark-cybersecurity-framework),
> [NIST SP 1299 resource guide](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1299.pdf)).
> No newer CSF revision has been published. Source wording was
> rephrased for licensing compliance.

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

Each top-level NIST CSF 2.0 concept below carries a status from the
index vocabulary (MAPPED / PARTIAL / EXTERNAL / NOT IN SCOPE / FUTURE /
OPTIONAL), so none is silently missing.

| External concept (CSF 2.0) | OSM target | Grain | Status + kind | Outside OSM |
|----------------------------|------------|-------|---------------|-------------|
| Functions (GV, ID, PR, DE, RS, RC) | `mappings.nist_csf`; `nist_functions` | Stack; Offering posture | **MAPPED** — Function labels. | Categories, Subcategories |
| Categories and Subcategories | — | — | **EXTERNAL** — OSM stores Functions only, not the outcome catalogue. | Category / Subcategory outcomes |
| Organizational / Community Profiles | — | Organization | **EXTERNAL** — OSM is not a profile. | Profiles |
| Tiers | — | Organization | **EXTERNAL** — implementation-tier judgement. | Tiers |
| Implementation / assessment status | `nist_control_status` | Offering posture | **PARTIAL** — OSM **signal** (`implemented` / `partially-implemented` / `planned` / `not-applicable`). **Not** a CSF object. Do not present examples as if OSM implements the NIST control catalogue. | Control catalogues, informative references |
| Review cadence | `last_security_review` | Offering posture | **PARTIAL** — operations signal. | Assessments |

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
