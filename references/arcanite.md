# Reference｜katelouie/arcanite

Repo: https://github.com/katelouie/arcanite

License: MIT（以來源 Repo 當下 LICENSE 為準）

## 類型

Python Tarot reading engine，將 interpretation 分成：

1. deterministic assembly：依牌位與 curated card meanings 組出結構化內容；
2. optional LLM synthesis：再由 LLM 做敘事整合。

它也提供 question classification、不同 spread、position-specific interpretations 與 question-context variations。

## 值得吸收

### ADAPTED — 先分類問題，再選 spread

Arcanite 會先辨識 question type，並讓牌義依 context 與 spread position 變化。

本 Playbook 吸收為：

> 不要先決定抽幾張才硬塞問題；先辨識比較／時間／流程／人物／原因等題型，再選牌陣。

### ADOPTED — Position semantics 必須先於 LLM 敘事

它的 deterministic layer 先依 spread position 取得 position-specific interpretation，再交給 LLM synthesis。

本 Playbook 吸收為：

> 牌位契約是上游權威；敘事只能整合已定義的牌位證據，不能在最後改寫牌位功能。

### ADAPTED — Structure first, narrative second

本 Playbook 進一步泛化成：

1. 先固定 question / spread / positions。
2. 先做逐位置與整組結構判讀。
3. 最後才產生整體故事。

目的：避免先有結論再挑牌義支持。

## 不直接採用

- 本 Repo 不需要複製 Arcanite 的完整 card database、RAG schema 或 PDF pipeline。
- question classification 只當作題型 routing，不代表 AI 自動分類永遠正確；高歧義問題仍應人工拆解。

## 已影響主文件

- `INPUT_CONTRACT.md`
- `TAROT.md`
- `QUESTION_DESIGN.md`
