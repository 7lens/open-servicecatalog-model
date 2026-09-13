# SaaS / Security / Data — Reference-Estate Research Notes

**Investigation:** 7lens OSM reference-estate, Phase 2–3 provider/service research  
**Research date:** 2026-09-13  
**Scope:** Atlassian, Okta, CrowdStrike, Palo Alto Networks, Zscaler, Datadog, Dynatrace, Snowflake, Databricks, plus short notes on GitHub (Microsoft), GitLab, HashiCorp Terraform (IBM), Splunk (Cisco), Zoom, CyberArk, SentinelOne, New Relic, Grafana Labs  
**Constraint:** Official trust / compliance / security / legal pages and primary SEC / corporate filings. No OSM schema or example edits.

## How to read this file

Evidence classes follow the investigation methodology:

| Class | Meaning |
|---|---|
| **A** | Publicly verified on an authoritative official page or filing |
| **B** | Publicly documented but conditional (product, region, edition, plan, or cell) |
| **C** | Customer-dependent; cannot be asserted as a universal technology fact |
| **D** | Not publicly determinable from official sources reviewed on 2026-09-13 |

Facts tables use: **fact | OSM field | value | scope | class | URL**.

OSM fields referenced (current frozen model; not proposals):

| OSM object | Fields used in this note |
|---|---|
| ICT Provider | `name`, `type`, `headquarters`, `data_processing_locations`, `substitutability`, `certifications`, `gdpr_dpa_signed`, `dora_notification_clause`, `subcontracting_allowed`, `subcontractors`, `contract_ref`, `audit_rights`, `risk_level` |
| Service / Offering | `name`, `description`, `providers[]`, `characteristics[]` |
| Technology Stack mappings | `mappings.dora.pillar`, `mappings.ai_act.contains_ai_systems` |
| Service / Offering posture | `operational_criticality`, `rto`, `rpo`, `data_classification` |

**Intentionally unset on every record in this investigation:** customer `contract_ref` / dates / notice period, `gdpr_dpa_signed`, `dora_notification_clause`, `risk_level`, `operational_criticality`, `rto`, `rpo`, and any invented SLA. Vendors publish *template* DPAs and *support* materials for DORA; that is not a signed customer DPA or a DORA notification clause.

`headquarters` in OSM is a single ISO 3166-1 alpha-2 code. Several vendors have dual principal offices, engineering HQs, or “no headquarters” statements. That mismatch is recorded, not forced.

`type` in OSM is a closed enum: `cloud-infrastructure` | `cloud-platform` | `managed-service` | `software-vendor` | `network-provider` | `data-center`. There is no `saas` value. Every vendor below stresses that enum.

---

## Cross-cutting stress-test observations

### 1. SaaS vs software-vendor vs cloud-platform

Almost every vendor in this file sells a multi-tenant cloud product that enterprises treat as SaaS, plus a self-managed / Data Center / appliance / CLI edition. OSM `type` cannot say “SaaS.” Closest fits:

| Pattern | Candidate OSM `type` | Why it is awkward |
|---|---|---|
| Multi-tenant product cloud (Jira Cloud, Okta WIC, Falcon, ZIA, Datadog, Snowflake) | `cloud-platform` | Matches the GitHub example, but these are not PaaS in the hyperscaler sense |
| Self-managed software (Jira Data Center, PAN-OS NGFW, Terraform CLI, Splunk Enterprise) | `software-vendor` | Same legal entity as the cloud product |
| Cloud-delivered inspection of customer traffic (Zscaler, Prisma Access) | `network-provider` *or* `cloud-platform` | They operate a global security fabric, not a telco |
| Human-operated MDR (Falcon Complete, some Zscaler MDR) | `managed-service` | Same platform, different commercial offering |
| Control-plane SaaS + customer data plane (Databricks) | `cloud-platform` *and* implicit hyperscaler ICT Providers | Two provider layers |

**Observation:** one ICT Provider record cannot carry a single honest `type` for a multi-edition vendor. Edition belongs on Service / Offering `characteristics` (for example `deployment_model`: `cloud` | `data-center` | `self-managed` | `managed`). `type` on the provider is then a coarse org-class, not a service-class.

### 2. One ICT Provider vs many, for multi-product vendors

Public legal identity is usually **one** Delaware / Israeli / Australian parent. Product clouds, acquired platforms, and managed services are **offerings**, not separate ICT Providers — except where a later acquisition changes the contracting party (IBM←HashiCorp, Cisco←Splunk, Microsoft←GitHub).

Recommended default for this estate: **one ICT Provider per legal seller**, multiple Services, multiple Offerings. Split a second ICT Provider only when the customer actually contracts a different legal entity (Auth0 still contracts through Okta, Inc.; GitHub, Inc. remains a distinct Microsoft subsidiary and is already modelled as its own ICT Provider in OSM examples).

### 3. Certifications have scope; OSM `certifications[]` does not

Every Trust Center reviewed lists ISO 27001 / SOC 2 at *company or platform* level, then qualifies products, regions, and government clouds. OSM stores a string array on the ICT Provider. That encourages the false inference “ISO 27001 therefore every service / region / edition.” Scope must live in provenance or a characteristic, not be implied by the badge.

### 4. DORA relevance (security and observability ICT)

DORA (Regulation (EU) 2022/2554) applies to in-scope **financial entities** and their **ICT third-party service providers**. Identity, endpoint, SASE, SIEM/observability, and data-platform vendors in this file are typical ICT third parties for ICT risk management, incident management, resilience testing, and third-party risk — **if** a financial entity uses them for a critical or important function. That use, criticality, RTO/RPO, and register-of-information fields are **C**. Vendor “DORA factsheets” are support materials, not a `dora_notification_clause` and not a claim that the vendor is a designated critical ICT third-party provider.

OSM already maps DORA to `providers[]`, posture `operational_criticality` / `rto` / `rpo` / `resilience_tested`, and ICT Provider contract flags. Do not copy vendor marketing into those fields.

### 5. AI Act: system vs platform hosting customer models

Do **not** classify customer risk. Public facts only:

| Pattern | Examples | OSM-safe statement |
|---|---|---|
| Vendor-operated AI features inside a SaaS product | Atlassian Rovo, Snowflake Cortex, CrowdStrike Charlotte AI, Datadog Bits/AI features, Dynatrace Davis, GitHub Copilot, Zoom AI Companion | `mappings.ai_act.contains_ai_systems` *may* be true for that Service if the vendor’s offering is an AI system. Risk class is **C/D** |
| Platform that hosts / serves **customer** models | Databricks Mosaic AI, Snowflake Snowpark Container Services bring-your-own models | Platform ≠ the customer’s AI system. Do not set a customer `ai_act_risk_class` |
| Optional / admin-gated AI | Cortex (RBAC / allow-list), Databricks Partner-powered AI (off under compliance profile), Atlassian AI activation | Applicability is an Offering characteristic, not a provider universal |

Vendor “EU AI Pact” / “ISO 42001” membership is governance evidence about the **vendor**, not a risk classification of any customer use.

### 6. Data-processing locations and region choice

OSM `data_processing_locations` is a coarse string array. Reality is: default global routing, optional pin/cell/site, support access outside the pin, subprocessors that ignore the pin, and CDN/inspection PoPs that follow the user. Record the **choice mechanism** as a characteristic (`data_residency_option`) and leave the selected region **C**.

### 7. Subprocessors

All major vendors publish a list and claim general authorization + notice/objection in a DPA. OSM `subcontracting_allowed` can be `conditional` at provider level (B). The live list is too large and too product-specific for `subcontractors[]` as a complete inventory. Put the official list URL in provenance; do not freeze a partial list as if exhaustive.

### 8. Product company vs network-provider vs software-vendor vs managed-service

CrowdStrike, Zscaler, and Palo Alto Networks all sell **software**, operate **global clouds**, and offer **managed** add-ons. They are not public electronic communications network operators. Prefer `cloud-platform` (or `software-vendor` for appliance-led Strata) plus an Offering characteristic for MDR/SASE, rather than `network-provider` unless the estate is literally modelling connectivity.

---

## 1. Atlassian

**Legal identity:** Atlassian Corporation (Delaware). Principal offices: Level 6, 341 George St, Sydney NSW 2000, Australia **and** 350 Bush Street, Floor 13, San Francisco, CA 94104. Founded Sydney 2002. Cloud is the primary commercial offering; Data Center is self-managed on customer infrastructure.

**Recommended ICT Provider:** one record `atlassian`. `headquarters` cannot be both `au` and `us` — dual-HQ stress. Investor FAQ treats both as principal offices.

**Candidate `type`:** `cloud-platform` for Cloud-first modelling; Data Center editions are `software-vendor` semantics on the **same** legal entity.

### Provider facts

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal name | `name` | Atlassian Corporation | Parent; business via subsidiaries | A | https://investors.atlassian.com/resources/investor-faqs/default.aspx |
| Dual principal offices | `headquarters` | `au` **or** `us` — OSM allows one code | Sydney + San Francisco | A | https://investors.atlassian.com/resources/investor-faqs/default.aspx |
| Cloud hosting partner | `subcontractors` / characteristic | AWS is primary outsourced data-center partner; Atlassian does not operate its own DCs | Cloud products | A | https://www.atlassian.com/trust/compliance/compliance-faq |
| Subprocessing | `subcontracting_allowed` | `conditional` (general authorization + 30-day notice + objection/terminate) | Cloud Products under DPA | A | https://www.atlassian.com/legal/data-processing-addendum |
| Pre-signed DPA exists | `gdpr_dpa_signed` | **unset** (template published; signature is C) | Cloud + related Support | A (template) / C (signed) | https://www.atlassian.com/legal/data-processing-addendum |
| DPA effective date | provenance | 2026-08-17 | Published DPA | A | https://www.atlassian.com/legal/data-processing-addendum |
| Processor role | — | Atlassian is Processor (or Sub-processor) of Customer Data | DPA | A | https://www.atlassian.com/legal/data-processing-addendum |
| Security incident notice | characteristic / contract (C) | Without undue delay; where feasible ≤72 hours | DPA | A | https://www.atlassian.com/legal/data-processing-addendum |
| Audit rights | `audit_rights` | Summary reports under NDA; on-site only if reports insufficient or required by law; ≤1/12 months | DPA | B | https://www.atlassian.com/legal/data-processing-addendum |
| ISO 27001:2022 | `certifications` | ISO/IEC 27001:2022 for Atlassian Trust Management System (ATMS) supporting **cloud offerings**; product list varies | Cloud ISMS; **not** Data Center customer deployments | B | https://www.atlassian.com/trust/compliance/resources/iso27001 |
| ISO 27018 | `certifications` | Additional PII-in-public-cloud controls on ATMS SoA | Cloud offerings | B | https://www.atlassian.com/trust/compliance/resources/iso27001 |
| SOC 2 Type 2 | `certifications` | Annual Type 2, period 1 Oct–30 Sep; product-specific reports (Jira, Confluence, JSM) | Named Cloud products in each report | B | https://www.atlassian.com/trust/compliance/compliance-faq ; https://customertrust.atlassian.com/ |
| HIPAA | — | Offered for some Cloud solutions; not universal | Conditional Cloud | B | https://www.atlassian.com/trust/compliance/compliance-faq |
| Customer contract / RTO / criticality | `contract_*`, posture | unset | Always C | C | — |
| Substitutability | `substitutability` | unset | Collaboration suites exist; lock-in is C | C | — |

