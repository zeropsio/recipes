# Karakoram Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
One-click deploy of [Karakoram](https://karakoram.dev) on [Zerops](https://zerops.io) — a self-hosted control plane that provisions and operates [Percona Server for MongoDB](https://www.percona.com/mongodb/software/percona-server-for-mongodb) replica sets and sharded clusters inside this project. Source stays at [KarakoramDev/Karakoram](https://github.com/KarakoramDev/Karakoram); the recipe does not fork the app.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/karakoram?environment=production)

![go](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-go.svg)

Offered in two basic environments:

- **Development** [[info]](/0%20—%20Development) — [[deploy with one click]](https://app.zerops.io/recipes/karakoram?environment=development)
- **Production** [[info]](/1%20—%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/karakoram?environment=production)

## Takeover and maintenance

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->

### Project token (required once)

After import, set `KARAKORAM_ZEROPS_TOKEN` on the **karakoram** service to a project-scoped **Full access** integration token, then restart or redeploy. Details are in each environment README.

### Upgrading Karakoram

Re-trigger the `karakoram` Git pipeline from **Pipelines & CI/CD**. Do not re-import the recipe onto an existing installation. See the upstream [upgrade guide](https://github.com/KarakoramDev/Karakoram/blob/main/docs/upgrade.md).

### Backing up control-plane state and MongoDB data

Back up `KARAKORAM_MASTER_KEY` separately from Zerops. Snapshot SQLite on Local Storage with a consistent stopped-writer copy of `/mnt/karakoramdata`. Configure PBM backups in the Karakoram UI for database data. See [backups and restore](https://github.com/KarakoramDev/Karakoram/blob/main/docs/user-guide/backups-and-restore.md).

### Add to an existing project

Use [deploy/zerops/import.yaml](https://github.com/KarakoramDev/Karakoram/blob/main/deploy/zerops/import.yaml) (service import) instead of this one-click **new project** recipe.

<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**Token after import** — Karakoram needs a project-scoped **Full access** integration token in `KARAKORAM_ZEROPS_TOKEN` on the `karakoram` service. The recipe leaves it empty because the project does not exist until import finishes. Create the token under **Settings → Access Tokens Management**, paste it, then restart. Never use the `ZEROPS_` prefix.

**What this import creates** — the control plane (`karakoram`) and its SQLite volume (`karakoramdata`). MongoDB members, mongos, and backup storage are created later in the Karakoram UI, in this same project.

**Not HA** — SQLite on Local Storage is single-writer and single-host. Keep `maxContainers: 1`. Production is not a highly available control plane. Read the [limitations](https://github.com/KarakoramDev/Karakoram/blob/main/docs/limitations.md) before production data.

**Existing project** — to add Karakoram to a project you already have, use the upstream service import in [`deploy/zerops/`](https://github.com/KarakoramDev/Karakoram/tree/main/deploy/zerops) instead of this one-click project recipe.

**Setups** — only `karakoram` (upstream `zerops.yaml`). There is no `dev` / `prod` split.
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

- `buildFromGit` is https://github.com/KarakoramDev/Karakoram. The pipeline setup is `karakoram`: Node 22 builds the UI, Go 1.24 embeds it in a static binary, runtime is Ubuntu 24.04.
- HTTP UI/API is port 8080 (`/healthz`). Port 9443 is private agent TLS — do not publish it.
- `KARAKORAM_PUBLIC_URL` and `KARAKORAM_ZEROPS_PROJECT_ID` come from the app pipeline (`${zeropsSubdomain}`, `${projectId}`). Do not duplicate them in import vault.
- First sign-in: user `admin`, password from `KARAKORAM_ADMIN_PASSWORD`, then a required password change.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

For more examples see [Go](https://app.zerops.io/recipes?lf=golang) and [database](https://app.zerops.io/recipes?lf=database) recipes on Zerops.

Need help setting your project up? Join [Zerops Discord community](https://discord.gg/zeropsio).
