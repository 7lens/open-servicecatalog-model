# Model stress-test results

Date: 2026-09-13. Schema unchanged. Test suite in `records/` validates
with `python3 validation/validate.py --catalog _internal/investigation/records`.

This is a report of where the **frozen OSM 1.3.0 model** succeeded or
failed when fed real public provider and service facts. It is not a
redesign.

## Method

1. Locked universe: 94-row CSV (filename says 100; see D-029).
2. Deep provider research for the 19 named vendors plus GitHub, GitLab,
   Red Hat, Workday, Broadcom.
3. About seven services each for AWS, Microsoft Azure and Google Cloud;
   about two each for smaller providers.
4. Encode only class A/B facts that fit current fields. Leave C/D unset.
5. Record every mismatch in `decision_register.md`.

## What succeeded (no schema change required)

| Stress | Result |
|---|---|
| Service → Offering → ICT Provider | Worked. Capability Services with provider-specific Offerings (VMs, object storage, managed Kubernetes, relational DB) match OSM intent and the existing synthetic examples. |
| Intrinsic vs distinguishing provider | Worked. Salesforce/ServiceNow/SAP/Workday use Service-level `providers`. Hyperscaler variants use Offering-level `providers`. |
| Multiple providers on one offering | Worked. Snowflake and Databricks list platform + hosting CSP. This is the correct DORA-relevant chain signal OSM can currently hold. |
| Characteristics instead of new fields | Worked. Vendor SLA, region selectable, deployment_model, operating_model, execution_model all fit OSM-M-001. |
| Customer-dependent posture | Worked **when left empty**. Empty `offering_posture: []` is valid. The model does not force fake RTO/criticality. |
| Identity split | Worked **once we refused** a single IAM Service. Cloud authorization vs workforce IdP is representable as two Services. |
| GitHub vs Microsoft | Worked as two ICT Providers (subsidiary seller). |
| IBM vs Red Hat | Worked as two ICT Providers. Managed OpenShift on IBM Cloud points at `ibm`. |
| Self-operated offering | Worked by omitting `providers` (Kubernetes self-operated, IaC self-operated). |
| AI Act applicability without classification | Worked. `ai_act_applicable: true` on a dedicated vendor-AI Service; risk class omitted. |
| Validation | The deeply evidenced test suite validates against the frozen rules. |

OSM did **not** need new entities to catalog a representative hyperscaler
and SaaS estate, provided the cataloguer already knows the modelling
rules. That is the main positive result.

## What failed or is dangerous

| Stress | Result | Decision |
|---|---|---|
| Certification as a string list | **Fails semantically.** Encoded tokens will be over-read as estate-wide compliance. | D-001 |
| Provider `type` enum | **Awkward everywhere.** No SaaS. Cloudflare/Zscaler/Prisma Access unclassifiable without loss. Microsoft cannot be IaaS and SaaS. | D-002 |
| HQ / legal person / CTPP | **Fails grain.** `headquarters: us` on AWS/Microsoft hides EMEA CTPP entities. Alibaba cannot be Cayman+Hangzhou+Singapore. Atlassian cannot be AU+US. GitLab has no HQ. Dynatrace Boston vs Linz. | D-003, D-026 |
| `gdpr_dpa_signed` | **Wrong question.** Every hyperscaler publishes a DPA. The field asks whether a customer signed it. | D-006 |
| `audit_rights` boolean | **Too coarse.** Public DPAs are report-based. | D-007 |
| `subcontractors[]` | **Unusable as a chain.** Public lists are huge and product-specific. Applicable subset is C. | D-008 |
| Processing locations | **Wrong grain.** Provider-level `[eu, us]` is not tenant residency or DORA location of provision. `global-edge` is a fudge for Cloudflare/Zscaler. No controlled vocabulary. | D-009 |
| Contract on provider | **Wrong grain.** Microsoft has many arrangements. One `contract_ref` cannot hold them. | D-010 |
| ICT Provider provenance | **Missing.** Provider facts in this investigation live only in the matrix. | D-025 |
| Provenance per field | **Missing.** One provenance object per Service cannot attach different URLs to SLA vs definition vs ISO list. | D-030 |
| Vendor SLA vs target | **Easy to misuse.** Model can hold both if SLA is a characteristic. Posture target is the trap. | D-011 |
| Product/project names | **Schema allows bad catalogs.** Kubernetes/Docker/Postgres/Jenkins will be entered as Services unless onboarding forbids it. | D-012 |
| Operating model | **Representable only by convention** (characteristic). Easy to list a software vendor on a self-operated offering and look like managed ICT. | D-013 |
| Service-to-Service | **Intentionally impossible.** Teams→Entra, lakehouse→CSP data plane (partially via `providers[]`), API gateway→compute. Misuse of `providers[]` is the failure mode. | D-014 |
| M365 suite | **No suite entity.** Decomposition works; commercial E3/E5 bundle and shared tenant are lost. | D-015 |
| Cloud Run vs Functions | **Capability mismatch** if forced into one Service. Characteristic records the mismatch; it does not fix it. | D-017 |
| VPC dual nature | **Partial.** Can catalog as a network Service; cannot catalog as account tenancy. | D-018 |
| CRM / ERP / HCM / CMDB | **Out of scope, but estate asked.** Encoding them as Services contradicts MODEL.md. Omitting them drops rows 57–61. | D-019 |
| DORA RoI | **Cannot be OSM.** No LEI, function, S01–S19, rank, arrangement×service. Canonical mapping (`providers`, RTO/RPO, criticality, tested) is the thin slice already documented. | D-020 |
| GDPR roles | **`iso27701_pii_role` is not Art. 4.** Dual controller/processor (common M365/Azure pattern) cannot be stored. | D-021 |
| AI Act roles | **Flags only.** Cannot say deployer vs provider vs GPAI. | D-022 |
| NIST CSF | **Looks like a certification** if `nist_control_status: implemented` is populated from vendor marketing. | D-028 |

## Certification scope (worked example)

All seven researched AWS services appear on the AWS ISO certified page
as of 2026-09-01. That is class B for those seven, **not** for “AWS”.
Microsoft Azure VMs are typically in the Azure ISO certificate; GitHub
Copilot is on a different SoA; Jira Data Center is on none of Atlassian
Cloud reports. OSM `certifications[]` cannot say any of that.

## Microsoft (worked example)

One ICT Provider `microsoft` is the honest legal-seller choice and the
wrong compliance/contract grain. Splitting `microsoft-azure` /
`microsoft-365` is convenient and not a legal entity. GitHub must not
be merged. Entra is shared substrate, so an Azure/M365 split still
shares identity. OSM cannot express this without either a parent
pointer (new semantics) or external join.

## What OSM should consider changing

See the investigation report. Short version: **do not change the
schema from this investigation.** The freeze holds. The valuable
outputs are onboarding rules, documentation warnings on
`certifications`, `gdpr_dpa_signed`, `availability_target`, and
identity modelling, plus optional later additive `provenance` on ICT
Provider if reviewers want evidence on the record.

Schema growth toward DORA RoI, GDPR ROPA, or AI Act technical files
would abandon OSM’s stated size and scope.
