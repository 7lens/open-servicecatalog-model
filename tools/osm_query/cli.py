#!/usr/bin/env python3
"""CLI: python3 -m tools.osm_query.cli <gaps|providers|compliance|export-context>"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from tools.osm_common.loader import CatalogLoadError, load_catalog
from tools.osm_common.tables import ascii_table, markdown_table
from tools.osm_query.context_export import write_agent_context
from tools.osm_query.queries import query_compliance, query_gaps, query_providers


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="osm-query",
        description=(
            "Query an OSM 1.3.0 catalog. Does not infer missing posture or "
            "claim regulatory compliance."
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(subparser: argparse.ArgumentParser, *, formats: tuple[str, ...] = ("table", "markdown", "json")) -> None:
        subparser.add_argument("--catalog", required=True, help="OSM catalog directory")
        subparser.add_argument("--format", choices=formats, default=formats[0])
        subparser.add_argument("--output", help="Write to this file instead of stdout")

    add_common(sub.add_parser("gaps", help="Owner, RTO/RPO, and provenance gaps"))
    add_common(sub.add_parser("providers", help="Legal-seller concentration"))
    compliance = sub.add_parser(
        "compliance",
        help="Framework locators (not certification)",
    )
    add_common(compliance)
    compliance.add_argument(
        "--framework",
        required=True,
        choices=("dora", "iso27001", "nist"),
        help="Locator set to surface",
    )
    export = sub.add_parser(
        "export-context",
        help="Deterministic JSON context for AI agents (Epic osm-context)",
    )
    export.add_argument("--catalog", required=True, help="OSM catalog directory")
    export.add_argument(
        "--output",
        default="osm-agent-context.json",
        help="JSON file to write (default: osm-agent-context.json)",
    )
    return parser


def _emit(text: str, output: str | None) -> None:
    if output:
        Path(output).write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
        return
    sys.stdout.write(text if text.endswith("\n") else text + "\n")


def _gaps_tables(payload: dict[str, list[dict[str, Any]]], kind: str) -> str:
    table = ascii_table if kind == "table" else markdown_table
    blocks = [
        "Gaps in this catalog. Services without posture are omitted from "
        "provenance/RTO checks (sparse catalogs are valid).",
        "",
        "Missing accountable",
        table(
            ("service_id", "name", "stack"),
            [
                (row["service_id"], row["name"], row["technology_stack"])
                for row in payload["missing_accountable"]
            ],
        ),
        "",
        "Critical services missing RTO/RPO",
        table(
            ("service_id", "offering_id", "reason"),
            [
                (row["service_id"], row["offering_id"], row["reason"])
                for row in payload["critical_missing_rto_rpo"]
            ],
        ),
        "",
        "Posture records missing provenance",
        table(
            ("grain", "service_id", "offering_id"),
            [
                (row["grain"], row["service_id"], row["offering_id"])
                for row in payload["posture_missing_provenance"]
            ],
        ),
    ]
    return "\n".join(blocks) + "\n"


def _providers_table(rows: list[dict[str, Any]], kind: str) -> str:
    table = ascii_table if kind == "table" else markdown_table
    return (
        "Offerings grouped by legal ICT Provider (derived from providers[]).\n"
        "This is concentration signal, not a risk rating.\n\n"
        + table(
            ("provider", "name", "offerings", "stacks", "stack_names"),
            [
                (
                    row["provider_id"],
                    row["provider_name"],
                    row["offering_count"],
                    row["stack_count"],
                    ", ".join(row["stacks_affected"]),
                )
                for row in rows
            ],
        )
        + "\n"
    )


def _compliance_table(payload: dict[str, Any], kind: str) -> str:
    table = ascii_table if kind == "table" else markdown_table
    framework = payload["framework"]
    rows = payload["rows"]
    if framework == "dora":
        headers = (
            "service_id",
            "offering_id",
            "providers",
            "criticality",
            "rto",
            "rpo",
            "resilience_tested",
        )
        body = [
            (
                row["service_id"],
                row["offering_id"],
                ",".join(row["providers"]),
                row.get("operational_criticality") or "",
                row.get("rto") or "",
                row.get("rpo") or "",
                row.get("resilience_tested")
                if row.get("resilience_tested") not in (None, "")
                else "",
            )
            for row in rows
        ]
    elif framework == "iso27001":
        headers = ("service_id", "offering_id", "stack_locator", "offering_controls")
        body = [
            (
                row["service_id"],
                row["offering_id"],
                row.get("stack_iso27001_locator") or "",
                ",".join(str(item) for item in row.get("offering_iso27001_controls") or []),
            )
            for row in rows
        ]
    else:
        headers = ("service_id", "offering_id", "nist_functions", "nist_control_status")
        body = [
            (
                row["service_id"],
                row["offering_id"],
                ",".join(row.get("nist_functions") or []),
                row.get("nist_control_status") or "",
            )
            for row in rows
        ]
    return payload["disclaimer"] + "\n\n" + table(headers, body) + "\n"


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        catalog = load_catalog(args.catalog)
    except CatalogLoadError as exc:
        sys.stderr.write(f"osm-query: {exc}\n")
        return 1

    if args.command == "export-context":
        path = write_agent_context(catalog, args.output)
        sys.stdout.write(f"wrote {path}\n")
        return 0

    fmt = args.format
    output = args.output

    if args.command == "gaps":
        payload = query_gaps(catalog)
        if fmt == "json":
            _emit(json.dumps(payload, indent=2, sort_keys=True), output)
        else:
            _emit(_gaps_tables(payload, fmt), output)
        return 0

    if args.command == "providers":
        rows = query_providers(catalog)
        if fmt == "json":
            _emit(json.dumps({"providers": rows}, indent=2, sort_keys=True), output)
        else:
            _emit(_providers_table(rows, fmt), output)
        return 0

    if args.command == "compliance":
        payload = query_compliance(catalog, args.framework)
        if fmt == "json":
            _emit(json.dumps(payload, indent=2, sort_keys=True), output)
        else:
            _emit(_compliance_table(payload, fmt), output)
        return 0

    sys.stderr.write(f"osm-query: unknown command {args.command}\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
