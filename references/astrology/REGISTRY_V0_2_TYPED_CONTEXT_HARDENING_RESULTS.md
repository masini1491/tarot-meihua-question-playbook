# Registry v0.2 Typed Context Hardening Results

Status: **REFERENCE-ONLY / RESEARCH RESULT / NOT PRODUCTION-ROUTABLE**

Baseline: `6448a2e0d0abd4eb56dc1d4714fcd2ecd432be91`

## Goal

Close the remaining typed-tradition integrity gap between the v0.2 query/retrieval/L5 contracts and the interpretation claim registries themselves.

Before this round, the real registries already carried explicit `tradition_context_refs[]`, but their schema identity and validator remained `0.1.0-research`. Explicit refs therefore had selector precedence without a registry-level taxonomy contract proving that every ref was known, unique, and in the correct dimension.

## Decision

Current real registries are migrated to:

```text
interpretation_claim_registry@0.2.0-research
```

Legacy support remains:

```text
interpretation_claim_registry@0.1.0-research
```

The version boundary is semantic, not cosmetic:

```text
0.1
→ canonical source / claim / conflict / privacy guards
→ legacy flat-tag retrieval compatibility

0.2
→ 0.1 canonical requirements
+ taxonomy-aware typed context invariants
+ registry preflight before claim selection
```

## v0.2 invariants

Every v0.2 claim must explicitly contain:

```text
tradition_context_refs[]
```

An empty array is valid and means no admitted doctrine/school selector.

When refs are present:

- every ref must exist in the supplied taxonomy;
- duplicates are invalid;
- `tradition_context_refs[]` accepts only `doctrinal_lineage` / `interpretive_school`;
- `historical_context_refs[]` accepts only `historical_context`;
- `meta_context_refs[]` accepts only `meta_perspective`.

Malformed explicit refs invalidate the registry. The implementation does not silently drop them, repair them from legacy tags, or select a valid subset.

## Retrieval integration

`retrieve_interpretation_claims.py` now performs registry preflight before selection.

```text
query validation
→ registry schema/version gate
→ full registry validation
→ claim selection
```

For a malformed v0.2 registry:

```text
retrieval_status = registry_not_research_safe
selected_claim_ids = []
```

This converts malformed typed metadata from a possible misleading no-match/subset outcome into an explicit registry failure.

## Taxonomy dependency

A v0.2 registry requires taxonomy even when the query itself uses the legacy flat-tag selector. Typed claim contexts are part of the registry schema, not merely a typed-query feature.

A v0.1 registry remains valid without taxonomy and retains legacy flat-tag retrieval compatibility.

## Real registry migration

The following current real registries change schema identity only:

```text
domicile_claim_family_registry.json
saturn_moon_aspect_claim_family_registry.json
```

Their existing claim statements, source admission, confidence/support, conflict semantics, and explicit typed-context assignments are not changed by the migration.

The migration therefore does not:

- invent doctrine from ambiguous legacy tags;
- upgrade source admission;
- upgrade claim confidence/support;
- resolve historical/tradition conflict;
- create predictive, scientific, clinical, or production authority.

## Regression coverage authored

`test_interpretation_claim_registry_validator.py` now covers:

- unversioned legacy compatibility;
- v0.1 compatibility without taxonomy;
- valid v0.2 registry with taxonomy;
- taxonomy-required fail closed;
- missing explicit `tradition_context_refs[]`;
- valid explicit empty doctrine refs;
- unknown typed ref;
- wrong-dimension meta ref in doctrine array;
- duplicate typed ref;
- historical/meta dimension enforcement;
- current real registries must be v0.2 and validator-clean.

`test_typed_contract_v0_2.py` additionally covers:

- malformed v0.2 registry rejected before selection;
- v0.2 registry taxonomy dependency even for a legacy flat-tag query;
- structurally valid partial-tradition coverage remains distinct from invalid registry state;
- v0.1 query + v0.1 registry compatibility remains available.

`test_retrieve_interpretation_claims.py` is aligned so:

- synthetic v0.1 fixtures satisfy the canonical v0.1 source metadata contract;
- current real v0.2 registry regressions explicitly provide taxonomy.

## Validation evidence boundary

This result records implemented contracts, regression cases, and bounded compatibility/static review.

The repository root `Validate Playbook` workflow does not automatically execute dedicated tests under `references/astrology/`. Therefore a green root workflow must not be described as execution proof for the dedicated registry/retrieval tests above.

No dedicated execution result is claimed by this document unless a later result record explicitly records an actual test command/runtime and outcome.

## Historical records

`INTERPRETATION_CLAIM_REGISTRY_VALIDATION_RESULTS.md` and earlier migration documents remain historical evidence for the state that existed when they were written. They are not rewritten to pretend they originally validated v0.2.

## Boundary

This hardening improves internal research integrity only.

It does not establish:

- scientific or predictive validity of astrology;
- a production interpretation doctrine;
- a default tradition;
- a production Astrology method owner;
- production routing;
- cross-validation authority.

**Current state: REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE.**
