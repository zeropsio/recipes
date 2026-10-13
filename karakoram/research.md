# Karakoram — Zerops Recipe Research

## Overview

- **Software:** Karakoram (self-hosted MongoDB orchestration for Zerops)
- **Type:** oss-source (build from public Git; pipeline in upstream `zerops.yaml`)
- **Official Site:** https://karakoram.dev
- **Source:** https://github.com/KarakoramDev/Karakoram (Apache-2.0)
- **Zerops Runtime:** `ubuntu@24.04` (run). Build uses `go@1` + `nodejs@22` from upstream `zerops.yaml`.
- **Sibling recipes:** `umami` / `elk` (OSS `_template_oss`, two environments); `elk` also uses `ubuntu@24.04` + `maxContainers: 1` for a stateful coordinator.

This recipe does **not** fork the app into `zerops-recipe-apps`. `buildFromGit` points at the upstream repository. The only setup name in that `zerops.yaml` is `karakoram`.

## Zerops Compatibility Assessment

### Requirements

- [x] State externalized — SQLite on Local Storage (`karakoramdata`), not the disposable runtime disk
- [x] Supported runtime — `ubuntu@24.04` ([type list](https://docs.zerops.io/references/import-yaml/type-list)); build bases `go@1`, `nodejs@22`
- [x] HTTP bind — port 8080 with `httpSupport: true`; health check `/healthz`
- [x] Filesystem — `run.volume.hostname: karakoramdata` → `/mnt/karakoramdata`

### Potential Issues

- **Single-writer control plane.** SQLite WAL forbids a second replica. `maxContainers: 1` and `deploy.temporaryShutdown: true` are correctness constraints. Production is **not** HA for the control plane (documented upstream limitation).
- **Project token after import.** Karakoram needs a project-scoped **Full access** integration token (`KARAKORAM_ZEROPS_TOKEN`). The token cannot exist before the recipe creates the project. Import leaves the secret empty; the operator pastes it and restarts. Do not name this `ZEROPS_TOKEN` (`userDataZeropsPrefixForbidden`).
- **No `dev` / `prod` setups.** Upstream pipeline is one setup (`karakoram`). AI Agent / Remote 6-env topology would require forking the app. OSS Development + Production is the honest fit.
- **Members are created later.** The recipe only imports the control plane + volume. Replica sets, shards, mongos and PBM backup storage are provisioned in-app inside this same project.
- **Local Storage minimum is 5 GB.** Mounted size follows **maxDisk**, not minDisk. Shrinking is rejected.
- **Go toolchain.** Zerops `go@1` currently starts at Go 1.22; `go.mod` `go 1.24.0` downloads the toolchain at build time. Build needs outbound access to Go module/toolchain registries and npm.

## Build Configuration

Refer to: https://docs.zerops.io/features/pipeline

Upstream `zerops.yaml` (`- setup: karakoram`):

### Build Commands

```bash
cd ui && npm ci && npm run build
CGO_ENABLED=0 go build -tags ui -trimpath \
  -ldflags "-s -w -X …Version/Commit/BuildDate…" \
  -o karakoram ./cmd/karakoram
```

### Build Dependencies

- Node 22 + npm (embedded React UI)
- Go 1.24+ via automatic toolchain download
- Git (short commit in ldflags; missing git prints `unknown`)

### Build Output

- Single static binary: `karakoram` (`deployFiles: [karakoram]`)

### Caching Recommendations

Upstream does not set `build.cache`. Optional later (do not change the app in this recipe): `ui/node_modules`, Go module cache.

## Runtime Configuration

### Start Command

```bash
./karakoram server
```

### Environment Variables

Refer to: https://docs.zerops.io/features/env-variables

Pipeline-injected in upstream `zerops.yaml` (do **not** duplicate in import):

| Variable | Required | Description |
|----------|----------|-------------|
| `KARAKORAM_DATA_DIR` | Yes | `/mnt/karakoramdata` |
| `KARAKORAM_ZEROPS_PROJECT_ID` | Yes | `${projectId}` |
| `KARAKORAM_PUBLIC_URL` | Yes | `${zeropsSubdomain}` (HTTPS origin). Custom domain: change this in `zerops.yaml` and redeploy — a service secret with the same key does **not** override pipeline runtime vars. |

Service secrets (import `vault:` on `karakoram` only — never project-level, never `ZEROPS_*` names):

| Variable | Required | Description |
|----------|----------|-------------|
| `KARAKORAM_MASTER_KEY` | Yes | 48 generated chars; encrypts stored credentials; preserve for the life of the SQLite DB |
| `KARAKORAM_ADMIN_PASSWORD` | Yes | 24 generated chars; bootstrap `admin` only; changing the secret later does not reset the account |
| `KARAKORAM_ZEROPS_TOKEN` | Yes (after import) | Project-scoped Full access integration token |
| `KARAKORAM_BACKUP_ENDPOINT_ALLOWLIST` | Optional | Private S3 verifier allowlist |
| `KARAKORAM_ZEROPS_API_URL` | Optional | Non-default Zerops API |
| `KARAKORAM_RECOVERY_PASSWORD` | Recovery only | Temporary local-admin reset; delete after use |

### Health Check

- Endpoint: `GET /healthz` on port 8080
- Upstream `readinessCheck.httpGet` with `failureTimeout: 120s`
- Port 9443 is private agent TLS — do not publish

## Database/Storage Requirements

### Database

- Control-plane state: **SQLite** on Local Storage (`karakoram.db`), not managed PostgreSQL/MongoDB.
- MongoDB (PSMDB) members are **not** in this import; Karakoram creates them via the Zerops API.

### Object Storage

- Required at import: **no**
- Use case: PBM backups / PITR, configured in the Karakoram UI against S3-compatible storage (Zerops object storage is supported; `storage-prg1.zerops.io` is trusted by default).

## Service Dependencies

Refer to: https://docs.zerops.io/references/import-yaml/type-list

| Service | Type | Purpose | Priority |
|---------|------|---------|----------|
| karakoramdata | `local-storage:single@1` | SQLite volume (5 GB min; capacity = maxDisk) | 10 |
| karakoram | `ubuntu@24.04` | Control plane, UI, API | default (after volume) |

No managed Postgres/Valkey/NATS in the recipe. `envIsolation: service` keeps master key / token off member services Karakoram creates later.

## Scaling Considerations

Refer to: https://docs.zerops.io/features/scaling-ha

Per-setup RAM floors (from upstream `deploy/zerops/import.yaml` + install guide):

| Setup | Runtime | minRam | Notes |
|-------|---------|--------|-------|
| `karakoram` | Ubuntu 24.04, static Go binary + SQLite | **0.5 GB** | Upstream range 0.5–1 GB shared CPU. Compiled Go, not Node SSR. `minFreeRamGB` omitted (0.25 would be the platform default for 0.5). |

| Environment | Control plane | Volume | HA? |
|-------------|---------------|--------|-----|
| Development | `minRam: 0.5`, `maxContainers: 1`, shared CPU | 5 GB (`minDisk`/`maxDisk`: 5) | No — SQLite + Local Storage are single-host |
| Production | same RAM floor, `maxContainers: 1` | 5 GB min, **maxDisk 10** so the volume can grow | **No control-plane HA.** Do not set `minContainers: 2` or `corePackage: SERIOUS` for this topology. MongoDB replica-set HA is created later in-app and is still subject to Zerops anti-affinity limitations. |

`maxContainers: 1` is **not** a cost ceiling — a second writer corrupts SQLite. Omit `maxRam` (upstream used 1 GB as an optional cap). LIGHT core is enough for the control plane; budget extra project capacity for members the operator creates.

## Maintenance Guide

### Upgrades

- Re-trigger the `karakoram` Git pipeline (pulls current `main` unless `buildFromGit` is pinned).
- Control-plane upgrades use `temporaryShutdown` — brief management downtime, not zero-downtime.
- Follow upstream [upgrade docs](https://github.com/KarakoramDev/Karakoram/blob/main/docs/upgrade.md). Do not re-import this recipe onto an existing installation.

### Backups

- Preserve `KARAKORAM_MASTER_KEY` outside Zerops. Replacing it makes the SQLite DB undecryptable.
- Consistent SQLite snapshot (stopped writer) of `/mnt/karakoramdata` — platform volume backups are live archives, not crash-consistent MongoDB/SQLite backups.
- Database data: configure PBM in the Karakoram UI (S3). Exercise restore before loading important data.

### Data Migrations

- None at import. First sign-in as `admin` with the generated password; Karakoram requires a password change before privileged API use.

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Clusters cannot be created | Empty `KARAKORAM_ZEROPS_TOKEN` | Paste Full access project token; restart/redeploy |
| `userDataZeropsPrefixForbidden` | Secret named `ZEROPS_*` | Use `KARAKORAM_ZEROPS_*` keys |
| Control plane not ready | Build/token/volume | Check `/healthz`, logs, volume mount, master-key length ≥ 32 |
| Secret change has no effect | Env is process-start | Restart or redeploy |
| Two containers | Horizontal scale | Keep `maxContainers: 1` |

## Security Considerations

- Full access project token can read other service secrets in the project. Treat Karakoram operators as project admins. Keep `envIsolation: service`.
- Do not commit or log `KARAKORAM_MASTER_KEY`, admin password, or the Zerops token. Do not put them in project-level vault.
- Public HTTPS is the UI/API on 8080 only. Do not publish 9443. MongoDB TCP is private unless the operator opts in with an allowlist.
- Read [limitations](https://github.com/KarakoramDev/Karakoram/blob/main/docs/limitations.md) before production data.

## References

- https://github.com/KarakoramDev/Karakoram — source, `zerops.yaml`, `deploy/zerops/`
- https://github.com/KarakoramDev/Karakoram/blob/main/docs/install.md — secrets, token, Git vs local import
- https://github.com/KarakoramDev/Karakoram/blob/main/docs/limitations.md — CP HA, Local Storage, anti-affinity
- https://docs.zerops.io/references/import-yaml/type-list — `ubuntu@24.04`, `local-storage:single@1`
- https://docs.zerops.io/features/rbac#integration-tokens — Full access project token

## Notes for Terminal Agent

- Copy `_template_oss/` (Development + Production), not the 6-env language template.
- `zeropsSetup: karakoram` — do not invent `dev`/`prod`.
- Do not add `APP_URL` to project vault; upstream maps `KARAKORAM_PUBLIC_URL` from `${zeropsSubdomain}`.
- Service `vault:` for the three secrets; `envIsolation: service`.
- `buildFromGit: https://github.com/KarakoramDev/Karakoram`.
- Cover SVG: no Karakoram asset yet — use `cover-go.svg` until `recipe-shared-assets` adds one.
- Do not modify the upstream app repo.
- Ready-for-testing requires a real import plus a human-supplied project token.
