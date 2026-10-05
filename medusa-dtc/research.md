# Medusa DTC — Zerops Recipe Research

## Overview

- **Software:** Medusa v2.21.0 DTC backend + official Next.js 15 storefront
- **Type:** framework (headless DTC commerce; TypeScript)
- **Official Site:** https://medusajs.com/
- **Zerops Runtime:** `nodejs@24` (both apps), `postgresql:single@17` / `postgresql:ha@17`, `valkey@7.2` (`:single@` / `:ha@`), `object-storage`

## Zerops Compatibility Assessment

### Requirements

- [x] Stateless HTTP (catalog, sessions, and workflows live in Postgres + Valkey)
- [x] Supported runtime (`nodejs@24`; Medusa 2.21 wants Node `^20.19.0` or `>=22.12.0`)
- [x] Binds to a fixed port (backend `9000`, storefront `8000`)
- [x] Health endpoint (`GET /health` on the backend; `GET /api/health` on the storefront)

### Potential Issues

- Local / Stage / Small / HA use hostnames `medusa` / `nextstore` (`zeropsSetup: medusa` / `nextstore`). AI Agent / Remote use `medusadev` + `nextstoredev` (idle `*-dev` setups, `zsc noop`) and `medusastage` + `nextstorestage` (prod `*-stage` setups). Stage storefront reads `${medusastage_CHANNEL_PUBLISHABLE_KEY}`.
- Backend is Yarn **1.22** (classic lockfile). Storefront is Yarn **Berry 3.2.3** via Corepack.
- New Valkey services require a password. `zerops.yml` must use `${redis_connectionString}`, not `redis://${redis_hostname}:6379`.
- Admin CORS is the backend origin (`API_URL`), not the storefront. Store CORS is `APP_URL`.
- First-deploy `initCommands` (`zsc execOnce`) migrate + sync-links per `${appVersionId}`; superadmin, seed, and publishable key run once per service lifetime.
- Combined API+admin: keep `admin.path` at `/app`. `GET /` redirects there. Do not set `path: "/"`.
- No Meilisearch in this recipe.

## Build Configuration

### Build Commands

