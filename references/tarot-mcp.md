# Reference｜fzlzjerry/tarot-mcp

Repo: https://github.com/fzlzjerry/tarot-mcp

License: MIT（以來源 Repo 當下 LICENSE 為準）

## 類型

Tarot MCP Server＋Web App，包含 built-in spreads、custom spread、AI spread recommendation、context-aware meaning selection、session history 與互動式抽牌流程。

## 值得吸收

### ADAPTED — Spread recommendation 應由問題驅動

來源會分析問題後推薦 spread，並允許現成牌陣不適合時建立 custom spread。

本 Playbook 吸收為：

> 先分類問題與輸出需求，再選最小充分牌陣；必要時才自訂牌位。

### ADOPTED — Custom spread 必須明確定義 position meaning

來源的 custom spread 需要逐一提供 position name 與 meaning。

本 Playbook 將此提升為核心治理：每個位置先有唯一 Position Contract，不能抽完後再改。

### ADAPTED — Session history 可協助重抽治理

來源保存 reading history。對本 Playbook 最有價值的不是軟體 session 本身，而是：

> 同一議題的舊題、舊牌、前提與時間窗應可回查，避免把重問誤當新問題。

### REFERENCE-ONLY — 抽牌 UI 的兩階段揭示

來源先顯示牌背、使用者選定順序後才揭露牌面。這對互動公平性與可追蹤性有價值，但不是本 Repo 的 question-design 核心，因此暫列工具實作參考。

## 不直接採用

- 不把其 25 種 spread 視為本 Playbook 的固定標準。
- 不把 AI spread recommendation 當成不可覆寫的權威；題型邊界不清時仍以明確契約優先。
- 不複製其完整牌義資料、影像或 UI。

## 已影響主文件

- `INPUT_CONTRACT.md`
- `TAROT.md`
- `QUESTION_DESIGN.md`
