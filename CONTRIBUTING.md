# Contributing

Thank you for considering a contribution to **7lens OSM** (7lens Open
Service Catalog Model).

This repository is a **small public data model**. The most useful
contributions make OSM clearer, easier to validate, or easier to
adopt. The least useful contributions try to turn it into a generic
enterprise ontology.

## What to propose

Welcome:

- clarifications to the specification or README
- schema improvements that remain backwards-compatible where possible
- generic technological-service concepts that many organizations share
- better synthetic examples
- optional standards mappings, clearly labelled as reference mappings
- compatibility or compliance analysis that does not invent mappings
- validation checks and documentation

Model changes require an accepted record in [`DECISIONS.md`](DECISIONS.md).
Detailed `OSM-M-*` documents are in [`decisions/`](decisions/).
Do not add fields because another framework has them until maintainers
accept an `OSM-M-*` decision (OSM-M-004: compatibility does not mean
copying). Compatibility scope is `OSM-C-001` in that register. See
[`COMPATIBILITY.md`](COMPATIBILITY.md).

**OSM-M-007** (Complete Service Definition) is **PROPOSED**. Do not
implement its schema or model changes until it is `ACCEPTED`.

Prefer a **characteristic** (OSM-M-001) over a new core field when
the property is not needed by most adopters. OSM-M-007 (when
accepted) classifies candidates as CORE FIELD, CHARACTERISTIC,
SERVICE POSTURE, EXTERNAL CONTEXT, FRAMEWORK MAPPING, or OUT OF SCOPE.

Not in scope:

- business capabilities or business services
- application, product, digital-product, or CMDB inventory models
- Service Instance / deployed runtime objects
- Application Service or Business Service entities
- value streams, consumers, or detailed SLA objects
- ITIL or CSDM practice/process/CMDB structures
- organization or geography models
- vendor-specific product implementations
- expanding the model into an enterprise-wide ontology

Do not add Service → Service relationships unless maintainers accept
a later decision; they are outside the current OSM core (OSM-C-004,
OSM-C-005). Canonical provider association is `providers` → ICT
Provider (OSM-M-006), not a service-to-service link.

If a change would require a reader to understand a broader enterprise
model in order to use this catalog, it does not belong here.

## Design constraints

Keep 7lens OSM:

1. **Small** — add a field only when many adopters would use it.
2. **Opinionated** — two tiers (service → offering), immutable IDs.
3. **Vendor-neutral** — no required coupling to a product or cloud.
4. **Technology-service focused** — `Service` is the stable definition
   of a technological service.
5. **Understandable** — a platform engineer should be able to read
   the spec in one sitting.
6. **Machine-readable** — YAML that a validator can check.
7. **Selective** — useful semantics only; do not accumulate standards.

## Identifier rules

Do not invent additional identity schemes. Preserve:

- Service ID = 2 dot-separated segments
- Offering ID = 3 dot-separated segments
- offering prefix = parent service ID
- IDs immutable after assignment
- definition `version` does not change `id`
- `lifecycle_state` belongs on Service, not on service attributes
- characteristics have a `name`, not an OSM identifier

## Examples

Examples must be synthetic. Do not contribute a real organization's
service catalog, vendor register, contract references, account IDs,
hostnames, or internal names.

Framework mappings in examples are illustrative. Do not present them
as legal advice or as proof of compliance.

## How to submit

1. Open an issue describing the proposed change, or a pull request
   with a focused diff.
2. If the change is a model or compatibility decision, it must already
   be `ACCEPTED` in [`DECISIONS.md`](DECISIONS.md). Proposed decisions
   in [`decisions/`](decisions/) are not authority to change schema.
3. Update `SPECIFICATION.md` when a field or rule changes.
4. Update examples and `validation/validate.py` when rules change.
5. Update `COMPATIBILITY.md` and the matching file under
   `compatibility/` or `compliance/` when analysis status changes.
6. Run `python3 validation/validate.py`.

## License

By contributing, you agree that your contribution is licensed under
the Apache License, Version 2.0.
