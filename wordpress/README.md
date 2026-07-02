# WordPress Recipe

<!-- #ZEROPS_EXTRACT_START:name# -->
WordPress
<!-- #ZEROPS_EXTRACT_END:name# -->

- **Shape:** <!-- #ZEROPS_EXTRACT_START:shape# -->app<!-- #ZEROPS_EXTRACT_END:shape# --> — you fork the app repo and deploy your own copy.

<!-- #ZEROPS_EXTRACT_START:intro# -->
Production-grade [WordPress](https://wordpress.org) on [Zerops](https://zerops.io) — Composer-managed core, an isolated web root, a Redis object cache, S3-backed media, and real cron. Bedrock's 12-factor philosophy, wired natively into the platform.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/wordpress?environment=production)

Offered in two environments:

- **Development** [[info]](/0%20—%20Development) — [[deploy with one click]](https://app.zerops.io/recipes/wordpress?environment=development)
- **Production** [[info]](/1%20—%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/wordpress?environment=production)

<!-- #ZEROPS_EXTRACT_START:description# -->
WordPress runs the open web, but the default "unzip it on a box" setup fights every cloud-native practice: core and plugins live in the document root, uploads pin you to one disk, and configuration hides in a file full of secrets. This recipe reshapes it into a 12-factor app. WordPress core, plugins and themes are Composer dependencies; only a `public/` directory is web-served (config, `vendor/` and tooling sit above it, unreachable over HTTP); every setting is read from the environment. Media is offloaded to S3 object storage and a persistent object cache lives on Valkey, so nothing durable touches the container disk and the app scales horizontally without going stale.

Two environments cover the lifecycle: **Development** is a single low-resource stack with `WP_DEBUG` on for building and testing your site; **Production** promotes the database and cache to highly-available clusters and runs the app on dedicated CPU across multiple containers behind zero-downtime rolling deploys.
<!-- #ZEROPS_EXTRACT_END:description# -->

<!-- #ZEROPS_EXTRACT_START:features# -->
- **Composer-managed WordPress** — core, plugins and themes are dependencies; no in-dashboard file writes (`DISALLOW_FILE_MODS`), so deploys stay reproducible.
- **Isolated web root** — only `public/` is served; `wp-config.php` and `vendor/` live one level up, physically unreachable, not just "denied".
- **Redis object cache** — persistent cache on Valkey (phpredis); the `object-cache.php` drop-in is baked into the build artifact, so every container ships with it and just connects to the managed Valkey — graceful if it's momentarily unreachable.
- **S3 media** — uploads go straight to object storage via `humanmade/s3-uploads`, path-style for MinIO; the container filesystem stays disposable.
- **Zero-downtime deploys** — a readiness check gates traffic on a static core asset; a health check restarts unhealthy containers.
- **Real cron** — WordPress pseudo-cron is disabled; a platform cron runs `wp cron event run` every 5 minutes on one container.
- **Hardened & tuned** — security headers, `xmlrpc.php` blocked, no PHP execution under uploads, production OPcache, WP-CLI pinned by checksum.
- **Email out of the box** — mail is routed to a bundled Mailpit; point it at a real SMTP relay with one env override.
<!-- #ZEROPS_EXTRACT_END:features# -->

<!-- #ZEROPS_EXTRACT_START:takeover-guide# -->
### First-run setup
1. **Open the site** — the `app` service's subdomain is the public URL. WordPress installs itself on first boot; there is no `wp-admin/install.php` step to click through.
2. **Log in** — go to `/wp/wp-admin`. The admin username defaults to `zadmin` and the password is the generated `WORDPRESS_ADMIN_PASSWORD` — read it from the `app` service's env vars in the Zerops GUI, then change it.
3. **Set the admin email** — `WORDPRESS_ADMIN_EMAIL` ships as a placeholder; update it in **Settings → General** so password resets and notifications reach you.

### Configure
- **Add plugins/themes via Composer, not the dashboard** — the file editor and installer are disabled because the filesystem is rebuilt on every deploy. `composer require wpackagist-plugin/<slug>`, commit, push.
- **Email** — mail goes to the bundled Mailpit (open its subdomain to read it). For real delivery set `SMTP_HOST_OVERRIDE` / `SMTP_PORT_OVERRIDE` (and `WORDPRESS_SMTP_*` auth) on the `app` service.
- **Custom domain** — add it in Zerops, then set `WORDPRESS_URL` to it (it defaults to the Zerops subdomain); WordPress uses it for every absolute URL.

### Upgrade
Bump `johnpbloch/wordpress` (and plugins) in `composer.json`, run `composer update`, commit and push. The deploy's `upgrade.sh` runs `wp core update-db`, so schema migrations apply automatically before traffic resumes — do NOT update core from the dashboard (it's disabled, and any write would be lost on the next deploy).
<!-- #ZEROPS_EXTRACT_END:takeover-guide# -->

<!-- #ZEROPS_EXTRACT_START:knowledge-base# -->
### Architecture
The `app` service (php-nginx) serves only `public/`; WordPress core is in `public/wp`, content in `public/wp-content`, and the real `wp-config.php` sits at the repo root — above the web root, so it can never be served. State is externalized: `db` (MariaDB) holds content, `storage` (object storage) holds media via `humanmade/s3-uploads`, and `cache` (Valkey) holds the persistent object cache via `redis-cache`. The `object-cache.php` drop-in is baked into the build artifact — copied from the version-matched `redis-cache` plugin during the build — so it ships inside every immutable container and connects to the managed Valkey on boot, with no runtime install step.

### Environment variables
- **Wired for you (in the app's `zerops.yaml`):** `WORDPRESS_DB_*` ← `db`, `WORDPRESS_STORAGE_*` ← `storage`, `WORDPRESS_REDIS_*` ← `cache`, `WORDPRESS_URL` ← the subdomain.
- **Generated secrets (in `import.yaml`):** the eight auth keys/salts and `WORDPRESS_ADMIN_PASSWORD`.
- **Yours to set:** `WORDPRESS_ADMIN_EMAIL`, and `SMTP_HOST_OVERRIDE`/`SMTP_PORT_OVERRIDE` for a real mail relay.
- **Booleans are coerced** — `WORDPRESS_DEBUG` etc. are parsed with `FILTER_VALIDATE_BOOLEAN`, so the string `"false"` is actually false (in plain WordPress it would be truthy and silently turn debug ON).

### Troubleshooting
- **Redis "connection timed out" right after deploy** — the drop-in degrades gracefully (`WP_REDIS_GRACEFUL`); the container serves uncached until Valkey warms up, then reconnects. Persistent failure → check the `cache` service and `WORDPRESS_REDIS_PASSWORD` (Valkey auth is mandatory on Zerops).
- **Media 404s** — media URLs point at the `storage` endpoint, not the app domain; confirm the bucket policy is `public-objects-read` and `mu-plugins/s3.php` set `use_path_style_endpoint`.
- **Uploads rejected at 50 MB** — that's the L7 balancer cap on the `*.zerops.app` subdomain, not PHP; use a custom domain for larger files.
<!-- #ZEROPS_EXTRACT_END:knowledge-base# -->

---

For more examples see all [CMS recipes](https://app.zerops.io/recipes?lf=cms) on Zerops.

Need help setting your project up? Join the [Zerops Discord community](https://discord.gg/zeropsio).
