# Payload + Next.js — Zerops Recipe Research

## Overview

- **Software:** Payload CMS 3.x + Next.js 16 storefront (SSR)
- **Type:** split repos — CMS + public site
- **Zerops runtime:** `nodejs@24` (both services), `postgresql@17` (CMS only)

## Setups

- Only **`dev`** and **`prod`** in each app `zerops.yaml`.
- Recipe “Stage” uses **`zeropsSetup: prod`** on `payload` / `frontend` (or `*stage` on Agent).

## Split repos

- `payload` — CMS, port 3000, admin + `/api`
- `payload-next-frontend` — Next standalone, `NEXT_PUBLIC_PAYLOAD_URL` → vault `API_URL`

## Scaling

| Component | prod floor | Notes |
|-----------|------------|-------|
| Payload CMS | 1 GB, 0.5 free | Next + Payload build |
| Next storefront | 0.5 GB | SSR standalone |
| Postgres | oltp-hobby / oltp-staging | Shared project DB for CMS |

## Composability

Omit `frontend*` services for CMS-only — use **`payload`** recipe.

## References

- https://payloadcms.com/docs/production/deployment
- https://github.com/zerops-recipe-apps/payload
- https://github.com/zerops-recipe-apps/payload-next-frontend