Monorepo [`zerops-recipe-apps/medusa-dtc`](https://github.com/zerops-recipe-apps/medusa-dtc) — root `zerops.yml` with `medusa` / `nextstore` (Local–HA), `medusa-stage` / `nextstore-stage` and idle `medusa-dev` / `nextstore-dev` (AI Agent / Remote).

Backend (`backend/`):

```bash
cd backend && yarn && yarn build
```

Storefront (`nextstore/`):

```bash
corepack enable   # prepareCommands on nextstore setup
cd nextstore && yarn && yarn build
```

### Build Output

| Service | Deploy paths |
|---------|----------------|
| `medusa` | `backend/.medusa/server/~`, `backend/~node_modules` (package.json/tsconfig overlaid into `.medusa/server`) |
| `nextstore` | `nextstore/.next`, `nextstore/package.json`, `nextstore/next.config.js`, `nextstore/yarn.lock`, `nextstore/.yarnrc.yml`, `nextstore/node_modules`, `nextstore/public` |

### Caching Recommendations

- Backend: `node_modules`
- Storefront: `node_modules` only — do not cache `.next` (Zerops restore can hit `EACCES`)

## Runtime Configuration

### Start Command

```bash
# Backend
yarn start          # port 9000, admin at /app

# Storefront
./node_modules/.bin/next start -p 8000
```

### Environment Variables

Project `import.yaml` is a **value store**. Apps map keys in each `zerops.yml`.

| Value store | Required | Mapped in |
|-------------|----------|-----------|
| `APP_URL` | yes | Medusa `STOREFRONT_URL` / CORS; Next `NEXT_PUBLIC_BASE_URL` |
| `API_URL` | yes | Medusa `BACKEND_URL` / `ADMIN_CORS`; Next `MEDUSA_BACKEND_URL` |
| `COOKIE_SECRET` / `JWT_SECRET` | yes (secrets) | Medusa session / JWT |
| `STRIPE_*` | optional | Empty key disables Stripe |
| `RELOAD_SECRET` | yes (secret) | nextstore `/api/internal/reload-env` |

No `envVariables` on import **service** blocks. Superadmin stays `envSecrets` on `medusa`.

### Health Check

- Backend: HTTP `GET /health` on port 9000 (readiness + healthCheck)
- Storefront: HTTP `GET /api/health` on port 8000 (readiness + healthCheck); `next start -H 0.0.0.0`
- Storefront must not `process.exit` on boot or in `/api/internal/reload-env`; publishable key loads from vault or medusa `GET /internal/publishable-key`
- `enableSubdomainAccess: true` on `nextstore`; if public URL is 502 while in-project health passes: `zcli service enable-subdomain nextstore` then `zcli service start nextstore`

## Database/Storage Requirements

- **PostgreSQL 17** — Medusa modules + links. `oltp-hobby` on agent / remote / local / stage; **`oltp-staging` on Small Production and HA demo**.
- **Valkey 7.2** — sessions, Caching Module, event bus, workflow engine, locking (one URL). `profile: hobby` on rehearsal tiers; **`profile: staging` on Small Production and HA**.
- **Object storage (MinIO)** — product images, `public-read`, `forcePathStyle: true` in Medusa file-s3. 2 GB on non-HA; 10 GB on HA.

## Service Dependencies

| Hostname | Type | Purpose | Priority |
|----------|------|---------|----------|
| db | postgresql | Medusa datasource | 10 |
| redis | valkey | Cache, events, workflows, locks, sessions | 10 |
| storage | object-storage | Product media | 10 |
| medusa | nodejs@24 | Admin + Store / Admin API (`setup: medusa`) | 6 |
| nextstore | nodejs@24 | Official Next.js DTC storefront (`setup: nextstore`) | 5 |

`nextstore` reads `${medusa_CHANNEL_PUBLISHABLE_KEY}` after seed. On AI Agent / Remote the same key lives on hostname `medusastage` (`${medusastage_CHANNEL_PUBLISHABLE_KEY}`).

## Scaling Considerations

Floors from the app `zerops.yml` setups (production `yarn start` / `next start` — not `medusa develop`).

| Setup | minRam | minFreeRamGB | Rationale |
|-------|--------|--------------|-----------|
| `medusa` | **1 GB** | **0.5 GB** | Admin UI + Store API + workflow engine + Redis clients. Platform default 0.25 GB OOMs on first boot (proven on the Medusa showcase). |
| `nextstore` | **0.5 GB** | **0.25 GB** | Next.js 15 SSR storefront (`next start -p 8000`). |
| PostgreSQL | profile only | — | `oltp-hobby` rehearsal; `oltp-staging` Small Production + HA demo. Never `minFreeRamGB` on DB. |
| Valkey | profile only | — | `hobby` rehearsal; `staging` Small Production + HA. No duplicate `verticalAutoscaling`. |

**Cost ladder**

- **Stage:** hobby Postgres + hobby Valkey + one container per app (1 + 0.5 GB floors) + 2 GB storage.
- **Small Production:** `oltp-staging` + Valkey `staging` + **same app floors** (required — omitting `verticalAutoscaling` would drop Medusa to the Node default and OOM). Omit `minContainers` (default 1).
- **HA:** `corePackage: SERIOUS`, `postgresql:ha@17` + `valkey:ha@7.2` (`oltp-staging` / `staging`), `minContainers: 2` on both HTTP apps, shared CPU, 10 GB storage.

This is a **showcase** (two apps + three data services), not a hello-world. Small Production still sets app `minRam` because the framework floor is above the platform default.

## Maintenance Guide

### Upgrades

- Pin every `@medusajs/*` package to **2.21.0**. Bump backend and storefront together.
- Re-run `yarn migrate` + `yarn syncLinks` after Medusa upgrades (already keyed by `${appVersionId}`).

### Data Migrations

- Schema: `zsc execOnce ${appVersionId}_migration -- yarn migrate`
- Links: `zsc execOnce ${appVersionId}_links -- yarn syncLinks`
- Demo seed / superadmin / publishable key: once per service lifetime

## References

- https://docs.medusajs.com/ — Medusa v2
- https://github.com/medusajs/dtc-starter — official DTC starter
- https://github.com/zerops-recipe-apps/medusa-dtc — monorepo (`backend/` + `nextstore/`)
- https://docs.zerops.io/references/import-yaml/type-list — service types

## Notes for Terminal Agent

- Closest sibling: `medusa-showcase` (same flatten/init; this recipe drops Meilisearch).
- Canonical `buildFromGit` is `zerops-recipe-apps/medusa-dtc` for both services (same repo, different `zeropsSetup`).
- Canonical import YAMLs live in `zeropsio/recipes/medusa-dtc`. This folder is the optional paste-import copy.
- Use `#zeropsPreprocessor=on` for `${zeropsSubdomainHost}` and `<@generateRandomString(...)>`.
