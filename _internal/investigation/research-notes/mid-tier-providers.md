# Mid-tier provider research notes

Research date: 2026-09-13.  
Scope: public facts only, for a 7lens OSM reference-estate investigation.  
Do not treat any value below as a customer contract, signed DPA, RTO/RPO, criticality, or `risk_level`. Those are class C or D unless a public source states a provider-level fact.

Evidence classes:

- **A** — publicly verified on an official vendor, regulator, or SEC/company-register page
- **B** — publicly documented but conditional (service, region, edition, SKU, contracting entity, or NDA-gated report)
- **C** — customer-dependent; do not populate as a universal OSM fact
- **D** — not publicly determinable; leave unset

OSM ICT Provider `type` enum is only: `cloud-infrastructure`, `cloud-platform`, `managed-service`, `software-vendor`, `network-provider`, `data-center`. There is no `saas` value.

OSM `headquarters` is a single ISO 3166-1 alpha-2 code. Legal incorporation and operational HQ often diverge; the field cannot hold both.

---

## Sources

Primary official pages used in this note. Secondary commentary is cited only when it restates an official document, and is never used to add Salesforce (or others) to the ESA CTPP list.

### Cross-cutting

| Source | URL |
|---|---|
| ESAs first list of designated DORA CTPPs (18 Nov 2025), ESMA copy | https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf |
| Same list, EIOPA copy | https://www.eiopa.europa.eu/document/download/56b1ca78-5dd2-4d36-8377-47a538eb7558_en?filename=List+of+designated+CTPPs.pdf |
| DORA Regulation (EU) 2022/2554 | https://eur-lex.europa.eu/eli/reg/2022/2554/oj |
| OSM out-of-scope (applications, business services, CMDB CIs) | `MODEL.md` / `SPECIFICATION.md` in this repository |

Official ESA CTPPs relevant to this batch: **Oracle Nederland B.V.**, **International Business Machine Corporation**, **SAP SE**. Not on the official 19-name list: Alibaba, Cloudflare, Salesforce, Slack, ServiceNow, Workday. Secondary blogs that add Salesforce to the 19 are incorrect against the ESA PDF.

### Oracle

| Source | URL |
|---|---|
| Oracle Trust Center | https://www.oracle.com/trust/ |
| Oracle Cloud Compliance | https://www.oracle.com/corporate/cloud-compliance/ |
| Oracle Cloud Services contracts hub | https://www.oracle.com/contracts/cloud-services/ |
| Cloud Hosting and Delivery Policies | https://www.oracle.com/contracts/docs/ocloud_hosting_delivery_policies_3089853.pdf |
| Services Privacy Policy (DPA / subprocessors) | https://www.oracle.com/legal/privacy/services-privacy-policy/ |
| Oracle Data Processing Agreement (published PDF) | https://www.oracle.com/contracts/docs/data_processing_agreement_011218_4261005.pdf |
| Supplier / sub-processor notice | https://www.oracle.com/corporate/security-practices/corporate/supply-chain/suppliers/ |
| OCI Compute overview | https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm |
| Autonomous AI Database product | https://www.oracle.com/autonomous-database/ |
| Autonomous AI Database region availability | https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-region-availability.html |
| OCI regions and availability domains | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm |
| Oracle Corporation FY2026 10-K cover (Austin HQ; DE incorporation) | https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/R1.htm |

### IBM / Red Hat

| Source | URL |
|---|---|
| IBM Trust Center | https://www.ibm.com/trust |
| IBM Cloud ISO 27001 | https://www.ibm.com/products/cloud/compliance/iso-27001 |
| IBM Cloud SOC 2 | https://www.ibm.com/products/cloud/compliance/soc-2 |
| IBM Cloud SOC 3 | https://www.ibm.com/products/cloud/compliance/soc-3 |
| IBM Cloud DORA page | https://www.ibm.com/products/cloud/compliance/dora |
| IBM newsroom DORA CTPP designation | https://newsroom.ibm.com/2025-12-05-ibm-designated-as-a-critical-third-party-provider-under-eu-dora |
| IBM Cloud DORA contractual mapping (PDF) | https://www.ibm.com/downloads/documents/us-en/11ed3283aed6ece6 |
| IBM DPA (canonical URL cited in IBM terms) | https://ibm.com/dpa |
| IBM Cloud Kubernetes Service | https://www.ibm.com/products/kubernetes-service |
| IKS overview | https://cloud.ibm.com/docs/containers?topic=containers-overview |
| IKS regions and zones | https://cloud.ibm.com/docs/containers?topic=containers-regions-and-zones |
| Red Hat OpenShift on IBM Cloud | https://www.redhat.com/en/technologies/cloud-computing/openshift/ibm |
| IBM completes Red Hat acquisition | https://www.ibm.com/investor/news/ibm-completes-acquisition-of-red-hat |
| Red Hat 8-K (merger; Red Hat survives as IBM subsidiary) | https://www.sec.gov/Archives/edgar/data/1087423/000095014219001516/eh1900894_8k-rh.htm |
| IBM FY2024 10-K (NY incorporation; Armonk HQ) | https://www.sec.gov/Archives/edgar/data/51143/000005114325000015/ibm-20241231.htm |

### Alibaba Cloud

| Source | URL |
|---|---|
| Alibaba Cloud Trust Center | https://www.alibabacloud.com/en/trust-center |
| Security & Privacy Compliance | https://www.alibabacloud.com/en/trust-center/compliance |
| Compliance Repository | https://www.alibabacloud.com/en/trust-center/compliance-repository-intro |
| International Website Terms of Use (contracting entities) | https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-terms-of-use-alibaba-cloud-international-website-terms-of-use |
| Data Processing Addendum | https://www.alibabacloud.com/help/en/legal/latest/fe2cxg |
| ECS regions and zones | https://www.alibabacloud.com/help/en/ecs/user-guide/regions-and-zones |
| What is OSS | https://www.alibabacloud.com/help/en/oss/user-guide/what-is-oss |
| OSS regions and endpoints | https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints |
| Alibaba Group Holding Limited articles (Cayman registered office) | https://www.sec.gov/Archives/edgar/data/1577552/000110465924092027/tm2422435d1_ex3-1.htm |
| HKEX: Alibaba Cloud (Singapore) Private Limited as international cloud entity | https://www1.hkexnews.hk/listedco/listconews/sehk/2024/0402/2024040200153.pdf |
| ISO 27001 certificate listing Alibaba Cloud Computing Ltd., Hangzhou | https://video-intl.alicdn.com/trust-center/ISO27001.pdf |
| Singapore international HQ anniversary (Alibaba Cloud blog, 2025-07-02) | https://www.alibabacloud.com/blog/alibaba-cloud-celebrates-10-years-in-singapore-with-new-data-centers-and-ai-global-competency-center_602337 |

### Cloudflare

| Source | URL |
|---|---|
| Cloudflare Trust Hub | https://www.cloudflare.com/trust-hub/ |
| ISO certifications FAQ | https://www.cloudflare.com/trust-hub/compliance-resources/iso-certifications/ |
| SOC 2 FAQ | https://www.cloudflare.com/trust-hub/compliance-resources/soc-2/ |
| DORA FAQ | https://www.cloudflare.com/trust-hub/compliance-resources/dora/ |
| Customer DPA (HTML) | https://www.cloudflare.com/cloudflare-customer-dpa/ |
| Customer DPA v6.4 (3 Apr 2026 PDF) | https://cf-assets.www.cloudflare.com/slt3lc6tev37/1TTgT35GoUNlKZYGuKWBFy/4e7dfc8cf402419a9b1cf624291fc69f/cloudflare_customer_dpa-v6.4_april_3_2026.pdf |
| Sub-processors (Cloudflare services; last updated 1 Oct 2025) | https://www.cloudflare.com/gdpr/subprocessors/cloudflare-services/ |
| Cloudflare Access | https://www.cloudflare.com/products/access/ |
| Cloudflare One / Zero Trust docs | https://developers.cloudflare.com/cloudflare-one/ |
| About / offices | https://www.cloudflare.com/about/ |
| Cloudflare, Inc. FY2024 10-K (DE; San Francisco HQ) | https://www.sec.gov/Archives/edgar/data/1477333/000147733325000069/fy202410k1.pdf |
| EU Cloud CoC verification (declared services include CDN, WAF, Access, Zero Trust) | https://eucoc.cloud/fileadmin/cloud-coc/files/reports/202503_ReportVerificationtDoA_Cloudflare_2023LVL02SCOPE4316.pdf |

