# 參考來源｜manhay212/t-ai-skills

Repo: https://github.com/manhay212/t-ai-skills

授權：AGPL-3.0（以來源 Repo 當下 LICENSE 為準）

Reviewed: 2026-09-04

## 類型

多個獨立 Agent Skill 的占卜／命理工具集合。核心架構是把「可計算／可抽取的結構事實」與「LLM 解讀」分離，並以統一 JSON envelope 回傳結果、參考資料與 unavailable 欄位。

## 可借鑑內容

### ADAPTED｜調整後採用 — Truth layer / Interpretation layer 分離

來源把 skill 定位成 truth layer：真正牌面、星盤、結構結果由程式產生；模型只負責解讀。

本手冊已有 `RUNTIME_DRAW.md` 的 DRAW / CAST FACT 與 Interpretation 分離，因此此概念屬於已存在方向的外部佐證，不另建新 owner。

### REFERENCE-ONLY｜僅供參考 — `unavailable[]` / graceful degradation

來源用一致的 `unavailable[]` 列出無法計算的內容，而不是猜測。

本手冊目前用 `UNRESOLVED`、partial success、fail-closed 與 reduced scope 處理相近問題。現階段不新增另一套 runtime schema，以避免和 Randomizer output contract drift。

### REFERENCE-ONLY｜僅供參考 — 統一 machine envelope

來源把 `inputs`、`result`、`reference`、`unavailable`、`notes` 分層，對跨 skill agent integration 很乾淨。

若未來 Randomizer 或正式 reading-record schema 擴充，可再評估是否吸收此 envelope 思路。

## 不直接採用

- 不採用其固定塔羅牌陣作為本手冊 canonical spread。
- 不採用其其他術數引擎或 dependency。
- 不複製其 AGPL 程式碼進本 Repo。

## 已影響／佐證主文件

- `RUNTIME_DRAW.md`
- `INPUT_CONTRACT.md`
- `READING_LIFECYCLE.md`
