# MongoDB Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
Deploy [Percona Server for MongoDB](https://www.percona.com/mongodb/software/percona-server-for-mongodb) on [Zerops](https://zerops.io) with replica sets, sharding, backups, and PITR. This recipe imports the [Karakoram](https://karakoram.dev) control plane from [KarakoramDev/Karakoram](https://github.com/KarakoramDev/Karakoram); you create and operate MongoDB clusters in the Karakoram UI inside the same project.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/mongodb?environment=production)

![go](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-go.svg)

Offered in two basic environments:

- **Development** [[info]](/0%20—%20Development) — [[deploy with one click]](https://app.zerops.io/recipes/mongodb?environment=development)
- **Production** [[info]](/1%20—%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/mongodb?environment=production)

## Takeover and maintenance

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->

### Project token (required once)

After import, replace `KARAKORAM_ZEROPS_TOKEN` on **karakoram** with a project-scoped **Full access** token before creating clusters. Do not shorten `KARAKORAM_MASTER_KEY` (minimum 32 characters). Details are in each environment README.

### Upgrading the control plane

Re-trigger the **karakoram** Git pipeline from **Pipelines & CI/CD**. Do not re-import this recipe onto an existing installation. See the upstream [upgrade guide](https://github.com/KarakoramDev/Karakoram/blob/main/docs/upgrade.md).

### Backing up control-plane state and MongoDB data

Back up `KARAKORAM_MASTER_KEY` separately from Zerops. Snapshot SQLite on Local Storage with a consistent stopped-writer copy of `/mnt/karakoramdata`. Configure PBM backups in the Karakoram UI for database data. See [backups and restore](https://github.com/KarakoramDev/Karakoram/blob/main/docs/user-guide/backups-and-restore.md).

### Add to an existing project

Use [deploy/zerops/import.yaml](https://github.com/KarakoramDev/Karakoram/blob/main/deploy/zerops/import.yaml) (service import) instead of this one-click **new project** recipe.

<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**Recipe name vs service names** — the Zerops recipe slug is `mongodb`. Imported services are still named **karakoram** and **karakoramdata** (required by upstream `zerops.yaml`).

**Token after import** — paste a project-scoped **Full access** integration token into `KARAKORAM_ZEROPS_TOKEN` on the **karakoram** service, then restart. Never use the `ZEROPS_` prefix.

**What this import creates** — the Karakoram control plane and its SQLite volume. MongoDB members, mongos, and backup storage are created later in the UI.

**Not HA** — the control plane is single-writer on Local Storage (`maxContainers: 1`). Read [limitations](https://github.com/KarakoramDev/Karakoram/blob/main/docs/limitations.md) before production data.

**Existing project** — use upstream [`deploy/zerops/`](https://github.com/KarakoramDev/Karakoram/tree/main/deploy/zerops) for service-only import.

**Pipeline setup** — `zeropsSetup: karakoram` only (no separate `dev` / `prod` app setups).
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

- `buildFromGit`: https://github.com/KarakoramDev/Karakoram. Setup `karakoram`: Node 22 UI build, Go 1.24 binary, Ubuntu 24.04 runtime.
- HTTP UI/API on port 8080 (`/healthz`). Do not publish port 9443 (agent TLS).
- `KARAKORAM_PUBLIC_URL` is set in recipe `zeropsYaml`. Project ID comes from Zerops-injected `projectId` (recipe omits upstream `KARAKORAM_ZEROPS_PROJECT_ID: ${projectId}` because an empty resolved value blocks Karakoram’s fallback).
- First sign-in: `admin` + `KARAKORAM_ADMIN_PASSWORD`, then mandatory password change.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

For more examples see [database](https://app.zerops.io/recipes?lf=database) recipes on Zerops.

Need help setting your project up? Join [Zerops Discord community](https://discord.gg/zeropsio).
