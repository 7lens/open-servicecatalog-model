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
- schema improvements that remain backwards-compatible
- generic technological-service concepts that many organizations share
- better examples (synthetic basics, or anonymized reference-estate records)
- optional standards mappings, clearly labelled as reference mappings
- compatibility analysis that does not invent mappings
- validation checks and documentation

The current model is the public product. Do not add a field because
another framework uses a different name. If OSM already represents
the concept, reuse that field and document a mapping.

Prefer a **characteristic** over a new core field when the property
is not needed by most adopters.

Model changes require maintainer agreement and an accepted
architectural decision. Do not treat a pull request as authority to
change the schema.

Not in scope:

- business capabilities or business services
- application, product, digital-product, or CMDB inventory models
- Service Instance / deployed runtime objects
- Application Service or Business Service entities
- value streams, consumers, or detailed SLA objects
- ITIL or CSDM practice/process/CMDB structures
- TM Forum Candidate, Category, CFS, RFS, or Service Inventory
- DORA RoI, LEI, CIF, contractual Arrangement, or incident feed
- GDPR RoPA, legal basis, DPO, SCCs, or processing-activity entities
- ISO SoA, control implementation, or PIMS processing structures
- NIST Profiles, Categories, Tiers, or control catalogues
- EU AI Act GPAI, deployer/provider legal roles, EU database, or technical-file structures
- organization or geography models
- vendor-specific product implementations
- expanding the model into an enterprise-wide ontology
- first-class Service → Service relationships
- a second provider relationship beside `providers`
- a second provider risk/severity field beside `risk_level`
- provider-role fields or a generic vendor/tool inventory
- framework-prefixed copies of canonical fields (`dora_rto`, …)

See `SPECIFICATION.md` §10 for **External Concepts — Intentionally
Outside OSM**.

If a change would require a reader to understand a broader enterprise
model in order to use this catalog, it does not belong here.

## Design constraints

Keep 7lens OSM:

1. **Small** — add a field only when many adopters would use it.
2. **Opinionated** — two tiers (service → offering), immutable IDs.
3. **Vendor-neutral** — no required coupling to a product or cloud.
4. **Technology-service focused** — Service is the stable definition
   of a technological service.
5. **Understandable** — a platform engineer should be able to read
   the spec in one sitting.
6. **Machine-readable** — YAML that a validator can check.
7. **Selective** — useful semantics only; do not accumulate standards.
8. **One concept** — one canonical parameter. Map frameworks to it.

## Identifier rules

Preserve:

- Service ID = 2 dot-separated segments
- Offering ID = 3 dot-separated segments
- offering prefix = parent service ID
- IDs immutable after assignment
- definition `version` does not change `id`
- `lifecycle_state` belongs on Service, not on service posture
- characteristics have a `name`, not an OSM identifier

## Examples

There are three public example layers:

- **Basic examples** (`examples/catalog/`, `examples/posture/`) are
  synthetic schema tutorials.
- **Reference estate** (`examples/reference-estate/`) is a researched,
  anonymized catalog using well-known public providers.
- **Reference enterprise** (`examples/reference-enterprise/`) is a
  predecessor enterprise catalog onboarded onto current OSM.

Do not contribute a real organization's service catalog, vendor
register, contract references, account IDs, hostnames, or internal
names. Public provider facts are allowed; customer contracts, signed
DPA flags, RTO/RPO and risk scores are not to be filled in from
imagination.

Framework mappings in examples are illustrative. They are not legal
advice and not proof of compliance.

## How to submit

1. Open an issue describing the proposed change, or a pull request
   with a focused diff.
2. Update `SPECIFICATION.md` when a field or rule changes.
3. Update examples and `validation/validate.py` when rules change.
4. Update [`models/`](models/) or [`compliance/`](compliance/) when
   those explanations change.
5. Run `python3 validation/validate.py`.

Maintainer commits are authored as GitHub user **Podwarack**.
Do not add `Co-authored-by: Cursor` or other AI attribution trailers.

## License

By contributing, you agree that your contribution is licensed under
the Apache License, Version 2.0.

Maintainers keep the development decision register under
`_internal/decisions/`. That archive is not public documentation.
