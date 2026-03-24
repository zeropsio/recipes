# Laravel Hello World — AI Agent Environment

Deploy a complete AI agent workspace: a dev service the agent can SSH into, a staging service for verification, and a shared PostgreSQL database.

## Deploy

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/green/deploy-button.svg)](https://app.zerops.io/recipe/laravel-hello-world-agent)

## What's included

| Service | Type | Purpose |
|---------|------|---------|
| `appdev` | `php-nginx@8.4` | Dev workspace — agent edits and runs code here |
| `appstage` | `php-nginx@8.4` | Staging — agent validates prod build here |
| `db` | `postgresql@16` | Shared PostgreSQL database |

## Workflow

1. Import `import.yaml` into your Zerops project.
2. Zerops builds `appdev` (dev setup) and `appstage` (prod setup) from the GitHub repo.
3. The AI agent SSHes into `appdev` via `zcli service remote-login appdev`.
4. Agent edits files at `/var/www/`, runs `php artisan` commands, tests changes via the subdomain URL.
5. Agent pushes to `appstage` for staging validation.

## Endpoints

After deploy, open the subdomain URLs from the Zerops dashboard:

- `https://appdev-<id>.prg1.zerops.app/` — Dashboard (dev)
- `https://appdev-<id>.prg1.zerops.app/api/health` — Health JSON (dev)
- `https://appstage-<id>.prg1.zerops.app/` — Dashboard (stage)
- `https://appstage-<id>.prg1.zerops.app/api/health` — Health JSON (stage)
