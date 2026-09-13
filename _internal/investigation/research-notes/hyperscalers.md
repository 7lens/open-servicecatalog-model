# Hyperscaler research notes

Research date: 2026-09-13. Public-source investigation for 7lens OSM reference-estate modelling. This file records provider and service facts, evidence class, and OSM field mapping. It does not populate a customer estate.

**Evidence classes:** A = publicly verified; B = publicly documented but conditional (service / region / edition / SKU); C = customer-dependent; D = not publicly determinable.

**Layer key (do not collapse):** provider fact · service fact · offering fact · customer posture · compliance evidence.

**Hard unknowns (never invent):** customer contract dates, RTO/RPO, operational_criticality, risk_level, whether a DPA is signed for a given customer, whether a DORA notification clause is in a given contract, exit strategy documented/tested, last_risk_assessment.

**ISO 27001 caveat (applies to all three providers):** a provider-level ISO/IEC 27001 certificate does **not** automatically cover every service, region, feature, sovereign cloud, or customer deployment. Scope is the certificate + statement of applicability + services-in-scope list current at audit time. Customer implementations remain the customer’s certification problem.

---

## Sources consulted

### Regulatory / survey

- https://eur-lex.europa.eu/legal-content/ENG/ALL/?uri=CELEX:32022R2554
- https://eur-lex.europa.eu/eli/reg_del/2024/1773/oj
- https://www.esma.europa.eu/press-news/esma-news/european-supervisory-authorities-designate-critical-ict-third-party-providers
- https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf
- https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act/dora-oversight
- https://www.flexera.com/blog/finops/the-latest-cloud-computing-trends-flexera-2025-state-of-the-cloud-report/
- https://resources.flexera.com/web/pdf/Flexera-State-of-the-Cloud-Report-2025.pdf
- https://info.flexera.com/CM-REPORT-State-of-the-Cloud?lead_source=Organic+Search
- https://resources.flexera.com/web/pdf/Flexera-State-of-the-Cloud-Report-2026.pdf

### Amazon / AWS

- https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
- https://aws.amazon.com/agreement/
- https://aws.amazon.com/legal/aws-contracting-party/
- https://aws.amazon.com/compliance/iso-certified/
- https://aws.amazon.com/compliance/services-in-scope/
- https://aws.amazon.com/compliance/services-in-scope/PCI/
- https://aws.amazon.com/compliance/data-privacy-faq/
- https://aws.amazon.com/compliance/faq/
- https://aws.amazon.com/compliance/dora/
- https://aws.amazon.com/blogs/security/aws-designated-as-a-critical-third-party-provider-under-eus-dora-regulation/
- https://aws.amazon.com/blogs/security/spring-2026-soc-1-2-and-3-reports-are-now-available-with-188-services-in-scope/
- https://aws.amazon.com/blogs/security/spring-2026-pci-dss-and-pci-3ds-compliance-packages-for-aws-now-available/
- https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/aws-data-processing-addendum-dpa.html
- https://d1.awsstatic.com/legal/aws-gdpr/AWS_GDPR_DPA.pdf
- https://aws.amazon.com/compliance/sub-processors/
- https://d1.awsstatic.com/fs-compliance-center/pdf-summaries/AWS-User-Guide-to-the-Digital-Operational-Resilience-Act.pdf
- https://aws.amazon.com/about-aws/global-infrastructure/
- https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- https://aws.amazon.com/compute/sla/
- https://aws.amazon.com/s3/sla/
- https://aws.amazon.com/rds/sla/
- https://aws.amazon.com/eks/sla/
- https://aws.amazon.com/lambda/sla/
- https://aws.amazon.com/vpc/sla/
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html
- https://aws.amazon.com/s3/
- https://aws.amazon.com/rds/
- https://aws.amazon.com/eks/
- https://aws.amazon.com/lambda/
- https://aws.amazon.com/vpc/
- https://aws.amazon.com/iam/

### Microsoft

- https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm
- https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA
- https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1
- https://azure.microsoft.com/en-us/support/legal/sla/
- https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-27001
- https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-iso-27001
- https://learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope
- https://learn.microsoft.com/en-us/azure/compliance/offerings/
- https://learn.microsoft.com/en-us/compliance/regulatory/offering-soc-2
- https://servicetrust.microsoft.com/viewpage/ISOIEC
- https://learn.microsoft.com/en-us/compliance/assurance/assurance-supplier-management
- https://learn.microsoft.com/en-us/compliance/dora/dora-what-is-dora
- https://learn.microsoft.com/en-us/compliance/dora/dora-contract-mapping
- https://learn.microsoft.com/en-us/compliance/dora/dora-entra
- https://www.microsoft.com/en-us/trust-center/compliance/dora-compliance
- https://learn.microsoft.com/en-us/azure/reliability/regions-list
- https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies
- https://learn.microsoft.com/en-us/azure/virtual-machines/availability
- https://learn.microsoft.com/en-us/azure/reliability/reliability-virtual-machines
- https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy
- https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview
- https://learn.microsoft.com/en-us/azure/reliability/reliability-sql-database
- https://learn.microsoft.com/en-us/azure/azure-sql/database/high-availability-sla-local-zone-redundancy?view=azuresql
- https://learn.microsoft.com/en-us/azure/aks/free-standard-pricing-tiers
- https://azure.microsoft.com/en-gb/pricing/details/kubernetes-service/
- https://azure.microsoft.com/en-us/products/functions
- https://azure.microsoft.com/en-us/products/virtual-network
- https://learn.microsoft.com/en-us/entra/fundamentals/whatis
- https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-sla-performance
- https://learn.microsoft.com/en-us/azure/cost-management-billing/microsoft-customer-agreement/microsoft-customer-agreement-faq
- https://www.microsoft.com/en-us/professionalservices/suppliers

### Google Cloud

- https://cloud.google.com/terms
- https://cloud.google.com/terms/google-entity
- https://cloud.google.com/terms/data-processing-addendum
- https://cloud.google.com/terms/cloud-privacy-notice
- https://cloud.google.com/terms/subprocessors
- https://cloud.google.com/security/compliance/iso-27001
- https://cloud.google.com/security/compliance/soc-2
- https://cloud.google.com/security/compliance/dora
- https://cloud.google.com/security/compliance/services-in-scope
- https://cloud.google.com/blog/products/identity-security/supporting-customers-as-a-critical-provider-under-eu-dora
- https://services.google.com/fh/files/misc/eu_dora_customer_guide_googlecloud.pdf
- https://cloud.google.com/about/locations
- https://docs.cloud.google.com/docs/geography-and-regions
- https://docs.cloud.google.com/compute/docs/regions-zones
- https://cloud.google.com/compute/sla
- https://cloud.google.com/storage/sla
- https://cloud.google.com/sql/sla
- https://cloud.google.com/kubernetes-engine/sla
- https://cloud.google.com/run/sla
- https://cloud.google.com/iam/sla
- https://docs.cloud.google.com/vpc/docs/resources
- https://cloud.google.com/compute
- https://cloud.google.com/run
- https://business.safety.google/compliance/

---

## Provider: Amazon Web Services (AWS)

