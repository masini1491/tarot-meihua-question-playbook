# 新聊天室初始化（Chat Initialization）

本檔只負責建立新聊天室的最低必要讀取起點，不重複保存完整占卜規則。

## 啟動順序

處理本手冊相關的出題、解牌、解卦或回測時：

1. 先確認目前任務是：出題、塔羅解讀、梅花解讀、塔羅＋梅花交叉、舊占回測，或外部 reference 研究。
2. 先建立**當前有效 Context**：以使用者本次訊息、已確認現實事實，以及使用者明確指定要承接的前占為主；其他未被引用的舊占、舊聊天室結論與歷史紀錄預設視為 Historical，不因存在就自動載入或影響本題。
3. 做最低充分 **Contract Admission Check**：
   - 設計／重寫新題，或題目缺少／混淆 `subject`、`horizon`、`completion_rule`、牌位、起卦規則、`exclusions` 等關鍵契約時，讀 `INPUT_CONTRACT.md`。
   - 若使用者已提供清楚完整的題目、牌位／卦象契約與實際牌面／卦象，直接依該契約處理；**不要為了形式每次都完整重讀 `INPUT_CONTRACT.md`**。
4. 依下方路由只讀本次任務最低必要主題文件；`CHATGPT_OUTPUT.md` 若有對應 Section Router，優先只讀相關 section，不預設全文載入。
5. 先讀最能否決後續工作的高槓桿前提：若題目契約、條件分支、完成定義或方法來源本身已不成立，先指出問題，不要先花大量 Context 完整解讀後才回頭修正前提。
6. 不為了「熟悉手冊」預設完整掃描所有文件、`references/`、案例或歷史紀錄。
7. 若使用者已提供實際牌面／卦象，直接處理既有結果；不要為了完整性自行重抽或重卦。

## 最低必要路由

- **設計新題／重寫題目**
  → `INPUT_CONTRACT.md` + `QUESTION_DESIGN.md` + `CHATGPT_OUTPUT.md` 的出題／Copy-ready／Pre-Send 相關 sections。
- **塔羅解讀**
  → `TAROT.md` + `CHATGPT_OUTPUT.md` 的解讀／Pre-Send 相關 sections；只有契約缺失或需正式校正時才補讀 `INPUT_CONTRACT.md`。
- **梅花易數解讀**
  → `MEIHUA.md` + `CHATGPT_OUTPUT.md` 的解讀／Pre-Send 相關 sections；只有契約缺失或需正式校正時才補讀 `INPUT_CONTRACT.md`。
- **塔羅＋梅花交叉驗證**
  → `TAROT.md` + `MEIHUA.md` + `CROSS_VALIDATION.md` + `CHATGPT_OUTPUT.md` 的解讀／Pre-Send 相關 sections；缺契約時才補讀 `INPUT_CONTRACT.md`。
- **舊占回測**
  → `CROSS_VALIDATION.md` + 該次原始 Input Contract／原始題目紀錄 + `CHATGPT_OUTPUT.md` 的回測／Pre-Send 相關 sections。
- **外部 GitHub 來源研究**
  → `references/README.md` + 必要來源 dossier；主規則只有在研究結果真的需要比較／修改時才讀。

## Context Admission｜舊占不預設進入當前題

預設把資訊分成兩類：

- **Active Context**：本次使用者訊息、已確認現實事實、本次題目／牌位／卦象，以及使用者明確指定「承接」的前占或必要前提。
- **Historical Context**：未被本題引用的舊占、舊排序、已失效時間窗、以前對其他人物／其他事件的結論、舊聊天室印象與 memory。

Historical Context 可以保存與回查，但**Persistence ≠ default loading**。只有下列情況才把特定歷史內容升為 Active Context：

- 使用者明確要求「承接／比較／回看」該次占卜；
- 當前問題本身以該前占結論作為條件前提；
- 舊占回測需要比對原題、原牌面與當時主結論。

不得只因某個舊結論曾被多次引用，就讓它在新獨立題中取得更高事實或預測權重。

## 權威順序

一般情況：

1. 使用者當次明確指示
2. 已確認的現實事實
3. 該次抽牌／起卦前固定的 Input Contract
4. 本 repository 最新主規則
5. 該次實際抽牌／起卦資料
6. 當時依契約做出的原始解讀
7. 外部 references
8. 舊聊天室印象／memory

新的現實事實可以更新下一題的前提，但不能回頭修改舊題當時已固定的牌位、完成規則或起卦方式。

核心原則：**先以最低充分 Context 建立正確當前題，再依原題與現實事實回答；資訊被保存，不代表每一題都要載入。**
