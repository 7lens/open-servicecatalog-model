# Golden-example decision candidates

**Date:** 2026-09-13  
**Status:** Historical working notes. Several items were closed by
the 2026-09-13 compatibility implementation (OSM-C-006–C-009,
OSM-D-001–D-003). Schema remains frozen.

In particular: D-GE-002 (RDS Oracle dual `providers`) is **closed**
— AWS only on `providers[]`; Oracle is `engine` characteristic.
ITSM request types as Offerings remain forbidden (D-GE-001).

Only issues that may need an OSM semantic or schema decision.
Example-local mapping choices that do not threaten the model are in
`golden-example-findings.md`.

---

## D-GE-001 — Offering = technological variant vs requestable activity

**Question.** Is a Service Offering only a variant of a technological
service (provider, environment, operating model), or any atomic
request a consumer can raise (MFA enrolment, password reset, restore)?

**Evidence from this enterprise.** Predecessor `sec.iam` offerings are
directory lifecycle, password reset, MFA, access governance.
`storage.backup` offerings are backup vs restore. `compute.vm-*`
included `os-patching` beside cloud lifecycle.

**Current OSM.** SPECIFICATION / MODEL: “atomic requestable /
deliverable **variant**.” Examples of dimensions: environment,
location, packaging, operating model, provider. `minItems: 1`
forces a dummy offering when there is no variant.

**Why it may be insufficient.** “Requestable” and “variant” pull in
opposite directions. This estate’s predecessor used a request catalog
grain. OSM 1.3 examples (estate golden, MODEL.md) use provider grain.

**How often.** Every IAM, backup, patching, and ITSM-like source
service.

**Options.** (1) Normative text: offerings are variants only; request
types stay in ITSM. (2) Allow request-type offerings. (3) Keep
ambiguous.

**Recommendation.** (1). Document in SPECIFICATION with this estate as
evidence. No new field.

---

## D-GE-002 — `providers[]` for engine licensor vs operator

**Question.** Does `providers[]` mean every third party with a
commercial relationship to the offering, or only who delivers /
operates it?

**Evidence.** Source RDS Oracle `dora_third_party_deps: [aws, oracle]`.
AWS operates RDS; Oracle is the engine.

**Current OSM.** Multiple provider ids allowed. DORA maps to
`providers`. No rank, no role (operator vs licensor vs host).

**Why it may be insufficient.** Dual-provider pattern used for
Snowflake-on-AWS (operator + host) is not the same as RDS Oracle
(operator + engine brand). Copiers will stack brands.

**How often.** Every managed engine (RDS Oracle, WebLogic on VMs,
OpenShift on IBM Cloud in other examples).

**Options.** (1) Documentation: operator/host only; engines are
characteristics. (2) Characteristic `engine_vendor`. (3) Provider role
object — schema change, freeze break.

**Recommendation.** (1) now. Do not add a role object during freeze.

---

## D-GE-003 — Service-level `providers` when only one product exists today

**Question.** If the enterprise currently consumes only Ansible, is
Red Hat intrinsic to `auto.configuration-automation`?

**Evidence.** Golden puts `providers: [redhat]` on the Service and the
Offering. MODEL: service-level providers when intrinsic.

**Current OSM.** Optional providers on Service or Offering. No rule
for “current sole seller vs intrinsic.”

**Why it may be insufficient.** Q3 (stable Service) fails if changing
Puppet→Ansible requires editing the Service’s provider list as if the
capability changed.

**How often.** Every capability that today has one vendor.

**Options.** (1) Documentation: service-level providers only when a
seller is definitional (rare). (2) Forbid service-level providers —
schema/semantics tightening.

**Recommendation.** (1).

---

## D-GE-004 — Platform vs Kubernetes capability (OpenShift)

**Question.** Is managed OpenShift the same technological service as
managed Kubernetes?

**Evidence.** Source: separate Service `compute.openshift` with two
offerings. Golden: offering under `compute.kubernetes`.

**Current OSM.** No platform entity. Adopter judgement.

**Why it may be insufficient.** Collapsing distribution/platform
products into the upstream capability will recur (OpenShift, Tanzu,
AKS vs “Kubernetes”).

**How often.** Every Kubernetes-compatible platform in the estate.

