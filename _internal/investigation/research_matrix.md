# Provider / Service Research Matrix

Investigation date: 2026-09-13. Encoded values are in
`records/`. Full narrative tables are in `research-notes/`.

Evidence classes:

- **A** — publicly verified
- **B** — publicly documented but conditional (service / region / edition)
- **C** — customer-dependent; not encoded as a universal fact
- **D** — not publicly determinable; left unset

`Verified` is `yes` when the official page was fetched or cited from an
authoritative URL on 2026-09-13.

---

## 1. ICT Provider facts encoded in OSM

| Provider | Fact | OSM field | Value | Scope / qualification | Class | Source | Verified |
|---|---|---|---|---|---|---|---|
| AWS | Legal/operating brand | `name` | Amazon Web Services | Parent is Amazon.com, Inc. Default US contracting party is Amazon Web Services, Inc. EU CTPP is AWS EMEA SARL — not stored | A | https://aws.amazon.com/legal/aws-contracting-party/ ; https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf | yes |
| AWS | Type | `type` | cloud-infrastructure | Least-wrong token; AWS is also PaaS/managed services | A | https://aws.amazon.com/about-aws/global-infrastructure/ | yes |
| AWS | HQ | `headquarters` | us | Seattle principal offices | A | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm | yes |
| AWS | Processing geography | `data_processing_locations` | us, eu, apac, me, sa, af, ca | Capability map. Customer region is C. China regions are local partners | B | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | yes |
| AWS | Subprocessing | `subcontracting_allowed` | conditional | DPA general authorization + notice + objection | B | https://d1.awsstatic.com/legal/aws-gdpr/AWS_GDPR_DPA.pdf | yes |
| AWS | Certifications listed | `certifications` | iso27001-2022, iso27701-2019, iso27017, iso27018, soc2-type2, soc1, soc3, pci-dss | **Service-scoped.** ISO page updated 2026-09-01. SOC Spring 2026 = 188 services. Do not read as all AWS | B | https://aws.amazon.com/compliance/iso-certified/ ; https://aws.amazon.com/blogs/security/spring-2026-soc-1-2-and-3-reports-are-now-available-with-188-services-in-scope/ | yes |
| AWS | DPA signed | `gdpr_dpa_signed` | null | Public DPA exists and is incorporated in Service Terms. Signed-for-customer is C | A/C | https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/aws-data-processing-addendum-dpa.html | yes |
| AWS | DORA clause | `dora_notification_clause` | null | DORA FSA exists for eligible customers. Clause in a given contract is C. CTPP designation is A for AWS EMEA SARL | C | https://aws.amazon.com/compliance/dora/ | yes |
| AWS | Audit rights | `audit_rights` | null | DPA is report-based, not unrestricted inspection | B | AWS GDPR DPA §10–11 | yes |
| AWS | Substitutability | `substitutability` | low | Flexera 2025 market observation, not customer risk | B | https://resources.flexera.com/web/pdf/Flexera-State-of-the-Cloud-Report-2025.pdf | yes |
| AWS | Concentration | `concentration_risk` | true | Same survey, market grain. Customer concentration remains C | B | Flexera 2025 | yes |
| AWS | Contract / risk / exit | `contract_*`, `risk_level`, `exit_strategy_*` | null | C | C | — | yes |
| Microsoft | Legal name | `name` | Microsoft Corporation | CTPP/contracting often Microsoft Ireland Operations Limited | A | https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm ; https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf | yes |
| Microsoft | Type | `type` | cloud-infrastructure | Awkward: Azure IaaS + M365 SaaS + Entra. Single enum | A | — | yes |
| Microsoft | HQ | `headquarters` | us | Redmond | A | Microsoft 10-K | yes |
| Microsoft | DPA | `gdpr_dpa_signed` | null | Products and Services DPA published (May 2026 edition listed). Signed is C | A/C | https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA | yes |
| Microsoft | Subprocessing | `subcontracting_allowed` | conditional | DPA + supplier-management notice periods | B | https://learn.microsoft.com/en-us/compliance/assurance/assurance-supplier-management | yes |
| Microsoft | Certifications | `certifications` | iso27001, iso27701, soc2-type2, soc1, pci-dss | Azure certificate covers Azure, Dynamics, Power Platform and **select** M365. Separate Office 365, Azure DevOps, GitHub audits | B | https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-iso-27001 | yes |
| Microsoft | Substitutability / concentration | `substitutability`, `concentration_risk` | low / true | Flexera 2025 Azure neck-and-neck with AWS | B | Flexera 2025 | yes |
| Google Cloud | Name | `name` | Google Cloud | Operating brand. US contractor Google LLC; EMEA often Google Cloud EMEA Limited (also CTPP) | A | https://cloud.google.com/terms/google-entity | yes |
| Google Cloud | Type / HQ | `type`, `headquarters` | cloud-infrastructure / us | Mountain View | A | https://cloud.google.com/terms/cloud-privacy-notice | yes |
| Google Cloud | Certifications | `certifications` | iso27001-2022, iso27017, iso27018, iso27701, soc2-type2, soc3, pci-dss | Service-listed on ISO page. DPA “Audited Services” follow live in-scope list | B | https://cloud.google.com/security/compliance/iso-27001 | yes |
| Google Cloud | DPA | `gdpr_dpa_signed` | null | CDPA published. Signed is C | A/C | https://cloud.google.com/terms/data-processing-addendum | yes |
| Google Cloud | Substitutability | `substitutability` | medium | Flexera 2025 ~46% some/significant workloads; third place | B | Flexera 2025 | yes |
| Oracle | Name / HQ / type | `name`, `headquarters`, `type` | Oracle Corporation / us / cloud-infrastructure | CTPP is Oracle Nederland B.V. Type does not cover Fusion/Database licenses | A | Oracle 10-K; ESA CTPP list | yes |
| Oracle | Certifications | `certifications` | iso27001, iso27017, iso27018, iso27701, soc1/2/3 | Oracle: generally specific to a cloud service and may be region-specific | B | https://www.oracle.com/corporate/cloud-compliance/ | yes |
| IBM | Name / HQ / type | `name`, `headquarters`, `type` | International Business Machines Corporation / us / cloud-infrastructure | NY incorporation, Armonk HQ. ESA list spelling “Machine”. Red Hat is a separate provider | A | IBM 10-K; ESA CTPP list | yes |
| IBM | Certifications | `certifications` | iso27001, iso27701, soc2-type2, soc3 | Classic IaaS ISO list does not name IKS; SOC 2 **does** name IKS and OpenShift on IBM Cloud | B | https://www.ibm.com/products/cloud/compliance/iso-27001 ; https://www.ibm.com/products/cloud/compliance/soc-2 | yes |
| Red Hat | Name / type | `name`, `type` | Red Hat / software-vendor | Wholly owned IBM subsidiary since 2019-07-09; still a distinct seller for self-managed OpenShift/RHEL | A | https://www.ibm.com/investor/news/ibm-completes-acquisition-of-red-hat | yes |
| Alibaba Cloud | Name / HQ | `name`, `headquarters` | Alibaba Cloud / cn | Forced to one code: Hangzhou operator / ISO certificate. Loses Cayman parent and Singapore international HQ/contractor | A | ISO 27001 certificate Alibaba Cloud Computing Ltd.; Alibaba international terms | yes |
| Cloudflare | Name / HQ / type | `name`, `headquarters`, `type` | Cloudflare, Inc. / us / network-provider | Also a security SaaS platform. Type is a compromise | A | Cloudflare 10-K; https://www.cloudflare.com/trust-hub/ | yes |
| Cloudflare | DORA CTPP | (no field) | Not on ESA list of 19. Vendor FAQ states it is not designated | A | https://www.cloudflare.com/trust-hub/compliance-resources/dora/ ; ESA list | yes |
| Salesforce | Name / HQ / type | `name`, `headquarters`, `type` | Salesforce, Inc. / us / software-vendor | No saas type. Slack encoded as a Salesforce offering | A | Salesforce DPA; 10-K | yes |
| ServiceNow | Name / HQ / type | `name`, `headquarters`, `type` | ServiceNow, Inc. / us / software-vendor | ITSM encoded. CMDB not encoded | A | ServiceNow 10-K | yes |
| SAP | Name / HQ / type | `name`, `headquarters`, `type` | SAP SE / de / software-vendor | Walldorf registered office. CTPP = SAP SE. Substitutability low is observational ERP lock-in, not a customer score | A/B | SAP Impressum; ESA CTPP list | yes |
| Atlassian | Name / HQ / type | `name`, `headquarters`, `type` | Atlassian Corporation / au / cloud-platform | Dual principal offices Sydney + San Francisco. `au` loses US office. Cloud vs Data Center is offering grain | A | https://investors.atlassian.com/resources/investor-faqs/default.aspx | yes |
| Atlassian | Certifications | `certifications` | iso27001-2022, iso27018, soc2-type2 | Cloud ATMS / named Cloud reports. **Not Data Center** | B | https://www.atlassian.com/trust/compliance/resources/iso27001 | yes |
| Atlassian | Hosting | (subprocessor, not copied) | AWS is primary Cloud host | A | https://www.atlassian.com/trust/compliance/compliance-faq | yes |
| Okta | Name / HQ / type | `name`, `headquarters`, `type` | Okta, Inc. / us / cloud-platform | Auth0 is a second service, same provider | A | Okta 10-K; https://security.okta.com/ | yes |
| CrowdStrike | Name / HQ / type | `name`, `headquarters`, `type` | CrowdStrike Holdings, Inc. / us / cloud-platform | Falcon Complete is managed-detection offering, same provider | A | CrowdStrike IR FAQ | yes |
| Palo Alto Networks | Name / HQ / type | `name`, `headquarters`, `type` | Palo Alto Networks / us / software-vendor | Prisma Access encoded as ZTNA offering. Type would be cloud-platform if estate were SASE-only | B | https://www.paloaltonetworks.com/about-us/locations | yes |
| Zscaler | Name / HQ / type | `name`, `headquarters`, `type` | Zscaler, Inc. / us / cloud-platform | Strongest type fight vs network-provider | B | https://www.zscaler.com/company/contact | yes |
| Datadog | Name / HQ / type | `name`, `headquarters`, `type` | Datadog, Inc. / us / cloud-platform | NYC HQ | A | https://www.datadoghq.com/about/contact/ | yes |
| Dynatrace | Name / HQ / type | `name`, `headquarters`, `type` | Dynatrace, Inc. / us / cloud-platform | US HQ Boston (2026). Linz remains engineering HQ and is not stored | A | Dynatrace 10-K / HQ relocation PR | yes |
| Snowflake | Name / HQ / type | `name`, `headquarters`, `type` | Snowflake Inc. / us / cloud-platform | Runs on customer-chosen AWS/Azure/GCP | A | Snowflake contact / SEC | yes |
| Databricks | Name / HQ / type | `name`, `headquarters`, `type` | Databricks, Inc. / us / cloud-platform | Control plane SaaS; data plane typically customer CSP | A | https://www.databricks.com/trust/compliance | yes |
| GitHub | Name / HQ / type | `name`, `headquarters`, `type` | GitHub, Inc. / us / cloud-platform | Microsoft subsidiary; separate trust/legal stack | A | https://github.com/trust-center | yes |
| GitLab | Name / HQ | `name`, `headquarters` | GitLab Inc. / us | Remote-only; `us` is a filing-address approximation | A | GitLab visiting / 10-K | yes |
| Workday | Name / HQ / type | `name`, `headquarters`, `type` | Workday, Inc. / us / software-vendor | HCM boundary test | A | Workday 10-K | yes |
| Broadcom | Name / HQ / type | `name`, `headquarters`, `type` | Broadcom Inc. / us / software-vendor | VMware brand. No VMware Service encoded (product, not service) | A | Broadcom VCF docs | yes |

