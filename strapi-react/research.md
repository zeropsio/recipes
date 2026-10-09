# Strapi + React — Zerops Recipe Research

## Overview

- **Software:** Strapi 5.12 + React 19 (Vite) SPA
- **Type:** headless CMS + static frontend
- **Zerops Runtime:** `nodejs@22` (Strapi), `nodejs@24` build + `static` (frontend), `postgresql@17`

## Setups

- Only **`dev`** and **`prod`** in each app `zerops.yml`.
- Recipe “Stage” tier uses **`zeropsSetup: prod`** on hostnames `strapi` / `frontend`.

## Split repos

- `strapi-react` — CMS, port 1337, `/_health`
- `strapi-react-frontend` — `VITE_API_URL` from vault `API_URL`

## Scaling

| Component | prod floor | Notes |
|-----------|------------|-------|
| Strapi | 1 GB, 0.5 free | Admin + API |
| Frontend static | platform default | Nginx serves `dist/` |
| Postgres stage | oltp-hobby | |
| Postgres small/HA demo | oltp-staging | |

## Composability

Omit frontend services for Mate/ZCP CMS-only imports.

## References

- https://docs.strapi.io/
- https://github.com/zerops-recipe-apps/strapi-react
