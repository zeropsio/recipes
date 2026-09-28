# Medusa B2B — AI Agent Environment

This is [an AI agent environment](https://app.zerops.io/recipes/medusa-b2b?environment=ai-agent) for the [Medusa B2B recipe (info + deploy)](https://app.zerops.io/recipes/medusa-b2b?environment=ai-agent) on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**AI agent** environment deploys a `*dev` + `*stage` pair from [zerops-recipe-apps/medusa-b2b](https://github.com/zerops-recipe-apps/medusa-b2b) plus hobby PostgreSQL, Valkey, and public-read object storage. `medusastage` / `nextstorestage` run the production setups (`/health`, `/app`). `medusadev` / `nextstoredev` are idle workspaces — SSH in and run `yarn dev`.
<!-- #ZEROPS_EXTRACT_END:intro# -->
