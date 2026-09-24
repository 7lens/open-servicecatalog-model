# OSM tooling backlog

Tools sit **on** OSM 1.3.0. They do not become OSM.

This backlog is the implementation queue for a proof of value. It does
not change `schema/`, `SPECIFICATION.md`, or `MODEL.md`. Code lives in
`tools/`. Runtime is Python 3 plus PyYAML.

Canonical catalog layout (read or produced):

```text
catalog/technology-stacks.yaml
catalog/services.yaml
catalog/ict-providers.yaml
posture/service-posture.yaml
```

Sparse honest catalogs beat complete-looking fiction. A tool that
imports a CMDB as Services, or auto-fills compliance from vendor
marketing, is out of scope.

---

## Epic 1 — `osm-lint`

**ID:** `OSM-TOOL-001`
**Title:** Semantic Guardrail CLI
**Status:** MVI in `tools/osm_lint/`
**Depends on:** `tools/osm_common/` loader

### Target persona and buying situation

**Persona:** Enterprise Architect / Principal Platform Architect.

**Buying situation:** The organisation has decided OSM is the
canonical technological-service layer. Architects can already run
`validation/validate.py` (shape and references). Catalogues still
validate while encoding products as Services, request types as
Offerings, or vendor marketing as compliance. The architect needs a
gate that fails those catalogues before they become “the source of
truth”.

### Core value proposition and JTBD

**JTBD:** When I review or accept an OSM catalog, I need to catch
semantic modelling anti-patterns, naming mistakes, and unevidenced
compliance claims so that a structurally valid YAML file cannot pass
as a correct OSM catalog.

**Value:** Deterministic, file-and-line findings with corrective
advice. Complements — does not replace — `validation/validate.py`.

### Inputs and outputs

| | |
|--|--|
| **Inputs** | Directory containing an OSM catalog (`--catalog <path>`). |
| **Outputs** | Deterministic CLI report (text or JSON): rule id, severity, file path, line number, entity id, message, advice. |
| **Exit codes** | `0` clean · `1` semantic errors · `2` warnings only |

### Enforced architectural constraints (§10 anti-patterns)

| Rule | What to block | Advice the tool must give |
|------|----------------|---------------------------|
| **10.1** | Product, project, or suite used as a Service (`compute.eks`, `compute.aks`, service named “S3”) | Name the capability (`compute.kubernetes`, `storage.object-storage`) and move the product to an Offering |
| **10.2** | Request-catalog / ITSM items as Offerings (`password-reset`, `mfa-request`, `ticket`, `provisioning`) | Offerings are technological variants, not request types |
| **10.3** | Identity conflation: one Service mixing cloud resource authorization (AWS IAM) and workforce IdP (Entra / Okta) | Split into distinct Services |
| **10.4** | Vendor towers as Technology Stacks (`aws`, `azure`, `m365`) | Stacks are adopter competency domains |
| **10.7** | Characteristic that duplicates `providers[]` (`deployment_environment: aws` when `providers: [aws]`) | `providers[]` is the cloud/seller dimension |
| **10.8** | Service-level `providers` when the seller is not intrinsic to the capability | Put distinguishing sellers on Offerings |
| **10.10** | Vendor SLA copied into posture `availability_target` | Vendor SLA is a characteristic; `availability_target` is the enterprise expectation |
| **10.12** | `gdpr_dpa_signed: true` without high-confidence evidence; `nist_control_status: implemented` without high-confidence provenance and `evidence_reference` | Unknown is better than invented compliance |

Do **not** invent OSM fields. Do **not** auto-populate compliance.

### Acceptance criteria

**10.1 product-as-service**

- Given a service whose id segment or name is a known product token (`eks`, `aks`, `s3`, …)
- When `osm-lint` runs
- Then it reports an **error** `OSM-LINT-10.1` at that service’s line, suggesting the capability id and an Offering for the product

**10.2 request-catalog offering**

- Given an offering whose slug or name contains `request`, `ticket`, `reset`, `mfa`, or `provisioning`
- When `osm-lint` runs
- Then it reports an **error** `OSM-LINT-10.2`

**10.3 identity conflation**

