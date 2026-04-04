# Laravel Minimal — Highly-available Production

A minimal Laravel application running on Zerops with PHP-Nginx and PostgreSQL. Demonstrates database connectivity, migrations, and the platform integration points every Laravel app needs.

## Services

| Service | Type | Setup | Description |
|---------|------|-------|-------------|
| app | php-nginx@8.4 | prod | HA production app (2 containers, dedicated CPU) |
| db | postgresql@16 | HA | Highly-available database (3 nodes) |
