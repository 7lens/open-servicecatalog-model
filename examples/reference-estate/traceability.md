# Traceability

How the public examples were derived from the anonymized source
estate. No source-system identifiers, contract numbers, account IDs
or organization names appear here.

The source was a multinational financial-sector technology landscape.
Public OSM records use well-known provider and product names in place
of internal labels.

Transformation rule used throughout:

> Map only technological services, offerings, providers,
> characteristics, posture and provenance that belong in OSM.
> Leave applications, CMDB inventory, geography of the enterprise,
> contracts and compliance registers outside.

---

## Golden example (complete)

| OSM Concept | Source Concept | Transformation | Notes |
|---|---|---|---|
| Stack `compute` | Cloud IaaS / container operations competency | Named as an organizational competency, not “AWS” | Stacks are adopter domains |
| Stack `storage` | Unstructured data storage operations | Same | |
| Stack `identity` | Workforce IAM plus cloud IAM sprawl | Split into one stack, two services | Avoids a single “IAM tower” |
| Stack `collaboration` | Messaging, mail and work-management tools | Competency, not “Microsoft 365” | Suite SKUs are not stacks |
| Stack `data` | Analytical platforms | Competency covering warehouse + vendor AI | AI is a sibling service, not a stack of its own |
| Service `compute.virtual-machines` | EC2 / Azure VM / GCE product records | Products collapsed into one technological service | Instances stay out of OSM |
| Offering `aws-ec2` | Amazon EC2 | Product → offering of the VM service | Provider `aws` |
| Offering `azure-vm` | Azure Virtual Machines | Product → offering | Provider `microsoft` |
| Offering `gce` | Google Compute Engine | Product → offering | Provider `google-cloud` |
| Characteristic `vendor_availability_sla` | Public Compute / VM SLAs | Stored as definition characteristic | Not copied to `availability_target` |
| Service `compute.kubernetes` | EKS / AKS / self-built clusters | One service for Kubernetes-as-a-service | CNCF project is not a service |
| Offering `aws-eks` | Amazon EKS | Managed offering | SLA is control-plane only |
| Offering `azure-aks` | Azure Kubernetes Service | Managed offering | Free tier has no financially backed SLA |
| Offering `self-operated` | Customer-operated clusters | Offering with no `providers` | Kubernetes is not an ICT Provider |
| Characteristics `service_hours`, `support_hours` | Operating-hours intent | Hours windows on EKS | Distinct from SLA and from targets |
| Posture `availability_target: 99.9%` on Kubernetes | Enterprise availability intent | Declared customer target | Provenance: `enterprise-declared-target-not-vendor-sla` |
| Omitted `operational_criticality` / `rto` / `rpo` | Source criticality and recovery objectives | **Not promoted** | Customer-dependent; public examples do not invent values |
| Service `storage.object-storage` | S3 / Blob inventory | One object-storage service | Buckets stay in cloud/CMDB |
| Offering `aws-s3` | Amazon S3 | Product → offering | Durability claims ≠ availability target |
| Offering `azure-blob` | Azure Blob Storage | Product → offering | |
| Service `identity.directory-idp` | Entra ID / Okta workforce tenants | Workforce directory service | Not AWS IAM |
| Offering `entra-id` | Microsoft Entra ID | Product → offering | Shared M365/Azure substrate |
| Offering `okta-workforce` | Okta Workforce Identity Cloud | Product → offering | Auth0/CIC not included |
| Service `identity.cloud-authorization` | AWS IAM | Separate service | No public IAM SLA found |
| Offering `aws-iam` | AWS IAM | Product → offering | Distinct from IAM Identity Center |
| Service `collab.issue-tracking` | Jira Cloud and Jira Data Center | One service, two offerings | Cloud ISO does not cover Data Center |
| Offering `jira-cloud` | Jira Cloud | `deployment_model: cloud` | Residency pin is selectable, not stored as chosen region |
| Offering `jira-data-center` | Jira Data Center | `deployment_model: data-center` | Self-managed edition |
| Service `collab.email` | Exchange Online / M365 mail | Suite decomposed to email service | Not Service `microsoft-365` |
| Offering `exchange-online` | Exchange Online | Product → offering | Provider `microsoft` |
| Service `collab.team-chat` | Microsoft Teams | Suite decomposed to chat service | Entra dependency not in `providers[]` |
| Offering `teams` | Microsoft Teams | Product → offering | |
| Service `data.cloud-warehouse` | Snowflake on AWS | Warehouse service | Dual providers |
| Offering `snowflake-aws` | Snowflake hosted on AWS | `providers: [snowflake, aws]` | Hosting CSP is a second third party |
| Service `data.vendor-ai-assist` | Snowflake Cortex | Separate AI feature service | Warehouse is not labelled an AI system |
| Offering `snowflake-cortex` | Cortex | Vendor-operated AI offering | `ai_act_applicable` is not a legal class |
| ICT Provider `aws` | Amazon Web Services as seller | One provider per legal seller | `certifications[]` are program names; DPA/DORA/risk null |
| ICT Provider `microsoft` | Microsoft Corporation as seller | Azure and M365 share one seller | Not split into fake Azure/M365 entities |
| ICT Provider `google-cloud` | Google Cloud as seller | One seller | |
| ICT Provider `okta` | Okta, Inc. as seller | Workforce IAM seller | |
| ICT Provider `atlassian` | Atlassian as seller | Cloud and Data Center share one seller | Edition on the offering |
| ICT Provider `snowflake` | Snowflake Inc. as seller | Data-platform seller | Dual-provider offerings still name AWS too |
| Provenance on catalog records | Public vendor documentation | `source_system: public-web` plus evidence URL | No internal ticket or CMDB ids |
| Provenance on posture | Service Owner declaration | `source_system: osm-catalog` | Customer facts are declared, not scraped |

