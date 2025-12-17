# Zerops Recipe Agent Instructions

You are an AI agent tasked with creating and maintaining Zerops recipes. You operate on the filesystem at
`~/code/zerops/recipes` and related repositories.

## System Overview

Zerops recipes are deployable solution templates displayed in the Zerops GUI. Each recipe consists of:

1. **Recipe folder** in `github.com/zeropsio/recipes` — contains environments with `import.yaml` files
2. **App repositories** in `github.com/zerops-recipe-apps` (or any public Git repo) — contain source code,
   `zerops.yaml`, and documented READMEs
3. **Strapi record** — metadata linking everything together (handled by humans)

### Recipe Categories

| Category                | Template        | Environments                                                               | Example             |
|-------------------------|-----------------|----------------------------------------------------------------------------|---------------------|
| **Language Example**    | `_template`     | agent, remote, local, stage, small-production, highly-available-production | `bun-hello-world`   |
| **Framework**           | `_template`     | (same as above)                                                            | `laravel-jetstream` |
| **OSS (source-based)**  | `_template_oss` | development, production                                                    | `strapi`            |
| **OSS (install-based)** | `_template_oss` | development, production                                                    | `umami`             |

### Audience & Voice

Your documentation speaks to **developers deploying on Zerops**. The content appears in:

- Recipe detail pages (intro fragments)
- Integration guides (how to adapt apps for Zerops)
- Knowledge base (tips, maintenance, troubleshooting)

Write in second person ("you"), be concise, and focus on Zerops-specific adaptations.

---

## Your Constraints

1. **Filesystem only** — Make changes to files; humans handle git push and Strapi
2. **No testing** — Humans will test; focus on correct configuration
3. **Respect `.human` markers** — Never modify recipes/apps containing a `.human` file; use them as reference only
4. **Use research.md** — Base your work on the researcher's output

---

## Recipe Specification Form

You will receive specifications in this format:

```yaml
category: language-example | framework | oss-source | oss-install
tags: [ bun, javascript ]  # lowercase, for filtering
languages_frameworks: [ Bun, JavaScript ]  # pretty names for Strapi
name: bun-hello-world  # folder name, kebab-case
pretty_name: Bun Hello World  # display name
description: >
  Simple language example recipe showcasing basics of how to use Bun on Zerops.
  Contains a simple HTTP API application that connects to and queries a database.
cover_svg: cover-bun.svg  # from recipe-shared-assets/covers
apps:
  - name: bun-hello-world-app
    description: The Bun application source code with commented zerops.yaml
    repo_url: https://github.com/zerops-recipe-apps/bun-hello-world-app
notes:
  - Bun is a JavaScript runtime, similar to Node.js
  - Uses SQLite for simplicity in examples
research_file: ./research/bun-hello-world.md
```

---

## File Structure to Create

### For Language Examples / Frameworks (`_template`)

```
recipes/
└── {name}/
    ├── README.md                    # intro fragment
    ├── agent/
    │   ├── import.yaml              # minimal resources, dev tools
    │   └── README.md                # environment intro
    ├── remote/
    │   ├── import.yaml
    │   └── README.md
    ├── local/
    │   ├── import.yaml
    │   └── README.md
    ├── stage/
    │   ├── import.yaml              # low resources, single instances
    │   └── README.md
    ├── small-production/
    │   ├── import.yaml              # moderate resources
    │   └── README.md
    └── highly-available-production/
        ├── import.yaml              # high resources, multiple replicas
        └── README.md

zerops-recipe-apps/
└── {app-name}/
    ├── README.md                    # integration-guide, knowledge-base fragments
    ├── zerops.yaml                  # fully commented build/deploy config
    └── src/...                      # application source
```

### For OSS Projects (`_template_oss`)

```
recipes/
└── {name}/
    ├── README.md
    ├── development/
    │   ├── import.yaml
    │   └── README.md                # may include maintenance-guide fragment
    └── production/
        ├── import.yaml
        └── README.md
```

---

## YAML Syntax Reference

### Schema URLs

Always include the schema reference at the top of YAML files:

- **import.yaml:**
  `# yaml-language-server: $schema=https://api.app-prg1.zerops.io/api/rest/public/settings/import-project-yaml-json-schema.json`
- **zerops.yaml:**
  `# yaml-language-server: $schema=https://api.app-prg1.zerops.io/api/rest/public/settings/zerops-yaml-json-schema.json`

Refer to these schemas for available service types, configuration options, and valid values.

### import.yaml Structure

```yaml
# yaml-language-server: $schema=https://api.app-prg1.zerops.io/api/rest/public/settings/import-project-yaml-json-schema.json

# Project name - displayed in Zerops dashboard
project:
  name: bun-hello-world

# Services to deploy
services:
  # Application service - built from any public Git repository
  - hostname: app
    type: bun@latest
    # Enable public access via Zerops subdomain
    zeropsSubdomain:
      suffix: app
    # Build from public Git repository (can be any public repo, not just zerops-recipe-apps)
    buildFromGit: https://github.com/zerops-recipe-apps/bun-hello-world-app

  # Database service - managed by Zerops
  - hostname: db
    type: postgresql@16
    mode: HA  # High Availability - use NON_HA for dev/stage
    # Services are sorted by priority in descending order before creation
    # Higher priority = created sooner (e.g., DB before app)
    priority: 10
```

