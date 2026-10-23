#!/usr/bin/env python3
"""Generate directus + directus-next recipe import trees."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CMS_GIT = "https://github.com/zerops-recipe-apps/directus"
NEXT_GIT = "https://github.com/zerops-recipe-apps/directus-next-frontend"
MAILPIT_GIT = "https://github.com/zerops-recipe-apps/mailpit-app"

HEADER_CMS = """#zeropsPreprocessor=on
# yaml-language-server: $schema=https://api.app-prg1.zerops.io/api/rest/public/settings/import-project-yaml-json-schema.json

# Directus showcase — zerops-directus-cms (PostgreSQL, Valkey, S3, optional Mailpit).
# Setups: `development` and `production` in app zerops.yaml.
# Vault: SECRET + APP_URL / API_URL (+ DEV_* on Agent/Remote). Map ADMIN_* on directus service.
"""

HEADER_NEXT = """#zeropsPreprocessor=on
# yaml-language-server: $schema=https://api.app-prg1.zerops.io/api/rest/public/settings/import-project-yaml-json-schema.json

# Directus + Next.js blog — CMS repo + zerops-directus-nextjs-blog.
# Setups: CMS `development` / `production`; frontend `nextjs` / `dev`.
# Vault: SECRET, ADMIN_TOKEN, APP_URL, API_URL (+ DEV_*). Frontend maps DIRECTUS_* in zerops.yaml.
"""


def vault_cms(agent: bool, name: str, extra: str = "") -> str:
    if agent:
        urls = """    APP_URL: https://directusstage-${zeropsSubdomainHost}-8055.prg1.zerops.app
    API_URL: https://directusstage-${zeropsSubdomainHost}-8055.prg1.zerops.app
    DEV_APP_URL: https://directusdev-${zeropsSubdomainHost}-8055.prg1.zerops.app
    DEV_API_URL: https://directusdev-${zeropsSubdomainHost}-8055.prg1.zerops.app
"""
    else:
        urls = """    APP_URL: https://directus-${zeropsSubdomainHost}-8055.prg1.zerops.app
    API_URL: https://directus-${zeropsSubdomainHost}-8055.prg1.zerops.app
    DEV_APP_URL: https://directus-${zeropsSubdomainHost}-8055.prg1.zerops.app
    DEV_API_URL: https://directus-${zeropsSubdomainHost}-8055.prg1.zerops.app
"""
    return f"""project:
  name: {name}
{extra}  vault:
{urls}
    SECRET:
      value: <@generateRandomString(<64>)>
      sensitive: true
    ADMIN_TOKEN:
      value: <@generateRandomString(<40>)>
      sensitive: true


"""


def vault_next(agent: bool, name: str, extra: str = "") -> str:
    if agent:
        urls = """    APP_URL: https://frontendstage-${zeropsSubdomainHost}.prg1.zerops.app
    API_URL: https://directusstage-${zeropsSubdomainHost}-8055.prg1.zerops.app
    DEV_APP_URL: https://frontenddev-${zeropsSubdomainHost}.prg1.zerops.app
    DEV_API_URL: https://directusdev-${zeropsSubdomainHost}-8055.prg1.zerops.app
"""
    else:
        urls = """    APP_URL: https://frontend-${zeropsSubdomainHost}.prg1.zerops.app
    API_URL: https://directus-${zeropsSubdomainHost}-8055.prg1.zerops.app
    DEV_APP_URL: https://frontend-${zeropsSubdomainHost}.prg1.zerops.app
    DEV_API_URL: https://directus-${zeropsSubdomainHost}-8055.prg1.zerops.app
"""
    return f"""project:
  name: {name}
{extra}  vault:
{urls}
    SECRET:
      value: <@generateRandomString(<64>)>
      sensitive: true
    ADMIN_TOKEN:
      value: <@generateRandomString(<40>)>
      sensitive: true


"""


def db_hobby() -> str:
    return """  - hostname: db
    type: postgresql:single@17
    profile: oltp-hobby
    priority: 10
"""


def db_staging() -> str:
    return """  - hostname: db
    type: postgresql:single@17
    profile: oltp-staging
    priority: 10
"""


def db_ha() -> str:
    return """  - hostname: db
    type: postgresql:ha@17
    profile: oltp-staging
    priority: 10
"""


def cache_single() -> str:
    return """  - hostname: cache
    type: valkey:single@7.2
    priority: 9
