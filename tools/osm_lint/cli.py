#!/usr/bin/env python3
"""CLI: python3 -m tools.osm_lint.cli --catalog <path>"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from tools.osm_common.loader import CatalogLoadError
from tools.osm_lint.engine import exit_code, lint_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="osm-lint",
        description=(
            "Semantic guardrail for OSM 1.3.0 catalogs. "
            "Reports modelling anti-patterns that structural validation accepts. "
            "Does not change the frozen model."
        ),
    )
    parser.add_argument(
        "--catalog",
        required=True,
        help="Directory containing catalog/ and optional posture/ YAML",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Report format (default: text)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    catalog_dir = Path(args.catalog)
    try:
        catalog, findings = lint_path(catalog_dir)
    except CatalogLoadError as exc:
        sys.stderr.write(f"osm-lint: {exc}\n")
        return 1

    code = exit_code(findings)
    errors = sum(1 for item in findings if item.severity == "error")
    warnings = sum(1 for item in findings if item.severity == "warning")

    if args.format == "json":
        payload = {
            "catalog": str(catalog.root),
            "error_count": errors,
            "warning_count": warnings,
            "exit_code": code,
            "findings": [item.to_dict() for item in findings],
        }
        sys.stdout.write(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        return code

    summary = f"osm-lint: {errors} error(s), {warnings} warning(s) in {catalog.root}"
    if not findings:
        sys.stdout.write(summary + "\nOK\n")
        return 0
    sys.stdout.write(summary + "\n\n")
    sys.stdout.write("\n\n".join(item.format_text() for item in findings) + "\n")
    return code


if __name__ == "__main__":
    sys.exit(main())
