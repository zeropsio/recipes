# 4 — Small Production

Small production environment with container redundancy.

- Minimum **2 app containers** for zero-downtime deploys and basic fault tolerance.
- Database runs in **NON_HA** mode (single node) to keep costs manageable.
- Suitable for low-to-medium traffic production workloads.
- Autoscaling enabled — containers scale up under load.
