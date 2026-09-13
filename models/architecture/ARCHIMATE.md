# ArchiMate

OSM is **not** an ArchiMate model, viewpoint set, or architecture
repository.

ArchiMate (The Open Group) is an enterprise-architecture modeling
language. It distinguishes **Business Service**, **Application
Service** and **Technology Service**, plus serving and realization
relationships across those layers.

OSM Service is the canonical **technological service** definition.
That is the natural ArchiMate landing.

## What maps

| OSM | ArchiMate | How they relate |
|-----|-----------|-----------------|
| Service | Technology Service | Conceptually the closest element. OSM Service is a definition, not a runtime object and not a layered architecture element. |
| Service Offering | — | No required ArchiMate twin. Offering variation stays in OSM. |
| Technology Stack | — | Operational ownership domain. Not absorbed as an ArchiMate grouping, capability or device. |
| ICT Provider | External actor / serving | Provider association stays as OSM `providers` → ICT Provider. Architecture views of serving relationships live in ArchiMate. |

There are no ArchiMate-specific schema fields.

## What stays in ArchiMate

- Business Service and Application Service
- serving and realization relationships
- architecture views and viewpoints
- operational attributes that ArchiMate does not model (lifecycle,
  RTO/RPO, cost characterization)

In ArchiMate, “service” is layered. In OSM, Service always means
technological service. Join OSM records to an architecture
repository when you need the other layers.
