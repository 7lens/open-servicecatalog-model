"""Checkpoint file for the osm-scaffold onboarding wizard."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any

STATE_FILENAME = ".osm-scaffold-state.json"
STEPS = (
    "frameworks",
    "domains",
    "draft",
    "refine_stacks",
    "refine_services",
    "refine_offerings",
    "params_stacks",
    "params_services",
    "params_offerings",
    "compile",
)


def state_path(catalog_dir: Path) -> Path:
    return Path(catalog_dir) / STATE_FILENAME


def empty_state() -> dict[str, Any]:
    return {
        "step": "frameworks",
        "cursor": 0,
        "frameworks": [],
        "domains": [],
        "stacks": [],
        "services": [],
        "providers": [],
        "updated": date.today().isoformat(),
    }


def load_state(catalog_dir: Path) -> dict[str, Any] | None:
    path = state_path(catalog_dir)
    if not path.is_file():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return None
    merged = empty_state()
    merged.update(data)
    return merged


def save_state(catalog_dir: Path, state: dict[str, Any]) -> Path:
    catalog_dir.mkdir(parents=True, exist_ok=True)
    path = state_path(catalog_dir)
    payload = dict(state)
    payload["updated"] = date.today().isoformat()
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def clear_state(catalog_dir: Path) -> None:
    path = state_path(catalog_dir)
    if path.is_file():
        path.unlink()


def render_tree(state: dict[str, Any]) -> str:
    frameworks = state.get("frameworks") or []
    domains = state.get("domains") or []
    stacks = state.get("stacks") or []
    services = state.get("services") or []
    lines = [
        f"step: {state.get('step')}",
        f"frameworks: {', '.join(frameworks) if frameworks else '(none)'}",
        f"domains: {', '.join(domains) if domains else '(none)'}",
        "catalog draft:",
    ]
    if not stacks:
        lines.append("  (no stacks yet)")
        return "\n".join(lines)
    by_stack: dict[str, list[dict[str, Any]]] = {row["id"]: [] for row in stacks}
    name_to_id = {row["name"]: row["id"] for row in stacks}
    unmatched: list[dict[str, Any]] = []
    for service in services:
        stack_name = service.get("technology_stack")
        stack_id = name_to_id.get(stack_name) if stack_name else None
        if stack_id is None:
            prefix = str(service.get("id") or "").split(".")[0]
            stack_id = prefix if prefix in by_stack else None
        if stack_id is None:
            unmatched.append(service)
            continue
        by_stack.setdefault(stack_id, []).append(service)
    for stack in stacks:
        lines.append(f"  {stack['id']}  {stack.get('name')}")
        for service in by_stack.get(stack["id"], []):
            owner = service.get("accountable") or "—"
            life = service.get("lifecycle_state") or "—"
            lines.append(f"    {service['id']}  {service.get('name')}  [{life}, {owner}]")
            for offering in service.get("offerings") or []:
                providers = ",".join(offering.get("providers") or []) or "self-operated"
                lines.append(f"      {offering['id']}  {offering.get('name')}  ({providers})")
    for service in unmatched:
        lines.append(f"    {service.get('id')}  (unassigned stack)")
    return "\n".join(lines)