### Salesforce / Slack

| Source | URL |
|---|---|
| Trust and Compliance Documentation | https://www.salesforce.com/company/legal/trust-and-compliance-documentation/ |
| SPARC (Security, Privacy and Architecture) PDF | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-security-privacy-and-architecture.pdf |
| Infrastructure & Sub-processors PDF | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/misc/salesforce-infrastructure-and-subprocessors.pdf |
| Data Processing Addendum | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Agreements/data-processing-addendum.pdf |
| DORA Mapping (Salesforce Compliance Site) | https://compliance.salesforce.com/en/documents/a006e00001ANW1mAAH |
| Slack acquisition complete | https://slack.com/blog/news/salesforce-completes-acquisition-of-slack |
| Salesforce 10-K excerpt (Salesforce Tower HQ) | https://d18rn0p25nwr6d.cloudfront.net/CIK-0001108524/388dd64f-ffa6-497c-89f3-3eea58d692de.pdf |

### ServiceNow

| Source | URL |
|---|---|
| Trust and Compliance Center | https://www.servicenow.com/company/trust.html |
| Compliance | https://www.servicenow.com/company/trust/compliance.html (regional variants exist, e.g. `/au/`) |
| Trust FAQ (DPA / subprocessors) | https://www.servicenow.com/company/trust/faq.html |
| Privacy FAQ | https://www.servicenow.com/company/trust/privacy/faq.html |
| Legal Schedules (DPA effective 3 May 2024; CMDB Amplified) | https://www.servicenow.com/schedules.html |
| Securing the ServiceNow AI Platform (ebook) | https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/ebook/ebk-how-servicenow-delivers-safe-and-secure-cloud-services.pdf |
| Office locations (HQ) | https://www.servicenow.com/company/locations.html |
| ITSM product | https://www.servicenow.com/products/itsm.html |
| CMDB product | https://www.servicenow.com/in/products/servicenow-platform/configuration-management-database.html |
| CMDB docs | https://www.servicenow.com/docs/r/servicenow-platform/configuration-management-database-cmdb/c_ITILConfigurationManagement.html |
| ServiceNow, Inc. 10-K (DE; Santa Clara HQ) | https://www.sec.gov/Archives/edgar/data/1373715/000137371526000007/now-20251231.htm |

### SAP

| Source | URL |
|---|---|
| Trust Center — certifications | https://www.sap.com/about/trust-center/certification-compliance.html |
| Trust Center — data privacy / DPA / subprocessors | https://www.sap.com/about/trust-center/data-privacy.html |
| Trust Center — agreements | https://www.sap.com/about/trust-center/agreements.html |
| Trust Center — data centers | https://www.sap.com/about/trust-center/data-center.html |
| SAP SE Impressum (Walldorf registered office) | https://www.sap.com/germany/about/legal/impressum-se.html |
| Articles of Incorporation (registered office Walldorf) | https://www.sap.com/docs/download/investors/2025/sap-2025-governance-articles-of-incorporation.pdf |
| Enterprise Management ISO 27001 certificate (includes S/4HANA Cloud Public Edition) | https://www.sap.com/documents/2025/06/98e011a4-0b7f-0010-bca6-c68f7e60039b.html |
| SAP designated CTPP under DORA | https://www.sap.com/documents/2025/12/dae8fa96-307f-0010-bca6-c68f7e60039b.html |
| S/4HANA Cloud Public Edition product | https://www.sap.com/canada/products/erp/s4hana.html |
| S/4HANA Cloud Public Edition CSA (IRAP; 2025-H1) | https://www.sap.com/about/trust-center/certification-compliance/sap-s-4hana-cloud--public-edition-cloud-security-assessment--csa.html |

### Workday (brief)

| Source | URL |
|---|---|
| Compliance and Third-Party Assessments | https://www.workday.com/en-us/why-workday/trust/compliance.html |
| Security Compliance program | https://security.workday.com/security-compliance |
| Shared responsibility | https://security.workday.com/shared-responsibility |
| Subprocessors | https://www.workday.com/en-us/legal/subprocessors.html |
| Universal Data Processing Exhibit (SCC v20.1 PDF) | https://workday.com/content/dam/web/en-us/documents/legal/workday-universal-data-processing-exhibit-scc-v20.1.pdf |
| Workday, Inc. 10-K (DE; Pleasanton HQ; HCM) | https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm |

---

## Oracle Cloud Infrastructure

### Legal / headquarters

Oracle Corporation is the US registrant. FY2026 10-K cover lists principal executive offices at 2300 Oracle Way, Austin, Texas 78741, and state of incorporation **Delaware**. OSM `headquarters` candidate: `us`. The model cannot record “Delaware legal entity / Austin operational HQ”.

The ESA CTPP designation is **Oracle Nederland B.V.**, not Oracle Corporation. A single OSM ICT Provider row named “Oracle” therefore collapses US parent, Dutch designated entity, and global OCI operations.

### OSM type pick

**`cloud-infrastructure`**, because OCI Compute, networking, and storage are IaaS. Insufficient: Oracle also sells Autonomous Database (PaaS), Fusion / NetSuite (SaaS — no enum), and on-premises Database (`software-vendor`). One type cannot describe the estate.

### Facts table

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal name | `name` | Oracle Corporation | US registrant | A | https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/R1.htm |
| Incorporation | *(no field)* | Delaware | Legal entity | A | same |
| Operational HQ | `headquarters` | `us` (Austin, TX) | Principal executive offices | A | same |
| Provider type | `type` | `cloud-infrastructure` (best-fit; insufficient) | OCI IaaS; not Fusion/NetSuite/DB license | B | https://www.oracle.com/cloud/ |
| Processing locations | `data_processing_locations` | Customer-selected OCI region / AD; Hosting Policies define Data Center Region (Europe = EU+UK+CH; APAC excludes China — Oracle states it has no data centers in China) | Per order / activation | B/C | https://www.oracle.com/contracts/docs/ocloud_hosting_delivery_policies_3089853.pdf ; https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm |
| Commercial + government regions | *(no first-class region object)* | Oracle states 50 commercial and government regions; each region one or more ADs | Marketing + docs; exact list is realm-specific | B | https://www.oracle.com/cloud/ ; https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm |
| DPA existence | `gdpr_dpa_signed` | Public DPA exists; **signed** is customer-order dependent — do not set `true` | Cloud Services orders that incorporate the DPA | A exists / C signed | https://www.oracle.com/legal/privacy/services-privacy-policy/ ; https://www.oracle.com/contracts/docs/data_processing_agreement_011218_4261005.pdf |
| Subprocessors | `subcontractors` / `subcontracting_allowed` | Affiliates and third-party subprocessors listed in My Oracle Support Doc ID **2121811.1**; change notices Doc ID **2288528.1**; 14-calendar-day objection in DPA | Login / support portal; not a public dump | B | https://www.oracle.com/legal/privacy/services-privacy-policy/ ; https://www.oracle.com/corporate/security-practices/corporate/supply-chain/suppliers/ |
| Subcontracting | `subcontracting_allowed` | `conditional` (authorized with notice/objection) | DPA Cloud Services | B | DPA PDF above |
| ISO/IEC 27001, 27017, 27018, 27701 | `certifications` | Attestations listed for OCI on Cloud Compliance; **service- and often region-specific** | Oracle: “generally specific to a certain cloud service and may also be specific to a certain data center or geographic region” | B | https://www.oracle.com/corporate/cloud-compliance/ |
| SOC 1 / SOC 2 / SOC 3 | `certifications` | Listed as OCI attestations | Same service/region caveat | B | same |
| CSA STAR, PCI DSS, C5, FedRAMP, IRAP, ISMAP, MTCS, HDS, ENS, EU Cloud CoC | `certifications` | Dashboard lists these frameworks for OCI; EU Cloud CoC shows Verification ID 2022LVL02SCOPE4214 for OCI | Per-framework scope; click-through on the dashboard | B | same |
| DORA contractual support | `dora_notification_clause` | Public **Oracle Contract Checklist for EU DORA** (PDF) on the compliance page; clause presence in a *customer* contract is C | Advisory, not a certification | B/C | https://www.oracle.com/corporate/cloud-compliance/ |
| DORA CTPP | *(no field for designated entity)* | **Oracle Nederland B.V.** on ESA list of 18 Nov 2025 | Dutch legal entity, not Oracle Corporation | A | https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf |
| Customer contract dates, notice, audit rights, risk_level, RTO/RPO, criticality | `contract_*`, `notice_period_days`, `audit_rights`, `risk_level`, posture fields | Unset | Always customer-specific | C/D | — |
| `gdpr_dpa_signed` as boolean | `gdpr_dpa_signed` | Unset unless a named customer signed | Existence of a form DPA ≠ signed | C | — |

