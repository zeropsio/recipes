# 1 — Remote (CDE)

Cloud Development Environment — dev + prod service pair for human developers.

- Same topology as the AI Agent tier but designed for interactive cloud development.
- **Dev service** runs in development mode with debugging enabled.
- **Prod service** validates production builds alongside development.
- Database runs in **NON_HA** mode (single node).
- Connect via SSH, VS Code Remote, or any CDE-compatible tooling.
