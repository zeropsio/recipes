# Medusa — AI Agent Environment

This is [an AI agent environment](https://app.zerops.io/recipes/medusa-showcase?environment=ai-agent) for the [Medusa recipe (info + deploy)](https://app.zerops.io/recipes/medusa-showcase?environment=ai-agent) on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**AI agent** environment deploys a `*dev` + `*stage` pair from [zerops-recipe-apps/medusa-showcase](https://github.com/zerops-recipe-apps/medusa-showcase) plus hobby PostgreSQL, Valkey, Meilisearch, and public-read object storage. `medusastage` / `nextstorestage` run the production setups (`/health`, `/app`). `medusadev` / `nextstoredev` are idle workspaces — SSH in and run `yarn dev`.
<!-- #ZEROPS_EXTRACT_END:intro# -->
