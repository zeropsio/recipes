# Wasp — Zerops Recipe Research

## Overview

- **Software:** Wasp v0.25.0
- **Type:** framework (full-stack TypeScript)
- **Official Site:** https://wasp.sh/
- **Zerops Runtime:** `nodejs@24` (build + API), `static` (client), `postgresql:single@16` / `postgresql:ha@16`

## Zerops Compatibility Assessment

### Requirements

- [x] Stateless API (state in PostgreSQL)
- [x] Supported runtime available (`nodejs@24`, Wasp 0.25 requires Node `>=24.14.1`)
- [x] Binds to `PORT` (default 3001 on server)
- [x] No local filesystem state required at runtime

### Potential Issues

- Wasp CLI must be installed in the build container (`npm install -g @wasp.sh/wasp-cli@0.25.0`).
- Prisma install scripts conflict with default `ignore-scripts=true` in recipe `.npmrc` — use `npm install --ignore-scripts=false` in build commands only.
- Client and server deploy separately ([self-hosted architecture](https://wasp.sh/docs/deployment/deployment-methods/self-hosted)); recipe uses two Zerops services from one git repo via `prod-client` and `prod-api` setups.
- `REACT_APP_API_URL` must be set before `vite build` (Wasp 0.25 client env).

## Build Configuration

### Build Commands

```bash
npm install --ignore-scripts=false
npm install -g @wasp.sh/wasp-cli@0.25.0 --ignore-scripts=false
wasp build
npm run build:client   # client service only
cd .wasp/out/server && npm run bundle   # API service only
```

### Build Output

| Service | Deploy paths |
|---------|----------------|
| Client (`prod-client`) | `.wasp/out/web-app/build/` |
| API (`prod-api`) | `node_modules/`, `.wasp/out/server/bundle`, `.wasp/out/server/node_modules`, `.wasp/out/db` |

### Caching Recommendations

- `node_modules`
- `.wasp/out` (Wasp codegen + nested installs)

## Runtime Configuration

### Start Command

```bash
# API
cd .wasp/out/server && npm run start-production
```

Client: Zerops `static` (Nginx).

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `PORT` | API | Server port (default 3001) |
| `DATABASE_URL` | API | PostgreSQL connection string |
| `APP_URL` | Project import | Public SPA URL — `zerops.yaml` maps to `WASP_WEB_CLIENT_URL` |
| `API_URL` | Project import | Public API URL — `zerops.yaml` maps to `WASP_SERVER_URL` and `REACT_APP_API_URL` |
| `NODE_ENV` | API | `production` in prod |

Project `import.yaml` stores `APP_URL` / `API_URL` only (no per-service `envVariables`). Wasp runtime keys are wired in `zerops.yaml`.

### Health Check

- API: HTTP `GET /auth/me` on port 3001 (readinessCheck in `zerops.yaml`).

## Database/Storage Requirements

- **Type:** PostgreSQL (Prisma)
- **Initialization:** `prisma migrate deploy` via `npm run db-migrate-prod` in `.wasp/out/server`
- **Profile:** `oltp-hobby` (local/dev/remote/small prod), `oltp-staging` (stage), `oltp-production` (HA prod only)

## Service Dependencies

| Service | Type | Purpose | Priority |
|---------|------|---------|----------|
| db | postgresql | Prisma datasource | 10 |
| appdev / apidev | nodejs@24 | Wasp dev workspace (`wasp start`) | 5 |
| appstage / app | static | React SPA (prod-client) | 5 |
| apistage / api | nodejs@24 | Wasp server (prod-api) | 5 |

## Scaling Considerations

- Static client: low RAM, `minContainers: 2` in production.
- API: SSR-less Express server; 0.25–0.5 GB RAM floor for small prod.
- HA: `:ha@` PostgreSQL, `corePackage: SERIOUS`, dedicated CPU on API.

## Maintenance Guide

### Upgrades

- Bump `@wasp.sh/wasp-cli` and `wasp: { version }` in `main.wasp.ts` together.
- Re-run `wasp build` after Wasp upgrades; check breaking changes in Wasp changelog.

### Data Migrations

- `zsc execOnce ${appVersionId} -- sh -c 'cd .wasp/out/server && npm run db-migrate-prod'`

## References

- https://wasp.sh/ — framework overview
- https://wasp.sh/docs/deployment/deployment-methods/self-hosted — client + server split
- https://docs.zerops.io/zerops-yaml/specification — pipeline config

## Notes for Terminal Agent

- Closest sibling: `nestjs-showcase` (app/api dev-stage pairs + PostgreSQL).
- Single app repo, three `zerops.yaml` setups: `dev`, `prod-client`, `prod-api`.
- Use `#zeropsPreprocessor=on` for subdomain URL env vars in `import.yaml`.
