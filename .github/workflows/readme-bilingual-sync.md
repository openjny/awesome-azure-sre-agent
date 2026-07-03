---
description: "Check that README.md and README.ja.md stay in sync"
on:
  pull_request:
    paths:
      - "README.md"
      - "README.ja.md"
  workflow_dispatch:
permissions:
  contents: read
engine: copilot
tools:
  bash: [":*"]
safe-outputs:
  add-comment:
  create-issue:
    title-prefix: "[readme-sync] "
    labels: [automation, readme-sync]
    close-older-issues: true
---

# Bilingual README Sync Check

This repository keeps an English README (`README.md`) and a Japanese README
(`README.ja.md`). Your job is to detect when the two drift out of sync according to the
repository's audience-language policy.

## Policy (from `AGENTS.md` / `CONTRIBUTING.md`)

- `README.md`: **English-audience / global content only.** A link belongs here only when the
  source material is primarily written for an English-speaking or global audience.
- `README.<locale>.md` (here `README.ja.md`): **locale-audience content.** It lists
  locale-specific (Japanese) content **and** every global item that is in `README.md`, shown
  in bilingual form (English description + Japanese description).

Concretely this means:

- **Every** link in `README.md` (global content) must also appear in `README.ja.md`.
- Locale-specific links (e.g. Japanese-only articles such as `zenn.dev` / `speakerdeck.com`
  posts) may appear in `README.ja.md` **only** and must **not** be added to `README.md`.

## Steps

1. Read `README.md` and `README.ja.md`.
2. Extract the set of URLs referenced in each file.
3. Compute:
   - **Missing from Japanese**: URLs present in `README.md` but absent from `README.ja.md`.
     These are policy violations — global content must be mirrored into `README.ja.md`.
   - **English-only extras**: URLs in `README.md` that are clearly locale-specific
     (e.g. a Japanese-audience article) and should be moved out of `README.md`.
   - **For awareness only**: URLs present in `README.ja.md` but not in `README.md`. Most of
     these are legitimately locale-specific and are **not** violations — list them separately
     as "review whether any are global content that should also be in README.md".
4. Ignore ordering, wording, and formatting differences. Only reason about which links exist
   in which file.

## Output

- If there are no "Missing from Japanese" and no "English-only extras", do **not** create an
  issue or comment. Log that the READMEs are in sync.
- When the workflow was triggered by a `pull_request` and there are findings, post a single
  concise review **comment** on the pull request describing exactly which links are out of
  sync and what the contributor should do.
- When triggered manually (no PR context) and there are findings, create a single GitHub issue
  titled `README.md and README.ja.md are out of sync` with the same details, grouped under the
  three headings above.

Do not edit any files. Report findings only.
