#!/usr/bin/env python3
"""CLI: python3 -m tools.osm_scaffold.cli [--resume] [--status] [--config FILE] [--output DIR]"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from tools.osm_scaffold.session import load_session, render_status, resume_briefing
from tools.osm_scaffold.state import state_path
from tools.osm_scaffold.wizard import (
    OnboardingWizard,
    SaveAndExit,
    ScaffoldError,
    build_records,
    load_config,
    merge_into_catalog,
    records_as_yaml,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CATALOG = REPO_ROOT / "servicecatalog"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="osm-scaffold",
        description=(
            "OSM onboarding. Same protocol as ONBOARDING.md: explain the "
            "canonical model, ask stacks then compliance, produce a draft "
            "the adopter is comfortable starting with. "
            "At prompts: :view  :pause. Resume with --resume."
        ),
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Continue from servicecatalog YAML and/or .osm-scaffold-state.json",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Print the current draft board and exit",
    )
    parser.add_argument(
        "--fresh",
        action="store_true",
        help="Ignore an existing checkpoint and start the conversation from step 1",
    )
    parser.add_argument(
        "--config",
        help="Non-interactive one-service YAML (does not run onboarding)",
    )
    parser.add_argument(
        "--output",
        help=f"Catalog directory (default: {DEFAULT_CATALOG})",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    catalog_dir = Path(args.output) if args.output else DEFAULT_CATALOG
    try:
        if args.config:
            config = load_config(Path(args.config))
            records = build_records(config)
            if args.output:
                merge_into_catalog(Path(args.output), records)
                sys.stdout.write(f"wrote OSM catalog fragment under {Path(args.output).resolve()}\n")
                sys.stdout.write(f"  service {records['service']['id']}\n")
                return 0
            sys.stdout.write(records_as_yaml(records))
            return 0

        if args.resume and args.fresh:
            sys.stderr.write("osm-scaffold: use either --resume or --fresh, not both\n")
            return 1
        session = load_session(catalog_dir)
        if args.status:
            if session is None:
                sys.stdout.write(f"No OSM draft yet at {catalog_dir.resolve()}\n")
                sys.stdout.write("Start: python3 -m tools.osm_scaffold.cli\n")
                return 0
            sys.stdout.write(render_status(session, catalog_dir) + "\n")
            return 0
        if session is not None and not args.resume and not args.fresh:
            sys.stdout.write(resume_briefing(session, catalog_dir) + "\n")
            sys.stdout.write(
                f"\nCheckpoint: {state_path(catalog_dir)}\n"
                "Continue: python3 -m tools.osm_scaffold.cli --resume\n"
                "Restart conversation: python3 -m tools.osm_scaffold.cli --fresh\n"
            )
            return 0
        if not args.config and not sys.stdin.isatty() and argv is None:
            sys.stderr.write("osm-scaffold: interactive session needs a TTY, or pass --config\n")
            return 1

        wizard = OnboardingWizard(REPO_ROOT, catalog_dir)
        wizard.run(resume=bool(args.resume))
        return 0
    except SaveAndExit as exc:
        session = load_session(catalog_dir)
        if session is not None:
            sys.stdout.write(render_status(session, catalog_dir) + "\n")
        sys.stdout.write(f"Paused. Checkpoint: {exc}\n")
        sys.stdout.write("Continue: python3 -m tools.osm_scaffold.cli --resume\n")
        return 0
    except ScaffoldError as exc:
        sys.stderr.write(f"osm-scaffold: {exc}\n")
        return 1
    except (OSError, yaml.YAMLError) as exc:
        sys.stderr.write(f"osm-scaffold: {exc}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
