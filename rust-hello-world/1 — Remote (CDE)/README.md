# Rust Hello World — Remote (CDE)

<!-- start-fragment: intro -->
This is the remote development environment for [Rust Hello World (info + deploy)](https://app.zerops.io/recipes/rust-hello-world?environment=remote-cde) recipe on [Zerops](https://zerops.io).

Two Rust services share a PostgreSQL database: `appdev` provides a cloud-hosted workspace with source code and Cargo registry deployed (dev setup) for IDE mounting via SSHFS, while `appstage` runs the compiled production binary for build pipeline validation.
<!-- end-fragment: intro -->

## How to use

1. Deploy this environment using the link above
2. Mount `appdev` via SSH in your IDE (VS Code Remote SSH, JetBrains Gateway, etc.)
3. Source code and dependencies are ready at `/var/www/` — database migration has run
4. Start the app: `cargo run` (or `cargo watch -x run` for live reload)
5. Push production build to validate: `zcli push <appstage-id> --setup=prod`

## Services

| Hostname | Setup | Purpose |
|----------|-------|---------|
| `appdev` | dev | Remote workspace — mount `/var/www/` via SSHFS from your IDE |
| `appstage` | prod | Validates production build pipeline — compiled binary, readiness check |
| `db` | PostgreSQL 17 | Shared database — migration runs automatically on first deploy |

## Tip: increase RAM for heavy compilation

Parallel `cargo build` jobs benefit from more RAM. Uncomment `minRam: 4` in the import.yaml and redeploy `appdev` if builds feel slow.
