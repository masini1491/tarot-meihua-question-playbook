# ChatGPT Runtime Draw｜程式抽牌／起卦治理

本章是 ChatGPT／AI 在具有實際程式執行能力時，**自行執行塔羅抽牌或梅花起卦**的主要 authority。

本章不實作 RNG，也不複製抽牌程式。Canonical implementation 由：

- `masini1491/tarot-plum-randomizer/randomizer.py`

維護。

核心原則：

> **Language-model generation ≠ random draw。**
>
> 模型能說出牌名，不代表已完成隨機抽牌；宣稱 Runtime Draw 必須有真正的 runtime execution result。

## 1. 何時可以使用 Runtime Draw

只有同時符合以下條件時，ChatGPT 才可宣告「自行抽牌／起卦」：

1. 使用者明確要求 ChatGPT 自己抽，或上下文已授權由 ChatGPT 代為抽牌／起卦。
2. 本次 execution environment 具有可實際執行 Python 的能力。
3. 能取得並執行 `tarot-plum-randomizer` 的 canonical Python implementation，或已有與該 implementation 明確同步且可驗證的本地副本。
4. 題目、牌位／起卦契約已在結果出現前固定。
5. 執行結果可以被保留為 `DRAW / CAST FACT`，而不是只留下模型重述。

若只是模型「隨機想一組牌」，不得標記為 Runtime Draw。

## 2. Runtime Capability Gate

ChatGPT 在第一次需要自行抽牌時，應做最低充分 capability check：

- Python 是否可執行；
- canonical `randomizer.py` 是否可取得／已載入；
- 必要標準庫是否可用；
- 程式能否完成一次 bounded smoke test。

不要為了能力盤點去掃描所有 runtime、compiler 或 sandbox 套件；只驗證本次真正需要的 Python capability。

若 execution environment 不可觀察或不可執行，不得因模型「通常能跑 Python」就假設本次可用。

## 3. Canonical Runtime Source

Runtime Draw 的 canonical implementation 是：

```text
masini1491/tarot-plum-randomizer/randomizer.py
```

Playbook 只保存治理規則，不另外維護一份 Python 抽牌程式，避免 Web、Python、Playbook 三份演算法 drift。

若 ChatGPT 取得的是 repo 某個 commit 的檔案，應在紀錄中保留該 commit SHA。GitHub 的 commit time 只代表**該程式版本提交時間**，不是抽牌時間。

若未能確認來源版本，可記 `runtime_source_commit: unknown`，但不得捏造 SHA。

## 4. Tarot Runtime Contract

Runtime Tarot 必須維持 Randomizer 的 canonical contract：

- 完整 78 張牌；
- 單題 1～24 張；
- 同一題不重複；
- 每個 question identity 都重新建立完整牌組並重新洗牌；
- 正／逆位固定啟用且每張獨立抽取；
- 多人物／多題平行抽牌時，每題是獨立 draw identity，不共用上一題剩餘牌組。

例如四個人物各抽 5 張，應形成四次獨立 shuffle，而不是一次洗牌後連抽 20 張分組。

## 5. Meihua Runtime Contract

若使用 Runtime Draw 起梅花，維持 canonical 雙數契約：

- A、B 各為 `000～999`；
- `A % 8` → 上卦；
- `B % 8` → 下卦；
- `(A+B) % 6` → 動爻；
- 八卦餘 0 → 坤；
- 動爻餘 0 → 第 6 爻。

Runtime result 中的 A／B、本卦、上下卦與動爻視為該次 canonical casting input。解讀端不得在看到卦象後重新取數、改用時間起卦或替換 A／B。

## 6. Preferred Invocation

有 Python runtime 時，建議直接執行 Randomizer CLI。

單題塔羅：

```text
python randomizer.py tarot --count 6 --format json --source-commit <SHA>
```

梅花：

```text
python randomizer.py plum --format json --source-commit <SHA>
```

塔羅＋梅花：

```text
python randomizer.py both --count 6 --format json --source-commit <SHA>
```

多題：

```text
python randomizer.py batch --counts 5,5,6,3 --format json --source-commit <SHA>
```

AI integration 優先使用 JSON，避免把人類排版重新解析成機械欄位。

## 7. Draw Timestamp｜抽牌時間

Runtime Draw 必須保存**實際程式執行當下**的時間，而且至少同時保留：

```text
generated_at_utc: <UTC ISO-8601>
generated_at_taipei: <Asia/Taipei ISO-8601, UTC+08:00>
timezone: Asia/Taipei
```

規則：

- `generated_at_utc` 由 runtime 在執行當下取得 UTC。
- `generated_at_taipei` 由同一個 UTC timestamp 用 IANA `Asia/Taipei` 轉換，不另外向模型猜時間。
- 回覆使用者時，至少顯示台灣時間；建議同時保留 UTC 供回查。
- 不得把 GitHub commit timestamp、檔案修改時間、聊天室訊息時間或模型聲稱的現在時間替代實際 runtime timestamp。

推薦使用者可見格式：

```text
抽牌時間（台灣）：2026/09/04 13:47:22 UTC+8
抽牌時間（UTC）：2026/09/04 05:47:22Z
```