---

## 2. Service and offering facts encoded in OSM

| Provider | Service | Fact | OSM field | Value | Scope / qualification | Class | Source | Verified |
|---|---|---|---|---|---|---|---|---|
| AWS | Amazon EC2 | Definition | offering `compute.virtual-machines.aws-ec2` | On-demand scalable compute in AWS | Vendor product as offering of capability Service | A | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html | yes |
| AWS | Amazon EC2 | Vendor SLA | characteristic `vendor_availability_sla` | 99.99% multi-AZ region / 99.5% instance | Configuration-conditional. Not `availability_target` | B | https://aws.amazon.com/compute/sla/ | yes |
| AWS | Amazon S3 | Vendor SLA | characteristic | 99.9% standard-class credits / 99.0% IA classes | Distinct from durability design claims | B | https://aws.amazon.com/s3/sla/ | yes |
| AWS | Amazon RDS | Vendor SLA | characteristic | 99.95% Multi-AZ / 99.5% Single-AZ | Engine and class exclusions | B | https://aws.amazon.com/rds/sla/ | yes |
| AWS | Amazon EKS | Vendor SLA | characteristic | 99.95% standard control plane / 99.99% provisioned | Control plane only; nodes under Compute SLA | B | https://aws.amazon.com/eks/sla/ | yes |
| AWS | AWS Lambda | Vendor SLA | characteristic | 99.95% per region | | B | https://aws.amazon.com/lambda/sla/ | yes |
| AWS | Amazon VPC | No general SLA | (omitted) | NAT Gateway 99.9% only | Do not invent VPC uptime | A/D | https://aws.amazon.com/vpc/sla/ | yes |
| AWS | AWS IAM | What it is | offering `identity.cloud-authorization.aws-iam` | Cloud-account authorization, not enterprise IdP | Distinct from IAM Identity Center | A | https://aws.amazon.com/iam/ | yes |
| AWS | AWS IAM | Vendor SLA | (omitted) | None found | D | D | — | yes |
| Microsoft | Azure VMs | SLA | characteristic | Conditional 99.99% / 99.95% / 99.9% | Authoritative: Online Services SLA | B | https://learn.microsoft.com/en-us/azure/virtual-machines/availability | yes |
| Microsoft | AKS | SLA | characteristic | None on Free tier; 99.95%/99.9% Standard | Tier-conditional | B | https://learn.microsoft.com/en-us/azure/aks/free-standard-pricing-tiers | yes |
| Microsoft | Entra ID | What it is | offering `identity.directory-idp.entra-id` | Enterprise directory/IdP; substrate for M365+Azure | Not AWS IAM | A | https://learn.microsoft.com/en-us/entra/fundamentals/whatis | yes |
| Microsoft | Exchange / SharePoint / Teams | Suite split | three Services | M365 is a SKU, not one OSM Service | A | Microsoft 365 / Exchange / Teams / SharePoint Learn pages | yes |
| Google | Cloud Run | Execution model | characteristic `execution_model=container-service` | Not a function platform | Encoded under compute.functions only as a mismatch test | A | https://cloud.google.com/run | yes |
| Google | Cloud IAM | No SLA | offering note | Official: no SLA applies | A | https://cloud.google.com/iam/sla | yes |
| Google | Compute Engine / GKE / Cloud SQL / Cloud Storage | Listed on ISO 27001 services page | (not copied as service certification) | In-scope list is B and changes | B | https://cloud.google.com/security/compliance/iso-27001 | yes |
| CNCF | Kubernetes | Not a Service | `compute.kubernetes.self-operated` has no provider | Project/runtime | A | https://kubernetes.io/ | yes |
| IBM | IKS / OpenShift on IBM Cloud | Provider | offering `providers: [ibm]` | Red Hat is origin, not the managed-service seller | A | IBM IKS / Red Hat on IBM pages | yes |
| IBM | HCP Terraform | Seller | `auto.infrastructure-as-code.hcp-terraform` providers `[ibm]` | Commercial ops to IBM from 2025-09-01 | A | https://www.hashicorp.com/en/blog/what-transition-to-ibm-means-hashicorp-customers-greater-value-same-commitment | yes |
| Atlassian | Jira / Confluence | Cloud vs Data Center | `deployment_model` characteristic | Cloud ISO/SOC does not cover Data Center | A/B | Atlassian Trust + 10-K | yes |
| Okta | Workforce Identity | Service | `identity.directory-idp.okta-workforce` | Auth0 not merged into this offering | A | Okta 10-K | yes |
| CrowdStrike | Falcon vs Complete | operating_model | saas-platform vs managed-detection | Same ICT Provider | A | CrowdStrike product/IR | yes |
| Zscaler | ZIA / ZPA | Two Services | `net.secure-web-gateway` / `net.ztna` | Not one “Zscaler” Service | A | Zscaler product split | yes |
| Cloudflare | CDN/WAF and Access | Two Services | `net.cdn-waf` / `net.ztna` | Same provider | A | Cloudflare Trust Hub / Cloudflare One | yes |
| Snowflake | Hosting CSP | `providers: [snowflake, aws\|microsoft\|google-cloud]` | Dual ICT Providers on the offering | A | Snowflake platform docs | yes |
| Databricks | Control vs data plane | `providers: [databricks, aws\|microsoft\|google-cloud]` | Databricks ISO does not certify customer data plane | B | Databricks Trust / platform docs | yes |
| Snowflake / Databricks | Vendor AI | separate Service `data.vendor-ai-assist` | Cortex / Mosaic hosted models. Risk class unset | B | Cortex and Mosaic docs | yes |
| Salesforce | Sales Cloud | BOUNDARY TEST | `crm.sales-cloud` | Application vs technological service | A | Salesforce Trust | yes |
| SAP | S/4HANA Cloud Public Edition | BOUNDARY TEST | `erp.s4hana-cloud` | ERP application. ISO certificate includes this product — still not an OSM-recommended Service | A/B | SAP product + Trust Center certificate | yes |
| ServiceNow | ITSM vs CMDB | ITSM encoded; CMDB omitted | CMDB is CI inventory, OSM out of scope | A | ServiceNow ITSM/CMDB pages; OSM MODEL.md | yes |
| GitHub | Actions hosted vs self-hosted | `operating_model` | Control plane still GitHub | A | https://docs.github.com/en/actions | yes |

