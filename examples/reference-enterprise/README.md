# Reference enterprise

This is a **worked onboarding** of a real (anonymized) enterprise
service catalog into frozen 7lens OSM 1.3.0.

The source was not a CMDB dump. It was a predecessor catalog that
already had stacks, services, offerings, a health record and a
third-party register — using older vocabulary (`service_attributes`,
DORA-prefixed fields, product-named Services).

This example shows the modelling decisions required to land that
catalog on current OSM:

```
Technology Stack
      ↓
   Service
      ↓
Service Offering ──► ICT Provider
```

with Characteristic, Service Posture, Offering Posture and Provenance
where the source actually supports them.

- **Anonymized.** No organization name, people, contract numbers or
  internal platform names.
- **Financial-sector multinational context** (user-supplied). The
  source files do **not** contain country-of-operation data; ~38
  countries stay outside OSM.
- **Representative, not a conversion of all 95 source services.**
- **Not a compliance certification and not a vendor recommendation.**
- **Schema unchanged.**

## Reading order

1. [Golden Example](golden-example/README.md)
2. [Onboarding Guide](onboarding-guide.md)
3. Full catalog in `catalog/` and `posture/`
4. [Traceability](traceability.md)

## What is in the full catalog

| File | Concept |
|------|---------|
| `catalog/technology-stacks.yaml` | 10 competency domains from the source |
| `catalog/services.yaml` | Technological services with nested offerings |
| `catalog/ict-providers.yaml` | Legal sellers for those services |
| `posture/service-posture.yaml` | Optional, source-dependent. Predecessor demo health values were not imported |

The predecessor listed 95 services. Most were vendor products, ITSM
processes, CMDB inventory or local platform names. They are not
copied. Traceability lists what was collapsed, kept or left out.

## Validate

```bash
python3 validation/validate.py --catalog examples/reference-enterprise
python3 validation/validate.py --catalog examples/reference-enterprise/golden-example
```
