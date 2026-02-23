# Rust Hello World — Small Production

<!-- start-fragment: intro -->
This is the small production environment for [Rust Hello World (info + deploy)](https://app.zerops.io/recipes/rust-hello-world?environment=small-production) recipe on [Zerops](https://zerops.io).

A Rust service runs across two containers behind a PostgreSQL database — `minContainers: 2` ensures zero-downtime deployments by default (new containers start before old ones stop) while keeping resource costs minimal.
<!-- end-fragment: intro -->

## How to use

1. Deploy this environment using the link above
2. Point your domain to the app's subdomain or IP
3. Push updates: `zcli push <app-id> --setup=prod` — zero-downtime by default

## Services

| Hostname | Setup | Purpose |
|----------|-------|---------|
| `app` | prod | Production app — 2 containers, vertical autoscaling, readiness check |
| `db` | PostgreSQL 17 | Production database — NON_HA, single primary |

## Scaling

Zerops monitors RAM every 10 seconds and scales vertically within the configured range. `minFreeRamGB: 0.05` reserves headroom above `minRam` so GC pauses and traffic spikes don't trigger OOM restarts. To handle more traffic, increase `minContainers` or raise `minRam`.
