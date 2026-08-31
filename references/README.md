# references｜外部 GitHub 參考索引

此目錄保存外部 GitHub 專案的**來源摘要、可借鑑方法、採用狀態、差異與授權注意事項**。

核心規則仍以本 Repo 根目錄文件為準；這裡不是第二套規則來源。

## 使用原則

每個來源檔盡量回答：

1. 這個 Repo 是什麼？
2. 哪些內容與「問題設計／牌位契約／起卦治理」直接相關？
3. 哪些已被本 Playbook 吸收？
4. 哪些不採用或只列為候選？
5. 授權上能否直接複製內容，還是只能概念性參考？

## 已收錄

### Tarot

- [`arcanite.md`](arcanite.md) — question classification、position-specific semantics、deterministic context → LLM synthesis。
- [`metaphysics-synthesis-skill.md`](metaphysics-synthesis-skill.md) — Tarot input gate、draw discipline、spread selection、reading order、reversal discipline。
- [`tarot-mcp.md`](tarot-mcp.md) — AI spread recommendation、custom spread、session history、question-context-aware interpretation。
- [`tarot-prompt.md`](tarot-prompt.md) — 結構化 question/cards/positions/context prompt input。
- [`tarot-api.md`](tarot-api.md) — deck/spread/card-data 分離的工具架構參考。

### Meihua

- [`muyen-meihua-yishu.md`](muyen-meihua-yishu.md) — 起卦來源、雙數算法、重卦紀律、主互變、體用、外應、應期等。
- [`metaphysics-synthesis-skill.md`](metaphysics-synthesis-skill.md) — Meihua input gate、證據階層、外應與應期約束。
- [`plum-yi.md`](plum-yi.md) — 簡化取卦 App 的工具化方向。

## 採用標記

- **ADOPTED**：已整併成主規則。
- **ADAPTED**：吸收概念，但改寫成符合本 Playbook 的規則。
- **REFERENCE-ONLY**：保留參考，不直接成為規則。
- **REJECTED**：明確不採用，並記錄原因。

若來源日後更新，不應自動覆寫本 Playbook；先比較差異，再決定是否修改主規則。
