# Research notes — open-source generics, capability rows, Microsoft 365, regulation stress

**Investigation:** 7lens OSM reference-estate  
**Research date:** 2026-09-13  
**Scope:** Parts A–D of the open-source / generics / regulation workstream  
**Frozen model:** OSM 1.3.0 (`SPECIFICATION.md`, `MODEL.md`, current schemas)  
**Constraint:** no schema or example changes. Gaps are decision-register candidates only.

---

## Estate universe note (94, not 100)

`TEMP/01_reference_estate_100.csv` contains **94 data rows** (ranks 1–94), not 100.

This is a Phase 1 lock-file fact, not a modelling recommendation. The investigation methodology still describes a “representative 100-item universe.” The CSV is the locked universe. Do not invent six extra rows to make the filename true.

Evidence class **A** (file count on 2026-09-13).

---

## Evidence classes

| Class | Meaning |
| --- | --- |
| **A** | Publicly verified from an authoritative source (official product page, EUR-Lex, NIST, ISO-accredited supervisor, vendor service description). |
| **B** | Publicly documented but conditional (edition, region, SKU, plan, self-managed vs hosted, edition year). |
| **C** | Customer-dependent. Cannot be asserted as a universal technology fact. |
| **D** | Not publicly determinable. Leave unknown. |

Stack Overflow Developer Survey 2025 and the CNCF Annual Cloud Native Survey (published 2026-01-20) are used **only as popularity evidence**. They do not identify a thing as a Service, Offering, or ICT Provider.

---

## OSM encoding rules used in this note

Taken from the frozen model; not proposed changes.

1. An OSM **Service** is the stable definition of a **technological service**. It is not a product, project, runtime, protocol, digital product, application, or Service Instance (`SPECIFICATION.md` §1; `MODEL.md` “Service”, “Out of scope”).
2. **Service → Service relationships are out of scope.** Validation rule 13 rejects `depends_on`, `consumes`, `provides_to`, `related_service`, `related_services`.
3. **ICT Provider** is a third-party technology organisation. Association is `providers[]` on Service or Offering. Foundations and projects are not ICT Providers unless they themselves deliver ICT services.
4. OSM ICT Provider `type` is a closed enum: `cloud-infrastructure` | `cloud-platform` | `managed-service` | `software-vendor` | `network-provider` | `data-center`. There is no `foundation`, `open-source-project`, or `protocol` type.
5. Use **Service-level `providers`** when the provider is intrinsic. Use **Offering-level `providers`** when provider choice distinguishes the variant. Omit `providers` when the enterprise self-operates and no third party underpins the service.
6. A **self-operated offering** is a Service Offering whose operating model is internal. OSM has no first-class `operating_model` field; that fact, if recorded, is a characteristic. `providers` is omitted (or a `software-vendor` is listed only if a support/licence contract is material).
7. Current examples already follow this pattern: `compute.kubernetes` is “Managed Kubernetes clusters offered as a technological service” with AWS/Azure offerings — not “the Kubernetes project.” `net.enterprise-dns` is a capability Service. `devops.continuous-delivery` has a GitHub-backed pipeline offering.

**Default recommendation for Part A items:** do **not** put the project/product name in the catalog as an ICT Provider or as the Service. Encode the **enterprise technological service** (if one exists). Put commercial hosted/managed variants on offerings. Leave the project itself out of the catalog.

---

## Part A — items that are often not ICT Providers

Each item answers: what is it; who would be the ICT Provider if any; how OSM should encode it.

### A.1 Kubernetes (CNCF)

| | |
| --- | --- |
| **Kind** | Open-source **project** and **runtime / orchestration system**. Not a technological service. Not an ICT Provider. |
| **Steward** | Cloud Native Computing Foundation. Graduated CNCF project (accepted 2016-03-10, graduated 2018-03-06). |
| **Official identity** | “an open source system for automating deployment, scaling, and management of containerized applications” (kubernetes.io; cncf.io/projects/kubernetes). |
| **ICT Provider?** | **None for upstream Kubernetes.** CNCF is a foundation, not an OSM ICT Provider. Managed Kubernetes (EKS, AKS, GKE, OpenShift Dedicated, etc.) has a provider. Self-operated kubeadm/on-prem clusters have no third-party provider unless a support vendor is contracted. |
| **OSM encode** | **Not in catalog as itself.** If the enterprise delivers a Kubernetes *service*, encode `compute.kubernetes` (or equivalent) as a Service with offerings such as `…aws`, `…azure`, `…gcp`, `…self-operated`. That is already the example pattern. Do not create an ICT Provider `cncf` or `kubernetes`. |
| **Popularity only** | CNCF Annual Cloud Native Survey (2026-01-20): 82% of container users run Kubernetes in production. Does not make Kubernetes a Service. |
| **Evidence** | A — kubernetes.io; cncf.io/projects/kubernetes; cncf.io/reports/the-cncf-annual-cloud-native-survey. |

### A.2 Docker

| | |
| --- | --- |
| **Kind** | Name collision: **platform / runtime** (Docker Engine, `dockerd`), **product** (Docker Desktop), **registry service** (Docker Hub). Not one ICT Provider identity. |
| **Steward / vendor** | Docker, Inc. for Desktop, Hub, and commercial offerings. Engine is documented as an open platform with a client–daemon architecture (docs.docker.com). |
| **Official identity** | “Docker is an open platform for developing, shipping, and running applications.” Desktop is “the #1 containerization software for developers and teams” and includes Engine, CLI, Compose, and a local Kubernetes option. |
| **ICT Provider?** | **Docker, Inc.** only for Docker Hub, Docker Desktop licensing, Hardened Docker Desktop, and any hosted registry/build service. Engine running on a customer host is a **runtime**, not an ICT service from Docker. |
| **OSM encode** | **Not in catalog as “Docker.”** If the enterprise offers a container-runtime or image-registry service, encode those Services. A Docker Hub or Docker Desktop enterprise subscription can list `docker-inc` as `software-vendor` or `managed-service` on the relevant offering. Do not treat Engine as a provider. |
| **Popularity only** | SO 2025: Docker “moved from a popular tool to a near-universal one” (+17 points). Popularity, not identity. |
| **Evidence** | A — docs.docker.com/get-started/docker-overview; docker.com/products/docker-desktop. B — which Docker artefact a given estate row meant. |

### A.3 VMware vSphere / VMware Cloud Foundation (Broadcom)

| | |
| --- | --- |
| **Kind** | **Product / product family** (hypervisor + private-cloud IaaS software). vSphere Foundation is a workload platform. VCF is documented as a “full-stack Infrastructure as a Service (IaaS) platform.” Not an ICT Provider. Not automatically a technological service. |
| **Vendor** | Broadcom Inc. (VMware brand). Current public docs: VCF / VVF 9.1 (techdocs last updated 2026-08). |
| **Official identity** | VCF: private cloud platform delivering software-defined compute, storage, networking, Kubernetes, security, and management. VVF: enterprise workload platform for VMs and containers; does not include VCF’s cloud-management and integrated automation. |
| **ICT Provider?** | **Broadcom** as `software-vendor` when the enterprise licenses vSphere/VCF and self-operates. **A managed VMware cloud operator** (historically VMware Cloud on AWS and similar) would be `managed-service` or `cloud-infrastructure` — that is a different offering, not the product name. |
| **OSM encode** | Do not catalog “vSphere” or “VCF” as the Service. Encode the technological service the estate actually consumes: virtual-machine compute, private-cloud IaaS, or Kubernetes-on-VCF. Offerings distinguish self-operated VCF vs a hosted VMware cloud. List Broadcom on the self-operated offering only if the licence/support contract is the third-party relationship being tracked. |
| **Evidence** | A — techdocs.broadcom.com VCF 9.0/9.1 “What Is VMware Cloud Foundation?”; vmware.com feature comparison; Broadcom VCF 9.1 product release (2026-05-05). |

### A.4 Red Hat OpenShift

| | |
| --- | --- |
| **Kind** | **Product** (enterprise Kubernetes application platform) **and**, in managed editions, a **technological service**. |
| **Vendor** | Red Hat (IBM). |
| **Official identity** | Application platform “with Kubernetes at its core.” Sold as **self-managed editions** (Entry-level / Standard / Advanced / VMs) and **managed cloud services** on partner clouds. |
| **ICT Provider?** | **Red Hat** for support and for Red Hat–managed OpenShift. Hyperscaler is an additional provider when the managed service runs on AWS/Azure/GCP (two providers, or offering-level split). Self-managed OpenShift: Red Hat is `software-vendor`; the cluster is not a Red Hat-operated service. |
| **OSM encode** | If the enterprise offers “managed Kubernetes / application platform,” OpenShift is an **offering or characteristic**, not the Service name by default. Preferred: Service = Kubernetes/application platform; offerings = `…openshift-self-managed`, `…rosa`, `…aro`, etc. Do not create ICT Provider `openshift`. |
| **Evidence** | A — redhat.com/en/technologies/cloud-computing/openshift. B — which edition is in the estate. |

