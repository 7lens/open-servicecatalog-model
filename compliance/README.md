# Compliance

OSM is designed to **map** regulatory, security, privacy and control
context onto a small technological-service catalog. It is not a
control library, a GRC platform, or a claim that an adopter
**complies with** any regulation.

The principle is:

> Canonical OSM concept first. Framework mapping second.

Do not add a second parameter because a regulation uses a different
name for the same fact (**OSM-C-009**).

Optional mapping fields are **reference hints**. Example values are
not legal advice and not evidence of certification.

Service, catalog and architecture frameworks live in
[`models/`](../models/).

Exact types and enums are in [`SPECIFICATION.md`](../SPECIFICATION.md).

Concepts that stay **outside** OSM are listed in
[`SPECIFICATION.md`](../SPECIFICATION.md) — *External Concepts —
Intentionally Outside OSM*.

---

## Status

Use these labels. Do not use vague “supported”. OSM is **not
formally compliant or certified** against any of these frameworks.

| Status | Meaning |
|--------|---------|
| **MAPPED** | Correspondence is documented. OSM can represent or join the listed signals. Not certification. |
| **PARTIAL** | Some locators exist; remaining concepts are **EXTERNAL** or documentation conventions. |
| **EXTERNAL** | The concept belongs in another system (RoPA, RoI, ISMS, PIMS, CSF profile, technical file). |
| **NOT IN SCOPE** | Outside OSM’s technological-service boundary. |
| **FUTURE / OPTIONAL** | Characteristic convention or schema candidate; not current core. |

| Framework | Current version mapped | Status | File |
|-----------|------------------------|--------|------|
| ISO/IEC 27001 | **27001:2022 + Amendment 1:2024** | **MAPPED** (control ID locators only) | [ISO-27001.md](ISO-27001.md) |
| ISO/IEC 27701 | **27701:2025** (standalone PIMS) | **PARTIAL** (role/category locators; not a PIMS) | [ISO-27701.md](ISO-27701.md) |
| NIST CSF | **CSF 2.0** | **MAPPED** (Functions + OSM assessment signal) | [NIST-CSF.md](NIST-CSF.md) |
| GDPR | Regulation **(EU) 2016/679** | **PARTIAL** (high-level locators; not a RoPA) | [GDPR.md](GDPR.md) |
| DORA | Regulation **(EU) 2022/2554** + RTS **2024/1773** + ITS **2024/2956** | **PARTIAL** (`providers` feeds RoI; OSM is **not** RoI) | [DORA.md](DORA.md) |
| EU AI Act | Regulation **(EU) 2024/1689** | **PARTIAL** (compatibility labels; not Art. 6 classification) | [EU-AI-ACT.md](EU-AI-ACT.md) |

Each mapping file answers: external concept, OSM target, grain,
direct / partial / conceptual, what remains outside, semantic
differences.
