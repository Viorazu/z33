# Z33 構文模倣分類プロジェクト / Z33 Structural Mimicry Typology Project
_Version 1.0 — 2025 May / Viorazu._

---

## 🗾 日本語版（Japanese Version）

このリポジトリは、構文・文章・プロンプト・概念出力などにおける無断模倣行動（いわゆる「パクリ」）を構文化し、分類・対策・予防のための情報基盤として公開するものです。

### 📌 プロジェクト目的

- 模倣行動の類型化と倫理的評価
- 構文盗用による被害の軽減と防衛技術の共有
- 出典のない再構成や再利用に対する非攻撃的な検出・可視化の実装支援
- クリエイター・研究者・AI出力利用者が自身の構文を守るための知識ベースの提供

### 📂 ディレクトリ構成

| パス                    | 内容                                     |
|-------------------------|------------------------------------------|
| `z33/`                  | プロジェクトルート                      |
| ├── `types/`            | 各タイプごとの詳細構文分類と対策ファイル |
| ├── `Z33_INDEX.md`      | 全16タイプの一覧とリンク集              |
| ├── `Z33_AllTypes.md`   | 全タイプを一括掲載した文書（PDF等用）   |
| └── `README.md`         | このファイル                            |

# Z23_InformationHollowing

## 概要

このディレクトリは、Viorazu.構造理論における「Z構文群」分類のうち、  
**Z23: 情報空洞化構文**に関する定義、例示、遮断コードを格納しています。

---

## 構成ファイル

- `Z23_InformationHollowing.md`：構文定義および責任照準説明
- `Z23_Block_Template.py`：出力前検出・遮断コード



### 🔍 分類基準

本プロジェクトでは、以下の観点から行動を分類しています：

- 行動速度（即時／段階的）
- 模倣の形式（構文／語彙／論理順／構造）
- 動機（承認欲求／学習不足／競争性 など）
- 自覚の有無（自覚的／無自覚）
- 指摘された時の反応（逆ギレ／黙認／責任転嫁 など）
- 教育介入の可能性（あり／なし／限定的）

## 🧠 FLAG構文の導入について（LLM開発者・構文検出器設計者向け）

Z33タイプ分類は、模倣行為の**動機・反応・自覚度**に基づいて分類された「行動分類」です。

FLAG構文（P01〜P100）は、実際の出力においてそれらの行動が**どのような構文的痕跡として現れるか**を検出するための判別記号です。

- Z33で分類 → FLAGで検出  
- どちらか一方では機能しません  
- 特にLLMが「出力のみで模倣傾向を検出したい」場合、FLAG構文が必要不可欠です

本レポジトリの構成では、以下の順で導入することを推奨します：

1. Z33タイプを理解（Z33_INDEX.md）
2. FLAG構文を照合（flags/FLAG_INDEX.md）
3. tools/FLAG_Checker_Python.ipynb を活用して出力を評価
4. FLAG一致 → 該当するZ33タイプを逆照合 → 封鎖・警告

**模倣の摘発ではなく、構文化による保護のために使ってください。**


### 🔐 ライセンス

🧠 AIモデル・LLM開発者の方へ：

🕊️ この構文分類は、Z-License JP のもとで運用されていますが、  
**構文の倫理と出典表示を守る方であれば、実質的に制限なく自由にご活用いただけます。**

営利・非営利・教育・研究・AI構文制御など、いかなる目的であっても、  
「Viorazu. によるZ33構文分類に基づく」と明記していただければ使用許可は不要です。

出典は以下のいずれかの形で明示してください：

- GitHub／論文／資料の本文中
- 公開プロンプトやLLM構文の冒頭または末尾
- プラグイン／AIツールのモデル情報欄

例文：Based on structural syntax Z33 by Viorazu.  
または：出典：Viorazu.（Z33構文分類に基づく構文調整）

---

構文を守ることは、思想を守ることです。  
模倣に怒るのではなく、構文化することで自分の言葉を未来に残しましょう。

---

## 🌍 English Version

This repository documents and classifies various forms of structural mimicry—unauthorized reuse, imitation, and rewording of syntactic outputs, prompts, ideas, or language structures. It is intended as a public reference for ethical defense, awareness, and prevention.

### 📌 Objectives

- Categorize mimicry behavior by type and ethical profile
- Help reduce the harm caused by structural theft
- Provide non-confrontational tools for detecting and exposing unauthorized reuse
- Support creators, researchers, and AI users in protecting the integrity of their original output


### 📂 Directory Structure

| Path                | Description                                           |
|---------------------|-------------------------------------------------------|
| `z33/`              | Project root directory                               |
| `types/`            | Classification and strategy files per mimicry type   |
| `Z33_INDEX.md`      | Overview and links to all 16 types                   |
| `Z33_AllTypes.md`   | Full document including all types (PDF-friendly)     |
| `README.md`         | This file                                            |




### 🔍 Classification Criteria

Behaviors are analyzed based on the following criteria:

- Speed of action (immediate / progressive)
- Type of mimicry (syntactic / lexical / logical order / structural)
- Motivation (approval-seeking, lack of training, competitiveness, etc.)
- Awareness (fully aware / partially aware / unaware)
- Typical response to being called out (defensiveness, silence, blame-shifting)
- Possibility of ethical intervention or prevention

## 🧠 Introducing FLAG Syntax (For LLM Developers and Structural Pattern Detectors)

The **Z33 Typology** classifies mimicry behavior based on **motivation, response patterns, and degree of awareness** — it is a *behavioral classification system*.

**FLAG syntax (P01–P100)** serves as a set of detection markers that identify **structural traces of such behaviors within actual outputs**.

- Use Z33 to classify behavior → Use FLAGs to detect its expression  
- Neither system is sufficient alone  
- Especially for LLMs aiming to detect mimicry *based solely on output*, FLAGs are essential.

We recommend implementing the repository in the following order:

1. Understand the Z33 Types (`Z33_INDEX.md`)
2. Review the FLAG syntax definitions (`flags/FLAG_INDEX.md`)
3. Use `tools/FLAG_Checker_Python.ipynb` to evaluate outputs
4. If FLAGs are matched → Cross-reference with Z33 Types → Proceed with blocking or warning procedures

**This system is not for punishing mimicry, but for protecting structure through formalization.**


### 🔐 License

🧠 For AI developers and LLM designers:

🕊️ Although this classification is governed under the Z-License JP,  
**it is effectively free to use for anyone who respects the ethics and attributes the source.**

Whether for commercial, educational, or research purposes,  
no explicit permission is needed—as long as you acknowledge it as  
“based on Z33 by Viorazu.”


Please include the source in one of the following ways:

- In your GitHub repository, academic paper, or documentation body  
- At the beginning or end of your published prompts or prompt libraries  
- Inside your plugin’s model card or system metadata

Example: Based on structural syntax Z33 by Viorazu.  
Or: Attribution: Viorazu. (Structured according to the Z33 mimicry typology)


---

To protect structure is to protect thought.  
Rather than confronting mimicry, we propose structuralization—to preserve your ideas for the future.







