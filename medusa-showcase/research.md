# Medusa — Zerops Recipe Research

## Overview

- **Software:** Medusa v2.19.0 backend + Next.js 16 storefront ([medusa-showcase-nextstore](https://github.com/zerops-recipe-apps/medusa-showcase-nextstore))
- **Type:** framework (headless commerce; TypeScript)
- **Official Site:** https://medusajs.com/
- **Zerops Runtime:** `nodejs@24` (both apps), `postgresql:single@17` / `postgresql:ha@17`, `valkey@7.2` (`:single@` / `:ha@`), `meilisearch@1.10`, `object-storage`

## Zerops Compatibility Assessment

### Requirements

- [x] Stateless HTTP (catalog, sessions, and workflows live in Postgres + Valkey)
- [x] Supported runtime (`nodejs@24`; Medusa 2.19 wants Node `^20.19.0` or `>=22.12.0`)
- [x] Binds to a fixed port (backend `9000`, storefront `8000`)
- [x] Health endpoint (`GET /health` on the backend)

### Potential Issues

- Only **`dev`** and **`prod`** setups. Local–HA: `medusa` + `nextstore` on `prod`. Agent / Remote: `*dev` workspaces + `*stage` on `prod`. Split `buildFromGit` for backend vs nextstore. Project vault `CHANNEL_PUBLISHABLE_KEY`; Mailpit on dev envs.
- Backend is Yarn **1.22** (classic lockfile). Storefront is Yarn **Berry 3.2.3** via Corepack. Do not switch either repo to npm.
- New Valkey services require a password. `zerops.yml` must use `${redis_connectionString}`, not `redis://${redis_hostname}:6379`.
- In-repo Meilisearch module (`src/modules/meilisearch/`). Do **not** add `@rokmohar/medusa-plugin-meilisearch` (breaks on 2.19).
- Admin CORS is the backend origin (`API_URL`), not the storefront. Store CORS includes `APP_URL` plus optional `ANALOG_STORE_URL`.
- First-deploy `initCommands` (`zsc execOnce`) migrate + sync-links per `${appVersionId}`; superadmin, seed, publishable key, and search index run once per service lifetime.
- Analog storefront is a **separate** recipe. Keep `ANALOG_STORE_URL` in the value store so CORS stays ready.
- Meilisearch has no `:ha@` type (single-node only). HA env still uses one search node.

## Build Configuration

### Build Commands

Split repos [`medusa-showcase`](https://github.com/zerops-recipe-apps/medusa-showcase) + [`medusa-showcase-nextstore`](https://github.com/zerops-recipe-apps/medusa-showcase-nextstore). `zerops.yml` uses `dev` / `prod` only. No Turbo — Yarn 1 backend + Yarn 3 storefront.

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
| `medusa` | `backend/.medusa/server/~`, `backend/tsconfig.json`, `backend/package.json`, `backend/node_modules`, `backend/src/scripts/seed-files` |
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

Project `import.yaml` **vault** is the value store (`envVariables` / `envSecrets` are deprecated). Apps map renamed keys in each `zerops.yml`. Identity maps (`JWT_SECRET: ${JWT_SECRET}`) are omitted.

| Value store | Required | Mapped in |
|-------------|----------|-----------|
| `APP_URL` | yes | Medusa `STOREFRONT_URL` / CORS; Next `NEXT_PUBLIC_BASE_URL` |
| `API_URL` | yes | Medusa `BACKEND_URL` / `ADMIN_CORS`; Next `MEDUSA_BACKEND_URL` |
| `NEXT_STORE_URL` / `MEDUSA_INSTANCE_URL` | aliases | Same URLs — kept for existing recipe buttons |
| `SEARCH_URL` | yes | Next `NEXT_PUBLIC_SEARCH_ENDPOINT` |
| `ANALOG_STORE_URL` | optional | Extra origin on Medusa `STORE_CORS` |
| `COOKIE_SECRET` / `JWT_SECRET` | yes (secrets) | Medusa session / JWT |
| `SMTP_*` / `STRIPE_*` / `GOOGLE_*` / `GITHUB_*` / `POSTHOG_*` | optional | Empty host/key disables the add-on |

No `envVariables` on import **service** blocks. Superadmin stays on the medusa service `vault`. Agent / Remote / Local include Mailpit (`SMTP_HOST: mailpit`).

### Health Check

- Backend: HTTP `GET /health` on port 9000 (readiness + healthCheck)
- Storefront: HTTP `GET /` on port 8000 (readiness)

## Database/Storage Requirements

- **PostgreSQL 17** — Medusa modules + links. `oltp-hobby` on agent / remote / local / stage; **`oltp-staging` on Small Production and HA demo**.
- **Valkey 7.2** — sessions, Caching Module, event bus, workflow engine, locking (one URL). `profile: hobby` on rehearsal tiers; **`profile: staging` on Small Production and HA**.
- **Meilisearch 1.10** — product index via the in-repo module.
- **Object storage (MinIO)** — product images, `public-read`, `forcePathStyle: true` in Medusa file-s3. 2 GB on non-HA; 10 GB on HA.

## Service Dependencies

| Hostname | Type | Purpose | Priority |
|----------|------|---------|----------|
| db | postgresql | Medusa datasource | 10 |
| redis | valkey | Cache, events, workflows, locks, sessions | 10 |
| search | meilisearch | Product search | 10 |
| storage | object-storage | Product media | 10 |
| medusa / medusastage | nodejs@24 | Backend (`zeropsSetup: prod`) | 6 |
| nextstore / nextstorestage | nodejs@24 | Storefront (`zeropsSetup: prod`) | 5 |
| mailpit | go@1 | SMTP catcher (Agent / Remote / Local) | 10 |
| medusadev / nextstoredev | nodejs@24 | Agent / Remote workspaces (`zeropsSetup: dev`) | 5 |

`nextstore` reads project vault `CHANNEL_PUBLISHABLE_KEY` after seed (`zsc setEnv` on the running medusa hostname, shared via `envIsolation`).

## Scaling Considerations

Floors from the app `zerops.yml` setups (production `yarn start` / `next start` — not `medusa develop`).

| Setup | minRam | minFreeRamGB | Rationale |
|-------|--------|--------------|-----------|
| `prod` (backend) | **1 GB** | **0.5 GB** | Admin UI + Store API + workflow engine + Redis clients. Platform default 0.25 GB OOMs on first boot. |
| `prod` (storefront) | **0.5 GB** | **0.25 GB** | Next.js SSR storefront on port 8000. |
| PostgreSQL | profile only | — | `oltp-hobby` rehearsal; `oltp-staging` Small Production + HA demo. Never `minFreeRamGB` on DB. |
| Valkey | profile only | — | `hobby` rehearsal; `staging` Small Production + HA. No duplicate `verticalAutoscaling`. |
| Meilisearch | omit / 1 GB HA | — | Demo catalog is tiny; HA bumps to 1 GB for index headroom. Single-node only. |

**Cost ladder**

- **Stage:** hobby Postgres + hobby Valkey + one container per app (1 + 0.5 GB floors) + 2 GB storage.
- **Small Production:** `oltp-staging` + Valkey `staging` + **same app floors** (required — omitting `verticalAutoscaling` would drop Medusa to the Node default and OOM). Omit `minContainers` (default 1).
- **HA:** `corePackage: SERIOUS`, `postgresql:ha@17` + `valkey:ha@7.2` (`oltp-staging` / `staging`, not `oltp-production`), `minContainers: 2` on both HTTP apps, shared CPU, 10 GB storage. Meilisearch stays single-node.

This is a **showcase** (two app repos + four data services), not a hello-world. Small Production still sets app `minRam` because the framework floor is above the platform default — documented exception to the hello-world “omit verticalAutoscaling” rule.

## Maintenance Guide

### Upgrades

- Pin every `@medusajs/*` package to **2.19.0**. Bump backend and storefront together.
- Keep Caching Module (`@medusajs/medusa/caching` + `@medusajs/caching-redis`) with `MEDUSA_FF_CACHING=true`.
- Re-run `yarn migrate` + `yarn syncLinks` after Medusa upgrades (already keyed by `${appVersionId}`).

### Data Migrations

- Schema: `zsc execOnce ${appVersionId}_migration -- yarn migrate`
- Links: `zsc execOnce ${appVersionId}_links -- yarn syncLinks`
- Demo seed / superadmin / publishable key / search index: once per service lifetime

## References

- https://docs.medusajs.com/ — Medusa v2
- https://docs.medusajs.com/resources/integrations — official add-ons
- https://github.com/zerops-recipe-apps/medusa-showcase — monorepo (`backend/` + `nextstore/`)
- https://docs.zerops.io/references/import-yaml/type-list — service types

## Notes for Terminal Agent

- Closest siblings: `nestjs-showcase` (multi-service + Valkey + Meilisearch + MinIO) and `analog-ssr-better-auth` (Small Production profiles, HA `:ha@` + `SERIOUS`).
- Canonical `buildFromGit` is `zerops-recipe-apps/medusa-showcase` for both medusa and nextstore services (same repo, different `zeropsSetup`).
- Use `#zeropsPreprocessor=on` for `${zeropsSubdomainHost}` and `<@generateRandomString(...)>`.
- Old GUI buttons (`medusa-next-devel` / `medusa-next-prod`) are a different Strapi slug. This folder / CMS slug is `medusa-showcase` (six environments).
- Cover SVG: `cover-nextjs.svg` until a Medusa-specific asset exists in recipe-shared-assets.
