# 占卜輸入契約（Input Contract）

本章定義一個占卜題目在抽牌／起卦前，最低限度應保存哪些資訊。目的不是把占卜變成表單，而是避免後續因上下文缺失、牌位漂移或起卦規則不明而無法回看。

## 1. 最小輸入欄位

建議至少記錄：

```text
question:        實際要判斷的問題
question_type:   比較 / 時間 / 流程 / 原因 / 人物 / 狀態 / 校正
subject:         誰／什麼是主要判斷對象
horizon:         時間範圍；若不適用寫 N/A
completion_rule: 何種現實事件才算「發生／完成」
method:          Tarot / Meihua / Tarot+Meihua
context_facts:   已確認、會改變判斷的現實資訊
exclusions:      明確不要求判斷的事項
```

若使用塔羅，再補：

```text
deck:            牌組；未指定時標示預設系統
reversals:       是否使用逆位
spread:          牌陣或自訂牌位
positions:       每一牌位的唯一語意
cards_source:    使用者提供 / 實體抽牌 / tarot-plum-randomizer / 其他工具
seed_or_record:  若工具支援可重現亂數，保存 seed 或 draw id
```

若使用梅花易數，再補：

```text
casting_source:  時間 / 數字 / 聲音 / 物象 / 方位 / 外應 / tarot-plum-randomizer / 其他
casting_rule:    此次實際採用的算法
calendar_rule:   若使用時間起卦，記錄曆法與時辰／跨日慣例
raw_input:       原始時間、數字或外應資料
perspective:     體／用與吉凶相對於誰、哪個事件與何種有利方向判定
```

`tarot-plum-randomizer` 指配套專案 [`masini1491/tarot-plum-randomizer`](https://github.com/masini1491/tarot-plum-randomizer)。若工具未提供 seed 或 draw id，也至少應保存題目、時間與實際抽牌／起卦結果。

若 `casting_source = tarot-plum-randomizer`，應把工具當次產生的 A、B 原始數字與其顯示的雙數起卦規則一併視為該卦的 canonical input；解讀端不應另行取數或切換起卦法。

## 2. 背景與真正問題必須分開

背景資訊可以很多，但真正問題只能有一個主要判斷功能。

錯誤：

> 我現在工作很忙、主管如何、公司十月調薪、也可能轉職，請看會不會升職、加多少、何時離職、去哪家公司。

較佳做法：

- `context_facts` 保存背景。
- `question` 只問這一輪真正要判斷的事。
- 其他問題拆成後續階段。

## 3. 預測題必須有時間範圍

凡涉及「會不會發生／何時發生」，至少要定義：

- 起始時間；
- 結束時間或候選窗口；
- 何種現實事件算完成。

「今年會不會跳槽」仍可能太模糊，因為「開始看職缺」與「新公司報到」是不同事件。

## 4. 牌位／起卦契約必須在結果出現前固定

### 塔羅

牌位語意先寫，再抽牌。

### 梅花易數

起卦來源、算法與判斷視角先寫，再看卦。

看到結果後才改規則，等同改變題目。

## 5. 可重現性

若工具能保存亂數種子（seed）、抽牌紀錄識別碼（draw id）、時間戳、原始數字或起卦算法，應一併保存。

這不是為了證明占卜具有客觀預測力，而是為了：

- 避免「重抽到滿意為止」；
- 能回查同一結果是否被不同方式重新解讀；
- 區分「同一題重占」與「新事實出現後的新題」。

## 6. 新問題與重問的判斷

符合任一條件，可視為新題：

- 現實前提已改變；
- 原本的大問題被拆成新的子問題；
- 時間窗或完成判定規則（completion rule）被明確重定義；
- 原題存在可指出的牌位／起卦契約錯誤。

若只是換句話，但核心判斷、前提與時間窗都沒變，仍視為同一題。

## 7. 建議保存格式

```yaml
question: "..."
question_type: comparison
subject: "..."
horizon: "2026-09-01 to 2026-12-31"
completion_rule: "..."
method: tarot
context_facts:
  - "..."
exclusions:
  - "不判斷結果好壞，只比較發生可能性"
tarot:
  deck: RWS-compatible
  reversals: true
  spread: custom-5
  positions:
    1: option-a-likelihood
    2: option-b-likelihood
    3: option-c-likelihood
    4: option-d-likelihood
    5: adjudicator
  cards_source: tarot-plum-randomizer
```

梅花易數若需要保存完整視角，可寫成：

```yaml
method: meihua
meihua:
  casting_source: tarot-plum-randomizer
  casting_rule: "A÷8→上卦；B÷8→下卦；(A+B)÷6→動爻；餘0分別視為坤／第6爻"
  raw_input: "574, 393"
  perspective:
    subject: "求問者本人"
    event: "正式收到 offer"
    favorable_means: "事件朝正式取得 offer 推進"
```

上方 YAML 是供工具與代理辨識的技術欄位，因此保留英文鍵名；其語意與使用規則以本文件的繁中說明為準。

這份結構化紀錄是後續解讀、交叉驗證與案例研究的共同輸入。
