# Directus + Next.js Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
[Directus](https://directus.io) ([zerops-directus-cms](https://github.com/kristiyan-velkov/zerops-directus-cms)) with a [Next.js 16](https://nextjs.org) blog ([zerops-directus-nextjs-blog](https://github.com/kristiyan-velkov/zerops-directus-nextjs-blog)) on [Zerops](https://zerops.io). PostgreSQL, Valkey, and S3 ship with the CMS; the blog uses ISR and server-side `DIRECTUS_TOKEN` from vault `ADMIN_TOKEN`. Omit `frontend*` for CMS-only — use [directus](https://app.zerops.io/recipes/directus).
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/directus-next?environment=small-production)

![cover](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-react.svg)

- **AI agent** [[info]](/0%20—%20AI%20Agent) — [[deploy with one click]](https://app.zerops.io/recipes/directus-next?environment=ai-agent)
- **Remote (CDE)** [[info]](/1%20—%20Remote%20(CDE)) — [[deploy with one click]](https://app.zerops.io/recipes/directus-next?environment=remote-cde)
- **Local** [[info]](/2%20—%20Local) — [[deploy with one click]](https://app.zerops.io/recipes/directus-next?environment=local)
- **Stage** [[info]](/3%20—%20Stage) — [[deploy with one click]](https://app.zerops.io/recipes/directus-next?environment=stage)
- **Small Production** [[info]](/4%20—%20Small%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/directus-next?environment=small-production)
- **Highly-available Production** [[info]](/5%20—%20Highly-available%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/directus-next?environment=highly-available-production)

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**CMS-only** — use the [directus](https://app.zerops.io/recipes/directus) recipe.

**Setups** — CMS `development` / `production`; frontend `dev` / `nextjs` (`prod`).

**Wiring** — `DIRECTUS_URL` ← vault `API_URL` (or `DEV_API_URL` on `frontenddev`); `DIRECTUS_TOKEN` ← vault `ADMIN_TOKEN`.
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

Split repos like [payload-next](https://app.zerops.io/recipes/payload-next): CMS showcase + Next standalone bundle. Project vault holds URLs, `SECRET`, and `ADMIN_TOKEN`.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

More [CMS recipes](https://app.zerops.io/recipes?lf=cms) on Zerops.

Need help? Join [Zerops Discord](https://discord.gg/zeropsio).
