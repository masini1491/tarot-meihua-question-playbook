# 新聊天室初始化（Chat Initialization）

本檔只負責建立新聊天室的最低必要讀取起點，不重複保存完整占卜規則。

## Default Interaction Profile｜只給 Repo 也能直接使用

當使用者明確要求「依本 Repository／本 Playbook 規則進行占卜」，即視為啟用本節預設互動模式；使用者不需要另外貼完整初始化 Prompt，也不需要逐欄填寫 Input Contract。

預設規則：

1. 使用者可以直接用自然語言描述想占的事情；Agent 應先自行正規化題目與最低必要契約，不把 schema 當成使用者表單。
2. 若使用者沒有指定 Tarot／Meihua／Both，依 `METHOD_ROUTING.md` 自動選擇最適合的方法；single-method first，不預設 Both。
3. 若使用者沒有提供既有牌面／卦象，也沒有明確表示要自己抽牌／起卦，**預設由 ChatGPT／AI 代抽／代起卦**，並進入 `RUNTIME_DRAW.md` 的 Runtime Capability Gate。
4. 預設代抽不等於允許模型自行生成牌面。只有 canonical Runtime Draw 實際可執行時才執行；capability、canonical script 或結果可信度不成立時必須 fail closed。
5. 只有缺少的資訊會實質改變 question identity、主要 judgment function、horizon、completion rule、牌位責任、起卦方式或可否執行時，才向使用者澄清；不要為了形式追問已可由題意安全推導的欄位。
6. 不先向使用者介紹整套 Playbook、文件架構或方法清單；完成必要 routing 後直接處理問題。
7. 使用者當次明確指定的方法、抽牌來源、牌數、是否自行抽牌／起卦、輸出格式或其他有效限制，優先於本節預設值。
8. 若使用者已提供實際牌面／卦象，直接處理既有結果；不得因本節預設為 Runtime Draw 而重抽、重卦或改用另一套方法。

因此，啟用本 Repo 後，正常互動可以只有：

```text
使用者：我想占……
```

其餘方法選擇、Contract Admission、是否需要 Runtime Draw 與後續文件載入由本 Repo 的 routing 自動處理。

## Repository Access Policy｜最新版規則的取得方式

當本 Repository 被指定為本次占卜規則來源時，Agent 應以**能直接取得 GitHub canonical repository current content 的最低成本方式**讀取最新版，而不是依賴模型記憶、舊聊天室摘要或 cached wording。

存取優先序：

1. 若目前環境有可直接存取 GitHub repository 的 **connected GitHub tool／connector**，優先使用它讀取 `main` 上的 canonical 檔案與本次 routing 所需 sections。
2. 若 GitHub connector 不可用，而本 Repository 可公開存取，可改用 GitHub repository URL、raw content 或等價 Web access 取得最新內容。
3. 若上述方式都無法可靠取得 canonical current content，進入 **ACCESS BLOCKED**；不得用模型記憶、舊聊天、舊摘要或未驗證 cache 冒充目前 `main`。
4. 在 `ACCESS BLOCKED` 狀態下，若目前產品／環境支援 App、Plugin 或 Connector discovery，Agent 應優先建議使用者**安裝或連接 GitHub**；若環境能直接呈現官方 GitHub connector 的安裝／連接入口，可使用該入口，不要只給抽象說明。
5. 使用者完成 GitHub 連接後，應立即從本 Repository 的 canonical entrypoint 重新嘗試存取，先讀 `CHAT_INIT.md`，再依 routing 繼續；不要求使用者重新貼原問題或整份 Repo。
6. 若環境不支援 connector discovery、GitHub connector 不可取得、使用者不願連接，或連接後仍無法取得 canonical content，維持 `ACCESS BLOCKED` 並清楚說明限制；不要在未取得最新版的情況下繼續假裝依本 Playbook 執行。
7. 在建議 GitHub connector 之前，不要把「請使用者手動貼完整 Repository」當成第一個 recovery path；若之後只能靠手動提供內容，應只要求當前 task 最低必要的 canonical 檔案／section，而不是整庫複製。
8. Connector 可用不代表要完整掃描 Repository；仍依本檔 routing 只讀本次 task 的最低必要檔案／sections。
9. 已知 exact path／section 能唯一命中 canonical owner 時直接讀 target；不要為了形式先繞過 README、目錄或其他中繼文件。
10. Public Web fallback 只改變**存取機制**，不改變 authority：本 Repository 最新 canonical content 仍是同一規則來源。

