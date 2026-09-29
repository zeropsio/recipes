# Medusa — AI Agent Environment

This is [an AI agent environment](https://app.zerops.io/recipes/medusa-showcase?environment=ai-agent) for the [Medusa recipe (info + deploy)](https://app.zerops.io/recipes/medusa-showcase?environment=ai-agent) on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**AI agent** environment deploys `medusadev` / `nextstoredev` (`zeropsSetup: dev`, workspaces) and `medusastage` / `nextstorestage` (`zeropsSetup: prod`) from [medusa-showcase](https://github.com/zerops-recipe-apps/medusa-showcase) and [medusa-showcase-frontend](https://github.com/zerops-recipe-apps/medusa-showcase-frontend), plus hobby PostgreSQL, Valkey, Meilisearch, MinIO, and Mailpit. Omit nextstore services for backend-only. SSH into `medusadev` (`cd backend && yarn dev`) or `nextstoredev` (`yarn dev`).
<!-- #ZEROPS_EXTRACT_END:intro# -->