---

## Full reference estate (summary)

The full catalog applies the same transformations at larger grain.

| OSM Concept | Source Concept | Transformation | Notes |
|---|---|---|---|
| 11 stacks | Operational groupings in the estate | Competency domains | `enterprise-applications` was an investigation boundary test and is **not** public |
| 24 technological services | Hyperscaler, SaaS, security, data, devops tools | Products collapsed onto capability services | ~7 offerings per hyperscaler family; ~2 for smaller providers |
| 60 offerings | Named vendor products and editions | Nested under services | Includes self-operated Kubernetes/IaC and dual-provider data platforms |
| 20 ICT Providers | Legal sellers used by the estate | One id per seller | GitHub ≠ Microsoft; HCP Terraform → IBM |
| Unused investigation providers | Red Hat, SAP, Workday, Broadcom as unused sellers | **Not promoted** | No remaining public offering referenced them |
| Thin `service_posture` (11 records) | Partial operational assessment | Representative posture only | Empty `offering_posture: []` until assessed |
| Customer contract / DPA / DORA / risk / RTO | Source vendor-risk and resilience data | **Left null / omitted** | Public catalog must not invent customer facts |
| Salesforce Sales Cloud, SAP S/4HANA Cloud, Workday HCM | Enterprise applications in the source | **Not promoted** | Taught as anti-patterns in the cookbook |
| ServiceNow CMDB | CI inventory | **Not promoted** | Only ITSM tooling is an OSM Service |
| 38 operating countries | Enterprise geographic footprint | **Not promoted** | Provider capability maps ≠ customer geography |
| 94-row technology list | Broader estate universe | Public examples use the researched subset | Not a dump of every row |

---

## What was never a source-to-OSM mapping

These were left outside on purpose, not because a field is missing:

- DORA Register of Information (LEI, function identifier, templates)
- GDPR Records of Processing
- AI Act provider / deployer / GPAI register
- Service-to-Service graphs (Teams → Entra, guest OS → VM)
- Full subcontractor lists
- Chosen cloud region per tenant
