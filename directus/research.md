# Directus — Zerops Recipe Research

## Overview

- **Software:** Directus 11 (npm / Alpine Node 22)
- **Type:** API + Data Studio (`/admin`)
- **Zerops Runtime:** `alpine/nodejs@22`, `postgresql@17`, `valkey@7.2`, `object-storage`

## Setups

- **`development`** and **`production`** in [zerops-directus-cms](https://github.com/kristiyan-velkov/zerops-directus-cms) `zerops.yaml` (extends `base`).
- Recipe stage/small-prod use **`zeropsSetup: production`** on hostname `directus` / `directusstage`.

## Repos

| Repo | Role |
|------|------|
| `kristiyan-velkov/zerops-directus-cms` | CMS (target: `zerops-recipe-apps/directus`) |
| `kristiyan-velkov/zerops-directus-nextjs-blog` | Next blog (target: `zerops-recipe-apps/directus-next-frontend`) |

## Scaling

| Component | prod floor | Notes |
|-----------|------------|-------|
| Directus | 1 GB | Cold start bootstrap + schema + seed |
| Valkey | single / HA | Required for cache + multi-container sync |
| Postgres stage | oltp-hobby | |
| Postgres small/HA | oltp-staging / HA | |

## Composability

CMS-only import; frontend via [directus-next](../directus-next/) or any client using vault `API_URL` and optional `ADMIN_TOKEN`.

## References

- https://directus.io/docs
- https://github.com/kristiyan-velkov/zerops-directus-cms

## Environment (vault)

Import uses `project.vault` / `service.vault` as the value store. Map keys explicitly in app `zerops.yaml` (`PUBLIC_URL`, `SECRET`, ties to `$db_*`, `$storage_*`, `$cache_*`).
