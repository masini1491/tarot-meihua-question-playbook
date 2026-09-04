# 新聊天室初始化（Chat Initialization）

本檔只負責建立新聊天室的最低必要讀取起點，不重複保存完整占卜規則。

## 啟動順序

處理本手冊相關的出題、解牌、解卦、承接、補占、Runtime Draw、正式保存或回測時：

1. 先確認目前任務是：方法選擇、出題、塔羅解讀、梅花解讀、塔羅＋梅花交叉、承接／補占、現實更新、ChatGPT 自行抽牌／起卦、正式 Reading Record、舊占回測，或外部 reference 研究。
2. 若使用者**尚未指定 Tarot／Meihua／Both**，而本次需要決定占卜方法，先讀 `METHOD_ROUTING.md`，依主要 judgment function 完成 Method Selection Gate；不要先問流派再把問題硬塞進去，也不要預設 Both。
3. 先建立**當前有效 Context**：以使用者本次訊息、已確認現實事實，以及使用者明確指定要承接的前占為主；其他未被引用的舊占、舊聊天室結論與歷史紀錄預設視為 Historical，不因存在就自動載入或影響本題。
4. 做最低充分 **Contract Admission Check**：
   - 設計／重寫新題，或題目缺少／混淆 `subject`、`horizon`、`completion_rule`、牌位、起卦規則、`exclusions` 等關鍵契約時，讀 `INPUT_CONTRACT.md`。
   - 若使用者已提供清楚完整的題目、牌位／卦象契約與實際牌面／卦象，直接依該契約處理；不要為形式每次完整重讀 `INPUT_CONTRACT.md`。
5. 若本次問題涉及「是不是新題、能不能承接／補占／重占、現實更新後怎麼轉題、是否已完成、怎麼回測」，讀 `READING_LIFECYCLE.md` 對應 section。
6. 若使用者要求 ChatGPT **自己抽牌／起卦**，而不是只產生題目讓使用者自行抽，讀 `RUNTIME_DRAW.md`；必須先確認實際 runtime capability，再執行 canonical Randomizer，不能用模型自行報牌冒充抽牌。
7. 若使用者要求**正式保存本次占卜、跨聊天室延續、建立 audit trail 或後續回測紀錄**，讀 `READING_RECORD.md`；只保存當時 Contract、Draw/Cast Fact、Original Interpretation 與後續追加層，不把私人日誌內容寫回本公開 Repo。
8. 依下方路由只讀本次任務最低必要主題文件；`CHATGPT_OUTPUT.md` 有 Section Router，優先 bounded-read 對應 section，不預設全文載入。
9. 先讀最能否決後續工作的高槓桿前提：若方法選擇、題目契約、條件分支、完成定義、方法來源或 Runtime Draw capability 本身已不成立，先指出問題，不要先花大量 Context 完整解讀後才回頭修正前提。
10. 不為了「熟悉手冊」預設完整掃描所有文件、`references/`、案例或歷史紀錄。
11. 若使用者已提供實際牌面／卦象，直接處理既有結果；不要為了完整性自行重抽、重卦或改用另一套方法。

## 最低必要路由

- **未指定方法／請 ChatGPT 判斷用什麼占**
  → `METHOD_ROUTING.md`；選定後再進對應的出題／方法／Runtime／輸出文件。
- **設計新題／重寫題目**
  → 若方法未定先 `METHOD_ROUTING.md`；之後 `INPUT_CONTRACT.md` + `QUESTION_DESIGN.md` + `CHATGPT_OUTPUT.md` 的出題／Copy-ready／Pre-Send sections；若是承接／條件世界再補 `READING_LIFECYCLE.md`。
- **塔羅解讀**
  → `TAROT.md` + `CHATGPT_OUTPUT.md` 的解讀／Pre-Send sections；只有契約缺失時補讀 `INPUT_CONTRACT.md`，涉及承接／完成／回測時才讀 `READING_LIFECYCLE.md`。
- **梅花易數解讀**
  → `MEIHUA.md` + `CHATGPT_OUTPUT.md` 的解讀／Pre-Send sections；只有契約缺失時補讀 `INPUT_CONTRACT.md`，涉及承接／完成／回測時才讀 `READING_LIFECYCLE.md`。
- **塔羅＋梅花交叉驗證**
  → `TAROT.md` + `MEIHUA.md` + `CROSS_VALIDATION.md` + `CHATGPT_OUTPUT.md`；若兩次占問之間有新現實資訊或不同 judgment node，再讀 `READING_LIFECYCLE.md`。
- **ChatGPT 自行抽牌／起卦**
  → 若方法未定先 `METHOD_ROUTING.md`；再完成／確認 Input Contract，讀 `RUNTIME_DRAW.md`；若成功取得 runtime result，依方法讀 `TAROT.md`／`MEIHUA.md`，最後依 `CHATGPT_OUTPUT.md` 解讀與呈現。
- **正式保存／跨聊天室承接／audit trail**
  → `READING_RECORD.md` + 該次 `INPUT_CONTRACT.md` 必要欄位；若涉及 status、parent/child、completion 或 backtest，再加 `READING_LIFECYCLE.md`；Runtime Draw 紀錄需要 provenance 時再讀 `RUNTIME_DRAW.md`。
- **承接／補占／重占／現實更新**
  → `READING_LIFECYCLE.md` + 需要的新題設計／方法／輸出 sections；若新 judgment node 尚未指定方法，再加 `METHOD_ROUTING.md`；若由 ChatGPT 代抽，再加 `RUNTIME_DRAW.md`；若要正式保存新節點，再加 `READING_RECORD.md`。
- **舊占回測**
  → `READING_LIFECYCLE.md` 的 Backtest sections + 該次原始 Input Contract／原始題目紀錄 + 對應 `TAROT.md` 或 `MEIHUA.md` + `CHATGPT_OUTPUT.md` 的回測／Pre-Send sections；若需要產生正式回測紀錄，再加 `READING_RECORD.md`。
- **外部 GitHub 來源研究**
  → `references/README.md` + 必要來源 dossier；主規則只有在研究結果真的需要比較／修改時才讀。

## Context Admission｜舊占不預設進入當前題

預設把資訊分成兩類：

- **Active Context**：本次使用者訊息、已確認現實事實、本次題目／牌位／卦象，以及使用者明確指定「承接」的前占或必要前提。
- **Historical Context**：未被本題引用的舊占、舊排序、已失效時間窗、以前對其他人物／其他事件的結論、舊聊天室印象與 memory。

Historical Context 可以保存與回查，但 **Persistence ≠ default loading**。只有使用者明確承接／比較／回看、當前題以該前占作條件前提，或進行舊占回測時，才把特定歷史內容升為 Active Context。

不得只因某個舊結論曾被多次引用，就讓它在新獨立題中取得更高事實或預測權重。完整規則見 `READING_LIFECYCLE.md`。

## 權威順序

一般情況：

1. 使用者當次明確指示
2. 已確認的現實事實
3. 該次抽牌／起卦前固定的 Input Contract
4. 本 repository 最新主規則
5. 該次實際抽牌／起卦資料（含可信 Runtime Draw output）
6. 當時依契約做出的原始解讀
7. 外部 references
8. 舊聊天室印象／memory

新的現實事實可以更新下一題的前提，但不能回頭修改舊題當時已固定的牌位、完成規則或起卦方式。

核心原則：**先以最低充分 Context 建立正確當前題；方法未定時先選對方法，再固定契約；資訊被保存，不代表每一題都要載入；能執行程式也不代表方法論上已允許重抽；需要長期保存時，保留原 judgment node 並以 append-only 追加現實與事後重讀。**
