# WordPress — Stage Environment

This is the staging environment for the [WordPress (info + deploy)](https://app.zerops.io/recipes/wordpress?environment=stage) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
A single non-HA instance built with the production setup: one app container over single-node MariaDB, Valkey and object storage, with frozen OPcache and `WP_DEBUG` off. For pre-production validation before Small or Highly-available Production.
<!-- #ZEROPS_EXTRACT_END:intro# -->

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->
- **Log in:** open the `app` subdomain, then `/wp/wp-admin` as `zadmin` with the generated `WORDPRESS_ADMIN_PASSWORD`; set a real `WORDPRESS_ADMIN_EMAIL`.
- **Deploys behave like production** — the readiness check gates traffic and OPcache is timestamp-frozen, so push a deploy to pick up code changes (no live editing here).
- **Email:** unset by default — set `SMTP_HOST_OVERRIDE`/`SMTP_PORT_OVERRIDE` (and `WORDPRESS_SMTP_*` auth) to route mail through your SMTP relay.
- **Data** is single-node — treat this env as disposable pre-production.
<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
