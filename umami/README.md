# Umami Recipe

<!-- #ZEROPS_EXTRACT_START:intro# -->
One-click deployment of [Umami](https://umami.is/) - modern analytics platform that makes it easy to collect, analyze and understand your website data.
<!-- #ZEROPS_EXTRACT_END:intro# -->

⬇️ **Full recipe page and deploy with one-click**

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/light/deploy-button.svg)](https://app.zerops.io/recipes/umami?environment=production)

![cover](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/umami)

Offered in two basic environments:

- **Development** [[info]](/0%20—%20Development) — [[deploy with one click]](https://app.zerops.io/recipes/umami?environment=development)
- **Production** [[info]](/1%20—%20Production) — [[deploy with one click]](https://app.zerops.io/recipes/umami?environment=production)

## Take-over guide

<!-- #ZEROPS_EXTRACT_START:takeover-guide# -->

### Run Umami on your domain
By default the recipe is set up to run on a Zerops preview domain, to run it on your own, do xyz.

### Upgrading Umami
When Umami releases a new version, you can either clone our source repository, modify the version number and setup deployment. If our recipes already includes the version you want to upgrade to, go to pipeline trigger and do xyz

### Backing up / restoring Umami data
Database backups are created daily by default, if you need to restore data, do xyz.

<!-- #ZEROPS_EXTRACT_END:takeover-guide# -->

## Knowledge Base

<!-- #ZEROPS_EXTRACT_START:knowledge-base# -->

### Next.js Standalone Build Artifact

The Umami app is built and deployed in "standalone" mode, see: [output: 'standalone'](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output).
That means the development and maintenance scripts (e.g. `update-tracker`) are not available in the runtime container by default.

To enable this functionality, follow these steps:
1. [SSH into the runtime container](https://docs.zerops.io/references/networking/ssh) or open service web shell in GUI
2. Add some RAM for `pnpm install`:
```shell
zsc scale ram +2GB 10m

# Wait for the scaling to apply.
sleep 10s 
```
3. Install script dependencies:
```shell
pnpm add npm-run-all dotenv chalk semver prisma@6.18.0 @prisma/adapter-pg@6.18.0
```

After that, you should be able to run the maintenance tasks, e.g.:
```shell
pnpm run update-tracker
pnpm run update-db
```

<!-- #ZEROPS_EXTRACT_END:knowledge-base# -->

---

For more advanced examples see all [Analytics recipes](https://app.zerops.io/recipes?lf=analytics,typescript) on Zerops.

Need help setting your project up? Join [Zerops Discord community](https://discord.gg/zeropsio).
