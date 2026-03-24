# Laravel Hello World — Remote (CDE) Environment

Cloud Development Environment: mount the remote `/var/www` directory locally via SSHFS, edit files in your IDE, and see changes served immediately by the live Nginx + PHP-FPM stack.

## Deploy

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/green/deploy-button.svg)](https://app.zerops.io/recipe/laravel-hello-world-remote)

## What's included

| Service | Type | Purpose |
|---------|------|---------|
| `appdev` | `php-nginx@8.4` | Development service with live file serving |
| `appstage` | `php-nginx@8.4` | Staging — test prod build before merging |
| `db` | `postgresql@16` | Shared PostgreSQL database |

## Workflow

1. Import `import.yaml` into your Zerops project.
2. Zerops builds `appdev` (dev setup) and `appstage` (prod setup) from the GitHub repo.
3. Mount the remote filesystem locally:
   ```sh
   zcli service remote-login appdev   # opens SSH session
   # or mount with SSHFS for IDE access
   sshfs -p 22 <user>@<host>:/var/www ./appdev
   ```
4. Edit files in your local IDE — changes are reflected immediately via Nginx.
5. Push to staging with `zcli push` when ready.

## Endpoints

After deploy, open the subdomain URLs from the Zerops dashboard:

- `https://appdev-<id>.prg1.zerops.app/` — Dashboard (dev)
- `https://appdev-<id>.prg1.zerops.app/api/health` — Health JSON (dev)
- `https://appstage-<id>.prg1.zerops.app/` — Dashboard (stage)
- `https://appstage-<id>.prg1.zerops.app/api/health` — Health JSON (stage)
