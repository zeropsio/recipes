# Payload Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
Payload CMS ([zerops-recipe-apps/payload](https://github.com/zerops-recipe-apps/payload)) on [Zerops](https://zerops.io) with PostgreSQL. **Site Info** and sample blog content seed on bootstrap; use the admin at `/admin`. Pair with [payload-next-frontend](https://github.com/zerops-recipe-apps/payload-next-frontend) or any client via `API_URL`.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/payload?environment=small-production)

![cover](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/payload.svg)

- **AI agent** [[info]](/0%20—%20AI%20Agent) — [[deploy with one click]](https://app.zerops.io/recipes/payload?environment=ai-agent)
- **Remote (CDE)** [[info]](/1%20—%20Remote%20(CDE)) — [[deploy with one click]](https://app.zerops.io/recipes/payload?environment=remote-cde)
- **Local** [[info]](/2%20—%20Local) — [[deploy with one click]](https://app.zerops.io/recipes/payload?environment=local)
- **Stage** [[info]](/3%20—%20Stage) — [[deploy with one click]](https://app.zerops.io/recipes/payload?environment=stage)
- **Small Production** [[info]](/4%20—%20Small%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/payload?environment=small-production)
- **Highly-available Production** [[info]](/5%20—%20Highly-available%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/payload?environment=highly-available-production)

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**Full stack with React** — use the [payload-next](https://app.zerops.io/recipes/payload-next) recipe (Payload + Next.js storefront).

**Setups** — `dev` and `prod` only. Stage hostnames use `zeropsSetup: prod`.

**Node** — Payload services use `nodejs@24`.

**Content** — edit **Site Info** and blog posts in `/admin`; public REST at `/api/*`.
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

- Payload `prod`: Next.js **`output: standalone`** — build runs `payload migrate`, `payload generate:importmap`, `next build`, and `prepare-standalone`; runtime starts `node .next/standalone/bin/run.mjs` (do not set `HOSTNAME` in zerops.yaml).
- Payload `dev`: `deployFiles: ./`, `npm run dev` over SSH (`zsc noop` start).
- Project **`vault`**: `PAYLOAD_SECRET`, `API_URL`, `APP_URL`, `DEV_*`; map in app `zerops.yaml` (never `HOSTNAME` — reserved by Zerops).
- Services use **`enableSubdomainAccess: true`** so public URLs work after deploy.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

For a React storefront see [payload-next](https://app.zerops.io/recipes/payload-next). More [CMS recipes](https://app.zerops.io/recipes?lf=cms) on Zerops.

Need help? Join [Zerops Discord](https://discord.gg/zeropsio).
