# Reference｜lizecheng2021-maker/metaphysics-synthesis-skill

Repo: https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill

License: MIT（以來源 Repo 當下 LICENSE 為準）

## 類型

跨系統 Agent Skill，涵蓋 Tarot、梅花易數、八字、六爻、風水等；特色是 input gate、method routing、固定 reading order、bounded evidence 與 verification signals。

## Tarot 可借鑑內容

### ADOPTED — Input gate

來源要求在解讀前確認：

- question
- spread
- deck
- reversals
- predictive horizon

本 Playbook 擴充成 `INPUT_CONTRACT.md`，並加入 completion rule、cards source、seed/draw record 等欄位。

### ADOPTED — 不重抽既有牌面

若使用者已提供牌面，直接解讀，不自行重抽。

本 Playbook 將此寫入 `TAROT.md`。

### ADAPTED — Spread selection by user need

來源將單牌、三牌、decision、relationship、five-card 等對應不同用途。

本 Playbook 不綁定特定固定牌陣，而吸收成：

> 先定義題型與輸出功能，再選最小充分 spread；必要時自訂牌位。

### ADOPTED — 先掃整組，再逐牌細讀

來源提醒先看 major/minor/court、花色、數字、人物朝向、重複象徵與 anchor card。

本 Playbook 吸收成 `TAROT.md` 的 reading order。

### ADOPTED — 逆位選一個主要模式

來源將逆位分成 blocked / internalized / excessive / delayed / shadow，並要求不要全部疊用。

本 Playbook直接納入。

### ADAPTED — Event / psychology / action / verification 分離

本 Playbook 擴充為固定四層輸出，避免把建議當預測。

## Meihua 可借鑑內容

### ADOPTED — Input gate 與 casting provenance

來源要求記錄起卦來源與 number rule，且多問題時只處理 central question。

本 Playbook納入：單一問題、新判斷節點、起卦來源、算法、原始輸入。

### ADAPTED — 主／互／變／體用／動爻／外應分層

來源對各層功能有明確分工。本 Playbook吸收成 evidence roles，而不宣稱其 hierarchy 是唯一傳統標準。

### ADOPTED — 外應不能覆蓋主要卦象結構

來源把外應定位成 who/where/how/when 的細化工具。

本 Playbook納入「外應只能細化，不應無證據翻盤」。

### ADOPTED — 應期的單位必須配合問題尺度

來源會依 hours/days/weeks/months 與現實 schedule 做對齊。

本 Playbook吸收為：應期不是看到數字就直接指定『幾天』，必須先看 horizon 與現實 checkpoint。

## 不直接採用

- 不把來源對體用／卦辭的特定優先序宣告成唯一正統。
- 不把 Tarot／Meihua 當作可客觀驗證的預測模型。
- 不直接複製完整 card meanings、八卦類象或術數資料庫。

## 已影響主文件

- `INPUT_CONTRACT.md`
- `TAROT.md`
- `MEIHUA.md`
- `CROSS_VALIDATION.md`