### Facts table (fact | OSM field | value | scope | class | URL)

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Legal / parent name | `ict_provider.name` (plus note; OSM has no legal-name field) | Parent registrant: **Amazon.com, Inc.** (Delaware). AWS is a business of Amazon, not a separately listed public company. | Parent legal identity. Not automatically the customer contracting party. | A | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm |
| Typical US/default contracting party | (no OSM field; gap) | **Amazon Web Services, Inc.**, 410 Terry Avenue North, Seattle, WA 98109-5210 | Default when Account Country is US or unlisted; also default if location cannot be determined. | A | https://aws.amazon.com/legal/aws-contracting-party/ |
| EU/EMEA contracting party (common) | (no OSM field; gap) | **Amazon Web Services EMEA SARL** (Luxembourg) for many EMEA account countries | Account-country dependent. This is the DORA CTPP legal name, not the US parent. | A | https://aws.amazon.com/legal/aws-contracting-party/ ; https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf |
| Other local contracting parties | (no OSM field; gap) | Local subsidiaries exist (Canada, Singapore, Korea, Indonesia, Mexico, South Africa, Australia, Turkey, etc.). | Conditional on Account Country / tax registration. | B | https://aws.amazon.com/legal/aws-contracting-party/ ; https://aws.amazon.com/agreement/recent-changes/ |
| OSM type candidate | `ict_provider.type` | Closest: **`cloud-infrastructure`**. Also fits **`cloud-platform`** (Lambda, EKS, managed DB) and **`managed-service`**. | Single enum is awkward: AWS is IaaS + PaaS + managed services under one brand. Do **not** also code `data-center` (AWS operates DCs but is not sold as a colo provider). | A (type awkwardness is modelling, not a vendor fact) | https://aws.amazon.com/about-aws/global-infrastructure/ |
| Legal / operational HQ | `headquarters` | **`us`** | SEC principal executive offices: Seattle, Washington. Same city for Amazon.com, Inc. and Amazon Web Services, Inc. No public split that would justify a different ISO code. | A | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm |
| Data processing locations | `data_processing_locations` | Public commercial Regions in (at least): US, CA, MX, BR, ZA, IN, JP, KR, SG, AU, NZ, ID, MY, TH, TW, HK, DE, IE, GB, FR, IT, ES, SE, CH, IL, BH, AE; plus GovCloud (US); China Regions operated by local partners (Sinnet / NWCD), not Amazon.com. Announced: SA, CL. | OSM has **no controlled vocabulary**. Customer data location is **region-chosen** (C). China and GovCloud are different operators/partitions. Edge / Local Zones / Outposts add further locations. | B | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; https://aws.amazon.com/about-aws/global-infrastructure/ |
| Region count (vendor claim) | (characteristic or note; not a core field) | 39 Geographic Regions, 124 AZs (vendor page as of research date) | Count changes; do not treat as immutable. | B | https://aws.amazon.com/about-aws/global-infrastructure/ |
| ISO/IEC 27001 | `certifications` (string only; **no scope field**) | ISO/IEC **27001:2022** (plus same page: 27017:2015, 27018:2019, **27701:2019**, 22301:2019, 20000-1:2018, 9001:2015, CSA STAR CCM v4.0) | **Service-scoped.** Page last updated 2026-09-01. All 7 researched AWS services are listed (EC2, S3, RDS, EKS, Lambda, VPC, IAM). Exclusions exist (e.g. Professional Services and Security Assurance Services LLC = ISO 27001 only; some features excluded on other services). **Not every AWS service; not automatically every region/feature.** | B | https://aws.amazon.com/compliance/iso-certified/ |
| ISO 27701 | `certifications` | ISO/IEC 27701:2019 listed on the same ISO certified page | Same service list caveat as ISO 27001. Certificate text itself is in Artifact (login). | B | https://aws.amazon.com/compliance/iso-certified/ |
| SOC 2 | `certifications` | SOC 2 Type II (Spring 2026 report: 188 services; period 2025-04-01 to 2026-03-31). SOC 1 and SOC 3 issued with it. | **Service-scoped.** SOC 1/2 via Artifact (account). SOC 3 public summary. Does not cover services outside the report. | B | https://aws.amazon.com/blogs/security/spring-2026-soc-1-2-and-3-reports-are-now-available-with-188-services-in-scope/ |
| PCI DSS | `certifications` | PCI DSS (and PCI 3DS) AoC available; Spring 2026 package added services/region | **Service- and region-scoped.** EC2 docs state EC2 is PCI DSS validated. Not every service/region. Customer CDE remains customer-owned. | B | https://aws.amazon.com/compliance/services-in-scope/PCI/ ; https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html |
| GDPR DPA exists | (no “DPA exists” field; nearest `gdpr_dpa_signed`) | Standard **AWS DPA exists publicly** and is incorporated into AWS Service Terms; applies automatically when customer data is processed. SCCs incorporated. | **Existence = A. Signed-for-this-customer = C.** OSM `gdpr_dpa_signed` is a customer-posture/contract boolean, not “vendor publishes a DPA”. Leave unset for a reference estate unless a specific customer contract is in evidence. | A (exists) / C (signed) | https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/aws-data-processing-addendum-dpa.html ; https://d1.awsstatic.com/legal/aws-gdpr/AWS_GDPR_DPA.pdf |
| DORA official pages | (no vendor-DORA-page field) | Official AWS DORA page + User Guide + DORA Financial Services Addendum (FSA) via Artifact | Vendor support materials. Not a customer compliance claim. | A | https://aws.amazon.com/compliance/dora/ |
| DORA CTPP | (no CTPP field) | Designated: **Amazon web Services EMEA Sarl** (ESA list 2025-11-18). AWS blog confirms AWS designated CTPP. | Designation is of the **EMEA legal entity**, not Amazon.com, Inc. Oversight ≠ customer DORA compliance. | A | https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf ; https://aws.amazon.com/blogs/security/aws-designated-as-a-critical-third-party-provider-under-eus-dora-regulation/ |
| DORA contractual notification | `dora_notification_clause` | AWS publishes a DORA FSA that “supplements existing financial services addenda” to address contracting requirements. Whether a given customer’s contract contains a DORA incident-notification clause is **not** publicly knowable. | Leave `dora_notification_clause` unset (C). Do not infer true from CTPP status. | C | https://aws.amazon.com/compliance/dora/ |
| Subcontracting allowed | `subcontracting_allowed` | Public DPA: customer gives **general authorization** to sub-processors; 30-day website notice; objection via terminate / cease service / move Region. | Public default = **conditional** (authorized list + notice + objection). Customer contracts may vary. | B | https://d1.awsstatic.com/legal/aws-gdpr/AWS_GDPR_DPA.pdf §6 |
| Public subprocessor list | `subcontractors` | Yes: https://aws.amazon.com/compliance/sub-processors/ — AWS entities (infra), AWS entities (service-specific), third parties, and a separate European Sovereign Cloud section. Relevant set depends on Region + services used. | Do **not** copy the full list into OSM `subcontractors` as if it were the customer’s chain. List is public; applicable subset is C. | A (list exists) / C (which apply) | https://aws.amazon.com/compliance/sub-processors/ |
| Public audit-rights language | `audit_rights` | DPA §10–11: customer “audit” is **instructing AWS to perform its third-party ISO/SOC audit** and receive reports under NDA. Customer may request a change of instruction; if AWS declines, customer may terminate. This is **not** an unrestricted on-site audit right. | OSM `audit_rights` is a boolean. Public language is **conditional / report-based**. Do not set `true` as if the customer has a negotiated inspection right. | B | https://d1.awsstatic.com/legal/aws-gdpr/AWS_GDPR_DPA.pdf |
| Contract dates / notice / exit / last risk assessment / risk_level | `contract_*`, `notice_period_days`, `exit_strategy_*`, `last_risk_assessment`, `risk_level` | Unknown | Customer-dependent. Customer Agreement has general termination language; that is not a customer notice period or exit strategy. | C / D | https://aws.amazon.com/agreement/ |
| Substitutability (survey, not customer risk) | `substitutability` | Survey-backed observation: AWS is one of two dominant public clouds (with Azure). Flexera 2025: enterprises AWS 53% vs Azure 50% **significant** workloads; Azure 81% vs AWS 79% when “some” workloads included; SMBs 53% AWS vs 29% Azure; GCP third (~46% some/significant all-org). Flexera 2026 (supplementary): AWS 83% vs Azure 79% some/significant; enterprise 84% vs 82%. | This supports a **low** substitutability hypothesis at market level (switching cost / skill / multi-cloud lock-in), **not** a customer `risk_level` or `concentration_risk` boolean. `concentration_risk` remains C. | B (survey) | https://resources.flexera.com/web/pdf/Flexera-State-of-the-Cloud-Report-2025.pdf ; https://www.flexera.com/blog/finops/the-latest-cloud-computing-trends-flexera-2025-state-of-the-cloud-report/ |

### Modelling notes

- Prefer **one ICT Provider** for “AWS public cloud” (`amazon-web-services` or similar), with `name` = Amazon Web Services and a provenance note that the legal parent is Amazon.com, Inc. and the EU CTPP/contracting entity is often AWS EMEA SARL. OSM cannot currently hold multiple legal entities, contracting-party tables, or CTPP status.
- `type`: `cloud-infrastructure` is the least-wrong single token. Record the enum awkwardness in the decision register rather than inventing a new type.
- `certifications`: OSM is a string array with **no scope**. Putting `ISO 27001` on the provider without a characteristic/provenance note will over-claim. Scope belongs in provenance or a characteristic, not as an implied all-services property.
- `gdpr_dpa_signed` / `dora_notification_clause` / `audit_rights` / `subcontracting_allowed` are **customer-contract posture**, even though public templates exist. For a reference estate, leave booleans null unless a fictional customer decision is explicitly labelled synthetic.
- `data_processing_locations`: there is no ISO country controlled vocabulary. A provider-level array of country names is only a **capability map**. Actual processing locations are offering/posture (region choice) and remain C.
- Shared responsibility is a **service/offering security fact**, not a provider certification: AWS is responsible for the security *of* the cloud; the customer is responsible for security *in* the cloud (config, IAM, encryption, OS on EC2, etc.).

---

## Service: Amazon EC2

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | `service.name` or offering name | Amazon Elastic Compute Cloud (Amazon EC2) | Vendor product name. | A | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html |
| Vendor definition | `service.description` | “Amazon Elastic Compute Cloud (Amazon EC2) provides on-demand, scalable computing capacity in the Amazon Web Services (AWS) Cloud.” | Paraphrase/quote of official user guide. | A | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html |
| Service vs product | (modelling) | Technological **service** an enterprise would catalog (IaaS virtual compute). Also a vendor product. | Catalog as a capability or as AWS-intrinsic compute — see modelling notes. | A | — |
| ISO 27001 / SOC / PCI | compliance evidence, not automatic service property | Listed on ISO certified page (2026-09-01). PCI DSS validated per EC2 user guide. SOC in-scope set is the Spring 2026 188-service list (confirm in Artifact). | **B — do not inherit “AWS is ISO 27001” without checking the list.** | B | https://aws.amazon.com/compliance/iso-certified/ ; https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html |
| Vendor SLA | characteristic (not `availability_target`) | Region-Level: **99.99%** monthly uptime when all running instances are concurrently across ≥2 AZs (or 2 regions if the region has one AZ). Instance-Level: **99.5%** per instance. Credits, not enterprise RTO. Last updated 2022-05-25. | Configuration-conditional. Exclusions apply. | B | https://aws.amazon.com/compute/sla/ |
| Offerings / SKUs | offering + characteristics | Instance families/types (1000+ claimed), purchase models (On-Demand, Spot, Reserved, Savings Plans, Dedicated Hosts, Capacity Reservations), OS/AMI, Nitro, Mac instances, placement (AZ, Local Zone, Outposts, Wavelength), tenancy. | Offering-level. | B | https://aws.amazon.com/ec2/ ; https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html |
| Data residency | characteristic / offering | Customer chooses Region (and AZ). AWS DPA: AWS will not transfer Customer Data from selected Region(s) except as necessary to provide initiated services or legal compulsion. | Region choice = C. Cross-region features (AMI copy, snapshots) are customer-initiated. | B / C | https://d1.awsstatic.com/legal/aws-gdpr/AWS_GDPR_DPA.pdf §12.1 |
| Shared responsibility | posture/security note | Customer owns guest OS, apps, security groups, IAM, encryption, patching. AWS owns hypervisor, facilities, physical network. | Classic IaaS split. | A | AWS Shared Responsibility Model (standard AWS compliance docs) |
| AI involvement | (note) | EC2 is general compute; GPU/Trainium/Inferentia instance types exist for ML. Not “Lambda AI”. Azure OpenAI is out of scope. | Intrinsic only as instance SKUs. | B | https://aws.amazon.com/ec2/ |

### Modelling notes

- Natural OSM: **(a) capability Service** `compute.virtual-machine` with offering `…aws-ec2`, **or (b)** provider-intrinsic `aws.ec2`. (a) better tests Service→Offering→Provider. (b) matches how enterprises buy it.
- Do not put vendor SLA into `service_posture.availability_target` (that is the enterprise target).

---

