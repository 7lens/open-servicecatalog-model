# OSM onboarding

This is the first-phase path for anyone who opens this repository —
a human reading it, or a coding assistant asked “how do I use this?”.
Same conversation. Do not skip it. Do not dump a finished catalog
before there is a draft the organization is comfortable starting with.

The CLI `python3 -m tools.osm_scaffold.cli` is one implementation.
A coding assistant that writes YAML must still run this conversation,
persist the same files, and honour pause / continue.

---

## What OSM is (say this at the start, and again on every continue)

OSM (7lens Open Service-Catalog Model) is a **small, vendor-neutral,
canonical data model** for technological services. Frozen at 1.3.0.
It is not an AI model, a CMDB, a DORA register, or a claim of
compliance.

The value is **owning the semantics**. That is the hard asset. Owned
semantics are what let you grow a **lock-in-free ontology** — the
enterprise’s own picture of technological services — instead of
inheriting a vendor’s, a cloud’s, or a framework’s.

If those semantics are not owned, and not available to the whole
organization, every team and every agent keeps translating between
incompatible pictures. OSM exists to close that gap.

Unknown facts stay unset. A small honest draft beats a
complete-looking fiction.

The ideal first user is a Principal Manager, Platform Lead, Head of
Architecture, or Enterprise Architect. Anyone who sees the problem
can start.

---

## Where the adopter’s model is stored

Everything the adopter owns is written under `servicecatalog/`:

```text
servicecatalog/catalog/technology-stacks.yaml
servicecatalog/catalog/services.yaml
servicecatalog/catalog/ict-providers.yaml
servicecatalog/posture/service-posture.yaml
servicecatalog/.osm-scaffold-state.json   ← pause / continue checkpoint
```

Remind them of this path at the beginning, after every change, and
when they continue. The checkpoint is how pause and continue work.
Do not delete it after the first draft. They will come back.

---

## Phase 1 objective

A **draft** of Technology Stacks and Services the adopter is
comfortable starting with. Not a complete estate. Not posture. Not
certification.

Lifecycle on new work is `draft`. Offerings may be thin placeholders
so the YAML is valid. Do not invent RTO, DPA, or control status.

---

## Conversation (every new session)

1. **Orient.** What OSM is. Where the catalog lives. Phase 1 goal.
   They can pause at any time and continue later from this checkpoint.
2. **Technology stacks.** Ask what capabilities they actually operate
   (compute, identity, data — not “AWS” or “M365”). Use the golden
   domains as prompts; allow names they give you. Stacks are adopter
   competencies, never vendor towers.
3. **Compliance.** Ask which frameworks apply as **locators only**
   (ISO 27001, DORA, GDPR, NIST, …). Selecting a framework is not a
   claim of compliance.
4. **Draft.** Propose Stacks and Services from their answers and,
   if useful, `examples/reference-enterprise/golden-example` and
   `examples/reference-estate/golden-example`. Show the board.
5. **Comfort loop.** Keep changing the draft until they say they are
   comfortable starting with it. After every change, show the board
   again: “this is what we currently have.”
6. **Write** the YAML under `servicecatalog/`. Keep the checkpoint.
   Stop. They can continue later.

### The board (show this constantly)

A simple view, every time:

- reminder: OSM is the lock-in-free canonical model; files live in
  `servicecatalog/`
- Technology Stacks (id + name)
- Services (id + name + lifecycle)
- Compliance locators selected (or “none yet”) — not claims
- how to pause, how to continue

Do not hide the draft behind a long questionnaire.

---

## Pause

At any moment the adopter may pause. Persist
`servicecatalog/.osm-scaffold-state.json` **and** any YAML already
written. Tell them they can continue from exactly this draft.

CLI: type `:pause` or `:save`, or `python3 -m tools.osm_scaffold.cli`
later with `--resume`.

---

## Continue (every resumed session)

Never restart from zero if a checkpoint or catalog YAML already exists.

1. Remind what OSM is and that **their** model is in `servicecatalog/`.
2. Summarise what is already configured (the board).
3. Say where it is stored (the paths above).
4. Propose how to continue — only these, unless they ask for more:
   - add a new Technology Stack
   - add a new Service
   - propose more from the golden examples
   - update the YAML on disk
   - pause again

Then wait. Do not push offerings, posture, or “completeness.”

CLI: `python3 -m tools.osm_scaffold.cli --status` prints the board
without changing anything. `--resume` continues. `--fresh` discards
the checkpoint (does not delete YAML unless they ask).

---

## Guardrails (do not violate)

- Do not name a Service after a product (`EKS`, `S3`). Name the
  capability; put the product on an Offering.
- Do not use ITSM request types as Offerings (`password-reset`).
- Do not create a Technology Stack named after a vendor (`AWS`).
- Do not invent posture or compliance evidence.
- Do not change `schema/`, `SPECIFICATION.md`, or `MODEL.md`.