---

## 3. Explicitly unset (do not invent)

| Fact | OSM field | Why unset | Class |
|---|---|---|---|
| Customer contract reference/dates/notice | `contract_*`, `notice_period_days` | Not a public provider property | C |
| Whether this estate signed the vendor DPA | `gdpr_dpa_signed` | Template ≠ execution | C |
| DORA notification clause in the customer contract | `dora_notification_clause` | FSA/addendum eligibility is customer-specific | C |
| Provider risk/severity | `risk_level` | Customer assessment | C |
| Exit strategy documented/tested | `exit_strategy_*` | Customer | C |
| Last risk assessment date | `last_risk_assessment` | Customer | C |
| Applicable subprocessor subset | `subcontractors` | Public lists exist; applicable set is C | A exists / C apply |
| Service criticality | `operational_criticality` | Customer / DORA function grain | C |
| RTO / RPO / resilience tests | offering posture | Customer objectives | C |
| Data / security classification | service posture | Depends on what the customer puts on the service | C |
| Enterprise availability/response/resolution targets | posture targets | Not vendor SLA | C |
| Tech debt, cost, automation, manual hours | posture | Estate telemetry | C/D |
| AI Act risk class | `ai_act_risk_class` | Legal assessment of intended purpose | C/D |

---

## 4. Estate rows not encoded as OSM Services