### A.5 Red Hat Enterprise Linux (RHEL)

| | |
| --- | --- |
| **Kind** | **Product** — operating system. Not a technological service. Not an ICT Provider. |
| **Vendor** | Red Hat. RHEL 10 is the current major release on the official page (2026). |
| **Official identity** | “The stable foundation” OS for public cloud, datacenter, and edge. Subscription, not a hosted service. |
| **ICT Provider?** | **Red Hat** as `software-vendor` if the enterprise has a RHEL subscription/support contract that must be tracked. The OS image on an Azure/AWS VM does not make Red Hat the compute provider. |
| **OSM encode** | **Not in catalog as a Service.** OS is Product Model / instance inventory — both out of scope. If vendor-risk tracking of the RHEL subscription is required, an ICT Provider `redhat` record is enough; do not invent `os.rhel` as a Service. |
| **Evidence** | A — redhat.com/en/technologies/linux-platforms/enterprise-linux. |

### A.6 Ubuntu (Canonical)

| | |
| --- | --- |
| **Kind** | **Product** (OS). Canonical also sells **technological services** (Ubuntu Pro, managed Kubernetes, managed apps). The estate row “Ubuntu” is the OS, not those services. |
| **Vendor** | Canonical Ltd. |
| **Official identity** | Ubuntu 26.04 LTS “Resolute Raccoon” current LTS on ubuntu.com (fetched 2026-09-13). “No mandatory subscriptions for Ubuntu.” Ubuntu Pro is security/compliance add-on. Canonical also offers fully managed infra and apps. |
| **ICT Provider?** | **Canonical** as `software-vendor` for Ubuntu Pro / support; as `managed-service` only for Canonical-operated offerings (Charmed Kubernetes managed, managed apps). Free Ubuntu on a VM has no ICT Provider. |
| **OSM encode** | Same as RHEL: **not a Service.** Do not catalog “Ubuntu.” Track Canonical only if a Pro/support/managed contract exists. |
| **Evidence** | A — ubuntu.com. B — whether the row meant desktop, server, Pro, or a managed Canonical service. |

### A.7 Terraform

| | |
| --- | --- |
| **Kind** | **Product / IaC tool** (CLI + language). HCP Terraform / IBM Terraform Self-Managed are **products or hosted services**. Not a protocol. Not automatically a Service. |
| **Vendor** | HashiCorp brand; licensor of Terraform ≥1.6.0 is **International Business Machines Corporation (IBM)** (Business Source License 1.1). IBM Terraform Self-Managed 2025.x.x GA 2025-03-20. |
| **Official identity** | “Terraform is an infrastructure as code tool that lets you build, change, and version infrastructure safely and efficiently” (terraform.io). HCP Terraform is the hosted collaboration/automation product. |
| **ICT Provider?** | **IBM / HashiCorp** as `software-vendor` for Enterprise/Self-Managed; as `managed-service` or `cloud-platform` for HCP Terraform. Open-source/BSL CLI used internally is not an ICT service from IBM. |
| **OSM encode** | OSM example already has `auto.infrastructure-as-code` as the Service. Terraform is an implementation/tool. Offerings: `…self-operated` (no provider or IBM as software-vendor) vs `…hcp` (IBM/HashiCorp). Do not catalog “Terraform” as the Service or as an ICT Provider id that means the tool. |
| **Evidence** | A — terraform.io; github.com/hashicorp/terraform LICENSE; ibm.com support page IBM Terraform Self-Managed_2025.x.x. |

### A.8 Ansible

| | |
| --- | --- |
| **Kind** | **Product / automation engine.** Ansible Automation Platform is the enterprise **product**. A hosted AAP could be a technological service. |
| **Vendor** | Red Hat. Official page: Red Hat Ansible Automation Platform — “Turn automation into your strategic advantage.” |
| **ICT Provider?** | **Red Hat** as `software-vendor` for AAP subscriptions; `managed-service` only if Red Hat or a partner operates AAP for the customer. |
| **OSM encode** | Not “Ansible” as a Service. Encode an automation / configuration-management Service if the enterprise delivers one. Offering distinguishes self-operated AAP vs managed AAP. |
| **Evidence** | A — redhat.com/en/technologies/management/ansible. ansible.com official fetch returned HTTP 409 on 2026-09-13 (D). |

### A.9 GitHub Actions

| | |
| --- | --- |
| **Kind** | **Technological service** when using GitHub-hosted runners; **product/runtime** when using self-hosted runners / Actions Runner Controller. Workflow engine is a GitHub product feature. |
| **Vendor** | GitHub, Inc. (Microsoft). |
| **Official identity** | “Automate, customize, and execute your software development workflows right in your repository.” Documents both **GitHub-hosted runners** (GitHub operates the VMs) and **self-hosted runners** (customer operates agents). Billing applies beyond free minutes for hosted usage. |
| **ICT Provider?** | **GitHub** (`managed-service` or `cloud-platform`) for Actions on github.com with hosted runners. For self-hosted runners, GitHub still provides the control plane (Actions service on github.com or GHES); the compute is customer-operated. GHES is closer to `software-vendor` + self-operated offering. |
| **OSM encode** | Fits a CI/CD Service (`devops.continuous-delivery` in the examples already points a pipeline offering at `github`). Offerings: `…github-hosted`, `…github-self-hosted`. Do not treat “GitHub Actions” as an ICT Provider. |
| **Evidence** | A — docs.github.com/en/actions. B — hosted vs self-hosted vs GHES. |

### A.10 GitLab CI/CD

| | |
| --- | --- |
| **Kind** | **Product feature** of GitLab; **technological service** on GitLab.com; self-operated on Self-Managed / Dedicated. |
| **Vendor** | GitLab Inc. |
| **Official identity** | Docs tier: Free / Premium / Ultimate. Offering: **GitLab.com, GitLab Self-Managed, GitLab Dedicated.** CI/CD is defined by `.gitlab-ci.yml`; runners execute jobs. GitLab.com provides hosted runners; Self-Managed requires customer-registered runners. |
| **ICT Provider?** | **GitLab** for GitLab.com and Dedicated (`managed-service`). Self-Managed: GitLab is `software-vendor`. |
| **OSM encode** | Same CI/CD Service as Actions/Jenkins; offerings per operating model (`…gitlab-com`, `…gitlab-dedicated`, `…gitlab-self-managed`). |
| **Evidence** | A — docs.gitlab.com/ci/. B — which offering. |

### A.11 Jenkins

| | |
| --- | --- |
| **Kind** | Open-source **project** / **automation server**. Not a SaaS. Not an ICT Provider. |
| **Steward** | Jenkins project (community; CDF/Linux Foundation ecosystem historically). Governance is a community project document (jenkins.io/project/governance). jenkins.io: “The leading open source automation server.” |
| **ICT Provider?** | **None for upstream Jenkins.** CloudBees or another vendor is `software-vendor` / `managed-service` only if a commercial distribution or hosted Jenkins is contracted. |
| **OSM encode** | **Not in catalog as itself.** If the enterprise runs Jenkins as its CI service, encode the CI/CD Service with a `…self-operated` offering and omit providers (or list CloudBees if that contract exists). |
| **Evidence** | A — jenkins.io; jenkins.io/project/governance. |

### A.12 Azure DevOps

| | |
| --- | --- |
| **Kind** | **Product suite** of technological services (Boards, Repos, Pipelines, Test Plans, Artifacts). Two delivery models: **Azure DevOps Services** (cloud) and **Azure DevOps Server** (self-hosted). |
| **Vendor** | Microsoft. |
| **Official identity** | “Azure DevOps is a cloud-based platform that provides integrated tools for software development teams.” Docs apply to Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022. Pipelines is the CI/CD component, not the whole product. |
| **ICT Provider?** | **Microsoft** as `cloud-platform` / `managed-service` for Azure DevOps Services. Server: Microsoft as `software-vendor`. |
| **OSM encode** | Do not collapse Azure DevOps into “CI/CD” only — Boards/Repos/Artifacts are different technological services. Preferred: one Service per capability the enterprise actually offers (or consumes as a catalogued service), with Microsoft on the offering; or one Service “Azure DevOps” **only if** the estate treats the suite as one requestable service. The latter is weaker OSM (suite-as-service). Flag as a suite-boundary issue (see Part C pattern). |
| **Evidence** | A — learn.microsoft.com Azure DevOps “What is Azure DevOps?” |

### A.13 Argo CD

