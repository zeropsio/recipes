# Umami — Production Environment
This is a Production environment for [Umami (info + deploy)](https://app.zerops.io/recipes/umami?environment=production) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**Production** environment provides a production-ready Umami setup with highly-available components.
_TODO: Update the description to better fit the software._
<!-- #ZEROPS_EXTRACT_END:intro# -->

# Takeover and Maintenance Guide

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->

## Upgrading Umami

> [!NOTE]
> Umami releases: https://github.com/umami-software/umami/releases

1. Add `UMAMI_RELEASE_TAG` environment variable with target Umami version:
```shell
UMAMI_RELEASE_TAG=v3.0.1
```

2. Trigger re-deploy of the `umami` service.

Pipelines & CI/CD Settings Menu > "Trigger a new pipeline" > "Prefill from active deploy"

This will build the Umami app with a new version and run migrations in build phase.

<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
