# Awesome Azure SRE Agent

> 🌐 [English version (英語版)](README.md)

このリポジトリは、Azure SRE Agent に関する公式ドキュメント、活用シナリオ、デモ動画、事例、リソース定義などをまとめています。Azure SRE Agent を導入・活用する際の参考資料としてご活用ください。

**目次**

- [🔗 公式リンク集](#-公式リンク集)
- [🚀 活用シナリオ](#-活用シナリオ)
- [🔌 MCP 連携ガイド](#-mcp-連携ガイド)
- [🎬 デモ動画](#-デモ動画)
- [🧪 ラボ環境](#-ラボ環境)
- [📣 事例](#-事例)
- [📚 その他](#-その他)
- [🛠️ リソース定義](#️-リソース定義)

## 🔗 公式リンク集

- ⭐ **[Azure SRE Agent Overview](https://learn.microsoft.com/azure/sre-agent/overview)**  
  公式ドキュメント
- ⭐ **[Azure SRE Agent tag - Microsoft Tech Community](https://techcommunity.microsoft.com/tag/azure%20sre%20agent)**  
  公式ブログ記事・コミュニティ投稿のまとめ
- ⭐ **[microsoft/sre-agent](https://github.com/microsoft/sre-agent)**  
  バグ報告・フィードバック用リポジトリ。公式リソースへのリンク集や、公式ハンズオンラボ ([`labs/`](https://github.com/microsoft/sre-agent/tree/main/labs))・レシピ集 ([`sreagent-templates/recipes/`](https://github.com/microsoft/sre-agent/tree/main/sreagent-templates/recipes)) を提供
- ⭐ **[Azure/sre-agent-plugins](https://github.com/Azure/sre-agent-plugins)**  
  Plugin Marketplace 経由でスキル・MCP ツール・オペレーションワークフローを配布するための公式プラグインリポジトリ
- **[Azure SRE Agent Product Home Page](https://www.azure.com/sreagent)**  
  製品公式サイト
- **[Azure SRE Agent Portal Documentation](https://sre.azure.com/docs/overview)**  
  ポータル上の操作ガイド
- **[Azure SRE Agent Pricing & Billing](https://aka.ms/sreagent/pricing)**  
  料金体系・Active Flow / Always-On の AAU モデルと FAQ
- **[Azure SRE Agent Blogs (aggregated)](https://aka.ms/sreagent/blog)**  
  公式ブログ記事の集約インデックス
- **[Azure SRE Agent YouTube Channel](https://aka.ms/sreagent/youtube)**  
  デモ・チュートリアル・ディープダイブを公開する公式 YouTube チャンネル
- **[Azure SRE Agent on X (Twitter)](https://x.com/azuresreagent)**  
  公式 X (Twitter) アカウント
- **[Agentic DevOps Live](https://aka.ms/agenticdevopslive)**  
  Azure SRE Agent を含むエージェンティック DevOps シナリオを扱うライブ配信シリーズ
- **[Request a new Azure SRE Agent region](https://aka.ms/sreagent/region)**  
  提供リージョン拡張のリクエストフォーム
- **[Azure MCP Center - Microsoft](https://mcp.azure.com/?vendors.microsoft=true)**  
  Microsoft 提供の MCP サーバー

## 🚀 活用シナリオ

**Scheduled Task**

- **[Azure WAF Compliance with MCP-Driven SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-waf-compliance-with-mcp-driven-sre-agent/4494687)**  
  Well-Architected Framework (WAF) の 5 本柱 + 組織固有のベストプラクティスに基いて、リソースのコンプライアンス評価と修復コマンドの提示を定期実行
- **[Build a Custom SSL Certificate Monitor with Azure SRE Agent: From Python Tool to Production Skill](https://techcommunity.microsoft.com/blog/appsonazureblog/build-a-custom-ssl-certificate-monitor-with-azure-sre-agent-from-python-tool-to-/4495832)**  
  SSL 証明書の有効期限を監視する Python ツールを作成し、定期的にヘルスチェック
- **[Event-Driven IaC Operations with Azure SRE Agent: Terraform Drift Detection via HTTP Triggers](https://techcommunity.microsoft.com/blog/appsonazureblog/event-driven-iac-operations-with-azure-sre-agent-terraform-drift-detection-via-h/4512233)**  
  Terraform Cloud の webhook をトリガーに、SRE Agent が drift を benign / risky / critical に分類し、インシデントと相関を取って修復まで実行するエンドツーエンドのパイプライン。"DO NOT revert" 判定で mitigated なインシデントの再発化を防ぐ
- 🇯🇵 **[Azure SRE Agent で定型業務を自動化する: インシデント対応だけじゃない活用法（Zenn / Microsoft 有志）](https://zenn.dev/microsoft/articles/66ae4396f95646)**  
  Service Health のリタイアメントや障害情報を定期的にチェックして、影響リソースの特定や回避策の提示を行うシナリオを紹介

**Incident Response**

- **[Azure Monitor in Azure SRE Agent: Autonomous Alert Investigation and Intelligent Merging](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-monitor-in-azure-sre-agent-autonomous-alert-investigation-and-intelligent-/4509069)**  
  Azure Monitor 連携の詳細解説。Incident Response Plans、アラートマージ（7 firings → 1 thread）、auto-resolve のトレードオフ、AKS + Redis で不正な資格情報を自律修復する実例を紹介
- 🇯🇵 **[Azure SRE Agent が利用可能に！ 仮想マシンを調査してもらった（Zenn / Microsoft 有志）](https://zenn.dev/microsoft/articles/sreagent-getstart)**  
  VM の CPU 高負荷シナリオで SRE Agent を試した入門レポート。作成手順・調査フロー・権限設定・日本語対応などを実演を交えて紹介

## 🔌 MCP 連携ガイド

- **[How to Connect Azure SRE Agent to Azure MCP](https://techcommunity.microsoft.com/blog/appsonazureblog/how-to-connect-azure-sre-agent-to-azure-mcp/4488905)**  
  Azure MCP サーバーを使用して、ネイティブの az コマンドとは異なる方法で Azure リソースを操作する
- **[Get started with Dynatrace MCP server in Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-dynatrace-mcp-server-in-azure-sre-agent/4492363)**  
  Dynatrace MCP サーバーを使用して、Dynatrace の機能（DQL クエリ、問題調査、セキュリティ脆弱性分析、時系列予測など）を SRE Agent から実行する
- **[Get started with Elasticsearch MCP server in Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-elasticsearch-mcp-server-in-azure-sre-agent/4492896)**  
  Elasticsearch の Agent Builder MCP エンドポイントを使い、自然言語でログ検索・ES|QL 実行・クラスターヘルス確認を行う Subagent を構築する
- **[MCP-Driven Azure SRE for Databricks](https://techcommunity.microsoft.com/blog/appsonazureblog/mcp-driven-azure-sre-for-databricks/4494630)**  
  Databricks MCP サーバーを Azure Container Apps にデプロイし、ワークスペースのベストプラクティス準拠を自動検証（Scheduled Task）したり、ジョブ障害の根本原因を自律調査・修復（Incident Response）する
- **[Get started with Atlassian Rovo MCP server in Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-atlassian-rovo-mcp-server-in-azure-sre-agent/4497122)**  
  公式 Atlassian Rovo MCP サーバーを使用して、Jira・Confluence・Compass・Jira Service Management に Azure SRE Agent から接続する
- **[Get started with Datadog MCP server in Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-datadog-mcp-server-in-azure-sre-agent/4497123)**  
  公式 Datadog MCP サーバーを使用して、ログ・メトリクス・APM トレース・モニター・インシデント・ダッシュボードなど Datadog のデータを SRE Agent から操作する
- **[Get started with PagerDuty MCP server in Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-pagerduty-mcp-server-in-azure-sre-agent/4497124)**  
  公式 PagerDuty MCP サーバーを使用して、インシデント・オンコールスケジュール・サービス・エスカレーションポリシーなどを Azure SRE Agent から操作する
- **[New in Azure SRE Agent: Log Analytics and Application Insights Connectors](https://techcommunity.microsoft.com/blog/appsonazureblog/new-in-azure-sre-agent-log-analytics-and-application-insights-connectors/4509649)**  
  Azure MCP Server (`monitor` ネームスペース) を裏側で使うネイティブコネクタ。Log Analytics ワークスペースおよび Application Insights リソースに対して調査中に KQL クエリを直接実行でき、RBAC の付与も自動化される

## 🎬 デモ動画

- **[Azure SRE Agent: End to End Agentic Operations Platform for Any Kind of Toil at Enterprise Scale](https://www.youtube.com/watch?v=06j-d0gsREw)**  
  Azure SRE Agent をエンタープライズ規模のエンドツーエンドなエージェンティック運用プラットフォームとして俯瞰する動画
- **[What is Azure SRE Agent — Official Overview](https://www.youtube.com/watch?v=6vDrThUjDOc)**  
  Microsoft Azure 公式のプロダクト概要動画。Azure SRE Agent とは何か、どう動くのか、どんな課題を解くのかを簡潔に解説
- **[Microsoft AI SRE Agent: Fixing Bugs While You Sleep](https://www.youtube.com/watch?v=3hPeKDtLvPg)**  
  Satya Nadella が Azure SRE Agent を AI 主導の運用変革の代表例として紹介
- **[Azure SRE Agent: Less Toil, More Uptime, Maximum Innovation — Azure Friday](https://www.youtube.com/watch?v=5c9pl8_DI3w)**  
  Azure Friday にて Scott Hanselman が Azure SRE Agent を紹介。運用トイルを削減し、チームがイノベーションに集中できるようになる様子をデモ
- **[Root Cause Analysis with Code Context: Azure SRE Agent + GitHub Integration — GA Launch](https://www.youtube.com/watch?v=1vKoxPeep_M)**  
  GA ローンチデモ。深い GitHub 統合によりコードコンテキスト付きで根本原因分析を行う様子を紹介
- **[Azure SRE Agent - Incident Management with PagerDuty](https://www.youtube.com/watch?v=5wrArcKzUaI)**  
  Azure SRE Agent 公式チャンネルによる PagerDuty 連携のエンドツーエンドデモ
- **[Use Azure SRE Agent to automate tasks and increase site reliability (Microsoft Build 2025 / DEM550)](https://build.microsoft.com/en-US/sessions/DEM550)**  
  Microsoft Build 2025 のデモセッション。自然言語でインテントを記述するだけで SRE Agent が一連のタスクを実行する仕組みを、e コマースサイトの障害対応シナリオを交えて紹介
- **[Using autonomous SRE to move from alerts to action (Microsoft Build 2026 / OD800)](https://build.microsoft.com/en-US/sessions/OD800)**  
  Microsoft Build 2026 セッション。VNet 統合・権限モデル・Managed Connectors などのエンタープライズ制御を活用した「アラートからアクションへ」の自律オペレーションを解説
- **[Proactive .NET Reliability with Azure SRE Agent](https://www.youtube.com/watch?v=Kx_6SB-mhgg)**  
  ASP.NET アプリを題材に、インシデント報告前に問題を検知・修復するプロアクティブな信頼性向上の方法をデモで解説

## 🧪 ラボ環境

- ⭐ **[microsoft/sre-agent — `labs/`](https://github.com/microsoft/sre-agent/tree/main/labs)**  
  Azure SRE Agent 公式のハンズオンラボ／サンプル環境。アプリのデプロイ・障害の再現・修復までを一通り試せる (`aka.ms/sreagent/lab`)
- 🇯🇵 **[azure-sre-agent-demokit (ussvgr/GitHub)](https://github.com/ussvgr/azure-sre-agent-demokit)**  
  Azure SRE Agent デモ環境を Terraform で一括プロビジョニングするキット。.NET Blazor デモアプリ・Application Insights アラート・SRE Agent リソースをまとめて作成できる
- 🇯🇵 **[azure-sre-agent-demo (kohei3110/GitHub)](https://github.com/kohei3110/azure-sre-agent-demo)**  
  Python API + React フロントエンド + Cosmos DB を Container Apps にデプロイするデモ環境。Terraform による CI/CD パイプラインも備える
- **[azure-sre-agent-demo (jiratouchmhp/GitHub)](https://github.com/jiratouchmhp/azure-sre-agent-demo)**  
  マルチ層アプリ（React + .NET 8 + PostgreSQL）を使ったハンズオンデモ環境。セキュリティ・コスト・可用性の欠陽を意図的に仅込み、ライブインシデントのトリガースクリプト付き
- **[azure-sre-agent-sandbox (matthansen0/GitHub)](https://github.com/matthansen0/azure-sre-agent-sandbox)**  
  AKS ベースのデモラボ。OOMKilled・CrashLoop・NetworkBlock など 10 種の壊せるシナリオとフルオブザーバビリティスタックを備えた自動化済み環境
- **[azure-sre-agent (pelithne/GitHub)](https://github.com/pelithne/azure-sre-agent)**  
  AKS クラスタでエラー・負荷テストをシミュレートするツール集。設定可能なメモリリーク Python アプリと nginx デプロイメントを含む


## 📣 事例

- **[How We Build and Use Azure SRE Agent with Agentic Workflows](https://techcommunity.microsoft.com/blog/appsonazureblog/how-we-build-and-use-azure-sre-agent-with-agentic-workflows/4508753)**  
  Customer Zero レポート。Microsoft 社内で SDLC 全体にエージェントを組み込んで SRE Agent を開発した事例。35,000 件超のインシデント処理、50,000 時間超の開発者時間削減、App Service の Time-to-Mitigation を 40.5 時間から 3 分に短縮
- 🇯🇵 **[Azure SRE Agent x PagerDutyによる近未来インシデント対応への期待（イオンスマートテクノロジー / AEON TECH HUB #23）](https://speakerdeck.com/aeonpeople/the-future-of-incident-response-azure-sre-agent-x-pagerduty)**  
  PagerDuty と Azure SRE Agent を連携し、インシデント検知から自律調査・復旧までを自動化するシナリオの実践報告

## 📚 その他

- **[Announcing General Availability for the Azure SRE Agent](https://aka.ms/sreagent/gablog)**  
  Azure SRE Agent 一般提供 (GA / 2026 年 3 月) の公式アナウンス。GA 時点で提供される機能・統合・ガバナンスモデルをまとめて紹介
- **[Context Engineering Lessons from Building Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200/)**  
  SRE Agent 開発チームが実地で得たコンテキストエンジニアリングの教訓（ツール設計・マルチエージェント・コード実行・コンパクション）を解説
- **[Reactive Incident Response with Azure SRE Agent: From Alert to Resolution in Minutes](https://techcommunity.microsoft.com/blog/azurearchitectureblog/reactive-incident-response-with-azure-sre-agent-from-alert-to-resolution-in-minu/4492938)**  
  SQL 接続障害・VM CPU スパイクの 2 シナリオで、アラート発火から自律調査・承認ベース修復・復旧確認までのフルフローをデモ。カスタム IRP 手順の書き方やセットアップ方法も解説
- **[Azure SRE Agent Architecture and Creation: Practical Benefits for SAP on Azure Customers](https://techcommunity.microsoft.com/blog/microsoftmissioncriticalblog/azure-sre-agent-architecture-and-creation-practical-benefits-for-sap-on-azure-cu/4497625)**  
  SRE Agent のアーキテクチャの概要と、自動診断・根本原因分析・ガイド付き修復を通じて SAP on Azure ワークロードに実践的なメリットをもたらす方法を解説
- **[Managing Multi-Tenant Azure Resources with SRE Agent and Lighthouse](https://techcommunity.microsoft.com/blog/appsonazureblog/managing-multi%E2%80%91tenant-azure-resource-with-sre-agent-and-lighthouse/4511789)**  
  Azure Lighthouse による委任を構成することで、単一の SRE Agent から複数テナントのリソースを監視・管理する手順を、ARM テンプレート・RBAC ロール・マネージド ID の設定まで含めて解説
- **[3 Ways to Get More from Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/3-ways-to-get-more-from-azure-sre-agent/4508993)**  
  コストと効果を高める実践 Tips 集。スコープを絞ってインシデントルーティングから始める / 高頻度ポーリングを push・batch に置き換える / スケジュールタスクは実行ごとに新スレッドで開始する
- **[An Update to the Active Flow Billing Model](https://aka.ms/sreagent/pricing/blog)**  
  Active Flow の課金モデルが時間ベースからトークンベースへ移行し、モデルプロバイダごとの AAU レートが適用されるようになった旨のアップデート。Always-on は引き続き 4 AAUs/エージェント時間
- **[Azure SRE Agent at Microsoft Build 2026: Bringing agentic operations to the enterprise](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-sre-agent-at-microsoft-build-2026-bringing-agentic-operations-to-the-enter/4524669)**  
  Microsoft Build 2026 で発表された 5 つのリリース（VNet 統合・Managed Connectors・詳細な権限モデル・GitHub Enterprise ネイティブ対応・Private Plugins Marketplace）をまとめたアンブレラ記事。エンタープライズ規模での本格利用を目指す機能群を紹介
- **[VNet integration for Azure SRE Agent (preview)](https://techcommunity.microsoft.com/blog/appsonazureblog/vnet-integration-for-azure-sre-agent-preview/4524287)**  
  エージェントのアウトバウンド通信を、NSG ルールやプライベート DNS を適用した自組織 VNet の委任サブネット経由に流す機能。3 種類のエグレスモード（Unrestricted / Limited / Azure VNet）とパッケージレジストリ・コードリポジトリ向けのマネージドインフラバイパス経路、構成手順を解説
- **[Managed Connectors for SRE Agent (preview) - Govern what your agent can do](https://techcommunity.microsoft.com/blog/appsonazureblog/managed-connectors-for-sre-agent-preview--govern-what-your-agent-can-do/4524840)**  
  次世代のコネクタ体験。OneDrive・SharePoint・Google Drive・GitLab・Power BI・Microsoft Security Copilot など SaaS カタログを拡充し、公開する操作の選択、パラメータの固定、ツール単位の Allow/Ask 承認、エージェントの信頼境界外での資格情報分離を提供
- **[Shaping what Azure SRE Agent does: Tool Permissions and Hooks](https://techcommunity.microsoft.com/blog/appsonazureblog/shaping-what-azure-sre-agent-does-tool-permissions-and-hooks/4524791)**  
  Global / Agent / Thread スコープごとに allow / ask / deny ルールを設定できるグローバルなツールアクセスポリシーと、ツール呼び出しの実パラメータを見てブロック・書き換え・リダイレクトを行える Command / Prompt Hooks を解説
- **[Bring Your Own GitHub App: Connecting Azure SRE Agent to Enterprise Repositories](https://techcommunity.microsoft.com/blog/appsonazureblog/bring-your-own-github-app-connecting-azure-sre-agent-to-enterprise-repositories/4524673)**  
  GitHub Enterprise Cloud (`*.ghe.com`) および github.com 向けに、独自の GitHub App を持ち込んで認証を行うファーストクラスの方式。秘密鍵は Azure Key Vault に格納し、エージェントのマネージド ID がランタイムに短命のインストールトークンを発行する
- **[Private Plugins with Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/private-plugins-with-azure-sre-agent/4523763)**  
  プラグインマーケットプレイスをプライベート GitHub / GitHub Enterprise リポジトリでホストし、組織で承認したスキル・ランブック・MCP ツールを全 SRE Agent に配布する仕組み。OAuth / PAT / GitHub App 認証とインストール時のバージョン固定に対応
- **[My Journey with Azure SRE Agent](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/my-journey-with-azure-sre-agent/4523519)**  
  Azure SRE Agent を導入して運用トイルの自動化・MTTR 短縮・オブザーバビリティシグナルと意思決定の橋渡しを実現した実践者レポート

## 🛠️ リソース定義

### Subagent

TBD

### Skill

TBD

### Connector

TBD

### Tools

- **[check_ssl_certificate_expiry.py](resources/tools/python/check_ssl_certificate_expiry.py)**  
  指定ドメインの SSL/TLS 証明書の有効期限・発行者・リスクレベルを返す
