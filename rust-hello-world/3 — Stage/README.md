# Rust Hello World — Stage

<!-- start-fragment: intro -->
This is the staging environment for [Rust Hello World (info + deploy)](https://app.zerops.io/recipes/rust-hello-world?environment=stage) recipe on [Zerops](https://zerops.io).

A single Rust service runs the production build pipeline against a dedicated PostgreSQL database — identical infrastructure to production, sized for pre-release validation rather than traffic.
<!-- end-fragment: intro -->

## How to use

1. Deploy this environment using the link above
2. Push your changes to test: `zcli push <app-id> --setup=prod`
3. The readiness check at `/` verifies the deployment before traffic is routed
4. Promote to production once staging passes

## Services

| Hostname | Setup | Purpose |
|----------|-------|---------|
| `app` | prod | Staging app — production build pipeline, single container |
| `db` | PostgreSQL 17 | Staging database — isolated from production data |
