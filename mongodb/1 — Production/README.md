# MongoDB — Production Environment
This is a Production environment for the [MongoDB (info + deploy)](https://app.zerops.io/recipes/mongodb?environment=production) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**Production** is the same control-plane topology as Development with a Local Storage volume that can grow to 10 GB. It is **not** a highly available control plane: SQLite and Local Storage stay single-writer and single-host. Replica-set HA is something you create later in the Karakoram UI, and even then Zerops does not guarantee physical-host anti-affinity. Read the [limitations](https://github.com/KarakoramDev/Karakoram/blob/main/docs/limitations.md) before loading important data.
<!-- #ZEROPS_EXTRACT_END:intro# -->

# Takeover and Maintenance Guide

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->

## After import

1. In **karakoram → Environment variables → Secret variables**, replace `KARAKORAM_ZEROPS_TOKEN` with a **project-scoped Full access** integration token (Settings → Access Tokens Management). Do not use the `ZEROPS_` prefix.
2. If logs still show `KARAKORAM_ZEROPS_PROJECT_ID … required`, set secret `KARAKORAM_ZEROPS_PROJECT_ID` to this project’s ID, or redeploy after a recipe revision with `zeropsYaml` (omits the empty `${projectId}` pipeline key).
3. Wait until `karakoram` is **ACTIVE**. Confirm `https://YOUR-SUBDOMAIN/healthz`.
4. Open the HTTPS subdomain. Sign in as `admin` with `KARAKORAM_ADMIN_PASSWORD`. Karakoram requires a password change before privileged API use; sign in again afterward.
5. Preserve `KARAKORAM_MASTER_KEY` outside Zerops. Losing it makes the SQLite state undecryptable.
6. For production traffic, attach a custom domain. `KARAKORAM_PUBLIC_URL` comes from the pipeline (`${zeropsSubdomain}`); override it in upstream `zerops.yaml` and redeploy — a service secret with the same key does not win.

Keep `maxContainers: 1`. Do not horizontally scale the control plane.

## Upgrading Karakoram

Re-trigger the `karakoram` pipeline (**Pipelines & CI/CD → Trigger a new pipeline → Prefill from active deploy**). The Git import tracks [KarakoramDev/Karakoram](https://github.com/KarakoramDev/Karakoram) `main`. Upgrades briefly stop the single writer. Do not re-import this recipe onto an existing installation. See the upstream [upgrade guide](https://github.com/KarakoramDev/Karakoram/blob/main/docs/upgrade.md).

## Backing up / restoring

Configure PBM backups and a restore drill **before** production data. Control-plane recovery needs a consistent SQLite snapshot plus the original master key; platform volume backups alone are not enough. See [backups and restore](https://github.com/KarakoramDev/Karakoram/blob/main/docs/user-guide/backups-and-restore.md) and [limitations](https://github.com/KarakoramDev/Karakoram/blob/main/docs/limitations.md).

## Local admin recovery

Set a temporary `KARAKORAM_RECOVERY_PASSWORD` secret on the service, restart, sign in and change the password, then delete the secret and restart again. See [upstream operations](https://github.com/KarakoramDev/Karakoram/blob/main/docs/operations.md).

<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
