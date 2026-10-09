# Strapi + React Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
Strapi v5 headless CMS ([zerops-recipe-apps/strapi-react](https://github.com/zerops-recipe-apps/strapi-react)) with a Vite + React frontend ([strapi-react-frontend](https://github.com/zerops-recipe-apps/strapi-react-frontend)) on [Zerops](https://zerops.io). PostgreSQL ships with the project. Default **Site Info** content seeds in Strapi and displays in React. Omit `frontend*` services for CMS-only.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/strapi-react?environment=small-production)

![cover](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-react.svg)

- **AI agent** [[info]](/0%20—%20AI%20Agent) — [[deploy with one click]](https://app.zerops.io/recipes/strapi-react?environment=ai-agent)
- **Remote (CDE)** [[info]](/1%20—%20Remote%20(CDE)) — [[deploy with one click]](https://app.zerops.io/recipes/strapi-react?environment=remote-cde)
- **Local** [[info]](/2%20—%20Local) — [[deploy with one click]](https://app.zerops.io/recipes/strapi-react?environment=local)
- **Stage** [[info]](/3%20—%20Stage) — [[deploy with one click]](https://app.zerops.io/recipes/strapi-react?environment=stage)
- **Small Production** [[info]](/4%20—%20Small%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/strapi-react?environment=small-production)
- **Highly-available Production** [[info]](/5%20—%20Highly-available%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/strapi-react?environment=highly-available-production)

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**CMS-only** — deploy `strapi` / `strapidev` / `strapistage`; skip `frontend*`.

**Setups** — `dev` and `prod` only. `strapistage` uses `prod`.

**Node** — Strapi services use `nodejs@22` (Strapi 5 engine cap). Frontend build uses `nodejs@24` + `static` runtime.

**Content** — edit **Site Info** in `/admin`; React reads `/api/site-info`.
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

Split repos like Medusa: backend `deployFiles: ./` on `dev`; frontend Vite `dist/` on `prod`. Project `vault` for URLs and Strapi secrets.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

For more examples see [framework recipes](https://app.zerops.io/recipes?lf=framework) on Zerops.

Need help? Join [Zerops Discord](https://discord.gg/zeropsio).
