---
description: "Weekly discovery of new Azure SRE Agent content to add to the list"
on:
  schedule:
    # Every Monday at 01:00 UTC
    - cron: "0 1 * * 1"
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
    - "aka.ms"
    - "www.youtube.com"
    - "youtu.be"
tools:
  bash: ["cat", "grep"]
  web-fetch:
  web-search:
safe-outputs:
  create-issue:
    title-prefix: "[new-content] "
    labels: [automation, content-discovery]
    close-older-issues: true
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

- If no new items are found, do **not** create an issue. Log that the list is up to date.
- Otherwise create a single GitHub issue titled `New Azure SRE Agent content to review`. In
  the body, list the candidates grouped by suggested section. For each candidate include the
  title (as a Markdown link), the publish date, the one-sentence summary, and the suggested
  README placement (global vs. Japanese-only). Make clear these are suggestions for a
  maintainer to review before adding.

Do not edit the README files yourself. Report candidates only.
