# 塔羅 × 梅花易數提問設計實戰手冊

一套可重用的 **塔羅（Tarot）＋梅花易數（Meihua Yishu）提問設計、占問生命週期與 ChatGPT 解讀治理方法論**。

本儲存庫不以整理完整牌義、卦辭或宣稱「算得準」為主要目的，而是處理更前面的問題：

> **怎麼把模糊、混合、容易被解讀污染的問題，改寫成可比較、可追蹤、可驗證、低歧義的占卜題目；並讓 ChatGPT 在承接、補占、現實更新與回測時仍維持原契約？**

本手冊把占卜視為**象徵性、反思性與結構化推理工具**；現實決策仍應以可驗證資訊、專業意見與實際條件為優先。

## 這套手冊主要解決什麼

常見失敗包括：

- 同一牌位同時承擔「發生可能性、好壞、滿意度、後果」多種功能。
- 把「牌很漂亮／卦很吉」直接當成事件機率最高。
- 尚未確認主分支，就繼續追問分支內的數值、時間或細節。
- 因不喜歡第一次結果而反覆重抽／重卦。
- 把同一卦批次套用到彼此獨立的新問題。
- 塔羅與梅花易數彼此硬投票，而沒有先分工。
- 把啟動、轉折、決策、完成等不同事件層級混在同一時間題。
- ChatGPT 把象徵推論講成已確認事實，或回答原題 `exclusions` 已排除的內容。
- 承接前占時，把「前一組較支持 X」逐步滑成「X 已經會發生」。
- 回測時用前置信號替代原本 `completion_rule`，或把事後重讀冒充當時主結論。
- 多人物平行題只給一份模板，要求使用者自行換名字。

## 核心原則

### 1. 牌位先有契約，才抽牌

每一牌位只能有清楚、可回查的主要功能。

例如比較四個薪資區間時，要先決定比較的是：

- 實際發生的相對可能性；
- 發生後的情境品質；
- 背後意圖；

不能抽完後再依牌面改功能。

### 2. 發生可能性不等於情境品質

> **最正面的牌，不必然等於最可能發生。**

若題目是純比較，應明確限制各選項只比較「實際落地的相對可能性」。

### 3. 先判斷主分支，再問分支細節

如果 B 問題成立依賴 A 問題，先處理 A。

若只是想分析「假設 A 成立時」的內部情況，而 A 尚未被現實確認，使用**條件世界（Conditional World）**，不要把 A 偷偷升格成事實。

### 4. 一題只保留一個主要判斷功能

「會不會、何時、為什麼、好不好、怎麼辦」通常應拆題，而不是全部塞進同一牌陣／同一卦。

### 5. 占問有生命週期，不只是一次抽牌

一次預測通常會經過：

```text
QUESTION DRAFT
  ↓
CONTRACT FIXED
  ↓
DRAW / CAST
  ↓
INTERPRETED
  ↓
WAITING FOR REALITY
  ├─ 新現實資訊 → 新 judgment node
  ├─ 明確 unresolved function → 合法 follow-up
  └─ completion rule / horizon 可判定 → RESOLVED
        ↓
      BACKTEST（需要時）
```

完整規則見 [`READING_LIFECYCLE.md`](READING_LIFECYCLE.md)。

### 6. 塔羅與梅花先分工，再交叉驗證

預設：

- **塔羅**：選項比較、人物／關係動態、事件流程、阻礙、相對適配度。
- **梅花易數**：事件結構、主客／體用、轉折、動爻、外應與應期。

交叉驗證是 reconciliation，不是多一票。完整規則見 [`CROSS_VALIDATION.md`](CROSS_VALIDATION.md)。

### 7. 輸入契約先於解讀

抽牌／起卦前至少固定：

- `question`
- `question_type`
- `subject`
- `horizon`
- `completion_rule`
- `context_facts`
- `exclusions`
- 塔羅牌位／牌面來源，或梅花起卦來源／算法／原始輸入／判斷視角

完整欄位見 [`INPUT_CONTRACT.md`](INPUT_CONTRACT.md)。

### 8. ChatGPT 的輸出也要有契約

ChatGPT 必須：

- 守住原題與 `exclusions`；
- 區分已確認現實事實、抽牌／起卦事實、方法規則與象徵推論；
- 證據不足時允許 `UNRESOLVED`／「無法可靠區分」；
- 不把塔羅／梅花直接換算成偽精確百分比；
- 只有原題需要時才輸出心理、時間、建議或補占；
- 送出前做 bounded Pre-Send check。

若產生讓使用者自己抽牌／起卦的正式題目：

> **One Question = One Copy Surface。**

多人物平行題即使只有名字不同，也必須每個人物完整展開一題，不要求使用者自行替換名稱。

完整規則見 [`CHATGPT_OUTPUT.md`](CHATGPT_OUTPUT.md)。

## 文件架構

