---
description: "Weekly broken-link checker for the README files"
on:
  schedule:
    # Every Monday at 00:00 UTC
    - cron: "0 0 * * 1"
  workflow_dispatch:
permissions:
  contents: write
  pull-requests: write
engine: copilot
# A curated link list can reference any domain and grows over time, so a fixed
# network allowlist would falsely flag links to new domains as broken. This
# workflow only performs outbound HTTP checks, so the agent firewall is disabled
# to allow reaching arbitrary URLs.
features:
  dangerously-disable-sandbox-agent: "Link checker must reach arbitrary curated URLs to verify them; no secrets are exposed."
sandbox:
  agent: false
tools:
  bash: [":*"]
safe-outputs:
  create-pull-request:
    title-prefix: "[link-check] "
    labels: [automation, link-check]
    draft: false
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

- If **no** broken links are found, do **not** create a pull request. Simply finish and log
  that all links are healthy.
- If one or more broken links are found, remove the broken Markdown link entries from the
  affected README files and create a pull request with those removals. The PR title should be
  `Remove broken links detected in README`. In the PR body, include a Markdown table with
  these columns:
  - `URL` — the broken link removed
  - `Status` — the HTTP status code or error (e.g. `404`, `timeout`, `DNS error`)
  - `File(s)` — which README file(s) the link was removed from (`README.md`, `README.ja.md`,
    or both)