### Service notes — Jira and Confluence

Treat **Jira** and **Confluence** as two Services. Cloud vs Data Center are **Offerings** (or a `deployment_model` characteristic), not two ICT Providers.

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Jira Cloud / Confluence Cloud | Service `name` | Jira Cloud; Confluence Cloud | Atlassian Cloud Platform | A | https://www.atlassian.com/trust/compliance |
| Data Center edition | Offering | Self-managed; customer deploys and hosts on own infrastructure | Jira, Confluence, JSM, Bitbucket, Crowd, Bamboo | A | Atlassian FY25 10-K (principal offices 350 Bush St): https://content.edgar-online.com/ExternalLink/EDGAR/0001650372-25-000036.html |
| Cloud vs DC capability gap | Offering description | DC products “do not have the enhanced capabilities of AI, Rovo, advanced analytics, and automation” of Cloud | Data Center | A | same 10-K |
| Isolated / Gov Cloud | Offering | Atlassian Government Cloud (FedRAMP Moderate EAP); Isolated Cloud announced FY25 (single-tenant) | US gov / high-isolation | B | same 10-K |
| In-scope Cloud products for data residency | characteristic `data_residency_option` | Jira, Confluence, Jira Service Management, Jira Product Discovery; Loom at provisioning | Standard / Premium / Enterprise Cloud | B | https://www.atlassian.com/software/data-residency ; https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/ |
| Pin locations | `data_processing_locations` (selected value is C) | Default **Global** (all AWS regions). Pin: Australia, Canada, EU (Frankfurt+Dublin), Germany (Frankfurt), India (Mumbai), Japan (Tokyo), Singapore, South Korea (Seoul), Switzerland (Zurich), UK (London), USA (N. Virginia + Oregon) | In-scope app data only; not all metadata / marketplace apps | B | https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/ |
| AWS as Cloud host | `subcontractors` | Amazon Web Services, Inc. — Jira Cloud, Confluence Cloud, Rovo, others | Locations vary; residency pin changes in-scope host region | A | https://www.atlassian.com/legal/sub-processors |
| Other Cloud subprocessors (illustrative, not exhaustive) | provenance | Cloudflare (CDN / MCP, processed at nearest PoP); OpenAI listed as LLM sub-processor for Rovo; Databricks, Twilio, Mailgun, etc. | Product-specific | A | https://www.atlassian.com/legal/sub-processors ; https://www.atlassian.com/trust/ai/transparency |
| Data Center processing location | `data_processing_locations` | Customer-chosen infrastructure | Data Center | A | 10-K Data Center description |
| Cloud compliance badges do not cover DC | `certifications` scope | ISO/SOC evidence is for Cloud ATMS / named Cloud reports | Data Center customer ISMS is C | B | https://www.atlassian.com/trust/compliance/compliance-faq |

**AI Act (do not classify customer risk).** Rovo and Atlassian Intelligence are vendor-operated AI features on Cloud. Atlassian joined the EU AI Pact (Sept 2024), publishes transparency notes, and states inputs/outputs are not used to train third-party LLMs; OpenAI and Google are the named third-party LLM providers; third-party LLMs operate under zero-data-retention. Shared responsibility: model providers, Atlassian as AI-system provider, customer as deployer. Data Center lacks Rovo.  
Sources: https://www.atlassian.com/trust/compliance/resources/eu-ai-act ; https://www.atlassian.com/platform/ai-trust ; https://www.atlassian.com/trust/ai/transparency

**DORA:** Collaboration / ticketing platforms are ICT services if a financial entity relies on them. Atlassian Cloud SLA, residency, DPA, and subprocessors are relevant evidence; criticality and register fields are C. No public `dora_notification_clause`.

**Stress:** Cloud vs Data Center is the cleanest Service→Offering test in this file. One Service `collaboration.jira` with offerings `…cloud` and `…data-center` (and maybe `…gov-cloud`) matches OSM. Copying Cloud ISO 27001 onto a Data Center offering is a model failure.

---

## 2. Okta

**Legal identity:** Okta, Inc. (Delaware). Principal executive offices: 100 First Street, Suite 600, San Francisco, CA 94105. Auth0 acquired 2021-05-03; Auth0 operated as a business unit; FY2025 10-K still distinguishes **Okta Platform** (workforce) and **Auth0 Platform** (developer / customer identity).

**Recommended ICT Provider:** one record `okta`. Auth0 is a **Service or Offering**, not a second ICT Provider, unless a customer still has a legacy Auth0 contract that names a different entity (D).

**Candidate `type`:** `cloud-platform` (identity-as-a-service). Not `network-provider`.

### Provider facts

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal name / HQ | `name`, `headquarters` | Okta, Inc.; `us` | Corporate | A | https://investor.okta.com/investor-services/investor-faqs/default.aspx ; https://www.okta.com/contact/ |
| Two platforms | Service split | Okta Platform (Workforce Identity); Auth0 Platform (customer/citizen identity) | Company | A | https://www.sec.gov/Archives/edgar/data/1660134/000166013425000049/okta-20250131.htm |
| Auth0 acquisition | provenance | Completed 2021-05-03; Auth0 as independent BU at close | Historical | A | https://www.okta.com/blog/company-and-culture/its-official-okta-joins-forces-with-auth0/ |
| Separate security docs | Offering / provenance | Distinct WIC vs CIC (formerly Auth0) Security & Privacy Documentation | Product clouds | A | https://www.okta.com/sites/default/files/2023-04/Workforce-Identity-Cloud-Security-Privacy.pdf ; https://www.okta.com/sites/default/files/2023-04/CIC-Security-Privacy-Doc.pdf |
| Trust Center badges | `certifications` | ISO/IEC 27001:2022, 27017:2015, 27018:2019; SOC 1/2/3; CSA STAR L1/L2; FedRAMP High/Moderate; GDPR; DPF; C5; DORA (listed as a framework tile); PCI DSS v4; TISAX; IRAP; ENS | **Confirm product/cell on each report** — Trust Center lists programs, not a single SoA | B | https://security.okta.com/ |
| WIC covered services (2023 doc) | Service description | SSO, Adaptive MFA, Mobility Management, Lifecycle Management, Universal Directory, API Access Management, Directory Integration, Inbound Federation, Advanced Server Access, Social Authentication | WIC doc; may be stale vs current SKUs | B | WIC Security & Privacy PDF above |
| CIC covered services | Service description | Services branded Customer Identity Cloud (previously Auth0) | Not Pro Services / non-Okta apps / free trials | B | CIC Security & Privacy PDF |
| Pre-signed DPA | `gdpr_dpa_signed` | Template at okta.com (2025-01 file reviewed); signed status C | Subscriptions under MSA | A / C | https://www.okta.com/sites/default/files/2025-01/DATA_PROCESSING_ADDENDUM.pdf |
| Data residency cells | characteristic | Cells in US, EMEA, Japan, Australia, Canada, India (primary + failover). Customer selects cell. Processing may still occur via subprocessors outside the cell | Workforce / Customer Identity hosting | B | https://www.okta.com/okta-data-residency/ |
| Subprocessors | `subcontracting_allowed` | `conditional`; separate tables for Workforce/Customer Identity vs CIC vs Access Governance | Product- and cell-specific locations | A | https://www.okta.com/legal/trustandcompliance/subprocessors/ ; https://www.okta.com/content/dam/okta---digital/en_us/legal/okta-sub-processor-information-2026-03.pdf |
| WIC infrastructure examples | `subcontractors` (illustrative) | AWS (cell-dependent: US / Canada / India / EU DE+IE / AU / JP); support access from Romania; Datadog analytics (EU cell DE, other cells often USA) | WIC | B | Okta sub-processor PDF 2026-03 |
| CIC infrastructure examples | `subcontractors` (illustrative) | AWS regions selectable at CIC deploy (public + private cloud list); MongoDB/Aiven follow customer region; SendGrid/Twilio USA | CIC / Auth0 | B | same PDF |
| DORA materials | `dora_notification_clause` | **unset**. Okta publishes a DORA factsheet and maps controls; compliance remains the financial entity’s | Support material | B | https://sec.okta.com/articles/2025/05/a-guide-to-dora-compliance-with-okta/ |

### Service notes — Workforce Identity Cloud; Auth0

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Service 1 | Service `name` | Okta Workforce Identity Cloud (Okta Platform) | Workforce IAM | A | 10-K; WIC security doc |
| Service 2 | Service `name` | Auth0 / Customer Identity Cloud | External identity; developer platform | A | 10-K; https://auth0.com/docs/secure/data-privacy-and-compliance |
| Auth0 ISO/SOC | `certifications` | Annual ISO 27001/27017/27018; SOC 2 Type 2 covering all five TSC | Auth0 platform; reports via Auth0 Support Center | B | https://auth0.com/docs/secure/data-privacy-and-compliance |
| Same legal seller | `providers[]` | `okta` on both Services | Unless a legacy Auth0 paper contract says otherwise (D) | A | Acquisition posts; 10-K |
| Region choice | Offering characteristic | Okta cell SKU vs Auth0 public/private region pick | Different control planes | B | Data residency page; CIC sub-processor table |

