# Device / Capture Repeatability — Formal Collection Extension Lock

Status: **REFERENCE-ONLY / PRE-INFERENCE FORMAL COLLECTION EXTENSION LOCK / NO PRODUCTION AUTHORITY**

## Purpose

本文件把 first-upload repeated-reposition pilot 與原先 predeclared 的 formal B2 three-session design 接起來，避免在已看過 detector / geometry 結果後重新挑選「比較漂亮」的來源照片。

Formal B2 closure 仍沿用 `DEVICE_CAPTURE_REPEATABILITY_PLAN.md` 的最低設計：

```text
2 devices × 3 true repositioned sessions × 5 captures/device/session = 30 images
```

本 lock 只固定如何使用 first-upload source set 中**已在 detector inference 前選定**的 earliest-five captures 作為 formal `S1`，並定義未來 `S2` / `S3` 尚需收集的資料。它不把 first-upload 的 ordinal `B1/B2/B3` 升格成 sessions。

## Evidence chain

```text
DEVICE_CAPTURE_REPEATABILITY_PLAN.md
→ DEVICE_CAPTURE_REPEATABILITY_CAPTURE_PROTOCOL.md
→ DEVICE_CAPTURE_REPEATABILITY_FIRST_UPLOAD_ADMISSION.md
→ DEVICE_CAPTURE_REPEATABILITY_FIRST_UPLOAD_SOURCE_FREEZE.md
→ DEVICE_CAPTURE_FIRST_UPLOAD_PILOT_RESULT_FREEZE.md
→ DEVICE_CAPTURE_FIRST_UPLOAD_PILOT_RESULTS.md
→ 本 formal collection extension lock
```

## Existing source identity

Frozen first-upload archive：

```text
archive name = 左手.zip
SHA256 = b5854b545f3ff0193b51cc02278efdbca25e1e3d1147a8559c7bb042ff2b7ca0
```

Device mapping：

```text
D1 = Google Pixel 5
D2 = Google Pixel 10 Pro
```

Anatomical-side authority：

```text
anatomical_side = left
side_authority = explicit_bodily_self_report
```

First-upload source contains 15 repeated-reposition stills/device in one short collection block. The entire 30-image upload remains a pilot dataset; only the fixed earliest-five subset per device is admitted below as candidate formal `S1` source material.

## S1 selection rule — locked before future S2/S3 inference

Selection rule：

```text
for each device independently:
  sort the frozen first-upload source entries by original capture order
  select ordinal 01–05 only
```

This is a deterministic source-order rule. It does not use detector candidate count beyond already frozen accounting, landmark geometry, canonical geometry, handedness score, visual preference, or device-result ranking.

The remaining first-upload ordinals `06–15` are **pilot extras only** and are not later promoted to `S2` or `S3`.

## Formal S1 entries

```text
D1-S1-01..05 = first-upload D1 ordinal 01..05
D2-S1-01..05 = first-upload D2 ordinal 01..05
```

The first-upload source freeze already established：

```text
30 / 30 decoded
30 / 30 unique source SHA256
EXIF Orientation = 1 for all 30
```

No source image bytes are committed to the public repository.

## Why S1 may be retained but B1/B2/B3 are still not sessions

The distinction is：

```text
formal S1 = one existing short collection block, using a predeclared 5-capture subset
B1/B2/B3 = three ordinal slices inside that same short collection block
```

Therefore the earliest-five subset can serve as the first collection session `S1`, but ordinals 06–10 cannot become `S2` and ordinals 11–15 cannot become `S3`. Formal cross-session evidence still requires two new, genuinely reset collection sessions.

## Remaining collection requirement

Formal B2 baseline therefore needs **20 new source images**, not another 30：

```text
S2: D1 × 5 + D2 × 5
S3: D1 × 5 + D2 × 5
new images total = 20
```

After adding the existing locked S1 subset：

```text
S1 = 10 existing selected images
S2 = 10 new images
S3 = 10 new images
formal total = 30 images
```

## Session reset rule for S2 and S3

Each future session must be a genuinely re-established capture state：

```text
finish current session
→ lower hand
→ put away / move phones from active framing
→ interrupt for at least several minutes or do something else
→ re-establish setup from scratch
→ begin next session
```

Exact elapsed minutes are not the scientific variable. The requirement is a real setup reset rather than continuous subdivision of one capture block.

Within each device/session, every one of the 5 captures still follows：

```text
one still
→ hand lowered / relaxed
→ hand raised again
→ small natural re-framing / reposition
→ next still
```

No burst and no video-frame extraction。

## Device order

Use the existing protocol's counterbalanced suggestion：

```text
S2: D2 → D1
S3: D1 → D2
```

## Capture-condition lock

S2 / S3 remain the same controlled baseline family as S1：

```text
same anatomical left hand
rear camera preferred
native still-photo mode
same general location/background/light family
near-frontal palm-facing pose
fingers naturally open
whole palm + wrist base + MCP region visible
nominal distance target ≈ 35 cm
no digital zoom
no portrait / beauty / deliberate AI filtering if controllable
no intentional blur / low-light / flash experiment / oblique perturbation
```

The user does not need to make pictures artificially different. Natural reposition variability is the signal being measured.

## Future source freeze discipline

After S2 and S3 are collected, before any new detector inference：

1. freeze the 20 new source-image SHA256 values；
2. verify exactly 5/device/session；
3. check duplicate bytes；
4. extract only task-relevant EXIF orientation / dimensions；
5. build a privacy-minimized formal 30-entry manifest using locked S1 + new S2/S3；
6. freeze the formal source-set manifest hash；
7. only then create / execute the formal P1/P2/P3 runner。

The already inspected pilot geometry must not be used to replace or re-rank S1 captures.

## Formal pair accounting after completion

```text
P1 within-device / within-session = 60 pairs
P2 cross-device / within-session  = 75 pairs
P3 within-device / cross-session  = 150 pairs
```

## Boundary

This lock does not itself close B2 and does not establish arbitrary-device portability, camera accuracy, biometric identity/authentication, production threshold/routing, or z-coordinate portability.

Current state：

```text
first-upload pilot characterization = complete
formal S1 source subset              = locked
formal S2 collection                 = pending
formal S3 collection                 = pending
formal B2 closure                    = open
```

Palmistry remains **REFERENCE-ONLY / DRAFT / NOT PRODUCTION-ROUTABLE**。
