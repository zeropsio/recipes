# Medusa B2B — AI Agent Environment

This is [an AI agent environment](https://app.zerops.io/recipes/medusa-b2b?environment=ai-agent) for the [Medusa B2B recipe (info + deploy)](https://app.zerops.io/recipes/medusa-b2b?environment=ai-agent) on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**AI agent** environment deploys `medusadev` / `nextstoredev` (`zeropsSetup: dev`, workspaces) and `medusastage` / `nextstorestage` (`zeropsSetup: prod`) from [medusa-b2b](https://github.com/zerops-recipe-apps/medusa-b2b) and [medusa-b2b-nextstore](https://github.com/zerops-recipe-apps/medusa-b2b-nextstore), plus hobby PostgreSQL, Valkey, Meilisearch, MinIO, and Mailpit. Omit nextstore services for backend-only. SSH into `medusadev` (`yarn dev`) or `nextstoredev` (`yarn dev` in the nextstore repo).
<!-- #ZEROPS_EXTRACT_END:intro# -->
