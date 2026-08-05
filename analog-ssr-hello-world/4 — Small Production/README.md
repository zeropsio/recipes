# Analog SSR Hello World - Small Production Environment

This is [a small production environment](https://app.zerops.io/recipes/analog-ssr-hello-world?environment=small-production) for [Analog SSR Hello World (info + deploy)](https://app.zerops.io/recipes/analog-ssr-hello-world?environment=small-production) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**Small production** — entry prod (~5 users): one SSR app container plus **oltp-staging** Postgres. Profiles and platform defaults set RAM — no manual autoscaling in yaml. HA tier adds a second app replica and `:ha@` Postgres.
<!-- #ZEROPS_EXTRACT_END:intro# -->
