# Golden example — learn OSM in ten minutes

This folder is a **small, independently validatable** subset of the
reference estate. It is not the whole enterprise.

| Count | What |
|------:|------|
| 5 | Technology Stacks |
| 10 | Services |
| 17 | Service Offerings |
| 6 | ICT Providers |
| 10 | Service Posture records |

Start here, then read the [onboarding guide](../onboarding-guide.md).

Validate from the repository root:

```bash
python3 validation/validate.py --catalog examples/reference-estate/golden-example
```

## The chain OSM is built for

```
Technology Stack
      ↓
   Service
      ↓
Service Offering ──► ICT Provider
      ↓
Characteristic          (definition facts, including vendor SLA)
      ↓
Service Posture         (how the enterprise currently stands)
      ↓
Provenance              (why a fact can be trusted)
```

Walk that chain once with **Managed Kubernetes**.

### 1. Technology Stack

`compute` is an operational competency of the adopting organization.
It is not “AWS” and not “the Kubernetes product family.”

### 2. Service

`compute.kubernetes` is the technological service: Kubernetes clusters
the enterprise can request or run.

It is **not**:

- the CNCF Kubernetes project
- Amazon EKS
- “containers”

### 3. Offerings

Three requestable variants:

| Offering | What it is |
|----------|------------|
| `compute.kubernetes.aws-eks` | Amazon EKS, provided by `aws` |
| `compute.kubernetes.azure-aks` | Azure Kubernetes Service, provided by `microsoft` |
| `compute.kubernetes.self-operated` | Clusters the enterprise operates. **No ICT Provider.** |

AWS is not a Service. EKS is not a Service. EKS is an Offering of the
Kubernetes service.

### 4. ICT Provider

`aws` and `microsoft` are legal sellers. `kubernetes` is not an ICT
Provider. CNCF is not an ICT Provider.

### 5. Characteristics

On the EKS offering:

- `vendor_availability_sla` — the vendor credit schedule
- `service_hours` — when the service is intended to be up
- `support_hours` — when support answers

Those three are **not** the same fact. Hours are not an SLA. An SLA is
not the customer’s availability target.

AKS Free has no financially backed SLA. That is recorded on the AKS
offering, not invented as a customer target.

### 6. Service Posture

`compute.kubernetes` is the one golden record that sets
`availability_target: "99.9%"`.

That value is an **enterprise-declared target**. Provenance says so
(`enterprise-declared-target-not-vendor-sla`). It is not copied from
the EKS or AKS SLA.

`operational_criticality`, `rto` and `rpo` stay unset. A public catalog
does not know this customer’s recovery objectives.

### 7. Provenance

Every important public fact points at vendor documentation or at an
enterprise declaration. ICT Provider records have no provenance field
in the frozen schema — that is a known limitation, not a reason to
invent certifications.

## What else this subset teaches

| Record | Lesson |
|--------|--------|
| `compute.virtual-machines` + EC2 / Azure VM / GCE | Same technological service, three hyperscaler offerings |
| `storage.object-storage` | Object storage is a service; S3 is an offering |
| `identity.directory-idp` vs `identity.cloud-authorization` | Entra/Okta is not AWS IAM |
| `collab.email` as Exchange Online | Microsoft 365 is a suite, not one OSM Service |
| `collab.issue-tracking` Cloud vs Data Center | Same seller, different operating model; Cloud ISO does not cover Data Center |
| `data.cloud-warehouse.snowflake-aws` | Dual providers: Snowflake **and** AWS |
| `data.vendor-ai-assist` | Vendor-operated AI is a separate service from the warehouse. `ai_act_applicable: true` is not a legal classification |

## What this subset deliberately omits

- CRM / ERP / HCM applications
- CMDB configuration items
- Customer contracts, signed DPA, DORA clauses, risk scores
- A filled RTO/RPO for every offering
- The rest of the researched estate (RDS, VPC, Falcon, ServiceNow, …)

Those live in the [full reference estate](../catalog/) and the
[mapping cookbook](../mapping-cookbook.md).