Oracle itself says attestations are “as-is”, not incorporated into contracts, and customers remain responsible for suitability. Do not copy the attestation dashboard into OSM as universal compliance.

---

## IBM Cloud (and Red Hat)

### Legal / headquarters

International Business Machines Corporation is incorporated in **New York** (1911), principal executive offices **One New Orchard Road, Armonk, New York 10504**. OSM `headquarters`: `us`. Incorporation is NY, not Delaware.

Red Hat: IBM completed the acquisition on **9 July 2019**. The 8-K states Merger Sub merged into Red Hat, Inc. (Delaware), **Red Hat surviving as a wholly owned subsidiary of IBM**. IBM’s investor release says IBM is “preserving Red Hat’s independence and neutrality”. Current trademark notices use **Red Hat, LLC** or its subsidiaries. Red Hat remains a distinct legal and commercial brand.

### IBM vs Red Hat as ICT Providers

| Situation | OSM treatment (investigation, not schema change) |
|---|---|
| Self-managed Red Hat OpenShift / RHEL on customer or third-party infrastructure | **Separate ICT Provider** `redhat` (`software-vendor`). IBM is parent, not the contracting software vendor. |
| Red Hat OpenShift **on IBM Cloud** (managed) | **IBM Cloud** is the ICT Provider of the managed service. Red Hat is the software origin and IBM affiliate/subprocessor. One Service, provider = IBM; optional second provider or characteristic for Red Hat IP. |
| IBM Cloud Kubernetes Service | IBM only. No Red Hat legal counterpart. |

Do not collapse Red Hat into IBM for the estate items “Red Hat OpenShift” and “Red Hat Enterprise Linux” (rows 33–34 of the 100-item list). Do not invent a second IBM provider for IKS.

### OSM type pick

**`cloud-infrastructure`** or **`cloud-platform`** for IBM Cloud. IKS/OpenShift-on-IBM-Cloud are closer to `managed-service`. Red Hat standalone is `software-vendor`. Enum cannot express hybrid-cloud vendor + subsidiary software company + managed OpenShift.

### Facts table

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal name | `name` | International Business Machines Corporation | US parent | A | https://www.sec.gov/Archives/edgar/data/51143/000005114325000015/ibm-20241231.htm |
| Incorporation | *(no field)* | New York | Legal entity | A | same |
| Operational HQ | `headquarters` | `us` (Armonk, NY) | Principal executive offices | A | same |
| Provider type | `type` | `cloud-infrastructure` (best-fit; insufficient) | IBM Cloud IaaS/PaaS; not Red Hat licenses | B | https://www.ibm.com/trust |
| Red Hat legal relationship | *(no parent/subsidiary field)* | Wholly owned subsidiary since 2019-07-09; Red Hat survived the merger | Corporate, not a service certification | A | https://www.ibm.com/investor/news/ibm-completes-acquisition-of-red-hat ; https://www.sec.gov/Archives/edgar/data/1087423/000095014219001516/eh1900894_8k-rh.htm |
| DPA existence | `gdpr_dpa_signed` | Canonical DPA at ibm.com/dpa plus **per-service DPA Exhibits** in the Service Description | Exhibit-scoped; signed is C | A/B / C signed | https://ibm.com/dpa ; https://www.ibm.com/downloads/documents/us-en/11ed3283aed6ece6 |
| Subprocessors / locations | `subcontractors`, `data_processing_locations` | Documented in DPA Exhibits / datasheets / transaction documents; IBM notifies location changes via a self-service portal | Per Cloud service | B/C | IBM DORA PDF above |
| Subcontracting | `subcontracting_allowed` | IBM DORA mapping: subcontracting of ICT services, including those supporting critical/important functions, **is permitted**; subcontractors documented in SD + DPA Exhibit | IBM Cloud public cloud | B | same |
| ISO 27001 — infrastructure certificate | `certifications` | Published list includes Backup, Bare Metal, Block Storage, Direct Link, File Storage, HSM, Load Balancer, Object Storage (IaaS), Virtual Servers, SAP-Certified Cloud Infrastructure | **That certificate list does not name IKS or OpenShift on IBM Cloud** | B | https://www.ibm.com/products/cloud/compliance/iso-27001 |
| ISO 27001 / 27701 — VPC, PaaS, SaaS | `certifications` | IBM states VPC/PaaS/SaaS offerings implemented PIMS under ISO/IEC 27701:2019; both ISMS and PIMS appear on the VPC/PaaS/SaaS ISO 27001 certificate | Separate certificate from classic IaaS list; check DPA Exhibit per offering | B | same |
| SOC 2 Type 2 | `certifications` | Explicitly includes **“IBM Cloud Kubernetes Service and Red Hat OpenShift on IBM Cloud”** (and ROKS Classic / VPC variants) | Platform SOC 2 list; reports on request | B | https://www.ibm.com/products/cloud/compliance/soc-2 |
| SOC 3 | `certifications` | Same IKS / OpenShift-on-IBM-Cloud naming | Public-style SOC 3 | B | https://www.ibm.com/products/cloud/compliance/soc-3 |
| DORA CTPP | *(no designated-entity field)* | IBM designated by EBA/EIOPA/ESMA; ESA list name **International Business Machine Corporation** (ESA spelling) | IBM parent, not Red Hat LLC | A | https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf ; https://www.ibm.com/products/cloud/compliance/dora ; https://newsroom.ibm.com/2025-12-05-ibm-designated-as-a-critical-third-party-provider-under-eu-dora |
| DORA notification clause | `dora_notification_clause` | Mapping PDF discusses Art. 30 location-change notice via portal; whether a *customer* contract contains the clause is C | Public mapping ≠ signed clause | B/C | https://www.ibm.com/downloads/documents/us-en/11ed3283aed6ece6 |
| IKS regions | `data_processing_locations` | Documented VPC multizone regions include Sydney, Chennai, Mumbai, Osaka, Tokyo, Frankfurt, Madrid, London, Montreal, Toronto, Dallas, Washington DC, São Paulo (each 3 zones) | Cluster location is customer-chosen | B/C | https://cloud.ibm.com/docs/containers?topic=containers-regions-and-zones |
| Customer risk / RTO / contract | several | Unset | — | C/D | — |

---

## Alibaba Cloud

### Legal / headquarters (Cayman vs Hangzhou vs Singapore)

Three layers, none of which OSM `headquarters` can hold together:

1. **Ultimate parent:** Alibaba Group Holding Limited — Cayman Islands exempted company; registered office Trident Trust Company (Cayman) Limited, Fourth Floor, One Capital Place, P.O. Box 847, George Town, Grand Cayman.
2. **PRC cloud operating entity on the ISO certificate:** Alibaba Cloud Computing Ltd. (阿里云计算有限公司), West Tower T6, UK Center (EFC), No. 1122 Xiang Wang Street, Yuhang District, **Hangzhou**, Zhejiang, China; registration address No. 12 Zhuantang Technology Economic Zone, Xihu District, Hangzhou.
3. **International contracting:** default **Alibaba Cloud (Singapore) Private Limited** (HKEX: Singapore-incorporated, indirect wholly owned subsidiary of Alibaba Holding). Terms of Use also assign **Alibaba Cloud (Europe) Limited** (UK/CH/non-EEA Europe), **Alibaba (Netherlands) B.V.** (EEA), **Alibaba Cloud US LLC** (US accounts registered before 20 Mar 2026), **Alibaba Cloud (India) LLP**, **Alibaba Cloud (Malaysia) Sdn. Bhd.** Alibaba Cloud’s own 2025-07-02 blog calls Singapore its **international headquarters**.