## Service: Amazon S3

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Amazon Simple Storage Service (Amazon S3) | | A | https://aws.amazon.com/s3/ |
| Vendor definition | description | “Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.” | Official product page. | A | https://aws.amazon.com/s3/ |
| Service vs product | | Technological object-storage **service**; also the canonical AWS product. | | A | — |
| ISO / SOC / PCI | compliance evidence | Listed on ISO certified page (2026-09-01). Confirm SOC/PCI columns on services-in-scope. | B | B | https://aws.amazon.com/compliance/iso-certified/ |
| Vendor SLA | characteristic | Credit tables imply commitments of **99.9%** monthly uptime for S3 Standard, Express One Zone, Glacier Flexible Retrieval, Glacier Deep Archive (and “all other requests not specified”); **99.0%** for Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier Instant Retrieval. Last updated 2023-11-28. Product page separately claims **99.99% availability design** and **11 nines durability** — that is a design/durability claim, **not** the SLA credit threshold. | Class/region/AZ (Express One Zone) conditional. | B | https://aws.amazon.com/s3/sla/ ; https://aws.amazon.com/s3/ |
| Offerings | offering | Storage classes (Standard, Intelligent-Tiering, IA, One Zone-IA, Glacier Instant/Flexible/Deep Archive, Express One Zone), S3 Tables, S3 Vectors, replication, Object Lock. | Offering-level. | B | https://aws.amazon.com/s3/ |
| Data residency | | Bucket is regional (except multi-AZ/One Zone classes). Customer chooses Region. | C for actual location. | B / C | https://aws.amazon.com/s3/ |
| Shared responsibility | | AWS: infrastructure, durability of stored objects (as designed). Customer: bucket policies, encryption keys (if CMK), public access, replication topology. | | A | — |
| AI | | S3 Vectors / data-lake-for-AI messaging on product page. Storage substrate, not a foundation-model service. | B | B | https://aws.amazon.com/s3/ |

### Modelling notes

- Prefer capability `storage.object` with offering `…aws-s3` (and further offerings per class if the estate requests classes separately). Storage class is the main Offering grain.

---

## Service: Amazon RDS

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Amazon Relational Database Service (Amazon RDS) | Distinct from Amazon Aurora (RDS family / sibling product). | A | https://aws.amazon.com/rds/ |
| Vendor definition | description | “Amazon Relational Database Service (Amazon RDS) is an easy-to-manage relational database service optimized for total cost of ownership.” Automates provisioning, backup, patching; engines include PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, Db2. | Official page. Aurora is marketed separately on the same page. | A | https://aws.amazon.com/rds/ |
| Service vs product | | Managed relational-database **service**. | | A | — |
| ISO | compliance evidence | Listed on ISO certified page. | B | B | https://aws.amazon.com/compliance/iso-certified/ |
| Vendor SLA | characteristic | Multi-AZ instance/cluster: credit below **99.95%**. Single-AZ: credit below **99.5%**. Engines listed: PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, Db2. Last updated 2024-01-22. Micro/similar classes excluded. | Deployment-option conditional. | B | https://aws.amazon.com/rds/sla/ |
| Offerings | offering | Engine × edition × Single-AZ vs Multi-AZ instance vs Multi-AZ cluster; RDS Custom; RDS on Outposts; instance class; storage type. Aurora should be a **separate** offering or service if used. | Offering-level. | B | https://aws.amazon.com/rds/ ; https://aws.amazon.com/rds/sla/ |
| Data residency | | Regional; Multi-AZ stays in Region; snapshots/replicas may cross Region if customer configures. | C | B / C | — |
| Shared responsibility | | AWS: OS, engine patching (standard RDS), hardware. Customer: schema, queries, users inside DB, parameter groups, encryption key choice, network (SG/VPC). RDS Custom shifts more OS responsibility to customer. | B (Custom vs standard) | — |
| AI | | pgvector / generative-AI messaging for PostgreSQL/Aurora on product page. Not a separate AI service. | B | https://aws.amazon.com/rds/ |

### Modelling notes

- Capability `data.relational-database` with provider offerings, **or** intrinsic `aws.rds` with engine offerings. Do not treat “RDS” and “Aurora” as the same offering.

---

## Service: Amazon EKS

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Amazon Elastic Kubernetes Service (Amazon EKS) | | A | https://aws.amazon.com/eks/ |
| Vendor definition | description | “Amazon Elastic Kubernetes Service (Amazon EKS) enables teams of any size or skill level to build, run, and scale production-ready applications easily across any environment.” | Official page. | A | https://aws.amazon.com/eks/ |
| Service vs product | | Managed Kubernetes **service** (control plane). Nodes may be EC2, Fargate, Auto Mode, Hybrid, Outposts, EKS Anywhere. | Hybrid/Anywhere changes the service boundary. | B | https://aws.amazon.com/eks/ |
| ISO | | Listed on ISO certified page. | B | B | https://aws.amazon.com/compliance/iso-certified/ |
| Vendor SLA | characteristic | Standard control plane: **99.95%** (5-min intervals). Provisioned control plane: **99.99%** (1-min). Covers Kubernetes **endpoint**, not worker nodes (nodes under Compute SLA). Fargate-for-EKS under Fargate/ECS SLA. Last updated 2026-03-20. | Control-plane mode conditional. | B | https://aws.amazon.com/eks/sla/ |
| Offerings | offering | Standard vs Provisioned control plane; Auto Mode; Fargate; Hybrid Nodes; Outposts; EKS Anywhere; Kubernetes version. | Offering-level. | B | https://aws.amazon.com/eks/ ; https://aws.amazon.com/eks/sla/ |
| Data residency | | Cluster is regional. etcd/control plane in Region; node data where nodes run. | C | B / C | — |
| Shared responsibility | | AWS: managed control plane. Customer: cluster config, RBAC, node/OS (unless Auto Mode/Fargate), workloads, network policies. | B | https://aws.amazon.com/eks/sla/ |
| AI | | Product page markets GenAI training/inference on EKS. Platform, not a model API. | B | https://aws.amazon.com/eks/ |

### Modelling notes

- Strong candidate for capability Service `compute.kubernetes` with offerings `…aws-eks`, `…azure-aks`, `…gcp-gke`. That is the OSM example pattern. Provider-intrinsic `aws.eks` also valid if the estate catalogs vendor products.

---

## Service: AWS Lambda

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | AWS Lambda | | A | https://aws.amazon.com/lambda/ |
| Vendor definition | description | Product page positions Lambda as “Serverless compute for every workload” / “Run code at any scale with zero infrastructure management.” | Marketing + product definition. Functions vs MicroVMs vs Managed Instances are now distinct modes. | A | https://aws.amazon.com/lambda/ |
| Service vs product | | Serverless function **service**. | | A | — |
| ISO | | Listed on ISO certified page. | B | B | https://aws.amazon.com/compliance/iso-certified/ |
| Vendor SLA | characteristic | **99.95%** Monthly Uptime Percentage **per AWS Region**. Last updated 2022-05-22. | Region-level. Excludes customer 500/503, VPC/SG misconfig, etc. | B | https://aws.amazon.com/lambda/sla/ |
| Offerings | offering | Functions (default); MicroVMs; Managed Instances; durable functions; architecture (x86/Arm); VPC-attached vs public. | Offering-level. | B | https://aws.amazon.com/lambda/ |
| Data residency | | Function is regional. Invocations/logs may involve CloudWatch in Region. Cross-region triggers are customer-configured. | C | B / C | — |
| Shared responsibility | | AWS: runtime platform, scaling, isolation. Customer: function code, dependencies, IAM role, secrets, event-source auth, VPC config. | A | https://aws.amazon.com/lambda/sla/ |
| AI | | Product page: “AI agent orchestration”, “AI-generated code” in MicroVMs, LangGenius plugin sandboxes. **Not** a foundation-model API. Lambda is not “Lambda AI” as a separate certified AI system. Azure OpenAI is out of scope. | B | https://aws.amazon.com/lambda/ |

### Modelling notes

- Capability `compute.functions` vs intrinsic `aws.lambda`. Comparability with Azure Functions and Cloud Run is a **stress point** (see below): Cloud Run is container-as-a-service, not only functions.

---

## Service: Amazon VPC

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Amazon Virtual Private Cloud (Amazon VPC) | | A | https://aws.amazon.com/vpc/ |
| Vendor definition | description | “Amazon Virtual Private Cloud (Amazon VPC) gives you full control over your virtual networking environment, including resource placement, connectivity, and security.” Product page subtitle: “Define and launch AWS resources in a logically isolated virtual network.” | Official. | A | https://aws.amazon.com/vpc/ |
| Service vs product | | Networking **service** *and* the default **tenancy/isolation boundary** for most AWS accounts. Dual nature is the modelling stress. | A | — |
| ISO | | Listed as Amazon Virtual Private Cloud (VPC) on ISO certified page. | B | B | https://aws.amazon.com/compliance/iso-certified/ |
| Vendor SLA | characteristic | **No general VPC SLA found.** Published SLA is **NAT Gateway only: 99.9%**. Other attachments (TGW, VPN, PrivateLink, endpoints) have their own docs/SLAs if any. | Do not invent a VPC uptime %. | A (NAT SLA) / D (core VPC) | https://aws.amazon.com/vpc/sla/ |
| Offerings | offering | VPC itself; subnets; NAT Gateway (public/private/regional); endpoints; peering; IPAM; Lattice/PrivateLink as adjacent products. | Offering-level. NAT is a billable service with SLA; the VPC construct is often “free/default”. | B | https://aws.amazon.com/vpc/ |
| Data residency | | VPC is regional. CIDR/subnets in AZs of that Region. | C | B / C | — |
| Shared responsibility | | AWS: underlying network fabric. Customer: CIDR, route tables, NACLs, SGs, peering, hybrid connectivity. | A | https://aws.amazon.com/vpc/ |
| AI | | None intrinsic. | A | — |

### Modelling notes

- If modelled as capability `network.virtual-network`, offerings can be AWS/Azure/GCP VPC. If modelled as tenancy boundary, it is closer to an **account characteristic** than a requestable service — OSM has no tenancy entity.

---