"""


def cache_ha() -> str:
    return """  - hostname: cache
    type: valkey:ha@7.2
    priority: 9
"""


def storage(size: int) -> str:
    return f"""  - hostname: storage
    type: object-storage
    priority: 8
    objectStorageSize: {size}
    objectStoragePolicy: public-read
"""


def mailpit() -> str:
    return f"""  - hostname: mailpit
    type: alpine@3.21
    buildFromGit: {MAILPIT_GIT}
    enableSubdomainAccess: true
"""


def directus_svc(
    hostname: str,
    setup: str,
    min_c: int = 1,
    max_c: int = 1,
    min_ram: float = 1,
    seed: str = "1.0.0",
) -> str:
    max_ram = 16 if max_c > 1 else 4
    scaling = f"""    verticalAutoscaling:
      minRam: {min_ram}
      maxRam: {max_ram}
"""
    if max_c > 1:
        scaling += f"""    minContainers: {min_c}
    maxContainers: {max_c}
"""
    return f"""  - hostname: {hostname}
    type: alpine/nodejs@24
    priority: 6
    zeropsSetup: {setup}
    buildFromGit: {CMS_GIT}
    enableSubdomainAccess: true
{scaling}    vault:
      ADMIN_EMAIL: admin@example.com
      ADMIN_PASSWORD:
        value: <@generateRandomString(<20>)>
        sensitive: true
      SEED_VERSION: "{seed}"
    envIsolation: service
"""


def frontend_svc(hostname: str, setup: str, min_ram: float = 0.5) -> str:
    return f"""  - hostname: {hostname}
    type: ubuntu/nodejs@24
    priority: 5
    zeropsSetup: {setup}
    buildFromGit: {NEXT_GIT}
    enableSubdomainAccess: true
    verticalAutoscaling:
      minRam: {min_ram}
      minFreeRamGB: 0.25
    envIsolation: service
"""


def write_env(slug: str, folder: str, body: str, intro: str) -> None:
    base = ROOT / slug / folder
    base.mkdir(parents=True, exist_ok=True)
    (base / "import.yaml").write_text(body)
    title = folder.split("—", 1)[-1].strip()
    readme = f"""# {slug.replace('-', ' ').title()} — {title}

