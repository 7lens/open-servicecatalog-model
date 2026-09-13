# TBM

OSM is **not** a TBM cost model, allocation engine, or TBM Council
taxonomy.

TBM (Technology Business Management) is a financial-management
taxonomy for technology spend. OSM is a catalog of technological
services with **operational** ownership.

A Technology Stack is an operational competency domain, not a chart
of accounts. Optional labels let finance *map* to stacks without
turning OSM into TBM.

## What maps

| OSM field | Where | Typical TBM use |
|-----------|--------|-----------------|
| `mappings.tbm_tower` | Technology Stack | IT Tower (L1) |
| `mappings.tbm_sub_tower` | Technology Stack | Sub-Tower (L2) |
| `cost_pool` | Offering posture | Cost-pool characterization |
| `chargeback_model` | Offering posture | Shared / dedicated / consumption pattern |
| Service | — | OSM Service is a technological capability, not a TBM cost service |
| Service Offering | — | Requestable variant; cost signals sit on offering posture |

Example tower names such as Infrastructure, Security or Data
Management are illustrative. They are not a TBM catalog.

## What stays in TBM

- allocation mathematics
- general-ledger integration
- a required TBM taxonomy version
- showback / chargeback operating model beyond the OSM
  characterization fields

TBM “service” is cost-oriented. OSM Service is a technological
capability with operational ownership. Those are different jobs.

Exact field definitions are in
[`SPECIFICATION.md`](../../SPECIFICATION.md).
