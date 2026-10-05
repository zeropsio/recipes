# Medusa B2B — Zerops Recipe Research

## Overview

- **Software:** Medusa v2.21.0 B2B backend + admin; storefront in [medusa-b2b-frontend](https://github.com/zerops-recipe-apps/medusa-b2b-frontend)
- **Type:** framework (headless B2B commerce; TypeScript)
- **Official Site:** https://medusajs.com/
- **Zerops Runtime:** `nodejs@24`, `postgresql@17`, `valkey@7.2`, `meilisearch@1.10`, `object-storage`

## Zerops Compatibility Assessment

### Requirements

- [x] Stateless HTTP (catalog, sessions, and workflows live in Postgres + Valkey)
- [x] Supported runtime (`nodejs@24`; Medusa 2.21 wants Node `^20.19.0` or `>=22.12.0`)
- [x] Binds to a fixed port (backend `9000`)
- [x] Health endpoint (`GET /health`)

### Potential Issues

- Setups are only **`dev`** and **`prod`**. `medusadev` → `dev`. `medusastage` / `medusa` → `prod`. There is no `stage` setup.
- Storefront is a **separate** repo (`medusa-b2b-frontend`). Omit `nextstore*` services for backend-only (Mate / ZCP).
- This app repo is **Medusa only** at repository root (no `backend/` or `nextstore/` folders).
- `dev` deploys `./`; `prod` deploys `.medusa/server` + `node_modules`.
- Vault keys inject as-is. Do not write `STRIPE_API_KEY: ${STRIPE_API_KEY}`.
- `run.start` is omitted — platform default.
- Admin CORS is the backend origin (`API_URL`). Store CORS is `APP_URL` (localhost storefront).
- Keep `admin.path` at `/app`.

## Build Configuration

### Build Commands

```bash
yarn && yarn build   # prod
yarn                 # dev workspace
```

### Build Output

| Setup | Deploy paths |
|-------|----------------|
| `prod` | `.medusa/server/~`, `~node_modules` |
| `dev` | `./` |

## Runtime Configuration

No `start` key. Vault injects `JWT_SECRET`, `COOKIE_SECRET`, `SMTP_*`, `STRIPE_*`, `SUPERADMIN_*`.

`zerops.yml` remaps `API_URL` → `BACKEND_URL`, `APP_URL` → `STOREFRONT_URL`, and computes `DATABASE_URL`, `REDIS_URL`, `MINIO_*`, `MEILISEARCH_*`.

### Health Check

- Backend (`medusa-b2b`): HTTP `GET /health` on port 9000 (readiness + healthCheck)
- Storefront (`medusa-b2b-frontend`): HTTP `GET /api/health` on port 8000; `next start -H 0.0.0.0`; no `process.exit` in instrumentation or reload-env
- Publishable key: project `CHANNEL_PUBLISHABLE_KEY` after seed, else medusa `GET /internal/publishable-key` (requires `RELOAD_SECRET` on both services)
- Subdomain 502 with healthy container: `zcli service enable-subdomain nextstore` then `zcli service start nextstore`

## Database/Storage Requirements

- **PostgreSQL 17** — `oltp-hobby` rehearsal; **`oltp-staging` Small Production + HA demo**
- **Valkey 7.2** — `hobby` rehearsal; **`staging` Small Production + HA**
- **Meilisearch 1.10** — product index; no HA type
- **Object storage** — 2 GB non-HA; 10 GB HA
- **Mailpit** — Agent / Remote / Local only

## Service Dependencies

| Hostname | Type | Purpose | Priority |
|----------|------|---------|----------|
| db | postgresql | Medusa datasource | 10 |
| redis | valkey | Cache, events, workflows, locks, sessions | 10 |
| search | meilisearch | Product index | 10 |
| storage | object-storage | Product media | 10 |
| mailpit | go@1 (mailpit-app) | SMTP catcher (dev envs) | 10 |
| medusa / medusastage | nodejs@24 | `zeropsSetup: prod` | 6 |
| nextstore / nextstorestage | nodejs@24 | `zeropsSetup: prod` | 5 |
| medusadev / nextstoredev | nodejs@24 | `zeropsSetup: dev` | 5 |

## Scaling Considerations

| Setup | minRam | minFreeRamGB | Rationale |
|-------|--------|--------------|-----------|
| `prod` | **1 GB** | **0.5 GB** | Admin + API + B2B + workflows. 0.25 GB OOMs. |
| `dev` | **1 GB** | — | SSH workspace + `yarn dev`. |
| PostgreSQL / Valkey | profile only | — | Never `minFreeRamGB` on DB. |

**Cost ladder:** Stage (hobby) < Small Production (`oltp-staging` + same 1 GB floor, no `minContainers`) < HA (`:ha@`, `minContainers: 2`, 10 GB storage).

## Maintenance Guide

- Pin `@medusajs/*` to **2.21.0**.
- `yarn migrate` + `yarn syncLinks` after upgrades (`${appVersionId}`).
- Re-index: `yarn addInitialSearchDocuments`.

## Recipe detail / FAQ

See the app README FAQ fragment: why no storefront service, setup vs hostname, search, mail, vault passthrough, `dev` deploy of `./`. Community FAQ with Medusa voices is still open.

## References

- https://docs.medusajs.com/
- https://github.com/medusajs/b2b-starter
- https://github.com/zerops-recipe-apps/medusa-b2b
- https://docs.zerops.io/references/import-yaml/type-list

## Notes for Terminal Agent

- Closest sibling: `medusa-dtc`. Full-stack import by default; composability = omit nextstore services.
- Canonical `buildFromGit` is `zerops-recipe-apps/medusa-b2b`.
- Use `#zeropsPreprocessor=on` and project **vault**.
