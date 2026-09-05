# Reading Record｜正式占卜紀錄格式

本章只處理一件事：**一個已完成抽牌／起卦並形成解讀的占問，若需要跨聊天室保存、後續承接、現實更新或回測，應如何留下可追蹤、可稽核、不可事後漂移的正式紀錄。**

本章不負責：

- 題目要保存哪些輸入欄位 → `INPUT_CONTRACT.md`
- 是否構成新題／能否補占／何時 resolved → `READING_LIFECYCLE.md`
- Tarot／Meihua 怎麼解 → `TAROT.md`／`MEIHUA.md`
- Runtime Draw provenance 怎麼產生 → `RUNTIME_DRAW.md`
- ChatGPT 最終怎麼說 → `CHATGPT_OUTPUT.md`

核心原則：

> **Record schema 負責忠實保存當時發生了什麼，不負責重新解釋它。**

> **Original interpretation 不因後來知道結果而覆寫；Reality update 與 retrospective interpretation 必須追加成新層。**

## 1. 何時需要正式 Reading Record

不是每次聊天都必須存檔。只有以下情況之一成立時，才值得建立正式紀錄：

- 使用者明確要求「記錄／保存這次占卜」；
- 本題有 `horizon`／`completion_rule`，未來需要現實驗證；
- 本題是後續 follow-up／conditional branch 的 parent；
- 本題之後可能進行 Backtest；
- 多人物／多時間窗／多方法比較需要保留原始契約；
- 使用者要跨聊天室延續同一 judgment node；
- 需要保留 Runtime Draw provenance 或 audit trail。

純即時反思、一次性聊天且沒有後續價值時，不要求為形式建立長期紀錄。

## 2. Stable Record Identity｜固定紀錄身分

正式紀錄應有穩定、唯一的 `reading_id`。

推薦使用可讀、低碰撞格式，例如：

```text
reading_id: 20260904-career-001
reading_id: 20260904-relationship-002
```

也可使用 UUID；重點是後續引用同一筆紀錄時不靠檔名猜測。

若本題承接既有紀錄，另保存：

```text
parent_reading_id: <id or null>
```

若關係不是單純 parent/child，可使用：

```yaml
related_readings:
  - reading_id: <id>
    relation: conditional_branch
  - reading_id: <id>
    relation: comparison_peer
```

`relation` 只是記錄關係，不自動賦予方法論上的承接權；是否能承接仍由 `READING_LIFECYCLE.md` 判斷。

### 2.1 Information Integrity Guards｜容器、衍生結論與來源精度

正式紀錄可以被 UI、batch、人物群組、時間窗比較或其他 physical container 包在一起，但 **container 不會合併其中各 reading 的 semantic identity 或 authority**。

- 多人物／多題／多時間窗若各自能被獨立詢問、驗證、更新、補占或回測，應各自保留 `reading_id`、question identity 與對應 Draw/Cast Fact；同一頁面、同一 JSON、同一 batch 或同一次輸出只代表 presentation／transport grouping。
- `container_id`、group label、batch id 等若外部系統需要可以另外保存，但它們不是其中 child reading 的替代 identity，也不能讓一筆 Reality Update 自動套到整個 group。
- Cross-validation、summary、ranking、comparison、digest、回顧表等由既有 readings 產生的內容預設是 **derived synthesis**。它可以新增分析／reconciliation 結論，但不得覆寫底層 Contract、Draw/Cast Fact、Reality Update，也不得在沒有新的 draw/cast／現實 observation 時製造新的 source-fact identity。
- Derived synthesis 若需長期保存，應保留足以回到各 source `reading_id` 的 pointer；若 synthesis 與 source record 衝突，回到各 canonical source layer reconciliation，不以較方便閱讀的總表靜默覆蓋原紀錄。
- 具有跨 session／未來 decision 持續價值的 confirmed fact，應保存在合理的 canonical evidence layer：題目既定事實在 Contract Fact、實際抽牌／起卦在 Draw/Cast Fact、後續可驗證現實在 Reality Update；不要讓聊天摘要、排行榜或 retrospective prose 成為唯一 de facto memory。
- Provenance 只保存實際可證明的 precision。只知道日期就不要補造時間，只知道來源 repo 不代表 commit SHA 已知；`unknown`／`unavailable`／`unverified` 應保持原狀。後來取得更高精度 metadata 可以追加或升級，但不得回寫成「當時已知」。

核心原則：**Container may group readings; it does not merge their identity or authority. Derived synthesis may add interpretation; it does not manufacture source facts. Preserve provenance precision。**

## 3. Lifecycle Status｜目前狀態

正式紀錄應保存一個 machine-readable `status`，方便跨聊天室快速判斷是否仍在等待現實。

建議值：

```text
interpreted
waiting_for_reality
resolved
unresolved
superseded_contract
reflective_only
```

語意：

