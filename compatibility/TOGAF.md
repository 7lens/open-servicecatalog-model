# TOGAF

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (model / taxonomy / architectural framework)
- **OSM schema fields today:** optional `mappings.togaf_domain` on Technology Stack

The existing field is a free-text **reference mapping** on stacks.
It is not a completed TOGAF compatibility analysis and not a claim
that OSM is a TOGAF method.

## 1. Model overview

TOGAF (The Open Group Architecture Framework) is an architecture
method and content framework. It is commonly discussed in terms of
architecture domains such as Business, Data, Application and
Technology, plus a wider ADM and content metamodel.

## 2. Scope

In scope for a later OSM comparison: whether OSM records can be
placed in a TOGAF technology (and possibly data) architecture
conversation without OSM becoming an architecture method.

Out of scope for OSM: TOGAF ADM phases, capability models, and
application architecture as OSM entities.

## 3. OSM concepts potentially corresponding to the model

NOT YET ANALYZED.

Candidates to compare later (not mappings):

| OSM (current) | TOGAF concept to inspect |
|---------------|--------------------------|
| Technology Stack | Technology architecture grouping / domain (possible) |
| Service | Technology service / architecture building block (uncertain) |
| Service Offering | Uncertain |
| `mappings.togaf_domain` | Informal domain label only |

Examples currently store values such as "Technology Architecture"
and "Data Architecture". Those strings are illustrative.

## 4. Attribute compatibility

NOT YET ANALYZED.

Current OSM field: `technology_stacks[].mappings.togaf_domain` (string).

## 5. Relationship compatibility

NOT YET ANALYZED.

## 6. Terminology differences

NOT YET ANALYZED.

Likely tension: TOGAF "service" is not limited to technological
services. OSM is.

## 7. Gaps

NOT YET ANALYZED.

`togaf_domain` exists only on stacks, not on services or offerings.
Whether that grain is correct is a later decision.

## 8. Potential extensions

None proposed. Do not add service-level TOGAF fields in this task.

## 9. Decisions still required

- Whether `togaf_domain` should remain stack-only
- Whether OSM should reference TOGAF content metamodel elements by
  name, or only informal domain labels
- How to keep OSM from being read as "the TOGAF service model"

## 10. Compatibility status

**NOT ANALYZED**
