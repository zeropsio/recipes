# TanStack Start — Zerops Recipe Research

## Overview

- **Software:** TanStack Start RC (via `@tanstack/react-start` 1.x + Nitro 3)
- **Type:** framework (full-stack React SSR)
- **Official Site:** https://tanstack.com/start/latest
- **Zerops Runtime:** `nodejs@22`

## Zerops Compatibility Assessment

### Requirements

- [x] Stateless app (no DB in hello-world demo)
- [x] Supported runtime (`nodejs@22`, docs recommend Node 18+)
- [x] Binds to `PORT` (default 3000)
- [x] Nitro bundles runtime into `.output/` — no `node_modules` at prod runtime

### Potential Issues

- TanStack Start RC packages may be newer than `min-release-age=7` in recipe `.npmrc` — use `--min-release-age=0` in Zerops build commands.
- Nitro plugin is under active development — pin exact versions in `package.json`.

## Build Configuration

### Build Commands

```bash
npm install --ignore-scripts=false --min-release-age=0
npm run build   # vite build + tsc --noEmit
```

Requires `nitro()` in `vite.config.ts` plugins ([hosting guide](https://tanstack.com/start/latest/docs/framework/react/guide/hosting#nitro)).

### Build Output

- Deploy `.output/` entirely
- Start: `node .output/server/index.mjs`

### Caching

- `node_modules`
- `.nitro`

## Runtime Configuration

| Variable | Required | Description |
|----------|----------|-------------|
| `PORT` | No | Default 3000 |
| `NODE_ENV` | Prod | `production` |

### Health Check

- `GET /` on port 3000

## Service Dependencies

Single `nodejs@22` app service — no database in hello-world recipe.

## References

- https://tanstack.com/start/latest/docs/framework/react/guide/hosting
- https://tanstack.com/start/latest/docs/framework/react/getting-started

## Notes for Terminal Agent

- Closest sibling: `nuxt-ssr-hello-world` (Nitro `.output` deploy pattern) without PostgreSQL.
- Also reference `react-router-ssr-hello-world` for React SSR conventions on Zerops.