- `interpreted`：已解讀，但不一定需要等待現實。
- `waiting_for_reality`：預測／時間／條件題，尚未到 completion 或 horizon 判定點。
- `resolved`：依 `completion_rule` 或 horizon 已可由現實判定。
- `unresolved`：期限已到或需判定，但現實證據不足。
- `superseded_contract`：原契約有明確缺陷，已建立修正版；舊紀錄保留但不再作主要判斷依據。
- `reflective_only`：純反思／象徵性探索，不建立現實預測完成責任。

狀態轉移由 `READING_LIFECYCLE.md` 判斷；本檔只負責保存結果。

## 4. Minimum Metadata｜最低 metadata

正式紀錄建議至少有：

```yaml
record_schema_version: "1"
reading_id: "..."
created_at: "<ISO-8601 with timezone>"
method: "tarot | meihua | tarot+meihua"
question_type: "..."
subject: "..."
horizon: "... | N/A"
completion_rule: "... | N/A"
status: "..."
parent_reading_id: null
```

若已有完整 Input Contract，不必在 metadata 重複所有細節；正文可直接保存原題、背景、exclusions、牌位／起卦契約。

## 5. Six Evidence Layers｜六層證據

正式紀錄應盡量把內容分成以下六層；沒有內容的層可以標示「尚無」，不必硬填。

### Layer 1 — QUESTION / CONTRACT FACT

保存**結果出現前已固定**的內容：

- 原始題目；
- `subject`；
- `horizon`；
- `completion_rule`；
- `context_facts`；
- `exclusions`；
- Tarot positions／Meihua casting contract；
- Both 時兩套 responsibility。

這層不能因後續結果或現實發展而回改。

### Layer 2 — DRAW / CAST FACT

保存實際抽牌／起卦結果本身。

Tarot：

```text
牌位 → 牌名 → 正／逆位
```

Meihua：

```text
raw input / A / B
本卦／互卦／變卦
動爻
體用（若已依契約固定）
```

若使用 Runtime Draw，保留必要 provenance；若使用者手抽，也應標明來源。

這層是 method input fact，不等於現實事實。

### Layer 3 — ORIGINAL INTERPRETATION

保存**當時第一次正式解讀**：

- 逐牌／逐層判讀；
- 當時主結論；
- 事前次級／條件分支；
- 當時認定的驗證訊號；
- 當時已明確保留的不確定性。

不得在知道後續結果後重寫這一層。

### Layer 4 — REALITY UPDATE

只保存後來**實際發生或可驗證的新事實**，並標日期／來源。

例如：

```text
2026-09-15：收到正式通知。
2026-09-22：實際見面。
```

Reality Update 不應偷塞新的象徵解讀；現實層與解讀層分開。

### Layer 5 — RETROSPECTIVE INTERPRETATION

知道後續現實後，如果重新看牌／卦發現新的可能語意，放在這一層。

必須明確標示：

> 這是事後重讀，不是當時已做出的預測。

### Layer 6 — BACKTEST JUDGMENT

依 `READING_LIFECYCLE.md` 的 Backtest Gate 對照：

- 原題／契約品質；
- 原牌／卦是否支持；
- 當時主結論；
- 事前次級分支；
- 實際結果；
- 是否命中／偏移／污染／UNRESOLVED。

Backtest 是評估層，不覆蓋前五層。

核心規則：

> **Interpretation is not reality evidence; retrospective insight is not original prediction。**

## 6. Append-Only｜後續更新以追加為主

已建立的正式紀錄原則上採 append-only：

- 新 Reality Update → 追加；
- 新 Retrospective Interpretation → 追加；
- 新 Backtest → 追加；
- 原始 Contract／Draw Fact／Original Interpretation → 不因後來結果覆寫。

若只是 typo、格式錯誤或明確資料轉錄錯誤，可以修正，但應留下最小更正註記；不能藉「修正」改變當時結論。

若原題契約本身有缺陷，依 `READING_LIFECYCLE.md` 建立新的修正版 reading；舊紀錄標 `superseded_contract`，不要刪除。

## 7. Runtime Provenance｜Runtime 紀錄

若 `cards_source = chatgpt-runtime` 或 `casting_source = chatgpt-runtime`，正式紀錄建議保存：

```yaml
runtime:
  tool: tarot-plum-randomizer-python
  algorithm_version: "1"
  schema_version: "2"
  source_commit: "<SHA or unknown>"
  generated_at_utc: "<ISO-8601 or unavailable>"
  generated_at_taipei: "<ISO-8601 or unavailable>"
```

詳細來源規則由 `RUNTIME_DRAW.md` 維護；本檔不重新定義演算法。

使用者可見的普通解讀不需要展示全部 provenance，但正式長期紀錄應盡量保存。

## 8. Human-Readable First｜人可讀，AI 也可解析

推薦格式是**薄 front matter + Markdown 正文**，而不是把整篇紀錄變成大型 YAML。

範例：

