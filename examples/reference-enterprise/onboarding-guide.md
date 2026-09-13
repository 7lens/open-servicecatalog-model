# Onboarding OSM from a real enterprise catalog

This guide uses the predecessor catalog behind
[reference-enterprise](README.md) as the worked example.

The source already looked like a service catalog. Onboarding OSM is
still a **modelling** job, not an import.

```
PREDECESSOR CATALOG
        ↓
UNDERSTAND WHAT YOU HAVE
        ↓
FIND THE TECHNOLOGICAL SERVICES
        ↓
DEFINE TECHNOLOGY STACKS
        ↓
DEFINE SERVICES (capabilities, not products)
        ↓
DEFINE OFFERINGS WHERE THE SOURCE HAS A REAL TECHNOLOGICAL VARIANT
        ↓
IDENTIFY ICT PROVIDERS (legal sellers)
        ↓
ADD CHARACTERISTICS (what the variant is)
        ↓
ADD SERVICE POSTURE (only known current state; omit if unknown)
        ↓
ADD PROVENANCE
        ↓
LEAVE THE REST OUT
```

Worked YAML: [golden example](golden-example/README.md).

---

## 1. Understand what you have

This estate arrived as YAML:

- 14 technology stacks
- 95 services / 153 offerings
- 6 health-record examples (`service_attributes` — a field-pattern
  demonstration, **not** assessed enterprise posture)
- 13 ICT Providers
- 2 governance roles

It did **not** arrive as a CMDB, a cloud bill, or a list of 38
countries. The predecessor specification already said geography,
organization and applications are out of scope.

If your enterprise also has a CMDB and 38 operating countries, they
remain outside OSM. Use them as sources of hints, not as records to
copy.

---

## 2. Find the technological services

Do not assume a source `service` is an OSM Service.

Ask: **what technological service does this actually represent?**

| Source row | OSM treatment |
|------------|---------------|
| `compute.eks` / `compute.aks` / `compute.openshift` | Offerings of `compute.kubernetes` |
| `compute.vm-linux` / `compute.vm-windows` | One Service `compute.virtual-machines`; OS is a Characteristic |
| `storage.s3` / `storage.azure-blob` / `storage.gcs` | Offerings of `storage.object-storage` |
| `db.rds-oracle` / `db.rds-postgresql` / `db.azure-sql` | Offerings of `db.managed-relational` |
| `lz.lz-aws` / `lz.lz-azure` | Offerings of `lz.landing-zone` |
| `ops.observability` | Already a capability Service — keep |
| `ops.asset-inventory` | CMDB — **out** |
| `sm.incident-mgmt` | ITSM process — **out** (no tooling product named) |
| `devops.portal-next` | Local platform — **ignore** |
| `contact-center-vendor` | Anonymized placeholder — **out** |

---

## 3. Stacks

Reuse source competency names where they are real operational domains:
Compute, Database, Storage, Network, Security, and so on.

Do not create a stack called AWS or Microsoft 365.

Source stack **mappings** (TBM, TOGAF, ISO, NIST, GDPR, DORA, AI Act)
are optional OSM `mappings`. They are translations, not proof that the
stack is certified.

---

## 4. Offerings only where the source has a technological variant

Create an Offering when the predecessor already distinguished:

- provider / cloud (AWS vs Azure vs on-prem)
- engine (Oracle vs PostgreSQL)
- product (EKS vs AKS vs OpenShift)

Do **not** create Offerings for ITSM/request-catalogue items: MFA,
password reset, directory lifecycle, access-governance tickets,
instance types, accounts or countries.

OSM requires at least one Offering (`minItems: 1`). A Service may
currently have only one. That singleton is not automatically a product
or a request type. Do not invent extra Offerings to mirror a request
catalogue.

The source has no per-country offerings; do not invent 38.

On-prem VM and on-prem VPC offerings have **no** `providers[]`.
There is no ICT Provider in the source for the data center itself.

Jenkins has no provider in the source register. Do not invent
CloudBees.

**OpenShift.** This estate consumed OpenShift as managed Kubernetes, so
it is an Offering of `compute.kubernetes`. That is this catalog’s
modelling choice, not an OSM rule.

---

## 5. ICT Providers

An ICT Provider is the **legal seller**.

**Bad (source):** `azure` and `microsoft` as two providers for the
same corporation.

**Good (OSM):** one `microsoft`. GitHub stays `github` because the
source listed GitHub as the seller of GitHub Enterprise / Actions.

Put `providers[]` on the Offering when the seller distinguishes the
variant. Do not copy a current sole seller onto the capability Service
unless that seller is intrinsic to the capability itself. Red Hat
belongs on the Ansible Offering, not on `auto.configuration-automation`.

Drop:

