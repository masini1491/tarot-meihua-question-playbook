# Research Routing｜研究線導向

本檔只負責**明確 research intent 的 owner discovery、authority boundary 與最低載入路徑**。

它不是 production method router，也不把 `references/**` 內的研究線升級成正式占卜方法。

目前 production method selection 仍由 `METHOD_ROUTING.md` 單獨負責：

```text
Tarot
Meihua
Liuyao
Tarot + Meihua（只有既有 canonical reconciliation contract 適用時）
```

## Research Line Registry｜研究線登錄

目前 root 可發現的 research lines：

### Astrology

Owner：[`references/astrology/README.md`](references/astrology/README.md)

Intent examples：

```text
星座／本命星盤
行運／transit
宮位／相位／逆行
Astrology chart facts
Astrology tradition-specific interpretation research
```

Current authority：

```text
REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE
```

目前已有 deterministic / typed research contracts 與 regression evidence，但沒有 `ASTROLOGY.md` production method owner，也不是 `METHOD_ROUTING.md` 的候選方法。

### Palmistry

Owner：[`references/palmistry/README.md`](references/palmistry/README.md)

Intent examples：

```text
手相／掌紋
手掌照片 observation
palm geometry / principal lines
Palmistry source / tradition research
```

Current authority：

```text
REFERENCE-ONLY / DRAFT / NOT PRODUCTION-ROUTABLE
```

目前 observation / normalization / repeatability 研究已累積多個 bounded evidence nodes；formal device/capture repeatability 仍等待真正分離的實拍 collection，未完成 production admission。

## Explicit Research Intent Gate｜明確研究意圖

只有下列情形進本 router：

- 使用者明確指定 Astrology／占星／星盤／行運等 research line；
- 使用者明確指定 Palmistry／手相／掌紋／手掌照片 research line；
- 使用者要求維護、驗證、比較或繼續上述 research dossier；
- machine consumer 已由 `PLAYBOOK_INDEX.json` 命中 `research.*` capability。

最低路徑：

```text
explicit research intent
→ RESEARCH_ROUTING.md
→ named research README / owner
→ only the minimum relevant research contracts / evidence
→ output with research authority preserved
```

不得因使用者明確指定 research line，又先把問題改寫成 Tarot / Meihua / Liuyao。

## Ordinary Reading Boundary｜普通占問邊界

使用者只說：

```text
幫我占……
這件事怎麼發展？
她怎麼想？
月底前會不會完成？
```

而沒有明確指定 research line 時，**不要**載入本檔來擴張候選方法。

應直接回到：

```text
CHAT_INIT.md
→ METHOD_ROUTING.md
→ production method owner
```

Astrology / Palmistry 不因 repository 已有 research dossier 就成為 ordinary auto-routing candidate。

## Research Routing ≠ Production Admission

下列行為一律禁止：

```text
research README exists
→ therefore production supported

PLAYBOOK_INDEX has research pointer
→ therefore METHOD_ROUTING may auto-select it

research validator/test passes
→ therefore scientific/predictive validity established

research result is detailed
→ therefore may silently create production rule
```

Research pointer 只代表：

```text
this repository knows where the bounded research owner lives
```

不代表：

```text
production method authority
runtime authority
scientific validity
cross-validation authority
user-facing predictive certainty
```

## Explicit User Request with Incomplete Research Capability

如果使用者明確要求 Astrology / Palmistry，但目前 research line 尚缺必要 fact / engine / image / permission / validation：

1. 保留使用者指定的 research identity；
2. 依該 research owner fail closed 在缺失層；
3. 可說明需要的最小 additional evidence；
4. 不因 research capability gap 就自行改成 Tarot / Meihua / Liuyao；
5. 若使用者另行要求 production method，才建立新的 distinct reading / task identity。

## Mixed Production + Research Request

同一 request 同時要求 production method 與 research line 時，預設保持兩個責任面：

```text
production reading
→ production method owner

research analysis
→ RESEARCH_ROUTING.md → research owner
```

除非已有獨立 canonical reconciliation contract，否則不得把兩者稱為正式 cross-validation，也不得把 research conclusion 當成 production source fact。

## Promotion Boundary

Research line 若未來要進 production，仍必須依 repository governance 走完整 adoption sequence：

```text
judgment gap
→ method owner
→ deterministic / runtime authority
→ routing
→ provenance
→ behavioral regression
→ user-facing docs
→ explicit admission decision
```

修改本檔或 `PLAYBOOK_INDEX.json` 的 research pointer **不能跳過上述 sequence**。

核心原則：

> **Research routing makes evidence discoverable without making it authoritative beyond its admitted layer. Explicit research intent stays research; ordinary reading stays on the production router.**
