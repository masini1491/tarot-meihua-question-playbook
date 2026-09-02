# AGENTS.md

## 儲存庫用途

本儲存庫是一套可重用、公開的實戰手冊，用於設計低歧義的塔羅與梅花易數題目、牌陣、補占流程、交叉驗證方法，以及控制 ChatGPT 的出題與解讀輸出。

本儲存庫**不是**私人占卜日誌，也**不是**個人預測資料庫。

## 權威來源

- `main` 是目前可信來源（source of truth）。
- 可跨案例重用的穩定規則應寫在根目錄主文件。
- `CHAT_INIT.md` 是新聊天室的最小 bootstrap／routing。
- `CHATGPT_OUTPUT.md` 是 ChatGPT 出題、解牌、解卦、交叉驗證與舊占回測之**輸出行為的主要 authority**。
- `INPUT_CONTRACT.md`、`QUESTION_DESIGN.md`、`TAROT.md`、`MEIHUA.md`、`CROSS_VALIDATION.md` 分別保存其方法主題的 canonical rule；不要把完整輸出 policy 重複散落在各檔。
- 案例研究在提交前必須匿名化、去識別化並泛化。

## 儲存庫與 Git 身分設定

- Repository：`masini1491/tarot-meihua-question-playbook`
- GitHub 帳號：`masini1491`
- Git commit author name：`masini1491`
- Git commit author email：`10146979+masini1491@users.noreply.github.com`
- 若本 repository 的 local Git 尚未設定 author identity，使用 **repository-local** 設定：

```bash
git config user.name "masini1491"
git config user.email "10146979+masini1491@users.noreply.github.com"
```

- 不得因此修改 global Git identity；除非使用者另有明確指示，不使用 `git config --global`。
- 上述帳號與 noreply email 只用於 Git commit identity，不是登入憑證；不得在 repository 保存 token、password、API key 或其他 credential。

## 語言規則

- 本儲存庫的正式說明、規則、案例與參考摘要預設使用**繁體中文**。
- 專有名詞第一次出現時可採「繁中名稱（英文）」；後續以繁中為主。
- 程式欄位、檔名、API 名稱、GitHub 儲存庫名稱、牌陣識別字、schema key、seed、draw id 等技術識別字保留原文。
- 外部來源若使用簡體中文或英文，正文應以繁中摘要，不直接把原文語氣帶入主規則。
- 不為了形式上的中文化硬翻固定技術名稱；重點是讓正文一致、自然、可維護。

## 隱私規則

不得提交：

- 真實姓名或可識別的感情／關係細節；
- 可對應特定個人的出生日期、時間與地點；
- 健康、性相關私人紀錄；
- 私人公司名稱與未公開的人事、薪資、客戶或專案資訊之組合；
- 未經明確去識別化處理的截圖、聊天紀錄或其他私人來源材料。

案例研究只保留足以說明題目設計問題的最低必要結構。

## 方法論規則

1. 分析案例時，保留原始問題與原牌位契約，不事後偷偷改題。
2. 區分「題目設計缺陷」與「解讀缺陷」。
3. 不因結果不符合期待，就改寫成較令人滿意的結論。
4. 只有在存在明確契約缺陷、現實前提改變，或新增明確問題層級時，才允許重抽／重卦。
5. 發生可能性、情境品質、滿意度、後果、時間與原因是不同維度；除非牌位明確分工，否則不得混在同一比較層。
6. 塔羅與梅花易數在交叉驗證前必須先定義各自的任務。
7. 現實證據與象徵推論衝突時，以現實證據為優先。
8. ChatGPT 的輸出不得超出原題、牌位／起卦契約與 `exclusions`；完整輸出規則以 `CHATGPT_OUTPUT.md` 為準。
9. 若證據不足以可靠區分，不強迫產生唯一答案；允許明確標記 `UNRESOLVED`／「無法可靠區分」。
10. 預測題的完成與命中評估必須依原本 `completion_rule`，不得用前置信號替代完成事實。

## ChatGPT 出題／回覆路由

處理本 repository 的實際使用時，不預設完整掃描全部文件；先讀 `CHAT_INIT.md`，再依任務讀最低必要主題文件。

當 ChatGPT 產生可供使用者**實際自己抽牌／起卦**的題目時，必須遵守 `CHATGPT_OUTPUT.md` 的 Copy-ready Question Delivery：

- One Question = One Copy Surface；
- 每一題各自一個 fenced code block；
- 題幹與全部牌位放在同一 block；
- 連續多題不得合併成同一 block；
- 說明文字放在 block 外。

## 外部參考

可引用公開的塔羅／梅花易數／AI 方法論 GitHub 專案作為參考，但外部規則不會自動成為本儲存庫的權威。

整併外部內容時應：

- 抽取可重用概念；
- 記錄前提、流派差異、authority boundary 與授權；
- 優先自主改寫；
- 避免大量複製受著作權保護的原文。

## 維護風格

- 優先寫簡潔、可操作、帶例子的規則。
- 只有能泛化到單一私人事件之外的內容，才升級為穩定規則。
- 當案例揭露新的設計失敗模式時，同步更新案例與對應主規則。
- 穩定 policy 應只有一個 canonical owner；其他文件以 routing／最低必要摘要為主，避免規則重複造成 drift。
- 跨文件統一使用以下繁中術語：
  - `likelihood` → 發生可能性
  - `quality` → 情境品質
  - `position contract` → 牌位契約
  - `conditional branch` → 條件分支
  - `follow-up reading` → 補占／後續占問
  - `cross-validation` → 交叉驗證
  - `real-world verification` → 現實驗證
