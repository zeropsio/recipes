# Analog Ssr Better Auth — Small Production Environment
This is a small production environment for [Analog Ssr Better Auth (info + deploy)](https://app.zerops.io/recipes/analog-ssr-better-auth?environment=small-production) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->

**Small Production** runs one app container (**0.5 GB RAM**) plus **oltp-staging** Postgres and **staging** Valkey (profiles set managed RAM). HA tier scales app replicas and moves data services to `:ha@`.
<!-- #ZEROPS_EXTRACT_END:intro# -->
