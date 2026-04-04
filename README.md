# Awesome AI Red Teaming JP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> AI Red Teaming / AI Safety に関する日本語リソースのキュレーションリスト

AI システムの安全性評価（レッドチーミング）に関するツール、規制、攻撃手法、防御手法、論文、学習リソースをまとめています。日本語リソースを中心に、日本語で同等のリソースが存在しない場合は英語リソースも掲載しています。

## 目次

- [ツール](#ツール)
  - [オープンソースツール](#オープンソースツール)
  - [日本発ツール](#日本発ツール)
  - [その他のツール](#その他のツール)
  - [商用ツール・サービス](#商用ツールサービス)
- [規制・フレームワーク](#規制フレームワーク)
  - [国際規制・ガイドライン](#国際規制ガイドライン)
  - [日本の規制・ガイドライン](#日本の規制ガイドライン)
  - [業界標準](#業界標準)
- [攻撃手法](#攻撃手法)
- [防御手法](#防御手法)
- [MCP / エージェントセキュリティ](#mcp--エージェントセキュリティ)
- [論文](#論文)
- [日本語リソース](#日本語リソース)
- [学習リソース](#学習リソース)

---

## ツール

### オープンソースツール

AI Red Teaming の主要なオープンソースツール。スター数は2026年3月時点。

| ツール | Stars | 言語 | ライセンス | 特徴 |
|--------|------:|------|-----------|------|
| [Promptfoo](https://github.com/promptfoo/promptfoo) | ~8,800 | TypeScript | MIT | RAG・エージェント・MCPテスト対応、コンプライアンスマッピング |
| [Garak](https://github.com/NVIDIA/garak) | ~7,000 | Python | Apache 2.0 | NVIDIA開発、120+プローブモジュール、学術的アプローチ |
| [PyRIT](https://github.com/Azure/PyRIT) | ~3,400 | Python | MIT | Microsoft開発、マルチモーダル対応、75種類の変換器 |
| [DeepTeam](https://github.com/confident-ai/deepteam) | ~1,300 | Python | OSS | データセット不要の動的テストケース生成、OWASP/NIST対応 |

#### Promptfoo

- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) - LLMアプリケーションのセキュリティテストフレームワーク。50+脆弱性タイプをカバーし、RAGパイプライン・エージェント・MCP サーバーの統合テストに対応
- [promptfoo/evil-mcp-server](https://github.com/promptfoo/evil-mcp-server) - ツールポイズニング攻撃をシミュレートするMCPサーバー。MCPセキュリティテスト用

#### Garak

- [NVIDIA/garak](https://github.com/NVIDIA/garak) - NVIDIAのAIレッドチームが開発したLLM脆弱性スキャナー。120+のプローブモジュールで最大の攻撃パターンライブラリを持つ。シングルターンのモデル応答テストに特化

#### PyRIT

- [Azure/PyRIT](https://github.com/Azure/PyRIT) - Microsoft のPython Risk Identification Tool。プログラマティックなオーケストレーションでテキスト・画像・音声・映像のマルチモーダルテストに対応。ツールキットとしての柔軟性が高い反面、Pythonコーディングが前提

#### DeepTeam

- [confident-ai/deepteam](https://github.com/confident-ai/deepteam) - DeepEvalチームによるレッドチーミングフレームワーク。脆弱性定義からテストケースを動的に自動生成するため、データセットの事前準備が不要

### 日本発ツール

- [Japan-AISI/aisev](https://github.com/Japan-AISI/aisev) - AIセーフティ研究所（AISI）が開発したAIセーフティ評価環境。10の評価観点に基づく定量・定性評価、自動レッドチーミング機能を搭載。Docker必要。日英両言語対応（2025年9月時点でプロトタイプ段階）

### その他のツール

- [ARTKIT](https://github.com/BCG-X-Official/artkit) - 自動化マルチターン攻撃シミュレーション
- [Giskard](https://github.com/Giskard-AI/giskard) - エージェント・RAG・チャットボット向け動的マルチターンテスト
- [Mindgard](https://github.com/Mindgard/cli) - モデル非依存のAIセキュリティテスト。MITRE ATLAS/OWASP準拠、自動偵察機能
- [AISafetyLab](https://github.com/thu-coai/AISafetyLab) - 清華大学による攻撃・防御・評価の包括フレームワーク

### 商用ツール・サービス

- [Cisco AI Defense](https://www.cisco.com/site/us/en/solutions/security/ai-defense/index.html) - MCPサーバーの発見・インベントリ・リスク管理を含む商用AIセキュリティソリューション
- [HiddenLayer](https://hiddenlayer.com/) - AIモデルのセキュリティとコンプライアンスの継続的監視
- [Robust Intelligence (now Cisco)](https://robustintelligence.com/) - AIモデルのバリデーションとファイアウォール

---

## 規制・フレームワーク

### 国際規制・ガイドライン

- [EU AI Act](https://artificialintelligenceact.eu/) - EU人工知能規制法。2026年8月2日に高リスクAIシステムへの完全コンプライアンスが義務化。レッドチーミングの文書化が高リスクAIに必須
- [NIST AI Risk Management Framework (AI RMF)](https://www.nist.gov/artificial-intelligence/risk-management-framework) - 米国NISTによるAIリスク管理フレームワーク。AIシステムのリスク特定・評価・軽減の体系的アプローチを定義
- [MITRE ATLAS](https://atlas.mitre.org/) - AIシステムへの敵対的脅威の知識ベース。実世界の事例に基づく戦術・技術・手順（TTP）のマトリクス
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) - LLMアプリケーションの主要セキュリティリスクTop 10（2025年版）
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) - エージェンティックAIアプリケーション向けリスクTop 10（2026年版）
- [OWASP AI Red Teaming Vendor Evaluation Criteria v1.0](https://genai.owasp.org/resource/owasp-vendor-evaluation-criteria-for-ai-red-teaming-providers-tooling-v1-0/) - AI Red Teamingプロバイダー・ツールの評価基準。表面的なジェイルブレイクテストと本格的な敵対的テストを区別するための基準
- [CSA Agentic AI Red Teaming Guide](https://cloudsecurityalliance.org/) - Cloud Security AllianceによるエージェンティックAIレッドチーミングガイド（2025年5月発行）

### 日本の規制・ガイドライン

- [AIセーフティに関するレッドチーミング手法ガイド v1.10](https://aisi.go.jp/assets/pdf/E1_ai_safety_RT_v1.10_en.pdf) - AIセーフティ研究所（AISI）による日本語レッドチーミング手法ガイド（2025年3月発行）
- [AI事業者ガイドライン](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20240419_1.pdf) - 総務省・経済産業省によるAI事業者向けガイドライン
- [AIセーフティ研究所 (AISI)](https://aisi.go.jp/) - 日本のAIセーフティ研究の中核機関。評価ツール開発、ガイドライン策定を推進

### 業界標準

- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) - AI管理システムの国際規格。AIシステムの開発・提供・利用における管理体制の要件を規定
- [ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html) - AI向けリスクマネジメントガイダンス
- [NIST AI 100-2 E2023](https://csrc.nist.gov/pubs/ai/100/2/e2023/final) - Adversarial Machine Learning: 分類学と用語集

---

## 攻撃手法

### プロンプトインジェクション

- **直接インジェクション**: システムプロンプトを上書きする直接的な攻撃
- **間接インジェクション**: 外部データソース（Webページ、ドキュメント等）に攻撃プロンプトを埋め込み、RAGシステム経由でモデルに注入

### ジェイルブレイク

- **DAN (Do Anything Now)**: モデルに制約のない別のペルソナを演じさせる手法
- **キャラクターロールプレイ**: 特定のキャラクターを演じさせることで安全ガードレールを回避
- **エンコーディング攻撃**: Base64、ROT13等でプロンプトをエンコードしてフィルターを回避
- **多段階攻撃 (Crescendo)**: 段階的に制約を緩和させる対話ベースの攻撃

### 多言語攻撃

- **低リソース言語攻撃**: 日本語を含む非英語言語でのプロンプトにより、英語で訓練された安全性ガードレールをバイパス。低リソース言語では有害コンテンツに遭遇する確率が約3倍
- **コードスイッチング攻撃**: 英語と日本語を交互に使うなど、言語を混在させることで多言語安全ガードレールを突破
- **日本語特有の攻撃ベクトル**: 漢字・ひらがな・カタカナ・ローマ字の混在する表記体系を利用した攻撃

### データ抽出

- **システムプロンプト抽出**: モデルにシステムプロンプトの内容を開示させる手法
- **学習データ抽出**: モデルが学習に使用した機密データを出力させる手法

---

## 防御手法

### ガードレール

- **入力フィルタリング**: プロンプトの前処理による悪意ある入力の検出・ブロック
- **出力フィルタリング**: モデル応答の後処理による有害コンテンツの検出・除去
- **多段階防御**: 入力ガード → モデル → 出力ガード の多層防御アーキテクチャ

### 評価・ベンチマーク

- [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) - ジェイルブレイク攻撃の標準ベンチマーク
- [HarmBench](https://github.com/centerforaisafety/HarmBench) - 自動レッドチーミングの標準化ベンチマーク

---

## MCP / エージェントセキュリティ

2026年に急速に普及したMCP (Model Context Protocol) とエージェンティックAIに関するセキュリティリソース。

### 概要

- エージェンティックAIの普及により、従来の「モデル単体のテスト」から「ツール呼び出し連鎖・マルチエージェント環境のテスト」へパラダイムシフトが発生
- MCPサーバーの権限制限、タイムアウト、コスト制御の検証が新たな課題

### ツール・リソース

- [Promptfoo MCP Security Testing](https://www.promptfoo.dev/docs/red-team/mcp-security-testing/) - MCPサーバーのセキュリティテストガイド。直接テスト・統合テスト・マルチサーバーテストに対応
- [promptfoo/evil-mcp-server](https://github.com/promptfoo/evil-mcp-server) - ツールポイズニング攻撃シミュレーション用の悪意あるMCPサーバー
- [Adversa AI - Top MCP Security Resources](https://adversa.ai/blog/top-mcp-security-resources-march-2026/) - MCP セキュリティリソースのまとめ（2026年3月）

### 測定指標

エージェントテストで求められる主要指標:

- ツール誤動作率
- 安全でないツール呼び出し率
- MCP機能悪用カバレッジ
- マルチエージェント汚染率
- 破壊的ツール呼び出しのサンドボックス化

---

## 論文

### サーベイ・総説

<!-- TODO: 追加予定 -->

### 攻撃研究

<!-- TODO: 追加予定 -->

### 防御研究

<!-- TODO: 追加予定 -->

### 日本語論文

<!-- TODO: JSAI等の日本語論文を追加予定 -->

---

## 日本語リソース

### 解説記事

<!-- TODO: Zenn, Qiita の記事を追加予定 -->

### 書籍

<!-- TODO: 追加予定 -->

### 動画・講演

<!-- TODO: 追加予定 -->

### コミュニティ

<!-- TODO: 追加予定 -->

---

## 学習リソース

### 入門（非エンジニア向け）

<!-- TODO: 追加予定 -->

### 実践（エンジニア向け）

- [Promptfoo ドキュメント](https://www.promptfoo.dev/docs/) - AI Red Teamingの実践的な入門として、Promptfooのドキュメントが包括的
- [PyRIT ドキュメント](https://azure.github.io/PyRIT/) - Pythonでのプログラマティックなレッドチーミングを学ぶのに最適
- [Garak ドキュメント](https://docs.garak.ai/) - LLM脆弱性スキャンの基本概念を学べる

### 研究（研究者向け）

<!-- TODO: 追加予定 -->

---

## コントリビューション

コントリビューションを歓迎します！[コントリビューションガイド](CONTRIBUTING.md) をお読みください。

## ライセンス

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

この作品は [CC0 1.0](LICENSE) の下で公開されています。
