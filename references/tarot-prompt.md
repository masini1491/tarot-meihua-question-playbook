# Reference｜eric32181630/tarot-prompt

Repo: https://github.com/eric32181630/tarot-prompt

License: 未在 Repo metadata 中明確標示；引用前應再次確認。

## 類型

前端 Tarot 抽牌與 LLM Prompt 組裝工具，可將 question、cards、upright/reversed、position/context 等資訊結構化後交給 LLM 解讀。

## 值得吸收

### ADAPTED — Structured serialization

來源把 Tarot reading 的主要輸入整理成結構化 prompt，而不是只丟一串牌名。

本 Playbook 吸收為 `INPUT_CONTRACT.md`：

- question
- question type
- horizon
- completion rule
- spread
- positions
- reversals
- cards source
- context facts

### ADOPTED — Question 與補充 context 分離

結構化輸入的價值在於可以把「真正問題」和「額外背景」分開保存，避免背景敘事蓋過牌位契約。

## 不直接採用

- 不把星盤資料視為 Tarot 解讀必需輸入。
- 不複製其前端 UI 或 prompt 文字。
- 本 Playbook 的重點是治理問題設計，不是建立特定 LLM prompt generator。

## 已影響主文件

- `INPUT_CONTRACT.md`
- `QUESTION_DESIGN.md`