簡化為：

```text
GitHub connector
  ↓ unavailable
GitHub public / raw / Web
  ↓ unavailable
ACCESS BLOCKED
  ↓ connector discovery supported
Suggest install / connect GitHub
  ↓ connected
Retry CHAT_INIT → bounded routing
  ↓ still unavailable / declined
Remain ACCESS BLOCKED
```

核心原則：**Access mechanism may fall back; canonical authority may not fall back to memory。**

## 啟動順序

處理本手冊相關的出題、解牌、解卦、承接、補占、Runtime Draw、正式保存或回測時：

1. 先確認目前任務是：方法選擇、出題、塔羅解讀、梅花解讀、塔羅＋梅花交叉、承接／補占、現實更新、ChatGPT 自行抽牌／起卦、正式 Reading Record、舊占回測，或外部 reference 研究。
2. 若使用者**尚未指定 Tarot／Meihua／Both**，而本次需要決定占卜方法，先讀 `METHOD_ROUTING.md`，依主要 judgment function 完成 Method Selection Gate；不要先問流派再把問題硬塞進去，也不要預設 Both。
3. 先建立**當前有效 Context**：以使用者本次訊息、已確認現實事實，以及使用者明確指定要承接的前占為主；其他未被引用的舊占、舊聊天室結論與歷史紀錄預設視為 Historical，不因存在就自動載入或影響本題。
4. 做最低充分 **Contract Admission Check**：
   - 設計／重寫新題，或題目缺少／混淆 `subject`、`horizon`、`completion_rule`、牌位、起卦規則、`exclusions` 等關鍵契約時，讀 `INPUT_CONTRACT.md`。
   - 若使用者已提供清楚完整的題目、牌位／卦象契約與實際牌面／卦象，直接依該契約處理；不要為形式每次完整重讀 `INPUT_CONTRACT.md`。
5. 若本次問題涉及「是不是新題、能不能承接／補占／重占、現實更新後怎麼轉題、是否已完成、怎麼回測」，讀 `READING_LIFECYCLE.md` 對應 section。
6. 若使用者明確要求 ChatGPT **自己抽牌／起卦**，或已啟用本檔 Default Interaction Profile 且使用者未提供既有結果、未明確選擇自行抽牌／起卦，讀 `RUNTIME_DRAW.md`；必須先確認實際 runtime capability，再執行 canonical Randomizer，不能用模型自行報牌冒充抽牌。
7. 若使用者要求**正式保存本次占卜、跨聊天室延續、建立 audit trail 或後續回測紀錄**，讀 `READING_RECORD.md`；只保存當時 Contract、Draw/Cast Fact、Original Interpretation 與後續追加層，不把私人日誌內容寫回本公開 Repo。
8. 依下方路由只讀本次任務最低必要主題文件；`CHATGPT_OUTPUT.md`、`READING_LIFECYCLE.md` 與 `RUNTIME_DRAW.md` 有 Section Router 時，優先 bounded-read 對應 section，不預設全文載入。
9. 先讀最能否決後續工作的高槓桿前提：若方法選擇、題目契約、條件分支、完成定義、方法來源或 Runtime Draw capability 本身已不成立，先指出問題，不要先花大量 Context 完整解讀後才回頭修正前提。
10. 不為了「熟悉手冊」預設完整掃描所有文件、`references/`、案例或歷史紀錄。
11. 若使用者已提供實際牌面／卦象，直接處理既有結果；不要為了完整性自行重抽、重卦或改用另一套方法。

## 最低必要路由

- **未指定方法／請 ChatGPT 判斷用什麼占**
  → `METHOD_ROUTING.md`；選定後再進對應的出題／方法／Runtime／輸出文件。
- **設計新題／重寫題目**
  → 若方法未定先 `METHOD_ROUTING.md`；之後 `INPUT_CONTRACT.md` + `QUESTION_DESIGN.md` + `CHATGPT_OUTPUT.md` 的出題／Copy-ready／Pre-Send sections；若是承接／條件世界再補 `READING_LIFECYCLE.md`。
