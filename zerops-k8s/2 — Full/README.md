# Kubernetes on Zerops — Full Environment

This is the full HA demonstration profile for [Kubernetes on Zerops (info + deploy)](https://app.zerops.io/recipes/zerops-k8s?environment=full) on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
**Full** provisions three control planes, three workers, redundant edge, backup storage, and dedicated Grafana/Prometheus plus ELK/APM Zerops services on `corePackage: SERIOUS`. The nested cluster runs Calico, Istio ambient, Gateway API, Longhorn, cert-manager, Headlamp, and telemetry collectors. CNCF conformance is mandatory for this profile.
<!-- #ZEROPS_EXTRACT_END:intro# -->

# Takeover and Maintenance Guide

<!-- #ZEROPS_EXTRACT_START:maintenance-guide# -->

After import, deploy with **Deploy Zerops Kubernetes** (`profile: full`, the workflow default). Rolling maintenance rolls workers first, then control planes, with backup and storage health gates. Retrieve admin kubeconfig and Headlamp tokens from sensitive project variables after a successful run. Configure age encryption keys for etcd/Longhorn recovery before enabling scheduled backups.

<!-- #ZEROPS_EXTRACT_END:maintenance-guide# -->
