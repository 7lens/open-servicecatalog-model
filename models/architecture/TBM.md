# TBM

**Mapped version:** **TBM Taxonomy 5.0.1** (18 July 2025).

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

## Mapping table

| External concept (Taxonomy 5.0.1) | OSM target | Grain | Kind | Outside OSM |
|-----------------------------------|------------|-------|------|-------------|
| Technology Resource Tower | `mappings.tbm_tower` | **Technology Stack** | Partial label. Illustrative names in examples are not a TBM catalog. | Full tower catalogue, Platform tower (retired) |
| Sub-tower | `mappings.tbm_sub_tower` | Stack | Partial label | Full L2 taxonomy |
| Solutions layer (incl. AI, Sustainability & ESG) | — | — | **NOT IN SCOPE** for current OSM mapping. Do not add Service-level TBM fields for this. | Solutions taxonomy |
| Consumer Layer | — | — | **EXTERNAL** | TBM consumer/business layer |
| Cost Pools | `cost_pool` | Offering posture | Characterization only | Allocation mathematics |
| Chargeback / consumption pattern | `chargeback_model` | Offering posture | Characterization | Showback operating model |
| TBM cost “service” | OSM Service is **not** this | Service | Different job: technological service vs cost object | TBM cost engine |

Example Resource Tower names from 5.0.1 include Compute, Storage,
Network, Data, Security, Application, Risk & Compliance. Older
example strings such as “Infrastructure” or “Management” are
**illustrative only** and are **not** Taxonomy 5.0.1 tower names.

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
