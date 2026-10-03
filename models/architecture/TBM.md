# TBM

**Mapped version:** **TBM Taxonomy 5.0.1** (July 2025).

> **Mapping basis (2026-06-11):** TBM Taxonomy 5.0.1 is confirmed as
> the current release, published by the TBM Council Standards
> Committee —
> [the TBM Council taxonomy page describes 5.0.x as the global
> standard spanning cost, resources, solutions and consumers](https://www.tbmcouncil.org/taxonomy/),
> and the
> [TBM Council resource-center entry dates the 5.0.1 paper to
> July 2025](https://www.tbmcouncil.org/learn-tbm/resource-center/the-tbm-taxonomy-5/).
> A notable 5.0.1 change is that Applications are modeled within the
> **Technology Tower** layer rather than the Solutions taxonomy
> ([TBM Council taxonomy page](https://www.tbmcouncil.org/taxonomy/)).
> The full canonical Resource-Tower name list lives in the gated
> 5.0.1 whitepaper and downloadable data tables, so individual tower
> labels below are illustrative and the complete L1/L2 enumeration is
> treated as **unverified at 2026-06-11 (sources consulted: TBM
> Council taxonomy and resource-center pages; the 5.0.1 whitepaper
> data tables are not openly extractable)**. Source wording was
> rephrased for licensing compliance.

**Status:** **MAPPED** (stack-level Technology Resource Tower labels)

OSM is **not** a TBM cost model, allocation engine, or TBM Council
taxonomy. OSM does not introduce a full TBM financial/resource
taxonomy.

TBM Taxonomy 5.0.1 names **Technology Resource Towers** (not
“IT Tower”). Mapping stays **primarily at Technology Stack**.
Do **not** add Service-level TBM mappings merely because TBM has a
Solutions layer. That can be a mapping extension later if a customer
integration requires it.

A Technology Stack is an operational competency domain, not a chart
of accounts. Optional labels let finance *map* to stacks without
turning OSM into TBM.

## Concept walk (TBM Taxonomy 5.0.1 layers)

Every top-level TBM 5.0.1 layer below carries a status from the index
vocabulary (MAPPED / PARTIAL / EXTERNAL / NOT IN SCOPE / FUTURE /
OPTIONAL), so none is silently missing.

| TBM 5.0.1 layer / concept | OSM target | Status + kind | Outside OSM |
|---------------------------|------------|---------------|-------------|
| Cost Pools layer | `cost_pool` (offering posture) | **MAPPED** — characterization only, not an allocation model. | Allocation mathematics, GL mapping |
| Technology Resource Towers (incl. Applications in 5.0.1) | `mappings.tbm_tower` on Technology Stack | **MAPPED** — partial label at stack grain. | Full tower catalogue, allocation rules |
| Resource Tower Sub-towers | `mappings.tbm_sub_tower` on Technology Stack | **MAPPED** — partial label; full L2 taxonomy stays external. | Full L2 sub-tower taxonomy |
| Solutions layer (incl. AI, Sustainability & ESG) | — | **NOT IN SCOPE** — do not add Service-level TBM fields for this. | Solutions taxonomy |
| Consumer layer | — | **EXTERNAL** — business/consumer alignment belongs to TBM, not OSM. | Consumer/business layer |
| Chargeback / showback operating model | `chargeback_model` (offering posture) | **MAPPED** — characterization only; the operating model stays external. | Showback operating model |
| Cost allocation math / general-ledger integration | — | **EXTERNAL** — OSM is not a cost engine. | Allocation engine, GL feeds |

## Mapping table

| External concept (Taxonomy 5.0.1) | OSM target | Grain | Status + kind | Outside OSM |
|-----------------------------------|------------|-------|---------------|-------------|
| Technology Resource Tower | `mappings.tbm_tower` | **Technology Stack** | **MAPPED** — partial label. Illustrative names in examples are not a TBM catalog. | Full tower catalogue, Platform tower (retired) |
| Sub-tower | `mappings.tbm_sub_tower` | Stack | **MAPPED** — partial label | Full L2 taxonomy |
| Solutions layer (incl. AI, Sustainability & ESG) | — | — | **NOT IN SCOPE** for current OSM mapping. Do not add Service-level TBM fields for this. | Solutions taxonomy |
| Consumer Layer | — | — | **EXTERNAL** | TBM consumer/business layer |
| Cost Pools | `cost_pool` | Offering posture | **MAPPED** — characterization only | Allocation mathematics |
| Chargeback / consumption pattern | `chargeback_model` | Offering posture | **MAPPED** — characterization | Showback operating model |
| TBM cost “service” | OSM Service is **not** this | Service | **EXTERNAL** — different job: technological service vs cost object | TBM cost engine |

Example Resource Tower names from 5.0.1 include Compute, Storage,
Network, Data, Security and Application. Older example strings such
as “Infrastructure” or “Management” are **illustrative only** and are
**not** Taxonomy 5.0.1 tower names.

## What stays in TBM (**EXTERNAL**)

- allocation mathematics
- general-ledger integration
- a required TBM taxonomy as OSM structure
- showback / chargeback operating model beyond OSM characterization
- the full Solutions and Consumer layers as OSM entities

TBM “service” is cost-oriented. OSM Service is a technological
service with operational ownership. Those are different jobs.

Exact field definitions are in
[`SPECIFICATION.md`](../../SPECIFICATION.md).
