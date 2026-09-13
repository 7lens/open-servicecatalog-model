# Examples

Synthetic catalog for a fictional technology platform organization.
It is not a real estate, not a recommended taxonomy, and not a real
vendor register.

Service Offerings are part of the parent Service definition. They
are nested under `services.yaml`. They are not a separate catalog
file.

```
technology-stacks.yaml
        │  1 stack : many services
        v
services.yaml                 ← catalog (Service + nested Offerings)
        │
        │  providers[] ──────────────────► ict-providers.yaml
        │
        │  service_id
        v
service-attributes.yaml       ← Service Posture + Offering Posture
```

| File | Concept |
|------|---------|
| `technology-stacks.yaml` | Operational competency domains |
| `services.yaml` | Service definitions, with nested Service Offerings |
| `ict-providers.yaml` | Canonical third-party providers |
| `service-attributes.yaml` | Current posture |

Identifiers are consistent across the set:

- Service ID = 2 segments, for example `compute.kubernetes`
- Offering ID = 3 segments, for example `compute.kubernetes.aws`
- `providers` values are ICT Provider ids
- posture `service_id` / `offering_id` match the catalog

Framework mappings in these files are illustrative. They are not
legal advice and not evidence of compliance.

Validate from the repository root:

```bash
python3 -m pip install -r validation/requirements.txt
python3 validation/validate.py
```