Environment for [{slug.replace('-', ' ').title()}](https://app.zerops.io/recipes/{slug}) on Zerops.

<!-- #ZEROPS_EXTRACT_START:intro# -->
{intro}
<!-- #ZEROPS_EXTRACT_END:intro# -->
"""
    (base / "README.md").write_text(readme)


def main() -> None:
    # ── directus CMS-only ─────────────────────────────────────────────
    agent_body = (
        HEADER_CMS
        + vault_cms(True, "directus-agent")
        + "services:\n"
        + db_hobby()
        + "\n"
        + cache_single()
        + "\n"
        + storage(10)
        + "\n"
        + mailpit()
        + "\n"
        + directus_svc("directusdev", "development")
        + "\n"
        + directus_svc("directusstage", "production", min_c=1, max_c=1)
    )
    write_env(
        "directus",
        "0 — AI Agent",
        agent_body,
        "**AI agent** — `directusdev` (`development`) and `directusstage` (`production`) with Valkey, S3, Mailpit, and demo seed.",
    )
    write_env(
        "directus",
        "1 — Remote (CDE)",
        agent_body.replace("name: directus-agent", "name: directus-remote-cde"),
        "**Remote (CDE)** — same topology as AI agent on hobby PostgreSQL.",
    )

    local_body = (
        HEADER_CMS
        + vault_cms(False, "directus-local")
        + "services:\n"
        + db_hobby()
        + "\n"
        + cache_single()
        + "\n"
        + storage(10)
        + "\n"
        + mailpit()
        + "\n"
        + directus_svc("directus", "development")
    )
    write_env(
        "directus",
        "2 — Local",
        local_body,
        "**Local** — single `directus` (`development`) with Mailpit; SSH + `npx directus start` after bootstrap.",
    )

    stage_body = (
        HEADER_CMS
        + vault_cms(False, "directus-stage")
        + "services:\n"
        + db_hobby()
        + "\n"
        + cache_single()
        + "\n"
        + storage(10)
        + "\n"
        + directus_svc("directus", "production", min_c=1, max_c=1)
    )
    write_env(
        "directus",
        "3 — Stage",
        stage_body,
        "**Stage** — single `directus` on `production` setup, hobby Postgres, no Mailpit.",
    )

    small_body = (
        HEADER_CMS
        + vault_cms(False, "directus-small-prod")
        + "services:\n"
        + db_staging()
        + "\n"
        + cache_single()
        + "\n"
        + storage(10)
        + "\n"
        + directus_svc("directus", "production", min_c=2, max_c=4)
    )
    write_env(
        "directus",
        "4 — Small Production",
        small_body,
        "**Small production** — `oltp-staging` Postgres, two Directus containers, Valkey + S3.",
    )

    ha_body = (
        HEADER_CMS
        + vault_cms(False, "directus-ha-prod", extra="  corePackage: SERIOUS\n")
        + "services:\n"
        + db_ha()
        + "\n"
        + cache_ha()
        + "\n"
        + storage(50)
        + "\n"
        + directus_svc("directus", "production", min_c=2, max_c=6)
    )
    write_env(
        "directus",
        "5 — Highly-available Production",
        ha_body,
        "**HA** — HA Postgres + Valkey, 2–6 Directus containers, 50 GB object storage.",
    )

    # ── directus-next ─────────────────────────────────────────────────
    def next_agent(name: str) -> str:
        return (
            HEADER_NEXT
            + vault_next(True, name)
            + "services:\n"
            + db_hobby()
            + "\n"
            + cache_single()
            + "\n"
            + storage(10)
            + "\n"
            + mailpit()
            + "\n"
            + directus_svc("directusdev", "development")
            + "\n"
            + directus_svc("directusstage", "production", min_c=1, max_c=1)
            + "\n"
            + frontend_svc("frontenddev", "dev")
            + "\n"
            + frontend_svc("frontendstage", "nextjs")
        )

    write_env(
        "directus-next",
        "0 — AI Agent",
        next_agent("directus-next-agent"),
        "**AI agent** — Directus dev/stage + Next.js dev/stage; vault wires `API_URL` → blog `DIRECTUS_URL`.",
    )
    write_env(
        "directus-next",
        "1 — Remote (CDE)",
        next_agent("directus-next-remote-cde"),
        "**Remote (CDE)** — same as AI agent.",
    )

    next_local = (
        HEADER_NEXT
        + vault_next(False, "directus-next-local")
        + "services:\n"
        + db_hobby()
        + "\n"
        + cache_single()
        + "\n"
        + storage(10)
        + "\n"
        + mailpit()
        + "\n"
        + directus_svc("directus", "development")
        + "\n"
        + frontend_svc("frontend", "dev")
    )
    write_env(
        "directus-next",
        "2 — Local",
        next_local,
        "**Local** — Directus `development` + Next `dev` with Mailpit.",
    )

    next_stage = (
        HEADER_NEXT
        + vault_next(False, "directus-next-stage")
        + "services:\n"
        + db_hobby()
        + "\n"
        + cache_single()
        + "\n"
        + storage(10)
        + "\n"
        + directus_svc("directus", "production", min_c=1, max_c=1)
        + "\n"
        + frontend_svc("frontend", "nextjs")
    )
    write_env(
        "directus-next",
        "3 — Stage",
        next_stage,
        "**Stage** — single Directus + Next on production/`nextjs` setups.",
    )

    next_small = (
        HEADER_NEXT
        + vault_next(False, "directus-next-small-prod")
        + "services:\n"
        + db_staging()
        + "\n"
        + cache_single()
        + "\n"
        + storage(10)
        + "\n"
        + directus_svc("directus", "production", min_c=2, max_c=4)
        + "\n"
        + frontend_svc("frontend", "nextjs", min_ram=0.5)
    )
    write_env(
        "directus-next",
        "4 — Small Production",
        next_small,
        "**Small production** — two Directus containers + Next blog; `ADMIN_TOKEN` in project vault.",
    )

    next_ha = (
        HEADER_NEXT
        + vault_next(False, "directus-next-ha-prod", extra="  corePackage: SERIOUS\n")
        + "services:\n"
        + db_ha()
        + "\n"
        + cache_ha()
        + "\n"
        + storage(50)
        + "\n"
        + directus_svc("directus", "production", min_c=2, max_c=6)
        + "\n"
        + frontend_svc("frontend", "nextjs")
    )
    write_env(
        "directus-next",
        "5 — Highly-available Production",
        next_ha,
        "**HA** — HA data plane + scaled Directus + Next frontend.",
    )

    print("generated directus + directus-next environments")


if __name__ == "__main__":
    main()
