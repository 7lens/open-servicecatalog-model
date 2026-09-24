"""Shared onboarding session: orientation, status board, pause/continue hydrate."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from tools.osm_common.loader import CatalogLoadError, load_catalog
from tools.osm_common.models import Catalog
from tools.osm_scaffold.state import empty_state, load_state, save_state

STEP_ALIASES = {
    "frameworks": "compliance",
    "domains": "stacks",
    "refine_offerings": "comfort",
    "params_stacks": "comfort",
    "params_services": "comfort",
    "params_offerings": "comfort",
    "compile": "write",
}

CONTINUE_CHOICES = (
    "add a Technology Stack",
    "add a Service",
    "propose more from the golden examples",
    "update the YAML on disk",
    "pause and continue later",
)


def normalize_step(step: str | None) -> str:
    raw = (step or "stacks").strip() or "stacks"
    return STEP_ALIASES.get(raw, raw)


def catalog_yaml_present(catalog_dir: Path) -> bool:
    return (Path(catalog_dir) / "catalog" / "services.yaml").is_file()


def orientation(catalog_dir: Path) -> str:
    root = Path(catalog_dir)
    return "\n".join(
        [
            "OSM is a canonical data model for technological services.",
            "It is not an AI model.",
            "",
            "The value: you own the semantics. That is the hard asset.",
            "Owned semantics let you grow a lock-in-free ontology — your",
            "enterprise picture of technological services — instead of",
            "inheriting a vendor's, a cloud's, or a framework's.",
            "",
            "If those semantics are not owned and not available to the whole",
            "organization, every team and every agent keeps translating",
            "between incompatible pictures. That is the gap OSM closes.",
            "",
            "Ideal first user: Principal Manager, Platform Lead, Head of",
            "Architecture, or Enterprise Architect. Anyone who sees the",
            "problem can start.",
            "",
            "Phase 1: a DRAFT of Stacks and Services you are comfortable",
            "starting with. Unknown stays unset. That is correct.",
            "",
            f"Your model is stored in {root.resolve()}",
            "  catalog/technology-stacks.yaml",
            "  catalog/services.yaml",
            "  catalog/ict-providers.yaml",
            "  posture/service-posture.yaml",
            "  .osm-scaffold-state.json  (pause / continue)",
            "",
            "Pause anytime with :pause. Continue later with",
            "  python3 -m tools.osm_scaffold.cli --resume",
            "The board below is what we currently have.",
        ]
    )


def reminder(catalog_dir: Path) -> str:
    return (
        "You own the semantics; OSM is the lock-in-free canonical core. "
        f"Files: {Path(catalog_dir).resolve()}  "
        "Pause: :pause   Continue: python3 -m tools.osm_scaffold.cli --resume"
    )


def continue_proposals() -> str:
    lines = [
        "How to continue:",
        "  1. add a Technology Stack",
        "  2. add a Service",
        "  3. propose more from the golden examples",
        "  4. update the YAML on disk",
        "  5. pause and continue later",
    ]
    return "\n".join(lines)


def render_status(state: dict[str, Any], catalog_dir: Path) -> str:
    root = Path(catalog_dir).resolve()
    frameworks = list(state.get("frameworks") or [])
    stacks = list(state.get("stacks") or [])
    services = list(state.get("services") or [])
    compliance = ", ".join(frameworks) if frameworks else "none yet (locators, not claims)"
    lines = [
        "This is what we currently have",
        "------------------------------",
        "OSM 1.3.0  ·  you own the semantics  ·  lock-in-free ontology",
        f"Stored in: {root}",
        "  catalog/technology-stacks.yaml",
        "  catalog/services.yaml",
        "  catalog/ict-providers.yaml",
        f"Checkpoint: {root / '.osm-scaffold-state.json'}",
        f"Step: {state.get('step') or 'stacks'}",
        "",
        f"Compliance locators (not claims): {compliance}",
        "",
        "Technology Stacks",
    ]
    if not stacks:
        lines.append("  (none yet)")
    else:
        for stack in stacks:
            lines.append(f"  {stack.get('id') or '—':<16} {stack.get('name') or ''}")
    lines.append("")
    lines.append("Services")
    if not services:
        lines.append("  (none yet)")
    else:
        for service in services:
            life = service.get("lifecycle_state") or "draft"
            lines.append(
                f"  {str(service.get('id') or '—'):<28} {service.get('name') or ''}  [{life}]"
            )
    lines.append("")
    lines.append(
        "Phase 1 goal: a draft of Stacks and Services you are comfortable starting with."
    )
    lines.append(reminder(catalog_dir))
    return "\n".join(lines)


def resume_briefing(state: dict[str, Any], catalog_dir: Path) -> str:
    return "\n".join(
        [
            orientation(catalog_dir),
            "",
            render_status(state, catalog_dir),
            "",
            continue_proposals(),
        ]
    )


def state_from_catalog(catalog: Catalog) -> dict[str, Any]:
    state = empty_state()
    state["step"] = "continue"
    locators: set[str] = set()
    stacks: list[dict[str, Any]] = []
    for stack in catalog.stacks:
        mappings = dict(stack.mappings or {})
        locators.update(str(key) for key in mappings)
        stacks.append(
            {
                "id": stack.id,
                "name": stack.name,
                "description": stack.description or stack.name,
                "mappings": mappings,
            }
        )
    services: list[dict[str, Any]] = []
    for service in catalog.services:
        services.append(
            {
                "id": service.id,
                "name": service.name,
                "description": service.description or service.name,
                "technology_stack": service.technology_stack,
                "accountable": service.accountable,
                "version": service.version or "1.0.0",
                "valid_from": service.valid_from,
                "valid_to": service.valid_to,
                "lifecycle_state": service.lifecycle_state or "draft",
                "providers": list(service.providers),
                "characteristics": [dict(item.raw) for item in service.characteristics],
                "offerings": [
                    {
                        "id": offering.id,
                        "name": offering.name,
                        "providers": list(offering.providers),
                        "characteristics": [dict(item.raw) for item in offering.characteristics],
                    }
                    for offering in service.offerings
                ],
            }
        )
    providers = [
        {
            "id": provider.id,
            "name": provider.name,
            "type": provider.type or "cloud-infrastructure",
            "substitutability": provider.substitutability or "medium",
            "gdpr_dpa_signed": provider.gdpr_dpa_signed,
            "dora_notification_clause": provider.dora_notification_clause,
            "certifications": list(provider.certifications),
            "risk_level": provider.risk_level,
        }
        for provider in catalog.providers
    ]
    state["stacks"] = stacks
    state["services"] = services
    state["providers"] = providers
    state["frameworks"] = sorted(locators)
    return state


def load_session(catalog_dir: Path) -> dict[str, Any] | None:
    """Checkpoint first; otherwise hydrate from catalog YAML already on disk."""
    state = load_state(catalog_dir)
    if state is not None:
        state["step"] = normalize_step(state.get("step"))
        return state
    if not catalog_yaml_present(catalog_dir):
        return None
    try:
        catalog = load_catalog(catalog_dir)
    except (CatalogLoadError, OSError, ValueError):
        return None
    return state_from_catalog(catalog)


def persist_session(catalog_dir: Path, state: dict[str, Any]) -> Path:
    state["step"] = normalize_step(state.get("step"))
    return save_state(catalog_dir, state)