| Rank | Candidate | Treatment | Reason |
|---|---|---|---|
| 29 | Kubernetes (project) | self-operated offering only | CNCF project, not a provider |
| 30 | Docker | not encoded | Runtime / Desktop / Hub name collision |
| 31–32 | vSphere / VCF | provider `broadcom` only | Product family, not a service |
| 34–35 | RHEL / Ubuntu | not encoded | Operating systems |
| 37 | Ansible | not encoded | Automation engine / product |
| 40 | Jenkins | not encoded | Community project |
| 41 | Azure DevOps | not encoded | Suite of several services |
| 42 | Argo CD | not encoded | CNCF project |
| 43–49, 52 | PostgreSQL, MySQL, SQL Server, Oracle DB, MongoDB, Redis, OpenSearch, Kafka | not encoded as themselves | Products/projects; managed offerings cover some |
| 53 | Microsoft 365 | decomposed | Suite SKU |
| 59 | ServiceNow CMDB | out of scope | CMDB CI inventory |
| 65, 67, 69, 73–74, 87–91 | Zoom, CyberArk, Defender, Splunk, SentinelOne, New Relic, Grafana, Prometheus, OpenTelemetry | surveyed only | Time-boxed; see research-notes |
| 75–78, 80–83, 92–94 | Generic connectivity / API / AI platform rows | surveyed as capabilities | Encode when an estate actually offers them; S2S deps remain out of scope |

