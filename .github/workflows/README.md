# GitHub Agentic Workflows (gh-aw)

This directory contains [GitHub Agentic Workflows](https://github.github.com/gh-aw/) that
automate maintenance of this curated list. Each `.md` file is a natural-language workflow
that an AI coding agent runs inside GitHub Actions with guardrails (read-only token,
sandboxing, and gated "safe outputs" — so the agent can only open issues/comments, never
push directly).

## Workflows

| File | Trigger | What it does |
|------|---------|--------------|
| [`link-checker.md`](link-checker.md) | Weekly (Mon 00:00 UTC) + manual | Checks every URL in `README.md` and `README.ja.md` and opens an issue listing any broken links. |
| [`readme-bilingual-sync.md`](readme-bilingual-sync.md) | Pull requests touching a README + manual | Verifies `README.md` (global content) and `README.ja.md` stay in sync per the audience-language policy, and comments on the PR (or opens an issue) when they drift. |
| [`new-content-discovery.md`](new-content-discovery.md) | Weekly (Mon 01:00 UTC) + manual | Discovers new official Azure SRE Agent content not yet listed and opens an issue with add candidates and suggested sections. |

## Prerequisites

These Markdown workflows are compiled into runnable `.lock.yml` GitHub Actions files by the
[`gh aw` CLI extension](https://github.github.com/gh-aw/):

```sh
gh extension install github/gh-aw
gh aw compile        # generates the .lock.yml files committed alongside each workflow
```

The agent engine is `copilot` (GitHub Copilot). Make sure the repository has access to the
[GitHub Copilot coding agent](https://github.github.com/gh-aw/reference/engines/) and any
required secrets before enabling scheduled runs. You can trigger any workflow on demand from
the Actions tab (each defines `workflow_dispatch`).

## Notes

- All three workflows are **read-only**: they only produce issues or PR comments via
  `safe-outputs` and never edit files or push commits.
- `link-checker.md` and `new-content-discovery.md` declare a `network:` allowlist of the
  domains currently referenced in the READMEs. If links to new domains are added, extend the
  allowlist so the agent can reach them.