OSM `headquarters` candidates if forced to one code: `cn` (Hangzhou operations / PRC entity), `sg` (international HQ / default contractor), or `ky` (listed parent). None is sufficient. Record the split; do not pick silently.

### OSM type pick

**`cloud-infrastructure`**. Insufficient: China vs international partitions, ECS/OSS vs many PaaS/SaaS products, and no `saas` value.

### Facts table

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Parent legal name | `name` (if modelling the group) | Alibaba Group Holding Limited | Cayman parent | A | https://www.sec.gov/Archives/edgar/data/1577552/000110465924092027/tm2422435d1_ex3-1.htm |
| Parent incorporation | *(no field)* | Cayman Islands | Registered office George Town | A | same |
| PRC operating entity | *(no field)* | Alibaba Cloud Computing Ltd., Hangzhou | ISO 27001 certificate holder / address | A | https://video-intl.alicdn.com/trust-center/ISO27001.pdf |
| International contractor (default) | *(no field)* | Alibaba Cloud (Singapore) Private Limited | Billing-address default; other entities by jurisdiction | A | https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-terms-of-use-alibaba-cloud-international-website-terms-of-use ; https://www1.hkexnews.hk/listedco/listconews/sehk/2024/0402/2024040200153.pdf |
| International HQ | `headquarters` tension | Singapore (international HQ claim) vs Hangzhou (PRC ops) vs Cayman (parent) | Do not flatten | A | https://www.alibabacloud.com/blog/alibaba-cloud-celebrates-10-years-in-singapore-with-new-data-centers-and-ai-global-competency-center_602337 |
| Provider type | `type` | `cloud-infrastructure` (best-fit; insufficient) | ECS/OSS IaaS | B | https://www.alibabacloud.com/en/trust-center |
| DPA existence | `gdpr_dpa_signed` | Public DPA; customer is controller/processor, Alibaba Cloud processor; **signed** is C | International site; PRC site may differ | A / C signed | https://www.alibabacloud.com/help/en/legal/latest/fe2cxg |
| Subprocessors | `subcontractors` | Up-to-date list **behind Alibaba Cloud account login**; ≥10 working days’ notice; objection + terminate that Service | Not a public URL | B | same |
| Subcontracting | `subcontracting_allowed` | `conditional` | DPA | B | same |
| ISO 27001 / 27017 / 27018 / 27701, SOC 1/2/3, CSA STAR, PCI DSS, C5, MTCS, DPTM, MLPS, K-ISMS, etc. | `certifications` | Trust Center lists frameworks; **certificate PDFs carry product and region/AZ scope** (ISO 27001 PDF enumerates services and AZs including Hangzhou, Singapore, Frankfurt, Virginia, etc.) | Do not copy the marketing list without the certificate SoA | B | https://www.alibabacloud.com/en/trust-center/compliance ; https://video-intl.alicdn.com/trust-center/ISO27001.pdf |
| Reports access | *(no field)* | Compliance Repository (SOC, certificates; BAA/NDA online) | Account / agreement gated | B | https://www.alibabacloud.com/en/trust-center/compliance-repository-intro |
| DORA CTPP | — | **Not** on ESA 18 Nov 2025 list. No official Alibaba DORA designation page found | Absence is A for the ESA list; Alibaba-specific DORA clause is D | A / D | https://www.esma.europa.eu/sites/default/files/2025-11/List_of_designated_CTPPs.pdf |
| Data residency | `data_processing_locations` | Customer-chosen region (e.g. `cn-hangzhou`, `eu-central-1` Frankfurt, `ap-southeast-1` Singapore). Mainland-China OSS access policy changed 20 Mar 2025 (custom domain for new users) | Per product/region | B/C | https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints |
| Customer contract / risk | several | Unset | — | C/D | — |

---

## Cloudflare

### Legal / headquarters

Cloudflare, Inc. — incorporated **Delaware** (July 2009); principal executive offices **101 Townsend Street, San Francisco, California 94107**. OSM `headquarters`: `us`. European offices exist (London, Munich, etc.) but are not the legal HQ.

### OSM type pick

**`network-provider`** is the closest enum (global anycast CDN, DNS, WAF, DDoS, Zero Trust edge). Alternative `cloud-platform` (Workers, R2) is worse as a single label. Insufficient: Cloudflare is not a classic IaaS cloud, not a software-license vendor, and SaaS/edge/SASE have no enum. “Connectivity cloud” is Cloudflare’s own term, not OSM’s.

### Facts table

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal name | `name` | Cloudflare, Inc. | US registrant | A | https://www.sec.gov/Archives/edgar/data/1477333/000147733325000069/fy202410k1.pdf |
| Incorporation | *(no field)* | Delaware | Legal entity | A | same |
| Operational HQ | `headquarters` | `us` (San Francisco) | Principal executive offices | A | same ; https://www.cloudflare.com/about/ |
| Provider type | `type` | `network-provider` (best-fit; insufficient) | CDN/WAF/edge; Workers/R2 are platform | B | https://www.cloudflare.com/trust-hub/ |
| DPA existence | `gdpr_dpa_signed` | Public DPA v6.4 dated **3 April 2026**; **signed** is C | Cloudflare services under the Main Agreement | A / C signed | https://www.cloudflare.com/cloudflare-customer-dpa/ |
| Subprocessors | `subcontractors` | Public list last updated **1 Oct 2025**; includes Slack, Zendesk, Salesforce, Google, Oracle America, AWS, plus Cloudflare Group affiliates | Activity-scoped (e.g. Google for Zero Trust and Developer Platform) | A | https://www.cloudflare.com/gdpr/subprocessors/cloudflare-services/ |
| Subprocessor notice | `subcontracting_allowed` | `conditional`; DPA: 30 days’ advance list update; 10-day written objection | DPA 4.3–4.4 | A | DPA PDF |
| ISO 27001:2022, 27018:2019, 27701:2019 | `certifications` | Certified; scope stated as **“Cloudflare global cloud platform and subsidiary offices”**; 27701 as processor **and** controller | Certificate/SoA via dashboard or sales; SoA under NDA | B | https://www.cloudflare.com/trust-hub/compliance-resources/iso-certifications/ |
| SOC 2 Type II | `certifications` | Security, Confidentiality, Availability; **all Cloudflare plans in-scope**; org-wide exam; NDA to obtain report; no SOC 1 / SOC 3 | Not a public report | B | https://www.cloudflare.com/trust-hub/compliance-resources/soc-2/ |
| PCI DSS Level 1 | `certifications` | Annual QSA; cited in DPA | Cardholder-data relevant services; confirm SoA | B | DPA |
| EU Cloud CoC | `certifications` | Verification report lists declared services including **CDN, WAF, Cloudflare Access, Cloudflare One, Cloudflare Zero Trust** | Adherence/verification, not ISO | B | https://eucoc.cloud/fileadmin/cloud-coc/files/reports/202503_ReportVerificationtDoA_Cloudflare_2023LVL02SCOPE4316.pdf |
| DORA CTPP | — | Cloudflare states it **has not been designated** critical; not on ESA list | Provider statement + ESA list | A | https://www.cloudflare.com/trust-hub/compliance-resources/dora/ ; ESA PDF |
| DORA contracts | `dora_notification_clause` | Cloudflare publishes a DORA mapping to standard terms; customer clause is C | Mapping ≠ signed Art. 30 pack | B/C | same |
| Processing locations | `data_processing_locations` | Global edge PoPs; Data Localization Suite / Regional Services optional; subprocessor locations listed (US, EEA, etc.) | Customer product + localization SKU | B/C | Trust Hub; subprocessors page |
| Customer risk / RTO | several | Unset | — | C/D | — |

---

## Salesforce (and Slack)

