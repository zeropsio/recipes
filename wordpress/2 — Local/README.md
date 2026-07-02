# WordPress — Local Environment

This is the local-development environment for the [WordPress (info + deploy)](https://app.zerops.io/recipes/wordpress?environment=local) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
Just the backing stores — MariaDB, Valkey and object storage — and no app container. Bring up the Zerops VPN (`zcli vpn up`) and run WordPress on your own machine, pointing `WORDPRESS_DB_*`, `WORDPRESS_REDIS_*` and `WORDPRESS_STORAGE_*` at the internal `db` / `cache` / `storage` hostnames. The cheapest way to develop against real managed services.
<!-- #ZEROPS_EXTRACT_END:intro# -->

- **Connect:** `zcli vpn up` into the project, then reach `db`, `cache` and `storage` by hostname over the VPN.
- **Run WordPress locally** against those services — `wp-config.php` reads everything from the environment, so point the `WORDPRESS_*` connection vars at the internal hostnames.
- No app container is deployed here — promote to **Stage** or a **Production** env to run WordPress on Zerops itself.
