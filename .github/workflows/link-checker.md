---
description: "Weekly broken-link checker for the README files"
on:
  schedule:
    # Every Monday at 00:00 UTC
    - cron: "0 0 * * 1"
  workflow_dispatch:
permissions:
  contents: read
engine: copilot
network:
  allowed:
    - defaults
    - "techcommunity.microsoft.com"
    - "learn.microsoft.com"
    - "build.microsoft.com"
    - "sre.azure.com"
    - "mcp.azure.com"
    - "www.azure.com"
    - "aka.ms"
    - "github.com"
    - "*.github.com"
    - "www.youtube.com"
    - "youtu.be"
    - "x.com"
    - "zenn.dev"
    - "speakerdeck.com"
tools:
  bash: ["curl", "grep", "sort", "uniq", "cat"]
safe-outputs:
  create-issue:
    title-prefix: "[link-check] "
    labels: [automation, link-check]
    close-older-issues: true
---

# README Broken Link Checker

You maintain a curated "awesome list" repository for Azure SRE Agent. Your job is to
find broken links in the two top-level README files.

## Steps

1. Read `README.md` and `README.ja.md` from the repository root.
2. Extract every HTTP(S) URL referenced in Markdown links (`[text](url)`) in both files.
   Deduplicate the list so each unique URL is checked only once.
3. For each unique URL, send an HTTP request (prefer `curl -sSIL --max-time 20`, following
   redirects) and record the final status code.
4. Treat a link as **broken** when the **final** status (after following redirects) is `4xx`
   or `5xx`, when the request times out, when a redirect chain loops or exceeds curl's default
   redirect limit, or when the host cannot be resolved. A redirect that ultimately lands on a
   `2xx` is healthy; a redirect that ultimately lands on a `4xx`/`5xx` is broken. Some hosts
   block automated `HEAD` requests — if a `HEAD` fails, retry
   once with `curl -sSL -o /dev/null -w "%{http_code}" --max-time 20` (a `GET`) before
   concluding the link is broken, to avoid false positives.

## Output

- If **no** broken links are found, do **not** create an issue. Simply finish and log that
  all links are healthy.
- If one or more broken links are found, create a single GitHub issue titled
  `Broken links detected in README` summarizing the findings. In the body, include a
  Markdown table with these columns:
  - `URL` — the broken link
  - `Status` — the HTTP status code or error (e.g. `404`, `timeout`, `DNS error`)
  - `File(s)` — which README file(s) reference it (`README.md`, `README.ja.md`, or both)

  Keep the report factual. Do not attempt to fix the links or edit any files.
