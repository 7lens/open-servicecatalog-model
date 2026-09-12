# ArchiMate

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (model / taxonomy / architectural framework)
- **OSM schema fields today:** none dedicated to ArchiMate

Do not treat this file as a mapping.

## 1. Model overview

ArchiMate (The Open Group) is an enterprise-architecture modeling
language. It distinguishes **Business Service**, **Application
Service** and **Technology Service**, plus serving / realization
relationships across business, application and technology layers.

## 2. Scope

In scope for a later OSM comparison: whether OSM Service corresponds
to ArchiMate **Technology Service** (or a related technology-layer
element).

Out of scope for OSM: ArchiMate business and application layers as
OSM entities.

## 3. OSM concepts potentially corresponding to the model

NOT YET ANALYZED.

Candidates to compare later (not mappings):

| OSM (current) | ArchiMate concept to inspect |
|---------------|------------------------------|
| Service | Technology Service (possible) |
| Service Offering | Uncertain (no direct standard element) |
| Technology Stack | Uncertain (grouping / capability / device — unknown) |
| ICT Provider | External actor / serving relationship (uncertain) |

## 4. Attribute compatibility

NOT YET ANALYZED.

ArchiMate is light on operational attributes (lifecycle, RTO, cost
pool). OSM health-record fields may have no ArchiMate counterpart.

## 5. Relationship compatibility

NOT YET ANALYZED.

## 6. Terminology differences

NOT YET ANALYZED.

Likely tension: in ArchiMate, "service" is layered. In OSM, Service
always means technological service.

## 7. Gaps

NOT YET ANALYZED.

## 8. Potential extensions

None proposed. No attributes are added in this baseline.

## 9. Decisions still required

- Whether OSM should ever expose an ArchiMate element-type mapping
- Whether Technology Stack is an architecture grouping or an
  operating-model concept that ArchiMate should not absorb

## 10. Compatibility status

**NOT ANALYZED**
