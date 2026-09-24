# OSM tooling

Tools sit **on** frozen OSM 1.3.0. They read and produce the standard
catalog layout. They do not change `schema/`, `SPECIFICATION.md`, or
`MODEL.md`.

```text
catalog/technology-stacks.yaml
catalog/services.yaml
catalog/ict-providers.yaml
posture/service-posture.yaml
```

Runtime: Python 3 and PyYAML. No other dependencies.

```bash
python3 -m pip install -r tools/requirements.txt
```

Run every command from the repository root.

Structural validation remains `python3 validation/validate.py --catalog <path>`.
`osm-lint` is the semantic layer on top of that.

Backlog and acceptance criteria: [`BACKLOG.md`](../BACKLOG.md).

---

## osm-lint

Semantic guardrail. Exit codes: `0` clean, `1` errors, `2` warnings only.

```bash
python3 -m tools.osm_lint.cli --catalog examples/reference-enterprise/golden-example
python3 -m tools.osm_lint.cli --catalog examples/reference-estate/golden-example
python3 -m tools.osm_lint.cli --catalog path/to/catalog --format json
```

Rules (usability brief §10):

| Id | Severity | Catches |
|----|----------|---------|
| OSM-LINT-10.1 | error | Product/project/suite used as a Service |
| OSM-LINT-10.2 | error | ITSM request slugs used as Offerings |
| OSM-LINT-10.3 | error | Cloud IAM and workforce IdP on one Service |
| OSM-LINT-10.4 | error | Vendor-tower Technology Stacks |
| OSM-LINT-10.7 | warning | Characteristic duplicating `providers[]` |
| OSM-LINT-10.8 | warning | Service-level `providers` on a non-intrinsic capability |
| OSM-LINT-10.10 | error/warning | Vendor SLA copied into `availability_target` |
| OSM-LINT-10.12 | error | Unevidenced `gdpr_dpa_signed: true` or `nist_control_status: implemented` |

---

## osm-query

Governance questions without grepping YAML. Does not attest compliance.

```bash
python3 -m tools.osm_query.cli gaps --catalog examples/reference-estate/golden-example
python3 -m tools.osm_query.cli providers --catalog examples/reference-estate/golden-example
python3 -m tools.osm_query.cli providers --catalog path/to/catalog --format json
python3 -m tools.osm_query.cli compliance --framework dora --catalog path/to/catalog
python3 -m tools.osm_query.cli compliance --framework iso27001 --catalog path/to/catalog --format markdown
python3 -m tools.osm_query.cli compliance --framework nist --catalog path/to/catalog
```

`--format` is `table` (default), `markdown`, or `json`. `--output FILE` writes the report.

`gaps` only inspects posture that exists. Services with no posture record
are valid sparse catalog rows, not missing-provenance failures.

---

## osm-context (`export-context`)

Deterministic JSON for AI agents. Unassessed operational fields are
`"UNKNOWN"`. ISO/NIST/GDPR mapping fields are stripped.

```bash
python3 -m tools.osm_query.cli export-context \
  --catalog examples/reference-estate/golden-example \
  --output osm-agent-context.json
```

---

## osm-scaffold

Onboarding for whoever sees that not owning enterprise semantics is a
problem in an AI future (ideal: Principal Manager, Platform Lead, Head
of Architecture). Same protocol as [`ONBOARDING.md`](../ONBOARDING.md):
own the semantics, grow a lock-in-free ontology, ask stacks then
compliance, first draft the adopter is comfortable starting with.
Writes under `servicecatalog/` (standard OSM `catalog/` + `posture/`
layout).

```bash
python3 -m tools.osm_scaffold.cli
python3 -m tools.osm_scaffold.cli --status
python3 -m tools.osm_scaffold.cli --resume
python3 -m tools.osm_lint.cli --catalog servicecatalog
```

Phase 1: technology stacks → compliance locators → golden-or-custom
draft → refine until comfortable → write YAML. Checkpoint is **kept**
so continue works.

At any prompt:

- `:view` / `:status` — the board (stacks, services, compliance, path)
- `:pause` / `:save` — write `servicecatalog/.osm-scaffold-state.json` and exit

`--resume` loads that checkpoint **or** hydrates from catalog YAML
already on disk, summarises what is configured, and proposes: new
stack, new service, more from the golden examples, write YAML, or
pause again. `--fresh` discards the checkpoint. `--status` prints the
board without changing anything.

The session refuses vendor-tower stacks, product-named Services, and
ITSM offering slugs. It does not invent posture.

A one-service non-interactive path remains for automation:

```bash
python3 -m tools.osm_scaffold.cli --config scaffold.yaml --output ./my-catalog
python3 validation/validate.py --catalog ./my-catalog
```

Example `scaffold.yaml`:

```yaml
stack:
  id: compute
  name: Compute
  description: Compute technological services.
service:
  slug: kubernetes
  name: Managed Kubernetes
  description: Kubernetes clusters as a technological service.
  accountable: Service Owner
offerings:
  - slug: aws-eks
    name: Amazon EKS
    provider_id: aws
providers:
  - id: aws
    name: Amazon Web Services, Inc.
    type: cloud-infrastructure
    substitutability: low
```

---

## Tests

From the repository root:

```bash
python3 -m unittest discover -s tools/tests -t .
```
