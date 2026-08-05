# Recipe resource sizing

Guide for `import.yaml` scaling in Zerops recipes. See also
[how-to-write-a-recipe.md](./how-to-write-a-recipe.md) and
[Scaling & HA](https://docs.zerops.io/features/scaling-ha).

---

## Small Production = entry prod (~5 users)

**Small Production is the start tier for real apps** — not Stage, not a separate “Start” env.
Size it for *“I just launched; I have about five users”*: the **lowest resources that are
still honest production**.

| Requirement | Rule |
|-------------|------|
| Postgres | **`oltp-staging`** (≥500 MiB managed) — never `oltp-hobby` on prod-named envs |
| Valkey (full-stack) | **`staging`** profile only |
| App replicas | **`minContainers: 1`** on hello-world HTTP (HA adds replicas) |
| **`verticalAutoscaling`** | **Omit on Small Production** — profiles + platform defaults only |
| Calculator | Small Production price = **default “from” production price** on recipe pages |

**Stage** = rehearsal / QA (`oltp-hobby` OK). **HA** = failover above Small Production; add
`verticalAutoscaling` there only when intentional (e.g. `cpuMode: DEDICATED`, `minDisk: 2`).

App RAM is **per technology** — document expected floors in `{recipe}/research.md` § Scaling.

---

## Database yaml

```yaml
- hostname: db
  type: postgresql:single@18
  profile: oltp-staging
  priority: 10
```

Profile only — **no `verticalAutoscaling`**. Never `minFreeRamGB` on DB.

---

## When to use `verticalAutoscaling`

| Service | Small Production | HA / dev / agent |
|---------|------------------|------------------|
| Postgres / Valkey with `profile` | **Never** | **Never** — profile only |
| App (nodejs / static) | **Omit** — platform defaults | Set **`minFreeRamGB`** + **`minRam`** when teaching or sizing above default |
| NATS / Meilisearch | **Omit** at platform floor | Set only when above default |

**Michal’s app teaching (HA+ tiers):** `minFreeRamGB` is the OOM buffer knob (~10 s peak × 1.2,
125 MiB steps); `minRam` is steady-state baseline. Omit values that match platform defaults.

Omit `maxRam` / `maxContainers` unless documenting a cost ceiling.

---

## Analog Small Production reference (validated)

| Recipe | App | DB / cache | verticalAutoscaling |
|--------|-----|------------|---------------------|
| SSR hello-world | `minContainers: 1` | `oltp-staging` | none |
| Static hello-world | `minContainers: 1` | — | none |
| better-auth / spartan | `minContainers: 1` | `oltp-staging` + `staging` Valkey | none |

---

## Checklist

- [ ] Small prod = ~5 users, `oltp-staging` DB, **no verticalAutoscaling**
- [ ] Profile-only managed services; no DB `minFreeRamGB`
- [ ] README intro matches yaml (refresh Strapi cache after merge)