| | |
| --- | --- |
| **Kind** | Open-source **project** — “declarative, GitOps continuous delivery tool for Kubernetes.” A Kubernetes controller, not a hosted service. |
| **Steward** | Argo project, CNCF graduated (accepted 2020-03-26, graduated 2022-12-06). |
| **ICT Provider?** | **None for upstream Argo CD.** A vendor offering managed Argo (Red Hat OpenShift GitOps, Akuity, etc.) would be an ICT Provider of that managed service. |
| **OSM encode** | **Not in catalog as itself.** If the enterprise delivers GitOps CD, encode a CD Service with `…self-operated` (Argo as implementation) vs `…managed` (named vendor). Do not create ICT Provider `argoproj` or `cncf`. |
| **Evidence** | A — argo-cd.readthedocs.io; cncf.io/projects/argo. |

### A.14 PostgreSQL

| | |
| --- | --- |
| **Kind** | Open-source **project** / **database product**. Not a service. Not an ICT Provider. |
| **Steward** | PostgreSQL Global Development Group. postgresql.org/about: “a powerful, open source object-relational database system.” Version 18 (September 2025) cited on the About page. |
| **ICT Provider?** | **None for community PostgreSQL.** Managed Postgres (Amazon RDS/Aurora, Azure Database for PostgreSQL, Cloud SQL, EnterpriseDB, Crunchy Bridge, etc.) has a provider. |
| **OSM encode** | **Not in catalog as itself.** Encode a relational-database Service; offerings per managed provider and `…self-operated`. Matches estate rows 14–16 (RDS, Azure SQL, Cloud SQL) vs row 43 (PostgreSQL the engine). |
| **Popularity only** | SO 2025: PostgreSQL “most desired and most admired” in its category since 2023. Not identity. |
| **Evidence** | A — postgresql.org/about. |

### A.15 MySQL

| | |
| --- | --- |
| **Kind** | **Product** (Community Edition project + Enterprise Edition). HeatWave is a **cloud technological service**. |
| **Vendor / steward** | Oracle (MySQL). Community governance model is published on mysql.com. |
| **Official identity** | mysql.com markets Community, Enterprise Edition, Cluster CGE, MySQL HeatWave, MySQL AI. |
| **ICT Provider?** | **Oracle** as `software-vendor` for Enterprise Edition; as `cloud-platform` / `managed-service` for HeatWave or MySQL HeatWave on AWS/OCI. Community binaries self-operated: no provider unless a support contract exists. |
| **OSM encode** | Same pattern as PostgreSQL. Do not catalog “MySQL.” Do not treat Oracle as the ICT Provider of every MySQL deployment. |
| **Evidence** | A — mysql.com. B — Community vs Enterprise vs HeatWave. |

### A.16 Microsoft SQL Server

| | |
| --- | --- |
| **Kind** | **Product** (editions: Enterprise, Standard, Developer, Express; SQL Server 2025 current on microsoft.com). Azure SQL Database / MI are **technological services**. SQL Server enabled by Azure Arc is hybrid management, not a new identity. |
| **Vendor** | Microsoft. |
| **ICT Provider?** | **Microsoft** as `software-vendor` for licensed SQL Server; as `cloud-platform` for Azure SQL. IaaS SQL on Azure VMs is compute (Microsoft) plus a SQL Server licence (Microsoft or BYOL) — two facts, one or two offerings. |
| **OSM encode** | Do not catalog “SQL Server.” Encode database Service offerings: `…sqlserver-self-operated`, `…azure-sql`. Estate already separates Azure SQL Database (row 15) from SQL Server (row 45). Keep that split. |
| **Evidence** | A — microsoft.com/en-us/sql-server. |

### A.17 Oracle Database

| | |
| --- | --- |
| **Kind** | **Product** (Oracle AI Database / Database). Autonomous AI Database and OCI/multicloud database services are **technological services**. |
| **Vendor** | Oracle. Official page (fetched 2026-09-13) brands “Oracle AI Database” / “Oracle AI Database 26ai.” Deployment options: OCI, multicloud (Azure, AWS, Google Cloud), Cloud@Customer, on-premises Exadata/ODA/Linux. |
| **ICT Provider?** | **Oracle** as `software-vendor` (on-prem licence) or `cloud-platform` / `managed-service` (Autonomous, Exadata Cloud@Customer). Multicloud: Oracle plus the hyperscaler — offering-level providers, not a Service→Service link. |
| **OSM encode** | Same as SQL Server. Estate already has OCI as a hyperscaler row and Oracle Database as a database product row. Do not merge them. |
| **Evidence** | A — oracle.com/database. B — which deployment option. |

### A.18 MongoDB

| | |
| --- | --- |
| **Kind** | **Product** (Community / Enterprise Server) and **technological service** (Atlas). |
| **Vendor** | MongoDB, Inc. SSPL v1 for versions after 2018-10-16 (mongodb.com). |
| **Official identity** | “MongoDB is a document database…” Server: Community and Enterprise. Cloud: Sandbox / Shared / Dedicated (Atlas). |
| **ICT Provider?** | **MongoDB, Inc.** as `managed-service` for Atlas; as `software-vendor` for Enterprise Server. Community self-operated: typically no provider. |
| **OSM encode** | Document-database Service; offerings `…atlas` (MongoDB) vs `…self-operated`. Do not catalog “MongoDB” as the Service name if the catalog already has a generic document-db Service. |
| **Evidence** | A — mongodb.com/company/what-is-mongodb. |

### A.19 Redis

| | |
| --- | --- |
| **Kind** | **Product** (in-memory database / cache) and **technological service** (Redis Cloud / Enterprise). |
| **Vendor** | Redis, Inc. License: RSALv2 or SSPLv1 (redis.io/about, fetched 2026-09-13). |
| **Official identity** | “Redis is the world’s fastest in-memory database. It provides cloud and on-prem solutions…” |
| **ICT Provider?** | **Redis, Inc.** for Cloud/Enterprise. Self-operated OSS/source-available Redis: no provider unless a Redis Enterprise contract exists. Hyperscaler “Redis” offerings (ElastiCache, Azure Cache, Memorystore) have the **hyperscaler** as ICT Provider, not Redis, Inc., unless the SKU is Redis Enterprise. |
| **OSM encode** | Cache / in-memory data Service; offerings per operator. Do not treat “Redis” as one provider. |
| **Popularity only** | SO 2025: Redis usage +8%. Not identity. |
| **Evidence** | A — redis.io/about. B — which licence/SKU/operator. |

### A.20 OpenSearch

| | |
| --- | --- |
| **Kind** | Open-source **project** (search, analytics, observability, vector DB). Amazon OpenSearch Service is a **technological service**. |
| **Steward** | OpenSearch Software Foundation under the Linux Foundation (AWS transferred the project 2024-09-16). Not AWS-owned as of that date. |
| **ICT Provider?** | **None for the project.** AWS is ICT Provider of Amazon OpenSearch Service. Other hosts (Aiven, etc.) are their own providers. |
| **OSM encode** | **Not in catalog as itself.** Search/analytics Service with offerings `…aws-opensearch-service`, `…self-operated`. Do not list AWS as provider of “OpenSearch the project.” Do not list Linux Foundation as ICT Provider. |
| **Evidence** | A — linuxfoundation.org press 2024-09-16; opensearch.org; LF 1-year anniversary 2025-08-25. |

### A.21 Apache Kafka

| | |
| --- | --- |
| **Kind** | Apache **project** / **distributed event-streaming platform**. Not a service. Not an ICT Provider. |
| **Steward** | Apache Software Foundation. kafka.apache.org: “an open-source distributed event streaming platform.” |
| **ICT Provider?** | **None for Apache Kafka.** Confluent Cloud, Amazon MSK, Azure Event Hubs (Kafka protocol), Redpanda, etc. are separate providers of streaming services. |
| **OSM encode** | Event-streaming Service; offerings per managed provider and `…self-operated`. Protocol compatibility (Kafka API) is a characteristic, not a Service→Service or provider fact. |
| **Evidence** | A — kafka.apache.org. |

### A.22 OpenTelemetry

| | |
| --- | --- |
| **Kind** | **Observability framework, specification, and protocol (OTLP).** Explicitly **not** an observability backend. Not a technological service. Not an ICT Provider. |
| **Steward** | CNCF project (merger of OpenTracing + OpenCensus). |
| **Official identity** | “OpenTelemetry is an observability framework and toolkit… OpenTelemetry is not an observability backend itself. The backend (storage) and the frontend (visualization) of telemetry data are intentionally left to other tools.” |
| **ICT Provider?** | **None.** Vendors that *support* OTLP (Datadog, Grafana, Dynatrace, etc.) are providers of **their** observability services, not of OpenTelemetry. |
| **OSM encode** | **Not in catalog.** If needed at all, OTLP support is a characteristic on an observability Service (`telemetry_protocol: otlp`). Creating `obs.opentelemetry` as a Service would mis-state OSM. |
| **Evidence** | A — opentelemetry.io/docs/what-is-opentelemetry. |

### A.23 Prometheus

