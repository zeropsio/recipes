# Analog SSR + Spartan on Zerops

## Stack

- **Framework:** Analog.js (Angular 22 SSR) + Vite
- **UI:** [spartan/ui](https://spartan.ng/) (vega style, Zerops teal theme)
- **Auth:** Better Auth (email/password on Postgres)
- **Services:** Postgres, Valkey, NATS, Meilisearch, object storage

## Deploy model

- **Runtime:** `nodejs@22` — single Nitro SSR process on port 3000 (prod) / Vite dev on 5173
- **Build:** `npm ci` → bundle migrate/seed → `npm run build`
- **Init:** one-shot migrations + seed on first deploy

## Spartan SSR notes

- Helm components under `libs/ui/` with `@spartan-ng/helm/*` tsconfig paths
- `vite-tsconfig-paths` + `ssr.noExternal: ['@spartan-ng/**']` required for Analog SSR
- Theme in `src/styles.css` using `@spartan-ng/brain/hlm-tailwind-preset.css`

## Sibling reference

Scaffolded from `analog-ssr-better-auth` (same backend topology, Spartan UI frontend).
