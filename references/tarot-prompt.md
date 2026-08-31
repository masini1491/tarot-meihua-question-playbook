# 參考來源｜eric32181630/tarot-prompt

Repo: https://github.com/eric32181630/tarot-prompt

授權：未在 Repo metadata 中明確標示；引用前應再次確認。

## 類型

前端塔羅抽牌與 LLM Prompt 組裝工具，可將問題、牌面、正逆位、牌位／背景等資訊結構化後交給 LLM 解讀。

## 值得吸收

### ADAPTED｜調整後採用 — 結構化序列化

來源把塔羅解讀的主要輸入整理成結構化 Prompt，而不是只丟一串牌名。

本手冊吸收為 `INPUT_CONTRACT.md`，核心欄位包括：

- 問題
- 問題類型
- 時間範圍
- 完成判定規則
- 牌陣
- 牌位
- 逆位規則
- 牌面來源
- 已知背景事實

技術欄位名稱仍保留英文，以利工具與 schema 對照。

### ADOPTED｜已採用 — 問題與補充背景分離

結構化輸入的價值在於可以把「真正問題」和「額外背景」分開保存，避免背景敘事蓋過牌位契約。

## 不直接採用

- 不把星盤資料視為塔羅解讀必需輸入。
- 不複製其前端 UI 或 Prompt 文字。
- 本手冊的重點是治理問題設計，不是建立特定 LLM Prompt 產生器。

## 已影響主文件

- `INPUT_CONTRACT.md`
- `QUESTION_DESIGN.md`
