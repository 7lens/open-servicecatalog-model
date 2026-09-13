# Traceability

How the public example was derived from the anonymized predecessor
catalog. No company names, people, paths or account IDs.

Source grain: 14 stacks, 95 services, 153 offerings, 13 providers,
6 health-record **demonstrations** (not assessed posture).

Public grain: 10 stacks, 18 services, ~40 offerings, 8 providers,
1 posture record (`auto.aiops`, AI-bearing flag only).

---

## Golden example

| OSM Record | Source | Transformation | Notes |
|---|---|---|---|
| Stack `compute` | Stack Compute | Kept | Competency domain |
| Stack `storage` | Stack Storage | Kept | |
| Stack `db` | Stack Database | Kept id `db`, name Database | Validator matches stack **name** |
| Stack `sec` | Stack Security | Kept | |
| Stack `auto` | Stack Automation | Kept | AI Act mapping stays on the full catalog |
| Service `compute.virtual-machines` | `compute.vm-linux` + `compute.vm-windows` | Collapsed | OS-patching offerings dropped (activity, not a variant) |
| Characteristic `os_family` | Two source Services | Characteristic | linux / windows, configurable |
| Offering `compute.virtual-machines.aws` | `*.vm-lifecycle-aws` | Cloud variant | Provider `aws`; no `deployment_environment: aws` |
| Offering `compute.virtual-machines.azure` | `*.vm-lifecycle-azure` | Cloud variant | Provider `microsoft` (source `azure` merged) |
| Offering `compute.virtual-machines.on-prem` | `*.vm-lifecycle-onprem` | Cloud variant | No provider in source |
| Service `compute.kubernetes` | `compute.eks` + `compute.aks` + `compute.openshift` | Collapsed | Provenance lists all three in `evidence_reference` |
| Offering `compute.kubernetes.aws-eks` | `compute.eks.managed-k8s` | Product → offering | Provider `aws`. OpenShift-as-Kubernetes-offering is this estate’s choice, not an OSM rule |
| EKS / RDS demo health | predecessor `service_attributes` | **Not copied** | Field-pattern demo, not assessed posture; would leak product facts onto collapsed Services |
| Offering `compute.kubernetes.azure-aks` | `compute.aks.managed-k8s` | Product → offering | Provider `microsoft` |
| Offering `compute.kubernetes.openshift` | `compute.openshift.openshift-platform` | Product → offering | Duplicate `container-platform` offering dropped |
| Service `compute.functions` | `compute.lambda` | Renamed | Singleton offering because the schema requires ≥1; Lambda is not the Service id |
| Service `storage.object-storage` | `storage.s3` + `storage.azure-blob` | Collapsed | GCS held for the full catalog only |
| Service `storage.backup` | `storage.backup` | Kept | Restore offering omitted in golden; remaining singleton is schema `minItems`, not a request type |
| Service `db.managed-relational` | several `db.rds-*` / `db.azure-*` / `db.aurora-*` | Collapsed | Representative engines only |
| Offering `rds-oracle` | `db.rds-oracle.rds-oracle` | Product → offering | Providers `aws` + `oracle` (open question D-GE-002; not resolved here) |
| Service `sec.iam` | `sec.iam` | Kept | One offering `entra-id`. MFA / password-reset / directory-lifecycle stay in ITSM |
| Service `sec.secrets` | `sec.secrets` | Kept | Singleton offering = schema requirement |
| Service `auto.configuration-automation` | `auto.ansible` | Capability + offering | `redhat` on the Ansible **Offering** only |
| Service `auto.aiops` | `auto.aiops` | 1:1 | `lifecycle_state: pilot` moved onto Service (source-derived) |
| Posture `auto.aiops` | source Service definition (AI-bearing) | `ai_act_applicable: true` only | Demo risk class / RTO / ISO / NIST / GDPR not copied |
| Provider `aws` | `aws` | Kept | Dropped `criticality`, `services_consumed`; `gdpr_dpa_signed` null; certifications unscoped |
| Provider `microsoft` | `azure` + `microsoft` | Merged | One legal seller |
| Provider `redhat` | `redhat` | Kept | Source labelled “(IBM)”; Red Hat remains the seller of OpenShift/Ansible |
| Provider `oracle` | `oracle` | Kept | |

