# Onboarding OSM with the reference estate

This guide uses the [reference estate](README.md) as a worked example.
It does not change the OSM schema.

The point of OSM is not to import every enterprise object. The point
is to own a small canonical picture of **technological services**.

```
SOURCE ENTERPRISE ESTATE
        ↓
UNDERSTAND WHAT YOU HAVE
        ↓
IDENTIFY TECHNOLOGICAL SERVICES
        ↓
DEFINE TECHNOLOGY STACKS
        ↓
DEFINE SERVICES
        ↓
DEFINE OFFERINGS WHERE THEY ARE REAL
        ↓
IDENTIFY ICT PROVIDERS
        ↓
ADD CHARACTERISTICS
        ↓
ADD SERVICE POSTURE
        ↓
ADD PROVENANCE
        ↓
LEAVE NON-OSM INFORMATION OUT
```

Worked YAML for a first pass: [golden example](golden-example/README.md).
Case-by-case mappings: [mapping cookbook](mapping-cookbook.md).

---

## 1. Understand what you have

A multinational financial-sector estate typically arrives as a mix of:

- CMDB configuration items
- cloud billing and inventory
- SaaS admin consoles
- architecture diagrams
- contract and vendor-risk registers
- “we operate in 38 countries”

None of those systems is OSM. Each can **contribute** facts. OSM
decides which facts belong.

Ask, for every source row:

> What technological service does the enterprise actually deliver or
> consume?

If the honest answer is “a product”, “an application”, “a server”,
“a project” or “a country”, it is not yet an OSM Service.

---

## 2. Identify technological services

| Estate token | Usually becomes | Usually does not become |
|---|---|---|
| Amazon EC2, Azure VM, GCE | Offerings of `compute.virtual-machines` | Three Services named after vendors |
| Amazon EKS, AKS, GKE | Offerings of `compute.kubernetes` | ICT Provider `kubernetes` |
| Kubernetes, Docker, PostgreSQL, Jenkins | Implementation notes / characteristics | Services or ICT Providers |
| Microsoft 365 | Several Services (email, content, chat, IdP) | One Service named Microsoft 365 |
| ServiceNow ITSM | Service (tooling) | — |
| ServiceNow CMDB | Out of catalog (CI inventory) | Service |
| Salesforce Sales Cloud, SAP S/4HANA, Workday | Out of catalog | Technological Services |

The public full catalog keeps the technological services. It does
**not** catalog CRM, ERP or HCM as OSM Services. That is a modelling
choice the frozen model already implies, not a missing field.

---

## 3. Define Technology Stacks

Stacks are **operational competency domains of the adopting
organization**: Compute, Storage, Identity, Collaboration, Data.

They are not vendor towers (“AWS”, “Microsoft 365”) and not a required
taxonomy. Another enterprise may name them differently. OSM only
requires that a Service names a stack that exists.

---

## 4. Define Services

A Service is a stable technological capability with a two-segment id
(`compute.kubernetes`).

Identity is the easy place to get this wrong. Do not create one “IAM”
Service that mixes:

| Thing | OSM Service | Why |
|---|---|---|
| AWS IAM, Google Cloud IAM | `identity.cloud-authorization` | Account/project resource policy. Often no public SLA. |
| Microsoft Entra ID, Okta Workforce | `identity.directory-idp` | People, groups, federation, SSO. |

Putting Entra, AWS IAM and Cloud IAM on one Service produces false
substitutability.

---

## 5. Define Offerings where they are real

An Offering is a requestable or deliverable variant
(`compute.virtual-machines.aws-ec2`).

Create an Offering when the variant is actually how the enterprise
requests or runs the service: different provider, different operating
model (Jira Cloud vs Data Center), different capability (functions
vs container-as-a-service — Lambda vs Cloud Run).

Do not create an Offering for every SKU, instance type, region or
CI. Regions are usually a **choice** (`region_selectable`), not a
separate offering.

Self-operated Kubernetes is a real offering with **no** `providers`
list. Upstream Kubernetes is a project, not a provider.

---

## 6. Identify ICT Providers

