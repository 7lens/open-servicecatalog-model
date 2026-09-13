# Golden-example validation scorecard

**Date:** 2026-09-13  
**Subject:** `examples/reference-enterprise/golden-example/`  
**Source:** read-only predecessor catalog `Downloads/example_enterprise/`  
**Schema:** frozen OSM 1.3.0 — not changed  
**This pass:** audit only. Examples were not modified.

## Verdict

**YES, WITH SPECIFIC FIXES**

The Kubernetes walk-through is the one genuinely golden lesson: a
predecessor product-Service (`compute.eks` / `compute.aks` /
`compute.openshift`) becomes one technological Service with provider
variants. Virtual machines and object storage follow the same rule.

A technically sophisticated organization that **copies the rest of
the golden YAML in isolation** can still build a bad OSM catalog.
The IAM offerings are request-catalog items, several Offerings have
no variant dimension, service-level posture leaks from one product
onto a collapsed capability, and compliance mapping fields read as
claims. The basic synthetic examples teach a contradictory VM and
provider pattern.

Validation success is not sufficient. The YAML is schema-valid and
semantically uneven.

## Scorecard

| Dimension | Score | Findings |
|-----------|:-----:|----------|
| Service abstraction | 4 | VM / Kubernetes / object storage / managed relational are capability Services. `compute.functions`, `auto.configuration-automation` and `auto.aiops` still look like single-product Services. `sec.iam` is workforce identity, which is right for this source, but the id still says IAM. |
| Offering semantics | 3 | Cloud/engine variants are real Offerings. `sec.iam.directory-lifecycle` / `mfa` are request types, not variants. `storage.backup.backup`, `sec.secrets.secrets-mgmt`, `auto.aiops.aiops` are tautological singletons. |
| Provider semantics | 3 | Legal-seller merge of source `azure`→`microsoft` is correct. `redhat` on a capability Service is too intrinsic. `oracle` on RDS Oracle is a source dual-provider that may only be an engine licensor. |
| Characteristic semantics | 3 | `os_family` is a good definition characteristic. `deployment_environment: aws` on offering `*.aws` duplicates identity. Overloads “environment” vs basic examples (`production`/`development`). |
| Posture semantics | 3 | Correctly refused to copy EKS `important` onto Kubernetes. Incorrectly copied EKS `vendor_support_status` and provenance dates onto the collapsed Service. Predecessor health file is itself a field-pattern demo. |
| Provenance | 3 | Import trail exists. Collapsed Services point at one of several source ids. `last_verified: 2026-01-01` is cataloguing metadata, not a source date. |
| Compliance semantics | 2 | Provider `certifications[]` have no golden-folder scope warning. ISO/NIST/GDPR/AI Act posture values look like assessments. Source `gdpr_dpa_signed: true` was correctly not copied; the golden folder never says why. |
| Unknown-value discipline | 3 | AKS/OpenShift RTO left unknown. DPA/risk null. `lifecycle_state: production` invented for services without source attributes. Seven of ten services have no posture record — unexplained if the golden folder is read alone. |
| Source traceability | 4 | Collapse map is reconstructable. Lost: OS-patching offerings, IAM password-reset, OpenShift’s second offering, restricted classification grain on RDS Oracle. |
| Documentation | 3 | Kubernetes README is excellent. Isolation fails: certifications, dummy offerings, IAM request types, and “health record was a demo subset” live in parent docs or not at all. |
| Copy-paste safety | 2 | See Phase 9. IAM offerings + singleton offerings + certs + leaked vendor_support + contradiction with `examples/catalog`. |
| Cross-example consistency | 2 | Basic examples: `azure` provider, VM offerings = tenancy, Kubernetes offerings `.aws`/`.azure`. Estate: `microsoft`/`google-cloud`, product offerings, identity split. Enterprise golden: `microsoft`/`gcp`, cloud offerings, `sec.iam`. |

Scoring: 5 excellent, 4 minor, 3 meaningful concern, 2 major, 1 fundamentally misleading.

## Chain (reconstructed)

```
SOURCE predecessor catalog (95 product-Services, 6 demo health records)
    → INTERPRETATION  technological capability, not vendor product
    → OSM             Service + Offerings + providers[] + optional posture
```

The interpretation is correct for EKS/AKS/S3. It is over-applied when
OpenShift is forced under Kubernetes, when IAM request types become
Offerings, and when demo health values become “imported enterprise
posture.”

## Record counts (golden)

| Record | Count |
|--------|------:|
| Technology Stacks | 5 |
| Services | 10 |
| Service Offerings | 17 |
| ICT Providers | 4 |
| Service Posture | 3 |
| Offering Posture | 3 |

## Validator

```
OK: examples/reference-enterprise/golden-example is valid
OK: examples/reference-enterprise is valid
OK: examples is valid
```

Errors: none. Warnings: none (validator has no warning channel).
Schema-valid ≠ semantically golden.
