# OSM Model Stress-Test Decision Register

Investigation date: 2026-09-13. Status `OPEN` means a human reviewer must
decide. Nothing here is implemented. The architecture remains frozen.

| ID | Topic | Kind | Recommendation | Status |
|---|---|---|---|---|
| D-001 | Certification scope vs `certifications[]` | schema or documentation | Do not treat the string list as scoped evidence. Prefer documentation now; structured scope only if reviewers need it | OPEN |
| D-002 | ICT Provider `type` has no SaaS / multi-edition value | schema | Keep the coarse enum. Put edition on Offering characteristics | OPEN |
| D-003 | Legal entity ≠ contracting party ≠ DORA CTPP ≠ HQ | schema | Out of core OSM unless RoI feed is in scope. Document the collapse | OPEN |
| D-004 | No LEI / EUID | out of scope or schema | Keep out of OSM if RoI stays external | OPEN |
| D-005 | Microsoft (and similar parents) as one vs many ICT Providers | semantics | One provider per legal seller; GitHub/Red Hat as subsidiaries when they sell | OPEN |
| D-006 | `gdpr_dpa_signed` ≠ “DPA exists” | schema or documentation | Document: leave unset unless a named customer signed. Optional `dpa_published` is a new field — do not add now | OPEN |
| D-007 | `audit_rights` boolean vs report-based DPA audits | schema | Leave null. Boolean cannot express “reports under NDA, on-site only if insufficient” | OPEN |
| D-008 | `subcontractors[]` cannot hold chain, rank or LEI | out of scope | Keep names-only. Put list URL in provenance. Do not freeze partial lists | OPEN |
| D-009 | `data_processing_locations` provider grain | grain | Provider list is a capability map only. Actual residency is C | OPEN |
| D-010 | Contract fields live on the provider, not arrangement × service | grain | Keep. Join to an external contract system | OPEN |
| D-011 | Vendor SLA vs `availability_target` | documentation | SLA is a characteristic. Never copy into posture targets | OPEN |
| D-012 | Project / runtime / product vs Service | documentation | Do not catalog Kubernetes, Docker, PostgreSQL, Jenkins as Services | OPEN |
| D-013 | Operating model is not first-class | documentation | Use Offering characteristic `operating_model`. Schema field not required | OPEN |
| D-014 | Service → Service dependency forbidden | out of scope | Do not misuse `providers[]` for Entra→Teams. Keep the prohibition | OPEN |
| D-015 | Product suite vs technological services (M365) | documentation | Decompose suites. No suite entity | OPEN |
| D-016 | AWS IAM ≠ Entra ID ≠ Cloud IAM | documentation | Two identity Services, not one | OPEN |
| D-017 | Cloud Run vs Lambda vs Functions | documentation | Do not force CaaS into a functions Service | OPEN |
| D-018 | VPC as tenancy boundary vs requestable service | semantics | Catalog as virtual-network Service; note the dual nature | OPEN |
| D-019 | CRM / ERP / HCM / CMDB vs technological service | out of scope | Do not catalog applications or CMDB inventory | OPEN |
| D-020 | DORA Register of Information facts missing | out of scope | OSM is not the RoI. Map only canonical fields already specified | OPEN |
| D-021 | GDPR controller/processor per activity | out of scope | `iso27701_pii_role` is not Art. 4. Do not treat OSM as ROPA | OPEN |
| D-022 | EU AI Act provider / deployer / GPAI | out of scope | Keep flags only. Do not classify customer risk | OPEN |
| D-023 | Dual-provider offerings (Snowflake, Databricks) | documentation | `providers[]` already allows multiple ids. Use it | OPEN |
| D-024 | `substitutability` / `concentration_risk` / `risk_level` grain | documentation | Market observation ≠ customer risk. `risk_level` stays C | OPEN |
| D-025 | ICT Provider has no `provenance` | schema | Evidence for provider facts cannot attach to the record | OPEN |
| D-026 | `headquarters` is one ISO country | documentation | Record dual-HQ and Cayman/Hangzhou/Singapore in notes, not by inventing codes | OPEN |
| D-027 | IBM / Red Hat / HashiCorp seller identity | documentation | Separate ICT Providers when they sell; IBM for HCP after 2025-09-01 | OPEN |
| D-028 | NIST CSF mapping looks like certification | documentation | NIST does not certify. Keep mapping labels | OPEN |
| D-029 | Reference CSV is 94 rows, filename says 100 | process | Do not pad. Treat 94 as the locked universe | OPEN |
| D-030 | Provenance is per-record, not per-field | schema | Matrix carries per-fact evidence. Acceptable for v1 | OPEN |