An ICT Provider is an **external party delivering or underpinning** an
OSM Service or Offering. One row per legal seller.

- GitHub is not Microsoft, even if Microsoft owns GitHub.
- After 2025-09-01, commercial HCP Terraform is typically IBM, not a
  HashiCorp ICT Provider.
- Slack may still contract as Slack Technologies; this estate models
  Slack as a Salesforce offering. Pick one rule and keep it.
- Do not create `microsoft-azure` and `microsoft-365` as fake legal
  entities to make `type` look tidy.
- `type` is a coarse org class. Put Cloud vs Data Center, SaaS vs
  appliance on **Offering characteristics**.

Snowflake on AWS lists **two** providers: `snowflake` and `aws`.
Databricks ISO 27001 does not certify the customer AWS data plane.

---

## 7. Add Characteristics

Characteristics belong on the Service or Offering **definition**.

Typical useful ones in this estate:

- `vendor_availability_sla` — vendor credit schedule
- `service_hours` / `support_hours` — time windows, not SLAs
- `region_selectable`, `data_residency_option`
- `operating_model` (`vendor-operated`, `self-operated`, `managed-detection`)
- `deployment_model` (`cloud`, `data-center`)
- `execution_model` (`function`, `container-service`)

Never copy a vendor SLA into posture `availability_target`.

---

## 8. Add Service Posture

Posture is how the **enterprise** currently stands.

Until the organization has assessed a service, publish definition
records and empty `offering_posture: []`.

Do not fill `operational_criticality`, `rto`, `rpo`,
`data_classification` or `risk_level` from a vendor website.

The golden example sets `availability_target: "99.9%"` on Managed
Kubernetes only, with provenance
`enterprise-declared-target-not-vendor-sla`. That is the pattern:
enterprise target, declared, evidenced. Not a copied AWS number.

AI Act fields on `data.vendor-ai-assist` record that vendor-operated
AI features exist. They are **not** a legal classification of the
customer as provider or deployer.

---

## 9. Add Provenance

Provenance explains why a fact can be trusted. Put it on Service,
Offering and Posture records.

The frozen schema has **no provenance field on ICT Provider**. Provider
certification lists therefore cannot carry scoped evidence on the
record itself. Treat `certifications[]` as published program names,
not proof.

---

## 10. Leave non-OSM information out

Hold elsewhere (and join by OSM id if needed):

- applications and product models
- CMDB configuration items
- organization and location hierarchies
- full contract and SLA management
- DORA Register of Information templates
- GDPR Records of Processing
- AI Act provider/deployer registers
- Service-to-Service dependency graphs (Teams depends on Entra)

OSM holds each canonical concept once. Frameworks map onto those
concepts. They do not get a second copy of the same fact.

---

## Practical questions

### “I have a CMDB. What do I do?”

Do not import the CMDB.

A CMDB is a configuration-item inventory: servers, clusters, databases,
application instances, locations, relationships. Most of that remains
**outside** OSM.

What a CMDB *can* contribute:

- hints that a technological service exists (there are Kubernetes
  clusters → consider `compute.kubernetes`)
- hints that an offering exists (those clusters are EKS → offering
  `compute.kubernetes.aws-eks`)
- a pointer back, in provenance `source_system` / `source_record_id`

What stays in the CMDB:

- every cluster, node, volume and application instance
- CI class models and relationship graphs
- discovery noise

ServiceNow ITSM can be an OSM Service (`ops.itsm`). ServiceNow CMDB
is still not.

### “I have AWS EC2 records.”

EC2 is not a Service.

Transform:

1. Technological service: virtual-machine compute
   (`compute.virtual-machines`).
2. Offering: Amazon EC2 (`compute.virtual-machines.aws-ec2`).
3. ICT Provider: AWS.
4. Instance inventory, AMI, VPC attachment, account ID: **not OSM**.
5. Vendor Compute SLA: characteristic `vendor_availability_sla`.
6. Your availability/RTO: posture, and only after you assess it.

### “I have Salesforce.”

Separate five different ideas:

