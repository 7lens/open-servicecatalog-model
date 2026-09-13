# Golden example — onboard a real catalog in ten minutes

This folder is a **small, independently validatable** subset of the
reference enterprise. It is not the whole estate.

| Count | What |
|------:|------|
| 5 | Technology Stacks |
| 10 | Services |
| 16 | Service Offerings |
| 4 | ICT Providers |
| 1 | Service Posture record |

The source was a predecessor service catalog that named **products** as
Services (`compute.eks`, `storage.s3`). OSM names the **technological
service** and puts the product on the Offering.

Validate from the repository root:

```bash
python3 validation/validate.py --catalog examples/reference-enterprise/golden-example
```

## The chain

```
Technology Stack
      ↓
   Service
      ↓
Service Offering ──► ICT Provider
      ↓
Characteristic          (what this variant is)
      ↓
Service Posture         (how it currently stands — optional)
      ↓
Provenance              (where the fact came from)
```

Walk it once with **Managed Kubernetes**.

### 1. Technology Stack

`compute` is an operational competency. It is not “AWS” and not “EKS”.

### 2. Service

`compute.kubernetes` is the technological service.

The predecessor catalog had three Services: `compute.eks`,
`compute.aks`, `compute.openshift`. That is the usual first mistake.

### 3. Offerings

| Offering | Source | Provider |
|----------|--------|----------|
| `compute.kubernetes.aws-eks` | `compute.eks.managed-k8s` | `aws` |
| `compute.kubernetes.azure-aks` | `compute.aks.managed-k8s` | `microsoft` |
| `compute.kubernetes.openshift` | `compute.openshift.openshift-platform` | `redhat` |

Offering slugs are catalog-specific (`aws-eks` here; other OSM
examples may use `compute.kubernetes.aws`). The modelling rule is the
same: the Offering is a **provider/product variant**, and `providers[]`
names the seller.

**OpenShift.** This estate consumed OpenShift as managed Kubernetes, so
it is an Offering of `compute.kubernetes`. That is an adopter modelling
choice, not an OSM rule. Another estate may keep OpenShift as its own
Service.

`providers[]` on the Offering is the cloud/seller dimension. Do not
repeat that identity as `deployment_environment: aws`.

### 4. Characteristic vs Posture

`os_family` on Virtual Machines is a Characteristic — it defines the
service (Linux and Windows were two source Services).

`engine` on RDS Offerings is a Characteristic — it distinguishes Oracle
from PostgreSQL.

Posture is **current assessed state**. It is optional.

### 5. Posture is sparse on purpose

Nine of these ten Services have **no** posture record.

The predecessor `service_attributes` file was a **field-pattern
demonstration**, not an assessed health record for this estate. Those
demo values (RTO, ISO controls, GDPR processor, NIST status, AI Act
risk class, EKS `important`) are not copied.

Unknown is preferable to invented.

`auto.aiops` has `ai_act_applicable: true` only because the source
**Service definition** classified it as AI-bearing. That is not a legal
classification.

### 6. Provider certifications

| Provider | `certifications[]` in this example |
|----------|-----------------------------------|
| `aws` | iso27001, iso27701, soc2-type2, c5, ens-alta, pci-dss |
| `microsoft` | iso27001, iso27701, soc2-type2, c5, ens-alta, pci-dss |
| `redhat` | iso27001, soc2-type2 |
| `oracle` | iso27001, soc2-type2, pci-dss |

Provider certifications are provider-level evidence. They do **not**
mean that every provider service, customer deployment, region, or OSM
Service is certified.

### 7. Provenance

Collapsed Services (Kubernetes, VMs, object storage, managed
relational) list **all** contributing source ids in
`evidence_reference`. OSM provenance has a single `source_record_id`;
it cannot name several ancestors. That is a schema limitation, not
evidence that EKS was the only source.

`last_verified` is omitted unless the source established a date.
`version` / `valid_from` / `lifecycle_state` are required OSM catalog
fields. Only `auto.aiops` `lifecycle_state: pilot` is source-derived.
Other Services use `draft` so the example does not manufacture
`production`.

### 8. Singleton Offerings

OSM requires at least one Offering (`minItems: 1`).

A Service may currently have only one Offering (`compute.functions.lambda`,
`sec.secrets.secrets-mgmt`, `auto.aiops.aiops`). That singleton is not
automatically a product-Service and not a request type.

Do not create Offerings to mirror an ITSM request catalogue.

## What else this subset teaches

| Record | Lesson |
|--------|--------|
| `compute.virtual-machines` + `os_family` | Linux/Windows were two source Services; OS is a Characteristic |
| `storage.object-storage` | S3 is an Offering, not a Service |
| `db.managed-relational` | Engine is a Characteristic. AWS operates RDS; Oracle is a licensor and is **not** listed on `providers[]` |
| `sec.iam.entra-id` | Workforce identity variant. MFA / password reset / directory lifecycle stay in ITSM |
| `auto.configuration-automation` | Red Hat is on the Ansible **Offering**, not on the capability Service |
| `auto.aiops` | `lifecycle_state: pilot` is source-derived and belongs on the Service |

Then read the [onboarding guide](../onboarding-guide.md).
