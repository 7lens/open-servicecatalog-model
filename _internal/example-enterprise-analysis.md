# Predecessor catalog analysis — example enterprise

Working notes for onboarding `Downloads/example_enterprise/` into
frozen OSM 1.3.0. Not public documentation. Source treated as
read-only. No Mapfre / insurance / local-platform names promoted.

## What the dataset actually is

It is **not** a CMDB extract, cloud bill, or application portfolio.

It is a **predecessor service-catalog model** (self-described as
“canonical / vendor-neutral”, version 1.0) already shaped as:

```
technology_stacks → services → service_offerings
service_attributes (health record)
ict_providers (DORA Art. 28 register)
governance (roles)
```

The source README states the catalog is illustrative reference data
using industry-standard names, with organization-specific platform
names reduced to generic capabilities. Geography, organization and
applications are **intentionally out of source scope**.

User context (not in the files): multinational financial-sector
enterprise, ~38 countries. Those facts stay **outside OSM**. They are
not in the YAML and must not be invented into records.

## Inventory

| File | Records | Role in source |
|------|--------:|----------------|
| `schema/technology_stacks.yaml` | 14 | Competency domains + framework mappings |
| `schema/services.yaml` | 95 services / 153 offerings | Catalog |
| `schema/service_attributes.yaml` | 6 services | Representative health-record examples |
| `schema/ict_providers.yaml` | 13 | Third-party register |
| `schema/governance.yaml` | 2 roles | Stack Owner / Service Owner |
| `README.md`, `SPECIFICATION.md` | — | Predecessor semantics |

No Mapfre. No insurance-sector tokens. Two ICT Providers are already
anonymized placeholders (`contact-center-vendor`,
`batch-scheduler-vendor`).

### Stacks (14)

`lz` Landing Zone, `compute` Compute, `db` Database, `net` Network,
`storage` Storage, `mw` Middleware & Integration, `devops` DevOps,
`auto` Automation, `data` Data, `sec` Security, `ops` Operations,
`finops` FinOps, `workplace` Workplace, `sm` Service Management.

### Services by stack

Landing Zone 5, Compute 11, Database 13, Network 8, Security 6,
Storage 6, Middleware 10, Operations 7, DevOps 11, Automation 5,
Data 5, FinOps 2, Workplace 2, Service Management 4.

### Attribute coverage (only 6)

`lz.landing-zone`, `compute.eks`, `db.rds-oracle`, `compute.vm-linux`,
`auto.aiops`, `sm.ai-assistant`.

Everything else has **no** source criticality, RTO/RPO, cost or
automation figures. OSM must not invent them.

### Providers (13)

Named: aws, azure, gcp, redhat, confluent, github, atlassian, oracle,
microsoft, ibm, mongodb.

Placeholders: contact-center-vendor, batch-scheduler-vendor.

Every named provider has `gdpr_dpa_signed: true` and a DORA-style
`criticality`. Contract dates, risk_level and exit fields are null.
`services_consumed` reverse-links services to providers.

## Predecessor vs frozen OSM

| Predecessor | OSM 1.3.0 |
|-------------|-----------|
| `service_attributes` / `offering_attributes` | `service_posture` / `offering_posture` |
| `lifecycle_state` on attributes | `lifecycle_state` on Service |
| no `version` / `valid_from` | required on Service |
| `dora_criticality` | `operational_criticality` |
| `dora_rto` / `dora_rpo` / `dora_resilience_tested` | `rto` / `rpo` / `resilience_tested` |
| `dora_third_party_deps` | catalog `providers[]` |
| `cloud_providers` | not a field; environment is a Characteristic; seller is `providers[]` |
| ICT Provider `criticality` | not a field; do not copy into `risk_level` |
| `services_consumed` | not a field; reverse links are derived |
| `azure` and `microsoft` as two sellers | one legal seller (`microsoft`) |
| Product-named Services (`compute.eks`, `storage.s3`) | Capability Service + Offerings |
| OSM as DORA Art. 28 register | OSM is not the RoI |
| `governance.yaml` in the catalog | public `GOVERNANCE.md`; not a catalog file |

## Modelling decisions (what is a technological service?)

### Collapse product-Services into capability Services

Source treats vendor products as Services. OSM treats them as
Offerings of a technological service.

| Source Services | OSM Service | Offerings |
|-----------------|-------------|-----------|
| `compute.vm-linux`, `compute.vm-windows` | `compute.virtual-machines` | aws / azure / on-prem; OS is a Characteristic |
| `compute.eks`, `compute.aks`, `compute.openshift` | `compute.kubernetes` | aws-eks, azure-aks, openshift |
| `compute.lambda` | `compute.functions` | lambda |
| `storage.s3`, `storage.azure-blob`, `storage.gcs` | `storage.object-storage` | s3, azure-blob, gcs |
| `db.rds-*`, `db.aurora-*`, `db.azure-sql`, `db.azure-postgresql` | `db.managed-relational` | representative engines only |
| `lz.lz-aws/azure/gcp/datacenter` | `lz.landing-zone` | per-cloud offerings |
| `mw.api-gateway-aws/onprem`, `mw.api-mgmt-azure` | `mw.api-gateway` | aws / azure / on-prem |
| `devops.github`, `devops.bitbucket` | `devops.source-control` | github, bitbucket |
| `devops.github-actions`, `devops.jenkins` | `devops.continuous-delivery` | github-actions, jenkins |