**AI Act:** Okta’s Trust Center lists AI-related programs only at a high level. Workforce MFA/risk scoring may involve automated decisioning; that does **not** justify setting `ai_act_risk_class`. Leave AI Act fields unset unless a specific Okta AI product is in the estate (D).

**DORA:** Identity is a typical ICT third-party for access management. Relevant, not automatically “critical.”

**Stress:** Auth0 is the acquisition-as-offering test. Two Services, one Provider. Separate compliance packs mean certifications cannot be copied from WIC to Auth0 without the CIC/Auth0 report.

---

## 3. CrowdStrike

**Legal identity:** CrowdStrike Holdings, Inc. (Delaware). Principal executive office: 206 E. 9th Street, Suite 1400, Austin, TX 78701. Cloud-native Falcon platform (endpoint, identity, cloud, SIEM, AI). Falcon Complete is 24/7 MDR (managed service) on the same platform.

**Recommended ICT Provider:** one record `crowdstrike`.

**Candidate `type`:** `cloud-platform` for Falcon SaaS; Falcon Complete Offering may additionally feel like `managed-service`. Not `network-provider`. Appliance residual is small.

### Provider facts

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal name / HQ | `name`, `headquarters` | CrowdStrike Holdings, Inc.; `us` | Corporate | A | https://ir.crowdstrike.com/shareholder-services/investor-faqs |
| Platform | Service family | CrowdStrike Falcon | Endpoint, identity, cloud, data | A | https://www.crowdstrike.com/en-us/why-crowdstrike/crowdstrike-compliance-certification/ |
| ISO 27001:2022 | `certifications` | Independently certified; 2024 press: scope extended to Falcon Next-Gen SIEM, Charlotte AI, Falcon for IT | Named modules; Trust Center holds current cert | B | https://www.crowdstrike.com/en-us/why-crowdstrike/crowdstrike-compliance-certification/ ; https://www.crowdstrike.com/en-us/press-releases/crowdstrike-achieves-new-iso-27001-certification/ |
| ISO 27017:2015 | `certifications` | Included with updated ISMS (Trust Center announcement) | Falcon Platform ISMS | B | https://trust.crowdstrike.com/ |
| ISO 22301:2019 | `certifications` | BCMS certification announced on Trust Center | Corporate BCMS | B | https://trust.crowdstrike.com/ |
| ISO/IEC 42001:2023 | `certifications` | AI management system certification | Vendor AI governance, not customer AI risk class | B | https://www.crowdstrike.com/en-us/why-crowdstrike/crowdstrike-compliance-certification/ |
| SOC 2 | `certifications` | Separate Type II reports: Corporate Operations; Falcon Platform; Type I Forensic Lab | **Do not merge** into one badge | B | https://trust.crowdstrike.com/ |
| Other programs | `certifications` | CSA STAR L2, FedRAMP High, DoD IL5, PCI DSS v4 (AOC + requirement 5 mapping), C5, ENS High (EDR), Cyber Essentials, TISAX, IRAP, DPF/PRP/CBPR | Product/authorization-specific | B | Compliance page + Trust Center |
| GDPR / DPA | `gdpr_dpa_signed` | Global DPA published; signed status C | Offerings under DPA | A / C | https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2024/07/crowdstrike-global-data-protection-agreement.pdf |
| Hosting region choice | characteristic | Customer designates cloud-hosting region (DPA text: EU or US) at order; international processing for support still possible | Falcon | B | same DPA |
| Regional clouds | `data_processing_locations` | Additional in-country regional clouds announced 2026-01-20 for Saudi Arabia, India, UAE (planned/expanding) | Data sovereignty initiative | B | https://www.crowdstrike.com/en-us/press-releases/crowdstrike-announces-new-regional-clouds-to-expand-secure-data-sovereignty/ |
| Subprocessors | `subcontracting_allowed` | `conditional`; live list behind Falcon login; email subscription page public | Not fully enumerable from public web | B | https://www.crowdstrike.com/en-us/subprocessor-notification/ ; DPA Exhibit E |
| DORA tile | `dora_notification_clause` | Trust Center lists “DORA” among frameworks; no public clause text reviewed | unset | D / B | https://trust.crowdstrike.com/ |
| Sales restriction | — | Does not sell Falcon to companies located in Russia or China | Corporate policy | A | Investor FAQs |

### Service notes — Falcon endpoint; Falcon Identity

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Service 1 | Service `name` | CrowdStrike Falcon endpoint protection / EDR | Lightweight sensor + Falcon cloud | A | Compliance page; Falcon Complete MDR page |
| Service 2 | Service `name` | CrowdStrike Falcon Identity Protection | ITDR for AD / Entra / Okta / AWS IAM Identity Center | A | https://www.crowdstrike.com/en-us/blog/announcing-protection-aws-iam-identity-center/ |
| Falcon Complete | Offering | 24/7 MDR: detect, investigate, contain, remediate | Optional managed overlay | A | https://www.crowdstrike.com/en-us/services/falcon-complete-mdr/ |
| Falcon Complete Identity | Offering | MDR team operates Identity Threat Protection | Managed identity | A | https://assets.crowdstrike.com/is/content/crowdstrikeinc/crowdstrike-falcon-complete-identity-threat-protection-data-sheetpdf |
| Charlotte AI | related offering / characteristic | In ISO 27001 extension list (2024) | Vendor AI feature | B | ISO 27001 press release |
| Customer compliance mappings | — | Coalfire letters map Falcon to PCI, HIPAA, NIST 800-53, FFIEC, CMMC — **customer** program support, not CrowdStrike “being HIPAA certified” as a CE | Support evidence | B | Compliance page disclaimer |

**Type tension:** Falcon sensor is software; Falcon cloud is SaaS; Falcon Complete is managed service. One `type` cannot express all three. Put `delivery_mode` = `saas` | `mdr` on the Offering.

**AI Act:** Charlotte AI is a vendor AI system inside a security product. ISO 42001 is vendor AMS evidence. Do not set customer risk class. CrowdStrike explicitly: products “are not compliance solutions.”

**DORA:** Endpoint and identity telemetry / MDR are core ICT security services for financial entities. Incident-notification timelines in a customer contract are C.

---

## 4. Palo Alto Networks

**Legal identity:** Palo Alto Networks (corporate HQ 3000 Tannery Way, Santa Clara, CA 95054). Portfolio spans Strata (NGFW / PAN-OS), Prisma (Access SASE, Cloud CNAPP), Cortex (XDR/XSOAR), Unit 42 services.

**Recommended ICT Provider:** one record `palo-alto-networks`.

**Two catalog-relevant technological services (picked):** **Prisma Access** (cloud-delivered SASE / FWaaS) and **Prisma Cloud** (cloud-native security platform). Strata NGFW is the appliance/VM software line — important, but it is closer to `software-vendor` + customer-operated network function than to a hosted technological service. Cloud NGFW (AWS Marketplace, PAN-managed) is a third pattern if needed later.

**Candidate `type`:** `cloud-platform` for Prisma Access / Prisma Cloud; `software-vendor` if the estate’s only PAN item is PA-Series hardware. **Not** a telco `network-provider`, even though Prisma Access carries user traffic.

### Provider facts

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| HQ | `headquarters` | `us` (Santa Clara) | Corporate | A | https://www.paloaltonetworks.com/about-us/locations |
| Trust Center | provenance | Conveyor portal; “41 Compliance Certifications and Frameworks” | Company | A | https://trust.paloaltonetworks.com/ |
| ISO 27000 series | `certifications` | ISO 27001, 27017, 27018, 27032, 27701 described; certificates downloadable | Confirm product SoA on each PDF | B | https://www.paloaltonetworks.com/legal-notices/trust-center/iso-27000-series |
| Historical ISO scope expansion (2020) | scope warning | Blog added Cortex Data Lake/XDR/XSOAR, DNS Security, Enterprise DLP, Prisma Access (+ Cloud Management), Prisma Cloud, Prisma SaaS, WildFire | **2020 list — verify current cert** | B | https://www.paloaltonetworks.com/blog/2020/09/policy-iso-27001-certifications/ |
| Other programs | `certifications` | SOC 2+, Germany C5, PCI DSS, FedRAMP, StateRAMP, CSA STAR, IRAP, ISMAP, TISAX, ENS High, Common Criteria, FIPS 140, Cyber Essentials Plus, NCSC CIR (Unit 42 Enhanced) | Framework pages; product mapping in Trust Center docs | B | https://www.paloaltonetworks.com/legal-notices/trust-center/certifications |
| GDPR page | — | Dedicated GDPR legal-notices page referenced from product privacy datasheets | Company | A | https://www.paloaltonetworks.com/legal-notices/gdpr (linked from Prisma Access privacy datasheet) |

### Service notes — Prisma Access; Prisma Cloud

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Prisma Access | Service `name` | Prisma Access — cloud-delivered SASE; inspects internet, SaaS, private-app traffic for mobile users and remote networks | Hosted by PAN on hyperscaler fabric | A | https://www.paloaltonetworks.com/sase/access ; https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview |
| Prisma Access infrastructure | `subcontractors` / locations | AWS, GCP, and OCI provide physical/environmental controls; those CSP controls excluded from Prisma Access privacy datasheet scope | Prisma Access | A | Prisma Access Privacy Datasheet: https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=%2Fcontent%2Fpan%2Fen_US%2Fresources%2Fdatasheets%2Fprivacy-prisma-access |
| Prisma Access attestations | `certifications` | Datasheet: SOC 2 Type II Plus and ISO 27001 **for Prisma Access** | Prisma Access operations | B | same datasheet; https://www.paloaltonetworks.com/sase/access (FAQ: SOC2 certified) |
| Logs | characteristic | Prisma Access logs stored in Strata Logging Service | Dependent service | A | Prisma Access overview docs |
| Prisma Cloud | Service `name` | Prisma Cloud — CNAPP: visibility, threat prevention, compliance, data protection across multi-cloud | Distinct from Prisma Access | A | https://www.paloaltonetworks.com/prisma/ |
| Strata NGFW (not selected as primary pair) | optional Service | PA-Series / VM-Series / CN-Series / Cloud NGFW; Strata Cloud Manager unifies NGFW + Prisma Access policy | Hardware/VM vs FWaaS | A | https://www.paloaltonetworks.com/network-security/next-generation-firewall-hardware ; https://docs.paloaltonetworks.com/strata-cloud-manager/getting-started/overview |
| Precision AI | characteristic | Marketing name for AI in Prisma Access | Vendor AI features | B | Prisma Access product page |