## Service: AWS IAM

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | AWS Identity and Access Management (IAM) | Distinct from **IAM Identity Center** (workforce SSO). Both appear on ISO list. | A | https://aws.amazon.com/iam/ |
| Vendor definition | description | “Use AWS Identity and Access Management (IAM) to manage and scale workload and workforce access securely supporting your agility and innovation in AWS.” | Account-scoped authorization to AWS APIs/resources. | A | https://aws.amazon.com/iam/ |
| Service vs product | | Control-plane **service** (and a prerequisite of the AWS account). Enterprises often do **not** catalog IAM as a business-facing service; they catalog IAM Identity Center / Entra / Okta as the IdP. | Conceptual mismatch with Entra. | A | — |
| ISO | | AWS Identity and Access Management (IAM) and AWS IAM Identity Center both listed. | B | B | https://aws.amazon.com/compliance/iso-certified/ |
| Vendor SLA | characteristic | **No public IAM availability SLA found.** | D | D | — |
| Offerings | offering | IAM (per-account users/roles/policies); IAM Identity Center (workforce, multi-account); SCPs via Organizations. These are **different products**. | Do not merge IAM and Identity Center. | B | https://aws.amazon.com/iam/ |
| vs Entra / Cloud IAM | (stress) | AWS IAM = **cloud-account authorization**. It is not an enterprise IdP. Workforce federation is IAM Identity Center or external IdP (Entra, Okta). Entra ID is a tenant-wide directory/IdP for M365 + Azure + SaaS. GCP Cloud IAM is project/org policy for GCP resources, similarly not Entra. | A | https://aws.amazon.com/iam/ ; https://learn.microsoft.com/en-us/entra/fundamentals/whatis |
| Data residency | | IAM is a **global** AWS service (us-east-1 control plane historically); Identity Center instance has Region choice. Exact residency of IAM identity data is **not fully customer-selectable** the way S3 is. | B / D | D for precise country list |
| Shared responsibility | | AWS: IAM service availability/integrity. Customer: policies, unused access, key rotation, federation design. | A | — |
| AI | | None intrinsic (Access Analyzer is analysis, not generative AI as a product). | B | — |

### Modelling notes

- Do **not** model AWS IAM as the same Service as Microsoft Entra ID. Entra is an enterprise IdP; IAM is cloud-platform RBAC. A capability Service `identity.access-management` with offerings `aws-iam`, `entra-id`, `gcp-iam` **over-unifies** them and will produce false DORA/substitutability mappings.
- Better: `identity.cloud-authorization` (AWS IAM / Azure RBAC / GCP IAM) vs `identity.directory-idp` (Entra, Okta, IAM Identity Center).

---

## Provider: Microsoft (Azure + Microsoft 365 as one legal-entity problem)

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Legal name | `name` | **Microsoft Corporation** (Washington corporation). Principal executive offices: One Microsoft Way, Redmond, WA 98052-6399. | Parent. Azure, Microsoft 365, Dynamics, Entra are product families, not separate listed companies. | A | https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm |
| Common EU contracting party | (no field) | **Microsoft Ireland Operations Limited (MIOL)** is frequently the Online Services / Cloud Agreement party and is the **DORA CTPP** name. Other countries invoice from local entities (e.g. Microsoft Srl in Italy). | Channel- and country-dependent (EA, MCA, CSP, MOSA). | B | https://learn.microsoft.com/en-us/compliance/dora/dora-what-is-dora ; https://learn.microsoft.com/en-us/azure/cost-management-billing/microsoft-customer-agreement/microsoft-customer-agreement-faq |
| GitHub | (provider split) | GitHub is a Microsoft subsidiary with **separate** product terms, DPA, and often a separate seller of record. Not the same Online Services stack as Azure/M365. | If the estate uses GitHub, it is a **second ICT Provider** or at least a distinct contract — even though the parent is Microsoft Corporation. | A (corporate) / B (contract) | Microsoft 10-K (subsidiaries); GitHub terms not fetched in full here |
| OSM type candidate | `type` | No single enum works. Azure ≈ `cloud-infrastructure` + `cloud-platform`. M365 ≈ `software-vendor` (SaaS). Entra ≈ identity platform. GitHub ≈ `software-vendor`. | **This is the legal-entity problem:** one `Microsoft Corporation` vs many ICT Providers (Azure vs M365 vs GitHub vs Entra). Splitting by product family is more useful than one row; merging hides DORA/certification grain. | A (awkwardness) | — |
| HQ | `headquarters` | **`us`** | Legal and operational HQ both Redmond, WA. MIOL is Dublin contracting/CTPP entity, not HQ. | A | https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm |
| Data processing locations | `data_processing_locations` | Public Azure geographies include (available or coming soon): US, BE, BR, CA, CL, MX, AU, CN (21Vianet), IN, ID, JP, KR, MY, NZ, TW, AT, DK, FI, FR, DE, GR, IT, NO, PL, ES, SE, CH, GB, ZA, IL, QA, AE, SA, plus Azure Government and other sovereign clouds. M365 has its own datacenter map / EU Data Boundary. | OSM has no vocabulary. **Azure region ≠ M365 geo ≠ Entra tenant geo.** China operated by 21Vianet. Service availability varies by region. | B | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ; https://learn.microsoft.com/en-us/azure/reliability/regions-list |
| ISO/IEC 27001 | `certifications` | Microsoft Azure, Dynamics 365, Power Platform, and **select Microsoft 365** services are audited for ISO/IEC 27001. Certificates and SoA on Service Trust Portal (login). Azure ISO 27001 page still mentions ISO/IEC 27001:2013 in places; STP lists current Azure/Dynamics ISO 27001 **and 27701** certificates (e.g. dated 2026-06-25). | **Certificate family + date + in-scope service list required.** Azure certificate does not automatically cover every Azure SKU, Azure Government, Azure China (21Vianet), M365, or GitHub. M365 has **separate** Office 365 audit streams. | B | https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-iso-27001 ; https://servicetrust.microsoft.com/viewpage/ISOIEC ; https://learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope |
| ISO 27701 | `certifications` | Covered in Azure/Dynamics/Online Services ISO 27001+27701 certificates / SoA on STP (2026 artifacts listed). | Same scope caveats. | B | https://servicetrust.microsoft.com/viewpage/ISOIEC |
| SOC 2 | `certifications` | SOC 2 Type 2 for Azure and many Online Services; **separate** Office 365 SOC 2; **separate** Azure DevOps SOC 2. | Multiple reports. Not one “Microsoft SOC 2”. | B | https://learn.microsoft.com/en-us/compliance/regulatory/offering-soc-2 |
| PCI | `certifications` | Azure PCI DSS attestations exist (Compliance Offerings / STP). Scope is service-listed, not all Azure. | B | B | https://learn.microsoft.com/en-us/azure/compliance/offerings/ |
| GDPR DPA exists | `gdpr_dpa_signed` | **Microsoft Products and Services Data Protection Addendum (DPA)** is published on the Licensing Documents site (current + archives). It is an addendum to Product Terms for Online Services. | Existence = A. Whether a given customer “signed” it = C (often incorporated by reference, not a wet signature). | A / C | https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA |
| DORA official pages | | Learn DORA hub + Trust Center DORA page + Contract Stack Mapping (Art. 30 / RTS 53) + DORA Addendum for eligible FSI + FSA. | A | A | https://learn.microsoft.com/en-us/compliance/dora/dora-what-is-dora ; https://learn.microsoft.com/en-us/compliance/dora/dora-contract-mapping ; https://www.microsoft.com/en-us/trust-center/compliance/dora-compliance |
| DORA CTPP | | **Microsoft Ireland Operations Limited** designated CTPP (ESA list 2025-11-18). Microsoft Learn confirms MIOL. | Parent Microsoft Corporation is **not** the listed CTPP name. | A | https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf ; https://learn.microsoft.com/en-us/compliance/dora/dora-what-is-dora |
| DORA notification clause | `dora_notification_clause` | Mapping document says the DORA Addendum + FSA + DPA + SLA address Art. 30 contractual points, including (but not limited to) listed items. Whether a given customer executed the DORA Addendum is C. | C | https://learn.microsoft.com/en-us/compliance/dora/dora-contract-mapping |
| Subcontracting | `subcontracting_allowed` | DPA: customer consents to Microsoft Affiliates and hired Subprocessors; Microsoft remains responsible. Notice: Learn page states **≥6 months** for new subprocessors that process Customer Data (except AI functionality: ≥30 days + ability to disable for ≥6 months); **≥30 days** for other Personal Data. Objection via termination of affected service. | Public default = **conditional**. | B | https://learn.microsoft.com/en-us/compliance/assurance/assurance-supplier-management |
| Public subprocessor list | `subcontractors` | Microsoft Online Services Subprocessor List on Service Trust Portal (DocumentPage id in Learn). Separate commercial support / consulting supplier lists. | Login/STP. Applicable subset is C. | A (list exists) / C | https://learn.microsoft.com/en-us/compliance/assurance/assurance-supplier-management ; https://www.microsoft.com/en-us/professionalservices/suppliers |
| Audit rights language | `audit_rights` | April 2025 DPA copy: Microsoft runs annual third-party audits and publishes reports on STP. If those cannot reasonably satisfy GDPR audit requirements, Microsoft will respond to additional audit instructions; scope/timing/fees mutually agreed; independent accredited firm; customer pays costs; no access to other customers’ data. | Conditional, not a free-form inspection right. Official current DPA is the Licensing Documents download (login/redirect). | B | https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA ; April 2025 DPA text as published in public copies |
| Contract / risk / exit fields | various | Unknown | C / D | — |
| Substitutability | `substitutability` | Flexera 2025: Azure 81% vs AWS 79% of **enterprises** when “some” workloads included; AWS 53% vs Azure 50% **significant**; SMBs favour AWS (53% vs 29%). Flexera 2026: still neck-and-neck (Azure 79% / AWS 83% some+significant all-org). Microsoft is also the dominant **non-SaaS software** vendor in the same survey. | Market concentration observation only. M365 lock-in is a **different** concentration than Azure IaaS. Do not invent customer `concentration_risk`. | B | https://resources.flexera.com/web/pdf/Flexera-State-of-the-Cloud-Report-2025.pdf |

### Modelling notes

- **Do not** treat “Microsoft” as one ICT Provider without recording the split. Recommended investigation options (decision register, not schema change): (1) one provider + offering-level product-family characteristics; (2) multiple providers (`microsoft-azure`, `microsoft-365`, `github`, `microsoft-entra`) sharing parent name in provenance; (3) one provider for legal entity + services pointing at it (hides contract/cert grain).
- Entra ID is **shared substrate** for Azure, M365, and Dynamics (“every new directory… if you’re a Microsoft 365, Azure, or Dynamics CRM Online subscriber, you’re already using Microsoft Entra ID”). That breaks a clean Azure-only provider boundary.
- `type` cannot express “IaaS + SaaS + IdP + developer platform under one corporation”.
- Certification strings on a single Microsoft provider row will be read as covering M365 + Azure + GitHub — that is false.

