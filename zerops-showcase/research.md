# Zerops Showcase — Zerops Recipe Research

## Overview

- **Software:** Bun + React 19.3 frontend, Python 3.12 worker
- **Type:** framework
- **Zerops Runtime:** `nodejs@24` / Bun frontend, `python@3.12` worker, PostgreSQL, Valkey, NATS, object storage

## Repo

- App repo: `https://github.com/zerops-recipe-apps/showcase-recipe-app`

## Environment (vault)

Import uses `project.vault` / `service.vault` as the value store (not `envVariables` / `envSecrets` on services). Map keys explicitly in each app `zerops.yaml` — do not rely on auto-injection. Avoid self-references (e.g. `KEY: ${KEY}`).
