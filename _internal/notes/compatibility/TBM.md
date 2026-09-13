# TBM (Technology Business Management)

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (model / taxonomy / architectural framework)
- **OSM schema fields today:** optional `mappings.tbm_tower`,
  `mappings.tbm_sub_tower` on Technology Stack; optional
  `cost_pool` and `chargeback_model` on offering attributes

These fields are **reference mappings / operational hints**. They are
not a completed TBM compatibility analysis and not a TBM Council
endorsement.

## 1. Model overview

TBM is a financial-management taxonomy and operating model for
technology spend. It commonly uses towers, sub-towers, cost pools
and a service taxonomy used by finance and technology leaders to
talk about cost.

OSM already states that a Technology Stack is an **operational**
ownership domain, **not** a financial taxonomy. TBM mappings, if
kept, are a translation layer.

## 2. Scope

In scope for a later OSM comparison: whether OSM stacks, services
and offerings can be labelled against TBM towers / cost ideas
without turning OSM into a chart of accounts.

Out of scope for OSM: a full TBM cost model, allocation math, or
GL integration.

## 3. OSM concepts potentially corresponding to the model

NOT YET ANALYZED.

Candidates to compare later (not mappings):

| OSM (current) | TBM concept to inspect |
|---------------|------------------------|
| Technology Stack | Tower / sub-tower (possible, but OSM says stacks are not a financial taxonomy) |
| Service | TBM service (uncertain) |
| Service Offering | TBM service offering (uncertain) |
| `cost_pool` | TBM cost pool (name collision; not yet analyzed) |
| `chargeback_model` | Showback / chargeback pattern (uncertain) |

## 4. Attribute compatibility

NOT YET ANALYZED.

Current OSM fields that mention TBM language:

- `tbm_tower`, `tbm_sub_tower` (stack)
- `cost_pool`, `chargeback_model` (offering attributes)

Examples use illustrative tower names such as Infrastructure,
Security, Data Management. Those values are not a TBM catalog.

## 5. Relationship compatibility

NOT YET ANALYZED.

## 6. Terminology differences

NOT YET ANALYZED.

Likely tension: TBM "service" is cost-oriented. OSM Service is a
technological capability with operational ownership.

## 7. Gaps

NOT YET ANALYZED.

TBM labels sit on stacks today, not on services. Whether that is
the right grain is a later decision.

## 8. Potential extensions

None proposed. No attributes are added in this baseline.

## 9. Decisions still required

- Keep TBM as optional labels vs. require a TBM taxonomy version
- Stack-level vs service-level TBM mapping
- Whether `cost_pool` should stay free text

## 10. Compatibility status

**NOT ANALYZED**
