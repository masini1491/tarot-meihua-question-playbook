# Typed Tradition Contract v0.2 Migration Results

Status: **REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE**

Baseline main: `23d28b1655a0cf68ff233f863655ae77a48640a0`

## Decision

Promote typed tradition routing from a wrapper-only integration into the core research contracts as version `0.2.0-research` while retaining `0.1.0-research` as an explicit migration-compatibility path.

This avoids silently changing the meaning of an existing schema version.

## Core changes

`validate_astrology_query_resolution.py`

- supports v0.2 typed and v0.1 legacy envelopes;
- v0.2 requires taxonomy-backed `tradition_context_refs_any[]`;
- only `doctrinal_lineage` / `interpretive_school` contexts are executable;
- non-empty legacy flat tradition tags are rejected in v0.2;
- route/requested tradition and synthesis-mode parity are required;
- synthesis-mode cardinality is deterministic;
- explicit blend requires explicit provenance.

`retrieve_interpretation_claims.py`

- consumes typed refs and taxonomy directly;
- filters claims through canonical typed tradition refs;
- emits `0.2.0-research` provenance bundles for typed routes;
- records requested / covered / missing tradition contexts;
- blocks incomplete parallel/blended coverage as `tradition_coverage_incomplete`;
- preserves v0.1 legacy tag retrieval when typed fields are absent.

`compose_interpretation_synthesis.py`

- consumes v0.2 bundles directly;
- checks typed route/provenance parity;
- preserves typed refs in route snapshots and synthesis units;
- blocks incomplete multi-tradition coverage before L5;
- adds parallel-separation / explicit-blend disclosures;
- preserves v0.1 envelope behavior for legacy bundles.

## Direct-core regression fixture

Added `test_typed_contract_v0_2.py` with 10 authored cases covering:

1. valid v0.2 typed resolution;
2. taxonomy required;
3. legacy flat selector rejected in v0.2;
4. meta/non-doctrine context rejected;
5. direct core psychological retrieval selects Greene without wrapper;
6. direct core composer preserves typed provenance without wrapper;
7. complete Ptolemaic + psychological parallel coverage reaches L5;
8. partial parallel coverage blocks core composer;
9. direct Ptolemaic domicile typed retrieval;
10. v0.1 legacy validation / retrieval / synthesis compatibility.

At the time of this migration, these were authored regression evidence only because repository CI did not automatically execute dedicated tests under `references/astrology/`. That historical boundary remains accurate.

## Compatibility boundary at migration time

`typed_tradition_pipeline.py` remained present as a transitional compatibility wrapper immediately after v0.2 core promotion. It was no longer the only typed executable path.

Retirement was intentionally deferred until direct-core parity, real-registry migration, and dedicated execution evidence were available.

## Subsequent retirement evidence

The deferred retirement conditions were later satisfied on audited main:

```text
9645c8206d61085c4047eb53375a7548975e75de
```

An isolated regression bundle was reconstructed from exact GitHub blobs and all 11 local source/test/fixture identities matched their Git blob SHA.

Dedicated execution under Python `3.13.5` produced:

```text
test_typed_contract_v0_2.py                 10 / 10 PASS
test_registry_typed_context_migration.py    11 / 11 PASS
test_typed_tradition_pipeline.py            11 / 11 PASS
combined                                      32 / 32 PASS
```

A fresh caller audit found no maintained executable consumer outside the wrapper's own parity test. The deprecated wrapper and wrapper-only parity test were therefore retired.

Current canonical typed execution is direct core only:

```text
validate_astrology_query_resolution.py
→ retrieve_interpretation_claims.py
→ compose_interpretation_synthesis.py
```

The explicit v0.1 flat-tag compatibility regression remains in the core test contract and is not dependent on wrapper existence.

See `TYPED_WRAPPER_RETIREMENT_EXECUTION_RESULTS.md` for exact execution provenance.

## Authority boundary

No production routing is granted.

No source admission is upgraded.

No claim meaning, confidence, conflict resolution, or scientific-validity assertion is changed.

No real birth data is introduced.

**Current state: REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE.**
