# solidstart static hello world — Zerops Recipe Research

## Overview

- **Software:** SolidStart 1.3.2+ (solid-js 1.9.14+) static
- **Type:** framework
- **Zerops Runtime:** `nodejs@24` (and `postgresql@18` where the app uses a database)

## Repo

- App repo: `https://github.com/zerops-recipe-apps/solidstart-static-hello-world-app`

## Environment (vault)

Import uses `project.vault` / `service.vault` as the value store (not `envVariables` / `envSecrets` on services). Map keys explicitly in each app `zerops.yaml` — do not rely on auto-injection. Avoid self-references (e.g. `KEY: ${KEY}`).