- Given one service whose offerings include both a cloud-authorization product (e.g. AWS IAM) and a workforce IdP (e.g. Entra / Okta)
- When `osm-lint` runs
- Then it reports an **error** `OSM-LINT-10.3`
- And a catalog that splits `identity.directory-idp` from `identity.cloud-authorization` does not trigger the rule

**10.4 vendor-tower stack**

- Given a stack id or name `aws`, `azure`, or `m365`
- When `osm-lint` runs
- Then it reports an **error** `OSM-LINT-10.4`

**10.7 redundant characteristic**

- Given `providers: [aws]` and a characteristic whose name/value restates that seller
- When `osm-lint` runs
- Then it reports a **warning** `OSM-LINT-10.7`

**10.8 provider placement**

- Given service-level `providers` on a multi-vendor capability (e.g. Kubernetes) while offerings already distinguish sellers
- When `osm-lint` runs
- Then it reports a **warning** `OSM-LINT-10.8`
- And a single-seller SaaS service (e.g. Jira with only Atlassian) is not flagged as non-intrinsic

**10.10 vendor SLA as target**

- Given posture `availability_target` equal to an offering `vendor_availability_sla` value
- When `osm-lint` runs
- Then it reports a **warning** (or **error** on exact copy) `OSM-LINT-10.10`
- And an enterprise-declared target with high-confidence provenance is not flagged merely because a vendor SLA string happens to contain a similar percentage

**10.12 unevidenced compliance**

- Given `gdpr_dpa_signed: true` on an ICT Provider (no provenance field exists on that entity)
- When `osm-lint` runs
- Then it reports an **error** `OSM-LINT-10.12`
- Given offering posture `nist_control_status: implemented` without `confidence: high` and `evidence_reference`
- Then it reports an **error** `OSM-LINT-10.12`

**Golden regression**

- Given `examples/reference-enterprise/golden-example` or `examples/reference-estate/golden-example`
- When `osm-lint` runs
- Then the exit code is `0`

**Determinism**

- Given the same catalog
- When `osm-lint` runs twice
- Then the report order (path, line, rule id, entity id) is identical

### Smallest usable slice (MVI)

CLI over a catalog directory; the eight rules above; text report with
paths and line numbers; JSON optional; exit codes `0/1/2`. No UI.
No auto-fix that rewrites modelling judgement.

---

## Epic 2 — `osm-query`

**ID:** `OSM-TOOL-002`
**Title:** Architectural Query and Governance Engine
**Status:** MVI in `tools/osm_query/`
**Depends on:** `tools/osm_common/` loader

### Target persona and buying situation

**Persona:** IT Governance / Compliance & Security Officer, and
Enterprise Architect.

**Buying situation:** A correct (or at least honest) OSM catalog
exists as YAML. The officer cannot grep their way to “where is AWS
concentration?” or “which critical services have no RTO?”. They will
over-read mapping fields as certification unless the tool labels them
as locators.

### Core value proposition and JTBD

**JTBD:** When I need a governance answer from the catalog, I want
provider concentration, resilience gaps, and framework locators as
tables I can trust, without opening raw YAML and without the tool
claiming the estate is compliant.

**Value:** The same catalog, asked different questions. Sparse
unknowns stay visible.

### Inputs and outputs

| | |
|--|--|
| **Inputs** | Validated OSM catalog directory (`--catalog <path>`). |
| **Outputs** | ASCII table (default), Markdown, or JSON. Optional `--output` file. |

Sub-commands:

1. `gaps` — missing `accountable`; critical services lacking RTO/RPO;
   posture records lacking provenance
2. `providers` — offerings grouped by legal ICT Provider
   (provider, offering count, stacks affected)
3. `compliance --framework {dora|iso27001|nist}` — mappings,
   `resilience_tested`, and provider dependencies, labelled as
   locators not certification

### Enforced architectural constraints (§10 anti-patterns)

- Do not fill RTO, criticality, or DPA flags from vendor marketing.
- Do not treat `certifications[]` as estate compliance.
- Do not present ISO/NIST/DORA locators as an attestation.
- Do not invent Service-to-Service graphs.
- Reverse provider → service links are derived from `providers[]` only.

### Acceptance criteria

**gaps**

- Given services with empty `accountable`
- When `osm-query gaps` runs
- Then those service ids appear under missing accountable
- Given a service with `operational_criticality: critical` and null
  `rto`/`rpo` on offering posture (or no offering posture rows)