### Legal / headquarters / Slack ownership

Salesforce, Inc. (f/k/a salesforce.com, inc.) — DPA: company **incorporated in Delaware, US**; 10-K: principal executive offices **Salesforce Tower, 415 Mission Street, 3rd Floor, San Francisco, California 94105**. OSM `headquarters`: `us`.

Salesforce completed the acquisition of Slack Technologies, Inc. (announcement on Slack’s news blog). Slack continues under the Slack brand. The Salesforce DPA still names **Slack Technologies, LLC** (Delaware LLC) and **Slack Technologies Limited** (Ireland private company) as SFDC entities, with **separate APEC PRP** for Slack vs the Salesforce Group.

Trust documentation: **Sales Cloud** is under “Salesforce Services” SPARC/NLI; **Slack** has its **own SPARC (2026-05-22) and NLI (2026-07-24)**. Shared Infrastructure & Sub-processors document (2026-08-18).

### One vs two ICT Providers

| Option | When it fits OSM | Stress |
|---|---|---|
| **One** ICT Provider `salesforce` | Same parent; one DPA family; Slack listed as SFDC affiliate | Hides Slack LLC as a possible contracting party and separate SPARC |
| **Two** ICT Providers `salesforce` + `slack` | Separate products, separate SPARC/NLI, Slack LLC / Slack Technologies Limited still named | Parent/subsidiary has no OSM field; double-counts concentration if both point at CRM+collab |

Investigation recommendation: **one parent ICT Provider** for vendor-risk roll-up, **two Services** (`….sales-cloud`, `….slack`) with distinct offerings and provenance. If a customer’s Slack order is with Slack Technologies, LLC, record that in `contract_ref` (customer fact, class C) rather than inventing a second global provider by default.

### OSM type pick

**`software-vendor`**. Insufficient: Sales Cloud and Slack are multi-tenant SaaS; no `saas` enum. Not `cloud-infrastructure` (they run on first-party + Hyperforce/AWS).

### Facts table

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal name | `name` | Salesforce, Inc. | Parent | A | DPA; 10-K |
| Incorporation | *(no field)* | Delaware | Legal entity | A | DPA (“incorporated in Delaware, US”) |
| Operational HQ | `headquarters` | `us` (San Francisco) | Principal executive offices | A | https://d18rn0p25nwr6d.cloudfront.net/CIK-0001108524/388dd64f-ffa6-497c-89f3-3eea58d692de.pdf |
| Slack ownership | *(no parent field)* | Slack acquired; Slack Technologies, LLC + Slack Technologies Limited named in DPA | Corporate + DPA entities | A | https://slack.com/blog/news/salesforce-completes-acquisition-of-slack ; DPA PDF |
| Provider type | `type` | `software-vendor` (best-fit; SaaS missing) | CRM + Slack SaaS | B | — |
| DPA existence | `gdpr_dpa_signed` | Public pre-signed DPA; becomes binding when Customer completes and Salesforce receives it | **Signed is C** | A / C | https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Agreements/data-processing-addendum.pdf |
| Subprocessors | `subcontractors` | Shared I&S document; subscribe for new sub-processors | Service × infrastructure (first-party vs Hyperforce vs Einstein) | B | https://www.salesforce.com/company/legal/trust-and-compliance-documentation/ ; I&S PDF |
| ISO 27001/27017/27018 | `certifications` | SPARC: certification for Covered Services **with a long exclusion list** (Communications Cloud, Consumer Goods Cloud, Salesforce Starter, Foundations, Agentforce Vibes, Tableau Next, etc.) | **Not all Salesforce SKUs** | B | SPARC PDF |
| SOC 1 / SOC 2 / SOC 3 | `certifications` | SPARC: independent SOC evaluations for Covered Services **with a different exclusion list** | Download from compliance site | B | SPARC PDF ; https://www.salesforce.com/company/legal/trust-and-compliance-documentation/ |
| DORA mapping | `dora_notification_clause` | Public DORA Mapping document for Salesforce online services vs Art. 30-style contract requirements | Mapping for regulated customers; **Salesforce is not on the official ESA CTPP list** | B / A (not designated) | https://compliance.salesforce.com/en/documents/a006e00001ANW1mAAH ; ESA PDF |
| Data residency | `data_processing_locations` | Instance / Hyperforce region; I&S lists countries of storage/processing per service | Customer org | B/C | I&S PDF ; Trust & Compliance “Where is my Salesforce instance located?” |
| Customer risk / RTO | several | Unset | — | C/D | — |

---

## ServiceNow

### Legal / headquarters

ServiceNow, Inc. — **Delaware** corporation; principal executive offices **2225 Lawson Lane, Santa Clara, California 95054**. OSM `headquarters`: `us`.

### OSM type pick

**`software-vendor`**. Insufficient: the commercial offering is SaaS on the “ServiceNow AI Platform”; no `saas` enum. Not `cloud-infrastructure` (they host on their sites and hyperscalers).

### Facts table

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal name | `name` | ServiceNow, Inc. | US registrant | A | https://www.sec.gov/Archives/edgar/data/1373715/000137371526000007/now-20251231.htm |
| Incorporation | *(no field)* | Delaware | Legal entity | A | same |
| Operational HQ | `headquarters` | `us` (Santa Clara, CA) | Company headquarters | A | https://www.servicenow.com/company/locations.html |
| Provider type | `type` | `software-vendor` (best-fit; SaaS missing) | ITSM/CMDB SaaS | B | https://www.servicenow.com/company/trust.html |
| DPA existence | `gdpr_dpa_signed` | Standard DPA effective **3 May 2024** on Legal Schedules; Trust FAQ points to it | **Signed is C** | A / C | https://www.servicenow.com/schedules.html ; https://www.servicenow.com/company/trust/faq.html |
| Subprocessors | `subcontractors` | DPA/FAQ: affiliates including USA, Netherlands, Australia, India, UK; new sub-processors notified via support portal; objection rights | Affiliate list in DPA; full third-party list via Trust/CORE | B | Trust FAQ; pre-signed DPA PDF |
| Subcontracting | `subcontracting_allowed` | `conditional` | DPA | B | same |
| ISO 27001:2022, 27017, 27018, 27701, 42001, 20000-1, 22301, 9001 | `certifications` | Stated on Trust/compliance and “Securing the ServiceNow AI Platform”; reports via CORE (customers) | Confirm current SoA per product/region in CORE — not all public PDFs | B | https://www.servicenow.com/company/trust.html ; ebook PDF |
| SOC 1 Type 2 (since 2011) / SOC 2 Type 2 (since 2013; security, availability, confidentiality) | `certifications` | Stated on compliance pages | CORE / NDA | B | compliance pages |
| Hosting / residency | `data_processing_locations` | Customer **selects hosting site region at order**; instance stays until written change; site pairs in compatible jurisdictions; also hyperscaler and Protected Platform variants (e.g. SPP Singapore) | Per instance | B/C | ebook PDF |
| DORA CTPP | — | **Not** on ESA list. ServiceNow publishes **customer** DORA enablement (IRM/ITSM/CMDB) — that is a product story, not a provider designation | Do not treat as `dora_notification_clause=true` | A / C | ESA PDF ; community/product blogs |
| Customer risk / RTO | several | Unset | — | C/D | — |

---

## SAP

### Legal / headquarters

**SAP SE** — registered office and domicile **Walldorf, Germany**; Impressum and Articles: **Dietmar-Hopp-Allee 16, 69190 Walldorf**; Commercial Register Mannheim **HRB 719915**. OSM `headquarters`: `de`. Legal and operational HQ align (unlike Alibaba). Walldorf/St. Leon-Rot are also named as SAP-owned data-center sites in Trust Center IT-Grundschutz text.

### OSM type pick

**`software-vendor`**. Insufficient: S/4HANA Cloud Public Edition is SaaS ERP (no `saas`); BTP is closer to `cloud-platform`; RISE private edition is closer to `managed-service`; on-prem S/4HANA is licensed software. Enum cannot say “ERP”.