**Type tension:** Prisma Access *is* a security network the customer does not build. OSM `network-provider` would lump PAN with a WAN/Internet carrier. Prefer `cloud-platform` + Offering characteristic `service_pattern` = `sase` | `cnapp` | `ngfw`.

**DORA:** Network security and CNAPP are ICT third-party services. Unit 42 is a *cyber incident response* service (NCSC CIR Enhanced) — closer to `managed-service` if catalogued.

**AI Act:** Precision AI / Cortex AI features are vendor systems. Prisma Cloud also governs *customer* cloud AI workloads — that is a platform hosting customer systems. Do not collapse the two.

**Data locations:** Prisma Access processing follows PAN PoPs / SPNs globally; log storage is a separate residency question (Strata Logging Service region — C). Hyperscaler region ≠ PAN legal HQ.

---

## 5. Zscaler

**Legal identity:** Zscaler, Inc. Worldwide HQ: 120 Holger Way, San Jose, CA 95134. Multi-tenant Security-as-a-Service cloud; 150+ data centers (co-location; Zscaler states DCs are **not** subprocessors).

**Recommended ICT Provider:** one record `zscaler`.

**Candidate `type`:** strongest enum fight in this file. Traffic inspection + private access looks like `network-provider`; the company is a security SaaS / software vendor; ISO scope says “Security as a Service platform.” Prefer `cloud-platform` with characteristic `service_pattern` = `sse` / `zta`. Use `network-provider` only if the estate models Zscaler as the access path itself.

### Provider facts

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| HQ | `name`, `headquarters` | Zscaler, Inc.; `us` | Corporate | A | https://www.zscaler.com/company/contact ; DPA amendment address |
| ISO/IEC 27001:2022 + 27701 + 27017 + 27018 | `certifications` | Schellman cert: ISMS for **Zscaler global cloud** in EMEA, NA, LATAM, APAC for the Security-as-a-Service platform, including ops employees; SoA v8.1 dated 2025-02-04 | Global cloud platform — not a customer’s own use of ZIA | A | https://www.zscaler.com/resources/legal/iso-certificate-of-registration.pdf |
| Other programs | `certifications` | SOC 2 Type 2, SOC 3, ISO 22301, CSA STAR L2, C5, Cyber Essentials Plus, HITRUST, PCI DSS, IRAP, ISMAP, ENS, MTCS L3, DPF, CMMC L2 (2026 cert announced on Compliance Center) | Confirm product on each artifact | B | https://compliance.zscaler.com/ |
| DPA | `gdpr_dpa_signed` | DPA incorporated in EUSA; amendments for SCCs / UK Addendum | Template / C for signed | A / C | https://www.zscaler.com/privacy-compliance/dpa |
| Processor role | — | Zscaler is a processor; DPA = customer instructions | Company | A | https://www.zscaler.com/privacy-compliance/faq |
| Inspection model | characteristic | Inspection in memory; limited personal data; transaction logs ~6 months | ZIA/ZPA | B | https://www.zscaler.com/resources/legal/zscaler-cover-letter-to-dpa.pdf |
| Log residency option | characteristic | Customer may store logs exclusively in **EEA+Switzerland (ZIA)** or **EEA (ZPA)** | Optional at deployment | B | DPA cover letter; SCC amendment PDF |
| User-proximate processing | `data_processing_locations` | Traffic processed in nearest of 150+ DCs (EU user in US → US DC). DCs are colo, Zscaler-controlled, **not** subprocessors | Default path | A | https://www.zscaler.com/privacy-compliance/faq ; https://trust.zscaler.com/data-center-map |
| Subprocessors | `subcontracting_allowed` | `conditional`; AWS/Azure/GCP host **certain features** (not the whole inspection fabric); affiliates for support | Feature-specific; hosted globally | A | https://www.zscaler.com/privacy-compliance/subprocessors |
| TIA / SCCs | — | TIA white paper; SCCs in DPA Exhibit C | Transfers | A | https://www.zscaler.com/privacy-compliance/transfer-impact-assessment-tia |

### Service notes — ZIA; ZPA

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| ZIA | Service `name` | Zscaler Internet Access — cloud security for internet/SaaS egress | SSE | A | Compliance Center; DPA tables |
| ZPA | Service `name` | Zscaler Private Access — zero-trust private-app access | ZTNA | A | same |
| Log pin differs | Offering characteristic | ZIA: EEA+CH option; ZPA: EEA option | Logs, not live inspection PoP | B | DPA cover letter |
| AWS/Azure on both | `subcontractors` | Hosting for **certain features** of ZIA and ZPA (plus many other SKUs) | Not equivalent to “ZIA runs on AWS” | B | Sub-processor page |
| MDR / AI SKUs | optional offerings | Sub-processor page lists MDR, AI Protect, Copilot, Z-Agent | Separate offerings | B | Sub-processor page |

**DORA:** Zscaler is a typical ICT third party for secure access. Business Continuity Cloud / DSPM appear in marketing as DORA-adjacent; do not invent a notification clause. Concentration: many financial entities use Zscaler — `concentration_risk` is still C for a given estate.

**AI Act:** Zscaler Copilot / AI Protect are vendor AI features. Inspection of customer traffic is not itself an “AI system” definition.

---

## 6. Datadog

**Legal identity:** Datadog, Inc. Global HQ: 620 8th Ave, 45th Floor, New York, NY 10018. European HQ: Paris.

**Recommended ICT Provider:** one record `datadog`.

**Candidate `type`:** `cloud-platform` (observability SaaS). Matches how OSM already types GitHub better than `software-vendor`.

### Provider facts

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| HQ | `headquarters` | `us` (NYC); EU office FR | Corporate | A | https://www.datadoghq.com/about/contact/ |
| Trust Center | `certifications` | ISO/IEC 27001, 27017, 27018, 27701, 42001:2023; SOC 2 Type 2; PCI DSS; FedRAMP High; GDPR; DPF; HIPAA; TISAX; IRAP; tiles for **DORA** and **EU AI Act** | Download reports via portal; scope per report | B | https://trust.datadoghq.com/ |
| DPA | `gdpr_dpa_signed` | Public DPA (2024-01-03 version reviewed); ISO 27001 + SOC 2 Type 2 + CAIQ on request; customer audit rights if law requires and reports insufficient | Template / C signed | A / C | https://www.datadoghq.com/legal/data-processing-addendum/2024-01-03/ |
| Sites (independent) | characteristic `datadog_site` | US1, US3, US5 (US); EU1 Germany; UK1 UK; AP1 Japan; AP2 Australia; US1-FED / US2-FED | **Cannot share data across sites** | A | https://docs.datadoghq.com/getting_started/site/ |
| UK hosting launch | `data_processing_locations` | AWS Europe (London) region launch announced 2026-07-16 | UK1 | A | https://www.datadoghq.com/about/latest-news/press-releases/datadog-expands-uk-data-hosting-capabilities-on-aws-europe-london-region/ |
| Support exception | locations | Data “never stored in a separate region” but may leave hosting region for support | All commercial sites | B | https://www.datadoghq.com/legal/data-transfer-impact-assessment/2023-09-05/ |
| Subprocessors | `subcontracting_allowed` | `conditional`; 30-day list update | See table | A | https://www.datadoghq.com/legal/subprocessors/ |
| Infrastructure subprocessors | `subcontractors` (illustrative) | AWS (US, AU, IT, JP, UK); Google (US, DE); Microsoft Azure (US); Snowflake (US); Salesforce/Zendesk support (US) | Infrastructure / ops | A | same |
| AI subprocessors | `subcontractors` | Anthropic PBC (US); OpenAI LLC (US) — “AI services” | Optional AI features | A | same |
| Privacy stance | characteristic | Services “not generally intended” for personal data; masking/filtering documented; DPA if PD is sent | Processor | B | https://www.datadoghq.com/gdpr/ |
| DORA support materials | `dora_notification_clause` | Blog + Cloud Security framework `dora` with 250+ mapped rules — **customer environment** posture, not Datadog-as-ICT-third-party clause | unset | B | https://www.datadoghq.com/blog/datadog-dora-compliance/ ; https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/frameworks_and_benchmarks/supported_frameworks.md |

### Service notes — Observability platform; APM

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Service 1 | Service `name` | Datadog observability platform (metrics, infra, UX) | Multi-product SaaS | A | https://www.datadoghq.com/privacy/ |
| Service 2 | Service `name` | Datadog APM (application performance / tracing) | Same sites / same provider | A | Product family on datadoghq.com; site docs apply |
| Alternate second service | — | Log Management is an equally valid second Service if the estate splits telemetry types | Same compliance boundary unless a report says otherwise | B | Trust Center |
| Site as Offering | Offering | `datadog.observability.us1` vs `…eu1` vs `…uk1` vs `…fed` | Independent instances | A | Sites docs |
| FedRAMP | Offering | US1-FED FedRAMP High; US2-FED IL5 in process | US government | B | Sites docs |

**AI Act:** Trust Center lists EU AI Act and ISO 42001. Anthropic/OpenAI as subprocessors show vendor-hosted models for platform AI. Do not classify customer traces/logs as an AI system.

**DORA:** Observability/APM is ICT for detection, incident, and resilience testing. Datadog’s DORA *framework pack* monitors **the customer’s cloud**, which is a different OSM object (customer posture) than Datadog as third party.

---

## 7. Dynatrace

**Legal identity:** Dynatrace, Inc. Principal executive offices **as of 2026 10-K:** 280 Congress Street, 11th Floor, Boston, MA 02210. Relocated from Waltham, MA in spring 2025 (announced 2025-01-22). **Engineering HQ / founding location:** Linz, Austria (Dynatrace Austria GmbH, Am Fünfundzwanziger Turm 20, 4020 Linz). Founded Linz 2005.

**Recommended ICT Provider:** one record `dynatrace`. `headquarters` = `us` (principal executive office). Record Linz as engineering location in notes — OSM cannot store two HQs.

