# Rust Hello World — Local

<!-- start-fragment: intro -->
This is the local development environment for [Rust Hello World (info + deploy)](https://app.zerops.io/recipes/rust-hello-world?environment=local) recipe on [Zerops](https://zerops.io).

A single production app service pairs with a cloud-hosted PostgreSQL database — you run Rust locally while connecting to Zerops infrastructure via VPN, keeping your database in the cloud without needing a local PostgreSQL installation.
<!-- end-fragment: intro -->

## How to use

1. Deploy this environment using the link above
2. Install and start the Zerops VPN: `zcli vpn up`
3. Set database credentials as local environment variables (copy from Zerops dashboard)
4. Run locally: `cargo run`
5. Push your changes to the cloud: `zcli push <app-id> --setup=prod`

## Services

| Hostname | Setup | Purpose |
|----------|-------|---------|
| `app` | prod | Cloud deployment — test your prod build after local development |
| `db` | PostgreSQL 17 | Cloud database — accessible from localhost via `zcli vpn up` |

## Getting database credentials

In the Zerops dashboard, navigate to the `db` service → **Environment variables** to find `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASS`, and `DB_NAME`.
