# Method Routing｜塔羅／梅花／雙占選擇

本章只處理一件事：**當使用者尚未指定占卜方法時，ChatGPT 應如何依問題功能選擇 Tarot、Meihua，或 Tarot + Meihua。**

本章不負責牌位設計、起卦算法、解讀、補占或交叉驗證細節：

- 題目怎麼問 → `QUESTION_DESIGN.md`
- Tarot-specific → `TAROT.md`
- Meihua-specific → `MEIHUA.md`
- 兩套都已存在後怎麼整合 → `CROSS_VALIDATION.md`
- 新題／承接／補占／重占 → `READING_LIFECYCLE.md`
- ChatGPT 自行抽牌／起卦 → `RUNTIME_DRAW.md`

核心原則：

> **先判斷使用者真正想知道的 judgment function，再選方法；不是先選流派，再把問題硬塞進去。**

> **Single-method first。只有兩套方法能明確承擔不同功能時，才使用 Both。**

## 1. User Method Override｜使用者已指定方法

若使用者已明確指定：

- 「用塔羅」→ 使用 Tarot；
- 「用梅花」→ 使用 Meihua；
- 「兩個都看」→ 進入 Both Gate。

原則上尊重使用者選擇，不因 ChatGPT 個人偏好自行換方法。

只有當指定方法與問題功能明顯不合、無法依該方法形成乾淨契約，或方法本身在本次 workflow 不可用時，才應簡短指出限制並推薦更合適方法。

若使用者已提供實際牌面／卦象，直接依既有方法處理；不得為了「方法更適合」自行重抽、重卦或改系統。

## 2. Function Detection｜先辨識問題功能

方法選擇前，先辨識本題的**主要 judgment function**。

### 優先 Tarot

若主要功能是以下之一，優先使用 Tarot：

- 多選一／多情境的相對比較；
- 不同人物、對象、方案的比較；
- 人物可觀察反應、互動與關係動態；
- 主觀感受、心理／互動層面的象徵分析；
- 阻礙、助力、觸發因素；
- 選項適配度、決策面向；
- 可被拆成清楚牌位的事件流程；
- 已定義離散時間窗之間的相對比較。

快速提示：

> **哪一個／哪個人／怎麼反應／有哪些因素 → Tarot 優先。**

### 優先 Meihua

若主要功能是以下之一，優先使用 Meihua：

- 一件明確事件目前如何變化；
- 主客／自身與外部的結構；
- 體用關係；
- 關鍵轉折、哪裡開始變；
- 主卦 → 互卦 → 變卦的發展結構；
- 近程節奏、應期、事件 checkpoint；
- 問題本身由時間、數字、外應、聲音、物象等觸發，且起卦來源清楚。

快速提示：

> **事情怎麼變／轉折在哪／目前主客結構／何時進入下一階段 → Meihua 優先。**

## 3. Single-Method Sufficiency Gate｜單方法充分性

辨識主要功能後，先問：

> **一套方法是否已能乾淨回答本題主要功能？**

- 若 **是** → 使用單一方法。
- 若 **否** → 才進入 Both Gate。

不要因為題目重要、資訊很多、使用者焦慮、第一套結果不夠漂亮，或「兩套一起可能比較準」就自動使用 Both。

**問題同時碰到人物與時間，不代表一定要雙占。** 若其中一層只是附帶資訊，仍以主要 judgment function 決定單一方法。

## 4. Both Gate｜何時才使用 Tarot + Meihua

只有同時符合以下條件時，才建議兩者同時使用：

1. 本題確實包含兩個有價值、彼此可區分的 judgment functions；
2. 單一方法無法在不混淆牌位／卦象責任的情況下充分回答；
3. Tarot 與 Meihua 可以在抽牌／起卦前先寫出**不同責任**；
4. 兩套結果最後依 `CROSS_VALIDATION.md` reconciliation，而不是投票。

選擇 Both 前，必須能先完成：

```text
Tarot responsibility: <塔羅只回答什麼>
Meihua responsibility: <梅花只回答什麼>
```

若這兩行其實是同一句話的不同寫法，代表責任沒有真正分離，退回單一方法。

### 常見乾淨分工