| | |
| --- | --- |
| **Kind** | Open-source **project** — monitoring system and time-series database. CNCF graduated (second project to graduate after Kubernetes; accepted 2016-05-09, graduated 2018-08-09). |
| **ICT Provider?** | **None for upstream Prometheus.** Grafana Cloud, Amazon Managed Service for Prometheus, etc. are managed offerings with those vendors as providers. |
| **OSM encode** | **Not in catalog as itself.** Metrics/monitoring Service; offerings `…self-operated` vs `…managed-prometheus` (named vendor). PromQL compatibility can be a characteristic. |
| **Evidence** | A — prometheus.io; cncf.io/projects/prometheus. |

### A.24 Grafana

| | |
| --- | --- |
| **Kind** | **Project** (Grafana OSS) **and** **technological service** (Grafana Cloud) **and** **product** (Grafana Enterprise). |
| **Vendor** | Grafana Labs leads OSS development and sells Cloud and Enterprise. |
| **Official identity** | grafana.com/oss/grafana: OSS for users who “set up, administer, and maintain their own installation.” Cloud is “fully managed.” Enterprise is self-managed with commercial plugins. |
| **ICT Provider?** | **Grafana Labs** for Cloud (`managed-service`) and Enterprise (`software-vendor`). OSS self-operated: no provider. |
| **OSM encode** | Observability / visualisation Service; offerings `…oss-self-operated`, `…enterprise`, `…grafana-cloud`. Do not treat “Grafana” as one provider for every dashboard. |
| **Evidence** | A — grafana.com/oss/grafana. |

### Part A summary table

| Item | Kind | ICT Provider if any | OSM encode |
| --- | --- | --- | --- |
| Kubernetes | project / runtime | none (managed K8s: hyperscaler/Red Hat) | Service = managed/self-operated K8s; not the project |
| Docker | runtime + products | Docker, Inc. only for Hub/Desktop/hosted | not “Docker”; registry/runtime Services if needed |
| vSphere / VCF | product / private-cloud software | Broadcom (`software-vendor`); optional managed operator | VM / private-cloud IaaS Service |
| OpenShift | product + managed service | Red Hat ± hyperscaler | offering on K8s/app-platform Service |
| RHEL | OS product | Red Hat subscription only | not a Service |
| Ubuntu | OS product | Canonical only for Pro/managed | not a Service |
| Terraform | IaC tool + hosted product | IBM/HashiCorp for HCP/Enterprise | IaC Service (example already exists) |
| Ansible | automation product | Red Hat for AAP | automation Service |
| GitHub Actions | SaaS feature ± self-hosted runtime | GitHub | CI/CD offering |
| GitLab CI/CD | product feature + SaaS | GitLab | CI/CD offering |
| Jenkins | project | none (CloudBees if contracted) | CI/CD self-operated offering |
| Azure DevOps | suite of cloud/server services | Microsoft | one or many Services; do not flatten to “CI/CD” |
| Argo CD | project / Kubernetes controller | none unless managed GitOps vendor | CD self-operated offering |
| PostgreSQL | project / engine | none (managed: cloud vendor) | database Service offering |
| MySQL | product / engine | Oracle only for EE/HeatWave | database Service offering |
| SQL Server | product | Microsoft | database Service offering |
| Oracle Database | product + cloud service | Oracle | database Service offering |
| MongoDB | product + Atlas | MongoDB, Inc. for Atlas/EE | document-db Service offering |
| Redis | product + cloud | Redis, Inc. or hyperscaler cache | cache Service offering |
| OpenSearch | project | none (AWS for Amazon OpenSearch Service) | search Service offering |
| Apache Kafka | project | none (Confluent/MSK/…) | streaming Service offering |
| OpenTelemetry | framework / protocol | none | characteristic, not a Service |
| Prometheus | project | none (managed Prometheus vendors) | metrics Service offering |
| Grafana | OSS + Cloud + Enterprise | Grafana Labs for Cloud/EE | observability Service offering |

---

## Part B — generic estate rows (capabilities, not vendors)

These CSV rows are **capabilities**. They are valid OSM Services. They are not ICT Providers. Each should be **one Service with multiple provider-distinguished offerings**.

| Capability | CSV rank | What the Service is | Typical offerings (`providers` on offering) | DORA ITS type (illustrative, not stored in OSM) |
| --- | --- | --- | --- | --- |
| Enterprise Internet Connectivity | 75 | Access to the public Internet as a technological service | per carrier / transit / DIA circuit | S10 Telecom carrier (conditional) |
| WAN | 76 | Wide-area connectivity between sites | per carrier / MPLS / private backbone | S10 / S11 |
| SD-WAN | 77 | Software-defined WAN overlay | Cisco/VMware/Fortinet/Palo Alto/etc. or self-operated | S11 Network infrastructure (conditional) |
| DNS | 78 | Authoritative and/or recursive DNS | Infoblox, Route 53, Azure DNS, Cloudflare, self-operated | S11 or S19 depending on delivery |
| CDN | 79 | Content delivery / edge cache | Cloudflare, Fastly, Akamai, CloudFront, Azure Front Door | S19 or cloud edge (conditional) |
| Load Balancing | 80 | L4/L7 traffic distribution | hyperscaler LB, F5, Citrix, self-operated | S11 / S17–S19 |
| API Gateway | 81 | Ingress, authn/z, routing for APIs | AWS API GW, Azure APIM, Kong, Apigee, self-operated | S19 / S18 (conditional) |
| Network Firewall | 82 | Network-layer filtering / NGFW | Palo Alto, Fortinet, hyperscaler FW, self-operated | S04 / S11 (conditional) |
| VPN | 83 | Encrypted remote or site connectivity | Zscaler, Palo Alto, hyperscaler VPN, self-operated | S11 / S19 |
| Zero Trust Network Access | 84 | Identity-aware application access (not a classic VPN) | Zscaler, Entra Private Access, Cloudflare, Palo Alto Prisma | S04 / S19 |
| Enterprise API Management | 92 | Full API lifecycle (design, publish, productise) — broader than gateway | Apigee, Azure APIM, MuleSoft, Kong Enterprise | S19 |
| Enterprise AI/ML Platform | 93 | Train/host/operate ML systems | SageMaker, Vertex AI, Azure ML, Databricks, self-operated | S18 / S19; AI Act facts are separate |
| Generative AI / LLM Platform | 94 | Hosted or self-operated generative-model access | Azure OpenAI, Amazon Bedrock, Vertex, self-hosted | S19; AI Act GPAI vs system applies |

### How OSM should treat them

1. **One Service per capability**, not one Service per vendor. Example already: `net.enterprise-dns` with an Infoblox-backed offering. Same pattern for CDN, firewall, ZTNA.
2. **Offerings** distinguish provider, operating model (self-operated vs managed), and location/environment via characteristics.
3. **Do not** create ICT Providers named `dns`, `cdn`, `vpn`, or `ai-platform`.
4. **Criticality, RTO/RPO, data classification** for these rows are **C** — customer-dependent. Do not fill them as universal facts.
5. **DORA S01–S19** cannot be stored on the Service (`service_type` is intentionally not a core field; Technology Stack is the classification axis). Mapping a capability to S10 vs S11 vs S19 is a RoI filing fact, not an OSM field.

### Service → Service dependency (flag)

Several of these capabilities **depend on other technological services**:

- API Gateway and API Management typically depend on compute, identity, and often a CDN or firewall.
- SD-WAN / ZTNA / VPN depend on underlay connectivity and usually identity.
- Generative AI / LLM platforms depend on GPU/compute, identity, and often a data platform.
- Load balancing depends on the compute or application endpoints it fronts.

**OSM cannot represent those dependencies.** `SPECIFICATION.md` §1 and validation rule 13 put first-class Service→Service relationships out of scope. `providers[]` is only Service/Offering → ICT Provider. Reverse Provider→Service links are derived; they are not a dependency graph.

This is **intentional out-of-scope**, not a missing field to add during research. Record it as a decision-register candidate so adopters do not overload `providers` or characteristics to fake a CMDB relationship.

---

## Part C — Microsoft 365 suite decomposition

### Official identity (what Microsoft says)

Microsoft 365 for enterprise is a **complete solution / plan family**, not one protocol and not one runtime. Official components (`learn.microsoft.com` Microsoft 365 for enterprise overview):

- Local apps and cloud productivity services (Microsoft 365 Apps + online services for email, files, meetings).
- Windows 11 Enterprise (in E3/E5/F3 as applicable).
- Device management and advanced security (Intune, Defender for Endpoint, antispam/antimalware for email).

Plans: **E3, E5, F3** (plus Business / Education / Government SKUs). E5 adds Defender Suite, Purview Suite, advanced security/voice/analytics. E3 can buy Defender Suite and Purview Suite as add-ons.

Microsoft’s own service descriptions treat the suite as **a bundle of individually described services**:

