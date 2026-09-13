# Compliance

OSM is designed to **accommodate** regulatory, security, privacy and
control context. It is not a control library, a GRC platform, or a
claim that an adopter complies with any regulation.

The principle is:

> Represent each concept once. Let the framework map onto it.

Do not add a second parameter because a regulation uses a different
name for the same fact.

Optional mapping fields are **reference hints**. Example values are
not legal advice and not evidence of certification.

Service, catalog and architecture frameworks live in
[`models/`](../models/).

Exact types and enums are in [`SPECIFICATION.md`](../SPECIFICATION.md).

| Framework | What it maps onto OSM |
|-----------|------------------------|
| [ISO/IEC 27001](ISO-27001.md) | Information-security control references |
| [ISO/IEC 27701](ISO-27701.md) | Privacy-information role, categories and retention |
| [NIST CSF](NIST-CSF.md) | Cybersecurity functions as a translation layer |
| [GDPR](GDPR.md) | Personal-data processing signals |
| [DORA](DORA.md) | Operational resilience via canonical OSM fields |
| [EU AI Act](EU-AI-ACT.md) | AI-system applicability on technological services |
