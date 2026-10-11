# Strapi Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
Strapi v5 headless CMS ([zerops-recipe-apps/strapi](https://github.com/zerops-recipe-apps/strapi)) on [Zerops](https://zerops.io) with PostgreSQL. **Site Info** and sample blog content seed on bootstrap; use the admin at `/admin`. Pair with [strapi-react-frontend](https://github.com/zerops-recipe-apps/strapi-react-frontend) or any client via `API_URL`.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/strapi?environment=small-production)

![cover](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/strapi.svg)

- **AI agent** [[info]](/0%20—%20AI%20Agent) — [[deploy with one click]](https://app.zerops.io/recipes/strapi?environment=ai-agent)
- **Remote (CDE)** [[info]](/1%20—%20Remote%20(CDE)) — [[deploy with one click]](https://app.zerops.io/recipes/strapi?environment=remote-cde)
- **Local** [[info]](/2%20—%20Local) — [[deploy with one click]](https://app.zerops.io/recipes/strapi?environment=local)
- **Stage** [[info]](/3%20—%20Stage) — [[deploy with one click]](https://app.zerops.io/recipes/strapi?environment=stage)
- **Small Production** [[info]](/4%20—%20Small%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/strapi?environment=small-production)
- **Highly-available Production** [[info]](/5%20—%20Highly-available%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/strapi?environment=highly-available-production)

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**Full stack with React** — use the [strapi-react](https://app.zerops.io/recipes/strapi-react) recipe (Strapi + Vite SPA).

**Setups** — `dev` and `prod` only. Stage hostnames use `zeropsSetup: prod`.

**Node** — Strapi services use `nodejs@24`.

**Content** — edit **Site Info** and blog posts in `/admin`; public REST at `/api/*`.
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

- Strapi `prod`: Yarn 4 from `.yarn/releases/`; deploy compiled app + `node_modules`.
- Strapi `dev`: `deployFiles: ./`, `yarn develop` over SSH.
- Project `vault` holds Strapi secrets and public `API_URL`.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

For a React storefront see [strapi-react](https://app.zerops.io/recipes/strapi-react). More [CMS recipes](https://app.zerops.io/recipes?lf=cms) on Zerops.

Need help? Join [Zerops Discord](https://discord.gg/zeropsio).
