# First–Seventh House Axis Evidence｜第一－第七宮軸證據

Status: **REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE**

Baseline: `8aeb16243e36bd381c4de39183555e69e66aaa4d`

## 1. Research question

本輪補的是 Astrology interpretation coverage 的 house/angle gap，而不是建立十二宮大全。

Bounded family：

```text
Ascendant / 1st place / 1st house
↔
Descendant / 7th place / 7th house
```

目標是分開記錄：

- Hellenistic primary-text place significations；
- early-modern Lilly house catalogue；
- contemporary traditional-practitioner framing；
- modern/reference-implementation psychological language；
- unknown-birth-time 對 house/angle interpretation 的 L3 precondition。

不同時期與流派不合併成一份 timeless universal house definition。

## 2. Primary evidence — Vettius Valens

Reviewed source：

```text
janegca/latex-valens@2d4a8b9890cd5cb7714abd52f6bd938272ba8237
Mark Riley English translation reformatted/annotated in LaTeX
repository LICENSE: GPL-2.0
translation-rights status: separately unresolved; no source text is vendored here
```

Direct locators：

```text
book04/12-places.tex
book02/37-marriage.tex
```

Bounded observations：

- Book IV's twelve-place list associates the Ascendant / first place with life, steering, body and breath.
- The same list names the seventh as the Descendant and associates it with marriage, success, an affair, friendship and travel.
- Book II's marriage section explicitly identifies the Place of Marriage as the seventh sign from the Ascendant.

These are historical doctrine claims. They do not prove scientific validity or establish a project-canonical modern meaning.

## 3. Primary evidence — William Lilly

Reviewed web edition：

```text
William Lilly, Christian Astrology (1647)
Skyscript / Deborah Houlding retyped edition
Of the Twelve Houses, their Nature and Signification
CA pp. 50ff
```

Bounded observations：

- Lilly's first house catalogue covers the native/querent's life, stature, complexion, form and bodily appearance, and names it the Ascendant.
- Lilly's seventh house catalogue covers marriage/love questions, spouse or person enquired after, lawsuits, open/public enemies, the opposing party and direct disputes.

This is early-modern doctrine. `context:early_modern` is historical context only; the current taxonomy intentionally has no canonical early-modern doctrinal-lineage selector.

## 4. Contemporary practitioner evidence — Deborah Houlding

Reviewed pages：

```text
The 1st house — House Rulerships in Practice
The 7th house — House Rulerships in Practice
Deborah Houlding / Skyscript
```

Bounded observations：

- The first-house page preserves life/vitality/body topics and adds practitioner language around personality and manner of expression.
- The seventh-house page preserves marriage/partnership, legal contracts, opponents and known enemies.

This source is useful for contemporary traditional-practice continuity but is not an independent ancient witness.

## 5. Reference implementation — wvanderen/astrology-skill

Pinned source：

```text
wvanderen/astrology-skill@a9339b3c7151313530aa5002572c6612a2cfd59f
references/houses/1st.md
references/houses/7th.md
root license: MIT
```

The modules intentionally combine classical notes with modern psychological language.

Useful modern/reference framing includes：

- first house: identity, self-presentation, personal agency, embodiment;
- seventh house: committed relating, mirroring, projection, attachment patterns, collaboration and negotiation.

These are stored as **REFERENCE_ONLY qualified claims**. They must not be silently projected backward onto Valens/Lilly or treated as an independently validated psychological model.

## 6. Unknown-birth-time boundary

Existing project evidence already showed that unknown birth time makes houses/angles topology-changing rather than safely approximated:

```text
UNKNOWN_TIME_SENSITIVITY_RESULTS.md
STRUCTURED_ASTROLOGY_FACT_SCHEMA_DRAFT.md
```

Therefore this family adopts the research precondition：

```text
1st/7th house interpretation
→ requires available Ascendant / house L2 facts
→ route declares requires_l2_facts=true
→ missing required L2 refs fails closed
```

Current boundary：

- this family records the L3 precondition;
- dedicated regressions exercise the existing generic L2 precondition gate;
- the core retrieval engine does **not** yet auto-infer a required L2 fact set from registry metadata.

So this round does not claim generic automatic enforcement beyond the route contract.

## 7. Tradition separation decision

Current typed taxonomy supports：

```text
lineage:hellenistic
context:classical_antiquity
context:early_modern
context:modern_contemporary
school:modern:psychological_astrology
```

Decisions：

- Valens claims may carry `lineage:hellenistic`.
- Lilly claims carry `context:early_modern` but no invented doctrinal lineage.
- Houlding practitioner continuity carries modern historical context, not a fabricated doctrine selector.
- wvanderen modern psychological wording remains REFERENCE_ONLY and is not automatically assigned to `school:modern:psychological_astrology` unless the source itself is admitted as that school for the specific claim.

This prevents broad tags such as `classical` or `modern` from becoming silent routing authority.

## 8. What this family does not claim

It does not establish：

- scientific predictive validity of houses;
- a universal house system;
- whole-sign vs quadrant house policy;
- deterministic physical appearance or medical diagnosis;
- a fixed personality essence from the Ascendant;
- certainty about a partner's private motives;
- production Astrology routing.

## 9. Promotion state

This family is a new research claim family only.

```text
source evidence
→ v0.2 typed registry
→ dedicated regression
→ retrieval evidence
```

Even if all regressions pass, status remains：

**REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE.**
