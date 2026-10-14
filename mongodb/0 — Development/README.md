# MongoDB — Development Environment
This is a development environment for the [MongoDB (info + deploy)](https://app.zerops.io/recipes/mongodb?environment=development) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**Development** imports a single Karakoram control plane (Ubuntu 24.04, 0.5 GB RAM) and a 5 GB Local Storage volume for SQLite. Use it to try the UI, create a small replica set, and learn the token + first-login flow. The control plane is not highly available — keep one container.
<!-- #ZEROPS_EXTRACT_END:intro# -->

# Takeover and Maintenance Guide

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->

## After import

1. Wait until `karakoram` is **ACTIVE**. Confirm `https://YOUR-SUBDOMAIN/healthz`.
2. In **karakoram → Environment variables → Secret variables**, paste a **project-scoped Full access** integration token into `KARAKORAM_ZEROPS_TOKEN`. Create the token under **Settings → Access Tokens Management** for this project only. Do not name it `ZEROPS_TOKEN`.
3. Restart or redeploy so the process picks up the secret.
4. Open the HTTPS subdomain. Sign in as `admin` with `KARAKORAM_ADMIN_PASSWORD`. Karakoram requires a password change before privileged API use; sign in again afterward.
5. Preserve `KARAKORAM_MASTER_KEY` outside Zerops. Losing it makes the SQLite state undecryptable.

Create clusters in the UI (advertised PSMDB versions, TLS required, public exposure off until you need it). Members appear as additional services in this same project.

## Upgrading Karakoram

Re-trigger the `karakoram` pipeline (**Pipelines & CI/CD → Trigger a new pipeline → Prefill from active deploy**). The Git import tracks [KarakoramDev/Karakoram](https://github.com/KarakoramDev/Karakoram) `main`. Upgrades use `temporaryShutdown` — the control plane is briefly unavailable. Do not re-import this recipe onto an existing installation. See the upstream [upgrade guide](https://github.com/KarakoramDev/Karakoram/blob/main/docs/upgrade.md).

## Backing up / restoring

- Control-plane state: consistent SQLite snapshot of `/mnt/karakoramdata` (stopped writer) plus the original `KARAKORAM_MASTER_KEY`. Platform volume backups are live archives, not crash-consistent SQLite.
- Database data: configure S3-compatible PBM storage in the Karakoram UI (Zerops object storage at `storage-prg1.zerops.io` is trusted by default). Exercise restore before loading important data.

## Local admin recovery

Set a temporary `KARAKORAM_RECOVERY_PASSWORD` secret on the service, restart, sign in and change the password, then delete the secret and restart again. See [upstream operations](https://github.com/KarakoramDev/Karakoram/blob/main/docs/operations.md).

<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