| 文件 | 主要責任 |
| --- | --- |
| [`CHAT_INIT.md`](CHAT_INIT.md) | 新聊天室最小 bootstrap、Context admission、task routing |
| [`INPUT_CONTRACT.md`](INPUT_CONTRACT.md) | 抽牌／起卦前要保存哪些題目與方法輸入 |
| [`QUESTION_DESIGN.md`](QUESTION_DESIGN.md) | 問題怎麼拆、牌位怎麼定、高頻 Question Patterns |
| [`READING_LIFECYCLE.md`](READING_LIFECYCLE.md) | 新題、承接、條件世界、補占、重占、現實更新、完成、horizon、回測 |
| [`TAROT.md`](TAROT.md) | Tarot-specific 牌位、牌陣與解讀規則 |
| [`MEIHUA.md`](MEIHUA.md) | Meihua-specific 起卦、主互變、體用、動爻、外應與應期 |
| [`CROSS_VALIDATION.md`](CROSS_VALIDATION.md) | Tarot × Meihua 分工、同題對齊、衝突 reconciliation |
| [`CHATGPT_OUTPUT.md`](CHATGPT_OUTPUT.md) | ChatGPT 出題／解讀、信心語言、Copy-ready、Pre-Send |
| [`CASE_STUDIES/`](CASE_STUDIES/) | Cold：匿名失敗案例與方法演進 |
| [`references/`](references/) | Cold：外部 GitHub 來源、採用狀態、授權、authority boundary |
| [`AGENTS.md`](AGENTS.md) | 薄 governance / maintenance router |

## AI 最小讀取方式

不要每次完整掃描全部文件。從 `CHAT_INIT.md` 進入，再依工作 bounded-read：

- **出新題** → `INPUT_CONTRACT` + `QUESTION_DESIGN` + `CHATGPT_OUTPUT` 出題 sections
- **一般塔羅解讀** → `TAROT` + `CHATGPT_OUTPUT` 解讀 sections
- **一般梅花解讀** → `MEIHUA` + `CHATGPT_OUTPUT` 解讀 sections
- **承接／補占／重占／現實更新／回測** → 再加入 `READING_LIFECYCLE`
- **塔羅＋梅花整合** → 再加入 `CROSS_VALIDATION`
- `CASE_STUDIES/`、`references/`、未被指定的舊占預設不載入

資訊被保存，不代表每一題都要付 Context cost。

## 高頻實戰模式

`QUESTION_DESIGN.md` 目前包含可重用模式：

- 主分支 → 分支細節
- 條件世界
- 已發生事件分析
- 承接前占但不重新比較
- 多人物／多對象平行題
- 純時間窗比較
- 現實事件出現後由抽象題切換成具體題

生命週期身份與是否能另抽，仍由 `READING_LIFECYCLE.md` 判定。

## 配套抽牌／起卦工具

本手冊可搭配 **Tarot + Plum Randomizer**：

- 線上工具：`https://tarot-plum-randomizer-masini1491-9205.vercel.app/`
- Repo：`https://github.com/masini1491/tarot-plum-randomizer`

目前工具支援：

- 單題塔羅 1～24 張
- 多題連續塔羅，每題獨立重新洗完整 78 張牌組
- 正／逆位隨機、單題內不重複
- 精簡牌名輸出，例如 `杯后正`、`劍七逆`、`命輪正`
- 梅花易數雙數起卦：A÷8→上卦、B÷8→下卦、(A+B)÷6→動爻，餘 0 視為坤／第 6 爻
- 顯示 A／B、上卦、下卦、動爻與本卦
- 同題可同時抽塔羅＋梅花
- 一鍵複製題目、時間與結果
- 手機版響應式排版

責任分工：

- **本手冊**：怎麼問、怎麼維持契約、怎麼承接／回測、怎麼控制 ChatGPT。
- **Tarot + Plum Randomizer**：怎麼隨機抽牌／起卦與格式化結果。

若 `casting_source = tarot-plum-randomizer`，其當次 A／B 與固定雙數算法是 canonical casting input；解讀端不得重取數或改換起卦法。

## 外部來源與案例

主文件只保存已被整理成穩定、可執行的規則。

- `references/` 保存外部來源 dossier、ADOPTED / ADAPTED / REFERENCE-ONLY / REJECTED、授權與限制。
- `CASE_STUDIES/` 保存匿名化失敗案例，用來說明「為什麼規則存在」。

兩者預設都是 Cold Context，不因存在就每次載入。

## 本手冊不保存什麼

這是公開方法論 repository，因此不保存：

- 真實姓名與可識別感情／關係細節
- 出生日期、時間與地點等可識別資料
- 健康、性相關私人紀錄
- 私人公司未公開人事、薪資、客戶或專案資訊
- 完整私人占卜日誌
- secrets / credentials

案例一律匿名化，只保留足以說明方法問題的最低必要結構。

## 與一般塔羅／梅花專案的差異

GitHub 上已有許多抽牌、起卦、牌義、卦義或 AI 解讀專案；本 Repo 專注在另一層：

> **題目設計 / 輸入契約 / Question identity / Reading lifecycle / ChatGPT output governance / Cross-validation / Backtest discipline**

也就是不只「怎麼解」，而是讓一個問題從提出、抽牌、承接到現實驗證都保持可追蹤、低歧義。

## 狀態

持續演進中。優先從真實使用中反覆出現的題型、生命週期與輸出失敗案例反向萃取規則，而不是追求文件數量或堆疊更多象徵資料庫。
