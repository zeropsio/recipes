# WordPress — AI Agent Environment

This is the AI-agent development environment for the [WordPress (info + deploy)](https://app.zerops.io/recipes/wordpress?environment=ai-agent) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
A dev + stage pair — the topology this recipe was built on. The `appdev` container builds with the `dev` setup and boots with the source ready for an AI agent (or you) to adopt and drive on the mounted filesystem, OPcache revalidating so edits show immediately; `appstage` builds with the production setup as an always-running reference. Single-node MariaDB, Valkey and object storage back both. Lightweight and non-HA.
<!-- #ZEROPS_EXTRACT_END:intro# -->

- **Two app services:** `appdev` (development build, edit-and-reload) and `appstage` (production build). Each has its own subdomain; both share the `db` / `cache` / `storage` services.
- **Log in:** open either subdomain, then `/wp/wp-admin` as `zadmin` with the generated `WORDPRESS_ADMIN_PASSWORD` (in that service's env). WordPress installs itself on first boot.
- **Add plugins/themes via Composer**, not the dashboard (`composer require wpackagist-plugin/<slug>`) — the filesystem is rebuilt on every deploy.
- **Email** is not wired here — set `SMTP_HOST_OVERRIDE` on a service to route mail through your own SMTP relay.
