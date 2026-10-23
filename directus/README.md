# Directus Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
Production-style [Directus](https://directus.io) 12 on [Zerops](https://zerops.io) ([zerops-recipe-apps/directus](https://github.com/zerops-recipe-apps/directus)) with PostgreSQL, Valkey, S3 object storage, schema snapshot, and idempotent demo seed. Pair with [directus-next](https://app.zerops.io/recipes/directus-next) for a Next.js blog or connect any client via `API_URL`.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/directus?environment=small-production)

![cover](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/directus.svg)

- **AI agent** [[info]](/0%20—%20AI%20Agent) — [[deploy with one click]](https://app.zerops.io/recipes/directus?environment=ai-agent)
- **Remote (CDE)** [[info]](/1%20—%20Remote%20(CDE)) — [[deploy with one click]](https://app.zerops.io/recipes/directus?environment=remote-cde)
- **Local** [[info]](/2%20—%20Local) — [[deploy with one click]](https://app.zerops.io/recipes/directus?environment=local)
- **Stage** [[info]](/3%20—%20Stage) — [[deploy with one click]](https://app.zerops.io/recipes/directus?environment=stage)
- **Small Production** [[info]](/4%20—%20Small%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/directus?environment=small-production)
- **Highly-available Production** [[info]](/5%20—%20Highly-available%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/directus?environment=highly-available-production)

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**Full stack with Next.js** — use the [directus-next](https://app.zerops.io/recipes/directus-next) recipe.

**Setups** — `development` and `production` in app `zerops.yaml`. Stage/small-prod hostnames use `zeropsSetup: production`.

**Runtime** — `alpine/nodejs@24`, port **8055**, readiness `GET /server/ping` (Directus 12; `/server/health` requires auth).

**Secrets** — project vault `SECRET`, `ADMIN_TOKEN`; service vault `ADMIN_PASSWORD`, `SEED_VERSION`.
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

- Bootstrap: `directus bootstrap` → `ensure-schema.mjs` → `directus start`; demo seed via extension hook.
- Valkey required (`SYNCHRONIZATION_STORE=redis`) even for single-container dev.
- Uploads on Zerops object storage (S3 path-style). Mailpit on agent/local imports only.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

More [CMS recipes](https://app.zerops.io/recipes?lf=cms) on Zerops.

Need help? Join [Zerops Discord](https://discord.gg/zeropsio).
