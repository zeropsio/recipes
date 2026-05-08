# Stage

_[← back to recipe root](../README.md)_

<!-- #ZEROPS_EXTRACT_START:intro# -->
Tier 3 — Stage. Same single-slot shape and shared-CPU runtime as tier 2, but with a 0.25 GB minFreeRamGB spike buffer on every container so rehearsal load doesn't push the working set into swap. Single-instance managed services with snapshot recovery; rehearsal-grade data, manual-restore window acceptable.
<!-- #ZEROPS_EXTRACT_END:intro# -->

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/nestjs-showcase?environment=stage)
