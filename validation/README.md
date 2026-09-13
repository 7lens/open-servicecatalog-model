# Validation

Lightweight checks for OSM catalogs. This is not a platform
and not a full JSON Schema compiler — it enforces the identity and
reference rules in `SPECIFICATION.md`.

## Run

From the repository root:

```bash
python3 -m pip install -r validation/requirements.txt
python3 validation/validate.py
python3 validation/validate.py --catalog examples/reference-enterprise
python3 validation/validate.py --catalog examples/reference-enterprise/golden-example
python3 validation/validate.py --catalog examples/reference-estate
python3 validation/validate.py --catalog examples/reference-estate/golden-example
```

Default `--catalog` is `examples/` (the small synthetic set).
`examples/reference-enterprise/` is the onboarded predecessor catalog.
`examples/reference-estate/` is the researched public-provider estate.
PyYAML is the only dependency. Point at another catalog
directory that uses the same layout:

```bash
python3 validation/validate.py --catalog path/to/your/yaml
```

Expected files:

- `catalog/technology-stacks.yaml`
- `catalog/services.yaml`
- `catalog/ict-providers.yaml`
- `posture/service-posture.yaml`

## What is checked

- required top-level keys
- unique IDs for stacks, services, offerings and providers
- service IDs have 2 segments; offering IDs have 3
- offering IDs are children of their parent service ID
- `technology_stack` matches a stack `name`
- service-posture and offering-posture references exist
- ICT Provider ids in Service/Offering `providers` exist in the
  provider register (omitted `providers` is valid)
- EU AI Act offering fields appear only when `ai_act_applicable` is true
- each service has `lifecycle_state`, `version` and `valid_from`; `valid_to` is not before `valid_from`
- `service_posture` must not contain `lifecycle_state`
- characteristic names are unique per parent; values respect `allowed_values`
- provenance objects use published `confidence` / `discovery_method` enums
- Service/Offering records must not declare Service-to-Service relationship fields
- unknown fields outside the specification are rejected
- ICT Provider risk/severity is `risk_level`
- canonical posture enums (`operational_criticality`, `privacy_classification`, `provisioning_automation`)

The checker exits `0` when the catalog is valid and `1` when it is not.