## Rules used

- Open a decision only when researched evidence exposes a real problem or ambiguity.
- Do not turn a vendor-specific quirk into a canonical OSM concept without testing it across multiple providers.
- Do not add a schema field merely because one example is awkward.
- Distinguish missing semantics from intentionally out-of-scope semantics.

---

## D-001 — Certification scope vs `certifications[]`

**Problem.** Provider ISO/SOC/PCI claims are scoped to named services, regions, editions and certificate dates. OSM stores a free-form string list on the ICT Provider.

**Evidence.** AWS ISO certified page (updated 2026-09-01) lists in-scope services and exclusions. Spring 2026 SOC covers 188 services. Microsoft splits Azure+Dynamics vs Office 365 vs Azure DevOps vs GitHub audits. Google ISO 27001 page enumerates governed services. Atlassian Cloud ISO does not cover Data Center. GitLab ISO covers GitLab.com and Dedicated, not Self-Managed. Oracle states attestations are generally service- and often region-specific.

**Current treatment.** `ict_provider.certifications: [iso27001, soc2-type2, …]`.

**Why insufficient.** Writing `iso27001` on AWS or Microsoft will be read as “every service in every region is certified.” That is the exact error this investigation forbids.

**Options.** (1) Documentation and onboarding only. (2) Move badges to provenance text. (3) Add a scoped certification object (standard, version, legal entity, services, regions, certificate id, valid_to).

**Recommendation.** (1) now. (3) only if reviewers want OSM to hold compliance evidence rather than pointers.

**Impact.** Schema if (3). Documentation if (1). Canonical-model impact is high if adopters treat the list as proof.

**Kind.** Schema or documentation.

---

## D-002 — ICT Provider `type` enum

**Problem.** Closed enum has no `saas`. Cloudflare, Zscaler and Prisma Access sit between `network-provider` and `cloud-platform`. Microsoft is IaaS and SaaS. CrowdStrike Falcon Complete is a managed service on a SaaS platform.

**Evidence.** Encoded 24 providers; every SaaS vendor stressed the enum. Schema `ict-provider.yaml` enum.

**Current treatment.** Single required `type`.

**Why insufficient.** One token cannot describe a multi-edition vendor. It is still useful as a coarse org class.

**Options.** (1) Keep enum; put `deployment_model` / `service_pattern` on Offerings. (2) Add `saas`. (3) Allow multiple types.

**Recommendation.** (1). Adding `saas` would still fail for Atlassian Cloud vs Data Center on the same legal entity.

**Impact.** Documentation. No freeze break required.

**Kind.** Schema (rejected for now) + documentation.

---

## D-003 / D-004 — Legal entity, contracting party, CTPP, LEI

**Problem.** OSM has `name` + `headquarters` (ISO country). DORA RoI and vendor legal pages need legal person, contracting party by account country, designated CTPP name, and LEI/EUID.

**Evidence.** ESA CTPP list 18 Nov 2025: Amazon Web Services EMEA SARL; Microsoft Ireland Operations Limited; Oracle Nederland B.V.; International Business Machine Corporation; SAP SE. AWS contracting-party page lists many local sellers. Alibaba: Cayman parent, Hangzhou PRC operator, Singapore international default contractor. ITS 2024/2956 Art. 2(5)–(6).

**Current treatment.** One name string. No LEI. No contracting-party table. No CTPP flag.

**Why insufficient.** A row named “AWS” with `headquarters: us` hides that the designated CTPP is a Luxembourg company. A row named “Microsoft” hides MIOL.

