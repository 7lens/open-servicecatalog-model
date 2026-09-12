# Governance

This document defines the two ownership roles used by the
`accountable` field in the Open Services Data Model.

The roles are deliberately small. They describe accountability for
**technological services**, not a complete operating model, RACI
matrix, or organizational hierarchy.

## Technology Stack Owner

| | |
|--|--|
| **ID** | `technology_stack_owner` |
| **Typical profile** | Platform lead, domain owner, or equivalent |
| **Scope** | One Technology Stack as an operational competency domain |

### Accountabilities

- Keep the stack's documented scope current so it is clear which
  technological services belong in the domain.
- Ensure the set of services in the stack covers the intended
  competency without unexplained duplication.
- Ensure every service in the stack has an assigned Service Owner.
- Review proposed new services and offerings for fit with the stack.
- Escalate gaps in ownership, lifecycle, or operational evidence.

The Technology Stack Owner is accountable for the *domain*. They are
not required to operate every service personally.

## Service Owner

| | |
|--|--|
| **ID** | `service_owner` |
| **Typical profile** | Principal engineer, service lead, or equivalent |
| **Scope** | One technological Service in the catalog |

### Accountabilities

- Ensure the service is used for its stated technological purpose.
- Own the service lifecycle: requestability, operation, change,
  incident support, decommissioning, and agreed service levels.
- Maintain the catalog identity of the service and its offerings
  (stable IDs, accurate names and descriptions).
- Keep operational attributes current enough to be useful, including
  lifecycle, criticality, automation and resilience evidence.
- Own applicable security, privacy and operational-resilience
  obligations of the service, or name the controlling control owner.
- Oversee vendor support, provider concentration and cost signals
  that attach to the service or its offerings.
- Act as the subject-matter expert for scalability, availability
  and recovery of the service.

The Service Owner is accountable for the *technological service*.
They are not, by this model, the owner of consuming teams, business
products, or application portfolios.

## How the roles appear in data

- `services[].accountable` names the Service Owner (role, person or
  team alias).
- Stack ownership is an operating-model concern. Record it beside
  the stack in your own process; the stack schema does not require a
  person field.

## What this file does not define

- reporting lines or HR structure
- geographic or legal-entity ownership
- application or product ownership
- a complete control library
- a GRC methodology

Those concerns belong in other systems.
