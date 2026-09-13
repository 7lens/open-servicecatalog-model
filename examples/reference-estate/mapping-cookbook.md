# Mapping cookbook

Modelling judgement, not YAML syntax. Each case is a transformation
from the anonymized estate into frozen OSM 1.3.0.

Pattern:

```
SOURCE
  ↓
OSM
  ↓
WHY
```

---

## 1. AWS EC2 — compute, not a vendor service

**SOURCE:** AWS EC2 instance inventory / product name “Amazon EC2”.

**OSM:**

- Service `compute.virtual-machines`
- Offering `compute.virtual-machines.aws-ec2`
- ICT Provider `aws`
- Characteristic `vendor_availability_sla`

**WHY:** The technological service is virtual-machine compute. EC2 is
how AWS sells that service. Azure VM and GCE are sibling offerings,
not three OSM Services named after vendors.

---

## 2. Kubernetes — project, managed offering, self-operated offering

**SOURCE:** “We run Kubernetes” plus EKS/AKS clusters in the cloud
bill, plus a few kubeadm clusters.

**OSM:**

- Service `compute.kubernetes`
- Offerings `aws-eks`, `azure-aks`, `self-operated`
- Providers `aws` / `microsoft` on the managed offerings
- **No** provider on `self-operated`
- **No** ICT Provider named `kubernetes`

**WHY:** Kubernetes the CNCF project is not a seller. Managed EKS is
an offering of a Kubernetes service. Self-operated clusters are still
that service, with operating model `self-operated`. Creating Provider
`kubernetes` would invent a third party that does not exist.

---

## 3. Object storage — S3 is an offering

**SOURCE:** Amazon S3 buckets, Azure Blob accounts.

**OSM:**

- Service `storage.object-storage`
- Offerings `aws-s3`, `azure-blob`
- Providers `aws`, `microsoft`

**WHY:** Object storage is the technological service. Bucket inventory
stays in the cloud account / CMDB. S3 durability marketing is not an
OSM availability target; the credit SLA is a characteristic.

---

## 4. Relational database — managed service vs engine product

**SOURCE:** Amazon RDS, Azure SQL Database, plus PostgreSQL running
on VMs.

**OSM:**

- Service `db.managed-relational`
- Offerings `aws-rds`, `azure-sql`, …
- PostgreSQL-on-VM is **not** this service (it is compute plus a
  product)

**WHY:** The OSM service is *managed* relational database. PostgreSQL
the engine is a product. Cataloguing “PostgreSQL” as a Service or as
an ICT Provider confuses software with a technological service.

---

## 5. Identity — two services, never one “IAM”

**SOURCE:** AWS IAM policies, Microsoft Entra ID tenants, Okta
workforce org.

**OSM:**

- `identity.cloud-authorization` → offering `aws-iam` → provider `aws`
- `identity.directory-idp` → offerings `entra-id`, `okta-workforce`

**WHY:** AWS IAM authorizes cloud resources. Entra/Okta authenticate
people. Mixing them produces false substitutability (“we can replace
Entra with IAM”) and false compliance mappings. AWS IAM has no public
availability SLA; do not invent one.

---

## 6. SaaS collaboration — Jira Cloud vs Data Center

**SOURCE:** Atlassian Jira (some teams on Cloud, some on Data Center).

**OSM:**

- Service `collab.issue-tracking` with intrinsic provider `atlassian`
- Offerings distinguished by `deployment_model`: `cloud` vs
  `data-center`

**WHY:** Same technological service, different operating model. Cloud
ISO/SOC evidence does **not** cover Data Center. One Jira Service with
no offerings would hide that. Two ICT Providers named `jira-cloud` and
`jira-data-center` would invent legal entities.

---

## 7. Security — endpoint platform vs managed detection

**SOURCE:** CrowdStrike Falcon, plus Falcon Complete on some estates.

**OSM:**

- Service `sec.endpoint-protection`
- Offering `falcon` (platform) and `falcon-complete`
  (`operating_model: managed-detection`)
- ICT Provider `crowdstrike`

**WHY:** Falcon Complete is not a second provider and not a different
technological service. It is a managed-detection offering of the same
endpoint-protection service. `type: managed-service` on the provider
would be wrong for the whole CrowdStrike company.

---

## 8. Networking — VPC is a service and a tenancy boundary

**SOURCE:** Amazon VPC, Azure VNet, Google Cloud VPC.