**Options.** (1) Intentionally out of scope; store LEI/CTPP elsewhere and join on `id`. (2) Add optional `legal_name`, `contracting_entities[]`, `lei`, `dora_ctpp`.

**Recommendation.** (1) unless OSM is explicitly scoped to feed the RoI. Current `compliance/DORA.md` already says OSM is not a DORA register.

**Impact.** Large schema if (2). Out of scope if (1).

**Kind.** Out of scope (preferred) or schema.

---

## D-005 — One ICT Provider per legal seller

**Problem.** Microsoft Corporation sells Azure, M365, Entra and owns GitHub. Salesforce owns Slack. IBM owns Red Hat and HashiCorp.

**Evidence.** Microsoft 10-K; GitHub Trust Center (separate terms); Slack acquisition; IBM Red Hat 8-K (Red Hat survived as subsidiary); HashiCorp operations transition to IBM 2025-09-01.

**Current treatment.** `providers[]` points at one id. No parent/subsidiary field.

**Why insufficient.** One Microsoft row makes Azure ISO look like GitHub ISO. Collapsing Red Hat into IBM falsifies who sells OpenShift software.

**Options.** (1) One provider per legal seller; subsidiaries that still sell (GitHub, Red Hat) are separate ids. (2) Product-family providers (`microsoft-azure`, `microsoft-365`) that are not legal entities.

**Recommendation.** (1). Product-family split is convenient and legally false.

**Impact.** Documentation / onboarding. Test suite follows (1).

**Kind.** Semantics.

---

## D-006 / D-007 — DPA signed and audit rights

**Problem.** Every major vendor publishes a DPA. OSM `gdpr_dpa_signed` is a boolean on the provider. `audit_rights` is true/false/null. Public DPAs grant report-based audit, not unrestricted inspection.

**Evidence.** AWS DPA (incorporated in Service Terms); Microsoft Products and Services DPA (May 2026 edition listed); Google CDPA; Atlassian DPA 2026-08-17; Cloudflare Customer DPA v6.4.

**Current treatment.** Booleans on ICT Provider.

**Why insufficient.** “AWS has a DPA” is class A. “This customer signed it” is class C (often incorporated by reference, not wet-signed). Setting `gdpr_dpa_signed: true` on the provider record over-claims. Setting `audit_rights: true` over-claims.

**Options.** (1) Leave both null in any non-customer catalog; document the trap. (2) Add `dpa_published` vs `dpa_executed`. (3) Replace `audit_rights` with an enum (`reports`, `conditional-onsite`, `contractual-inspection`).

**Recommendation.** (1) now. (2)/(3) only after freeze review.

**Impact.** Documentation. Schema if (2)/(3).

**Kind.** Schema or documentation.

---

## D-011 — Vendor SLA vs enterprise target

**Problem.** Public SLAs are configuration-conditional credit schedules. OSM `availability_target` is the enterprise’s expected performance.

**Evidence.** EC2 compute SLA; S3 class-conditional SLA; AKS Free tier has no financially backed SLA; Google Cloud IAM SLA page states there is no SLA; VPC has no general SLA (NAT Gateway 99.9% only).

**Current treatment.** `availability_target` on service posture.

**Why insufficient.** Copying “99.99%” from a vendor SLA into posture asserts an enterprise target that was not decided and often does not match the SKU in use.

**Options.** Characteristic `vendor_availability_sla` (used in the test suite). New core field (reject under OSM-M-008).

**Recommendation.** Characteristic. Leave `availability_target` unset until the enterprise sets it.

**Impact.** Documentation. No schema change.

**Kind.** Documentation.

---

## D-012 / D-019 — What is allowed in the catalog

**Problem.** The 94-row universe mixes hyperscalers, vendor products, open-source projects, OS images, capability names, and business applications.

**Evidence.** kubernetes.io; PostgreSQL about; ServiceNow CMDB docs; SAP S/4HANA product page; OSM `MODEL.md` out of scope (applications, CMDB CIs, Product Models).