---

## Service: Azure Virtual Machines

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Azure Virtual Machines | | A | https://learn.microsoft.com/en-us/azure/virtual-machines/availability |
| Vendor definition | description | IaaS VMs: on-demand scalable compute in Azure (availability options documented as Availability Zones, availability sets, scale sets). 10-K: Azure includes IaaS/PaaS for computing. | Prefer Learn/product docs over China SLA pages. | A | https://learn.microsoft.com/en-us/azure/virtual-machines/availability ; https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm |
| Service vs product | | Technological compute **service**. | | A | — |
| ISO | | In Azure ISO 27001 audit scope **if** listed on the current certificate (Azure VMs are core Azure). Confirm in STP certificate, not by brand. | B | B | https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-iso-27001 |
| Vendor SLA | characteristic | Widely documented: **99.99%** connectivity to ≥1 instance when ≥2 VMs across ≥2 AZs; **99.95%** for ≥2 VMs in an availability set; single-instance **99.9%** with Premium/Ultra disks (lower for Standard SSD/HDD). **Authoritative text** is the consolidated Online Services SLA (latest English edition listed September 2026 on Licensing Documents). China 21Vianet pages match these percentages but are a different operator. | Configuration-conditional. Use WW SLA PDF for a given customer, not azure.cn. | B | https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1 ; https://learn.microsoft.com/en-us/azure/virtual-machines/availability |
| Offerings | offering | Size/family, spot vs reserved, availability set vs AZ vs scale set, Dedicated Host, disk type, OS image, region. | Offering-level. | B | https://learn.microsoft.com/en-us/azure/virtual-machines/availability |
| Data residency | | Regional (+ AZ). Paired-region GRS is a storage/ASR concern, not automatic for VM disks. | C | B / C | https://learn.microsoft.com/en-us/azure/reliability/regions-list |
| Shared responsibility | | Classic IaaS: customer OS/app; Microsoft hypervisor/facility. | A | — |
| AI | | GPU SKUs exist. Not Azure OpenAI. | B | — |

### Modelling notes

- Pair with AWS EC2 / GCP Compute Engine under `compute.virtual-machine` if testing capability Services.

---

## Service: Azure Blob Storage

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Azure Blob Storage (part of Azure Storage) | | A | https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy |
| Vendor definition | description | Object storage for unstructured data (blobs) with hot/cool/cold/archive tiers and LRS/ZRS/GRS/RA-GRS/GZRS/RA-GZRS redundancy. | Learn. | A | https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview |
| Service vs product | | Object-storage **service**. | | A | — |
| ISO | | Azure Storage typically in Azure ISO scope — confirm current certificate. | B | B | https://learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope |
| Vendor SLA | characteristic | Learn redundancy table: Hot reads/writes generally **≥99.9%** (LRS/ZRS/GRS); RA-GRS/RA-GZRS **reads ≥99.99%** (retry on secondary); cool/cold/archive **99%** (RA secondary reads 99.9%). Durability claims (11/12/16 nines) are **not** the availability SLA. Points to `https://azure.microsoft.com/support/legal/sla/storage/v1_5/`. | Redundancy × tier conditional. | B | https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy |
| Offerings | offering | Account kind; redundancy; access tier; hierarchical namespace (ADLS Gen2). | Offering-level. | B | same |
| Data residency | | Primary region required; GRS uses paired/secondary region (data leaves primary). LRS/ZRS stay in-region. | B / C | same |
| Shared responsibility | | Microsoft: platform durability/replication as configured. Customer: keys, access, public containers, lifecycle. | A | — |
| AI | | Common training-data store. Not a model service. | B | — |

---

## Service: Azure SQL Database

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Azure SQL Database | Distinct from SQL Managed Instance, SQL Server on VMs, Synapse. | A | https://learn.microsoft.com/en-us/azure/reliability/reliability-sql-database |
| Vendor definition | description | Fully managed relational database (PaaS) with built-in HA and optional geo-replication. | Learn / China SLA blurb (same product). | A | https://learn.microsoft.com/en-us/azure/reliability/reliability-sql-database |
| Service vs product | | Managed relational **service**. | | A | — |
| ISO | | Typically in Azure ISO scope — confirm certificate. | B | B | https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-iso-27001 |
| Vendor SLA | characteristic | Zone-redundant supported tiers: higher SLA (**99.995%** on documented ZR GP/BC/Premium/Hyperscale). Non-ZR commonly **99.99%**. Hyperscale varies by replica count (docs cite 99.95% / 99.9% for one/zero replicas on some SLA versions). Basic/Standard: no zone redundancy. **Authoritative:** Online Services SLA PDF (Sept 2026 listing). | Tier × zone-redundancy × replica count. | B | https://learn.microsoft.com/en-us/azure/reliability/reliability-sql-database ; https://learn.microsoft.com/en-us/azure/azure-sql/database/high-availability-sla-local-zone-redundancy?view=azuresql |
| Offerings | offering | DTU vs vCore; Basic/Standard/Premium vs GP/BC/Hyperscale; single DB vs elastic pool vs (separate) Managed Instance; zone redundant; geo-replication. | Offering-level. | B | same |
| Data residency | | Regional; geo-replication is customer-opted and crosses regions. | C | B / C | same |
| Shared responsibility | | Microsoft: patching, HA fabric. Customer: auth, TDE keys (if BYOK), firewall, queries, classification. | A | — |
| AI | | Intelligent tuning / threat detection are platform features, not Azure OpenAI. | B | — |

---

## Service: Azure Kubernetes Service (AKS)

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Azure Kubernetes Service (AKS) | | A | https://learn.microsoft.com/en-us/azure/aks/free-standard-pricing-tiers |
| Vendor definition | description | Managed Kubernetes: Microsoft manages the control plane; customer (or Automatic SKU) manages/uses nodes. | Learn. | A | https://learn.microsoft.com/en-us/azure/aks/free-standard-pricing-tiers |
| Service vs product | | Managed Kubernetes **service**. | | A | — |
| ISO | | Confirm on current Azure certificate (AKS is a standard Azure service). | B | B | https://learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope |
| Vendor SLA | characteristic | **Free tier: no financially backed SLA** (internal goal ~99.5% API server). **Standard/Premium:** Uptime SLA **99.95%** API server with AZs, **99.9%** without. Nodes covered by **VM SLA**. Automatic SKU includes Standard + pod readiness SLA. | Tier-conditional. | B | https://learn.microsoft.com/en-us/azure/aks/free-standard-pricing-tiers ; https://azure.microsoft.com/en-gb/pricing/details/kubernetes-service/ |
| Offerings | offering | Free / Standard / Premium; Automatic vs standard node-pool management; LTS on Premium; region/AZ. | Offering-level. | B | same |
| Data residency | | Regional cluster. | C | B / C | — |
| Shared responsibility | | Microsoft: managed control plane (and nodes on Automatic). Customer: cluster config, workloads, node pools (standard). | B | same |
| AI | | Common GPU node pools. Not Azure OpenAI. | B | — |

---

## Service: Azure Functions

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Azure Functions | | A | https://azure.microsoft.com/en-us/products/functions |
| Vendor definition | description | Event-driven serverless functions on Azure; plans include Flex Consumption, App Service, Container Apps. | Official product page. | A | https://azure.microsoft.com/en-us/products/functions |
| Service vs product | | Serverless function **service**. | | A | — |
| ISO | | Confirm current Azure certificate. | B | B | https://learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope |
| Vendor SLA | characteristic | Product FAQ: Flex Consumption or App Service plan **99.95%**. (Consumption-plan wording on older China summary also 99.95% after successful trigger.) Authoritative: Online Services SLA PDF. | Plan-conditional. | B | https://azure.microsoft.com/en-us/products/functions |
| Offerings | offering | Flex Consumption, Consumption, Premium, App Service, Container Apps plans. | Offering-level. | B | same |
| Data residency | | Regional function app. | C | B / C | — |
| Shared responsibility | | Microsoft: host platform. Customer: code, bindings, keys, identity, network isolation. | A | — |
| AI | | Triggers/bindings to other services; not Azure OpenAI unless the customer binds it. | C (if used) | — |

---

## Service: Azure Virtual Network

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Azure Virtual Network (VNet) | | A | https://azure.microsoft.com/en-us/products/virtual-network |
| Vendor definition | description | “Azure Virtual Network lets you build an isolated, secure environment to run virtual machines (VMs) and applications.” Optional hybrid via VPN/ExpressRoute. | Official. | A | https://azure.microsoft.com/en-us/products/virtual-network |
| Service vs product | | Networking service **and** Azure subscription isolation boundary (similar to AWS VPC). | A | — |
| ISO | | Confirm Azure certificate. | B | B | https://learn.microsoft.com/en-us/azure/compliance/offerings/cloud-services-in-audit-scope |
| Vendor SLA | characteristic | **No standalone financially backed VNet SLA found** on global pages in this research. VM SLA defines “Virtual Network” and measures **VM connectivity** (which may traverse a VNet). Do not invent a VNet %. | D (core VNet) / B (VM connectivity SLA) | https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1 |
| Offerings | offering | VNet; peering; NAT gateway; VNet Manager; Route Server; Private Endpoint/Link (adjacent). | Offering-level. | B | https://azure.microsoft.com/en-us/products/virtual-network |
| Data residency | | Regional. Peering/global VNet peering can cross regions. | C | B / C | — |
| Shared responsibility | | Microsoft: fabric. Customer: address space, NSGs, peering, hybrid. | A | — |
| AI | | None intrinsic. | A | — |

---