| Name | Official kind | Notes |
| --- | --- | --- |
| **Microsoft 365** | Product **suite / subscription SKU** | Commercial packaging. Includes different service combinations by plan. Customers can buy components separately (Office 365 + Windows + EMS). |
| **Microsoft Teams** | Technological **service** (collaboration hub) | Built on Microsoft 365 groups, Graph, Entra ID. Creating a team creates a M365 group, SharePoint site, Exchange shared mailbox/calendar, OneNote. Separate admin center. Teams add-on licensing exists; some markets sell M365 with/without Teams. |
| **Exchange Online** | Technological **service** (hosted messaging) | Standalone plans Plan 1 / Plan 2 / Kiosk / Protection / Archiving. Mailboxes in Microsoft datacenters. Integrates with Entra ID. EWS deprecated (disablement from 2026-10-01, retirement 2027-04-01). |
| **SharePoint Online** | Technological **service** (content / intranet / files) | Standalone Plan 1 / Plan 2. Files in Teams are stored in SharePoint. Tight integration with Teams, Outlook, OneDrive. |
| **Microsoft Entra ID** | Technological **service** (cloud IAM) | “Foundational product of Microsoft Entra.” Every M365/Azure/Dynamics tenant is an Entra tenant. Also sold as Entra ID Free / P1 / P2 / Suite and inside M365/EMS. Entra is a **family** (ID, Domain Services, Private Access, Internet Access, ID Governance, ID Protection, External ID, Workload ID, Agent ID). |
| **Microsoft Defender** | **Product family**, not one service | Official page is **Microsoft Defender XDR**: coordinates Defender for Endpoint, Office 365, Identity, Cloud Apps, Vulnerability Management, Cloud, Entra ID Protection, DLP, etc. Licensing is per component. “Defender” in the CSV is not a single technological service. |

### One service or many?

**Many technological services; one commercial suite.**

OSM recommendation:

1. **Do not** encode Microsoft 365 as a single Service that “is” Teams + Exchange + SharePoint + Entra + Defender. That is a **product suite / SKU**, which OSM lists as out of scope (`digital products`, `Product Models`).
2. **Do** encode separate Services for the technological capabilities the enterprise actually governs, for example:
   - messaging / email (`…exchange-online`)
   - team collaboration (`…teams`)
   - content collaboration / intranet (`…sharepoint-online`)
   - identity and access (`…entra-id`) — estate already has row 27 Microsoft Entra ID
   - endpoint / email / identity threat protection as **separate** security Services, not one “Defender”
3. **Microsoft** is the ICT Provider (`cloud-platform` or `managed-service`) on those offerings. One provider record; many Services.
4. Suite SKU (E3 vs E5, Teams-included vs add-on) is a **characteristic or contract fact**, not a Service id. Contract dates/SKU belong on the ICT Provider contract fields or outside OSM — there is no SKU field.
5. **Runtime coupling is not representable.** Teams *uses* Entra ID, Exchange, and SharePoint. That is a Service→Service (and product-integration) dependency. OSM cannot store it. Do not put Entra, Exchange, and SharePoint in `providers[]` of Teams — they are not ICT Providers.
6. Entra ID is both a standalone identity Service and a **prerequisite control plane** for M365. Catalog it as identity, not as “part of Microsoft 365.”
7. Defender XDR is a **coordination layer over licensed components**. Encoding “Microsoft Defender” as one Service hides Endpoint vs Office 365 vs Identity vs Cloud Apps, which have different data, RTO, and DORA function mappings (all of those mappings are **C** anyway).

**Product suite vs technological services:** Microsoft 365 = suite. Teams, Exchange Online, SharePoint Online, Entra ID = technological services. Defender = family of technological services plus an XDR workspace.

Evidence: **A** — Microsoft Learn M365 enterprise overview; Exchange Online service description; Teams admin overview; SharePoint introduction; Entra “What is Microsoft Entra?”; Defender XDR overview; Microsoft 365 Enterprise licensing FAQ (components can be bought separately).

---

## Part D — regulation stress (primary sources)

OSM already declares it is not a DORA register, GDPR ROPA, ISMS, NIST profile, or AI Act technical file (`compliance/*.md`). This section maps **which facts exist** and **which required/contractual facts cannot be stored**.

### D.1 DORA — Regulation (EU) 2022/2554

**Source:** https://eur-lex.europa.eu/legal-content/ENG/ALL/?uri=CELEX:32022R2554  

Direct EUR-Lex HTML/TXT fetch timed out on 2026-09-13. Article 3(21) definition is quoted by the EBA Single Rulebook Q&A 2024_7290 (official EU supervisor):

> “ICT services” means digital and data services provided through ICT systems to one or more internal or external users on an ongoing basis, including hardware as a service and hardware services which includes the provision of technical support via software or firmware updates by the hardware provider, excluding traditional analogue telephone services.

Article 3(19) (via EIOPA Q&A DORA124-3169 citing the Regulation): **ICT third-party service provider** = an undertaking providing ICT services.

Article 28 is the third-party risk chapter (register of information, contractual principles). ITS 2024/2956 and RTS 2024/1773 are adopted under Article 28.

Evidence: **B** for 2022/2554 article text (supervisor quotation; primary page timed out). **A** for the existence and ELI of the act.

**Implication for Part A:** a self-operated PostgreSQL or Jenkins is usually **not** an ICT service *provided by an ICT third-party service provider*. A RHEL subscription can be DORA **S13 software licensing (excluding SaaS)**. GitHub Actions hosted is an ICT service. The OSM catalog can represent the technological service either way; it cannot represent the DORA legal characterisation.

### D.2 DORA RTS 2024/1773 (contractual-arrangement policy)

**Source (fetched):** https://eur-lex.europa.eu/eli/reg_del/2024/1773/oj  
Commission Delegated Regulation (EU) 2024/1773 of 13 March 2024, OJ L 2024/1773, 25.6.2024.  
ELI: http://data.europa.eu/eli/reg_del/2024/1773/oj  
Evidence: **A**.

This RTS specifies the **policy** on contractual arrangements for ICT services supporting **critical or important functions**. It is not the Register of Information (that is ITS 2024/2956). It requires the policy to cover, among other things:

- overall risk profile including **type of ICT services**, **location of provider / parent**, **location from which services are provided and where data is processed and stored**, third-country risk, intra-group vs external, concentration, **transferability**, impact of disruption (Art. 1);
- annual management-body review (Art. 3);
- methodology for determining which ICT services support critical or important functions (Art. 3(2));
- consistency with ICT risk-management framework, information-security policy, ICT BCP, incident-reporting (Art. 3(6));
- audit/access rights for the entity, its auditors, and competent authorities (Art. 3(8));
- lifecycle: planning, due diligence, implementation, monitoring, **documentation for the register of information (Art. 28(3) of 2022/2554)**, exit and termination (Art. 4);
- ex-ante risk assessment including operational, legal, ICT, reputational, confidentiality/personal data, availability, **location of processing/storage**, provider location, concentration (Art. 5);
- due diligence including **use of ICT subcontractors**, third-country processing, on-site audit consent, ethical/human-rights/environmental factors (Art. 6);
- conflicts of interest, including intra-group objectivity (Art. 7);
- written contractual clauses, KPIs/SLAs, incident reporting, exit (later articles).

Recital 11: the policy is **without prejudice to GDPR** (written processing contract, security of processing).

### D.3 DORA Register of Information — ITS (EU) 2024/2956

**Not the same act as 2024/1773.** RoI standard templates are Commission Implementing Regulation (EU) **2024/2956** (29 November 2024).  
Fetched: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402956  
Evidence: **A**.

Four keys that link RoI templates (recital 8):

1. **contractual arrangement reference number** (financial entity ↔ direct ICT third-party provider);
2. **identifier of financial entities and ICT third-party providers** (LEI and/or EUID);
3. **function identifier**;
4. **type of ICT services** (closed list S01–S19).

**`rank`** = position in the ICT service supply chain. Direct provider is always rank `1`. Subcontractors have rank `> 1` (Art. 1 definitions in the ITS).

Function identifier (template B_06.01): unique per combination of **financial entity LEI × licensed activity × function**.

ICT service types (Annex III) — identifier only may be reported:

| ID | Type |
| --- | --- |
| S01 | ICT project management |
| S02 | ICT Development |
| S03 | ICT help desk and first level support |
| S04 | ICT security management services |
| S05 | Provision of data |
| S06 | Data analysis |
| S07 | ICT, facilities and hosting services (excluding Cloud services) |
| S08 | Computation |
| S09 | Non-Cloud Data storage |
| S10 | Telecom carrier |
| S11 | Network infrastructure |
| S12 | Hardware and physical devices |
| S13 | Software licencing (excluding SaaS) |
| S14 | ICT operation management (including maintenance) |
| S15 | ICT Consulting |
| S16 | ICT Risk management |
| S17 | Cloud services: IaaS |
| S18 | Cloud services: PaaS |
| S19 | Cloud services: SaaS |

