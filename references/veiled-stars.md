# 參考來源｜SeithAsync/veiled-stars

Repo: https://github.com/SeithAsync/veiled-stars

授權：MIT（以來源 Repo 當下 LICENSE 為準）

Reviewed: 2026-09-04

## 類型

本地 Tarot journal / MCP server，特色是把原始牌陣、當次解讀、後續回顧與個人經驗結晶分層保存，並採 append-only 思路避免後見污染。

## 可借鑑內容

### ADAPTED｜調整後採用 — Evidence layer isolation

來源把原始經歷、當次解讀與後續經驗結晶分開，並明確避免「AI 解讀自己引用自己」成為新的現實證據。

本手冊已將此擴充成 `READING_LIFECYCLE.md` 的六層：

1. QUESTION / CONTRACT FACT
2. DRAW / CAST FACT
3. ORIGINAL INTERPRETATION
4. REALITY UPDATE
5. RETROSPECTIVE INTERPRETATION
6. BACKTEST JUDGMENT

### ADAPTED｜調整後採用 — Append-only history

來源的 interpretations、reflections 與 insight versions 不覆蓋舊內容。

本手冊採用相同治理方向：後來的重解、現實更新與回測應追加保存，不能覆蓋原契約或原始解讀。

### REFERENCE-ONLY｜僅供參考 — Evidence de-duplication

來源在個人經驗結晶中以原始 reading 作為樣本單位，避免把多段解讀、回顧或版本修訂重複算成多個證據樣本。

若未來本手冊建立正式資料庫／長期 reading ledger，可再吸收此設計。

## 不直接採用

- 不採用其 SQLite schema 作為本手冊現階段的必備資料格式。
- 不採用其固定牌陣、牌意資料庫或 UI。
- 不把個人經驗結晶當成客觀預測效度。

## 已影響主文件

- `READING_LIFECYCLE.md`
