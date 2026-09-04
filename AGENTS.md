# AGENTS.md

## 儲存庫用途

本儲存庫是一套可重用、公開的實戰手冊，用於設計低歧義的塔羅與梅花易數題目、方法選擇、牌陣、占問生命週期、ChatGPT Runtime Draw、交叉驗證方法，以及控制 ChatGPT 的出題與解讀輸出。

本儲存庫**不是**私人占卜日誌，也**不是**個人預測資料庫。

## 權威與文件 ownership

- `main` 是目前可信來源（source of truth）。
- `CHAT_INIT.md`：新聊天室最小 bootstrap／routing。
- `METHOD_ROUTING.md`：使用者未指定方法時，依主要 judgment function 選 Tarot／Meihua／Both；包含 single-method sufficiency、Both responsibility 與 tie-breaker gate。
- `INPUT_CONTRACT.md`：抽牌／起卦前需要保存的輸入契約與 draw/cast provenance。
- `QUESTION_DESIGN.md`：問題拆解、牌位功能與高頻題型模式。
- `READING_LIFECYCLE.md`：新題／承接／補占／重占／現實更新／完成／回測。
- `RUNTIME_DRAW.md`：ChatGPT／AI 何時可以實際執行程式抽牌／起卦、canonical tool、provenance 與 fail-closed fallback。
- `TAROT.md`：塔羅特有的牌位、牌陣與解讀規則。
- `MEIHUA.md`：梅花特有的起卦、體用、主互變、動爻、外應與應期規則。
- `CROSS_VALIDATION.md`：只處理 Tarot × Meihua 的分工與 reconciliation。
- `CHATGPT_OUTPUT.md`：ChatGPT 最終出題、解讀、copy-ready 與 pre-send output contract。
- `CASE_STUDIES/`：匿名化、低頻載入的失敗案例與方法演進。
- `references/`：外部來源 dossier；不自動取得主規則權威。

Runtime Draw 的 RNG／抽牌／起卦**實作**不在本 Repo 維護；canonical implementation 是 `masini1491/tarot-plum-randomizer/randomizer.py`。本 Repo 只維護治理與使用契約，避免演算法重複造成 drift。

穩定 policy 只保留一個 canonical owner；本檔只 routing，不複製各主文件的完整規則。

## 儲存庫與 Git 身分設定

- Repository：`masini1491/tarot-meihua-question-playbook`
- GitHub 帳號：`masini1491`
- Git commit author name：`masini1491`
- Git commit author email：`10146979+masini1491@users.noreply.github.com`
- 若 local Git 尚未設定 author identity，只做 repository-local 設定：

```bash
git config user.name "masini1491"
git config user.email "10146979+masini1491@users.noreply.github.com"
```

除非使用者明確要求，不修改 global Git identity；不得保存 token、password、API key 或其他 credential。

## 語言規則

- 正式說明、規則、案例與參考摘要預設使用繁體中文。
- 程式欄位、檔名、API 名稱、GitHub repository、schema key、seed、draw id 等技術識別字保留原文。
- 外部來源以繁中摘要，不直接把原文語氣搬進主規則。

## 隱私與公開安全

不得提交：

- 真實姓名或可識別的感情／關係細節；
- 可對應特定個人的出生日期、時間與地點；
- 健康、性相關私人紀錄；
- 私人公司名稱與未公開人事、薪資、客戶或專案資訊之組合；
- 未經去識別化的截圖、聊天紀錄或其他私人來源材料；
- secrets、credentials 或未授權第三方內容的大段複製。

案例只保留足以說明方法問題的最低必要結構。

## AI 讀取紀律

- 實際使用先讀 `CHAT_INIT.md`，再依 task 只讀最低必要 canonical sections。
- 使用者未指定 Tarot／Meihua／Both，而 workflow 需要決定占卜方法時，才載入 `METHOD_ROUTING.md`；若方法已由使用者指定或已有既存牌面／卦象，不為形式重跑 method routing。
- 不因某文件存在就預設完整載入；`CASE_STUDIES/`、`references/`、Historical Context 預設是 Cold。
- 只有使用者要求 ChatGPT 自己抽牌／起卦，或 workflow 明確需要 AI Runtime Draw 時才載入 `RUNTIME_DRAW.md`；一般使用者自行抽牌不付這段 Context 成本。
- 若 exact section／問題身份已能唯一命中 owner，可直接 bounded-read，不為 routing 做額外 ceremony。
- 舊聊天室、memory 或歷史占卜不得覆蓋 current reality、原 Input Contract 或目前主規則。

## 維護風格

- 優先修改既有 canonical owner；只有形成獨立 retrieval intent 才新增文件。
- 新案例若揭露可泛化失敗模式，先判斷應更新哪個主規則，再新增匿名案例。
- 不在 README、AGENTS、CHAT_INIT 與主題文件間複製完整 normative policy。
- Runtime implementation 變更優先修改 Randomizer repo；Playbook 只在 governance contract 改變時同步。
- 純 Markdown 修改至少檢查 routing、heading、link 與 ownership 是否矛盾。

## 外部參考

可引用公開的塔羅／梅花易數／AI 方法論 GitHub 專案，但外部規則不會自動成為本儲存庫權威。整併時記錄前提、流派差異、authority boundary、授權與不採用項目。
