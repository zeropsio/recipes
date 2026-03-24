# Laravel Hello World — Stage Environment

Staging environment that mirrors the production setup. Single-container app with a non-HA PostgreSQL database. Use this to validate the full build pipeline before promoting to production.

## Deploy

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/green/deploy-button.svg)](https://app.zerops.io/recipe/laravel-hello-world-stage)

## What's included

| Service | Type | Purpose |
|---------|------|---------|
| `app` | `php-nginx@8.4` | Staging app (prod setup, single container) |
| `db` | `postgresql@16` | Non-HA PostgreSQL for staging |

## Workflow

1. Import `import.yaml` into your Zerops project.
2. Zerops builds the app using the `prod` setup from the GitHub repo:
   - Runs `composer install --optimize-autoloader --no-dev`
   - Caches config, routes, views, events on first container start
   - Runs `php artisan migrate --isolated --force` once via `zsc execOnce`
3. Enable subdomain access to get a public HTTPS URL.
4. Test the staging endpoint before merging to main.

## Endpoints

After deploy, open the subdomain URL from the Zerops dashboard:

- `https://app-<id>.prg1.zerops.app/` — Dashboard
- `https://app-<id>.prg1.zerops.app/api/health` — Health JSON