**Candidate `type`:** `cloud-platform` for SaaS; Dynatrace Managed is self-hosted control plane (`software-vendor` semantics on the same entity).

### Provider facts

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| US principal office | `headquarters` | `us` (Boston, not Waltham) | Corporate 2026 | A | https://ir.dynatrace.com/sec-filings/all-sec-filings/content/0001773383-26-000019/dt-20260331.htm ; https://www.dynatrace.com/news/press-release/dynatrace-to-relocate-corporate-headquarters-to-boston/ |
| Engineering HQ | note (no field) | Linz, Austria | R&D | A | https://www.dynatrace.com/careers/locations/linz/ ; https://www.dynatrace.com/careers/locations/ |
| Trust Center programs | `certifications` | ISO 27001:2022; SOC 1 Type II; SOC 2 Type II; FedRAMP Moderate; GDPR; DPF; HIPAA; IRAP; TISAX; TX-RAMP; ENS; CSA; CCPA | Portal holds reports | B | https://www.dynatrace.com/company/trust-center/ ; https://trust.dynatrace.com/ |
| Privacy contact | — | Dynatrace, LLC, 280 Congress Street, Boston | Privacy notice | A | https://www.dynatrace.com/company/trust-center/privacy/ |
| Deployment modes | Offering | Majority SaaS; **Dynatrace Managed** = customer-provisioned infra, data residency/sovereignty under customer control; Dynatrace auto-upgrades instances | SaaS vs Managed | A | 2026 10-K |
| SaaS regions | `data_processing_locations` (choice C) | AWS, Azure, Google Cloud regions listed in docs (e.g. AWS IAD/PDX/DUB/SYD + others; Azure Virginia/Arizona/NL/Toronto/Dubai/Zurich/Sydney; GCP us-east4, europe-west3) | SaaS | B | https://docs.dynatrace.com/docs/manage/data-privacy-and-security/data-security/data-security-controls |
| Isolation | characteristic | Per-environment tenant; dedicated S3 bucket (AWS) or Azure storage account for platform data at rest | SaaS AWS/Azure | B | same docs |

### Service notes — Observability platform; second service

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Service 1 | Service `name` | Dynatrace observability platform (OneAgent, Smartscape, PurePath, Grail, Davis AI) | Unified platform | A | Privacy notice; 10-K |
| Service 2 (catalog pick) | Service `name` | Dynatrace Application Security *or* Digital Experience Monitoring | Same platform, different capability | B | 10-K product list |
| Davis AI | AI characteristic | Vendor AIOps / root-cause engine — AI system *inside* the observability service | Do not set customer risk class | B | 10-K / product docs |
| SaaS vs Managed | Offering `deployment_model` | SaaS vs customer-provisioned Managed | Same Service | A | 10-K |

**HQ stress:** Investigation brief said “Waltham US vs Linz Austria.” As of 2026-09-13 the official US HQ is **Boston**; Waltham is historical. Linz remains Engineering HQ. OSM `headquarters` = `us` loses Austria entirely.

**DORA:** Observability + application security are ICT for operational monitoring and incident. FedRAMP Moderate ≠ DORA.

**AI Act:** Davis AI / AIOps is a vendor AI system. Grail is a data lakehouse (not automatically an AI system).

---

## 8. Snowflake

**Legal identity:** Snowflake Inc. (Delaware). SEC principal executive office: 106 East Babcock Street, Suite 3A, Bozeman, MT 59715 (company has stated it is globally distributed and designates Bozeman because the SEC requires a principal office). Marketing “HQ” listing: 135 Constitution Drive, Menlo Park, CA 94025 (also ISO 27001 in-scope ISMS location).

**Recommended ICT Provider:** one record `snowflake`. `headquarters` = `us`.

**Candidate `type`:** `cloud-platform` (data platform SaaS on customer-chosen AWS/Azure/GCP). Underlying CSP is a **second** ICT Provider on the Offering if the estate tracks hosting.

### Provider facts

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| HQ / PE office | `headquarters` | `us` (Bozeman PE office; Menlo Park ISMS/marketing HQ) | Dual-address US | A | SEC entity data; https://www.snowflake.com/en/contact/ |
| ISO 27001:2022 | `certifications` | Schellman: ISMS for development, maintenance, operations of **Snowflake AI Data Cloud**; features in same auth boundary including Native Apps, Streamlit, SPCS, **Cortex**, Samooha; regions on all supported CSPs in three geo segments (Americas, Europe/ME, APAC); includes 27017:2015 and 27018:2019; SoA v2.1 dated 2025-04-02; location 135 Constitution Drive, Menlo Park | Platform + listed features — **not** customer workloads’ own compliance | A | https://www.snowflake.com/content/dam/snowflake-site/en/legal/2025-ISO-27001-Certificate.pdf ; https://docs.snowflake.com/en/user-guide/cert-iso-27001 |
| Other programs (marketing list) | `certifications` | SOC 1 & 2 Type 2, FedRAMP Moderate/High, DoD IL4/IL5, PCI-DSS, HITRUST, TISAX, ITAR | Confirm each report’s boundary | B | https://www.snowflake.com/en/why-snowflake/snowflake-security-hub/ |
| DPA | `gdpr_dpa_signed` | Customer DPA published; hosting in customer-selected region; processing outside region only as reasonably necessary to provide Services or as required by law | Template / C signed | A / C | https://www.snowflake.com/legal-files/Snowflake-Customer-Data-Processing-Addendum.pdf |
| Hosting region | characteristic | Customer selects Hosting Region on Order Form or in-service config; customer responsible for user access location and onward sharing | Service | A | same DPA §7.1 |
| Subprocessors | `subcontracting_allowed` | `conditional`; list at snowflake.com/legal/snowflake-sub-processors; ≥14 days notice; objection path | Includes customer-chosen AWS/Azure/GCP | A | DPA §4 ; https://www.snowflake.com/legal/snowflake-sub-processors/ |
| Audit evidence | `audit_rights` | On request: ISO 27001, HITRUST, PCI, SOC 1/2 Type II, HIPAA BA report, SIG/CAIQ | DPA §6.1 | B | DPA |
| DORA page | `dora_notification_clause` | Snowflake states DORA applies to financial entities **and their third-party providers like Snowflake**; points to Financial Services Addendum for additional EU FI commitments; vendor-risk program for subprocessors | FSA terms are contractual **C** | B | https://www.snowflake.com/en/solutions/industries/financial-services/dora/ |

### Service notes — Snowflake Data Cloud; Cortex AI

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Service 1 | Service `name` | Snowflake Data Cloud / AI Data Cloud | Multi-cloud SaaS warehouse / platform | A | ISO cert; security hub |
| Service 2 | Service `name` | Snowflake Cortex AI (AI Features) | Cortex AI Functions, Copilot, Fine-tuning, Search, Analyst, Agents, Snowflake Intelligence | A | https://www.snowflake.com/en/legal/compliance/snowflake-ai-trust-and-safety/ |
| Cortex in ISO boundary | `certifications` scope | Cortex explicitly in ISO 27001 authorization boundary | Cortex as part of Service | A | 2025 ISO certificate |
| Models | characteristic | Proprietary, open-source, and licensed proprietary models hosted/managed by Snowflake | Cortex | A | AI Trust page (updated 2026-01-01) |
| Training use | characteristic | Customer Data / Inputs / Outputs **not** used to train models for other customers; remain in Snowflake Security Boundary | GA AI Features | A | same |
| Optional | characteristic | AI Features optional; RBAC and model allow-lists | Account | A | same |
| BYO models | distinction | Models brought via SPCS are **Customer Data**, not part of the Service | AI Act: customer system | A | same |
| Cross-region inference | characteristic `cortex_cross_region` | `CORTEX_ENABLED_CROSS_REGION`; payload transient to processing region; data at rest stays in account region; geography scopes e.g. `AWS_EU` | Compliance-sensitive; defaults have been changing (BCR 2026_06) | B | https://docs.snowflake.com/En/user-guide/snowflake-cortex/cross-region-inference |

**AI Act stress (explicit):** Cortex **is** a vendor-operated AI system (and a suite of them). SPCS / customer-hosted models are **the customer’s** AI systems on Snowflake’s platform. OSM must not put one `ai_act_risk_class` on “Snowflake.” Offering split: `snowflake.datacloud.warehouse` vs `snowflake.datacloud.cortex` vs `snowflake.datacloud.spcs-models`. Do not classify customer risk.

**DORA:** Data platforms used for regulatory reporting or trading books are often critical ICT — that determination is C. Snowflake FSA is the public hook for extra financial-sector terms.

**Type:** SaaS data platform on a customer-chosen hyperscaler = two `providers[]` on the Offering (`snowflake` + `aws`|`azure`|`gcp`).

---

## 9. Databricks

**Legal identity:** Databricks, Inc. Address on Trust pages: 160 Spear Street, 15th Floor, San Francisco, CA 94105.

**Recommended ICT Provider:** one record `databricks`. Azure Databricks is a **Microsoft-operated** channel of the same platform — may need `providers[]` = `databricks` + `azure` on that Offering.

**Candidate `type`:** `cloud-platform`. Control plane is Databricks SaaS; data plane is typically in the **customer’s** cloud account (not classic multi-tenant SaaS). That shared-responsibility split is the Databricks-specific stress.

