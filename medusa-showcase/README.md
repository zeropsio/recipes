# Medusa Showcase Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
Medusa v2.19 backend and admin ([zerops-recipe-apps/medusa-showcase](https://github.com/zerops-recipe-apps/medusa-showcase)) with optional Next.js storefront ([medusa-showcase-nextstore](https://github.com/zerops-recipe-apps/medusa-showcase-nextstore)) on [Zerops](https://zerops.io). PostgreSQL, Valkey, Meilisearch, MinIO, and Mailpit (dev envs). Omit nextstore for backend-only.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/medusa-showcase?environment=small-production)

![cover](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-nextjs.svg)

Offered in examples for the whole development lifecycle — from environments for AI agents like [Claude Code](https://www.anthropic.com/claude-code) or [opencode](https://opencode.ai) through environments for remote (CDE) or local development of each developer to stage and productions of all sizes.

- **AI agent** [[info]](/0%20—%20AI%20Agent) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-showcase?environment=ai-agent)
- **Remote (CDE)** [[info]](/1%20—%20Remote%20(CDE)) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-showcase?environment=remote-cde)
- **Local** [[info]](/2%20—%20Local) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-showcase?environment=local)
- **Stage** [[info]](/3%20—%20Stage) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-showcase?environment=stage)
- **Small Production** [[info]](/4%20—%20Small%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-showcase?environment=small-production)
- **Highly-available Production** [[info]](/5%20—%20Highly-available%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-showcase?environment=highly-available-production)

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**Backend-only** — omit nextstore services when you only need Medusa admin/API.

**OAuth / analytics** — optional `GOOGLE_*`, `GITHUB_*`, `POSTHOG_*` in project vault on showcase imports.

**Analog storefront** — separate recipe; keep `ANALOG_STORE_URL` in backend CORS.

**Meilisearch** — in-repo module (not the Rok Mohar plugin).
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

Split `medusa-showcase` + `medusa-showcase-nextstore`; setups `dev` / `prod` only. Imports live under `recipes/medusa-showcase/` and in the app `.zerops-recipe/` copy.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

For more advanced examples see all [Medusa recipes](https://app.zerops.io/recipes?lf=medusa) on Zerops.

Need help setting your project up? Join [Zerops Discord community](https://discord.gg/zeropsio).
