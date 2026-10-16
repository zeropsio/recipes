#!/usr/bin/env python3
"""Migrate recipe import.yaml envVariables/envSecrets to vault (semantics-only)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

VAULT_DOC = """
## Environment (vault)

Import uses `project.vault` / `service.vault` as the value store (not `envVariables` / `envSecrets` on services). Map keys explicitly in each app `zerops.yaml` — do not rely on auto-injection. Avoid self-references (e.g. `KEY: ${KEY}`).
""".strip()

NO_VAULT_DOC = """
## Environment (vault)

No project or service vault entries — this demo does not use import env store keys; the app uses platform ties (`$zeropsSubdomain`, managed service hostnames) only.
""".strip()


def _append_research(recipe_dir: Path, had_env: bool) -> bool:
    research = recipe_dir / "research.md"
    if not research.exists():
        return False
    text = research.read_text()
    if "## Environment (vault)" in text:
        return False
    snippet = VAULT_DOC if had_env else NO_VAULT_DOC
    research.write_text(text.rstrip() + "\n\n" + snippet + "\n")
    return True


def _sensitive_value(val: str) -> list[str]:
    val = val.strip()
    if "generateRandomString" in val:
        return [f"      value: {val}", "      sensitive: true"]
    return [f"    {val}"]  # fallback unused


def migrate_project_env_variables(text: str) -> tuple[str, bool]:
    changed = False
    pattern = re.compile(
        r"(?m)^  envVariables:\n((?:    [^\n]+\n)+)",
    )

    def repl(m: re.Match[str]) -> str:
        nonlocal changed
        changed = True
        lines = m.group(1).splitlines()
        vault_lines = ["  vault:"]
        for line in lines:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            key, val = s.split(":", 1)
            key, val = key.strip(), val.strip()
            if key == "APP_KEY":
                key = "APP_SECRET"
            if "generateRandomString" in val:
                vault_lines.append(f"    {key}:")
                vault_lines.append(f"      value: {val}")
                vault_lines.append("      sensitive: true")
            else:
                vault_lines.append(f"    {key}: {val}")
        return "\n".join(vault_lines) + "\n"

    return pattern.sub(repl, text), changed


def migrate_service_env_variables_to_vault(text: str) -> tuple[str, bool]:
    changed = False

    def repl(m: re.Match[str]) -> str:
        nonlocal changed
        changed = True
        body = m.group(1)
        return "    vault:\n" + body

    new_text, n = re.subn(
        r"^    envVariables:\n((?:      [^\n]+\n(?:      #[^\n]+\n)*)+)",
        repl,
        text,
        flags=re.MULTILINE,
    )
    return new_text, changed or n > 0


def migrate_service_env_secrets(text: str) -> tuple[str, bool]:
    """Service envSecrets -> vault; map APP_KEY/SECRET_KEY to APP_SECRET."""
    changed = False
    pattern = re.compile(
        r"^    envSecrets:\n((?:      [^\n]+\n)+)",
        re.MULTILINE,
    )

    def repl(m: re.Match[str]) -> str:
        nonlocal changed
        changed = True
        lines = m.group(1).splitlines()
        vault_lines = ["    vault:"]
        for line in lines:
            s = line.strip()
            if not s or s.startswith("#"):
                vault_lines.append("      " + s if s.startswith("#") else line)
                continue
            key, val = s.split(":", 1)
            key, val = key.strip(), val.strip()
            if key in ("APP_KEY", "SECRET_KEY"):
                key = "APP_SECRET"
            if key == "SECRET_TOKEN":
                key = "APM_SECRET"
            if "generateRandomString" in val:
                vault_lines.append(f"      {key}:")
                vault_lines.append(f"        value: {val}")
                vault_lines.append("        sensitive: true")
            else:
                vault_lines.append(f"      {key}: {val}")
        return "\n".join(vault_lines) + "\n"

    return pattern.sub(repl, text), changed


PROJECT_VAULT_DJANGO = """  vault:
    APP_SECRET:
      value: <@generateRandomString(<32>)>
      sensitive: true
    ADMIN_PASSWORD:
      value: <@generateRandomString(<12>)>
      sensitive: true

"""

PROJECT_VAULT_LARAVEL = """  vault:
    APP_SECRET:
      value: <@generateRandomString(<32>)>
      sensitive: true

"""


def migrate_project_level_service_secrets(text: str, vault_block: str) -> tuple[str, bool]:
    """Remove service envSecrets; add project vault once (django, laravel-jetstream)."""
    if "envSecrets:" not in text:
        return text, False
    text = re.sub(r"\n    envSecrets:\n(?:      [^\n]+\n)+", "\n", text)
    head = text.split("services:", 1)[0]
    if "vault:" not in head:
        text = re.sub(
            r"(project:\n  name: [^\n]+\n\n)",
            r"\1" + vault_block,
            text,
            count=1,
        )
    return text, True


def migrate_recipe_dir(recipe_dir: Path) -> bool:
    if not recipe_dir.is_dir():
        return False
    any_change = False
    had_env = False
    for import_path in sorted(recipe_dir.rglob("import.yaml")):
        original = import_path.read_text()
        text = original
        c = False
        text, c1 = migrate_project_env_variables(text)
        c |= c1
        text, c2 = migrate_service_env_variables_to_vault(text)
        c |= c2
        slug = recipe_dir.name
        if slug == "django":
            text, c3 = migrate_project_level_service_secrets(text, PROJECT_VAULT_DJANGO)
        elif slug == "laravel-jetstream":
            text, c3 = migrate_project_level_service_secrets(text, PROJECT_VAULT_LARAVEL)
        else:
            text, c3 = migrate_service_env_secrets(text)
        c |= c3
        if c and text != original:
            had_env = True
            import_path.write_text(text)
            any_change = True
        elif "envVariables:" in original or "envSecrets:" in original:
            had_env = True
    if _append_research(recipe_dir, had_env):
        any_change = True
    elif not had_env:
        any_change = _append_research(recipe_dir, False) or any_change
    return any_change


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: migrate-import-vault.py <recipe-slug>", file=sys.stderr)
        return 1
    slug = sys.argv[1]
    recipe_dir = Path.cwd() / slug
    if migrate_recipe_dir(recipe_dir):
        print(f"migrated {slug}")
        return 0
    print(f"no changes {slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
