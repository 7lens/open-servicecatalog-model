# Models and frameworks

OSM is the **canonical technological-service core**.

It does not replace specialized service, catalog or architecture
models. It gives an enterprise a stable place to own the definition
of what its technology organization delivers, then map richer
frameworks onto that core.

```
OSM canonical core
        ↓
semantic mapping
        ↓
ITIL / TM Forum / CSDM / TOGAF / ArchiMate / TBM
        ↓
customer tools and systems
```

Compatibility means an adopter can relate OSM records to another
model without inventing a private translation for every field.
It does **not** mean OSM implements, certifies or replaces that
model.

A framework must not drive a new OSM field simply because it uses a
different name. If OSM already represents the concept, reuse that
field.

Regulatory, security, privacy and control mappings live in
[`compliance/`](../compliance/).

Exact field definitions are in [`SPECIFICATION.md`](../SPECIFICATION.md).

---

## Service management and catalogs

| Model | Role beside OSM |
|-------|-----------------|
| [ITIL](service-management/ITIL.md) | Service management and operational excellence |
| [TM Forum TMF633](service-management/TMFORUM-TMF633.md) | Richer catalog, commercial and service concepts |
| [ServiceNow CSDM](service-management/CSDM.md) | ServiceNow-oriented service and CMDB modeling |

## Architecture and technology finance

| Model | Role beside OSM |
|-------|-----------------|
| [TOGAF](architecture/TOGAF.md) | Architecture method; OSM records can be labelled, not replaced |
| [ArchiMate](architecture/ARCHIMATE.md) | Architecture language; OSM Service maps to the technology layer |
| [TBM](architecture/TBM.md) | Technology financial management; optional tower and cost labels |