**Options.** (1) Adopter judgement, documented. (2) Characteristic
`distribution`. (3) Separate Service when the platform is sold/operated
as more than Kubernetes API.

**Recommendation.** (1) + (3) as onboarding rule. No schema field.

---

## D-GE-005 — ICT Provider `type` for a multi-line seller

**Question.** After merging source `azure` and `microsoft`, which
`type` applies to Microsoft Corporation?

**Evidence.** Source used two rows to keep cloud-infrastructure vs
cloud-platform. OSM forbids fake legal entities (`microsoft-azure`).
Enum has no multi-value.

**Current OSM.** Single required `type`. Investigation D-002 (OPEN):
no `saas`; put edition on offerings.

**Why it may be insufficient.** Recurs for every conglomerate seller.

**How often.** Microsoft, Google, IBM/Red Hat already in this repo’s
examples.

**Options.** Reuse investigation D-002: keep coarse enum; do not split
legal entities.

**Recommendation.** Do not reopen a second decision; link D-002.

---

## D-GE-006 — Certification scope

**Question.** Can `certifications[]` on ICT Provider be published
without scoped evidence?

**Evidence.** Golden copies ISO/SOC/PCI/C5/ENS lists. No provenance
on ICT Provider (investigation D-025 OPEN).

**Current OSM.** Free-form string list. No scope object.

**Why it may be insufficient.** Golden-folder copiers treat the list
as estate compliance.

**How often.** Every provider row.

**Options.** Documentation (investigation D-001 option 1) vs scoped
object (schema).

**Recommendation.** Documentation now. Do not add a field. Repeat the
warning inside the golden example, not only in parent READMEs.

---

## D-GE-007 — Predecessor demo health records vs customer posture

**Question.** When a source catalog’s posture file is explicitly a
field-pattern demo, should OSM copy rto/rpo/PII/AI Act values?

**Evidence.** Source `service_attributes.yaml`: “REPRESENTATIVE SUBSET
… demonstrate every field and every value pattern.” Golden imported
those numbers as enterprise posture.

**Current OSM.** No “synthetic” flag on posture. Provenance
`discovery_method: imported` does not mean “demo data.”

**Why it may be insufficient.** Adopters will import CMDB/tooling
demo tenants as OSM posture.

**How often.** Any migration from a tutorial or incomplete health
file.

**Options.** (1) Onboarding rule: demo/source-example posture is
unknown. (2) Provenance confidence `low` / `unknown`. (3) Schema flag
— freeze break, unnecessary.

**Recommendation.** (1) + (2). No schema change.

---

## D-GE-008 — Characteristic `environment` meaning

**Question.** Is `environment` / `deployment_environment` a cloud
(aws/azure), a region, or a delivery stage (production/development)?

**Evidence.** Basic examples: `environment: production`. Enterprise
golden: `deployment_environment: aws`. MODEL offering example is
cloud-named (`compute.kubernetes.aws`) without that characteristic.

**Current OSM.** Characteristics are free-named. No canonical
environment vocabulary.

**Why it may be insufficient.** Same word, three grains, three
example catalogs.

**How often.** Every multi-cloud and multi-stage estate.

**Options.** (1) Document three distinct characteristic names
(`delivery_stage`, cloud via `providers[]`, region via
`region_selectable`). (2) Canonical characteristic names in SPEC — still
not a new core field.

**Recommendation.** (1).

---

## D-GE-009 — Mandatory Offering when there is no variant

**Question.** Must every Service have an Offering even when the
capability has a single unvaried deliverable?

**Evidence.** `sec.secrets.secrets-mgmt`, `auto.aiops.aiops`. Schema
`minItems: 1`.

**Current OSM.** At least one offering required.

**Why it may be insufficient.** Forces tautological offerings that
copiers treat as a modelling pattern.

**How often.** Intrinsic single-deliverable services.

**Options.** (1) Keep minItems; document dummy offering. (2) Allow
zero offerings — schema change.

**Recommendation.** (1) for freeze. Revisit only if dummy offerings
prove systematically misleading.

---

Not duplicated here: investigation D-001…D-030 remain OPEN and still
apply (certification scope, DPA execution, SLA vs target, IAM split,
provider provenance, OSM ≠ DORA RoI).
