# WordPress — Production Environment

This is the production environment for the [WordPress (info + deploy)](https://app.zerops.io/recipes/wordpress?environment=production) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
A production-ready stack on the SERIOUS package: highly-available MariaDB and Valkey (3-node clusters with automatic failover), a 25 GB media bucket, and the app on dedicated CPU scaling across 2–6 containers behind zero-downtime rolling deploys. OPcache is timestamp-frozen and `WP_DEBUG` is off. Use it to run a real, public WordPress site.
<!-- #ZEROPS_EXTRACT_END:intro# -->

# Takeover and Maintenance Guide

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->
- **Secure the admin:** log in at `/wp/wp-admin` as `zadmin` with the generated `WORDPRESS_ADMIN_PASSWORD`, then change both the password and `WORDPRESS_ADMIN_EMAIL`.
- **Custom domain:** add it in Zerops and set `WORDPRESS_URL` to it so every absolute URL is correct; keep Cloudflare (if used) on **Full (strict)**.
- **Real email:** replace Mailpit by setting `SMTP_HOST_OVERRIDE` / `SMTP_PORT_OVERRIDE` (and `WORDPRESS_SMTP_AUTH`/`WORDPRESS_SMTP_USER`/`WORDPRESS_SMTP_PASSWORD`) on the `app` service.
- **Scaling & state:** the app is stateless (media on S3, object cache on Valkey), so raise `maxContainers` freely; MariaDB and Valkey are HA with failover. Enable backups on the `db` service — object storage is NOT backed up by the platform.
- **Upgrades:** bump versions in `composer.json`, `composer update`, push. `wp core update-db` runs automatically on deploy; never update core from the dashboard (disabled and non-durable).
- **Full-page caching:** this stack ships a persistent object cache; put a CDN / edge cache in front for full-page caching that stays coherent across containers.
<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