- **塔羅解讀**
  → `TAROT.md` + `CHATGPT_OUTPUT.md` 的解讀／Pre-Send sections；只有契約缺失時補讀 `INPUT_CONTRACT.md`，涉及承接／完成／回測時才讀 `READING_LIFECYCLE.md`。
- **梅花易數解讀**
  → `MEIHUA.md` + `CHATGPT_OUTPUT.md` 的解讀／Pre-Send sections；只有契約缺失時補讀 `INPUT_CONTRACT.md`，涉及承接／完成／回測時才讀 `READING_LIFECYCLE.md`。
- **塔羅＋梅花交叉驗證**
  → `TAROT.md` + `MEIHUA.md` + `CROSS_VALIDATION.md` + `CHATGPT_OUTPUT.md`；若兩次占問之間有新現實資訊或不同 judgment node，再讀 `READING_LIFECYCLE.md`。
- **ChatGPT 自行抽牌／起卦／Default Interaction Profile 預設代抽**
  → 若方法未定先 `METHOD_ROUTING.md`；再完成／確認 Input Contract，讀 `RUNTIME_DRAW.md`；若成功取得 runtime result，依方法讀 `TAROT.md`／`MEIHUA.md`，最後依 `CHATGPT_OUTPUT.md` 解讀與呈現。
- **正式保存／跨聊天室承接／audit trail**
  → `READING_RECORD.md` + 該次 `INPUT_CONTRACT.md` 必要欄位；若涉及 status、parent/child、completion 或 backtest，再加 `READING_LIFECYCLE.md`；Runtime Draw 紀錄需要 provenance 時再讀 `RUNTIME_DRAW.md`。
- **承接／補占／重占／現實更新**
  → `READING_LIFECYCLE.md` + 需要的新題設計／方法／輸出 sections；若新 judgment node 尚未指定方法，再加 `METHOD_ROUTING.md`；若由 ChatGPT 代抽，再加 `RUNTIME_DRAW.md`；若要正式保存新節點，再加 `READING_RECORD.md`。
- **舊占回測**
  → `READING_LIFECYCLE.md` 的 Backtest sections + 該次原始 Input Contract／原始題目紀錄 + 對應 `TAROT.md` 或 `MEIHUA.md` + `CHATGPT_OUTPUT.md` 的回測／Pre-Send sections；若需要產生正式回測紀錄，再加 `READING_RECORD.md`。
- **外部 GitHub 來源研究**
  → `references/README.md` + 必要來源 dossier；主規則只有在研究結果真的需要比較／修改時才讀。

## Context Admission｜舊占不預設進入當前題

預設把資訊分成兩類：

- **Active Context**：本次使用者訊息、已確認現實事實、本次題目／牌位／卦象，以及使用者明確指定「承接」的前占或必要前提。
- **Historical Context**：未被本題引用的舊占、舊排序、已失效時間窗、以前對其他人物／其他事件的結論、舊聊天室印象與 memory。

Historical Context 可以保存與回查，但 **Persistence ≠ default loading**。只有使用者明確承接／比較／回看、當前題以該前占作條件前提，或進行舊占回測時，才把特定歷史內容升為 Active Context。

不得只因某個舊結論曾被多次引用，就讓它在新獨立題中取得更高事實或預測權重。完整規則見 `READING_LIFECYCLE.md`。

## 權威順序

一般情況：

1. 使用者當次明確指示
2. 已確認的現實事實
3. 該次抽牌／起卦前固定的 Input Contract
4. 本 repository 最新主規則
5. 該次實際抽牌／起卦資料（含可信 Runtime Draw output）
6. 當時依契約做出的原始解讀
7. 外部 references
8. 舊聊天室印象／memory

Default Interaction Profile 屬於本 Repository 的穩定預設，但只在使用者沒有給出相反的當次明確指示時生效；不得覆蓋第 1 順位的使用者指示。

新的現實事實可以更新下一題的前提，但不能回頭修改舊題當時已固定的牌位、完成規則或起卦方式。

核心原則：**啟用本 Repo 後，使用者可以直接自然語言提出占問；Agent 自動完成方法 routing、最低充分 Contract Admission 與預設 Runtime Draw。資訊被保存，不代表每一題都要載入；能執行程式也不代表方法論上已允許重抽；需要長期保存時，保留原 judgment node 並以 append-only 追加現實與事後重讀。**
