# 新聊天室初始化（Chat Initialization）

本檔只負責建立新聊天室的最低必要讀取起點，不重複保存完整占卜規則。

## 啟動順序

處理本手冊相關的出題、解牌、解卦或回測時：

1. 先確認目前任務是：出題、塔羅解讀、梅花解讀、塔羅＋梅花交叉、舊占回測，或外部 reference 研究。
2. 先讀 `INPUT_CONTRACT.md` 與本次任務直接相關的最低必要主題文件。
3. 若需要 ChatGPT 產生題目或輸出解讀，讀 `CHATGPT_OUTPUT.md`。
4. 不為了「熟悉手冊」預設完整掃描所有文件。
5. 若使用者已提供實際牌面／卦象，直接處理既有結果；不要為了完整性自行重抽或重卦。

## 最低必要路由

- 設計新題／重寫題目
  → `INPUT_CONTRACT.md` + `QUESTION_DESIGN.md` + `CHATGPT_OUTPUT.md`
- 塔羅解讀
  → `TAROT.md` + `CHATGPT_OUTPUT.md`
- 梅花易數解讀
  → `MEIHUA.md` + `CHATGPT_OUTPUT.md`
- 塔羅＋梅花交叉驗證
  → `TAROT.md` + `MEIHUA.md` + `CROSS_VALIDATION.md` + `CHATGPT_OUTPUT.md`
- 舊占回測
  → `CROSS_VALIDATION.md` + 原始 Input Contract + `CHATGPT_OUTPUT.md`
- 外部 GitHub 來源研究
  → `references/README.md` + 必要來源 dossier

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

核心原則：**先讀最低必要規則，再依原題與現實事實回答；不要用舊聊天印象覆蓋當次契約。**