Templates B_01.01–B_07.01 plus B_99.01 cover entity, group, branches, contracts, signatories, providers, **supply chain**, functions, and CIF assessments.

### D.4 OSM fields that exist vs DORA facts that cannot be stored

| DORA / RoI / RTS fact | OSM field if any | Stores it? |
| --- | --- | --- |
| ICT third-party association | `providers[]` on Service/Offering | Partial — ids only, no LEI, no role (direct vs subcontractor), no rank |
| Provider legal name | ICT Provider `name` | Yes (string, not LEI) |
| **LEI / EUID** | — | **No** |
| Provider type (OSM enum) | `type` | Yes, but **not** S01–S19 |
| **ICT service type taxonomy S01–S19** | — (`service_type` intentionally absent) | **No** |
| **Function identifier** (LEI × licensed activity × function) | — | **No**. OSM has no licensed-activity or DORA function entity |
| Critical or important function | `operational_criticality`; stack `mappings.dora.criticality` | Partial and **wrong grain**. OSM criticality is the *service*, not the financial-entity function. Stack label is not the RoI function |
| RTO / RPO | offering `rto`, `rpo` | Yes (customer-dependent, class C) |
| Resilience testing | `resilience_tested`, `last_resilience_test`, `resilience_evidence` | Partial |
| Contract reference | `contract_ref` | Partial — one string per **provider**, not per contractual arrangement / service |
| Contract dates, notice | `contract_start`, `contract_end`, `notice_period_days` | Partial — provider grain, not arrangement×service grain |
| Audit rights | `audit_rights` | Boolean only; no scope, on-site, competent-authority access |
| Subcontracting allowed | `subcontracting_allowed` | Boolean / `conditional` |
| Subcontractor names | `subcontractors[]` | Names only — **no rank, no LEI, no chain, no “underpins CIF” flag** |
| **Supply-chain depth / rank** | — | **No** |
| Intra-group vs extra-group contract links (B_02.03) | — | **No** |
| Entity vs consolidating parent vs branch | — | **No** (org/legal-entity hierarchy out of scope) |
| Data processing / storage location (RTS Art. 1, 5) | `data_processing_locations` | Partial — provider-level list, not per service/arrangement/region |
| Exit strategy | `exit_strategy_documented`, `exit_strategy_tested` | Booleans only; no plan content, no transferability assessment |
| Concentration | `concentration_risk` | Boolean |
| Substitutability | `substitutability` | Yes (low/medium/high) — RoI B_07.01 has a related assessment; not equivalent |
| DORA notification clause | `dora_notification_clause` | Boolean only |
| Provider risk | `risk_level` | Yes — **not** service criticality |
| DORA pillar | stack `mappings.dora.pillar` | Stack label only |
| Register-of-information templates / filing | — | **No**. OSM says so in `compliance/DORA.md` |
| Policy annual review, due-diligence file, conflicts of interest, ethical/human-rights checks (RTS 1773) | — | **No** |
| Competent-authority cooperation clause | — | **No** |

### D.5 GDPR — controller vs processor; DPA

**Source:** Regulation (EU) 2016/679. EUR-Lex consolidated HTML fetched 2026-09-13.  
https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?from=EN&uri=CELEX:02016R0679-20160504  
Evidence: **A**.

Article 4(7): **controller** determines purposes and means of processing (alone or jointly).  
Article 4(8): **processor** processes personal data **on behalf of** the controller.  
Article 26: joint controllers.  
Article 28: processing by a processor **shall be governed by a contract or other legal act** (the DPA) setting out subject-matter, duration, nature and purpose, type of personal data, categories of data subjects, and obligations/rights of the controller; plus documented instructions, confidentiality, security (Art. 32), sub-processor rules, assistance with data-subject rights and Arts. 32–36, deletion/return, and audits. Art. 28(9): same obligations flow to sub-processors; initial processor remains liable. Art. 28(15): a processor that determines purposes and means becomes a controller for that processing.

| GDPR fact | OSM field | Stores it? |
| --- | --- | --- |
| Whether processing occurs | `gdpr_processing_activity` | Boolean, offering posture |
| DPIA signal | `gdpr_dpia_required` | Boolean — not a DPIA |
| Erasure capability | `gdpr_erasure_capable` | Coarse |
| Privacy class of the service | `privacy_classification` | Coarse |
| Controller / processor / joint | `iso27701_pii_role` | **Mis-labelled grain**: this is an ISO 27701 mapping on *offering posture*, not a GDPR Art. 4 determination. One enum cannot express “enterprise is controller, Microsoft is processor” plus “Microsoft is controller for some telemetry” |
| DPA exists | `gdpr_dpa_signed` | Boolean on **ICT Provider**, not per processing activity or per service |
| DPA contents (subject-matter, duration, data types, sub-processor list, TOMs, deletion, audit) | — | **No** |
| Legal basis | — | **No** |
| International transfers / SCCs / TIA | — | **No** |
| ROPA (Art. 30) | — | **No** |
| DPO | — | **No** |
| Sub-processor chain (Art. 28(2)/(9)) | `subcontractors[]` names only | **No** legal-role chain |

### D.6 ISO/IEC 27001 vs ISO/IEC 27701 — certification scope

ISO.org pages were blocked by Cloudflare on 2026-09-13 (D for iso.org HTML). Secondary official/accreditation sources:

- Microsoft Learn Azure ISO 27701 offering (describes **ISO/IEC 27701:2019**): 27701 is built as an extension of 27001/27002; “Certification for ISO/IEC 27701 must be obtained as an extension of an ISO/IEC 27001 certification and can't be obtained independently.” Evidence **B** (vendor compliance page, not ISO).
- ACCREDIA Technical Circular DC 39/2024: 27001 is a certifiable Type A HS standard; 27701 (as then in force) is certifiable **only as an extension** of 27001; standalone 27701 certificates are not permitted; certificate must reference the SoA. Evidence **B** (national accreditation body).
- Commercial commentary that **ISO/IEC 27701:2025** can be applied independently is **not treated as class A**. Edition year matters. Record as **B/D** until ISO.org or an IAF document is fetched.

OSM fields:

| Fact | OSM | Stores it? |
| --- | --- | --- |
| Annex A control IDs | `iso27001_controls`; stack `mappings.iso27001` | IDs only — **not** implementation evidence, **not** SoA |
| 27701 PII role / categories / retention | `iso27701_pii_*` | Characterisation, not a PIMS |
| Provider “has ISO 27001” | `certifications[]` free-form | **No scope**: missing legal entity, sites, services, statement of applicability, certificate number, validity dates, accredited CB |
| Provider 27701 as extension of 27001 | — | **No**. A string `iso27701` in `certifications` cannot record “extension of certificate X covering services Y in regions Z” |
| Last security review | `last_security_review` | Date only |

**Do not** treat a provider-level `iso27001` token as certification of every Service, region, or customer deployment (`TEMP/02` rule; OSM compliance docs).

### D.7 NIST CSF 2.0 — mapping, not certification

**Source (fetched):** NIST CSWP 29, 26 February 2024, https://doi.org/10.6028/NIST.CSWP.29  
NIST CSF site: https://www.nist.gov/cyberframework  
NIST CSF FAQ: https://www.nist.gov/cyberframework/faqs  

> “NIST does not offer certifications or endorsements of CSF-related products, implementations, or services, and there are no plans to develop a conformity assessment program.”

CSF 2.0 is a **taxonomy of high-level cybersecurity outcomes** (Functions: Govern, Identify, Protect, Detect, Respond, Recover). It does not prescribe how outcomes are achieved. Profiles and Tiers are organisational, not catalog fields.

OSM stores Function tags (`mappings.nist_csf`, offering `nist_functions`) and a coarse `nist_control_status`. It does **not** store Categories, Subcategories, current/target Profiles, or Tiers.

Evidence: **A**. Third-party “NIST CSF 2.0 certifications” (SCF CAP, HITRUST add-on) are **not NIST certifications**.

### D.8 EU AI Act — GPAI vs AI system vs provider vs deployer

**Source:** Regulation (EU) 2024/1689. Official Article 3 text via EC AI Act Service Desk (official version of 13 June 2024) and EUR-Lex OJ L 2024/1689.  
https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-3  
https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng  
Evidence: **A** for definitions.

| Term | Art. 3 | OSM field? |
| --- | --- | --- |
| **AI system** | machine-based system, varying autonomy, may adapt; infers outputs (predictions, content, recommendations, decisions) | Stack `contains_ai_systems`; service `ai_act_applicable` — **flag only**, not an AI-system register |
| **Provider** | develops or has developed an AI system or **GPAI model** and places it on the market or puts it into service under its name/trademark | **No role field.** ICT Provider is a technology vendor, not an AI Act provider |
| **Deployer** | uses an AI system under its authority (except personal non-professional use) | **No** |
| **GPAI model** | model with significant generality, trained at scale, integrable into downstream systems (research/prototype exception) | **No** |
| **GPAI system** | AI system based on a GPAI model, serving a variety of purposes | **No** distinction from “AI system” |
| Risk class | unacceptable / high / limited / minimal (OSM enum) | `ai_act_risk_class`, stack `max_risk_class` — **not a legal classification** |
| Intended purpose, oversight, transparency, conformity date, training-data doc | offering AI Act fields **only if** `ai_act_applicable: true` | Partial catalog metadata; not a technical file |
| Annex III high-risk taxonomy | — | **No** |
| Downstream provider | — | **No** |