- Then those ids appear under critical missing RTO/RPO
- Given a posture record with no `provenance`
- Then it appears under posture missing provenance
- And services with no posture record are **not** required to have
  provenance (sparse catalogs are valid)

**providers**

- Given offerings that list `aws` and/or inherit a service-level
  provider
- When `osm-query providers` runs
- Then each legal seller has a count of underpinned offerings and
  the distinct stacks those offerings sit in
- And an offering with `[snowflake, aws]` increments both providers
- And results are sorted by offering count descending, then provider id

**compliance**

- Given `--framework dora`
- When `osm-query compliance` runs
- Then the report lists provider linkage, RTO/RPO, criticality, and
  `resilience_tested` as **signals**, with a header that OSM is not
  the DORA Register of Information
- Given `--framework iso27001` or `nist`
- Then only existing mapping fields are shown; missing values stay
  empty/unknown; `nist_control_status: implemented` is labelled as an
  OSM assessment signal, not a CSF object

**format**

- Given `--format json` or `markdown`
- Then output is valid JSON / GitHub-flavoured Markdown tables
- And key/row order is deterministic

### Smallest usable slice (MVI)

Three sub-commands, table/JSON/Markdown, no dashboards, no GRC
workflow, no evidence vault.

---

## Epic 3 — `osm-context`

**ID:** `OSM-TOOL-003`
**Title:** Deterministic Context Exporter for AI Agents
**Status:** MVI as `osm-query export-context` (`tools/osm_query/context_export.py`)
**Depends on:** `tools/osm_common/` loader

The implementation tree keeps a single `osm_query` CLI. The exporter
is the Epic 3 deliverable.

### Target persona and buying situation

**Persona:** AI Agent Builder / Platform Automation Engineer.

**Buying situation:** Agents need a bounded, machine-readable picture
of technological services. Feeding raw YAML (or a CMDB dump) causes
hallucinated ownership, inferred RTO, and fake compliance. The builder
wants one JSON file that is stable across runs.

### Core value proposition and JTBD

**JTBD:** When I attach enterprise technology context to an agent, I
need a single JSON matrix of services, variants, lifecycle, and
operational boundaries, with unknown facts marked `UNKNOWN` rather
than omitted or guessed.

**Value:** Deterministic operational boundaries. Unassessed framework
fields are stripped so agents cannot over-read them.

### Inputs and outputs

| | |
|--|--|
| **Inputs** | OSM catalog directory (`--catalog <path>`). |
| **Outputs** | One JSON document (`--output osm-agent-context.json`). |

Payload contains:

- OSM version (`1.3.0`)
- Services: id, name, stack, lifecycle, accountable, providers
- Offerings: id, name, providers
- Operational boundary fields, always present for the agent contract,
  with `"UNKNOWN"` when unset / `null` / `not-assessed`
- Provider register (id, name, type) without contract fiction

### Enforced architectural constraints (§10 anti-patterns)

- Do not infer RTO, criticality, or lifecycle onto offerings.
- Do not copy vendor SLA into `availability_target`.
- Strip unassessed ISO/NIST/GDPR/AI Act mapping fields from the
  agent payload (they are locators, not agent facts).
- Do not emit `null`; use `"UNKNOWN"` for the contracted operational
  keys; omit stripped mapping keys entirely.
- Deterministic key ordering (`sort_keys`) and sorted entity lists.

### Acceptance criteria

- Given a catalog where some services have no posture
- When `export-context` runs
- Then those services still appear, and posture keys are `"UNKNOWN"`
- Given `privacy_classification: not-assessed` or `rto: null`
- Then the JSON value is `"UNKNOWN"`
- Given ISO/NIST mapping fields present on posture
- Then they are **absent** from the agent JSON
- Given the same catalog twice
- Then the bytes of pretty-printed JSON (sorted keys) are identical
- Given `--output file.json`
- Then the file is valid JSON with `osm_version: "1.3.0"`

### Smallest usable slice (MVI)

One command, one JSON file, no agent runtime, no recommendations.

---

## Epic 4 — `osm-scaffold`

