# Payload + Next.js — Zerops Recipe Research

## Overview

- **Software:** Payload CMS 3.90+ + Next.js 16 storefront (SSR, standalone)
- **Type:** split repos — CMS + public site
- **Zerops runtime:** `nodejs@24` (both services), `postgresql@17` (CMS only)

## Split repos

| Repo | Role | Port |
|------|------|------|
| [payload](https://github.com/zerops-recipe-apps/payload) | CMS, admin, REST | 3000 |
| [payload-next-frontend](https://github.com/zerops-recipe-apps/payload-next-frontend) | Storefront | 3000 |

Storefront **`NEXT_PUBLIC_PAYLOAD_URL`** at build (template hostname) and runtime (`${API_URL}`). Server Components fetch Payload REST — no browser CORS.

## Setups

- Only **`dev`** and **`prod`** in each app `zerops.yaml`.
- Recipe “Stage” uses **`zeropsSetup: prod`** on `payloadstage` / `frontendstage` (Agent) or `payload` / `frontend` (Stage folder).

## Scaling considerations

| Component | Small prod floor | Stage / dev | Notes |
|-----------|------------------|-------------|-------|
| Payload CMS | 1 GB, 0.5 free | 0.5 GB, 0.25 free (`*stage`) | migrate + importmap + next build |
| Next storefront | 0.5 GB, 0.25 free | 0.5 GB on `frontenddev` | standalone + prepare-standalone |
| Postgres | oltp-staging (small/HA) | oltp-hobby (stage/agent) | Single DB for CMS |

## Composability

Omit **`frontend*`** services for CMS-only — use **`payload`** recipe.

## Operations

- Payload: same prod pipeline as CMS-only recipe (`generate:importmap`, standalone `bin/run.mjs`).
- Storefront: `node .next/standalone/bin/run.mjs`; do not set `HOSTNAME` in zerops.yaml.
- **`enableSubdomainAccess: true`** on all HTTP services.
- Vault **`APP_URL`** / **`DEV_APP_URL`** use the routed hostname `https://frontend{,stage,dev}-${zeropsSubdomainHost}-3000.prg1.zerops.app` (port suffix), matching **`API_URL`** — not the portless `frontend-{host}.prg1.zerops.app` alias.

## References

- https://payloadcms.com/docs/production/deployment
- https://github.com/zerops-recipe-apps/payload
- https://github.com/zerops-recipe-apps/payload-next-frontend
