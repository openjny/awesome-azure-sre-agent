# Contributing Guide

このリポジトリへの貢献を歓迎します。  
貢献の種類や手順を以下にまとめています。

## 貢献できること

| 種類 | 内容 |
|------|------|
| **リンク追記** | README の各セクションへの公式ドキュメント・ブログ・事例リンクの追加 |
| **ドキュメント記事** | `docs/` 配下へのシナリオ解説・TIPS の追加 |
| **リソース定義** | `resources/` 配下への Subagent / Skill / Connector / Tool サンプルの追加 |
| **誤記・リンク切れ修正** | 既存コンテンツの修正 |

## ディレクトリ構成

```text
awesome-azure-sre-agent/
├── docs/
│   └── <title>.md       # README にフィットしないが有用な TIP など
├── resources/
│   ├── subagents/       # Subagent 設定サンプル
│   ├── skills/          # Skill 定義サンプル
│   ├── connectors/      # Connector 設定サンプル
│   └── tools/
│       ├── python/      # Python スクリプト
│       └── kql/         # KQL クエリ
└── README.md
```

**重要**: `docs/` は人間が読む記事・解説、`resources/` は実際に使えるリソースファイルです。混在させないでください。

## Pull Request の手順

1. このリポジトリを Fork する
2. ブランチを切る（例: `feature/add-incident-response-scenario`）
3. 変更を加えてコミットする
4. Pull Request を作成する

## コンテンツごとの規約

### README へのリンク追記

- 適切なセクションに追記する
- 形式: `**[タイトル](URL)**` の後に 1〜2 行の日本語説明
- 重複リンクがないか確認する

### ドキュメント記事 (`docs/`)

- 言語は日本語ベース（技術用語・固有名詞は英語を併記可）
- 1 ファイル = 1 シナリオ・TIPS
- ファイル名: kebab-case（例: `ssl-certificate-monitor.md`）
- 記事には以下を含める:
  - 目的・ユースケース
  - 前提条件
  - 手順
  - ポイント・注意事項

### Subagent / Skill / Connector (`resources/`)

- 1 ディレクトリ = 1 リソース
- 各ディレクトリに `README.md` を必ず含める（目的・前提条件・使い方）
- ファイル構成:
  - Subagent: `{name}/README.md`, `{name}/{name}.yaml`
  - Skill: `{name}/README.md`, `{name}/{name}.yaml`
  - Connector: `{name}/README.md`, `{name}/connector.yaml`
- **機密情報（API キー・パスワード等）は絶対にコミットしない**。プレースホルダー `<YOUR_API_KEY>` を使用する

### Tools (`resources/tools/`)

- **Python スクリプト** (`python/*.py`):
  - 単体で実行可能な形式にする
  - ファイル冒頭のコメントに用途・引数・前提パッケージを記載する
- **KQL クエリ** (`kql/*.kql`):
  - ファイル冒頭のコメントにクエリの目的・対象テーブルを記載する

## セキュリティに関する注意

- シークレット・認証情報・個人情報をコミットしない
- サブスクリプション ID・テナント ID などの固有情報はプレースホルダーに置き換える
- セキュリティの脆弱性を発見した場合は Issue ではなく、リポジトリオーナーに直接連絡する

## ライセンス

このリポジトリは [MIT License](LICENSE) のもとで公開されています。貢献いただいたコンテンツも同ライセンスが適用されます。
