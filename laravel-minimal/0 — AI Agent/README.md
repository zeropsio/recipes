# 0 — AI Agent

Dev + prod service pair for AI-driven development via ZCP (Zerops Control Plane).

- **Dev service** starts with code from the repository, used for iterative AI edits.
- **Prod service** mirrors the production setup and builds from the same codebase.
- Database runs in **NON_HA** mode (single node) to minimize cost during development.
- Intended for use with the Zerops AI agent workflow, not manual development.