### Provider facts

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Address | `name`, `headquarters` | Databricks, Inc.; `us` | Trust footer | A | https://www.databricks.com/trust/compliance |
| Stated certifications | `certifications` | ISO 27001, 27017, 27018; SOC 2 Type II; offerings for PCI-DSS, HIPAA, FedRAMP | Company pages; SoA/certificate via due-diligence pack | B | https://www.databricks.com/trust/trust ; https://www.databricks.com/trust/compliance/iso-27001 |
| ISO 27001:2022 | `certifications` | “Databricks is ISO 27001:2022 certified”; certificate + SoA downloadable | Confirm SoA product list in pack (not fully public in fetch) | B | https://www.databricks.com/trust/compliance/iso-27001 |
| Security Addendum | contract (C) | Contractual security commitment in customer agreement | All customers (claimed) | B | Trust page |
| Enhanced Security and Compliance add-on | Offering characteristic | Required for many regulated profiles; standards include C5, HIPAA, HITRUST, IRAP, ISMAP, PCI-DSS, TISAX, etc. | **Not on by default** | B | https://learn.microsoft.com/en-us/azure/databricks/security/privacy/ ; https://docs.databricks.com/aws/en/security/privacy/enhanced-security-compliance |
| Partner-powered AI | characteristic | Disabled by default when compliance security profile is on | AI features vs regulated workspace | B | AWS enhanced security docs |
| DORA white paper | `dora_notification_clause` | Dec 2024 paper: Databricks as platform ICT; FSA cooperation with FS regulators; shared responsibility (Databricks = control plane) | unset clause; FSA is C | B | https://www.databricks.com/sites/default/files/2024-12/databricks-dora-operational-resilience-whitepaper.pdf |
| Subprocessors | `subcontracting_allowed` | Public list exists (search indexed); includes customer-optional model providers (Anthropic, OpenAI) in secondary sources — **confirm live official list before encoding** | D if URL not re-fetched as HTML | D / B | Use current Trust/legal subprocessor page at research time |
| Pen test / bug bounty | provenance | Public HackerOne; 8–10 external / 15–20 internal tests/year claimed | Platform | B | https://www.databricks.com/trust/trust |

### Service notes — Data Intelligence Platform; Mosaic AI / Databricks SQL

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Service 1 | Service `name` | Databricks Data Intelligence Platform (lakehouse + Unity Catalog) | ETL, ML/AI, DWH/BI | A | https://www.databricks.com/product/platform ; https://docs.databricks.com/aws/en/lakehouse-architecture/scope |
| Service 2 (AI) | Service `name` | Mosaic AI / Databricks AI capabilities (foundation models, agents, AI Gateway, AI Functions) | Build/deploy/monitor AI apps; hosted + external + custom models | A | https://docs.databricks.com/aws/en/agents/gen-ai-capabilities |
| Service 2 alt. | Service `name` | Databricks SQL | SQL warehouses, editor, dashboards; Unity Catalog | A | https://docs.databricks.com/aws/en/query/ |
| Cloud choice | Offering `providers[]` | AWS / Azure / GCP workspace | Data plane in customer CSP account | A | Platform docs |
| AI Act split | `mappings.ai_act` | Mosaic AI **hosts** customer apps and can **serve** Databricks-hosted foundation models. Customer-built agents are customer AI systems. Databricks-hosted FM endpoints are vendor AI systems. | Do not set one risk class | B | AI capabilities docs; Trust page (“from APIs like OpenAI to custom-built models”) |

**Stress:** Databricks is the sharpest “SaaS vs cloud-platform vs customer IaaS” case. The technological service “lakehouse analytics” is delivered by Databricks **and** the customer’s AWS/Azure/GCP account. OSM `providers[]` on the Offering should list both. ISO 27001 on Databricks does not certify the customer data plane.

**DORA:** Control-plane vs data-plane split matters for ICT subcontracting chains (Databricks → AWS/Azure/GCP, and customer → same CSP).

---

## 10. Short notes (time-boxed)

### GitHub (Microsoft)

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Distinct legal seller | ICT Provider | GitHub, Inc. — already `cloud-platform` / `us` in OSM examples | Subsidiary of Microsoft | A | https://github.com/trust-center |
| Trust surfaces | provenance | GitHub Trust Center; GHEC Trust Center; Copilot Trust Center | Product-split trust | A | https://github.com/trust-center ; https://ghec.github.trust.page/ |
| ISO / SOC | `certifications` | ISO 27001 ISMS; ISO 27701, 27018, CSA STAR (2023 changelog); Copilot Business/Enterprise added to ISO 27001 SoA 2024-05-09; SOC 2 Type I Copilot Business (2024), Type II planned | **Product-scoped** | B | https://github.blog/changelog/2023-07-05-new-and-updated-iso-and-csa-star-certifications-are-now-available/ ; https://github.blog/changelog/2024-06-03-github-copilot-compliance-soc-2-type-1-report-and-iso-iec-270012013-certification-scope/ |
| Copilot data residency | characteristic | Policy to keep inference in US or EU (EU Data Boundary incl. EFTA as of 2026-05-01 per changelog); off by default | GHEC with data residency | B | https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/github-copilot-with-data-residency ; https://github.blog/changelog/2026-04-13-copilot-data-residency-in-us-eu-and-fedramp-compliance-now-available/ |
| AI Act | — | GitHub follows Microsoft Responsible AI Standard; Copilot is a vendor AI system | Do not classify customer code | B | https://github.com/trust-center |
| Provider question | `providers[]` | Prefer `github` not `microsoft` unless the contract is a Microsoft Enterprise Agreement that names Microsoft as seller (C) | Contracting party | C | — |

### GitLab

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal / HQ | `headquarters` | GitLab Inc.; **remote-only, no headquarters** (FY26 10-K). Mailing: 268 Bush Street #350, San Francisco, CA 94104 | OSM `us` is a filing-address approximation | A | https://about.gitlab.com/company/visiting/ ; FY26 10-K |
| Editions | Offerings | GitLab.com (multi-tenant SaaS); Dedicated (single-tenant SaaS, customer-chosen AWS region); Self-Managed | Three delivery models | A | 10-K; https://about.gitlab.com/security/ |
| ISO / SOC | `certifications` | ISO 27001:2022 + 27017 + 27018 for **GitLab.com and GitLab Dedicated** SaaS; SOC 2 Type 2 Security/Confidentiality/Availability **separately** for .com and Dedicated; ISO 42001 for AI governance | Self-Managed **not** in SaaS ISO scope | A | https://about.gitlab.com/security/ ; https://trust.gitlab.com/ |
| Subprocessors | `subcontractors` | Google, AWS (Dedicated region = customer choice), Anthropic, OpenAI, Fireworks.ai, HiddenLayer, Zendesk, ClickHouse, … | Product-tagged | A | https://about.gitlab.com/privacy/subprocessors/ |
| Type | `type` | `cloud-platform` for .com/Dedicated; Self-Managed is software | Same legal entity | B | — |

### HashiCorp Terraform (IBM)

**Is IBM the ICT Provider?** For **commercial HCP / IBM Terraform subscriptions invoiced by IBM after 2025-09-01: yes, IBM (or the IBM contracting entity on the order) is the seller.** HashiCorp continues as “HashiCorp, an IBM Company.” For **Terraform CLI** used as a local binary, there may be **no ICT Provider relationship** at all (software license only). For **OpenTofu**, the steward is the Linux Foundation ecosystem — a different provider.

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Acquisition close | provenance | IBM completed HashiCorp acquisition 2025-02-27; $6.4B | Corporate | A | https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform |
| Ops transition | contract party | From 2025-09-01 HashiCorp business operations transition to IBM; invoices issued by IBM; new IBM customer numbers | Commercial customers | A | https://www.hashicorp.com/en/blog/what-transition-to-ibm-means-hashicorp-customers-greater-value-same-commitment |
| Rename | Offering names | Legacy “HCP Terraform / Terraform Cloud / Terraform Enterprise” map to IBM Terraform Standard/Premium / IBM Terraform Self-Managed Premium | SKU names | A | https://support.hashicorp.com/hc/en-us/articles/43559447807251-HashiCorp-IBM-Product-Renaming-Update |
| Certifications (HashiCorp security page) | `certifications` | SOC 2 Type 2, ISO 27001, 27017, 27018 covering Enterprise products (Terraform, Vault, …) **and** Cloud products (HCP, HCP Terraform, …) | Listed products | A | https://www.hashicorp.com/en/trust/security |
| Certifications (compliance overview snippet) | scope | ISO 27001 scope text names **IBM Terraform, IBM Terraform EU, IBM Terraform Self-Managed**, plus Vault/Boundary/… | Post-rebrand SoA | B | https://www.hashicorp.com/en/trust/compliance |
| PCI | `certifications` | PCI DSS v4.0.1 AOC as Level 1 SP for HCP Vault Radar, Vault Dedicated, Boundary, Waypoint, **HCP Terraform**, Packer | Named HCP products | B | HashiCorp compliance overview |
| License | characteristic | Terraform 1.6+ is BSL 1.1 (source-available, **not** OSI open source); production use grant excludes competing hosted/embedded offerings | CLI | A | https://www.hashicorp.com/en/trust/security (product signing); HashiCorp BSL terms referenced in public legal correspondence |
| OpenTofu | different Service | MPL 2.0 fork under Linux Foundation | Not IBM | A | https://opentofu.org/manifesto/ |

**OSM treatment:** do **not** set IBM as ICT Provider for a team that only runs OSS-era MPL Terraform or OpenTofu. Do set `ibm` (or `hashicorp` with a note that the contracting party is now IBM) for HCP Terraform / IBM Terraform. Dual-provider during transition is C (which entity is on the MSA).

**Type:** HCP Terraform = `cloud-platform` (or IBM `cloud-platform` / `software-vendor`). Terraform CLI = no hosted service.

### Splunk (Cisco)

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Acquisition | ICT Provider | Cisco completed Splunk acquisition 2024-03-18 (~$28B); Splunk delisted | Contracting party may be Cisco or Splunk — C | A | https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2024/m03/cisco-completes-acquisition-of-splunk.html |
| Trust | provenance | Splunk compliance page + Cisco Trust Portal (Splunk Trust Documents) | Dual portals | A | https://www.splunk.com/en_us/about-splunk/splunk-data-security-and-privacy/compliance-at-splunk.html ; https://trustportal.cisco.com/c/r/ctp/home.html |
| Cloud vs Enterprise | Offerings | Splunk Cloud Platform vs on-prem Splunk Enterprise | Cloud Security Addendum **excludes** on-prem hybrid components and splunk.com trials | B | https://www.splunk.com/en_us/legal/splunk-cloud-security-exhibit.html |
| Cloud audits | `certifications` | Splunk Cloud Platform audited to ISO 27001 and SOC 2 Type 2 (Standard Environment); product×control matrix on compliance page | Named Cloud features | B | Compliance page; CSE §19.1 |
| Type | `type` | Cloud = `cloud-platform`; Enterprise = `software-vendor`; seller may be `cisco` | One vs two ICT Providers | B | — |
| DORA | — | SIEM/observability ICT third party if used for security monitoring | C criticality | — | — |

