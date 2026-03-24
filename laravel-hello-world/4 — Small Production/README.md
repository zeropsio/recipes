# Laravel Hello World — Small Production Environment

Single-container production app with HA PostgreSQL. Vertical autoscaling handles traffic spikes. Suitable for low-to-medium traffic apps that need database durability without the cost of a fully replicated app layer.

## Deploy

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/green/deploy-button.svg)](https://app.zerops.io/recipe/laravel-hello-world-prod-small)

## What's included

| Service | Type | Purpose |
|---------|------|---------|
| `app` | `php-nginx@8.4` | Production app (1 container, autoscales vertically) |
| `db` | `postgresql@16` | HA PostgreSQL (2-node, auto-failover) |

## Configuration

Before going live, replace the auto-generated `APP_KEY` with your own:

```sh
zcli service env set app APP_KEY="base64:$(openssl rand -base64 32)"
```

## Vertical autoscaling

The app container scales from 0.5 vCPU / 0.5 GB to 4 vCPU / 4 GB automatically under load. No containers are added — scale `minContainers: 2` and enable the `prod` setup's rolling deploy for zero-downtime deploys.

## Endpoints

After deploy, enable subdomain access in the Zerops dashboard or connect your domain via DNS:

- `https://app-<id>.prg1.zerops.app/` — Dashboard
- `https://app-<id>.prg1.zerops.app/api/health` — Health JSON
