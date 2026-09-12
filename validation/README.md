# Validation

Lightweight checks for the example catalog. This is not a platform
and not a full JSON Schema compiler — it enforces the identity and
reference rules in `SPECIFICATION.md`.

## Run

From the repository root:

```bash
python3 -m pip install -r validation/requirements.txt
python3 validation/validate.py
```

PyYAML is the only dependency. Point at another catalog directory:

```bash
python3 validation/validate.py --catalog path/to/your/yaml
```

Expected files in that directory:

- `technology-stacks.yaml`
- `services.yaml`
- `service-attributes.yaml`
- `ict-providers.yaml`

## What is checked

- required top-level keys
- unique IDs for stacks, services, offerings and providers
- service IDs have 2 segments; offering IDs have 3
- offering IDs are children of their parent service ID
- `technology_stack` matches a stack `name`
- service-attribute and offering-attribute references exist
- ICT provider references exist in both directions
- EU AI Act offering fields appear only when `ai_act_applicable` is true
- basic enum membership for lifecycle, criticality and similar fields

The checker exits `0` when the catalog is valid and `1` when it is not.
