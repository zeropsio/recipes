# Payload CMS — Zerops Recipe Research

## Overview

- **Software:** Payload CMS 3.x (Next.js-native admin + REST/GraphQL)
- **Type:** Next.js app on port **3000** (`/admin`, `/api/*`)
- **Zerops runtime:** `nodejs@24`, `postgresql@17`

## Setups

- Only **`dev`** and **`prod`** in app `zerops.yaml`.
- Recipe “Stage” tier uses **`zeropsSetup: prod`** on hostname `payload` / `payloadstage`.

## Repo

- `zerops-recipe-apps/payload` — CMS (Next standalone + Payload)

## Scaling

| Component | prod floor | Notes |
|-----------|------------|-------|
| Payload (Next build) | 1 GB, 0.5 free | Admin + API; heavy `next build` |
| Postgres stage | oltp-hobby | |
| Postgres small/HA demo | oltp-staging | |

## Composability

Import without storefront; use **`payload-next`** for Next.js frontend or any client via `API_URL`.

## References

- https://payloadcms.com/docs/production/deployment
- https://github.com/zerops-recipe-apps/payload
