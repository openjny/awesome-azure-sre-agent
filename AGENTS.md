# Repository Overview

A collection of configuration samples and resources for Azure SRE Agent.

## Directory Structure

```text
awesome-azure-sre-agent/
├── docs/                    # Docs
├── resources/
│   ├── subagents/           # Subagent configuration samples
│   │   └── {name}/
│   │       ├── README.md
│   │       └── {name}.yaml
│   ├── skills/              # Skill definition samples
│   │   └── {name}/
│   │       ├── README.md
│   │       └── {name}.yaml
│   ├── connectors/          # Connector configuration samples
│   │   └── {name}/
│   │       ├── README.md
│   │       └── {name}.yaml
│   └── tools/               # Python scripts and KQL queries
│       ├── python/
│       │   └── {name}.py
│       └── kql/
│           └── {name}.kql
└── README.md                # Link collection and overview
```

**Key separation principle**: `docs/` is for human-readable articles and explanations. Files under `resources/` (`subagents/`, `skills/`, `connectors/`, `tools/`) are actual usable resource files.

## Conventions

### README

- `README.md`: **English-audience content only.** Add a link or article here only if it is primarily written for English-speaking or global audiences. Translating a description does not make locale-specific content eligible for `README.md`.
- `README.<locale>.md`: **Locale-audience content.** Add content written for that locale's audience here. Items shared with `README.md` (global content) are also listed here in bilingual form (English + locale language).

When adding new content, always check the **intended audience language** of the source material first, then decide which README(s) it belongs in (e.g., Japanese contents -> `README.ja.md`, English contents -> `README.md` and all other locale-specific README files).

### Documentation articles (`docs/`)

- Language: English-based
- 1 article = 1 scenario or tip
- Clearly describe the purpose, prerequisites, steps, and key points
- Use screenshots and code examples whenever possible

### Subagent resources (`resources/subagents/`)

- 1 directory = 1 subagent
- Include a `README.md` describing purpose, prerequisites, and usage

### Skill resources (`resources/skills/`)

- 1 directory = 1 skill
- Include a `README.md` describing purpose, prerequisites, and usage

### Connector resources (`resources/connectors/`)

- 1 directory = 1 connector
- Never commit sensitive information (API keys, etc.). Use the placeholder `<YOUR_API_KEY>`

### Tools (`resources/tools/`)

- `python/`: Standalone executable scripts. Include a comment block at the top of each file with purpose, arguments, and required packages
- `kql/`: Query files. Include a comment at the top with the query's purpose and target table