### Facts table

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal name | `name` | SAP SE | European Company | A | https://www.sap.com/germany/about/legal/impressum-se.html |
| Registered office | `headquarters` | `de` (Walldorf) | Articles + Impressum | A | same ; https://www.sap.com/docs/download/investors/2025/sap-2025-governance-articles-of-incorporation.pdf |
| Provider type | `type` | `software-vendor` (best-fit; SaaS/ERP/BTP missing) | Cloud ERP + platform | B | — |
| DPA existence | `gdpr_dpa_signed` | SAP states it **signs DPAs with each customer**; cloud DPA on Trust Center | Form exists (A); a given customer’s signature is C | A / C | https://www.sap.com/about/trust-center/data-privacy.html |
| Subprocessors | `subcontractors` | Product- and service-specific lists on Trust Center; email subscribe for changes | Per cloud service; often login | B | same |
| ISO 27001 | `certifications` | Enterprise Management certificate includes **SAP S/4HANA Cloud Public Edition** (SoA Ver. 2.2 dated 2025-04-29; operations of a named product set) | **That certificate is not “all SAP products”** | B | https://www.sap.com/documents/2025/06/98e011a4-0b7f-0010-bca6-c68f7e60039b.html |
| ISO 27017 / 27018 / 22301 / 42001, SOC 1, SOC 2, C5, PCI, CSA STAR | `certifications` | Trust Center lists; SOC/C5 increasingly as “SAP Central Cloud Services”; many downloads via SAP for Me | Report- and period-specific | B | https://www.sap.com/about/trust-center/certification-compliance.html |
| Data centers | `data_processing_locations` | Interactive map; S/4HANA and BTP hosted; customer may select DC at implementation; secondary DCs in region for DR; some services on Microsoft/Amazon (CSA notes Australian hyperscaler deployment) | Per service/SKU | B/C | https://www.sap.com/about/trust-center/data-center.html ; CSA page |
| DORA CTPP | *(no designated-entity field)* | SAP states designation by ESAs as CTPP on **17 November 2025**; **SAP SE** is on the official ESA list | SAP SE, not a US subsidiary | A | https://www.sap.com/about/trust-center/certification-compliance.html ; https://www.sap.com/documents/2025/12/dae8fa96-307f-0010-bca6-c68f7e60039b.html ; ESA PDF |
| DORA notification clause | `dora_notification_clause` | Designation ≠ a populated boolean on a customer contract | Leave unset unless a named contract is in evidence | C | — |
| Customer risk / RTO | several | Unset | — | C/D | — |

---

## Workday (brief — estate item 61 HCM)

Workday, Inc. — **Delaware**; principal executive offices **6110 Stoneridge Mall Road, Pleasanton, California 94588**. OSM `headquarters`: `us`. Type pick: **`software-vendor`** (SaaS HCM; enum insufficient).

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal / HQ | `name`, `headquarters` | Workday, Inc.; `us` | DE corp / Pleasanton HQ | A | https://www.sec.gov/Archives/edgar/data/1327811/000132781125000056/wday-20250131.htm |
| HCM as product | Service candidate | Human Capital Management is a named Workday suite (recruit-to-retire) | Product, not a customer’s HR business service | A | same 10-K ; https://www.workday.com/en-us/why-workday/trust/compliance.html |
| ISO 27001/27017/27018 | `certifications` | Consolidated certificate; **Information Security scope includes Human Capital Management** (and Finance, Payroll, Platform, etc.) | Product-scoped | B | compliance page |
| ISO 27701 | `certifications` | Privacy Governance scope includes HCM | Product-scoped | B | same |
| SOC 1/2/3 | `certifications` | Enterprise Products (and other named lines); SOC 2+ maps NIST CSF / 800-171 | Report-scoped | B | same |
| DPE / DPA | `gdpr_dpa_signed` | Universal Data Processing Exhibit published; signed is C | Covered Services | A / C | https://workday.com/content/dam/web/en-us/documents/legal/workday-universal-data-processing-exhibit-scc-v20.1.pdf |
| Subprocessors | `subcontractors` | Public enterprise list + professional-services list; AWS/Azure/colocation called out as hosting (ISO cert excludes hosting locations from ISMS boundary) | Product-line columns | B | https://www.workday.com/en-us/legal/subprocessors.html ; ISO 27018 cert text |
| DORA CTPP | — | **Not** on ESA list. No official Workday DORA designation page found in this pass | Leave `dora_notification_clause` unset | A / D | ESA PDF |
| Customer risk / RTO | several | Unset | — | C/D | — |

---

## Service sections

Each service below is a **candidate OSM Service** (stable technological capability), not a vendor SKU dump. Offerings are variants. Customer posture (criticality, RTO/RPO, `risk_level`) stays unset.

### OCI Compute

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical name | Oracle Cloud Infrastructure Compute (instances: VM and bare metal) | A | https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm |
| Technological service | On-demand compute capacity in an OCI region/AD | — | — |
| vs offering | Shapes (standard / dense I/O / GPU / HPC; AMD, Intel, Arm), Flex VMs, dedicated VM hosts, Cloud@Customer | B | https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm |
| Provider | Intrinsic: Oracle / OCI | A | — |
| Location | Instance is **availability-domain-specific**; region chosen by customer | B/C | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm |
| Certifications | Fall under OCI attestations; **do not assert ISO/SOC without the service/region row** on the compliance dashboard | B | https://www.oracle.com/corporate/cloud-compliance/ |
| OSM fit | Strong: IaaS compute is a technological service. Shared-responsibility: customer OS/workload is not the Service definition. | — | — |
| Do not invent | Tenant-level SLA, RTO/RPO, “production criticality” | C/D | — |

### Oracle Database / Autonomous Database

| Item | Notes | Class | URL |
|---|---|---|---|
| Product naming | Marketing now uses **Autonomous AI Database**; estate list says Oracle Database / Autonomous Database. On-premises Oracle Database is a **different** delivery (license / `software-vendor`) than ADB on OCI. | A | https://www.oracle.com/autonomous-database/ |
| Technological service | Managed Oracle Database engine (self-patching, encryption-on cited on Trust Center) | B | https://www.oracle.com/trust/ |
| Offerings | Serverless vs dedicated Exadata; Cloud@Customer; **multicloud** (ADB in AWS/Azure/Google data centers) — provider chain is then Oracle **plus** hyperscaler | B | Autonomous product page |
| Region | Docs: Autonomous AI Database **available in all commercial-realm regions**; government cloud separate | B | https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/autonomous-region-availability.html |
| OSM clash | Licensed Oracle Database (row 46) vs ADB as cloud PaaS. One Service “oracle-database” with offerings `on-prem`, `oci-autonomous`, `multicloud` is cleaner than three fake providers. | — | — |
| Do not invent | Customer Data Guard topology, RPO, “this DB is critical” | C/D | — |

### IBM Cloud Kubernetes Service

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical name | IBM Cloud Kubernetes Service (managed, certified Kubernetes; IBM manages the master) | A | https://www.ibm.com/products/kubernetes-service ; https://cloud.ibm.com/docs/containers?topic=containers-overview |
| Technological service | Managed Kubernetes control plane + worker-node lifecycle on IBM Cloud | — | — |
| Offerings | Classic vs VPC infrastructure; region/zone placement | B | https://cloud.ibm.com/docs/containers?topic=containers-regions-and-zones |
| Provider | IBM Cloud only | A | — |
| Certifications | Named on **SOC 2 Type 2** and **SOC 3** platform lists. **Not** in the published ISO 27001 *infrastructure* bullet list. Check the offering’s DPA Exhibit / platform ISO certificate before writing ISO 27001 on this Service. | B | https://www.ibm.com/products/cloud/compliance/soc-2 ; https://www.ibm.com/products/cloud/compliance/iso-27001 |
| OSM fit | Strong managed container platform. Distinct from estate “Kubernetes” (CNCF project) and from self-managed OpenShift. | — | — |

