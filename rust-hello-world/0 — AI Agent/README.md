# Rust Hello World — AI Agent

<!-- start-fragment: intro -->
This is the AI agent development environment for [Rust Hello World (info + deploy)](https://app.zerops.io/recipes/rust-hello-world?environment=ai-agent) recipe on [Zerops](https://zerops.io).

Two Rust services share a PostgreSQL database: `appdev` deploys full source code with a downloaded Cargo registry (dev setup) for interactive SSH development, while `appstage` runs the compiled production binary to validate the build pipeline via `zcli push`.
<!-- end-fragment: intro -->

## How to use

1. Deploy this environment using the link above
2. SSH into `appdev` — source code and dependencies are already deployed, database migration has run
3. Start the app: `cargo run` (or `cargo watch -x run` for live reload)
4. Test changes, then push the production build: `zcli push <appstage-id> --setup=prod`

## Services

| Hostname | Setup | Purpose |
|----------|-------|---------|
| `appdev` | dev | SSH workspace — source + registry deployed, `zsc noop` keeps container idle |
| `appstage` | prod | Validates production build pipeline — compiled binary, readiness check |
| `db` | PostgreSQL 17 | Shared database — migration runs automatically on first deploy |
