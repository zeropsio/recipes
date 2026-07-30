# Kubernetes on Zerops — Production Environment

This is the compact production profile for [Kubernetes on Zerops (info + deploy)](https://app.zerops.io/recipes/zerops-k8s?environment=production) on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**Production** provisions one control plane (not HA), two workers, redundant VRRP/HAProxy edge, and private backup object storage on `corePackage: SERIOUS`. Calico, Traefik Gateway API, Longhorn, and metrics-server run inside the cluster. Zerops platform observability covers outer runtimes — no dedicated Grafana/ELK services.
<!-- #ZEROPS_EXTRACT_END:intro# -->

# Takeover and Maintenance Guide

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->

After import, deploy with **Deploy Zerops Kubernetes** (`profile: production`). Sole control-plane maintenance interrupts the Kubernetes API until the node recovers — choose **Full** when etcd quorum and control-plane failover are required. Backup and restore drill workflows are supported; configure `K8S_RECOVERY_AGE_RECIPIENT` and `K8S_RECOVERY_AGE_IDENTITY` before first backup.

<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
