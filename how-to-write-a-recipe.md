# How to Write a Zerops Recipe

## Quick Links

| Resource               | URL                                                                                            | Notes                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Recipe System GUI      | https://stage-34.prg1.zerops.app/recipes                                                       | Uses production backend/data — be careful not to be logged in as a real user                         |
| Strapi Admin (Recipes) | https://api-d89-1337.prg1.zerops.app/admin/content-manager/collection-types/api::recipe.recipe | Recipes use cache for GitHub repo data. Click "Refresh Cache" in recipe detail after pushing changes |
| Cover SVGs             | https://github.com/zeropsio/recipe-shared-assets/tree/main/covers                              | Shared logo/cover assets                                                                             |

### Internal Notes

- [Notes after 1st iteration](https://www.dropbox.com/scl/fi/g5ndejel1irjvv3m6uhom/Recipe-system-poznamky.paper?rlkey=1ikfof3o9s2yzg8awe4kipt8m&dl=0)
- [Zerops 2026](https://www.dropbox.com/scl/fi/6odrk21hxh0tvk0su7vui/Zerops-launch-2026.paper?rlkey=ukor1l7tz7ili11lqsdeqah90&dl=0)
- [Discord thread](https://discord.com/channels/735781031147208777/1151834963688304680/1441340949258174544)

---

## Recipe Types & Templates

There are two recipe templates, each designed for different use cases:

### `_template` — Languages & Frameworks

Use for simple language examples or framework starters (e.g., Go Hello World, Bun API).

**Environments included:**

- `agent` — AI Agent development space
- `remote` — Remote (CDE) cloud development
- `local` — Local development setup
- `stage` — Staging environment
- `small-production` — Small Production deployment
- `highly-available-production` — Highly-Available Production deployment

### `_template_oss` — Open-Source Projects

Use for deploying open-source software (e.g., Strapi, Umami, ELK stack).

**Environments included:**

- `development`
- `production`

#### Two OSS Deployment Patterns

| Pattern           | Description                                                                                            | Example |
|-------------------|--------------------------------------------------------------------------------------------------------|---------|
| **Source-based**  | Run a starter command (e.g., `npm prepare`) to generate source code, then build and deploy that source | Strapi  |
| **Install-based** | No source code needed — software is installed/built entirely via CLI commands in `zerops.yaml`         | Umami   |

For install-based OSS, you only need `zerops.yaml` with build, prepare, and deploy instructions.

---

## Step-by-Step Process

### 1. Research Existing Recipes

Review similar recipes, both in the GUI and source code. Pay attention to the structure — the key files are:

- `README.md`
- `zerops.yaml`
- `import.yaml`

### 2. Migrate Apps to New Structure

Move all apps from the old recipe format to the new structure
at [zerops-recipe-apps](https://github.com/zerops-recipe-apps):

#### 2.1 Create a New Repository

[Create new repo](https://github.com/organizations/zerops-recipe-apps/repositories/new) with naming convention:
`{runtime}-hello-world-app` (e.g., `bun-hello-world-app`)

> **Important:** Check the "Public template" checkbox in Settings

#### 2.2 Clone and Re-point the Old Repo

```bash
git clone git@github.com:zeropsio/recipe-bun.git
mv recipe-bun bun-hello-world-app
cd bun-hello-world-app
git remote set-url origin git@github.com:zerops-recipe-apps/bun-hello-world-app.git
git push -u origin main
```

#### 2.3 Remove `import.yaml` from App Repo

Delete `import.yaml` from the app repo. The service definitions should be moved to `recipes/{recipe-name}/import.yaml`.

> **Key principle:** Reuse service definitions across environments, but adjust **scaling configuration** based on
> environment type (e.g., minimal resources for stage, higher resources and replicas for HA production).

#### 2.4 Add Extract Fragments to `README.md`

Add the appropriate extract fragments (see [Fragments Reference](#fragments-reference) below).

#### 2.5 Update and Comment `zerops.yaml`

Add detailed comments explaining each configuration section.

### 3. Create Recipe Directory

Copy the appropriate template from https://github.com/zeropsio/recipes:

- `_template` — for languages/frameworks
- `_template_oss` — for open-source projects

Perform find-and-replace on these placeholders:

| Placeholder                      | Example Value                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------|
| `PLACEHOLDER_PROJECT_NAME`       | `go-hello-world`                                                                          |
| `PLACEHOLDER_PRETTY_RECIPE_NAME` | `Go Hello World`                                                                          |
| `PLACEHOLDER_RECIPE_DIRECTORY`   | `go-hello-world`                                                                          |
| `PLACEHOLDER_RECIPE_SOFTWARE`    | `[Go](https://go.dev) applications`                                                       |
| `PLACEHOLDER_RECIPE_DESCRIPTION` | `Simple Go API with single endpoint that reads from and writes to a PostgreSQL database.` |
| `PLACEHOLDER_COVER_SVG`          | `cover-go.svg`                                                                            |
| `PLACEHOLDER_RECIPE_TAGS`        | `golang,echo`                                                                             |
| `PLACEHOLDER_PRETTY_RECIPE_TAGS` | `Go`                                                                                      |

### 4. Create `import.yaml` Files

Create and document `import.yaml` for each environment. Remember to adjust scaling/resources appropriately per
environment.

### 5. Register Recipe in Strapi

[Add the recipe to Strapi](https://api-d89-1337.prg1.zerops.app/admin/content-manager/collection-types/api::recipe.recipe/create)

### 6. Test All Environments

- Dev services have runtime-specific commands available (`go`, `bun`, `cargo`, etc.)
- Verify that apps function as expected
- **Always click "Refresh Cache"** in Strapi after pushing changes during development

---

## Expected Output

### In Strapi

- Recipe entry with logo and correct categories

### In the [recipes repo](https://github.com/zeropsio/recipes)

A folder containing environment subdirectories based on template type:

**For `_template` (languages/frameworks):**

- `agent`, `remote`, `local`, `stage`, `small-production`, `highly-available-production`

**For `_template_oss` (OSS projects):**

- `development`, `production`

**Each environment contains:**

- Documented `import.yaml` (with environment-appropriate scaling)
- `README.md` with environment description in `intro` fragment

**Main `README.md`** includes recipe description in `intro` fragment

### In [zerops-recipe-apps](https://github.com/zerops-recipe-apps)

Repository for each related app (e.g., https://github.com/zerops-recipe-apps/bun-hello-world-app):

- Documented `zerops.yaml`
- Updated `README.md` with extract fragments
- Meaningful README when visiting the GitHub repo directly

---

## Fragments Reference

The recipe system only processes marked sections of `README.md` files, called **fragments**.

### Fragment Syntax

```markdown
Lorem Ipsum ...

<!-- #ZEROPS_EXTRACT_START:intro# -->
**AI agent** environment provides a development space for AI agents to build and version the app.
Comes with a dev service with the source code and necessary development tools, a staging service,
email & SMTP testing tool, and low-resource databases and storage.
<!-- #ZEROPS_EXTRACT_END:intro# -->

... Lorem Ipsum
```

Content between `ZEROPS_EXTRACT_START` and `ZEROPS_EXTRACT_END` tags with a given key (e.g., `intro`) is extracted and
available in the recipe system.

### Supported Fragment Keys

| Key                 | Description                                                                                   | README Location                       |
|---------------------|-----------------------------------------------------------------------------------------------|---------------------------------------|
| `intro`             | Introduction/description of the entity based on which README contains it                      | app, recipe, recipe environment       |
| `knowledge-base`    | Useful information specific to the software, framework, language, or recipe as a whole        | anywhere                              |
| `integration-guide` | Instructions for adapting an application to run on Zerops, including documented `zerops.yaml` | app (for frameworks)                  |
| `maintenance-guide` | Operations and maintenance guides for the app or entire recipe on Zerops                      | app (for OSS), OSS recipe environment |

---

## Important Notes

### YAML Documentation Purpose

Documenting YAML files serves two purposes:

1. **User education** — explaining configuration to users
2. **LLM training** — more importantly, providing context for future AI/LLM instruction

**Best practice:** Add implementation notes as comments. Any non-obvious YAML section should include a description of
*why* it exists and *how* it works.

---

## Open Questions

- **Cache duration** — How long does the GitHub cache last before auto-refresh? (For now: always manually refresh during
  development)