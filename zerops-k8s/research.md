# Kubernetes on Zerops — Recipe Research

## Overview

- **Software:** Upstream Kubernetes (pinned in `versions.env`, currently v1.36.x)
- **Type:** infrastructure / OSS (nested cluster on Zerops Docker runtimes)
- **Automation repo:** [zerops-recipe-apps/zerops-k8s](https://github.com/zerops-recipe-apps/zerops-k8s)
- **Zerops runtimes:** `docker@26.1.5` (nodes), `go@1.22` (edge agent), plus profile-specific observability services on **Full**

## Deploy model

Unlike hello-world recipes, this is a **two-phase** deploy:

1. **Import** (recipes repo) — creates Zerops project service inventory with `startWithoutCode: true`. No `buildFromGit` on node services; the GitHub Actions workflow applies `zerops.yaml` setups and bootstraps kubeadm.
2. **Reconcile** (automation repo) — owner-triggered workflows build node agents, load pinned node images, join the cluster, install add-ons, and run acceptance tests.

Three profiles are **mutually exclusive** per project: `staging`, `production`, `full`.

## Profile summary

| Profile | Control planes | Workers | Edge | Backup storage | In-cluster add-ons | Observability |
|---------|----------------|---------|------|----------------|-------------------|---------------|
| staging | 1 | 1 | 2× VRRP/HAProxy | none | Calico, Traefik, metrics-server | Zerops logs/stats only |
| production | 1 | 2 (+ optional 3rd) | 2× VRRP/HAProxy | 25 GB object storage | Calico, Traefik, Longhorn, metrics-server | Zerops logs/stats only |
| full | 3 | 3 (+ optional 4th) | 2× VRRP/HAProxy | 25 GB object storage | Calico, Istio ambient, Gateway API, Longhorn, cert-manager, Headlamp, collectors | Grafana, Prometheus, ELK stack |

## Zerops compatibility

- [x] Docker runtime for nested kubeadm nodes
- [x] Object storage for node image cache and backups (production/full)
- [x] VRRP VIP derived from project `/22` — no hard-coded project addresses in imports
- [x] VPN-only API and Headlamp; demo ingress on private VIP
- [x] `#yamlPreprocessor=on` for Grafana/ELK secrets on full profile

## Recipe repo layout

Custom OSS layout (not `_template` six-env lifecycle):

```
zerops-k8s/
├── 0 — Staging/import.yaml
├── 1 — Production/import.yaml
└── 2 — Full/import.yaml
```

Environment slugs: `staging`, `production`, `full`.

## Assets gap

- **Cover SVG:** no `cover-kubernetes.svg` in recipe-shared-assets yet — README temporarily uses `cover-go.svg` (edge agent runtime). Add a Kubernetes cover before Strapi registration.

## References

- [zerops-k8s README](https://github.com/zerops-recipe-apps/zerops-k8s/blob/main/README.md)
- [profiles.md](https://github.com/zerops-recipe-apps/zerops-k8s/blob/main/docs/profiles.md)
- [operations.md](https://github.com/zerops-recipe-apps/zerops-k8s/blob/main/docs/operations.md)