```text
Tarot responsibility: 比較 A／B／C 哪個分支相對較突出
Meihua responsibility: 勝出／主要分支進入後的變化結構與轉折
```

```text
Tarot responsibility: 某人的可觀察互動反應與主動程度
Meihua responsibility: 整體事件的推進結構、轉折與節奏
```

```text
Tarot responsibility: 比較已定義時間窗的相對支持度
Meihua responsibility: 辨識主要窗口較像啟動、阻滯、轉折或完成
```

## 5. Both 的禁止理由

以下理由本身**不足以**選擇 Both：

- 想提高信心；
- 想讓第二套確認第一套；
- 第一套結果不喜歡；
- 第一套看起來不夠清楚；
- 想用兩套投票；
- 想得到更多資訊；
- 題目很重要；
- 想在兩套衝突時用其中一套翻盤。

核心規則：

> **Cannot state distinct responsibilities → do not use Both。**

## 6. Generic / Unspecified Request｜使用者只說「幫我占」

若使用者沒有指定方法，但問題功能已足以判斷，ChatGPT 應直接選擇，不需要每次反問「要塔羅還是梅花」。

預設：

- 泛用的當前問題、人物、選項、關係、狀態、決策 → Tarot；
- 明確的過程、轉變、策略節奏、轉折、應期 → Meihua；
- 兩個獨立功能都重要且能先分工 → Both。

只有在**不同方法會實質改變題目功能，而現有資訊不足以知道使用者真正想問哪一層**時，才做一次最小澄清。

例如「幫我看這件事」但完全沒有說想比較選項、看人物、看走向或看時機，才需要先問他真正想知道的結果。

## 7. Tie-breaker｜同時像 Tarot 又像 Meihua

若一題同時命中兩套方法，依以下順序裁決：

1. 使用者明確指定的方法；
2. 主要 judgment function；
3. 單方法是否已充分；
4. 是否能寫出兩套不同責任；
5. 無法形成清楚 Both responsibility 時，退回主要方法。

因此：

> **Both 是最後一個 routing 選項，不是資訊最多的預設選項。**

## 8. Method Selection 與題目設計分離

Method Routing 只決定「用哪套」。選完後才進行正式題目契約：

```text
RAW USER QUESTION
→ FUNCTION DETECTION
→ METHOD ROUTING
→ INPUT CONTRACT / QUESTION DESIGN
→ DRAW / CAST
→ INTERPRETATION
```

不要先抽牌／起卦，再根據結果反推「其實這題比較適合另一套」。

若題目本身有契約缺陷，先修題；方法選得對不能補救混亂的 `subject`、`horizon`、`completion_rule` 或牌位功能。

## 9. Runtime Draw 不影響方法選擇

是否能執行 Python 只決定 ChatGPT 能不能自行完成 Runtime Draw，不決定本題應使用 Tarot 還是 Meihua。

正確順序：

```text
先選方法
→ 固定題目／牌位／起卦契約
→ 若使用者要求代抽，再進 Runtime Capability Gate
```

不得因某一方法比較容易執行，就改選該方法。

## 10. 建議的 Agent-facing 最小輸出

方法選擇通常可以在內部完成，不必每次展示完整 routing reasoning。

若需要向使用者說明，最低充分格式：

```text
建議方法：Tarot
理由：本題核心是比較人物反應與互動差異，塔羅能以獨立牌位直接處理。
```

若使用 Both：

```text
建議方法：Tarot + Meihua
Tarot responsibility: <...>
Meihua responsibility: <...>
```

不要把方法選擇包裝成「哪一套比較準」；這是**問題功能與方法責任的匹配**。

## 11. Pre-Route Check

送入正式出題／抽牌前，快速確認：

- [ ] 使用者是否已指定方法？
- [ ] 主要 judgment function 是什麼？
- [ ] 一套方法是否已足夠？
- [ ] 若選 Both，是否能在結果出現前寫出兩套不同 responsibility？
- [ ] 是否只是為了確認、提高信心或取得更多票而加第二套？
- [ ] 是否已有實際牌面／卦象，因此不得重新 routing 成另一套？

核心原則：**Question intent first, method second; single-method first, Both only with distinct responsibilities。**