### Red Hat OpenShift on IBM Cloud

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical name | Red Hat OpenShift on IBM Cloud (managed OpenShift; IBM automates infra + upgrades) | A | https://www.redhat.com/en/technologies/cloud-computing/openshift/ibm |
| vs self-managed OpenShift | Different Service. Self-managed OpenShift → ICT Provider Red Hat. This managed SKU → ICT Provider IBM (Red Hat as software/affiliate). | A | IBM SOC 2 names both “IBM Cloud Kubernetes Service and Red Hat OpenShift on IBM Cloud” |
| Legal | Does not make Red Hat cease to be a separate company | A | 2019 8-K |
| Certifications | Same SOC 2/3 naming as IKS; ISO only if the Exhibit/certificate says so | B | IBM SOC 2 page |
| OSM fit | Tests **provider vs product brand**. Do not set `providers: [ibm, redhat]` unless the investigation decides dual-provider semantics for IP vs operator. | — | — |

### Alibaba Cloud ECS

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical name | Elastic Compute Service (ECS) | A | https://www.alibabacloud.com/help/en/ecs/user-guide/regions-and-zones |
| Technological service | Elastic VM compute in a public-cloud region/zone | — | — |
| Location | Many regions; China (Hangzhou) `cn-hangzhou` has multiple zones; international regions include Frankfurt, Singapore, Virginia, etc. **Supported regions vary by product.** | B/C | same |
| Certifications | Appear on Alibaba Cloud ISO/SOC materials **when the certificate scope lists ECS** (ISO 27001 PDF is product-listed). Do not inherit every Trust Center logo. | B | Trust Center; ISO PDF |
| Contracting entity | Depends on account billing address (Singapore / Netherlands / Europe Ltd / US LLC / India / Malaysia) | B | Terms of Use |
| OSM fit | Strong IaaS analogue to EC2. China vs international partition is a residency/provider-entity stress, not a second Service. | — | — |

### Alibaba Cloud Object Storage Service

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical name | Object Storage Service (OSS) | A | https://www.alibabacloud.com/help/en/oss/user-guide/what-is-oss |
| Technological service | Object/blob storage (buckets, region endpoints) | — | — |
| Durability/availability claims | Vendor states 12 nines durability and 99.995% availability | B | same (vendor claim; not a customer SLO) |
| Location | Region-specific endpoints (e.g. Hangzhou, Frankfurt `eu-central-1`) | B/C | https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints |
| Mainland policy | From 20 Mar 2025, **new** OSS users: custom domain for data API on Chinese mainland buckets | B | same |
| OSM fit | Strong storage Service. Do not copy durability marketing into posture `rto`/`rpo`. | — | — |

### Cloudflare CDN / WAF

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical names | Cloudflare CDN; Cloudflare WAF (often sold together on the edge) | A | Trust Hub; EU Cloud CoC declared services |
| Technological service | Reverse-proxy content delivery and Layer-7 application firewall on Cloudflare’s network | — | — |
| Offerings | Plan tiers; all plans in SOC 2 scope per Cloudflare | B | SOC 2 FAQ |
| Provider | Cloudflare, Inc. | A | — |
| Certifications | ISO scope = global cloud platform; EU Cloud CoC lists **CDN** and **WAF** among declared services | B | ISO FAQ; CoC PDF |
| OSM fit | Network/security service. Estate also has generic “CDN” and “WAF / CDN / Cloudflare” rows — do not create both a generic CDN Service *and* a Cloudflare CDN Service without an offering relationship. | — | — |
| Type tension | Service sits under a `network-provider` ICT Provider; characteristics carry WAF vs CDN. | — | — |

### Cloudflare Zero Trust / Access

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical names | Cloudflare One (SASE platform); Cloudflare Access (ZTNA); “Cloudflare Zero Trust” in docs and CoC list | A | https://developers.cloudflare.com/cloudflare-one/ ; https://www.cloudflare.com/products/access/ |
| Technological service | Identity-aware access (ZTNA) and related SWG/CASB/DLP on the same network | — | — |
| Offerings | Access vs Gateway vs Tunnel vs full One suite; Free vs Paid | B | Cloudflare One docs |
| Subprocessors | Google LLC listed for **Cloudflare Zero Trust** (and Developer Platform, AI Gateway) | A | subprocessors page |
| OSM fit | Maps to estate “Zero Trust Network Access” better than to “VPN”. Distinct Service from CDN/WAF even though same provider and often same contract. | — | — |

### Salesforce Sales Cloud

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical name | Sales Cloud (listed under Salesforce Services SPARC) | A | https://www.salesforce.com/company/legal/trust-and-compliance-documentation/ |
| Technological service? | Multi-tenant CRM **application**. OSM excludes **applications / Application Services** and **business capabilities**. A charitable read is “hosted CRM application platform”; a strict read is **out of OSM core** (business CRM). | — | `MODEL.md` out of scope |
| Infrastructure | SPARC/I&S: many customers’ Sales Cloud features on **first-party** Salesforce infrastructure; Einstein features on **Einstein Platform**; Hyperforce/AWS possible | B | I&S PDF |
| Certifications | In SPARC Covered Services **unless** a SKU is on the exclusion list | B | SPARC PDF |
| OSM fit | Stress-test: product name ≠ technological service. If included, one Service with offerings (Sales Cloud editions, Hyperforce vs first-party). Do not model “opportunity management” as the Service. | — | — |

### Slack

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical name | Slack (Salesforce family; own SPARC/NLI) | A | Trust & Compliance page (Slack SPARC 2026-05-22, NLI 2026-07-24) |
| Ownership | Salesforce owns Slack; Slack LLC / Slack Technologies Limited remain DPA entities | A | Acquisition blog; DPA |
| Technological service? | Collaboration/messaging SaaS — same application-vs-service tension as Sales Cloud | — | — |
| Provider modelling | Same parent; **do not** create a second ICT Provider by default; **do** keep a separate Service | — | — |
| Certifications | Slack SPARC, not the Salesforce Services SPARC. Slack PRP is separate from Salesforce Group PRP. | B | DPA §13 ; Slack SPARC |
| OSM fit | Estate rows 57 Salesforce and 64 Slack. Two Services, one (or two) providers — see provider section. | — | — |

### ServiceNow ITSM

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical name | ServiceNow IT Service Management (incident, problem, change, request on the AI Platform) | A | https://www.servicenow.com/products/itsm.html |
| Technological service? | SaaS ITSM **application**. Closer to a technological service than CMDB (it *delivers* IT management workflows), but still an application product. Strict OSM: applications are out of scope. | — | `MODEL.md` |
| Hosting | Region selected at order; paired sites | B/C | Securing the ServiceNow AI Platform PDF |
| Certifications | Platform-level ISO/SOC; confirm ITSM is in the SoA (typically yes as part of the subscription service) | B | Trust / CORE |
| OSM fit | If kept, Service = “ITSM platform capability”, Offering = ITSM SKU/edition. Do not encode ITIL processes as Services. | — | — |

### ServiceNow CMDB — modelling clash

| Item | Notes | Class | URL |
|---|---|---|---|
| Vendor definition | “Single system of record for configuration item (CI) data”; docs: store CIs and relationships; populate via Discovery, ETL, import sets; tables extend `cmdb_ci` | A | https://www.servicenow.com/in/products/servicenow-platform/configuration-management-database.html ; https://www.servicenow.com/docs/r/servicenow-platform/configuration-management-database-cmdb/c_ITILConfigurationManagement.html |
| OSM exclusion | OSM **does not define** “CMDB configuration items or running-system inventory” | A | `MODEL.md` / `SPECIFICATION.md` Out of scope |
| Clash | The estate item *is* a CMDB product. Representing it as an OSM Service either (1) violates the out-of-scope rule, or (2) reduces it to “the SaaS application that *implements* a CMDB”, which is an **application**, also out of scope. | — | — |
| Legal schedule | “CMDB Amplified” exists as a ServiceNow legal schedule (effective 11 May 2023) — product add-on, not an OSM entity | A | https://www.servicenow.com/schedules.html |
| Investigation treatment | **Do not** invent an OSM Service whose payload is CI inventory. Optional: record ServiceNow as ICT Provider only; leave CMDB as a **decision-register** gap (product vs out-of-scope inventory). If a Service is forced for estate coverage, name it as the **CMDB SaaS application** and flag it non-conformant with OSM purpose. | — | — |
| DORA blogs | ServiceNow marketing uses CMDB/CSDM to *help customers* implement DORA registers. That does not make CMDB an OSM technological service or ServiceNow a CTPP. | B | Community GRC blog (non-normative) |

