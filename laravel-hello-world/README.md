# Laravel Hello World

A minimal Laravel 11 application deployed on Zerops. Demonstrates PHP-FPM + Nginx via `php-nginx@8.4`, PostgreSQL integration, multi-container-safe migrations with `zsc execOnce`, and the `extends: base` pattern for sharing config between prod and dev setups.

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/green/deploy-button.svg)](https://app.zerops.io/recipe/laravel-hello-world)

## App repository

[github.com/zerops-recipe-apps/laravel-hello-world-app](https://github.com/zerops-recipe-apps/laravel-hello-world-app)

## Environments

| # | Environment | App services | DB mode | Use case |
|---|-------------|-------------|---------|---------|
| 0 | [AI Agent](./0%20—%20AI%20Agent/) | `appdev` + `appstage` | NON_HA | AI agent builds the recipe from scratch |
| 1 | [Remote (CDE)](./1%20—%20Remote%20(CDE)/) | `appdev` + `appstage` | NON_HA | Cloud development via SSH/SSHFS |
| 2 | [Local](./2%20—%20Local/) | _(none — run locally)_ | NON_HA | Local PHP server + Zerops PostgreSQL via VPN |
| 3 | [Stage](./3%20—%20Stage/) | `app` (1 container) | NON_HA | Pre-production validation |
| 4 | [Small Production](./4%20—%20Small%20Production/) | `app` (1 container) | HA | Low-to-medium traffic production |
| 5 | [Highly-available Production](./5%20—%20Highly-available%20Production/) | `app` (2–6 containers) | HA | Fault-tolerant production |

## What the app demonstrates

- **`php-nginx@8.4`** — PHP-FPM + Nginx service type; Zerops wires FPM and Nginx automatically
- **`extends: base`** — shared env vars (DB credentials, `APP_URL`, `LOG_CHANNEL`) inherited by both `prod` and `dev` setups
- **Build path vs runtime path** — `config:cache` runs in `initCommands` (not `buildCommands`) because build containers use `/build/source/` while runtime uses `/var/www/`
- **`zsc execOnce`** — ensures `php artisan migrate` runs exactly once across multi-container deploys
- **`APP_MAINTENANCE_DRIVER=cache`** — maintenance mode flag stored in the shared database cache, visible to all containers simultaneously
- **`COMPOSER_HOME=/tmp/composer`** — required in dev `initCommands` because runtime containers don't set `HOME`

## Tech stack

| Layer | Technology |
|-------|-----------|
| Language | PHP 8.4 |
| Framework | Laravel 11 |
| Web server | Nginx + PHP-FPM (`php-nginx@8.4`) |
| Database | PostgreSQL 16 |
| Template engine | Blade |