## Service: Microsoft Entra ID

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Microsoft Entra ID (formerly Azure Active Directory) | Part of the **Microsoft Entra** product family (ID, Domain Services, ID Governance, External ID, Workload ID, Agent ID, etc.). | A | https://learn.microsoft.com/en-us/entra/fundamentals/whatis |
| Vendor definition | description | “Microsoft Entra ID is the foundational product of Microsoft Entra. It's a cloud-based identity and access management service that provides authentication, policy enforcement, and protection for users, devices, apps, and resources.” “If you're a Microsoft 365, Azure, or Dynamics CRM Online subscriber, you're already using Microsoft Entra ID — every tenant is automatically a Microsoft Entra tenant.” | Official Learn. | A | https://learn.microsoft.com/en-us/entra/fundamentals/whatis |
| Service vs product | | Enterprise **IdP / directory service** (SaaS identity). Not equivalent to AWS IAM. | A | — |
| ISO / SOC | | Entra/Azure AD typically covered under Microsoft Online Services / Azure or M365 audit packages — **confirm the specific certificate**. Do not assume the Azure ISO list equals Entra Free. | B | B | https://learn.microsoft.com/en-us/azure/compliance/offerings/ ; https://learn.microsoft.com/en-us/compliance/regulatory/offering-soc-2 |
| Vendor SLA | characteristic | Public SLA performance page + China SLA (Premium): **99.99%** authentication availability. Scribd October 2025 consolidated SLA excerpt: Entra ID Basic **and** Premium; downtime = users cannot log in or tokens not emitted; credits from <99.99%. **Authoritative:** September 2026 Online Services SLA PDF. Historical: 99.99% auth SLA announced 2021 (then Azure AD). | Edition-conditional (Free vs P1/P2 may differ — confirm current WW SLA). Performance table is global, not a customer SLO. | B | https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-sla-performance ; https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1 |
| Offerings | offering | Free / P1 / P2 / Entra Suite; External ID; Domain Services; ID Governance; Workload ID; Agent ID. Licenses also bundled in M365 / EMS. | Offering-level. **Do not** collapse the family into one offering. | B | https://learn.microsoft.com/en-us/entra/fundamentals/whatis |
| vs AWS IAM / GCP IAM | | Entra = **enterprise directory + IdP** (users, Conditional Access, SaaS SSO, device). AWS IAM = **AWS-account resource authorization**. GCP IAM = **GCP resource authorization**. Federation: Entra often *is* the IdP for AWS Identity Center / GCP Workforce Identity. | A | https://learn.microsoft.com/en-us/entra/fundamentals/whatis ; https://aws.amazon.com/iam/ |
| Data residency | | Tenant geo / EU Data Boundary options exist; exact residency is tenant- and feature-conditional (not a customer-picked “region” like a VM). | B / C | D for a complete country list without tenant config |
| Shared responsibility | | Microsoft: IdP platform. Customer: Conditional Access, lifecycle, app registrations, guest access, privileged roles. | A | https://learn.microsoft.com/en-us/compliance/dora/dora-entra |
| AI | | Entra integrates with Security Copilot; Agent ID for AI agents. Intrinsic-adjacent, not Azure OpenAI. | B | https://learn.microsoft.com/en-us/entra/fundamentals/whatis |
| DORA note | | Microsoft publishes Entra-specific DORA guidance: Entra can support some ICT risk controls; **IAM alone is not DORA compliance**. | A | https://learn.microsoft.com/en-us/compliance/dora/dora-entra |

### Modelling notes

- Provider link is **Microsoft**, not “Azure only”. Putting Entra only under an Azure provider hides M365 dependency.
- Natural Service: `identity.directory` / `identity.idp` with offering `microsoft-entra-id`. Not the same Service as `aws.iam`.

---

## Provider: Google Cloud

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Legal names | `name` | Operating cloud brand: **Google Cloud**. Ultimate parent: **Alphabet Inc.** Contracting default US: **Google LLC**, 1600 Amphitheatre Parkway, Mountain View, CA 94043. EMEA (except FR/IT/PL): **Google Cloud EMEA Limited**, 70 Sir John Rogerson’s Quay, Dublin 2, Ireland. FR/IT/PL and other countries have local Cloud entities. | “Google” in the Cloud ToS means the entity at cloud.google.com/terms/google-entity. Privacy notice also names Google LLC as primary controller of Service Data. | A | https://cloud.google.com/terms ; https://cloud.google.com/terms/google-entity ; https://cloud.google.com/terms/cloud-privacy-notice |
| OSM type candidate | `type` | Closest: **`cloud-infrastructure`** / **`cloud-platform`**. Same enum awkwardness as AWS (IaaS + PaaS + serverless). Workspace is a different product family (often same DPA, different SoW). | Single enum insufficient. | A (awkwardness) | https://cloud.google.com/terms/data-processing-addendum |
| HQ | `headquarters` | **`us`** | Google LLC / Alphabet operational HQ: Mountain View, CA. ISO 27001 certificate: ISMS centrally managed from Mountain View. Dublin is EMEA contracting/CTPP, not HQ. | A | https://cloud.google.com/terms/cloud-privacy-notice ; Firebase/Google Cloud ISO 27001 certificate excerpt (Mountain View) |
| Data processing locations | `data_processing_locations` | 43 regions / 130 zones (locations page last updated 2026-08-31). Countries include US, CA, MX, BR, CL, BE, NL, DE, FI, FR, GB, CH, IT, PL, ES, SE, QA, IL, SA, IN, JP, KR, TW, SG, ID, AU, ZA, and others. Some regions (Stockholm, Mexico, Osaka, Montreal) noted as still expanding physical DC count. ISO 27001 certificate lists in-scope DC cities (owned or leased). | No OSM vocabulary. Service availability ≠ region list. Customer location = C. | B | https://cloud.google.com/about/locations ; https://docs.cloud.google.com/docs/geography-and-regions |
| ISO/IEC 27001 | `certifications` | ISO/IEC **27001:2022** for Google Cloud ISMS; **Enterprise Customers**; product/location scoped on the certificate. Public compliance page lists governed services including Compute Engine, Cloud Storage, Cloud SQL, GKE, Cloud Run / Cloud Run functions, VPC-related networking, **Identity & Access Management (IAM)**. Certificate re-issue example: 2026-01-12, expires 2027-05-14. | **Service- and location-scoped. Enterprise-customer limitation on certificate text.** Not every Google product (Ads vs Cloud vs Workspace have related but distinct certs). | B | https://cloud.google.com/security/compliance/iso-27001 |
| ISO 27701 | `certifications` | DPA commits to ISO 27001 and additional certs in Appendix 4; GCP audited services also ISO 27017/27018 and PCI AoC. ISO 27701: confirm on current certificate/services-in-scope page rather than assume. | B / D if 27701 not on the fetched certificate excerpt | https://cloud.google.com/terms/data-processing-addendum ; https://cloud.google.com/security/compliance/services-in-scope |
| SOC 2 | `certifications` | **SOC 2 Type II only** (Google states it does not issue SOC 2 Type I). Core GCP and Workspace reports **quarterly** via Compliance Reports Manager. | Product-scoped. | B | https://cloud.google.com/security/compliance/soc-2 |
| PCI | `certifications` | DPA: PCI DSS AoC for GCP Audited Services. | Service-scoped. | B | https://cloud.google.com/terms/data-processing-addendum |
| GDPR DPA exists | `gdpr_dpa_signed` | **Cloud Data Processing Addendum** is public and **incorporated into the Agreement**. Covers GCP, Workspace/Cloud Identity (legacy names), etc. | Existence = A. Customer signature = C (usually click-through / incorporated). | A / C | https://cloud.google.com/terms/data-processing-addendum |
| DORA official pages | | Compliance DORA page + customer guides + blog on CTPP designation. | A | A | https://cloud.google.com/security/compliance/dora |
| DORA CTPP | | ESA list: **Google Cloud EMEA Limited**. Google states designation **includes subsidiaries** Google Cloud France SARL, Google Cloud Italy S.r.l., Google Cloud Poland Sp. z o.o. | Parent Google LLC / Alphabet is not the listed CTPP name. | A | https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf ; https://cloud.google.com/security/compliance/dora |
| DORA notification clause | `dora_notification_clause` | Google offers “DORA-specific contract and subcontractor resources” via account team. Public DPA has incident notification (Data Incident) — that is **GDPR-style**, not proof of a DORA Art. 30 clause in a given deal. | C | https://cloud.google.com/blog/products/identity-security/supporting-customers-as-a-critical-provider-under-eu-dora |
| Subcontracting | `subcontracting_allowed` | DPA authorizes subprocessors; public list by entity, service, region, activity, processing country. | Conditional (list + notice mechanics in DPA). | B | https://cloud.google.com/terms/subprocessors ; https://cloud.google.com/terms/data-processing-addendum |
| Public subprocessor list | `subcontractors` | Yes, live table. | Applicable subset C. | A / C | https://cloud.google.com/terms/subprocessors |
| Audit rights language | `audit_rights` | DPA §7.5: (a) if required under applicable privacy law, customer or appointed independent auditor may audit/inspect per business terms (notice, scope, **fee**, Google may reject unsuitable auditor); (b) customer may alternatively review Security Documentation / SOC. SCCs add further audit language. | Stronger **on-paper** inspection right than AWS’s “instruct us to run our audit”, but still conditional and fee-bearing. Boolean `true` would over-simplify. | B | https://cloud.google.com/terms/data-processing-addendum |
| Contract / risk / exit | various | Unknown | C / D | — |
| Substitutability | `substitutability` | Flexera 2025: GCP **third** for a decade; ~46% of organizations some/significant workloads; **leads experimenting** (20%, seven years). Flexera 2026: “firmly in third… lags significantly behind the two frontrunners.” | Higher market substitutability *toward* AWS/Azure than the reverse; still material switching cost. Not customer risk. | B | https://resources.flexera.com/web/pdf/Flexera-State-of-the-Cloud-Report-2025.pdf ; https://info.flexera.com/CM-REPORT-State-of-the-Cloud?lead_source=Organic+Search |

### Modelling notes

- Same pattern as AWS: one ICT Provider for Google Cloud; do not automatically merge Google Workspace, Google Ads, or Mandiant unless the estate’s contract does.
- Contracting entity and CTPP entity are **Ireland-registered Cloud companies**, while `headquarters` ISO code is still `us`. OSM cannot express that split.
- DPA “Audited Services” are defined as whatever is on `services-in-scope` **at the time** — certifications move. OSM `certifications[]` cannot version this.

---

