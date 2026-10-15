# nextjs static hello world — Zerops Recipe Research

## Overview

- **Software:** Next.js 16.4.x (React 19.3) static export
- **Type:** framework
- **Zerops Runtime:** `nodejs@24` (and `postgresql@18` where the app uses a database)

## Repo

- App repo: `https://github.com/zerops-recipe-apps/nextjs-static-hello-world-app`

## Environment (vault)

Static export bakes `NEXT_PUBLIC_*` at build time. Per-service **`vault.APP_ENV`** (not `envVariables` on import services) is lifted as `RUNTIME_APP_ENV` during build. The app repo maps it explicitly:

`NEXT_PUBLIC_APP_ENV: ${RUNTIME_APP_ENV:-production}` in `zerops.yaml` `build.envVariables` (do not rely on project vault auto-injection).
