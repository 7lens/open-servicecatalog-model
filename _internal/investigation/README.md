# OSM reference-estate investigation

**Date:** 2026-09-13  
**Model:** frozen OSM 1.3.0  
**Schema changes from this work:** none  
**Public examples:** researched, anonymized records now live at
`examples/reference-estate/`. This folder is maintainer investigation
history. It is not public OSM documentation and not a real vendor
register. The 30 OPEN decisions here are not public OSM requirements.
Records under `records/` may still show the earlier Cloud Run–under–
Functions mismatch test; the public estate catalog splits CaaS as
`compute.container-service`.

## What was asked

Stress-test OSM with a representative technology estate: research
providers and services from authoritative public sources, try to encode
them in the current schema, and record every place the model is
ambiguous, too coarse, or would encourage bad semantics.

## What was produced

| Deliverable | Path |
|---|---|
| This report | `README.md` |
| Decision register | `decision_register.md` |
| Evidence matrix | `research_matrix.md` |
| Stress-test results | `stress_test_results.md` |
| Onboarding guide | `ONBOARDING_GUIDE.md` |
| Estate universe + treatment | `reference_estate_100.csv` (94 rows) |
| Validated test-suite YAML | `records/` |
| Source research notes | `research-notes/` |

Validate the test suite:

```bash
python3 validation/validate.py --catalog _internal/investigation/records
```

## Scope actually researched

**Providers (encoded):** AWS, Microsoft, Google Cloud, Oracle, IBM, Red
Hat, Alibaba Cloud, Cloudflare, Salesforce, ServiceNow, SAP, Atlassian,
Okta, CrowdStrike, Palo Alto Networks, Zscaler, Datadog, Dynatrace,
Snowflake, Databricks, GitHub, GitLab, Workday, Broadcom.

**Hyperscaler services (~7 each):** EC2, S3, RDS, EKS, Lambda, VPC, IAM;
Azure VMs, Blob, SQL Database, AKS, Functions, VNet, Entra ID; Compute
Engine, Cloud Storage, Cloud SQL, GKE, Cloud Run, VPC, Cloud IAM.

**Smaller-provider services (~2):** OCI Compute + Autonomous Database;
IKS + OpenShift on IBM Cloud; ECS + OSS; Cloudflare CDN/WAF + Access;
Sales Cloud + Slack; ServiceNow ITSM (CMDB refused); S/4HANA Cloud
(boundary test); Jira + Confluence; Okta Workforce; Falcon + Falcon
Complete; Prisma Access; ZIA + ZPA; Datadog + Dynatrace; Snowflake +
Cortex; Databricks lakehouse + Mosaic hosted models.

A smaller deeply evidenced catalog was preferred over 94 shallow rows.

## Headline result

**OSM can represent a real hyperscaler-and-SaaS estate without schema
changes** if the cataloguer:

1. Catalogues **technological services**, not products, projects or
   suites.
2. Puts **vendor products on Offerings** (or intrinsic `providers`).
3. Leaves **customer-dependent** criticality, RTO/RPO, signed DPA, DORA
   clauses, risk and classification **unset**.
4. Treats vendor SLAs as **characteristics**, not `availability_target`.
5. Does not treat `certifications[]` as proof that every service/region
   is certified.

The model **fails** — or is dangerous — when those rules are not known.
The schema will accept a bad catalog.

## Changes OSM should consider

None are implemented. All are `OPEN` in the decision register.

### Do now (no freeze break)

Document and teach:

- Certification tokens have no scope (D-001).
- `gdpr_dpa_signed` is execution, not publication (D-006).
- Vendor SLA ≠ enterprise target (D-011).
- Identity: do not unify AWS IAM, Entra ID and Cloud IAM (D-016).
- Suites (M365) decompose; projects (Kubernetes, PostgreSQL) stay out
  (D-012, D-015).
- Applications, CMDB and Product Models stay out (D-019).
- OSM is not the DORA Register of Information (D-020). Already stated
  in `compliance/DORA.md`; onboarding should repeat it.

These are documentation/onboarding. They do not change architecture.

### Consider later (additive, freeze decision required)

- Optional `provenance` on ICT Provider (D-025). Smallest high-value
  schema change: provider facts currently cannot carry evidence.
- Optional scoped certification object **only if** OSM is expected to
  hold compliance evidence rather than pointers (D-001 option 3).

### Do not do (would abandon OSM’s size)

- DORA RoI templates (LEI, function identifier, S01–S19, subcontracting
  rank, arrangement×service).
- GDPR ROPA / controller-processor matrices.
- AI Act provider/deployer/GPAI register.
- Service-to-Service relationship graph.
- A `saas` type enum as a panacea (it does not fix Cloud vs Data Center
  on one legal entity).

## Modelling pattern that survived contact with reality

```text
Technology Stack     adopter competency (not a vendor tower)
      ↓
   Service           stable technological service (Virtual Machines,
                     Managed Kubernetes, Workforce IdP, …)
      ↓
 Service Offering    requestable variant (aws-ec2, jira-cloud, …)
      ↓
 ICT Provider        legal seller (aws, atlassian, github — not
                     “Kubernetes”, not “Microsoft 365”)
```

Posture stays empty until the **enterprise** assesses it.

## Quality bar

Important non-synthetic facts in `research_matrix.md` and
`research-notes/` trace to official vendor, SEC, ESA or EUR-Lex URLs.
Customer facts were not invented. Provider certification is never
treated as customer compliance.