## Service: Compute Engine

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Compute Engine | | A | https://cloud.google.com/compute |
| Vendor definition | description | “Virtual machines for any workload” / run VMs on Google Cloud infrastructure with preset or custom machine types. | Official product page. | A | https://cloud.google.com/compute |
| Service vs product | | IaaS VM **service**. | | A | — |
| ISO | | Listed among Google Cloud ISO 27001-governed services (confirm current list). | B | B | https://cloud.google.com/security/compliance/iso-27001 |
| Vendor SLA | characteristic | Premium tier, most regions: multi-zone instances **≥99.99%**; single memory-optimized **≥99.95%**; other single instance **≥99.9%**; LB **≥99.99%**. **Mexico and Stockholm lower** (multi-zone 99.95%, LB 99.95%). Standard Network Tier lower (multi-zone 99.9%). | Region × machine family × network tier. | B | https://cloud.google.com/compute/sla |
| Offerings | offering | Machine family, custom types, Confidential VM, GPU/TPU, disk type, region/zone. | Offering-level. | B | https://cloud.google.com/compute |
| Data residency | | Zonal/regional resources. | C | B / C | https://docs.cloud.google.com/compute/docs/regions-zones |
| Shared responsibility | | IaaS split; live migration is Google-operated. | A | https://cloud.google.com/compute |
| AI | | GPU/TPU SKUs. Not Vertex AI unless attached. | B | https://cloud.google.com/compute |

---

## Service: Cloud Storage

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Cloud Storage | | A | https://cloud.google.com/storage/sla |
| Vendor definition | description | Object storage with Standard/Nearline/Coldline/Archive/Rapid classes and regional / dual-region / multi-region locations. | From SLA covered-service + locations docs. | A | https://cloud.google.com/storage/sla |
| Service vs product | | Object-storage **service**. | | A | — |
| ISO | | Listed on ISO 27001 services page. | B | B | https://cloud.google.com/security/compliance/iso-27001 |
| Vendor SLA | characteristic | Typical (ex-MX/Stockholm): Standard multi/dual-region **≥99.95%**; Standard regional / Nearline-Coldline-Archive multi-dual / Rapid zonal **≥99.9%**; Nearline/Coldline/Archive regional or DRA **≥99.0%**. Mexico/Stockholm reductions. Turbo replication has separate RPO-like SLOs. | Location class × storage class × region. | B | https://cloud.google.com/storage/sla |
| Offerings | offering | Storage class; regional vs dual vs multi-region; turbo replication. | Offering-level. | B | same |
| Data residency | | Multi-region **spreads across countries** in that multi-region. Dual-region is two regions. | B / C | https://cloud.google.com/about/locations |
| Shared responsibility | | Google: platform. Customer: IAM, ACLs, CMEK, public access. | A | — |
| AI | | Common ML data store. | B | — |

---

## Service: Cloud SQL

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Cloud SQL | | A | https://cloud.google.com/sql/sla |
| Vendor definition | description | Fully managed relational database for MySQL, PostgreSQL, SQL Server. | SLA covered-service definitions. | A | https://cloud.google.com/sql/sla |
| Service vs product | | Managed relational **service**. | | A | — |
| ISO | | Cloud SQL listed on ISO 27001 page. | B | B | https://cloud.google.com/security/compliance/iso-27001 |
| Vendor SLA | characteristic | Enterprise Plus + HA or read pool ≥2 nodes: **≥99.99%**. Enterprise edition + HA: **≥99.95%**. **Shared-core, single-zone, and 1-node read pools are excluded.** | Edition × HA. | B | https://cloud.google.com/sql/sla |
| Offerings | offering | Enterprise vs Enterprise Plus; MySQL/Postgres/SQL Server; HA; read pool. | Offering-level. | B | same |
| Data residency | | Regional instance. | C | B / C | — |
| Shared responsibility | | Google: OS/engine HA fabric. Customer: users, schema, flags, authorized networks. | A | — |
| AI | | Not a model service. | A | — |

---

## Service: Google Kubernetes Engine (GKE)

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Google Kubernetes Engine (GKE) | | A | https://cloud.google.com/kubernetes-engine/sla |
| Vendor definition | description | Managed Kubernetes. SLA distinguishes zonal, regional, and Autopilot control planes. | Official SLA. | A | https://cloud.google.com/kubernetes-engine/sla |
| Service vs product | | Managed Kubernetes **service**. | | A | — |
| ISO | | GKE listed on ISO 27001 page. | B | B | https://cloud.google.com/security/compliance/iso-27001 |
| Vendor SLA | characteristic | Default regions: zonal CP **99.5%**; regional CP **99.95%**; Autopilot CP **99.95%**; Autopilot pods multi-zone **99.9%**. Mexico/Stockholm: regional/Autopilot CP **99.9%**, Autopilot pods **99.5%**. Nodes (non-Autopilot) under Compute Engine SLA. Version must be Stable/Regular/Extended — Rapid/EOS excluded. | Topology × region × channel. | B | https://cloud.google.com/kubernetes-engine/sla |
| Offerings | offering | Standard zonal/regional; Autopilot; release channel; version. | Offering-level. | B | same |
| Data residency | | Regional/zonal cluster. | C | B / C | — |
| Shared responsibility | | Google: control plane (and nodes on Autopilot). Customer: workloads; node pools on Standard. | B | same |
| AI | | GPU node pools / Autopilot GPUs possible. | B | — |

---

## Service: Cloud Run

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Cloud Run | **Cloud Functions is now Cloud Run functions** (same platform). | A | https://cloud.google.com/run |
| Vendor definition | description | “Run frontend and backend services, batch jobs, host LLMs, and queue processing workloads without the need to manage infrastructure.” “The flexibility of containers with the simplicity of serverless.” | Official. | A | https://cloud.google.com/run |
| Service vs product | | Container/serverless **platform service** — broader than Lambda/Functions. | A | — |
| ISO | | Cloud Run / Cloud Run functions listed on ISO page. | B | B | https://cloud.google.com/security/compliance/iso-27001 |
| Vendor SLA | characteristic | Non-GPU (ex-MX/Stockholm): **99.95%**. GPU zonal redundancy: **99.95%**. GPU no ZR: **99.5%**. Mexico/Stockholm non-GPU: **99.9%**. | GPU × zonal redundancy × region. | B | https://cloud.google.com/run/sla |
| Offerings | offering | Services vs Jobs; Cloud Run functions; GPU; direct VPC; source vs container deploy. | Offering-level. | B | https://cloud.google.com/run |
| Data residency | | Regional service. | C | B / C | — |
| Shared responsibility | | Google: platform. Customer: container, concurrency, IAM, VPC egress. | A | — |
| AI | | **Intrinsic product feature:** NVIDIA L4 GPUs, “host LLMs”, “Build AI Agents with Cloud Run”. In-scope for AI notes (unlike Azure OpenAI). | A | https://cloud.google.com/run |

### Modelling notes

- Do not treat Cloud Run as a drop-in offering of `compute.functions`. It is closer to a **container serverless** capability that *includes* functions. Comparability with Lambda/Functions is incomplete.

---

## Service: Google Cloud VPC

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Virtual Private Cloud (VPC) | Global VPC (subnets are regional) — different topology from AWS/Azure regional VPCs. | A | https://docs.cloud.google.com/vpc/docs/resources |
| Vendor definition | description | Google Cloud VPC is the virtual network for GCP resources; docs point SLA to Compute Engine. | | A | https://docs.cloud.google.com/vpc/docs/resources |
| Service vs product | | Networking service **and** project/org network boundary. Global by default. | A | — |
| ISO | | Cloud NAT / NGFW / related networking on ISO list; confirm “VPC” line on current list. | B | B | https://cloud.google.com/security/compliance/iso-27001 |
| Vendor SLA | characteristic | **No separate VPC SLA.** Docs: “VPC uses the same SLA as Compute Engine.” Cloud VPN has its own SLA (HA VPN often 99.99% when correctly topologized). | Inherited / adjacent. | B | https://docs.cloud.google.com/vpc/docs/resources ; https://cloud.google.com/compute/sla |
| Offerings | offering | Auto vs custom mode; Shared VPC; VPC Service Controls (adjacent security product); Cloud NAT; HA VPN. | Offering-level. | B | — |
| Data residency | | Global resource; subnet regional. Traffic may leave a zone depending on routing. | B / C | https://docs.cloud.google.com/docs/geography-and-regions |
| Shared responsibility | | Google: fabric. Customer: firewall rules, routes, Shared VPC IAM. | A | — |
| AI | | None intrinsic. | A | — |

### Modelling notes

- GCP “global VPC” vs AWS/Azure “regional VPC” is an offering/characteristic difference. Same Service name would hide a residency/blast-radius distinction.

---

## Service: Cloud IAM

### Facts table

| Fact | OSM field | Value | Scope / qualification | Class | URL |
|---|---|---|---|---|---|
| Official name | name | Identity and Access Management (IAM) / Cloud IAM | | A | https://cloud.google.com/iam/sla |
| Vendor definition | description | Authorization system for Google Cloud resources (roles/bindings on org, folder, project, resource). Distinct from **Cloud Identity / Google Workspace** (user directory / IdP). | Official SLA page exists specifically to say there is no SLA. | A | https://cloud.google.com/iam/sla |
| Service vs product | | Control-plane **authorization service** (and a prerequisite of every GCP project). Not an enterprise IdP. | Same conceptual class as AWS IAM, **not** Entra ID. | A | — |
| ISO | | “Identity & Access Management (IAM)” listed on the Google Cloud ISO 27001 services page. | B — listed ≠ every IAM feature / every org. | B | https://cloud.google.com/security/compliance/iso-27001 |
| Vendor SLA | characteristic | **Official: “No Service Level Agreement (SLA) applies to the Identity and Access Management (IAM) service.”** Other services that use IAM may have their own SLAs. | Explicit D. Do not invent an uptime %. | A | https://cloud.google.com/iam/sla |
| Offerings | offering | Allow policies; IAM Conditions; Workforce Identity Federation; Workload Identity Federation; Privileged Access Manager (adjacent). Cloud Identity is a **different** product. | Do not merge Cloud IAM with Cloud Identity / Workspace. | B | https://cloud.google.com/iam/sla |
| vs AWS IAM / Entra | (stress) | Cloud IAM = **GCP resource authorization**. Workforce users typically come from Cloud Identity, Workspace, or an external IdP (often Entra or Okta) via Workforce Identity Federation. Entra remains the enterprise IdP. | A | https://cloud.google.com/iam/sla ; https://learn.microsoft.com/en-us/entra/fundamentals/whatis |
| Data residency | | IAM is a global control-plane service. Precise residency of policy/identity metadata is **not** customer-picked like a regional bucket. | B / D | D for a complete country list |
| Shared responsibility | | Google: IAM API integrity. Customer: bindings, service accounts, key hygiene, federation trust. | A | — |
| AI | | None intrinsic (IAM is used *by* AI products; it is not an AI system). | A | — |

