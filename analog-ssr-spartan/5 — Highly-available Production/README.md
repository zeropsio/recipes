# Analog SSR Spartan — Highly-available Production Environment
This is a highly-available production environment for [Analog SSR Spartan (info + deploy)](https://app.zerops.io/recipes/analog-ssr-spartan?environment=highly-available-production) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->

**Highly-available Production** environment provides zero-single-point-of-failure infrastructure for production traffic that can't tolerate a database or cache outage — dedicated CPU, the SERIOUS core package, and the `:ha` variant on db, cache, and broker, with a 1 GB managed-RAM floor. HA Postgres and Valkey use **staging** profiles (demo-scale HA, not production ~4 GB) — bump profiles when traffic outgrows hello-world scale.
<!-- #ZEROPS_EXTRACT_END:intro# -->
