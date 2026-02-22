# Repository Overview

Azure SRE Agent の設定サンプルやリソースをまとめたリポジトリ。

## Directory Structure

```text
awesome-azure-sre-agent/
├── docs/                # Docs
│   ├── scenarios/       # 活用シナリオ集
│   └── tips/            # その他 TIPS
├── resources/
│   ├── subagents/           # Subagent 設定サンプル
│   │   └── {name}/
│   │       ├── README.md
│   │       └── {name}.yaml
│   ├── skills/              # Skill 定義サンプル
│   │   └── {name}/
│   │       ├── README.md
│   │       └── {name}.yaml
│   ├── connectors/          # Connector 設定サンプル
│   │   └── {name}/
│   │       ├── README.md
│   │       └── connector.yaml
│   └── tools/               # Python スクリプト・KQL クエリ
│       ├── python/
│       │   └── *.py
│       └── kql/
│           └── *.kql
└── README.md                # リンク集や全体説明
```

**重要な分離原則**: `docs/` は人間が読む記事・解説 / `resources/` 配下（`subagents/`, `skills/`, `connectors/`, `tools/`）は実際に使えるリソースファイル。

## Conventions

### ドキュメント記事 (`docs/`)

- 言語は日本語ベース（公式リンクや技術用語は英語を併記しても良い）
- 1 記事 = 1 シナリオ・TIPS
- 目的・前提条件・手順・ポイントを明確に記載
- 可能な限りスクリーンショットやコード例を活用

### Subagent リソース (`resources/subagents/`)

- 1 ディレクトリ = 1 subagent
- `README.md` に目的・前提条件・使い方を記載

### Skill リソース (`resources/skills/`)

- 1 directory = 1 skill
- `README.md` に目的・前提条件・使い方を記載

### Connector リソース (`resources/connectors/`)

- 1 ディレクトリ = 1 connector
- 機密情報（API キー等）は絶対にコミットしない。プレースホルダー `<YOUR_API_KEY>` を使用

### Tools (`resources/tools/`)

- `python/`: 単体で実行可能なスクリプト。ファイル冒頭に用途・引数・前提パッケージをコメントで記載
- `kql/`: クエリファイル。冒頭コメントにクエリの目的・対象テーブルを記載
