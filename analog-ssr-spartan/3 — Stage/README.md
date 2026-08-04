# Analog SSR Spartan — Stage Environment
This is a stage environment for [Analog SSR Spartan (info + deploy)](https://app.zerops.io/recipes/analog-ssr-spartan?environment=stage) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->

**Stage** environment uses the same service shape as Small Production, but runs a single app container — sized for rehearsal traffic and QA runs against realistic data, not sustained load. Managed Postgres and Valkey use **hobby** profiles (~0.5 GB).
<!-- #ZEROPS_EXTRACT_END:intro# -->