### Zoom

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal / HQ | `name`, `headquarters` | Zoom Communications, Inc. (name restored Nov 2024); 55 Almaden Blvd, 6th Floor, San Jose, CA 95113; `us` | Corporate | A | https://investors.zoom.us/static-files/7370d7ce-5293-4f6f-b91e-6eb90c9a37b3 |
| ISO 27001:2022 | `certifications` | Certificate issued **2026-02-17**; long explicit product list including Meetings, Phone, Rooms, Contact Center, **Zoom AI Companion and AI Expert Assist**, AI Studio/CAIC, AI Notetaker, … | **Only listed UCaaS products** | A | https://www.zoom.com/en/trust/legal-compliance/iso-27001/ |
| AI Act | — | AI Companion is a vendor AI system in the ISO scope list | Do not classify meeting content risk | B | same |
| Type | `type` | `cloud-platform` (UCaaS) | — | B | — |

### CyberArk

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal / HQ | `headquarters` | CyberArk Software Ltd., **Israel**; principal executive offices 9 Hapsagot St., Park Ofer B, Petach-Tikva 4951040. US office 60 Wells Avenue, Newton, MA | OSM `il` (legal HQ) vs US go-to-market office | A | https://www.sec.gov/Archives/edgar/data/1598110/000117891325000811/zk2532806.htm ; https://www.cyberark.com/ko/company/office-locations/ |
| Trust Center | `certifications` | ISO 27001:2022, 27017, 27018, 42001:2023, 22301, 9001; SOC 2/3; CSA STAR; FedRAMP High; PCI DSS v4.0.1; Common Criteria; IRAP; HIPAA tile | Confirm Identity Security Platform vs self-hosted Privilege Cloud vs self-hosted PAM | B | https://trust.cyberark.com/ |
| Type | `type` | Privilege Cloud / Identity Security Platform = `cloud-platform`; self-hosted PAM = `software-vendor` | Same Israeli legal entity | B | — |
| DORA | — | Privileged access / secrets are typical critical IAM ICT | C | — | — |

### SentinelOne

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Legal / HQ | `headquarters` | SentinelOne, Inc. (Delaware); 444 Castro Street, Suite 400, Mountain View, CA 94041; `us`. Tel Aviv R&D; Amsterdam European HQ | Corporate | A | https://www.sec.gov/Archives/edgar/data/1583708/000158370826000035/sentineloneincfy2026annuala.pdf |
| Trust Center | `certifications` | ISO 27001:2022 + SoA, 27017, 27018; SOC 2 Type 2; FedRAMP High; FISMA High; GDPR; Common Criteria; Cyber Essentials / Plus | Singularity platform — confirm module | B | https://trust.sentinelone.com/ |
| AI | — | Purple AI statements (data usage, model training) on Trust Center | Vendor AI feature | B | Trust Center AI docs |
| Type | `type` | `cloud-platform` (+ optional MDR offering as `managed-service` characteristic) | CrowdStrike analogue | B | — |

### New Relic

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| ISO 27001:2022 | `certifications` | Certificate 2025-09-18; Observability Platform on **AWS, Azure, First Party**; **main location Portland, Oregon**; also SF, London, Barcelona, Bangalore, Hyderabad | **Pixie (GCP) explicitly out of scope** | A | https://docs.newrelic.com/docs/security/security-privacy/compliance/certificates-standards-regulations/iso-27001/ |
| HQ | `headquarters` | ISO main location Portland OR; LEI/head-office datasets still list 188 Spear St, San Francisco | Prefer `us`; city is dual | B | New Relic ISO doc (official); LEI secondary |
| Type | `type` | `cloud-platform` | Observability SaaS | B | — |
| Scope lesson | — | Official page models OSM’s required behavior: named services **not** in the cert | — | A | same ISO doc |

### Grafana Labs

| Fact | OSM field | Value | Scope | Class | URL |
|---|---|---|---|---|---|
| Trust Center | `certifications` | SOC 2; ISO 27001 + SoA; ISO 22301; PCI DSS v4.0.1; GDPR; DPF; TISAX; CSA STAR; FedRAMP High; TX-RAMP | **Grafana Cloud** vs self-managed OSS Grafana are different delivery models | B | https://trust.grafana.com/ |
| OSS vs Cloud | Offerings | Grafana OSS/Enterprise (software) vs Grafana Cloud (SaaS) | Two types, possibly one vendor | B | Trust Center + product split |
| Type | `type` | Cloud = `cloud-platform`; OSS = often **no** ICT Provider (community software) or `software-vendor` for Grafana Enterprise | Do not mark Linux Foundation/CNCF as provider for Grafana OSS | B | — |
| HQ | `headquarters` | Not confirmed from an official 10-K in this pass (private company). Commonly New York — **D** for OSM until an official legal page is captured | D | — | — |

---

## Service → Offering → Provider mapping (recommended for later Phase 4)

| Service (stable capability) | Offerings (requestable) | ICT Provider id(s) |
|---|---|---|
| Issue / work tracking | Jira Cloud; Jira Data Center; (Gov/Isolated later) | `atlassian` |
| Team wiki | Confluence Cloud; Confluence Data Center | `atlassian` |
| Workforce IAM | Okta WIC cell (US/EU/…) | `okta` |
| Customer IAM | Auth0 / CIC region | `okta` |
| Endpoint detection & response | Falcon; Falcon Complete (MDR) | `crowdstrike` |
| Identity threat detection | Falcon Identity; Falcon Complete Identity | `crowdstrike` |
| Cloud-delivered secure access | Prisma Access | `palo-alto-networks` (+ implicit AWS/GCP/OCI) |
| Cloud-native application security | Prisma Cloud | `palo-alto-networks` |
| Internet / SaaS security edge | ZIA (log region option) | `zscaler` |
| Zero-trust private access | ZPA (log region option) | `zscaler` |
| Observability | Datadog site (US1/EU1/UK1/…) | `datadog` |
| APM | Datadog APM on same site | `datadog` |
| Observability | Dynatrace SaaS region; Dynatrace Managed | `dynatrace` |
| Data platform | Snowflake account on AWS/Azure/GCP region | `snowflake` + CSP |
| Generative / analytic AI on Snowflake | Cortex (cross-region setting) | `snowflake` |
| Lakehouse / data intelligence | Databricks workspace on AWS/Azure/GCP | `databricks` + CSP |
| Mosaic AI / Databricks SQL | Feature SKUs on that workspace | `databricks` + CSP |
| Source hosting | GitHub.com / GHEC / GHEC data residency | `github` |
| DevSecOps | GitLab.com / Dedicated / Self-Managed | `gitlab` |
| IaC control plane | IBM/HCP Terraform | `ibm` (post-2025-09-01 commercial) |
| IaC CLI | Terraform BSL binary or OpenTofu | none or `ibm` / Linux Foundation — see notes |
| Security analytics | Splunk Cloud vs Enterprise | `splunk` and/or `cisco` |
| Meetings | Zoom Meetings (+ AI Companion optional) | `zoom` |
| Privileged access | CyberArk Privilege Cloud vs self-hosted | `cyberark` |
| Endpoint | SentinelOne Singularity (± MDR) | `sentinelone` |
| Observability | New Relic platform (Pixie excluded from ISO) | `new-relic` |
| Dashboards | Grafana Cloud vs Grafana Enterprise | `grafana-labs` |

---

## Fields that stay empty (do not invent)

| Field | Why |
|---|---|
| `contract_ref`, `contract_start`, `contract_end`, `notice_period_days` | No public customer contracts |
| `gdpr_dpa_signed` | Templates exist; signature is per customer |
| `dora_notification_clause` | No public clause text that can be asserted as true for all customers |
| `risk_level` | OSM-M-009: customer assessment |
| `operational_criticality`, `rto`, `rpo` | Posture / DORA maps; customer-dependent |
| `substitutability` as a universal enum | Alternatives exist in each category, but lock-in is estate-specific |
| `ai_act_risk_class` | Legal classification of a *use* is not a public product fact |
| Exhaustive `subcontractors[]` | Lists are long, product-scoped, and change; store URL in provenance |

`subcontracting_allowed` = `conditional` is the only provider-level subcontracting value that is generally A across this set.

---

## OSM stress-test register (for the decision register, not schema changes)

| ID | Topic | Evidence | Why OSM is awkward |
|---|---|---|---|
| ST-SAAS-01 | No `saas` in `type` enum | Entire file | Forced into `cloud-platform` or `software-vendor` |
| ST-SAAS-02 | Dual HQ / no HQ | Atlassian AU+US; Dynatrace Boston vs Linz; Snowflake Bozeman vs Menlo Park; GitLab remote-only; CyberArk IL legal vs US office | Single `headquarters` code |
| ST-SAAS-03 | Certification without scope | All Trust Centers | `certifications[]` on Provider |
| ST-SAAS-04 | Cloud vs self-managed edition | Atlassian, GitLab, Dynatrace, Splunk, Grafana, CyberArk, Terraform | Edition is Offering, but certs attach to Provider |
| ST-SAAS-05 | Acquisition = new seller | IBM←HashiCorp; Cisco←Splunk; Microsoft←GitHub | One vs two ICT Providers; invoice entity C |
| ST-SAAS-06 | Auth0 vs Okta | Separate platforms, one 10-K | Offering vs second Provider |
| ST-SAAS-07 | SASE as network vs platform | Zscaler, Prisma Access | `network-provider` vs `cloud-platform` |
| ST-SAAS-08 | MDR vs product | Falcon Complete, Zscaler MDR | `managed-service` vs Offering characteristic |
| ST-SAAS-09 | Control plane vs data plane | Databricks; Snowflake on CSP; Atlassian on AWS | Multiple `providers[]` required |
| ST-SAAS-10 | Region pin ≠ all processing | Atlassian Global default; Okta subprocessor exceptions; Zscaler user-proximate PoP; Datadog support access; Cortex cross-region inference | `data_processing_locations` too coarse |
| ST-SAAS-11 | AI system vs AI platform | Cortex vs SPCS; Mosaic AI hosted FM vs customer agents; Rovo vs customer Rovo Agents from Marketplace | One `ai_act_applicable` on Service is too blunt |
| ST-SAAS-12 | DORA marketing vs clause | Okta/Datadog/Snowflake/CrowdStrike “DORA” tiles | Cannot fill `dora_notification_clause` |
| ST-SAAS-13 | Terraform without a provider | CLI-only / OpenTofu | ICT Provider optional — correct, but estate CSV lists “Terraform” as if it were a vendor service |
| ST-SAAS-14 | New Relic Pixie | Official ISO exclusion | Proves certifications must be service-scoped |
| ST-SAAS-15 | Subprocessor arrays | Atlassian/Okta/Datadog/Zscaler public tables | OSM `subcontractors[]` cannot hold the real list |

