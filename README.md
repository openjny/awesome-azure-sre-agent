# awesome-azure-sre-agent

Azure SRE Agent は、Microsoft が提供する MCP（Microsoft Connected Partner）プラットフォームを活用した、SRE（Site Reliability Engineering）向けの自律型エージェントです。Azure SRE Agent を利用することで、インシデント対応や運用タスクの自動化を実現し、システムの信頼性と運用効率を向上させることができます。

このリポジトリでは、Azure SRE Agent に関する公式ドキュメント、活用シナリオ、デモ動画、事例、リソース定義などをまとめています。Azure SRE Agent を導入・活用する際の参考資料としてご活用ください。

## 公式リンク集

| タイトル | 説明 |
|:---|:--- |
| [Azure SRE Agent 概要](https://learn.microsoft.com/azure/sre-agent/overview)                                   | 公式ドキュメント                              |
| [Azure SRE Agent ポータル ドキュメント](https://sre.azure.com/docs/overview)                                   | ポータル上の操作ガイド                        |
| [Azure MCP Center - Microsoft 製](https://mcp.azure.com/?vendors.microsoft=true)                               | Microsoft 提供の MCP サーバー                 |
| [Azure SRE Agent タグ - Microsoft Tech Community](https://techcommunity.microsoft.com/tag/azure%20sre%20agent) | 公式ブログ記事・コミュニティ投稿のまとめ      |
| [microsoft/sre-agent](https://github.com/microsoft/sre-agent)                                                  | バグ報告・フィードバック・Subagent サンプル集 |

## 活用シナリオ

| タイトル | 説明 |
|:---|:---|
| [Azure WAF Compliance with MCP-Driven SRE Agent (Microsoft Community Hub)](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-waf-compliance-with-mcp-driven-sre-agent/4494687) | WAF の 5 本柱 + 組織固有のベストプラクティスに基づくコンプライアンス評価と修復コマンド生成を自律的に実行 |
| [Reactive Incident Response with Azure SRE Agent: From Alert to Resolution in Minutes (Azure Architecture Blog)](https://techcommunity.microsoft.com/blog/azurearchitectureblog/reactive-incident-response-with-azure-sre-agent-from-alert-to-resolution-in-minu/4492938) | SQL 接続障害・VM CPU スパイクの 2 シナリオで、アラート発火から自律調査・承認ベース修復・復旧確認までのフルフローをデモ。カスタム IRP 手順の書き方やセットアップ方法も解説 |
| [Azure SRE Agent が利用可能に！ 仮想マシンを調査してもらった（Zenn / Microsoft 有志）](https://zenn.dev/microsoft/articles/sreagent-getstart) | VM の CPU 高負荷シナリオで SRE Agent を試した入門レポート。作成手順・調査フロー・権限設定・日本語対応などを実演を交えて紹介 |

## デモ動画

| タイトル | 説明 |
|:---|:---|
| [Proactive .NET Reliability with Azure SRE Agent](https://www.youtube.com/watch?v=Kx_6SB-mhgg) | ASP.NET アプリを題材に、インシデント報告前に問題を検知・修復するプロアクティブな信頼性向上の方法をデモで解説 |

## 事例

| タイトル | 説明 |
|:---|:---|
| [Azure SRE Agent x PagerDutyによる近未来インシデント対応への期待（イオンスマートテクノロジー / AEON TECH HUB #23）](https://speakerdeck.com/aeonpeople/the-future-of-incident-response-azure-sre-agent-x-pagerduty) | PagerDuty と Azure SRE Agent を連携し、インシデント検知から自律調査・復旧までを自動化するシナリオの実践報告 |

## リソース定義

### Subagent

TBD

### Skill

TBD

### Connector

TBD

### Tools

TBD
