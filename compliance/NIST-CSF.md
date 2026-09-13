# NIST CSF

OSM is **not** a NIST CSF profile and not a claim that an adopter
“complies with” the Cybersecurity Framework.

NIST CSF 2.0 organizes cybersecurity outcomes into Functions
(Govern, Identify, Protect, Detect, Respond, Recover). OSM stores
those **Functions** as a translation layer on stacks and offerings.
It does not store Categories, Subcategories, or current/target
profiles.

## What maps

| OSM field | Where | Role |
|-----------|--------|------|
| `mappings.nist_csf` | Technology Stack | List of CSF functions |
| `nist_functions` | Offering posture | List of CSF functions |
| `nist_control_status` | Offering posture | Implementation status |
| `last_security_review` | Offering posture | Security-operations signal |

## What stays in NIST CSF

- Categories and Subcategories
- organizational profiles (current-state / target-state)
- a security assessment or certification

A function tag is not an implemented control. NIST CSF is a
framework, not a certification OSM can satisfy.

Exact field definitions are in
[`SPECIFICATION.md`](../SPECIFICATION.md).
