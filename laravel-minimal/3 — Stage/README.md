# 3 — Stage

Staging environment with autoscale RAM buffer.

- Single production app service with `minFreeRamGB: 0.25` for autoscale headroom.
- Database runs in **NON_HA** mode (single node).
- Mirrors production configuration at lower resource allocation.
- Use this tier to validate deployments before promoting to production.
