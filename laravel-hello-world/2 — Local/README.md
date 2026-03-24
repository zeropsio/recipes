# Laravel Hello World — Local Environment

Run the app locally against a Zerops-hosted PostgreSQL database. Connect via Zerops VPN (`zcli vpn up`) to access the `db` service directly.

## Deploy

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/green/deploy-button.svg)](https://app.zerops.io/recipe/laravel-hello-world-local)

## What's included

| Service | Type | Purpose |
|---------|------|---------|
| `db` | `postgresql@16` | PostgreSQL — accessible via VPN as `db.zerops` |

## Workflow

1. Import `import.yaml` into your Zerops project.
2. Clone the app repo locally:
   ```sh
   git clone https://github.com/zerops-recipe-apps/laravel-hello-world-app
   cd laravel-hello-world-app
   ```
3. Install dependencies:
   ```sh
   composer install
   ```
4. Configure `.env` with your Zerops project details:
   ```dotenv
   APP_KEY=base64:<your-key>
   APP_URL=http://localhost:8000
   DB_CONNECTION=pgsql
   DB_HOST=db.zerops
   DB_PORT=5432
   DB_DATABASE=db
   DB_USERNAME=<user>
   DB_PASSWORD=<password>
   ```
   Find credentials in the Zerops dashboard under the `db` service → Access details.
5. Start Zerops VPN and run the app:
   ```sh
   zcli vpn up
   php artisan migrate
   php artisan serve
   ```
6. Open `http://localhost:8000/`.

## Endpoints

- `http://localhost:8000/` — Dashboard
- `http://localhost:8000/api/health` — Health JSON
