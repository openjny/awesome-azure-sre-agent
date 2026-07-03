---
description: "Weekly discovery of new Azure SRE Agent content to add to the list"
on:
  schedule:
    # Every Monday at 01:00 UTC
    - cron: "0 1 * * 1"
  workflow_dispatch:
permissions:
  contents: write
  pull-requests: write
engine: copilot
# Content discovery must search and fetch across arbitrary sites, so a fixed
# allowlist is impractical. This workflow only reads public web pages, so the
# agent firewall is disabled.
features:
  dangerously-disable-sandbox-agent: "Content-discovery agent must search/fetch arbitrary public web pages; no secrets are exposed."
sandbox:
  agent: false
tools:
  bash: [":*"]
  web-fetch:
  web-search:
safe-outputs:
  create-pull-request:
    title-prefix: "[new-content] "
    labels: [automation, content-discovery]
    draft: false
---

# Azure SRE Agent New Content Discovery

This repository is a curated list of Azure SRE Agent resources. Your job is to find recently
published **official or high-quality** Azure SRE Agent content that is **not yet listed** and
propose it for inclusion.

## Steps

1. Read `README.md` and `README.ja.md` and build the set of URLs already listed. Anything
   already present must be ignored.
2. Look for new Azure SRE Agent content from authoritative sources, such as:
   - Microsoft Tech Community, tag "Azure SRE Agent"
     (`https://techcommunity.microsoft.com/tag/azure%20sre%20agent`)
   - The aggregated blog index (`https://aka.ms/sreagent/blog`)
   - The official YouTube channel (`https://aka.ms/sreagent/youtube`)
   - Microsoft Learn / Build session catalog pages for Azure SRE Agent
   Use `web-search` and `web-fetch` to gather candidates. Prefer items published in roughly
   the last 2–3 months.
3. For each candidate, capture: the title, the canonical URL, the publish date (if known),
   and a one-sentence English summary.
4. Discard any candidate whose URL (or an obvious equivalent/redirect) already appears in the
   READMEs.

## Categorization

For each new item, suggest which README section it fits best, using the existing sections:
Official Links, Use Case Scenarios, MCP Integration Guide, Demo Videos, Lab Environments,
Case Studies, or Other Resources. Also state, per the repository's audience-language policy,
whether it is **global content** (goes in both `README.md` and `README.ja.md`) or
**Japanese-audience content** (goes in `README.ja.md` only).

## Output

- If no new items are found, do **not** create a pull request. Log that the list is up to date.
- Otherwise, add the new candidates to the appropriate sections of the README files according
  to the audience-language policy (global content → both `README.md` and `README.ja.md`;
  Japanese-only content → `README.ja.md` only), then create a pull request with the changes.
  The PR title should be `Add new Azure SRE Agent content`. In the PR body, list the
  candidates grouped by suggested section. For each candidate include the title (as a
  Markdown link), the publish date, the one-sentence summary, and the README placement
  (global vs. Japanese-only), so a maintainer can review before merging.
