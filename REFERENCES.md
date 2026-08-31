# References｜外部參考

本檔只整理與「提問設計、牌陣契約、起卦流程、AI 結構化占卜」相關的公開 GitHub 專案。引用不代表本手冊全盤採用其方法。

## Meihua Yishu

### `muyen/meihua-yishu`

- 類型：梅花易數 AI Skill＋計算工具＋案例／方法論。
- 可參考：起卦方式契約、雙數起卦、體用／變卦／應期流程、不要無因反覆占問、具體問題應先決定起卦方式。
- 注意：其部分方法包含現代擴充與特定流派選擇；本手冊若採用應明確標示，不視為唯一正統。
- Repo: https://github.com/muyen/meihua-yishu

### `lizecheng2021-maker/metaphysics-synthesis-skill`

- 類型：八字／梅花／六爻／風水／塔羅的綜合 Agent Skill。
- 可參考：方法路由、輸入契約、先分系統判斷再做 synthesis、驗證訊號與不確定性分層。
- Repo: https://github.com/lizecheng2021-maker/metaphysics-synthesis-skill

### `haoc0114/plum_yi`

- 類型：梅花易數取卦 App。
- 可參考：工具化起卦的簡化介面。
- Repo: https://github.com/haoc0114/plum_yi

## Tarot

### `eric32181630/tarot-prompt`

- 類型：前端 Tarot 抽牌＋結構化 LLM Prompt。
- 可參考：把問題、牌陣、正逆位與可選星盤資料序列化成固定輸入。
- Repo: https://github.com/eric32181630/tarot-prompt

### `howlCode/tarot_api`

- 類型：Tarot API，提供牌義與常見 spread。
- 可參考：把牌陣結構與牌資料分離；不直接解決 question-design governance。
- Repo: https://github.com/howlCode/tarot_api

## 本手冊的差異化

上述多數專案著重：

- 起卦／抽牌
- 牌義／卦義
- AI 解讀
- Agent Skill
- UI／API

本 Repo 聚焦：

> **問題怎麼拆、牌位怎麼定義、不同條件分支何時先後詢問、何時允許補占，以及 Tarot × Meihua 如何避免互相污染。**
