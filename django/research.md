# Django — Zerops Recipe Research

## Overview

- **Software:** Django 5.2.17 on Python 3.12
- **Type:** language-example
- **Zerops Runtime:** `python@3.12`, `postgresql@17`, optional Mailpit / php-apache sidecars

## Repo

- App repo: `https://github.com/zerops-recipe-apps/django-app`

## Environment (vault)

Import uses `project.vault` / `service.vault` as the value store (not `envVariables` / `envSecrets` on services). Map keys explicitly in each app `zerops.yaml` — do not rely on auto-injection. Avoid self-references (e.g. `KEY: ${KEY}`).
