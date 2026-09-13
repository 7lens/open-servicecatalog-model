# Examples

OSM ships several example catalogs. Start at the smallest that answers
your question. You do not need `_internal` to learn the model.

```
examples/
├── catalog/                 ← basic synthetic examples
├── posture/
├── reference-enterprise/    ← real predecessor catalog onboarded to OSM
│   └── golden-example/
└── reference-estate/        ← researched public-provider estate
    └── golden-example/
```

Service Offerings are nested under `catalog/services.yaml`.
Characteristics belong on Service and Offering definitions.
Posture is recorded separately as `service_posture` /
`offering_posture`.

```
catalog/technology-stacks.yaml
        │  1 stack : many services
        v
catalog/services.yaml          ← catalog (Service + nested Offerings)
        │                       characteristics[] on Service / Offering
        │
        │  providers[] ──────────► catalog/ict-providers.yaml
        │
        │  service_id
        v
posture/service-posture.yaml   ← Service Posture + nested Offering Posture
```

Identifiers:

- Service ID = 2 segments, for example `compute.kubernetes`
- Offering ID = 3 segments, for example `compute.kubernetes.aws-eks`
- `providers` values are ICT Provider ids
- posture `service_id` / `offering_id` match the catalog

Framework mappings in these files are illustrative. They are not
legal advice and not evidence of compliance.

---

## Basic examples

**Syntax tutorial only.** Small synthetic YAML in this directory
(`catalog/`, `posture/`) to learn field shape. Modelling follows the
same core rules as the golden example (Service = technological
service; Offering = provider/product variant; legal seller ids;
posture is current state). Lifecycle, posture numbers and extra
characteristics are illustrative. Do not copy them as a real estate.

For onboarding a real catalog, start at
[reference-enterprise/golden-example](reference-enterprise/golden-example/README.md).

```bash
python3 validation/validate.py
```

## Reference Enterprise

**[examples/reference-enterprise/](reference-enterprise/)**

A real anonymized enterprise predecessor catalog onboarded onto
current OSM. Product-named services become capability services;
`service_attributes` become `service_posture`; DORA-prefixed fields
become canonical OSM fields.

Reading order:

1. [Golden Example](reference-enterprise/golden-example/README.md)
2. [Onboarding Guide](reference-enterprise/onboarding-guide.md)
3. Full catalog in `reference-enterprise/catalog/`
4. [Traceability](reference-enterprise/traceability.md)

```bash
python3 validation/validate.py --catalog examples/reference-enterprise
python3 validation/validate.py --catalog examples/reference-enterprise/golden-example
```

## Reference Technology Estate

**[examples/reference-estate/](reference-estate/)**

A researched, anonymized hyperscaler/SaaS estate encoded from public
provider documentation (not the predecessor catalog above).

```bash
python3 validation/validate.py --catalog examples/reference-estate
python3 validation/validate.py --catalog examples/reference-estate/golden-example
```