**ID:** `OSM-TOOL-004`
**Title:** Onboarding Wizard
**Status:** MVI in `tools/osm_scaffold/`
**Depends on:** `tools/osm_common/` semantics, golden examples, `models/`, `compliance/`

### Target persona and buying situation

**Persona:** Principal Manager, Platform Lead, or Head of Architecture.
Technology Stack Owners work under that accountability. Cloud
operations and FinOps consume the catalog; they do not decide the
taxonomy.

**Buying situation:** Establishing OSM is principal modelling work:
what is a Service versus a product, how stacks are cut, which legal
sellers belong on Offerings, which frameworks apply as locators.
The wizard must let that owner pause, review, and resume.

### Core value proposition and JTBD

**JTBD:** When I establish the enterprise technological-service
catalog, I want the same onboarding whether I read the docs or ask
a coding assistant: explain OSM as the lock-in-free canonical model,
ask my technology stacks then compliance locators, and stop at a
draft of Stacks and Services I am comfortable starting with.

**Value:** Own the semantics under `servicecatalog/`. Constant board
(“this is what we currently have”). Flawless `:pause` / `--resume`.
No invented posture.

### Inputs and outputs

| | |
|--|--|
| **Inputs** | Interactive TTY wizard (default → `servicecatalog/`). Checkpoint `.osm-scaffold-state.json`. Optional `--config` one-service YAML for automation. |
| **Outputs** | OSM 1.3.0 YAML in `servicecatalog/catalog/` and empty `servicecatalog/posture/service-posture.yaml`. |

Pipeline: stacks → compliance locators → golden/custom draft →
refine until comfortable → write YAML (checkpoint **kept**).
`:view` and `:pause` at every prompt. `--resume` summarises what
exists, where it is stored, and proposes new stacks, new services,
or more from the golden examples. `--status` prints the board.

### Enforced architectural constraints (§10 anti-patterns)

- Refuse product-token service slugs/names (same dictionary as 10.1).
- Refuse ITSM offering slugs (same tokens as 10.2).
- Refuse vendor-tower stack ids and vendor domain labels (same tokens as 10.4).
- Require 2-segment service id `{stack_id}.{service_slug}` and
  3-segment offering id `{service_id}.{offering_slug}`.
- Require at least one Offering.
- Do not invent posture, DPA, certifications, or RTO.
- Do not create a second provider relationship.
- Framework selection only exposes existing optional mapping fields.

### Acceptance criteria

- Given interactive or `--config` input for stack Compute, service
  slug `kubernetes`, offering slug `aws-eks`, provider `aws`
- When `osm-scaffold` runs with `--output <dir>`
- Then it writes valid YAML whose service id is `compute.kubernetes`
  and offering id is `compute.kubernetes.aws-eks`
- And `python3 validation/validate.py --catalog <dir>` exits 0
- Given service slug `eks`
- Then it refuses to emit a catalog (error, no YAML)
- Given offering slug `password-reset`
- Then it refuses
- Given stack id `aws`
- Then it refuses
- Given a config with zero offerings
- Then it refuses
- Given `--output` pointing at an existing catalog
- Then it merges new records and rejects duplicate ids
- Given `:pause` during onboarding
- Then a checkpoint is written and `--resume` continues from that draft
- Given a finished phase-1 draft
- Then YAML exists under `servicecatalog/` **and** the checkpoint remains
  so they can add stacks, add services, or pull golden examples later
- Given catalog YAML but no checkpoint
- Then `--resume` hydrates from disk, shows the board, and proposes continue

### Smallest usable slice (MVI)

Onboarding wizard + checkpoint + golden draft + `--config` path.
No CMDB import. No spreadsheet upload.

---

## Implementation notes

| Tool | Module | CLI |
|------|--------|-----|
| Shared loader | `tools/osm_common/` | — |
| `osm-lint` | `tools/osm_lint/` | `python3 -m tools.osm_lint.cli --catalog <path>` |
| `osm-query` | `tools/osm_query/` | `python3 -m tools.osm_query.cli {gaps\|providers\|compliance\|export-context} --catalog <path>` |
| `osm-scaffold` | `tools/osm_scaffold/` | `python3 -m tools.osm_scaffold.cli` · `--resume` · `--config` |

Tests: `tools/tests/`. Golden catalogs under `examples/` must stay
green for `osm-lint`.
