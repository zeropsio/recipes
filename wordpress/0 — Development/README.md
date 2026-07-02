# WordPress — Development Environment

This is the development environment for the [WordPress (info + deploy)](https://app.zerops.io/recipes/wordpress?environment=development) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
A single low-resource stack — single-node MariaDB and Valkey, a 2 GB bucket, one shared-CPU app container — with `WP_DEBUG` on and OPcache timestamp validation enabled so file edits over SSH take effect immediately. Use it to build and test a site, evaluate plugins, or run a staging copy. Not sized for public traffic — promote to **Production** for that.
<!-- #ZEROPS_EXTRACT_END:intro# -->

# Takeover and Maintenance Guide

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->
- **Log in:** open the `app` subdomain, then `/wp/wp-admin` as `zadmin` with the generated `WORDPRESS_ADMIN_PASSWORD` (in the `app` service env). Set a real `WORDPRESS_ADMIN_EMAIL`.
- **Iterate:** edit files in the SSHFS-mounted `app` service; OPcache revalidates on every request in this env, so changes show without a restart. Plugins/themes are still added via Composer (`composer require wpackagist-plugin/<slug>`), not the dashboard.
- **Email:** all mail is captured by the bundled **Mailpit** — open its subdomain to read it. Nothing leaves the project.
- **Data:** MariaDB and the object-storage bucket are single-node here (no HA, no backup on object storage) — treat this env as disposable.
<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
