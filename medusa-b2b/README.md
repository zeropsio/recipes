# Medusa B2B Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
Medusa v2.21 B2B backend and admin ([zerops-recipe-apps/medusa-b2b](https://github.com/zerops-recipe-apps/medusa-b2b)) with optional Next.js storefront ([medusa-b2b-nextstore](https://github.com/zerops-recipe-apps/medusa-b2b-nextstore)) on [Zerops](https://zerops.io). PostgreSQL, Valkey, Meilisearch, MinIO, and Mailpit (dev envs). Omit nextstore services for a backend-only project.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/medusa-b2b?environment=small-production)

![cover](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-nextjs.svg)

- **AI agent** [[info]](/0%20—%20AI%20Agent) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-b2b?environment=ai-agent)
- **Remote (CDE)** [[info]](/1%20—%20Remote%20(CDE)) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-b2b?environment=remote-cde)
- **Local** [[info]](/2%20—%20Local) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-b2b?environment=local)
- **Stage** [[info]](/3%20—%20Stage) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-b2b?environment=stage)
- **Small Production** [[info]](/4%20—%20Small%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-b2b?environment=small-production)
- **Highly-available Production** [[info]](/5%20—%20Highly-available%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-b2b?environment=highly-available-production)

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**Backend-only** — import the recipe and skip `nextstore` / `nextstoredev` / `nextstorestage` services.

**Setups** — only `dev` and `prod`. `medusastage` is a hostname on the `prod` setup, not a third setup.

**Search / mail** — Meilisearch `search` service; Mailpit on Agent, Remote, and Local (`SMTP_HOST=mailpit`).

**Secrets** — project `vault:` in import YAML; do not duplicate `KEY: ${KEY}` in `zerops.yml`.

**Monorepo** — `nextstore/` in the backend repo is for local dev; Zerops uses `medusa-b2b-nextstore` so git-connected `dev` deploys `./` safely.
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

- Backend `prod`: deploy `backend/.medusa/server`. Backend `dev`: `deployFiles: ./`.
- Storefront: separate repo; `dev` deploys `./`, `prod` ships the Next build output.
- No `run.start` in `zerops.yml`.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

For more examples see all [Medusa recipes](https://app.zerops.io/recipes?lf=medusa) on Zerops.

Need help setting your project up? Join [Zerops Discord community](https://discord.gg/zeropsio).
