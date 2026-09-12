# NIST CSF

- **Status:** NOT ANALYZED
- **Universe:** OSM-C-001 (compliance / governance)
- **OSM schema fields today:** optional stack `mappings.nist_csf`;
  optional offering `nist_functions`, `nist_control_status`

These fields are reference mappings. They are **not** a NIST CSF
profile and not a claim that OSM or any adopter "complies with"
NIST CSF.

## 1. Framework overview

The NIST Cybersecurity Framework (CSF 2.0) organizes cybersecurity
outcomes into Functions (Govern, Identify, Protect, Detect, Respond,
Recover) and a set of Categories / Subcategories.

## 2. Relevant scope for technological services

Later analysis should ask whether tagging a stack or offering with
CSF Functions is useful operational metadata, versus a full CSF
profile which OSM cannot host.

## 3. OSM concepts/attributes relevant to the framework

Present in the current schema (not yet analyzed as a mapping):

| OSM field | Where |
|-----------|--------|
| `mappings.nist_csf` | Technology Stack (list of functions) |
| `nist_functions` | Offering attributes |
| `nist_control_status` | Offering attributes |
| `last_security_review` | Offering attributes |

OSM currently stores Functions, not Categories or Subcategories.

## 4. Mapping opportunities

NOT YET ANALYZED.

## 5. Missing information

NOT YET ANALYZED.

No CSF profile, current-state/target-state, or subcategory coverage
exists in OSM.

## 6. Potential extensions

None proposed. No attributes are added in this baseline.

## 7. Important caveats

- A function tag is not an implemented control.
- NIST CSF is a framework, not a certification OSM can satisfy.
- This file is not a security assessment.

## 8. Status

**NOT ANALYZED**