---

## 5. Primary sources (also listed in research-notes)

- AWS compliance programs: https://aws.amazon.com/compliance/programs/
- AWS ISO certified: https://aws.amazon.com/compliance/iso-certified/
- AWS DORA: https://aws.amazon.com/compliance/dora/
- Microsoft Azure ISO 27001: https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-iso-27001
- Microsoft DPA: https://www.microsoft.com/licensing/docs/view/Microsoft-Products-and-Services-Data-Protection-Addendum-DPA
- Google Cloud ISO 27001: https://cloud.google.com/security/compliance/iso-27001
- ESA CTPP list (18 Nov 2025): https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf
- DORA 2022/2554: https://eur-lex.europa.eu/legal-content/ENG/ALL/?uri=CELEX:32022R2554
- DORA RTS 2024/1773: https://eur-lex.europa.eu/eli/reg_del/2024/1773/oj
- DORA ITS RoI 2024/2956: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402956
- GDPR consolidated: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?from=EN&uri=CELEX:02016R0679-20160504
- NIST CSF 2.0: https://doi.org/10.6028/NIST.CSWP.29
- EU AI Act Art. 3: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-3
- Flexera 2025 State of the Cloud: https://resources.flexera.com/web/pdf/Flexera-State-of-the-Cloud-Report-2025.pdf
- Stack Overflow 2025 (popularity only): https://survey.stackoverflow.co/2025/technology
- CNCF Annual Cloud Native Survey (popularity only): https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/
