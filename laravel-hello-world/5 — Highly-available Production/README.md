# Laravel Hello World — Highly-available Production Environment

Full HA setup: minimum 2 app containers behind Zerops' L7 balancer with horizontal autoscaling up to 6 containers, and an HA PostgreSQL cluster. Zero-downtime rolling deploys. Suitable for production workloads that require fault tolerance.

## Deploy

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/green/deploy-button.svg)](https://app.zerops.io/recipe/laravel-hello-world-prod-ha)

## What's included

| Service | Type | Purpose |
|---------|------|---------|
| `app` | `php-nginx@8.4` | Production app (2–6 containers, rolling deploy) |
| `db` | `postgresql@16` | HA PostgreSQL (2-node, auto-failover) |

## How it works

- **Rolling deploys**: Zerops replaces one container at a time. The `readinessCheck` on `/api/health` gates traffic until the new container passes. The previous version continues serving traffic during the rollout.
- **One migration per deploy**: `zsc execOnce ${appVersionId}` ensures `php artisan migrate` runs on exactly one container. The others wait for it to complete before serving traffic.
- **Maintenance mode**: `APP_MAINTENANCE_DRIVER=cache` stores the maintenance flag in the shared database cache table, so all containers see the same maintenance state instantly.

## Configuration

Before going live, replace the auto-generated `APP_KEY` with your own:

```sh
zcli service env set app APP_KEY="base64:$(openssl rand -base64 32)"
```

## Endpoints

After deploy, enable subdomain access in the Zerops dashboard or connect your domain via DNS:

- `https://app-<id>.prg1.zerops.app/` — Dashboard
- `https://app-<id>.prg1.zerops.app/api/health` — Health JSON