### Keep when already a capability

`net.vpc`, `net.cdn`, `sec.iam`, `sec.secrets`, `ops.observability`,
`storage.backup`, `mw.confluent` (as event-streaming), `auto.aiops`,
`auto.ansible` (as configuration-automation offering).

### Out of OSM (do not promote)

| Source | Why |
|--------|-----|
| `ops.asset-inventory` | CMDB / CI inventory |
| `ops.change-mgmt`, `ops.problem-mgmt`, `sm.incident-mgmt`, `sm.prod-ops` | ITSM **processes**, no tooling product named |
| `sm.organization`, `sm.adoption` | programme / change-adoption, not a technological service |
| `finops.cost-mgmt`, `finops.licenses` | financial processes |
| `compute.resilience` | DR/BCP process, not a requestable tech service |
| `db.database-ops` | operations runbook, not a database service |
| `data.*` | overlapping generic platforms; no vendor grain in source |
| `sec.soc` | operating function (SOC), not a service offering of a platform |
| `net.certificates` mixed with vuln-intake | two capabilities glued together; prefix vs stack already inconsistent |

### Ignore as local / placeholder (user rule)

| Source | Why |
|--------|-----|
| “Landing Zone Vending Machine” | local nickname; keep the capability, not the nickname |
| `devops.portal-classic`, `devops.portal-next` | local portals |
| `auto.iac-orchestration` (“control abstraction engine”), `auto.automation-engine`, `auto.notifications` | local automation fabric |
| `compute.spa-private`, `compute.spa-public` | local SPA hosting platforms |
| `workplace.contact-center` + `contact-center-vendor` | anonymized local platform |
| `mw.batch` + `batch-scheduler-vendor` | anonymized local scheduler |

### Application servers / engines as products

`mw.jboss`, `mw.tomcat`, `mw.weblogic`, `mw.websphere`, `mw.mq`,
`db.mongodb`, `db.elasticache-redis`, `db.oracle-odb-*`, `db.oracle-oci`
are products or engines. Not promoted. Oracle remains an ICT Provider
because RDS Oracle is a real offering of managed relational.

## Facts we will not invent

- 38 countries / operating locations (user context; absent from files)
- RTO/RPO/criticality for the 89 services without attributes
- `service_hours` / `support_hours` / pricing (not in source)
- Named contact-center or batch-scheduler vendors
- Merging GitHub into Microsoft (source keeps GitHub as seller)
- `gdpr_dpa_signed: true` copied as OSM execution-of-DPA
- Provider `criticality` copied as `risk_level`
- `availability_target` (source has none)

## Facts we will carry (canonical names)

From the six attribute blocks, mapped:

- `lifecycle_state` → Service definition
- `dora_criticality` → `operational_criticality` only when the OSM
  Service is 1:1 with the source service
- `dora_rto` / `dora_rpo` / `dora_resilience_tested` → offering posture
- `chargeback_model`, `automation_coverage`, `manual_hours_week`,
  `last_security_review`, `asset_coverage`, ISO/NIST/GDPR mapping
  fields → offering posture
- `cloud_providers` → Characteristic `deployment_environment` and/or
  `providers[]` (seller), never kept as `cloud_providers`
- AI Act fields on `auto.aiops` only

`lz.landing-zone` is 1:1, so service-level criticality/classification
can be copied. Collapsed services (kubernetes, managed-relational, VMs)
do **not** inherit one product’s criticality for the whole capability.

## ICT Provider treatment

- Merge source `azure` into `microsoft` (same legal entity; source
  split Azure vs Productivity/Identity).
- Keep `github` distinct from `microsoft`.
- Keep `redhat` distinct from `ibm`.
- Keep source id `gcp` (enterprise identifier).
- Drop placeholder vendors.
- Drop `criticality` and `services_consumed`.
- Leave `gdpr_dpa_signed` and `risk_level` null.
- Keep headquarters, processing locations, substitutability,
  concentration_risk, certifications, subcontracting_allowed from source.

## OSM required fields the source lacks

Service `version` and `valid_from` are required by OSM. They are
cataloguing metadata, not operational facts:

- `version: "1.0.0"` — source spec is version 1.0
- `valid_from: 2026-01-01` — cataloguing date for this example
- `lifecycle_state: production` for live catalog entries without
  attributes; `pilot` for `auto.aiops` (source)

## Representative public subset

See `examples/reference-enterprise/`. Not a conversion of all 95
services.
