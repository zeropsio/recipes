# Laravel Minimal

A minimal Laravel application running on Zerops with PHP-Nginx and PostgreSQL. Demonstrates database connectivity, migrations, and the platform integration points every Laravel app needs.

## Environments

| Folder | Description |
|--------|-------------|
| 0 — AI Agent | AI-driven development with dev/stage pair |
| 1 — Remote (CDE) | Cloud development environment with dev/stage pair |
| 2 — Local | Single prod service for local development via VPN |
| 3 — Stage | Staging with memory autoscaling |
| 4 — Small Production | 2 containers, shared CPU |
| 5 — Highly-available Production | 2 containers, dedicated CPU, HA database |

## Quick Start

Import any environment via the Zerops GUI or CLI:

```bash
zcli project project-import ./path-to/import.yaml
```

## Stack

- **Runtime**: php-nginx@8.4
- **Database**: postgresql@16
- **Build**: php@8.4 + nodejs@22 (Vite asset compilation)
