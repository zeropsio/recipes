# Medusa DTC — Remote Environment

This is a remote (CDE) environment for [Medusa DTC (info + deploy)](https://app.zerops.io/recipes/medusa-dtc?environment=remote-cde) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**Remote (CDE)** environment mirrors the agent topology — `medusadev` / `nextstoredev` workspaces plus `medusastage` / `nextstorestage` deploy targets, on a shared hobby data plane — so a developer can SSH in and run `yarn dev` without installing Postgres, Valkey, or MinIO locally.
<!-- #ZEROPS_EXTRACT_END:intro# -->