**Current treatment.** Anything can be typed as a Service if it has 2-segment id.

**Why insufficient.** Schema will not stop `id: infra.kubernetes` meaning the CNCF project, or `id: erp.s4hana` meaning a business application.

**Recommendation.** Onboarding rule: catalog the technological service the enterprise delivers or consumes as a service. Leave projects, OS, CMDB, and ERP/CRM/HCM out unless reviewers explicitly extend OSM.

**Impact.** Documentation. Test suite encodes S/4HANA, Sales Cloud and Workday only as labelled boundary tests.

**Kind.** Documentation + intentionally out of scope.

---

## D-014 — Service-to-Service relationships

**Problem.** Teams depends on Entra, Exchange and SharePoint. Databricks depends on a hyperscaler data plane. API Gateway depends on compute. Validation rejects `depends_on`.

**Evidence.** `SPECIFICATION.md` §1; validation rule 13; Microsoft Teams architecture.

**Current treatment.** Forbidden. `providers[]` is who-provides, not who-depends.

**Why insufficient for operators; sufficient for OSM’s stated scope.** The failure mode is stuffing Entra into Teams `providers[]`.

**Recommendation.** Keep the prohibition. Onboarding must say so. Do not “fix” with a relationship field during this investigation.

**Impact.** None if kept out of scope.

**Kind.** Intentionally out of scope.

---

## D-016 — Identity over-unification

**Problem.** Estate rows 26–28 look like three “IAM” products.

**Evidence.** AWS IAM docs (cloud-account authorization, no public SLA found). Entra fundamentals (enterprise directory/IdP; DORA Entra guidance). Cloud IAM SLA page (“No Service Level Agreement applies”).

**Recommendation.** Two Services: `identity.cloud-authorization` and `identity.directory-idp`. Never one `identity.iam` with three offerings.

**Impact.** Documentation / catalog convention.

**Kind.** Documentation.

---

## D-020 — DORA RoI

**Problem.** ITS 2024/2956 register templates need function identifier, licensed activity, LEI, ICT service type S01–S19, subcontracting rank, arrangement×service contracts. OSM has `providers`, `rto`/`rpo`, `operational_criticality`, `resilience_tested`, and provider contract booleans.

**Evidence.** ITS 2024/2956; RTS 2024/1773; `compliance/DORA.md`.

**Current treatment.** Thin mapping. Explicitly not a filing.

**Recommendation.** Do not grow OSM into the RoI. If a financial entity needs the register, join OSM ids to an external RoI store.

**Impact.** Out of scope. Freeze-compatible.

**Kind.** Intentionally out of scope.

---

## D-022 — EU AI Act

**Problem.** Cortex and Mosaic AI mix vendor AI systems and platforms that host customer models. OSM has applicability + risk class, not provider/deployer/GPAI.

**Evidence.** AI Act Art. 3; Snowflake Cortex docs; Databricks gen-AI capabilities; `compliance/EU-AI-ACT.md`.

**Recommendation.** Split vendor-operated AI features into their own Service. Leave `ai_act_risk_class` unset. Do not classify customer use.

**Impact.** Catalog convention. No schema.

**Kind.** Out of scope for roles; documentation for split.

---

## D-025 — Provider provenance

**Problem.** Provenance may attach to Service, Offering and posture. ICT Provider has no provenance object. Provider facts in this investigation (HQ, type, certifications, CTPP) cannot carry trust metadata on the record.

**Evidence.** `schema/catalog/ict-provider.yaml`; `schema/shared/provenance.yaml`.

**Recommendation.** Optional `provenance` on ICT Provider is a small, freeze-breaking additive change worth reviewing. Until then the research matrix is the evidence store.

**Impact.** Schema (additive, backwards-compatible).

**Kind.** Schema.

---

## D-029 — 94 vs 100

**Problem.** `01_reference_estate_100.csv` has 94 data rows.

**Evidence.** File count 2026-09-13.

**Recommendation.** Do not invent six rows. Rename in future process docs if needed.

**Kind.** Investigation process. Not an OSM schema issue.
