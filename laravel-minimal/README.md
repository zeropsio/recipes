# Laravel Minimal — Zerops Recipe

Minimal Laravel application running on Zerops with PHP-Nginx, PostgreSQL, database-backed sessions and cache.

## Environments

| Folder | Purpose | DB Mode | App Scaling |
|--------|---------|---------|-------------|
| 0 — AI Agent | AI/ZCP-driven development | NON_HA | dev + prod pair |
| 1 — Remote (CDE) | Cloud development environment | NON_HA | dev + prod pair |
| 2 — Local | Local development with Zerops | NON_HA | single prod |
| 3 — Stage | Staging | NON_HA | single prod, autoscale buffer |
| 4 — Small Production | Small production | NON_HA | min 2 containers |
| 5 — Highly-available Production | HA production | HA | min 2, dedicated CPU |

## Quick Start

Import any environment's `import.yaml` via the Zerops GUI or CLI:

```bash
zcli project import ./3\ —\ Stage/import.yaml
```