```markdown
---
record_schema_version: "1"
reading_id: "20260904-career-001"
created_at: "2026-09-04T16:09:00+08:00"
method: "meihua"
question_type: "process"
subject: "示例事件"
horizon: "2026-12-31"
completion_rule: "雙方正式達成條件並開始執行"
status: "waiting_for_reality"
parent_reading_id: null
---

# 示例事件｜梅花｜2026-09-04

## Contract

### 原始題目
...

### Exclusions
...

## Draw / Cast Fact
...

## Original Interpretation
...

## Original Conclusion
...

## Reality Updates
尚無。

## Retrospective Interpretation
尚無。

## Backtest
尚未到判定點。
```

這個格式只是建議，不要求所有外部儲存系統使用 Markdown；真正重要的是 identity、status、六層證據與 append-only 邊界。

## 9. Record Schema Version｜紀錄 schema 版本

`record_schema_version` 只代表**紀錄資料結構**，與 Randomizer 的 `algorithm_version`、`schema_version` 完全分開。

只有欄位語意／必要結構改變時才升版；純排版、範例文字或說明補強不需要升版。

目前：

```text
record_schema_version: 1
```

## 10. Legacy Records｜舊紀錄不強制重寫

已有歷史快照不需要為了符合新 schema 全部覆寫。

推薦做法：

```text
legacy record
→ 保留原文
→ 後續需要承接／回測時建立新 record 或 audit record
→ 用 reading_id／related_readings 指回舊來源
```

若外部系統想建立 machine-readable index，可以額外建立索引；不要為了補 metadata 改寫舊占當時的原始結論。

## 11. Storage-Agnostic Boundary｜與私人紀錄庫分離

本 Playbook 是公開方法論，不保存私人占卜日誌，也不規定私人 Vault 的目錄名稱、人物代稱或檔名策略。

`masini1491/tarot-meihua-question-playbook` **永遠不是 Reading Record 的合法儲存目的地**。對本 Repository 具有 `push`、`maintain`、`admin` 或其他寫入能力，只代表 technical capability，**不構成把占卜紀錄寫入本 Repo 的授權**。

因此，AI／Agent 必須遵守以下 storage boundary：

- 不得在本 Playbook 建立、追加或修改任何個人 Reading Record、Reality Update、Retrospective Interpretation、Backtest、占卜摘要或其他以「保存某次占問」為目的的資料。
- 使用者只說「記錄／保存這次占卜」，不代表可把本 Playbook 當成 fallback storage；即使目前只有本 Repo 可寫，也必須 fail closed，不得為了完成保存而寫入。
- 即使使用者明確要求把某筆占卜紀錄寫進本 Playbook，也應拒絕該 storage target，並改用使用者指定的外部私人紀錄庫；若沒有可用或已授權的外部目的地，則提供 copy-ready record 或請使用者指定目的地。
- 本 Repo 可以保存的是方法論、治理規則、匿名化且具有泛化價值的 case study／behavioral eval 等 Playbook 內容；不得把原始占卜紀錄偽裝成案例、測試資料、note 或其他檔名繞過此限制。
- 若某次占卜揭露值得回饋到 Playbook 的方法問題，只能把**去個資、去特定事件、可泛化的方法結論**另行整理成規則／案例；原 Reading Record 仍必須留在 Playbook 之外。

核心原則：**Write permission is capability, not authorization. Reading Records never live in the Playbook。**

外部紀錄庫可以自由決定：

- 依人物分目錄；
- 依主題／日期分目錄；
- 用 Markdown、SQLite、JSON 或其他格式；
- 是否另外建立 daily digest／index。

只要需要與本 Playbook 相容，應保留本章的核心語意：

```text
stable reading identity
+ lifecycle status
+ contract fact
+ draw/cast fact
+ original interpretation
+ reality update
+ retrospective interpretation
+ backtest judgment
+ append-only history
```

## 12. Pre-Save Check

正式保存前快速確認：

- [ ] 儲存目的地是否位於本 Playbook 之外？若 target 是 `masini1491/tarot-meihua-question-playbook`，必須停止寫入並改用外部紀錄庫或 copy-ready fallback。
- [ ] 是否有穩定 `reading_id`？
- [ ] 多 reading 被同一 batch／UI／檔案容器包住時，是否仍各自保留 identity，而不是用 container 取代？
- [ ] 是否保存方法、日期、subject、horizon／completion rule（若適用）？
- [ ] 原始 Contract 是否與結果分開？
- [ ] Draw / Cast Fact 是否忠實保存？
- [ ] Original Interpretation 是否仍是當時原版？
- [ ] Reality Update 是否只放現實事實？
- [ ] derived summary／cross-validation 是否仍可回到 source `reading_id`，且沒有覆蓋 source fact？
- [ ] provenance 的未知／不可得欄位是否保持 `unknown`／`unavailable`，沒有為了填滿 schema 猜值？
- [ ] 事後重讀是否放在 Retrospective Interpretation，而不是改寫原解？
- [ ] Backtest 是否沒有把 hindsight 冒充 prediction？
- [ ] 後續更新是否以 append-only 為原則？

核心原則：**Preserve the original judgment node; append reality and hindsight, never rewrite history。**