---

## Full catalog (additional)

| OSM Record | Source | Transformation | Notes |
|---|---|---|---|
| Stacks lz, net, mw, devops, ops | Same names | Kept | FinOps, Workplace, Service Management, Data not used |
| `lz.landing-zone` offerings aws/azure/gcp/datacenter | `lz.lz-*` | Per-cloud offerings | Nickname “Vending Machine” dropped; functional request offerings account-lifecycle / guardrails dropped |
| Predecessor landing-zone health | source service-level attributes | **Not copied** | Demo field-pattern values |
| `storage.object-storage.gcs` | `storage.gcs` | Product → offering | Provider `gcp` (source id kept) |
| `storage.backup.restore` | `storage.backup.restore` | Kept | Restore is a source activity; not used as a pattern for IAM request types |
| `db.managed-relational.azure-sql` / `aurora-postgresql` | source product Services | Offerings | |
| `net.virtual-network` | `net.vpc` | Renamed | Source already had per-environment offerings |
| `net.cdn` | `net.cdn` | Kept | No CDN vendor in source register — no invented provider |
| `mw.api-gateway` | aws + azure + on-prem API services | Collapsed | |
| `mw.event-streaming.confluent` | `mw.confluent` | Capability + offering | `confluent` on the Offering only; Kafka is not an ICT Provider |
| `devops.source-control` | `devops.github` + `devops.bitbucket` | Collapsed | GitHub ≠ Microsoft |
| `devops.continuous-delivery` | `devops.github-actions` + `devops.jenkins` | Collapsed | Jenkins has no provider in source |
| `ops.observability` | `ops.observability` | Kept | Tooling-admin offering omitted |
| Provider `gcp`, `confluent`, `github`, `atlassian` | same ids | Kept | |

---

## Not promoted

| Source | Why |
|---|---|
| `ops.asset-inventory` | CMDB |
| `ops.change-mgmt`, `ops.problem-mgmt`, `sm.incident-mgmt`, `sm.prod-ops` | ITSM processes |
| `sm.organization`, `sm.adoption` | Programme / adoption |
| `finops.*` | Financial processes |
| `compute.resilience`, `db.database-ops` | Runbooks |
| `compute.spa-*`, `devops.portal-*`, `auto.iac-orchestration`, `auto.automation-engine` | Local platform names |
| `workplace.contact-center`, `mw.batch` | Placeholder vendors |
| `sm.ai-assistant` | Valid AI example; omitted to keep stacks ≤ 10 (AIOps already demonstrates AI Act) |
| `sec.soc`, `sec.siem`, `sec.waf` | Functions / overlapping with `net.cdn` WAF |
| `mw.jboss` / `tomcat` / `weblogic` / `websphere` / `mq` | Application-server products |
| `db.mongodb`, `db.elasticache-redis`, `db.oracle-odb-*`, `db.oracle-oci` | Extra engine products |
| Provider `ibm`, `mongodb`, placeholders | No remaining offering |
| 38 operating countries | Not in source files; geography was out of predecessor scope |
| Predecessor demo `service_attributes` (RTO, ISO, NIST, GDPR, EKS criticality) | Field-pattern demonstration, not assessed posture |

---

## Field mapping (health record)

Predecessor vocabulary only. Demo values were **not** imported.

| Predecessor | OSM |
|---|---|
| `service_attributes` | `service_posture` (optional; omit if unknown) |
| `offering_attributes` | `offering_posture` (optional; omit if unknown) |
| `lifecycle_state` (attributes) | Service `lifecycle_state` — copy only when sourced (`auto.aiops`: `pilot`); otherwise required catalog metadata `draft` |
| `dora_criticality` | `operational_criticality` — not copied from demo rows |
| `dora_rto` / `dora_rpo` | `rto` / `rpo` — not copied from demo rows |
| `dora_resilience_tested` | `resilience_tested` — not copied |
| `dora_third_party_deps` | catalog `providers[]` |
| `cloud_providers` | Offering `providers[]` (not `deployment_environment`) |
| Provider `criticality` | dropped |
| `services_consumed` | dropped |
| `gdpr_dpa_signed: true` | null |
