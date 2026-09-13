# Models and frameworks

OSM is the **canonical technological-service core**.

It does not replace specialized service, catalog or architecture
models. It gives an enterprise a stable place to own the definition
of its technological services, then map richer frameworks onto that
core.

```
OSM canonical core
        ↓
semantic mapping
        ↓
ITIL / TM Forum / CSDM / TOGAF / ArchiMate / TBM
        ↓
customer tools and systems
```

Compatibility means an adopter can **map** OSM records to another
model without inventing a private translation for every field.
It does **not** mean OSM implements, certifies, fully models, or
replaces that model.

A framework must not drive a new OSM field simply because it uses a
different name. If OSM already represents the concept, reuse that
field (**OSM-C-009**). Canonical OSM concept first; framework
mapping second.

Regulatory, security, privacy and control mappings live in
[`compliance/`](../compliance/).

Exact field definitions are in [`SPECIFICATION.md`](../SPECIFICATION.md).

Concepts that stay **outside** OSM are listed in
[`SPECIFICATION.md`](../SPECIFICATION.md) — *External Concepts —
Intentionally Outside OSM*.

---

## Status

Use these labels. Do not use vague “supported”.

| Status | Meaning |
|--------|---------|
| **MAPPED** | Correspondence is documented. OSM can represent or join the listed concepts. Not certification. |
| **PARTIAL** | Some catalog-relevant correspondences work; remaining concepts are gaps or **deliberate** OSM-core boundaries. |
| **EXTERNAL** | The concept belongs in another system. OSM does not absorb it. |
| **NOT IN SCOPE** | Outside OSM’s technological-service boundary. |
| **FUTURE / OPTIONAL** | Documented convention or schema candidate; not current core. |

OSM is **not formally compliant or certified** against any of these
models.

| Model | Current version mapped | Status | File |
|-------|------------------------|--------|------|
| TM Forum TMF633 | Service Catalog API **v4.0.0** | **PARTIAL** | [TMFORUM-TMF633.md](service-management/TMFORUM-TMF633.md) |
| ITIL | **Version 5** (ITIL 4 still relevant) | **PARTIAL** | [ITIL.md](service-management/ITIL.md) |
| ServiceNow CSDM | **CSDM 5** | **PARTIAL** | [CSDM.md](service-management/CSDM.md) |
| ArchiMate | **ArchiMate 4** | **MAPPED** (conceptual, technology-service grain) | [ARCHIMATE.md](architecture/ARCHIMATE.md) |
| TOGAF | **Standard 10th Edition** + Corrigendum 1 | **MAPPED** (stack-level domain label) | [TOGAF.md](architecture/TOGAF.md) |
| TBM | Taxonomy **5.0.1** | **MAPPED** (stack-level Resource Tower labels) | [TBM.md](architecture/TBM.md) |

Each mapping file answers: external concept, OSM target, grain,
direct / partial / conceptual, what remains outside, semantic
differences.

---

## Service management and catalogs

| Model | Role beside OSM |
|-------|-----------------|
| [ITIL](service-management/ITIL.md) | Service management practices and Product/Service Lifecycle — **EXTERNAL** to OSM `lifecycle_state` |
| [TM Forum TMF633](service-management/TMFORUM-TMF633.md) | Richer catalog API and information model |
| [ServiceNow CSDM](service-management/CSDM.md) | ServiceNow-oriented service and CMDB modeling; Service Instance remains **EXTERNAL** |

## Architecture and technology finance

| Model | Role beside OSM |
|-------|-----------------|
| [TOGAF](architecture/TOGAF.md) | Architecture method; optional `togaf_domain` on Technology Stack only |
| [ArchiMate](architecture/ARCHIMATE.md) | Architecture language; OSM Service maps to generic **Service** in technology-domain context |
| [TBM](architecture/TBM.md) | Technology financial management; optional Resource Tower labels on stacks |
