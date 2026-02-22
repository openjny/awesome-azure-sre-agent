# Contributing Guide

Contributions to this repository are welcome.  
Below is a summary of contribution types and procedures.

## What You Can Contribute

| Type | Description |
|------|-------------|
| **Add links** | Add official documentation, blog, or case study links to README sections |
| **Documentation articles** | Add scenario explanations or tips under `docs/` |
| **Resource definitions** | Add Subagent / Skill / Connector / Tool samples under `resources/` |
| **Fix typos or broken links** | Fix issues in existing content |

## Directory Structure

```text
awesome-azure-sre-agent/
├── docs/
│   └── <title>.md       # Useful tips that don't fit directly in README
├── resources/
│   ├── subagents/       # Subagent configuration samples
│   ├── skills/          # Skill definition samples
│   ├── connectors/      # Connector configuration samples
│   └── tools/
│       ├── python/      # Python scripts
│       └── kql/         # KQL queries
└── README.md
```

**Important**: `docs/` is for human-readable articles and explanations. `resources/` is for actual usable resource files. Do not mix them.

## Pull Request Steps

1. Fork this repository
2. Create a branch (e.g., `feature/add-incident-response-scenario`)
3. Make your changes and commit
4. Open a Pull Request

## Content Conventions

### README language policy

- `README.md`: **English-audience content only.** Add a link or article here only if it is primarily written for English-speaking or global audiences. Simply translating a description does not make locale-specific content eligible for `README.md`.
- `README.<locale>.md`: **Locale-audience content.** Add content written for that locale's audience here. Items shared with `README.md` (global content) are also listed here in bilingual form (English + locale language).

When adding new content, always check the **intended audience language** of the source material first, then decide which README(s) it belongs in:

| Source material language | Add to `README.md` | Add to `README.<locale>.md` |
|---|---|---|
| English / global | Yes | Yes (bilingual) |
| Locale-specific only | No | Yes |

### Adding links to README

- Add to the appropriate section
- Format for `README.md`: `**[Title](URL)**` followed by 1–2 lines of **English** description
- Format for `README.<locale>.md`: follow the English description with the locale language description on the next line (bilingual)
- Check for duplicate links before adding

### Documentation articles (`docs/`)

- Language: English-based (Japanese may be used alongside for locale-specific content)
- 1 file = 1 scenario or tip
- File name: kebab-case (e.g., `ssl-certificate-monitor.md`)
- Articles should include:
  - Purpose and use case
  - Prerequisites
  - Steps
  - Key points and notes

### Subagent / Skill / Connector (`resources/`)

- 1 directory = 1 resource
- Each directory must include a `README.md` (purpose, prerequisites, and usage)
- File structure:
  - Subagent: `{name}/README.md`, `{name}/{name}.yaml`
  - Skill: `{name}/README.md`, `{name}/{name}.yaml`
  - Connector: `{name}/README.md`, `{name}/connector.yaml`
- **Never commit sensitive information (API keys, passwords, etc.)**. Use the placeholder `<YOUR_API_KEY>`

### Tools (`resources/tools/`)

- **Python scripts** (`python/*.py`):
  - Must be standalone executable
  - Include a comment block at the top with purpose, arguments, and required packages
- **KQL queries** (`kql/*.kql`):
  - Include a comment at the top with the query's purpose and target table

## Security Notes

- Do not commit secrets, credentials, or personal information
- Replace environment-specific values such as subscription IDs and tenant IDs with placeholders
- If you discover a security vulnerability, contact the repository owner directly rather than opening an Issue

## License

This repository is published under the [MIT License](LICENSE). Contributed content is subject to the same license.