### Modelling notes

- Same rule as AWS IAM: do **not** put Cloud IAM on the same OSM Service as Microsoft Entra ID. Pair it with AWS IAM / Azure RBAC under a cloud-authorization capability if a capability Service is used.
- `availability_target` cannot be filled from a vendor SLA here — there isn’t one.

---

## Stress-test observations

These are model-pressure points found while mapping public facts to OSM 1.3. They are investigation notes, not schema change proposals.

### 1. Certification scope grain (ISO 27001 / 27701 / SOC 2 / PCI)

- All three vendors publish **service-in-scope lists** that change (AWS ISO page updated 2026-09-01; AWS SOC Spring 2026 = 188 services; Google DPA defines “Audited Services” as whatever is on `services-in-scope` *now*).
- Microsoft splits audits: Azure+Dynamics+Power Platform vs Office 365 vs Azure DevOps vs (separately) GitHub.
- OSM `ict_provider.certifications` is a **string array with no scope, no standard version, no date, no service/region qualifier**. Writing `ISO 27001` on the provider **over-claims**. Writing it on a Service still cannot express “this Region / this SKU / this sovereign cloud is out of scope”.
- ISO 27001 on the **customer’s implementation** is never implied by the provider certificate (Microsoft and AWS both say this explicitly).
- **Do not** treat provider certification as compliance evidence for a customer offering.

### 2. Microsoft as one vs many ICT Providers

- **One legal parent** (Microsoft Corporation, HQ `us`) sells Azure, Microsoft 365, Dynamics, Entra, and owns GitHub.
- **Different contracting entities** (often MIOL in the EU), **different CTPP name** (MIOL, not Microsoft Corporation), **different DPA/SLA/audit packs**, **different data-residency maps**.
- Entra ID is **shared substrate**: every Azure *and* M365 tenant *is* an Entra tenant. A provider split “azure” vs “m365” still shares identity.
- GitHub is a subsidiary with a separate commercial stack — treating it as the same ICT Provider as Azure will falsify subcontractors, DPA, and certifications.
- OSM `type` cannot be simultaneously `cloud-infrastructure` (Azure) and `software-vendor` (M365).
- Recommended investigation options (for the decision register, not for this file to implement): multiple provider records with a parent note in provenance; or one legal-entity provider plus offering-level product-family characteristics. Both lose something.

### 3. AWS IAM ≠ Entra ID ≠ Cloud IAM

| | AWS IAM | Microsoft Entra ID | Google Cloud IAM |
|---|---|---|---|
| What it is | Account/org **authorization** for AWS APIs | Enterprise **directory + IdP** | Project/org **authorization** for GCP APIs |
| Users live in | IAM users (discouraged) or **external IdP** / IAM Identity Center | The Entra tenant | Cloud Identity / Workspace / **external IdP** |
| Typical enterprise catalog | Often *not* catalogued; Identity Center / Okta / Entra is | Yes — core identity service | Often *not* catalogued; Cloud Identity / Entra is |
| Public SLA | **D** (none found) | **B** (~99.99% auth, edition-conditional) | **A** (explicitly **no SLA**) |
| DORA mapping | Cloud control plane, not workforce IdP | Microsoft publishes Entra-specific DORA guidance | Cloud control plane |

- A single capability Service `identity.access-management` with three provider offerings **erases** the IdP vs cloud-RBAC distinction and will produce false substitutability and false DORA “who provides identity” mappings.
- IAM Identity Center and Cloud Identity are the closer Entra *peers* — and they were **not** in the requested seven-service lists except as adjacent notes.

### 4. Cloud Run vs Azure Functions vs AWS Lambda

- All three are “serverless compute”, but:
  - **Lambda** = functions (+ newer MicroVMs / Managed Instances).
  - **Azure Functions** = functions on multiple *hosting plans* (Flex Consumption, App Service, Container Apps).
  - **Cloud Run** = **container platform** that also hosts **Cloud Run functions**; official positioning includes websites, jobs, **LLM hosting, GPUs, agents**.
- Same capability Service is acceptable only if offerings carry the packaging difference (function vs container vs GPU). Otherwise comparability is false.
- Cloud Run has **intrinsic AI** (GPUs / host LLMs). Lambda/Functions have AI *usage patterns* but are not model hosts by default. Azure OpenAI remains out of this seven-service set.

### 5. VPC as networking service vs tenancy boundary

- AWS VPC, Azure VNet, and GCP VPC are requestable networking products **and** the default isolation boundary of the account/subscription/project.
- Core VPC/VNet often has **no dedicated financially backed SLA** (AWS: NAT Gateway 99.9% only; Azure: connectivity measured via VM SLA; GCP: “uses Compute Engine SLA”).
- GCP VPC is **global** (regional subnets); AWS/Azure VPCs are **regional**. Data-residency and blast-radius are not the same Service.
- OSM has no tenancy/account entity. Modelling VPC only as `network.virtual-network` loses “this is the account boundary”; modelling it only as a characteristic loses a catalogued networking service.

### 6. Provider type enum is too small

- `cloud-infrastructure` | `cloud-platform` | `managed-service` | `software-vendor` | `network-provider` | `data-center`
- Each hyperscaler is infrastructure **and** platform **and** managed service. Microsoft is also a software vendor. None is a `data-center` colo seller.
- CTPP designations are of **regional subsidiaries** (AWS EMEA SARL, MIOL, Google Cloud EMEA Limited), not the HQ legal name OSM would store.

### 7. Fields that look populate-able but are customer posture

Leave **unset** on a public reference provider unless labelled synthetic:

- `gdpr_dpa_signed` — DPA **exists** (A); signed-for-this-customer (C).
- `dora_notification_clause` — DORA addenda **exist** (A); clause in *this* contract (C). CTPP status does not set this true.
- `audit_rights` — public DPA language is **conditional** (reports ± fee-bearing inspection). Boolean cannot encode AWS “instruct our auditor” vs Google/Microsoft “additional audit if reports insufficient”.
- `subcontracting_allowed` — public default is **conditional** (general authorization + notice + objection), not a raw `true`.
- `subcontractors` — public lists exist; the applicable subset is C.
- `contract_start` / `contract_end` / `notice_period_days` / `exit_strategy_*` / `last_risk_assessment` / `risk_level` — C/D. Never invent.
- `concentration_risk` — Flexera supports a **market** observation only. Customer concentration is C.
- `service_posture.availability_target`, `rto`, `rpo`, `operational_criticality` — **enterprise** posture, not vendor SLA.

### 8. Vendor SLA vs enterprise availability_target

- Every researched compute/storage/database/kubernetes/functions product (except AWS IAM, GCP IAM, and core VPC/VNet) has a **published vendor SLA**.
- SLAs are almost always **SKU/region/edition/topology-conditional** (class B).
- OSM records enterprise **expectations** in posture and says it does not manage vendor SLAs. Vendor SLA belongs in a characteristic or provenance note on the **offering**, never as a universal Service fact and never as the customer’s `availability_target`.

### 9. Headquarters vs contracting vs processing vs CTPP

- All three: `headquarters` = **`us`** (Seattle / Redmond / Mountain View).
- EU financial-entity reality: contracts and DORA CTPP sit on **IE/LU subsidiaries**.
- Processing locations are **dozens of countries**, customer-selected per service, plus China/GovCloud/sovereign partitions with **different operators**.
- OSM can store one HQ code and a free-text location array. It cannot store “legal HQ vs operational HQ vs contracting entity vs CTPP entity vs processing geography”.

### 10. Data-processing locations have no controlled vocabulary

- Vendors speak in Regions / geographies / multi-regions (GCP multi-region is **multi-country by design**).
- OSM `data_processing_locations[]` is unconstrained strings. A provider-level dump of countries is a **capability map**, not the customer’s processing record. Actual residency is offering- or posture-level and C.

### 11. Shared responsibility is not a certification and not posture.risk

- IaaS (EC2 / Azure VM / Compute Engine): customer owns the guest OS.
- PaaS/K8s: split at the control plane; node responsibility depends on Autopilot / Automatic / Fargate / Auto Mode.
- IAM/IdP: customer owns policy design.
- OSM has no shared-responsibility object. Putting “ISO 27001” on the provider does not record who patches the VM.

### 12. Substitutability / concentration (Flexera only)

- **Flexera 2025** (N=759, winter 2024): AWS and Azure neck-and-neck; enterprises Azure 81% / AWS 79% when “some” workloads included, AWS 53% / Azure 50% for significant workloads; SMBs AWS 53% vs Azure 29%; GCP third (~46% some/significant; leads experimenting at 20% for seven years). 70% hybrid. Average ~2.4 public clouds.
- **Flexera 2026** (N=753, supplementary because TODAY is 2026-09-13): AWS 83% vs Azure 79% some/significant; both used in some capacity by 88%; GCP still a distant third.
- Use this **only** as a market-concentration observation behind a cautious `substitutability: low` (AWS/Azure) or `medium` (GCP relative to the duopoly). Do **not** set customer `concentration_risk` or `risk_level` from the survey.

### 13. What OSM mapped cleanly

- Provider `name`, `headquarters` (as ISO country of legal/operational HQ), `type` (with documented awkwardness), `substitutability` (survey-backed, not customer risk).
- Service `name` / `description` from vendor pages.
- Offering grain for edition/SKU/region/SLA conditionality via nested offerings + characteristics.
- Provider-intrinsic vs capability Service is expressible (`providers` on Service vs Offering) — Kubernetes is the cleanest capability example.

### 14. What OSM cannot express without over-claiming

- Certification **scope** (service × region × sovereign cloud × certificate date).
- Multiple legal entities / CTPP / contracting-party tables.
- DPA **exists** vs DPA **signed**.
- Conditional subcontracting and report-based vs inspection audit rights.
- Global vs regional IAM/VPC control planes.
- Vendor SLA as a first-class object distinct from customer `availability_target`.
