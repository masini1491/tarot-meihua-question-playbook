# 參考來源｜william0wang/yifortune

Repo: https://github.com/william0wang/yifortune

授權：MIT（以來源 Repo 當下 LICENSE 為準）

Reviewed: 2026-09-04

## 類型

Agent Skills 架構的多主題命理／占卜 skill，強調單一入口、routing table、progressive disclosure、Agent 主動選工具、最小必要提問與兩層輸出。

## 可借鑑內容

### ADAPTED｜調整後採用 — Progressive contract admission

來源明確主張：Agent 應先從使用者自然語言推導可確定資訊，只在真正缺少且會影響結果時才問最小必要問題，不把 routing 或工具選擇外包給使用者。

本手冊已將此概念整併到 `INPUT_CONTRACT.md`：

> 完整 schema 是 Agent 的正規化與保存責任，不是要求使用者逐欄填寫的表單。

### ADAPTED｜調整後採用 — Proactive routing

來源以單一 `SKILL.md` 作入口，依題意自動 route 至最低必要 reference。

本手冊已有 `CHAT_INIT.md` + `METHOD_ROUTING.md`，採同類型 progressive routing，但保留 Tarot／Meihua 方法責任與生命週期規則。

### REFERENCE-ONLY｜僅供參考 — Two-layer output

來源區分專業 traceability layer 與使用者 plain-language layer。

本手冊已有 fact／inference／output contract，不另外建立新的固定雙層格式，避免與 `CHATGPT_OUTPUT.md` 重複 owner。

## 不直接採用

- 不採用其八字、占星或其他本 Repo 未支援的術數規則。
- 不使用其外部 MCP／API 服務作為本手冊 runtime 依賴。
- 不照搬其工具選擇與方法優先序。

## 已影響主文件

- `INPUT_CONTRACT.md`
- `CHAT_INIT.md`
- `METHOD_ROUTING.md`
