# Medusa DTC — AI Agent Environment

This is [an AI agent environment](https://app.zerops.io/recipes/medusa-dtc?environment=ai-agent) for the [Medusa DTC recipe (info + deploy)](https://app.zerops.io/recipes/medusa-dtc?environment=ai-agent) on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**AI agent** environment deploys `medusadev` / `nextstoredev` (`zeropsSetup: dev`, workspaces) and `medusastage` / `nextstorestage` (`zeropsSetup: prod`) from [medusa-dtc](https://github.com/zerops-recipe-apps/medusa-dtc) and [medusa-dtc-nextstore](https://github.com/zerops-recipe-apps/medusa-dtc-nextstore), plus hobby PostgreSQL, Valkey, Meilisearch, MinIO, and Mailpit. Omit nextstore services for backend-only. SSH into `medusadev` (`cd backend && yarn dev`) or `nextstoredev` (`yarn dev`).
<!-- #ZEROPS_EXTRACT_END:intro# -->