- `criticality` (not an OSM field; do not copy it into `risk_level`)
- `services_consumed` (reverse links are derived from `providers[]`)
- placeholder vendors

`gdpr_dpa_signed: true` was set on **every** source provider. OSM
means *this customer executed the DPA*. The predecessor did not
evidence that. Leave the field null.

Provider `certifications[]` are **provider-level** published program
names. They do **not** mean that every provider service, customer
deployment, region, or OSM Service is certified.

---

## 6. Characteristic vs Service Posture

This is the distinction the example is built to show.

**Characteristic** — what the service / offering *is*.

From this source: `os_family` (linux / windows), `engine` (oracle /
postgresql). Cloud/seller identity is `providers[]` on the Offering,
not a Characteristic named `deployment_environment: aws`.

The source stored `cloud_providers` on the health record. OSM does
not have that field.

**Service Posture** — current assessed state of this customer’s
service. It is optional.

The predecessor health file demonstrated field patterns. Those demo
values (RTO, ISO controls, GDPR processor, NIST status, AI Act risk
class, EKS `important`) are **not** imported as assessed posture.

Unknown is preferable to invented. Most Services in this example have
no posture record because the source did not establish those values.

`lifecycle_state` is required OSM catalog metadata. Only `auto.aiops`
(`pilot`) is source-derived operational truth. Other Services use
`draft` so the example does not manufacture `production`.

---

## 7. Provenance

Every promoted record can point at the predecessor catalog:

- `source_system: predecessor-catalog`
- `source_record_id`: original id **when there is exactly one**
- `evidence_reference`: concatenated source ids when a Service was
  collapsed from several records (OSM has a single `source_record_id`)
- `discovery_method: imported`

Do not claim `compute.eks` as the sole source of the Kubernetes
Service. Do not invent `last_verified` dates.

Do not put filesystem paths, company names or account IDs here.

---

## 8. What not to do

**Bad:** `compute.eks` as a Service  
**Good:** `compute.kubernetes` → offering `aws-eks` → provider `aws`

**Bad:** MFA / password reset as OSM Offerings  
**Good:** one identity Offering (`sec.iam.entra-id`); request types stay in ITSM

**Bad:** copy predecessor demo health into `service_posture`  
**Good:** omit posture until the enterprise has assessed current state

**Bad:** copy EKS `important` / RTO onto the Kubernetes Service (or
onto AKS/OpenShift)  
**Good:** leave collapsed-service posture unset; do not promote demo
values onto a sibling Offering either

**Bad:** `deployment_environment: aws` on the AWS Offering  
**Good:** `providers: [aws]`; the offering id already names the variant

**Bad:** `service_attributes`  
**Good:** `service_posture` / `offering_posture`

**Bad:** treat OSM as the DORA register (`services_consumed`, provider
`criticality`, Art. 28 narrative)  
**Good:** canonical OSM fields; RoI stays external

**Bad:** import the CMDB (`ops.asset-inventory`)  
**Good:** leave configuration items out

**Bad:** invent `availability_target`, `service_hours`, or
`lifecycle_state: production`  
**Good:** omit or use `draft` — the source does not establish them

**Bad:** `gdpr_dpa_signed: true` because the predecessor ticked every vendor  
**Good:** null until execution is evidenced

---

## Practical questions

### “I have a CMDB.”

This source already had `ops.asset-inventory`. It is still not an OSM
Service. CIs can hint that EKS clusters exist. They do not become
Offerings.

### “I have AWS EC2 / EKS records.”

The predecessor used `compute.vm-linux.vm-lifecycle-aws` and
`compute.eks`. OSM uses Virtual Machines / Managed Kubernetes with
AWS as provider. Instance inventory stays out.

### “I have Salesforce / Microsoft 365.”

This source did not catalog Salesforce CRM. It did catalog Microsoft
as the seller of Entra/workforce identity (`sec.iam.entra-id`). That is
workforce identity, not a suite SKU named Microsoft 365.

### “I have 38 countries.”

Not in the source files. The predecessor model excluded geography on
purpose. OSM `data_processing_locations` is a **vendor capability
map** (here: `eu`, `us` from the source). It is not the enterprise’s
operating footprint.

### “I have criticality and RTO/RPO.”

Use them only where the enterprise **assessed** them. This source’s
health file was a field-pattern demonstration. After collapsing
products into capabilities, do not stamp one product’s demo RTO on
the Service or on sibling offerings. Unknown is preferable to invented.

### “My Service has only one Offering.”

That is allowed. The schema requires at least one. A singleton
Offering is not automatically a product-Service and not a request type.

---

## Validate

```bash
python3 validation/validate.py --catalog examples/reference-enterprise
python3 validation/validate.py --catalog examples/reference-enterprise/golden-example
```

The validator will not catch “EKS as a Service”. That is an onboarding
mistake, not a schema error.