Part B rows 93–94 (AI/ML platform, Generative AI/LLM platform) **cannot** record whether the enterprise is deployer of Azure OpenAI (GPAI system provided by Microsoft/OpenAI) or provider of an in-house model. That is a decision-register issue.

`compliance/EU-AI-ACT.md` already lists provider/deployer/manufacturer roles as staying in AI Act operations.

---

## Popularity evidence only (not identity)

| Source | Date | What it supports | What it must not be used for |
| --- | --- | --- | --- |
| [Stack Overflow Developer Survey 2025 — Technology](https://survey.stackoverflow.co/2025/technology) | 2025 | Docker near-universal (+17); Redis +8%; PostgreSQL most desired/admired in category since 2023 | Claiming any of those is an OSM Service or ICT Provider |
| [CNCF Annual Cloud Native Survey](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/) | Published 2026-01-20 | 82% of container users run Kubernetes in production | Claiming CNCF or Kubernetes is an ICT Provider |

Evidence class **A** as popularity surveys; they remain **non-identity**.

---

## Candidate decision-register issues

Open these only if reviewers agree the frozen model is insufficient or dangerously ambiguous. Options/recommendations are for the register, not for implementation in this investigation.

### D-OSG-001 — Project / runtime / protocol vs Service vs ICT Provider

- **Problem:** Estate rows name Kubernetes, Docker, Terraform, Ansible, Jenkins, Argo CD, PostgreSQL, Kafka, OpenTelemetry, Prometheus, Grafana, OpenSearch as if they were providers or services.
- **Evidence:** Official project/product pages (Part A); OSM `MODEL.md` Service and ICT Provider definitions; example `compute.kubernetes` already means *managed clusters*, not the CNCF project.
- **Why OSM is insufficient / ambiguous:** The model is semantically clear, but the estate (and many CMDB practices) will keep using product names as service names. There is no catalog field that says “this row is a product, not a Service.” ICT Provider `type` cannot be `project` or `foundation`. Documentation alone may not stop bad encoding.
- **Kind:** semantics + documentation (not necessarily schema).

### D-OSG-002 — Operating model (self-operated vs vendor-operated) is not a first-class field

- **Problem:** GitHub Actions hosted vs self-hosted, GitLab.com vs Self-Managed, Grafana OSS vs Cloud, OpenShift self-managed vs ROSA, Postgres self-operated vs RDS are different DORA facts (often S13 vs S19 / S18) and different `providers` patterns.
- **Evidence:** GitHub Actions docs; GitLab CI docs; Grafana OSS page; Red Hat OpenShift editions; DORA Annex III S13 vs S17–S19.
- **Why insufficient:** OSM can approximate via offering slug + omitted `providers` + a characteristic, but nothing prevents listing a software vendor on a self-operated offering and making the row look like a managed ICT service. No `operating_model` enum.
- **Kind:** schema (optional) vs documentation convention.

### D-OSG-003 — Service → Service dependency out of scope

- **Problem:** API Gateway depends on compute and identity; Teams depends on Entra, Exchange, SharePoint; LLM platform depends on GPU compute; ZTNA depends on identity.
- **Evidence:** Microsoft Teams architecture (Learn); OSM `SPECIFICATION.md` §1 and validation rule 13; Part B flag.
- **Why insufficient:** Adopters will misuse `providers[]` (putting Entra as a “provider” of Teams) or invent characteristics that fake a relationship. The model forbids the relationship and offers no approved external join key beyond ids.
- **Kind:** intentionally out of scope — record so it is not “fixed” ad hoc.

### D-OSG-004 — Capability Service vs vendor-named Service

- **Problem:** Rows 75–84 and 92–94 are capabilities; rows 1–7 and 57–74 are vendors/products. Mixing them in one estate invites encoding Cloudflare both as ICT Provider and as the CDN Service.
- **Evidence:** CSV structure; OSM example `net.enterprise-dns`; `MODEL.md` “do not turn this into a generic vendor/product inventory.”
- **Why insufficient:** No rule in the schema distinguishes a capability Service from a vendor-tied Service. `providers` on the Service vs Offering is documented but easy to invert.
- **Kind:** semantics + onboarding guidance.

### D-OSG-005 — Product suite vs technological services (Microsoft 365 and Azure DevOps)

- **Problem:** One SKU / portal name covers multiple technological services with different data, identity, and (for financial entities) DORA functions.
- **Evidence:** Microsoft 365 for enterprise overview; Exchange / Teams / SharePoint / Entra / Defender XDR service descriptions; Azure DevOps core services list.
- **Why insufficient:** OSM has no suite entity and forbids Product Models. Encoding M365 as one Service loses Exchange vs Teams vs Entra. Encoding five Services loses the commercial bundle and shared tenant. Contract fields sit on one ICT Provider, so E3 vs E5 vs add-on Defender Suite cannot be attached to the right Service.
- **Kind:** semantics; possible documentation pattern (suite as characteristic / external contract system).

### D-OSG-006 — DORA function identifier and licensed activity

- **Problem:** RoI B_06.01 requires a function identifier per LEI × licensed activity × function. OSM has no function entity and no legal-entity identifier.
- **Evidence:** ITS 2024/2956 recital 8, 10 and template B_06.01 (EUR-Lex fetch).
- **Why insufficient:** `operational_criticality` is service grain. Stack `mappings.dora.criticality` is stack grain. Neither is a DORA function. OSM explicitly does not model organisational or legal-entity hierarchy.
- **Kind:** intentionally out of scope for a technological-service catalog — but then OSM cannot be “the” DORA register.

### D-OSG-007 — LEI / EUID missing

- **Problem:** ITS Art. 2(5)–(6) require LEI or EUID for ICT third-party providers (and for CIF subcontractors).
- **Evidence:** ITS 2024/2956 official text.
- **Why insufficient:** ICT Provider `id` is a slug. `name` is a string. No ISO 17442 field.
- **Kind:** schema gap **if** OSM is expected to feed RoI; out of scope if RoI stays external.

### D-OSG-008 — ICT service type taxonomy S01–S19 missing

- **Problem:** RoI key (iv) is a closed 19-value taxonomy. OSM refuses a core `service_type` and uses Technology Stack instead. Stacks (Compute, Network, DevOps…) do not map 1:1 to S01–S19 (e.g. S13 software licensing vs S19 SaaS is operating-model, not stack).
- **Evidence:** ITS Annex III; `SPECIFICATION.md` design principle 5.
- **Why insufficient:** A RHEL subscription (S13) and GitHub Actions hosted (S19) might both be forced into a “DevOps” or “Compute” stack with no place to record the RoI type.
- **Kind:** mapping / out of scope vs optional mapping field (do not add during research).

### D-OSG-009 — Subcontracting chain depth and rank

- **Problem:** ITS defines `ICT service supply chain` and `rank`. RTS 2024/1773 Art. 6 requires assessing intended ICT subcontractors. OSM has `subcontractors: [names]` and `subcontracting_allowed`.
- **Evidence:** ITS 2024/2956 Art. 1 and template B_05.02; RTS 2024/1773 Art. 6(1)(c).
- **Why insufficient:** A name list cannot store rank, LEI, which service in the chain, or whether the subcontractor underpins a CIF. Intra-group reconciliation (B_02.03) is impossible.
- **Kind:** schema gap relative to RoI; OSM already says fields are not a filing.

### D-OSG-010 — Contract grain is provider, not arrangement × service

- **Problem:** RoI keys contracts by arrangement reference and links them to ICT service types and functions. OSM stores one `contract_ref` / dates / notice / audit flag **per ICT Provider**.
- **Evidence:** ITS templates B_02.01, B_02.02; OSM ICT Provider schema.
- **Why insufficient:** Microsoft will have many contractual arrangements (M365, Azure, Premier support) underpinning many Services. One provider row cannot hold them. GitHub Actions and GitHub Enterprise Cloud may share a provider with different contracts.
- **Kind:** schema / external-system join.

### D-OSG-011 — GDPR DPA and controller/processor roles

- **Problem:** Art. 28 DPA is a contract with mandatory content. OSM has `gdpr_dpa_signed` (provider boolean) and `iso27701_pii_role` (offering enum).
- **Evidence:** GDPR Arts. 4 and 28 (EUR-Lex consolidated); OSM posture and ICT Provider schemas.
- **Why insufficient:** Cannot record who is controller vs processor **per processing activity**, joint-controller arrangements, DPA subject-matter, or that Microsoft is processor for customer content and controller for some service-generated data (common M365/Azure pattern — the split itself is **C/B** and must not be invented per tenant).
- **Kind:** intentionally thin mapping; dangerous if treated as ROPA.

### D-OSG-012 — ISO certification scope vs `certifications[]`

- **Problem:** 27001/27701 certificates are scoped (entity, sites, SoA, services). 27701:2019 is an extension of 27001. OSM `certifications` is a free-form string list.
- **Evidence:** ACCREDIA DC 39/2024; Microsoft Learn ISO 27701 offering; OSM ICT Provider schema; `compliance/ISO-27001.md`.
- **Why insufficient:** `certifications: [iso27001, iso27701]` claims nothing about scope and invites the exact error the investigation forbids (provider cert ≠ every service/region).
- **Kind:** documentation + possible structured certification object (not to be added now).

### D-OSG-013 — NIST CSF tagged as if it were a certification

- **Problem:** Offering `nist_control_status: implemented` plus `nist_functions` can be misread as “NIST CSF certified.”
- **Evidence:** NIST CSF FAQ (no NIST certification programme); CSWP 29; `compliance/NIST-CSF.md`.
- **Why insufficient:** The fields exist and look like control status. The spec says they are mappings, but the schema does not say “not a certification.”
- **Kind:** documentation / semantics.

### D-OSG-014 — EU AI Act roles and GPAI vs system

- **Problem:** Estate rows 93–94 and any Copilot/OpenAI-backed offering need provider vs deployer and GPAI model vs AI system. OSM has applicability + risk class + five offering fields.
- **Evidence:** AI Act Art. 3(1), (3), (4), (63), (66); `compliance/EU-AI-ACT.md`.
- **Why insufficient:** No role, no GPAI flag, no model-vs-system, no downstream-provider. ICT Provider cannot play “AI Act provider.”
- **Kind:** intentionally out of scope for roles; schema gap if catalog must distinguish GPAI platforms.

### D-OSG-015 — Name collisions (Docker, Defender, Redis, OpenSearch, Terraform)

- **Problem:** One estate token refers to multiple legal and delivery objects (see Part A).
- **Evidence:** Docker overview vs Desktop vs Hub; Defender XDR component list; Redis Inc. vs hyperscaler Redis-compatible caches; OpenSearch Foundation vs Amazon OpenSearch Service; Terraform CLI vs HCP vs IBM Self-Managed.
- **Why insufficient:** OSM identity is a slug. Nothing prevents `id: docker` as an ICT Provider that then gets attached to every container host.
- **Kind:** onboarding / naming guidance.

### D-OSG-016 — Data-processing location grain

- **Problem:** RTS 2024/1773 Art. 1(c) and Art. 5 require location of provision and of processing/storage, including third-country risk. OSM `data_processing_locations` is a provider-level string list.
- **Evidence:** RTS 2024/1773 official text; ICT Provider schema.
- **Why insufficient:** M365, Azure, and GitHub have per-service, per-tenant, per-region processing. A provider-level `["eu","us"]` is not a DORA location fact.
- **Kind:** grain mismatch; customer-dependent (C) for actual tenant residency.

### D-OSG-017 — Reference CSV is 94 rows, methodology says ~100

- **Problem:** Filename and Phase 1 text say 100; file has 94.
- **Evidence:** CSV row count (A).
- **Why insufficient:** Not an OSM schema issue. Process/lock-file inconsistency. Do not pad the universe.
- **Kind:** investigation process.

---

## Sources

### OSM (frozen)

- `/Users/mjovanovic/Documents/open-servicecatalog-model/MODEL.md`
- `/Users/mjovanovic/Documents/open-servicecatalog-model/SPECIFICATION.md` (v1.3.0)
- `schema/catalog/ict-provider.yaml`, `schema/catalog/service.yaml`, `schema/posture/service-posture.yaml`
- `compliance/DORA.md`, `compliance/GDPR.md`, `compliance/ISO-27001.md`, `compliance/ISO-27701.md`, `compliance/NIST-CSF.md`, `compliance/EU-AI-ACT.md`
- `examples/catalog/services.yaml` (`compute.kubernetes`, `net.enterprise-dns`, `devops.continuous-delivery`, `auto.infrastructure-as-code`)
- `TEMP/01_reference_estate_100.csv` (94 rows), `TEMP/02_investigation_methodology.md`

### Part A — official product / project pages (fetched 2026-09-13 unless noted)

- https://kubernetes.io/
- https://www.cncf.io/projects/kubernetes/
- https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/
- https://docs.docker.com/get-started/docker-overview/
- https://www.docker.com/products/docker-desktop/
- https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/overview-of-vmware-cloud-foundation-9/what-is-vmware-cloud-foundation-and-vmware-vsphere-foundation.html
- https://www.vmware.com/docs/vmware-vsphere-foundation-feature-comparison
- https://www.broadcom.com/company/news/product-releases/64326
- https://www.redhat.com/en/technologies/cloud-computing/openshift
- https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux
- https://www.redhat.com/en/technologies/management/ansible
- https://ubuntu.com/
- https://www.terraform.io/
- https://github.com/hashicorp/terraform/blob/HEAD/LICENSE
- https://www.ibm.com/support/pages/node/7184927
- https://docs.github.com/en/actions
- https://docs.gitlab.com/ci/
- https://www.jenkins.io/
- https://www.jenkins.io/project/governance/
- https://learn.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops
- https://argo-cd.readthedocs.io/en/stable/
- https://www.cncf.io/projects/argo/
- https://www.postgresql.org/about/
- https://www.mysql.com/
- https://www.microsoft.com/en-us/sql-server
- https://www.oracle.com/database/
- https://www.mongodb.com/company/what-is-mongodb
- https://redis.io/about/
- https://opensearch.org/
- https://www.linuxfoundation.org/press/linux-foundation-announces-opensearch-software-foundation-to-foster-open-collaboration-in-search-and-analytics
- https://kafka.apache.org/
- https://opentelemetry.io/docs/what-is-opentelemetry/
- https://prometheus.io/
- https://www.cncf.io/projects/prometheus/
- https://grafana.com/oss/grafana/
- https://survey.stackoverflow.co/2025/technology

### Part C — Microsoft

- https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-overview
- https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-platform-service-description/office-365-plan-options
- https://learn.microsoft.com/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-service-description
- https://learn.microsoft.com/en-us/microsoftteams/teams-overview
- https://learn.microsoft.com/en-us/sharepoint/introduction
- https://learn.microsoft.com/en-us/entra/fundamentals/whatis
- https://learn.microsoft.com/en-us/microsoft-365/security/defender/microsoft-365-defender
- https://www.microsoft.com/en-us/licensing/product-licensing/microsoft-365-enterprise

### Part D — regulation

- DORA 2022/2554: https://eur-lex.europa.eu/legal-content/ENG/ALL/?uri=CELEX:32022R2554 (primary URL; full-text fetch timed out; definition via EBA Q&A 2024_7290)
- EBA Q&A 2024_7290: https://www.eba.europa.eu/single-rule-book-qa/qna/view/publicId/2024_7290
- DORA RTS 2024/1773: https://eur-lex.europa.eu/eli/reg_del/2024/1773/oj (fetched)
- DORA ITS RoI 2024/2956: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402956 (fetched)
- GDPR 2016/679 consolidated: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?from=EN&uri=CELEX:02016R0679-20160504 (fetched)
- NIST CSF 2.0 CSWP 29: https://doi.org/10.6028/NIST.CSWP.29 (fetched)
- NIST CSF site: https://www.nist.gov/cyberframework
- NIST CSF FAQ: https://www.nist.gov/cyberframework/faqs
- EU AI Act Art. 3: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-3
- EU AI Act OJ: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- Microsoft Learn ISO 27701: https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-iso-27701
- ACCREDIA DC 39/2024 (27001/27701 accreditation): https://accredia.it/wp-content/uploads/2024/11/Circolare_tecnica_DC_39-2024_ENG-Accreditation-ISOIEC-17021-1-against-ISOIEC-27001-e-ISOIEC-27701.pdf

### Fetch failures (do not cite as verified page content)

- iso.org 27001/27701 product pages — Cloudflare challenge (D).
- ansible.com — HTTP 409 (used Red Hat AAP page instead).
- EUR-Lex 32022R2554 and 32024R1773 alternate TXT URLs — timeout (1773 succeeded via ELI HTML).

---

## What this note does not do

- Does not add OSM fields.
- Does not populate customer-dependent criticality, RTO/RPO, classification, or risk as universal facts.
- Does not claim any provider, project, or suite is DORA/GDPR/ISO/AI-Act compliant.
- Does not treat Stack Overflow or CNCF survey results as identity.
- Does not invent the six missing estate rows.
