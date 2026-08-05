# Analog SSR Spartan — Small Production Environment
This is a small production environment for [Analog SSR Spartan (info + deploy)](https://app.zerops.io/recipes/analog-ssr-spartan?environment=small-production) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->

**Small Production** — entry prod (~5 users): one app container plus **oltp-staging** Postgres and **staging** Valkey. Profiles set managed-service RAM; no manual autoscaling in yaml. HA tier scales app replicas and moves data services to `:ha@`.
<!-- #ZEROPS_EXTRACT_END:intro# -->
