# WordPress — Remote (CDE) Environment

This is the remote cloud-development environment for the [WordPress (info + deploy)](https://app.zerops.io/recipes/wordpress?environment=remote-cde) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
One cloud development container carrying the whole app (the `dev` setup: full Composer build, OPcache revalidation for live edits) plus single-node MariaDB, Valkey and object storage. Connect your IDE or SSH and iterate inside Zerops with no local toolchain; the `app` subdomain serves what you build.
<!-- #ZEROPS_EXTRACT_END:intro# -->

- **Iterate:** edit the mounted source over SSH; OPcache revalidates on each request, so changes show without a restart. Plugins/themes still come via Composer (`composer require wpackagist-plugin/<slug>`).
- **Log in:** open the `app` subdomain, then `/wp/wp-admin` as `zadmin` with the generated `WORDPRESS_ADMIN_PASSWORD` (in the `app` service env).
- **Email:** unset by default — set `SMTP_HOST_OVERRIDE` to route mail through your SMTP relay.
