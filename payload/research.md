# Payload CMS — Zerops Recipe Research

## Overview

- **Software:** Payload CMS 3.90+ (Next.js admin + REST/GraphQL on port **3000**)
- **Type:** CMS / Next.js app (`/admin`, `/api/*`)
- **Zerops runtime:** `nodejs@24`, `postgresql@17`
- **App repo:** [zerops-recipe-apps/payload](https://github.com/zerops-recipe-apps/payload)

## Setups

- Only **`dev`** and **`prod`** in app `zerops.yaml`.
- Recipe “Stage” tier uses **`zeropsSetup: prod`** on hostname `payload` / `payloadstage`.

## Build / deploy (prod)

1. `npm ci --include=dev`
2. `npx payload migrate`
3. `npx payload generate:importmap` (required for Payload 3.90 admin dashboard)
4. `npm run build` → `next build` + `prepare-standalone` (`.npmrc` has `ignore-scripts=true`, so prepare is chained in the build script)
5. Deploy `.next/standalone`, `.next/static`, `public`
6. Start: `node .next/standalone/bin/run.mjs` (sets bind `0.0.0.0`; **never** `HOSTNAME` in zerops.yaml)

## Scaling considerations

| Tier / hostname | Payload app | Postgres | Notes |
|-----------------|-------------|----------|-------|
| Agent/Remote/Local `*dev` | platform default | oltp-hobby | SSH + `npm run dev` |
| Agent `payloadstage` | 0.5 GB, 0.25 free | oltp-hobby | Stage rehearsal |
| Stage `payload` | 0.5 GB, 0.25 free | oltp-hobby | Lighter than small prod |
| Small prod / HA `payload` | 1 GB, 0.5 free | oltp-staging | `next build` + Payload admin |
| HA | `:ha@` + `corePackage: SERIOUS` where applicable | oltp-staging | |

## Composability

CMS-only recipe. Full stack: **`payload-next`** (+ `payload-next-frontend`) or any client via vault **`API_URL`**.

## Operations

- **`enableSubdomainAccess: true`** on services — required for public HTTPS.
- Admin import map must match `@payloadcms/next/rsc#CollectionCards` after Payload upgrades — regenerate on build.

## References

- https://payloadcms.com/docs/production/deployment
- https://github.com/zerops-recipe-apps/payload
