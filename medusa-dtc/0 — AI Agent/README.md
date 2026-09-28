# Medusa DTC — AI Agent Environment

This is [an AI agent environment](https://app.zerops.io/recipes/medusa-dtc?environment=ai-agent) for the [Medusa DTC recipe (info + deploy)](https://app.zerops.io/recipes/medusa-dtc?environment=ai-agent) on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**AI agent** environment deploys a `*dev` + `*stage` pair from [zerops-recipe-apps/medusa-dtc](https://github.com/zerops-recipe-apps/medusa-dtc) plus hobby PostgreSQL, Valkey, and public-read object storage. `medusastage` / `nextstorestage` run the production setups (`/health`, `/app`). `medusadev` / `nextstoredev` are idle workspaces — SSH in and run `yarn dev`.
<!-- #ZEROPS_EXTRACT_END:intro# -->
