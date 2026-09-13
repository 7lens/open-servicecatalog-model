# OSM onboarding guide — lessons from the reference-estate investigation

This guide is the **investigation** onboarding note. The public
guide is `examples/reference-estate/onboarding-guide.md`.

This file stays here as maintainer history. It does not change the
schema.

## 1. Decide what you are cataloguing

An OSM **Service** is the technological service **your enterprise**
delivers or consumes as a service.

| Estate token | Usually becomes | Usually does not become |
|---|---|---|
| Amazon EC2, Azure VM, GCE | Offerings of Service `compute.virtual-machines` | Three Services named after vendors |
| Amazon EKS, AKS, GKE | Offerings of `compute.kubernetes` | ICT Provider `kubernetes` |
| Kubernetes, Docker, PostgreSQL, Jenkins, Kafka, Prometheus, OpenTelemetry | Implementation notes / characteristics | Services or ICT Providers |
| RHEL, Ubuntu | Out of catalog (OS / product) | Services |
| Microsoft 365 | Several Services (email, content, chat, IdP) | One Service named Microsoft 365 |
| ServiceNow ITSM | Service (tooling) | — |
| ServiceNow CMDB | Out of catalog (CI inventory) | Service |
| Salesforce Sales Cloud, SAP S/4HANA, Workday | Out of catalog unless you have explicitly extended OSM to applications | Technological Services |

If a row is a **product**, ask: “what technological service do we
actually offer or consume?” Catalog that.

## 2. Identity: never one “IAM” Service

| Thing | OSM Service | Why |
|---|---|---|
| AWS IAM, Google Cloud IAM, Azure RBAC | Cloud platform authorization | Account/project resource policy. Often no public SLA. |
| Microsoft Entra ID, Okta Workforce, IAM Identity Center | Workforce directory / IdP | People, groups, federation, SSO. |
| Auth0 / Customer Identity Cloud | A second identity Service if you run CIAM | Not workforce IAM. |

Putting Entra ID, AWS IAM and Cloud IAM on one Service produces false
substitutability and false DORA mappings.

## 3. Providers: legal seller, not brand family

- One ICT Provider per **legal seller**.
- Keep **GitHub** and **Red Hat** distinct from Microsoft and IBM when
  they are the seller.
- After 2025-09-01, commercial HCP Terraform is typically **IBM**, not
  a HashiCorp ICT Provider.
- Slack may still contract as Slack Technologies; in this investigation
  it was modelled as a Salesforce offering. Pick one rule and keep it.
- `type` is a coarse org class. Put Cloud vs Data Center, SaaS vs
  appliance, MDR vs platform on **Offering characteristics**.

Do not create `microsoft-azure` and `microsoft-365` as fake legal
entities just to make `type` look tidy.

## 4. Certifications

`certifications: [iso27001]` on a provider means “this organisation
publishes that program,” **not**:

- every service is in scope
- every region is in scope
- Data Center / self-managed editions are in scope
- your deployment is certified
- you are DORA/GDPR compliant

Put the services-in-scope URL in provenance (on the Service/Offering
today; ICT Provider has no provenance field). Confirm the current
certificate before asserting anything in a customer catalog.

## 5. GDPR and DORA flags

| Field | Public fact you will find | What you may store |
|---|---|---|
| `gdpr_dpa_signed` | Vendor publishes a DPA | `true` only if **your** organisation executed or incorporated it |
| `dora_notification_clause` | Vendor publishes an FSA/addendum | `true` only if **your** contract contains it |
| `audit_rights` | Report-based rights in the DPA | Leave `null` unless counsel maps the boolean |
| `subcontracting_allowed` | Usually `conditional` in public DPAs | Acceptable as B if you cite the DPA |
| `subcontractors[]` | Public lists of hundreds of names | Do not paste a partial list. Link the official list |
| ESA CTPP designation | Named **legal entities** (e.g. AWS EMEA SARL, MIOL) | OSM has no field. Do not infer it from `headquarters` |

OSM is not the DORA Register of Information. Join OSM ids to whatever
system holds LEI, function identifier and S01–S19.

## 6. SLA, targets, hours

| Concept | Where it lives |
|---|---|
| When the service is supposed to be up | Offering characteristic `service_hours` |
| When support answers | Offering characteristic `support_hours` |
| Vendor credit SLA | Offering characteristic (e.g. `vendor_availability_sla`) |
| **Your** availability/response/resolution target | Service posture `*_target` |
| **Your** RTO/RPO | Offering posture `rto` / `rpo` |

Never copy a vendor SLA into `availability_target`. AKS Free has no
financially backed SLA. Cloud IAM officially has none. VPC often has
none except NAT Gateway.

## 7. Location

`data_processing_locations` on the provider is a **capability map**
(where they operate). The region your tenant uses is customer-dependent.
Record the **choice** as a characteristic (`region_selectable`,
`data_residency_option`). Leave the selected region off the provider
record.

Edge networks (Cloudflare, Zscaler) do not fit country lists well.

## 8. Operating model

Use an Offering characteristic:

- `vendor-operated` — hosted runners, Jira Cloud, Falcon SaaS
- `self-operated` — kubeadm, Jira Data Center, Terraform CLI
- `managed-detection` — Falcon Complete

Omit `providers` on a truly self-operated offering unless a
licence/support contract is the ICT third-party you must track.

## 9. Dual providers

If a SaaS control plane runs on a hyperscaler **and** you need both
relationships (Snowflake, Databricks, Atlassian Cloud→AWS):

```yaml
providers: [snowflake, aws]
```

Databricks ISO 27001 does not certify your AWS data plane.

## 10. Posture discipline

Until your organisation has assessed a service, publish definition
records and **empty** `offering_posture: []`.

Do not fill `operational_criticality`, `rto`, `rpo`,
`data_classification` or `risk_level` from a vendor website.

## 11. AI

If the vendor operates an AI feature (Cortex, Copilot, Rovo, Mosaic
hosted models), prefer a **separate Service** from the warehouse /
IDE / wiki. Set `ai_act_applicable: true` only there. Leave risk class
unset until a real assessment exists.

A platform that **hosts customer models** is not the customer’s AI
system.

## 12. What not to put in `providers[]`

`providers[]` means **who provides this Service or Offering**.

It does not mean:

- Entra as a provider of Teams
- AWS as a provider of every VM guest OS
- CNCF as a provider of Kubernetes
- Microsoft as the provider of GitHub unless Microsoft is the seller
  on that contract

Service-to-Service dependency is out of OSM. Hold it elsewhere.

## 13. Suggested first catalog

Start with capability Services you actually run:

1. Virtual machines
2. Object storage
3. Managed Kubernetes
4. Managed relational database
5. Virtual network
6. Workforce IdP
7. CI/CD
8. Observability

Add SaaS identity, email, ITSM, endpoint protection as intrinsic-
provider Services. Add CRM/ERP only if you have decided OSM should
hold applications — the frozen model says it should not.

## 14. Validate

```bash
python3 validation/validate.py
```

Use `--catalog` for any additional catalog tree. The validator will
not catch semantic mistakes (IAM unified, ISO over-claimed, SLA copied
into targets). Those are onboarding problems, not schema problems.
