# Rust Hello World — Highly-available Production

<!-- start-fragment: intro -->
This is the highly-available production environment for [Rust Hello World (info + deploy)](https://app.zerops.io/recipes/rust-hello-world?environment=highly-available-production) recipe on [Zerops](https://zerops.io).

A Rust service runs across two dedicated-CPU containers backed by an HA PostgreSQL cluster (primary + replica with automatic failover) — the Serious core package eliminates noisy-neighbor interference at the project balancer level for consistent latency under enterprise load.
<!-- end-fragment: intro -->

## How to use

1. Deploy this environment using the link above
2. Point your domain to the app's subdomain or IP
3. Push updates: `zcli push <app-id> --setup=prod` — zero-downtime across both containers

## Services

| Hostname | Setup | Purpose |
|----------|-------|---------|
| `app` | prod | HA app — 2 containers, dedicated CPUs, vertical autoscaling |
| `db` | PostgreSQL 17 HA | Primary + replica, automatic failover, no single point of failure |

## Infrastructure highlights

- **Serious core**: dedicated physical CPUs for the project balancer — no CPU sharing with other projects
- **`cpuMode: DEDICATED`**: physical CPU cores for both app and database — eliminates scheduling jitter
- **HA database**: automatic failover; a primary failure promotes the replica with no manual intervention
- **`minFreeRamGB`**: reserved headroom prevents OOM restarts under traffic spikes and WAL write bursts
