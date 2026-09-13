# Reference technology estate

This is a researched, anonymized reference technology estate
demonstrating how 7lens OSM can be applied to a large enterprise
technology landscape.

- **Anonymized.** No organization name, contract numbers, account IDs,
  hostnames or internal identifiers.
- **Based on a real enterprise estate**, reshaped into public OSM
  records using well-known provider and product names.
- **Financial-sector context**, multinational.
- **Representative, not a universal template.** Another enterprise
  will choose different stacks, services and offerings.
- **Designed for learning and model validation.**
- **Not a compliance certification.**
- **Not a recommendation of any vendor.**

The frozen OSM schema was not changed to produce this catalog.

## Reading order

1. [Golden Example](golden-example/README.md) — learn OSM in ten minutes
2. [Onboarding Guide](onboarding-guide.md) — how to transform an estate
3. [Mapping Cookbook](mapping-cookbook.md) — modelling judgement, case by case
4. [Full Reference Estate](catalog/) — the researched catalog
5. [Traceability](traceability.md) — how public records were derived

## What is in the full catalog

| File | Concept |
|------|---------|
| `catalog/technology-stacks.yaml` | Operational competency domains |
| `catalog/services.yaml` | Technological services with nested offerings |
| `catalog/ict-providers.yaml` | Canonical third-party sellers |
| `posture/service-posture.yaml` | Thin service posture and nested offering posture |

Approximate richness of this public set:

- 11 Technology Stacks
- 25 Services
- 60 Service Offerings
- 20 ICT Providers
- 12 Service Posture records

Hyperscalers carry more offerings (compute, storage, database,
Kubernetes, functions, network, identity). Smaller providers carry
about two. That is intentional: the catalog shows structure, not a
vendor dump.

The golden example is a smaller independently validatable catalog under
`golden-example/`.

## What this catalog refuses to claim

Customer-dependent fields are left null or omitted:

- `gdpr_dpa_signed`
- `dora_notification_clause`
- `risk_level`
- `rto` / `rpo`
- `operational_criticality`
- contract references and dates

Provider `certifications[]` are published program names. They are not
proof that every service, region or customer deployment is certified.

Vendor SLAs are offering characteristics (`vendor_availability_sla`).
They are not `availability_target`.

OSM is not the DORA Register of Information, not a GDPR ROPA, and not
an AI Act provider/deployer register.

## Validate

From the repository root:

```bash
python3 validation/validate.py --catalog examples/reference-estate
python3 validation/validate.py --catalog examples/reference-estate/golden-example
```
