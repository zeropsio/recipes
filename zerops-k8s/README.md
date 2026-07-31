# Kubernetes on Zerops Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
Run upstream [Kubernetes](https://kubernetes.io/) inside a single Zerops project — nested kubeadm cluster, Calico CNI, Gateway API ingress, and profile-specific add-ons (Istio/Longhorn/Headlamp on **Full**, Traefik/Longhorn on **Production**, Traefik-only on **Staging**). Cluster lifecycle is driven by [zerops-recipe-apps/zerops-k8s](https://github.com/zerops-recipe-apps/zerops-k8s) GitHub Actions after the project import.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/zerops-k8s?environment=full)

![kubernetes](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-go.svg)

Three **mutually exclusive** profiles — import exactly one per project:

- **Staging** [[info]](/0%20—%20Staging) — [[deploy with one click]](https://app.zerops.io/recipes/zerops-k8s?environment=staging)
- **Production** [[info]](/1%20—%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/zerops-k8s?environment=production)
- **Full** [[info]](/2%20—%20Full) — [[deploy with one click]](https://app.zerops.io/recipes/zerops-k8s?environment=full)

After import, connect the Zerops VPN and run **Deploy Zerops Kubernetes** from the [automation repository](https://github.com/zerops-recipe-apps/zerops-k8s/actions) with the matching `profile`. Do not import a second profile over a running cluster — profile changes are deliberate clean replacements.

## Take-over guide

<!-- #ZEROPS_EXTRACT_START:takeover-guide# -->

### Post-import deployment

1. Import one profile (creates Zerops services with `startWithoutCode`; no nested cluster yet).
2. Fork or clone [zerops-recipe-apps/zerops-k8s](https://github.com/zerops-recipe-apps/zerops-k8s).
3. Configure repository secrets and variables (`ZEROPS_TOKEN`, `ZEROPS_PROJECT_ID`, `ZEROPS_CLIENT_ID`, `K8S_PROFILE`, age backup keys for Full/Production).
4. Run **Deploy Zerops Kubernetes** with the same `profile` as the import.

### Access

Connect the Zerops VPN. The Kubernetes API, Headlamp (Full only), and demo ingress use a project-local VRRP VIP (`https://<derived-vrrp-vip>:6443`). Retrieve kubeconfig and Headlamp tokens from sensitive Zerops project variables after a successful deploy run — never from repository files.

### Operations

Use the profile-aware workflows in the automation repo: maintenance, upgrade, resize, backup, restore drill, destroy. See [docs/operations.md](https://github.com/zerops-recipe-apps/zerops-k8s/blob/main/docs/operations.md).

<!-- #ZEROPS_EXTRACT_END:takeover-guide# -->

---

For more infrastructure examples see all [DevOps recipes](https://app.zerops.io/recipes?lf=devops) on Zerops.

Need help setting your project up? Join [Zerops Discord community](https://discord.gg/zeropsio).
