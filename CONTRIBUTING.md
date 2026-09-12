# Contributing

Thank you for considering a contribution to the 7lens Open Services
Data Model.

This repository is a **small public model**. The most useful
contributions make the model clearer, easier to validate, or easier
to adopt. The least useful contributions try to turn it into a
generic enterprise ontology.

## What to propose

Welcome:

- clarifications to the specification or README
- schema improvements that remain backwards-compatible where possible
- generic technological-service concepts that many organizations share
- better synthetic examples
- optional standards mappings, clearly labelled as reference mappings
- validation checks and documentation

Not in scope:

- business capabilities or business services
- application, product, or CMDB inventory models
- organization or geography models
- vendor-specific product implementations
- expanding the model into an enterprise-wide ontology

If a change would require a reader to understand a broader enterprise
model in order to use this catalog, it does not belong here.

## Design constraints

Keep the model:

1. **Small** — add a field only when many adopters would use it.
2. **Opinionated** — two tiers (service → offering), immutable IDs.
3. **Vendor-neutral** — no required coupling to a product or cloud.
4. **Technology-service focused** — `Service` means technological service.
5. **Understandable** — a platform engineer should be able to read
   the spec in one sitting.
6. **Machine-readable** — YAML that a validator can check.

## Identifier rules

Do not invent additional identity schemes. Preserve:

- Service ID = 2 dot-separated segments
- Offering ID = 3 dot-separated segments
- offering prefix = parent service ID
- IDs immutable after assignment

## Examples

Examples must be synthetic. Do not contribute a real organization's
service catalog, vendor register, contract references, account IDs,
hostnames, or internal names.

Framework mappings in examples are illustrative. Do not present them
as legal advice or as proof of compliance.

## How to submit

1. Open an issue describing the proposed change, or a pull request
   with a focused diff.
2. Update `SPECIFICATION.md` when a field or rule changes.
3. Update examples and `validation/validate.py` when rules change.
4. Run `python3 validation/validate.py`.

## License

By contributing, you agree that your contribution is licensed under
the Apache License, Version 2.0.