| Idea | In this estate |
|------|----------------|
| Product / suite | Sales Cloud, Slack, and other Salesforce products |
| Provider | ICT Provider `salesforce` (legal seller) |
| Technology | Salesforce platform — implementation detail |
| Technological service | Team chat is an OSM Service; CRM is an application and is **out** |
| Offering | `collab.team-chat.slack` |

Salesforce the company can be an ICT Provider without Salesforce CRM
becoming an OSM Service.

### “I have 38 countries.”

Where the **enterprise operates** is external enterprise context.
OSM does not catalog countries of incorporation, branches or users.

What OSM does hold:

- `headquarters` on an ICT Provider (one ISO country — coarse)
- `data_processing_locations` on an ICT Provider — a **capability
  map** of where the vendor can process data, not the tenant’s chosen
  region
- characteristics such as `region_selectable` and
  `data_residency_option` — that a choice exists

The region a given tenant actually uses is customer-dependent. Do not
write “38 countries” onto AWS. Edge networks (Cloudflare, Zscaler)
do not fit country lists well; this estate uses tokens such as
`global-edge`.

### “I have criticality and RTO/RPO.”

Those are **customer / service posture**, not universal properties of
EC2, S3 or Salesforce.

AWS does not have an RTO. Your payment-processing workload on EC2
might. Until the enterprise assesses it, leave `operational_criticality`,
`rto` and `rpo` unset. Filling them from a vendor website makes a
catalog look complete and be wrong.

---

## What not to do

### AWS is not a Service

**Bad:** `id: aws` as a Service, or one Service per vendor product.

**Good:** Compute Service → Offering `aws-ec2` → ICT Provider `aws`.

### Vendor SLA is not `availability_target`

**Bad:** copy “99.99%” from the AWS Compute SLA into
`availability_target`.

**Good:** vendor SLA as characteristic `vendor_availability_sla`.
Customer target on service posture, with provenance that it is an
enterprise declaration. AKS Free has no financially backed SLA.
Cloud IAM officially has none. VPC often has none except NAT Gateway.

### Not every software product is an ICT Provider

**Bad:** ICT Providers named `kubernetes`, `postgresql`, `jira`,
`microsoft-365`.

**Good:** ICT Provider is the external party delivering or underpinning
the OSM Service/Offering (`aws`, `atlassian`, `microsoft`). Products
and projects stay on offerings or out of the catalog.

### Do not copy every CMDB object into OSM

**Bad:** one Service or Offering per CI.

**Good:** use the CMDB as a source and map only concepts that belong
to OSM.

### Do not duplicate DORA fields throughout the model

**Bad:** DORA-named copies of criticality, RTO, provider, subcontracting
on every record.

**Good:** use canonical OSM concepts (`operational_criticality`, `rto`,
`rpo`, `providers`) and keep the Register of Information in an
external mapping. OSM is not the DORA RoI.

### Related compliance traps

- Provider certifications must not become universal service compliance
  claims. AWS ISO is scoped; Atlassian Cloud ISO does not cover Data
  Center; GitLab ISO does not cover Self-Managed.
- `gdpr_dpa_signed: true` means **your** organization executed or
  incorporated the DPA, not “the vendor publishes a DPA”.
- OSM is not a GDPR ROPA.
- OSM is not an AI Act provider/deployer register.
  `ai_act_applicable: true` on Cortex records that a vendor-operated
  AI feature exists. It does not classify the customer.

---

## Suggested first catalog

Start with capability services you actually run, as the golden example
does:

1. Virtual machines
2. Object storage
3. Managed Kubernetes
4. Workforce IdP
5. Cloud-platform authorization
6. One SaaS collaboration service with Cloud vs Data Center
7. One dual-provider data platform

Add managed databases, virtual networks, endpoint protection,
observability and ITSM when you need them. Add CRM/ERP only if you
have explicitly decided OSM should hold applications — the frozen
model says it should not.

## Validate

```bash
python3 validation/validate.py --catalog examples/reference-estate
python3 validation/validate.py --catalog examples/reference-estate/golden-example
```

The validator will not catch semantic mistakes (IAM unified, ISO
over-claimed, SLA copied into targets). Those are onboarding problems,
not schema problems.
