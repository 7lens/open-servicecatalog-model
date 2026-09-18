#!/usr/bin/env python3
"""CLI: python3 -m tools.osm_scaffold.cli [--resume] [--config FILE] [--output DIR]"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from tools.osm_scaffold.state import load_state, state_path
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
            "Onboarding wizard for OSM 1.3.0. The Principal Manager, "
            "Platform Lead, or Head of Architecture uses this to establish "
            "the canonical catalog under servicecatalog/. "
            "At prompts: :view  :save. Resume with --resume."
        ),
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Load servicecatalog/.osm-scaffold-state.json and continue",
    )
    parser.add_argument(
        "--fresh",
        action="store_true",
        help="Ignore an existing checkpoint and start the wizard from step 1",
    )
    parser.add_argument(
        "--config",
        help="Non-interactive one-service YAML (does not run the onboarding wizard)",
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
        checkpoint = load_state(catalog_dir)
        if checkpoint is not None and not args.resume and not args.fresh:
            sys.stderr.write(
                f"osm-scaffold: checkpoint exists at {state_path(catalog_dir)}\n"
                "  resume:  python3 -m tools.osm_scaffold.cli --resume\n"
                "  restart: python3 -m tools.osm_scaffold.cli --fresh\n"
            )
            return 1
        if not args.config and not sys.stdin.isatty() and argv is None:
            sys.stderr.write("osm-scaffold: interactive wizard needs a TTY, or pass --config\n")
            return 1

        wizard = OnboardingWizard(REPO_ROOT, catalog_dir)
        wizard.run(resume=bool(args.resume))
        return 0
    except SaveAndExit as exc:
        sys.stdout.write(f"checkpoint saved: {exc}\n")
        sys.stdout.write("resume with: python3 -m tools.osm_scaffold.cli --resume\n")
        return 0
    except ScaffoldError as exc:
        sys.stderr.write(f"osm-scaffold: {exc}\n")
        return 1
    except (OSError, yaml.YAMLError) as exc:
        sys.stderr.write(f"osm-scaffold: {exc}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
