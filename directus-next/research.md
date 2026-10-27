# Directus + Next.js — Zerops Recipe Research

## Overview

- **CMS:** Directus 12 — same stack as [directus](../directus/) recipe
- **Frontend:** Next.js 16 App Router, standalone, ISR 60s
- **Repos:** `zerops-directus-cms` + `zerops-directus-nextjs-blog`

## Setups

| Service | Setup |
|---------|--------|
| `directus*` | `development` / `production` |
| `frontend*` | `dev` / `nextjs` |

## Scaling

| Component | floor |
|-----------|--------|
| Directus | 1 GB |
| Next frontend | 0.5 GB |

## Environment (vault)

`API_URL`, `APP_URL`, `SECRET`, `ADMIN_TOKEN` at project level; `ADMIN_PASSWORD` on Directus service vault.
