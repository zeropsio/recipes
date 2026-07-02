# WordPress — Small Production Environment

This is a production environment for the [WordPress (info + deploy)](https://app.zerops.io/recipes/wordpress?environment=small-production) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
A production-ready stack sized for moderate traffic: single-node MariaDB, Valkey and a 10 GB media bucket, with the app on shared CPU scaling 1 → 2 containers behind readiness-gated rolling deploys. OPcache is timestamp-frozen and `WP_DEBUG` is off. The cheapest way to run a real, public WordPress site; not redundant.
<!-- #ZEROPS_EXTRACT_END:intro# -->

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->
- **Secure the admin:** log in at `/wp/wp-admin` as `zadmin` with the generated `WORDPRESS_ADMIN_PASSWORD`, then change both it and `WORDPRESS_ADMIN_EMAIL`.
- **Custom domain:** add it in Zerops, set `WORDPRESS_URL` to it, and disable subdomain access once it's live.
- **Email:** set `SMTP_HOST_OVERRIDE`/`SMTP_PORT_OVERRIDE` (and `WORDPRESS_SMTP_AUTH`/`WORDPRESS_SMTP_USER`/`WORDPRESS_SMTP_PASSWORD`) to route mail through your relay; unset, WordPress uses PHP's default `mail()`.
- **Backups & scaling:** enable backups on the `db` service (object storage is NOT backed up by the platform). The app is stateless (media on S3, cache on Valkey), so raise `maxContainers` freely. Step up to **Highly-available Production** for HA stores with failover.
- **Upgrades:** bump versions in `composer.json`, `composer update`, push — `wp core update-db` runs on deploy; never update core from the dashboard.
<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
