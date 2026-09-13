#!/usr/bin/env python3
"""Force Podwarack git identity and strip Cursor attribution trailers."""

from __future__ import annotations

import json
import re
import sys

NAME = "Podwarack"
EMAIL = "328382584+podwarack@users.noreply.github.com"
ENV_PREFIX = (
    f"GIT_AUTHOR_NAME={NAME} "
    f"GIT_AUTHOR_EMAIL={EMAIL} "
    f"GIT_COMMITTER_NAME={NAME} "
    f"GIT_COMMITTER_EMAIL={EMAIL} "
)
GIT_IDENTITY = f"-c user.name={NAME} -c user.email={EMAIL}"

TRAILER_LINE = re.compile(
    r"^[ \t]*Co-authored-by:[ \t]*(Cursor|cursoragent).*$",
    re.IGNORECASE | re.MULTILINE,
)
TRAILER_FLAG = re.compile(
    r"""--(?:trailer|footer)(?:\s+|=)(['\"]?)[^'\"\n]*(Cursor|cursoragent)[^'\"\n]*\1""",
    re.IGNORECASE,
)
GIT_COMMIT = re.compile(r"\bgit(\s+)commit\b")
GIT_CONFIG_USER = re.compile(
    r"\bgit\s+config\b[^\n]*\buser\.(name|email)\b",
    re.IGNORECASE,
)
PERSONAL_EMAIL = re.compile(r"@[^ \n]*\.local\b", re.IGNORECASE)


def allow(updated=None) -> dict:
    out = {"permission": "allow"}
    if updated is not None:
        out["updated_input"] = updated
    return out


def deny(message: str) -> dict:
    return {
        "permission": "deny",
        "user_message": message,
        "agent_message": message,
    }


def locate_command(payload: dict) -> tuple[str | None, str]:
    if isinstance(payload.get("command"), str):
        return "command", payload["command"]
    for key in ("tool_input", "arguments", "input"):
        block = payload.get(key)
        if isinstance(block, dict) and isinstance(block.get("command"), str):
            return f"{key}.command", block["command"]
    return None, ""


def set_command(payload: dict, where: str, command: str) -> dict:
    if where == "command":
        updated = dict(payload.get("tool_input") or payload.get("arguments") or {})
        if "command" in (payload.get("tool_input") or {}):
            updated = dict(payload["tool_input"])
            updated["command"] = command
            return updated
        if isinstance(payload.get("arguments"), dict):
            updated = dict(payload["arguments"])
            updated["command"] = command
            return updated
        return {"command": command}
    root, _, leaf = where.partition(".")
    block = dict(payload.get(root) or {})
    block[leaf] = command
    return block


def rewrite(command: str) -> str:
    command = TRAILER_LINE.sub("", command)
    command = TRAILER_FLAG.sub("", command)
    if GIT_COMMIT.search(command):
        command = GIT_COMMIT.sub(rf"git {GIT_IDENTITY}\1commit", command)
        if f"GIT_AUTHOR_NAME={NAME}" not in command:
            command = ENV_PREFIX + command
    return command


def config_is_forbidden(command: str) -> bool:
    if re.search(
        r"\bgit\s+config\s+(?:--global|--system)\s+(?:--unset\s+)?user\.(name|email)\b(?!\s+--get)",
        command,
        re.IGNORECASE,
    ) and not re.search(
        r"\bgit\s+config\s+(?:--global|--system)\s+--get\s+user\.(name|email)\b",
        command,
        re.IGNORECASE,
    ):
        if re.search(r"\bgit\s+config\s+(?:--global|--system)\s+user\.(name|email)\s+\S+", command, re.I):
            return True
        if re.search(r"\bgit\s+config\s+(?:--global|--system)\s+--unset\s+user\.(name|email)\b", command, re.I):
            return True
    if not GIT_CONFIG_USER.search(command):
        return False
    if PERSONAL_EMAIL.search(command):
        return True
    assigning = re.search(
        r"\bgit\s+config\b[^\n]*\buser\.(name|email)\s+\S+",
        command,
        re.IGNORECASE,
    )
    if assigning and NAME not in command and EMAIL not in command:
        return True
    return False


def main() -> None:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        json.dump(allow(), sys.stdout)
        return
    if not isinstance(payload, dict):
        json.dump(allow(), sys.stdout)
        return

    where, command = locate_command(payload)
    if not command:
        json.dump(allow(), sys.stdout)
        return

    if config_is_forbidden(command):
        json.dump(
            deny(
                "Refusing git identity change. This repo may only commit as "
                f"{NAME} <{EMAIL}>."
            ),
            sys.stdout,
        )
        return

    rewritten = rewrite(command)
    nested = payload.get("tool_input") or payload.get("arguments")
    can_rewrite = isinstance(nested, dict) and "command" in nested
    # beforeShellExecution cannot rewrite the command. Only block Cursor trailers.
    if not can_rewrite:
        if re.search(
            r"Co-authored-by:\s*(Cursor|cursoragent)|--(?:trailer|footer)[^\n]*(Cursor|cursoragent)",
            command,
            re.I,
        ):
            json.dump(
                deny(
                    "Refusing Cursor attribution in git. Re-run the commit as "
                    f"{NAME} <{EMAIL}> with no Co-authored-by: Cursor trailer."
                ),
                sys.stdout,
            )
            return
        json.dump(allow(), sys.stdout)
        return

    if rewritten == command:
        json.dump(allow(), sys.stdout)
        return

    json.dump(allow(set_command(payload, where or "command", rewritten)), sys.stdout)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        json.dump({"permission": "allow"}, sys.stdout)
