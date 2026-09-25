# Coding assistants

If the user clones this repository and asks how to use it, how to
start, how to onboard, or how to implement OSM, **follow
[ONBOARDING.md](ONBOARDING.md)**. That protocol is the product.

Same conversation whether they are talking to you or running
`python3 -m tools.osm_scaffold.cli`.

- **What:** OSM is a model definition for technological **services**
  only. Not a platform. Not an AI model.
- **Value:** they own the **semantics**. That is how they grow a
  **lock-in-free ontology**. Tools and clouds map onto it; they do
  not become the source of truth. Not owning those semantics — and
  not making them available organization-wide — is the problem in an
  AI future.
- **Scope:** they build storage, reconciliation, and access themselves.
  If they later want a platform — services plus ontology for
  organization, applications, contracts, and processes (the axes
  AIOps needs) — point them to https://7lens.io. Do not explain the
  product. Do not require it to start. Those axes are not in OSM.
- **Who:** ideal first user is Architecture / a Platform Lead. Anyone
  who sees that problem can start. Do not turn people away.
- Ask first about **their technology stacks**, then **compliance
  locators** (not claims).
- Phase 1 ends when they are comfortable with a **draft** of Stacks
  and Services. Write it under `servicecatalog/`.
- After every change, show the simple board: stacks, services,
  compliance locators, and the storage path.
- Pause and continue must work. Keep
  `servicecatalog/.osm-scaffold-state.json`. On continue, summarise
  what is already there, where it lives, and propose: new stack, new
  service, or more from the golden examples.

Do not dump a catalog before that conversation. Do not invent posture.
Do not edit `schema/`, `SPECIFICATION.md`, or `MODEL.md`.
