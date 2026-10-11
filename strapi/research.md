# Strapi — Zerops Recipe Research

## Overview

- **Software:** Strapi 5.12 headless CMS
- **Type:** API + admin (`/admin`)
- **Zerops Runtime:** `nodejs@24`, `postgresql@17`

## Setups

- Only **`dev`** and **`prod`** in app `zerops.yml`.
- Recipe “Stage” tier uses **`zeropsSetup: prod`** on hostname `strapi` / `strapistage`.

## Repo

- `zerops-recipe-apps/strapi` — CMS only, port 1337, `/_health`

## Scaling

| Component | prod floor | Notes |
|-----------|------------|-------|
| Strapi | 1 GB, 0.5 free | Admin + API |
| Postgres stage | oltp-hobby | |
| Postgres small/HA demo | oltp-staging / HA | |

## Composability

Import without frontend; connect any SPA using vault `API_URL` (see `strapi-react-frontend`).

## References

- https://docs.strapi.io/
- https://github.com/zerops-recipe-apps/strapi