---

## Source register (official, retrieved 2026-09-13)

**Atlassian:**  
https://www.atlassian.com/trust/compliance  
https://www.atlassian.com/trust/compliance/compliance-faq  
https://www.atlassian.com/trust/compliance/resources/iso27001  
https://www.atlassian.com/trust/compliance/resources/eu-ai-act  
https://www.atlassian.com/trust/ai/transparency  
https://www.atlassian.com/platform/ai-trust  
https://www.atlassian.com/legal/data-processing-addendum  
https://www.atlassian.com/legal/sub-processors  
https://www.atlassian.com/software/data-residency  
https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/  
https://customertrust.atlassian.com/  
https://investors.atlassian.com/resources/investor-faqs/default.aspx  

**Okta / Auth0:**  
https://security.okta.com/  
https://www.okta.com/contact/  
https://investor.okta.com/investor-services/investor-faqs/default.aspx  
https://www.okta.com/okta-data-residency/  
https://www.okta.com/legal/trustandcompliance/subprocessors/  
https://www.okta.com/content/dam/okta---digital/en_us/legal/okta-sub-processor-information-2026-03.pdf  
https://www.okta.com/sites/default/files/2025-01/DATA_PROCESSING_ADDENDUM.pdf  
https://www.okta.com/sites/default/files/2023-04/Workforce-Identity-Cloud-Security-Privacy.pdf  
https://www.okta.com/sites/default/files/2023-04/CIC-Security-Privacy-Doc.pdf  
https://auth0.com/docs/secure/data-privacy-and-compliance  
https://sec.okta.com/articles/2025/05/a-guide-to-dora-compliance-with-okta/  
https://www.sec.gov/Archives/edgar/data/1660134/000166013425000049/okta-20250131.htm  

**CrowdStrike:**  
https://trust.crowdstrike.com/  
https://www.crowdstrike.com/en-us/why-crowdstrike/crowdstrike-compliance-certification/  
https://ir.crowdstrike.com/shareholder-services/investor-faqs  
https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2024/07/crowdstrike-global-data-protection-agreement.pdf  
https://www.crowdstrike.com/en-us/subprocessor-notification/  
https://www.crowdstrike.com/en-us/services/falcon-complete-mdr/  
https://www.crowdstrike.com/en-us/press-releases/crowdstrike-announces-new-regional-clouds-to-expand-secure-data-sovereignty/  

**Palo Alto Networks:**  
https://trust.paloaltonetworks.com/  
https://www.paloaltonetworks.com/about-us/locations  
https://www.paloaltonetworks.com/legal-notices/trust-center/certifications  
https://www.paloaltonetworks.com/legal-notices/trust-center/iso-27000-series  
https://www.paloaltonetworks.com/sase/access  
https://www.paloaltonetworks.com/prisma/  
https://docs.paloaltonetworks.com/prisma-access/administration/prisma-access-overview  
https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=%2Fcontent%2Fpan%2Fen_US%2Fresources%2Fdatasheets%2Fprivacy-prisma-access  

**Zscaler:**  
https://compliance.zscaler.com/  
https://www.zscaler.com/company/contact  
https://www.zscaler.com/resources/legal/iso-certificate-of-registration.pdf  
https://www.zscaler.com/privacy-compliance/dpa  
https://www.zscaler.com/privacy-compliance/faq  
https://www.zscaler.com/privacy-compliance/subprocessors  
https://www.zscaler.com/privacy-compliance/transfer-impact-assessment-tia  
https://www.zscaler.com/resources/legal/zscaler-cover-letter-to-dpa.pdf  
https://trust.zscaler.com/data-center-map  

**Datadog:**  
https://trust.datadoghq.com/  
https://www.datadoghq.com/about/contact/  
https://www.datadoghq.com/legal/data-processing-addendum/2024-01-03/  
https://www.datadoghq.com/legal/subprocessors/  
https://www.datadoghq.com/legal/data-transfer-impact-assessment/2023-09-05/  
https://docs.datadoghq.com/getting_started/site/  
https://www.datadoghq.com/gdpr/  
https://www.datadoghq.com/privacy/  
https://www.datadoghq.com/blog/datadog-dora-compliance/  
https://www.datadoghq.com/about/latest-news/press-releases/datadog-expands-uk-data-hosting-capabilities-on-aws-europe-london-region/  

**Dynatrace:**  
https://www.dynatrace.com/company/trust-center/  
https://trust.dynatrace.com/  
https://www.dynatrace.com/company/trust-center/privacy/  
https://www.dynatrace.com/company/trust-center/data-privacy/  
https://www.dynatrace.com/news/press-release/dynatrace-to-relocate-corporate-headquarters-to-boston/  
https://www.dynatrace.com/careers/locations/  
https://www.dynatrace.com/careers/locations/linz/  
https://docs.dynatrace.com/docs/manage/data-privacy-and-security/data-security/data-security-controls  
https://ir.dynatrace.com/sec-filings/all-sec-filings/content/0001773383-26-000019/dt-20260331.htm  

**Snowflake:**  
https://www.snowflake.com/en/why-snowflake/snowflake-security-hub/  
https://www.snowflake.com/content/dam/snowflake-site/en/legal/2025-ISO-27001-Certificate.pdf  
https://docs.snowflake.com/en/user-guide/cert-iso-27001  
https://www.snowflake.com/legal-files/Snowflake-Customer-Data-Processing-Addendum.pdf  
https://www.snowflake.com/legal/snowflake-sub-processors/  
https://www.snowflake.com/en/legal/compliance/snowflake-ai-trust-and-safety/  
https://www.snowflake.com/en/solutions/industries/financial-services/dora/  
https://docs.snowflake.com/En/user-guide/snowflake-cortex/cross-region-inference  
https://www.snowflake.com/en/contact/  

**Databricks:**  
https://www.databricks.com/trust/trust  
https://www.databricks.com/trust/compliance  
https://www.databricks.com/trust/compliance/iso-27001  
https://www.databricks.com/product/platform  
https://www.databricks.com/sites/default/files/2024-12/databricks-dora-operational-resilience-whitepaper.pdf  
https://docs.databricks.com/aws/en/lakehouse-architecture/scope  
https://docs.databricks.com/aws/en/agents/gen-ai-capabilities  
https://docs.databricks.com/aws/en/query/  
https://docs.databricks.com/aws/en/security/privacy/enhanced-security-compliance  
https://learn.microsoft.com/en-us/azure/databricks/security/privacy/  

**GitHub / Microsoft:**  
https://github.com/trust-center  
https://ghec.github.trust.page/  
https://github.blog/changelog/2023-07-05-new-and-updated-iso-and-csa-star-certifications-are-now-available/  
https://github.blog/changelog/2024-06-03-github-copilot-compliance-soc-2-type-1-report-and-iso-iec-270012013-certification-scope/  
https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/github-copilot-with-data-residency  
https://github.blog/changelog/2026-04-13-copilot-data-residency-in-us-eu-and-fedramp-compliance-now-available/  

**GitLab:**  
https://trust.gitlab.com/  
https://about.gitlab.com/security/  
https://about.gitlab.com/privacy/subprocessors/  
https://about.gitlab.com/company/visiting/  

**HashiCorp / IBM Terraform:**  
https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform  
https://www.hashicorp.com/en/blog/what-transition-to-ibm-means-hashicorp-customers-greater-value-same-commitment  
https://www.hashicorp.com/en/trust  
https://www.hashicorp.com/en/trust/security  
https://www.hashicorp.com/en/trust/compliance  
https://support.hashicorp.com/hc/en-us/articles/43559447807251-HashiCorp-IBM-Product-Renaming-Update  
https://opentofu.org/manifesto/  

**Splunk / Cisco:**  
https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2024/m03/cisco-completes-acquisition-of-splunk.html  
https://www.splunk.com/en_us/about-splunk/splunk-data-security-and-privacy/compliance-at-splunk.html  
https://www.splunk.com/en_us/legal/splunk-cloud-security-exhibit.html  
https://trustportal.cisco.com/c/r/ctp/home.html  

**Zoom:**  
https://www.zoom.com/en/trust/legal-compliance/iso-27001/  
https://investors.zoom.us/static-files/7370d7ce-5293-4f6f-b91e-6eb90c9a37b3  

**CyberArk:**  
https://trust.cyberark.com/  
https://www.sec.gov/Archives/edgar/data/1598110/000117891325000811/zk2532806.htm  
https://www.cyberark.com/ko/company/office-locations/  

**SentinelOne:**  
https://trust.sentinelone.com/  
https://www.sec.gov/Archives/edgar/data/1583708/000158370826000035/sentineloneincfy2026annuala.pdf  

**New Relic:**  
https://docs.newrelic.com/docs/security/security-privacy/compliance/certificates-standards-regulations/iso-27001/  

**Grafana Labs:**  
https://trust.grafana.com/  

**Regulatory (context, not vendor compliance claims):**  
https://eur-lex.europa.eu/legal-content/ENG/ALL/?uri=CELEX:32022R2554  

---

## Research limits (2026-09-13)

- Trust Center portals (Conveyor/SafeBase) often hide SoA PDFs and SOC reports behind login. Product-level ISO/SOC **scope sentences** above are taken from public pages and published certificates only.
- CrowdStrike’s live subprocessor table is behind Falcon login (D for names).
- Databricks public HTML subprocessor page was not fully retrieved as a stable table in this pass (D until re-fetched).
- HashiCorp `/en/trust/compliance` intermittently served a bot-check; ISO/SOC product lists are taken from the successfully fetched `/en/trust/security` page plus search-visible compliance-overview text.
- Grafana Labs headquarters is **D** (no official 10-K). New Relic city-level HQ is dual (Portland ISO main location vs San Francisco commercial address).
- No customer contracts, RTO/RPO, criticality, signed DPA flags, or risk levels were inferred.

This file is investigation evidence. It is not OSM catalog content and not a compliance attestation.