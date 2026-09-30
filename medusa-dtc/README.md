# Medusa DTC Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
Medusa v2.21 DTC backend and admin ([zerops-recipe-apps/medusa-dtc](https://github.com/zerops-recipe-apps/medusa-dtc)) with optional Next.js storefront ([medusa-dtc-frontend](https://github.com/zerops-recipe-apps/medusa-dtc-frontend)) on [Zerops](https://zerops.io). PostgreSQL, Valkey, Meilisearch, MinIO, and Mailpit (dev envs). Omit nextstore services for backend-only.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/medusa-dtc?environment=small-production)

![cover](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-nextjs.svg)

Offered in examples for the whole development lifecycle — from environments for AI agents like [Claude Code](https://www.anthropic.com/claude-code) or [opencode](https://opencode.ai) through environments for remote (CDE) or local development of each developer to stage and productions of all sizes.

- **AI agent** [[info]](/0%20—%20AI%20Agent) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-dtc?environment=ai-agent)
- **Remote (CDE)** [[info]](/1%20—%20Remote%20(CDE)) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-dtc?environment=remote-cde)
- **Local** [[info]](/2%20—%20Local) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-dtc?environment=local)
- **Stage** [[info]](/3%20—%20Stage) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-dtc?environment=stage)
- **Small Production** [[info]](/4%20—%20Small%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-dtc?environment=small-production)
- **Highly-available Production** [[info]](/5%20—%20Highly-available%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/medusa-dtc?environment=highly-available-production)

<!-- #ZEROPS_EXTRACT_START:faq# -->
## FAQ

**Backend-only** — omit nextstore services; backend `buildFromGit` stays `medusa-dtc`.

**Setups** — `dev` and `prod` only. Stage hostnames use `zeropsSetup: prod`.

**Search / mail** — Meilisearch + Mailpit on dev environments; configure SMTP vault on stage/prod.

**Repos** — [medusa-dtc](https://github.com/zerops-recipe-apps/medusa-dtc) is Medusa API + admin at repository root. [medusa-dtc-frontend](https://github.com/zerops-recipe-apps/medusa-dtc-frontend) is the optional Next.js DTC storefront. No Turbo/Nx.
<!-- #ZEROPS_EXTRACT_END:faq# -->

<!-- #ZEROPS_EXTRACT_START:integration-guide# -->
## Integration

Same deploy model as [medusa-b2b](https://github.com/zeropsio/recipes/tree/main/medusa-b2b): backend at repo root (`prod` → `.medusa/server`, `dev` → `./`); storefront from `medusa-dtc-frontend`.
<!-- #ZEROPS_EXTRACT_END:integration-guide# -->

---

For more advanced examples see all [Medusa recipes](https://app.zerops.io/recipes?lf=medusa) on Zerops.

Need help setting your project up? Join [Zerops Discord community](https://discord.gg/zeropsio).