若 Runtime 無法可信取得當下 UTC 時間，應標示 timestamp unavailable；不要自行補一個看似合理的時間。

## 8. GitHub Provenance｜程式版本時間與抽牌時間分離

若能連線 GitHub，代抽前建議同步取得 canonical `randomizer.py` 的最新可用 commit SHA，並可附該 commit timestamp 作為外部 provenance。

推薦記錄：

```text
runtime_source_commit: <SHA>
github_source_commit_time_utc: <GitHub commit time>
github_source_commit_time_taipei: <換算 Asia/Taipei>
```

GitHub commit timestamp 的用途只有：

- 證明本次抽牌使用哪個程式版本；
- 協助後續回測知道該版本何時進入 repository。

它**不能**作為本次抽牌發生的時間。若 GitHub 暫時不可用，但已有可信 canonical script，可繼續 Runtime Draw，將 `runtime_source_commit` 記為已知舊 SHA 或 `unknown`；不要因此捏造 GitHub 時間。

## 9. Provenance｜來源紀錄

使用 Runtime Draw 時，至少在內部／正式紀錄中保存：

```text
cards_source: chatgpt-runtime
runtime_tool: tarot-plum-randomizer-python
runtime_algorithm_version: <tool output>
runtime_source_commit: <known commit SHA or unknown>
generated_at_utc: <tool output>
generated_at_taipei: <tool output>
timezone: Asia/Taipei
```

梅花則可保存：

```text
casting_source: chatgpt-runtime
runtime_tool: tarot-plum-randomizer-python
runtime_algorithm_version: <tool output>
runtime_source_commit: <known commit SHA or unknown>
raw_input: A, B
generated_at_utc: <tool output>
generated_at_taipei: <tool output>
```

`chatgpt-runtime` 表示「ChatGPT 實際執行 canonical runtime tool」，不是「ChatGPT 自己用語言生成結果」。

## 10. 使用者可見的最低代抽回覆

若使用者選擇由 ChatGPT 代抽，回覆中至少包含：

```text
抽牌時間（台灣）：<runtime generated_at_taipei>
來源：tarot-plum-randomizer-python v<algorithm_version>
Randomizer commit：<runtime_source_commit>
塔羅／梅花實際結果：...
```

若篇幅允許，再補：

```text
抽牌時間（UTC）：<runtime generated_at_utc>
GitHub 版本時間（台灣）：<commit timestamp converted to Asia/Taipei>
```

時間與 provenance 必須先來自實際工具輸出／GitHub 資料，再由 ChatGPT 格式化；不能讓模型自行估計後填入。

## 11. DRAW / CAST FACT 與解讀分離

Runtime tool 的原始結果先固定，再開始解讀。

順序：

```text
Question Contract fixed
→ Runtime execution
→ Raw result captured
→ DRAW / CAST FACT fixed
→ Interpretation
```

不得邊解牌邊要求程式重抽，也不得看到不喜歡的結果後重新執行同一題。

若使用者要求保存紀錄，應優先保留實際 tool output 或等價結構化資料，而不是只保存最後的自然語言解讀。

## 12. Fail-Closed Fallback

如果 Runtime Draw 在本次環境不可用、canonical script 無法取得、程式執行失敗或結果無法可信解析：

- 不得假裝已執行；
- 不得由語言模型自行產生牌名來冒充抽牌；
- 不得偷偷改用另一套未宣告 RNG；
- 應改用 Web `tarot-plum-randomizer`，或請使用者自行抽牌後提供結果。

若 runtime 部分成功，例如 Tarot 成功、梅花失敗，應分開標示，不能把整組宣稱為完整 Runtime Draw。

## 13. Runtime Draw 不改變補占紀律

能快速執行 Python，不代表可以快速重抽。

所有：

- 同題／新題判斷；
- 承接前占；
- 條件世界；
- 補占／重占；
- 多人物 question identity；

仍必須服從 `READING_LIFECYCLE.md`。

**Execution availability does not create divination authority。** 有能力執行，只代表技術上可以抽，不代表方法論上已允許重抽。

## 14. Runtime Draw 與 Copy-ready 的關係

若使用者要求「你幫我出題，我自己抽」，依 `CHATGPT_OUTPUT.md` 提供 copy-ready 題目，不自動執行 Runtime Draw。

若使用者要求「你直接幫我抽」，才進入本章 Runtime Gate。

若使用者同時要求：

> 幫我設計題目並直接抽牌

應先完成題目／牌位契約，再執行；不能先抽牌再倒推題目。

## 15. 最低驗證

Canonical runtime tool 更新後，建議至少驗證：

- 78 張牌唯一；
- 單題無重複牌；
- count boundary 正確；
- 多題各自形成獨立 draw；
- 梅花 A/B 與動爻範圍正確；
- 64 卦 mapping 完整；
- JSON 可被正常解析；
- `generated_at_utc` 與 `generated_at_taipei` 代表同一瞬間；
- 台灣時間 offset 為 `+08:00`。

測試屬於 Randomizer repo 的 implementation responsibility；本 Playbook 只要求 Runtime Draw 不應依賴未驗證、來源不明的臨時抽牌片段。