### SAP S/4HANA Cloud

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical name | SAP S/4HANA Cloud **Public Edition** (also Private Edition / RISE). Estate row says “SAP S/4HANA”. | A | https://www.sap.com/canada/products/erp/s4hana.html |
| Vendor definition | “Foundational **application** of SAP Cloud ERP”; finance, supply chain, HR, sales **business processes** | A | same |
| Product vs service vs application | **Product** (SKU). **Business application / ERP** (OSM excludes applications and business services). **Technological service** only if stretched to “hosted ERP application runtime” — that stretch is the stress-test, not a recommended encoding. | — | `MODEL.md` |
| Editions | Public Edition (standardized SaaS) vs Private Edition (managed private / RISE). Different ops and cert packs. On-prem S/4HANA is licensed software, not this cloud Service. | B | product page ; private-edition community FAQ |
| ISO 27001 | Named on Enterprise Management ISO 27001 certificate (Public Edition) | B | https://www.sap.com/documents/2025/06/98e011a4-0b7f-0010-bca6-c68f7e60039b.html |
| CSA / IRAP | 2025-H1 CSA for Public Edition; Australian deployment on Microsoft and Amazon noted | B | CSA page |
| Second service if needed | **SAP BTP** is a better OSM technological-service candidate (app dev, integration, data/AI platform) than SuccessFactors (HCM SaaS, same application problem as Workday). This note does not deeply research BTP beyond Trust Center hosting of BTP in SAP DCs. | B | https://www.sap.com/about/trust-center/data-center.html |
| OSM fit | Prefer **not** to pretend S/4HANA is a compute/platform Service. Record as ICT Provider SAP + decision: ERP applications out of scope. If estate coverage requires a row, mark semantic exception. | — | — |

### Workday HCM (brief)

| Item | Notes | Class | URL |
|---|---|---|---|
| Canonical name | Workday Human Capital Management | A | 10-K ; compliance page (HCM in ISO scope) |
| OSM fit | Same SaaS-application exclusion as Sales Cloud / SuccessFactors. Estate row 61. Type `software-vendor`. | — | — |
| Hosting | Workday + public cloud (AWS/Azure) or colocation; shared-responsibility page | B | https://security.workday.com/shared-responsibility |

---

## Stress-test observations

### 1. SaaS is missing from `type`

Salesforce, ServiceNow, SAP Cloud ERP, Workday, Slack, and much of Oracle Applications are SaaS. Forced values (`software-vendor` or `cloud-platform`) lose the delivery model. Cloudflare is not SaaS in the CRM sense and not IaaS; `network-provider` is a compromise.

### 2. Headquarters is one country code

Fails for Alibaba (Cayman parent / Hangzhou PRC operator / Singapore international HQ and default contractor). Weak for Oracle (DE corp / Austin HQ) and IBM (NY corp / Armonk HQ) — same country, different legal facts. SAP Walldorf is the clean case (`de` = registered office). OSM cannot store “designated DORA entity = Oracle Nederland B.V.” while `headquarters` is `us`.

### 3. Certification is a string list without scope

Every vendor in this batch publishes **service × region × edition** attestations. IBM’s ISO 27001 *infrastructure* list omits IKS while SOC 2 includes it. Salesforce SPARC ISO and SOC exclusion lists differ. SAP ISO 27001 Enterprise Management includes S/4HANA Cloud Public Edition, not “SAP”. Cloudflare ISO is platform-wide; SoA is NDA. OSM `certifications: ["iso-27001"]` would be an unsupported compliance claim.

### 4. DPA existence ≠ `gdpr_dpa_signed`

All seven vendors publish a DPA/DPE. The boolean field asks whether a **customer signed** it. Class C. Alibaba/Salesforce/ServiceNow/Cloudflare/Workday forms are public; Oracle/IBM/SAP also exist but are order-incorporated. Never set `true` from these notes.

### 5. DORA designation is entity-scoped and not an OSM field

Official ESA list (18 Nov 2025): Oracle **Nederland B.V.**, **IBM** (ESA spelling “International Business Machine Corporation”), **SAP SE**. Cloudflare explicitly not designated. Salesforce, Alibaba, ServiceNow, Workday, Slack are **not** on the official 19. OSM has only `dora_notification_clause` (boolean on the provider), which cannot store designated legal entity, lead overseer, or “mapping PDF exists”.

### 6. Subprocessors are lists behind portals

Oracle MOS 2121811.1, IBM DPA Exhibits, Alibaba account login, SAP for Me / Trust Center per product, ServiceNow CORE, Salesforce I&S (public PDF but infrastructure-conditional), Cloudflare (public). OSM `subcontractors: [string]` cannot carry purpose, location, or service scope. `subcontracting_allowed: conditional` is the only honest public value.

### 7. IBM / Red Hat are two legal persons

Red Hat survived the 2019 merger as a wholly owned subsidiary and still owns OpenShift trademarks. **Red Hat should be a separate ICT Provider** for self-managed OpenShift/RHEL. **IBM** is the ICT Provider for IKS and for OpenShift *on IBM Cloud*. OSM has no `parent_provider` / `affiliate_of` field.

### 8. Salesforce / Slack are one group, two products, leftover Slack entities

One parent is true. Separate SPARC, separate Slack LLC / Limited, separate PRP. OSM can do one Provider + two Services. Two Providers would need a parent link the schema lacks. Do not merge Slack into Sales Cloud.

### 9. ServiceNow CMDB vs OSM CMDB exclusion

Hard clash. Vendor CMDB *is* CI inventory. OSM refuses CMDB CIs and running-system inventory, and also refuses applications. Estate row 59 cannot be encoded without violating OSM purpose. Record in the decision register; do not “fix” it by pretending CMDB is a compute Service.

### 10. S/4HANA is a business application

SAP’s own page calls Public Edition an ERP **application** for business processes. OSM excludes applications and business services. Treating S/4HANA Cloud as an OSM Service confuses product, technological service, and business capability. BTP is the less-wrong second SAP Service if the estate needs two; SuccessFactors repeats the HCM/SaaS problem (Workday).

### 11. Multicloud and hyperscaler subprocessors

ADB on AWS/Azure/Google; S/4HANA CSA on Microsoft/Amazon in Australia; Workday on AWS/Azure; Salesforce Hyperforce; ServiceNow hyperscaler/SPP; Cloudflare using Google/Oracle/AWS as subprocessors. OSM `subcontractors` strings cannot express “ICT Provider A runs on ICT Provider B in region R”. Concentration and DORA register-of-information grain are lost.

### 12. Customer-dependent fields must stay empty

Do not populate for any provider in this file: `contract_ref`, `contract_start`, `contract_end`, `notice_period_days`, `audit_rights`, `last_risk_assessment`, `risk_level`, `exit_strategy_*`, `concentration_risk`, Service Posture criticality, RTO/RPO. Substitutability, if required by the schema later, is a judgement call — not a public certificate fact.

### 13. Generic estate rows vs vendor services

The 100-item list has both “Cloudflare” (provider) and “WAF / CDN / Cloudflare”, plus generic CDN, DNS, Zero Trust, VPN. Also “Oracle Cloud Infrastructure” and “Oracle Database”. OSM should use **one Service definition** with vendor Offerings, not duplicate Services per marketing name.

### 14. What mapped cleanly

- OCI Compute, Alibaba ECS/OSS, IKS as technological cloud services
- Public DPA **existence** (not signature)
- Country HQ for US/DE vendors when legal and operational countries match
- ESA CTPP names as provenance facts (not OSM enums)
- Cloudflare public subprocessor list and public DPA version/date

### 15. Decision-register candidates (do not implement)

- Add `saas` (or delivery-model) distinct from `type`
- Split legal entity vs operational HQ vs designated regulatory entity
- Certification objects with scope, standard version, and evidence URL
- `gdpr_dpa_available` vs `gdpr_dpa_signed`
- Affiliate/parent provider
- Explicit “out of OSM: business application / CMDB product” treatment for S/4HANA, Sales Cloud, Slack, ITSM, CMDB, Workday HCM
)
