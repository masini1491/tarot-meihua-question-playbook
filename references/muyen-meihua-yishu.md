# Reference｜muyen/meihua-yishu

Repo: https://github.com/muyen/meihua-yishu

License: CC BY-NC-SA 4.0（以來源 Repo 當下 LICENSE 為準）

## 類型

梅花易數 AI Skill＋起卦工具＋參考資料＋案例。包含時間、數字、聲音、方位、物象等起卦方式，以及主卦、互卦、變卦、體用、應期與外應相關流程。

## 值得吸收

### ADOPTED — 先決定起卦方式

來源明確要求具體問題起卦前先決定取象／時間／數字等方法，而不是 AI 自動換方法。

本 Playbook 吸收為：

> 起卦來源與算法在看結果前固定，並保存原始輸入。

### ADOPTED — 雙數起卦公式

來源對兩個數字的做法：

- 第一數 ÷ 8 → 上卦
- 第二數 ÷ 8 → 下卦
- 兩數總和 ÷ 6 → 動爻

本 Playbook 將此列為目前採用的一種明確雙數契約；若未來支援其他流派，必須標示並分開。

### ADOPTED — 同題不反覆起卦

來源明確提出不要無因反覆占問。

本 Playbook 吸收為重卦紀律：只有新事實、新子問題、重新定義 completion rule 或原題契約有錯時，才允許新卦。

### ADAPTED — 主／互／變與體用流程

來源把各層拆開處理。本 Playbook 吸收的是「證據角色固定」與「可回查」，而不複製其完整術數解讀資料。

### ADOPTED — 外應與環境訊號要有邊界

來源會使用聲音、顏色、人物、方位等作為外應。本 Playbook 只吸收治理原則：

> 外應必須基於已發生的明確訊號，不應無限制搜尋任何細節來補強期待中的答案。

### ADAPTED — 應期與現實節點對齊

來源強調應期。本 Playbook 進一步要求：先定義問題 horizon，再判斷數字應落在小時／天／週／月，並優先參照合理現實 checkpoint。

## 不直接採用／需標示差異

- 來源包含現代擴充的秒級時間起卦；本 Playbook 不自動視為傳統標準。
- 時間起卦涉及農曆、子時跨日等流派／實作選擇時，必須把規則寫入 input contract。
- 不直接複製來源的完整卦辭、爻辭、十八占、萬物類象內容。
- 因來源採 CC BY-NC-SA，若未來要大量改編其實質文字／資料，需另外處理 attribution、non-commercial、share-alike 條件；目前主規則只做概念性摘要與自主改寫。

## 已影響主文件

- `INPUT_CONTRACT.md`
- `MEIHUA.md`
- `CROSS_VALIDATION.md`
