"""Plain ASCII / Markdown tables. No extra terminal dependencies."""

from __future__ import annotations

from collections.abc import Sequence


def ascii_table(headers: Sequence[str], rows: Sequence[Sequence[object]]) -> str:
    str_rows = [[_cell(item) for item in row] for row in rows]
    widths = [len(header) for header in headers]
    for row in str_rows:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(cell))

    def fmt(cells: Sequence[str]) -> str:
        parts = [cell.ljust(widths[index]) for index, cell in enumerate(cells)]
        return "| " + " | ".join(parts) + " |"

    rule = "|-" + "-|-".join("-" * width for width in widths) + "-|"
    lines = [fmt(list(headers)), rule]
    if not str_rows:
        lines.append(fmt(["—"] * len(headers)))
        return "\n".join(lines)
    for row in str_rows:
        padded = list(row) + [""] * (len(headers) - len(row))
        lines.append(fmt(padded[: len(headers)]))
    return "\n".join(lines)


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[object]]) -> str:
    return ascii_table(headers, rows)


def _cell(value: object) -> str:
    if value is None:
        return ""
    text = str(value).replace("\n", " ").strip()
    return text