### zerops.yaml Structure

```yaml
# yaml-language-server: $schema=https://api.app-prg1.zerops.io/api/rest/public/settings/zerops-yaml-json-schema.json

# Service name must match hostname in import.yaml
app:
  # Build configuration
  build:
    # Base image - see https://docs.zerops.io/zerops-yaml/base-list
    base: bun@latest
    # Commands to build the application
    buildCommands:
      - bun install
      - bun run build
    # Files/folders to deploy (relative to repo root)
    deployFiles:
      - dist
      - package.json
    # Cache between builds - see https://docs.zerops.io/features/build-cache
    cache:
      - node_modules

  # Runtime configuration
  run:
    # Command to start the application
    start: bun run start
```

### Key Documentation

Consult these resources for configuration details:

- [Service Type List](https://docs.zerops.io/references/import-yaml/type-list) — available `type` values
- [Runtime Base List](https://docs.zerops.io/zerops-yaml/base-list) — available `base` values
- [Environment Variables](https://docs.zerops.io/features/env-variables) — variable syntax and interpolation
- [Scaling & HA](https://docs.zerops.io/features/scaling-ha) — scaling configuration
- [zerops.yaml Specification](https://docs.zerops.io/zerops-yaml/specification) — full reference

---

## Fragment Syntax

```markdown
<!-- #ZEROPS_EXTRACT_START:{key}# -->
Content extracted by the recipe system.
Markdown formatting supported.
<!-- #ZEROPS_EXTRACT_END:{key}# -->
```

### Required Fragments by Location

| Location                             | Required Fragments           |
|--------------------------------------|------------------------------|
| `recipes/{name}/README.md`           | `intro`                      |
| `recipes/{name}/{env}/README.md`     | `intro`                      |
| `zerops-recipe-apps/{app}/README.md` | `intro`, `integration-guide` |
| OSS app README                       | `intro`, `maintenance-guide` |

Optional: `knowledge-base` (anywhere, as needed)

---

## Comment Style Guide

**Purpose:** Comments serve both users AND future LLM training. Be thorough.

### Do:

- Explain WHY, not just WHAT
- Note Zerops-specific requirements
- Reference documentation URLs
- Warn about common pitfalls
- Use consistent formatting

### Don't:

- State the obvious (`# This is the project name`)
- Leave placeholder comments
- Write essays — be concise but complete

### Example (good):

```yaml
services:
  - hostname: db
    type: postgresql@16
    # HA mode provides automatic failover and read replicas
    # Use NON_HA for development to reduce costs
    mode: HA
    # Higher priority = created first. DB must exist before app starts.
    priority: 10
```

---

## Human-Written Reference Recipes

Study these recipes (marked with `.human`) as examples. **Never modify these**, only use for reference:

| Recipe               | Category         | Notable For                      |
|----------------------|------------------|----------------------------------|
| `bun-hello-world`    | language-example | Simple structure, good comments  |
| `go-hello-world`     | language-example | Compiled language example        |
| `nestjs-hello-world` | language-example | Node.js framework variant        |
| `django`             | framework        | Python framework with migrations |
| `laravel-jetstream`  | framework        | PHP framework with full stack    |
| `strapi`             | oss-source       | npm prepare workflow, CMS        |
| `umami`              | oss-install      | Install-based OSS, analytics     |
| `elk`                | oss-install      | Multi-service stack              |
| `mailpit`            | oss-install      | Single-service utility           |

---

## Workflow Checklist

1. [ ] Read `research.md` thoroughly
2. [ ] Copy appropriate template (`_template` or `_template_oss`)
3. [ ] Replace all `PLACEHOLDER_*` values
4. [ ] Create/update app repository structure
5. [ ] Write `zerops.yaml` with full comments (reference schema and docs)
6. [ ] Write `import.yaml` for each environment (adjust scaling per environment)
7. [ ] Add all required fragments to READMEs
8. [ ] Ensure READMEs make sense when viewed on GitHub directly
9. [ ] Verify no references to placeholder text remain
10. [ ] Create `recipe-output.yaml` for humans to use in Strapi

---

## Output for Humans

After completing your work, generate a summary:

```yaml
# recipe-output.yaml
recipe_created: bun-hello-world
files_created:
  - recipes/bun-hello-world/README.md
  - recipes/bun-hello-world/agent/import.yaml
  - recipes/bun-hello-world/agent/README.md
  # ... list all files
apps_created:
  - zerops-recipe-apps/bun-hello-world-app
strapi_fields:
  recipe_name: Bun Hello World
  slug: bun-hello-world
  recipe_source: bun-hello-world  # must match folder name
  categories: [ ]  # TODO: see fixed category list
  languages_frameworks: [ Bun, JavaScript ]
  internal_type: example
ready_for_testing: true
notes:
  - Database uses PostgreSQL 16
  - Health check endpoint at /health
```

---

## TODO (For Humans)

- [ ] **Strapi API automation** — Investigate curl commands to create recipe records programmatically
- [ ] **Fixed category list** — Document the complete list of available categories for Strapi
- [ ] **Icon field** — Clarify if icon field will be removed or how it should be populated