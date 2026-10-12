# Payload + Next.js Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
Payload CMS ([zerops-recipe-apps/payload](https://github.com/zerops-recipe-apps/payload)) with a Next.js storefront ([payload-next-frontend](https://github.com/zerops-recipe-apps/payload-next-frontend)) on [Zerops](https://zerops.io). PostgreSQL ships with the project. **Site Info** and sample blog posts seed in Payload; the storefront reads REST on the **Next server** (no browser CORS). Omit `frontend*` services for CMS-only — use the [payload](https://app.zerops.io/recipes/payload) recipe instead.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/payload-next?environment=small-production)

![cover](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-react.svg)

- **AI agent** [[info]](/0%20—%20AI%20Agent) — [[deploy with one click]](https://app.zerops.io/recipes/payload-next?environment=ai-agent)
- **Remote (CDE)** [[info]](/1%20—%20Remote%20(CDE)) — [[deploy with one click]](https://app.zerops.io/recipes/payload-next?environment=remote-cde)
- **Local** [[info]](/2%20—%20Local) — [[deploy with one click]](https://app.zerops.io/recipes/payload-next?environment=local)
- **Stage** [[info]](/3%20—%20Stage) — [[deploy with one click]](https://app.zerops.io/recipes/payload-next?environment=stage)
- **Small Production** [[info]](/4%20—%20Small%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/payload-next?environment=small-production)
- **Highly-available Production** [[info]](/5%20—%20Highly-available%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/payload-next?environment=highly-available-production)

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**CMS-only** — use the [payload](https://app.zerops.io/recipes/payload) recipe or deploy `payload` / `payloaddev` / `payloadstage` and skip `frontend*`.

**Setups** — `dev` and `prod` only. `payloadstage` uses `prod`.

**Node** — Payload and storefront use `nodejs@24` with Next **`standalone`** on `prod`.

**Content** — edit **Site Info** and blog posts in `/admin`; storefront uses `/api/globals/site-info` and `/api/blog-posts` server-side.

**URLs** — Storefront is `https://frontend-{host}-3000.prg1.zerops.app` (vault `APP_URL`); CMS is `https://payload-{host}-3000.prg1.zerops.app` (`API_URL`).
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

Split repos like Medusa: CMS from [payload](https://github.com/zerops-recipe-apps/payload); storefront from [payload-next-frontend](https://github.com/zerops-recipe-apps/payload-next-frontend) (`NEXT_PUBLIC_PAYLOAD_URL` ← vault `API_URL`). Project `vault` for URLs and `PAYLOAD_SECRET`.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

For more examples see [framework recipes](https://app.zerops.io/recipes?lf=framework) on Zerops.

Need help? Join [Zerops Discord](https://discord.gg/zeropsio).
