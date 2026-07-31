# Kubernetes on Zerops — Staging Environment

This is the minimal staging profile for [Kubernetes on Zerops (info + deploy)](https://app.zerops.io/recipes/zerops-k8s?environment=staging) on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**Staging** provisions one control plane, one worker, and a two-instance Keepalived/HAProxy edge on `corePackage: LIGHT`. Traefik Gateway API and metrics-server run inside the cluster; there is no object storage, Longhorn, backups, or dedicated observability stack. Intended for disposable validation — API maintenance causes expected outage.
<!-- #ZEROPS_EXTRACT_END:intro# -->

# Takeover and Maintenance Guide

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->

After import, deploy with **Deploy Zerops Kubernetes** (`profile: staging`) from [zerops-recipe-apps/zerops-k8s](https://github.com/zerops-recipe-apps/zerops-k8s). Backup, restore, and horizontal worker resize workflows are rejected for this profile. Platform logs and statistics on the three outer runtimes (`k8scp1`, `k8sworker1`, `k8sedge`) cover operational visibility.

<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