**OSM:**

- Service `net.virtual-network`
- Offerings `aws-vpc`, `azure-vnet`, `gcp-vpc`

**WHY:** Teams request virtual networks, so a service record is
justified. VPC is also an isolation boundary OSM cannot represent as
a separate entity. There is often no general VPC uptime SLA (NAT
Gateway is a different product SLA). Do not copy NAT Gateway’s 99.9%
onto the VPC offering as `availability_target`.

---

## 9. Observability — Datadog is an offering of a service

**SOURCE:** Datadog and Dynatrace subscriptions.

**OSM:**

- Service `ops.observability`
- Offerings `datadog`, `dynatrace`
- Providers `datadog`, `dynatrace`

**WHY:** Metrics/logs/traces is the technological service. Prometheus
or OpenTelemetry running on self-operated Kubernetes is usually an
implementation of that service (or of the Kubernetes offering), not a
new ICT Provider named `prometheus`.

---

## 10. Enterprise platform — Microsoft 365 is a suite

**SOURCE:** “We have Microsoft 365.”

**OSM:** decompose into technological services already in this estate:

| Suite token | OSM |
|-------------|-----|
| Exchange Online | `collab.email` / `exchange-online` |
| SharePoint Online | `collab.content` / `sharepoint-online` |
| Teams | `collab.team-chat` / `teams` |
| Entra ID | `identity.directory-idp` / `entra-id` |

Provider for all of them: `microsoft`.

**WHY:** A suite SKU is a commercial bundle. OSM catalogs technological
services. Teams depends on Entra; OSM cannot record that
Service-to-Service dependency — do not stuff Entra into Teams
`providers[]`.

---

## 11. Salesforce — provider of Slack, not a CRM service

**SOURCE:** Salesforce Sales Cloud plus Slack.

**OSM:**

- ICT Provider `salesforce`
- Offering `collab.team-chat.slack` (team-chat service)
- Sales Cloud **out of the public catalog** (application / product)

**WHY:** Having Salesforce as a seller does not make CRM a
technological service in OSM. Slack is team chat. Sales Cloud is an
enterprise application. The investigation encoded CRM only as a
boundary test; the public examples do not repeat that mistake as if
it were recommended.

---

## 12. Dual providers — Snowflake on AWS

**SOURCE:** Snowflake warehouse hosted on AWS.

**OSM:**

```yaml
id: data.cloud-warehouse.snowflake-aws
providers: [snowflake, aws]
```

**WHY:** Two third parties actually underpin the offering: Snowflake
operates the control plane; AWS hosts. Listing only Snowflake hides
concentration on AWS. Listing only AWS pretends Snowflake is not a
seller. Snowflake’s ISO attestation does not certify the customer’s
AWS account.

---

## 13. Cloud Run — container-as-a-service is not Functions

**SOURCE:** Google Cloud Run next to AWS Lambda and Azure Functions.

**OSM:** Cloud Run is Service `compute.container-service`, offering
`compute.container-service.cloud-run`. Lambda and Azure Functions
remain under `compute.functions`.

**WHY:** Lambda and Functions are function platforms. Cloud Run is
container-as-a-service. Product names may appear on Offerings; they
must not collapse distinct capabilities into one Service. An earlier
teaching cut placed Cloud Run under Functions as a visible mismatch;
the catalog now uses the correct grain.

---

## 14. HCP Terraform — seller identity after acquisition

**SOURCE:** HashiCorp Terraform CLI locally, HCP Terraform as a hosted
control plane.

**OSM:**

- Service `auto.infrastructure-as-code`
- Offering `self-operated` — no provider (CLI/OpenTofu in a pipeline)
- Offering `hcp-terraform` — provider `ibm`

**WHY:** Terraform the tool is not an ICT Provider. After 2025-09-01
the commercial seller of HCP Terraform is IBM. Creating provider
`hashicorp` to match the product brand would be convenient and legally
false for that offering.

---

## 15. ServiceNow — ITSM in, CMDB out

**SOURCE:** ServiceNow platform, ITSM module, CMDB module.

**OSM:**

- Service `ops.itsm` / offering `servicenow` / provider `servicenow`
- CMDB configuration items: **leave out**

**WHY:** ITSM tooling is a technological service the enterprise
consumes. A CMDB is an inventory of CIs. Copying CIs into OSM recreates
the CMDB under another name.
