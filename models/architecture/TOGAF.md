# TOGAF

OSM is **not** a TOGAF method, ADM implementation, or architecture
content metamodel.

TOGAF (The Open Group Architecture Framework) is an architecture
method. OSM is a small machine-readable catalog of **technological**
services. The two work together: OSM holds the canonical service
definition; TOGAF describes how an architecture practice plans,
governs and communicates the wider estate.

## What maps

| OSM | TOGAF | How they relate |
|-----|-------|-----------------|
| Technology Stack | Technology architecture grouping | A stack is an **operational competency domain**. It may be discussed as part of technology architecture; it is not a TOGAF entity. |
| Service | Technology service / building block | OSM Service is the stable definition of a technological service. TOGAF “service” is broader and is not limited to technological services. |
| Service Offering | — | Variant grain stays in OSM. Do not import TOGAF catalog hierarchy. |
| `mappings.togaf_domain` | Architecture domain label | Optional free-text reference on a stack (examples use values such as “Technology Architecture” and “Data Architecture”). A translation hint, not a TOGAF building block. |

## What stays in TOGAF

- ADM phases and architecture governance
- capability models
- application architecture as OSM entities
- the TOGAF content metamodel

OSM does not implement those. Join OSM records to an architecture
repository when you need them.

The `togaf_domain` mapping sits on Technology Stack, not on Service
or Offering. Exact field definitions are in
[`SPECIFICATION.md`](../../SPECIFICATION.md).
