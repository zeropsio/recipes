# WordPress — Highly-available Production Environment

This is the highly-available production environment for the [WordPress (info + deploy)](https://app.zerops.io/recipes/wordpress?environment=highly-available-production) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
The full production topology: highly-available MariaDB and Valkey clusters with automatic failover, a 50 GB media bucket, and the app on dedicated CPU scaling 2 → 6 containers behind zero-downtime rolling deploys. OPcache is timestamp-frozen and `WP_DEBUG` is off. Built to run a real, public WordPress site at scale.
<!-- #ZEROPS_EXTRACT_END:intro# -->

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->
- **Secure the admin:** log in at `/wp/wp-admin` as `zadmin` with the generated `WORDPRESS_ADMIN_PASSWORD`, then change both it and `WORDPRESS_ADMIN_EMAIL`.
- **Custom domain:** add it in Zerops and set `WORDPRESS_URL` to it so every absolute URL is correct; disable subdomain access once it's live. Keep Cloudflare (if used) on **Full (strict)**.
- **Email:** set `SMTP_HOST_OVERRIDE`/`SMTP_PORT_OVERRIDE` (and `WORDPRESS_SMTP_*` auth) to route mail through your relay; unset, WordPress uses PHP's default `mail()`.
- **Scaling & state:** the app is stateless (media on S3, object cache on Valkey), so raise `maxContainers` freely; MariaDB and Valkey are HA with failover. Enable backups on the `db` service — object storage is NOT backed up by the platform.
- **Full-page caching:** this stack ships a persistent object cache; put a CDN / edge cache in front for full-page caching that stays coherent across containers.
- **Upgrades:** bump versions in `composer.json`, `composer update`, push. `wp core update-db` runs automatically on deploy; never update core from the dashboard.
<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
