# Astrology Retrieval / Output Provenance Contract Draft

Status: **REFERENCE-ONLY / RESEARCH DRAFT / NOT PRODUCTION-ROUTABLE**

Current bundle schema: `interpretation_retrieval_provenance_bundle@0.2.0-research`

Legacy compatibility bundle: `interpretation_retrieval_provenance_bundle@0.1.0-research`

This contract defines deterministic selection between a resolved Astrology route and later L5 synthesis. It does not perform natural-language intent inference, astronomical calculation, source admission upgrades, or final prose generation.

## 1. Typed v0.2 query surface

The v0.2 selector consumes:

```text
query_id
claim_types[]
tradition_tags_any[] = []
tradition_context_refs_any[]
synthesis_mode
applies_to_all[]
requires_l2_facts
l2_fact_refs[]
requires_l3_policy
l3_policy_refs[]
allow_reference_only_qualified
include_registry_guardrails
```

Typed retrieval additionally requires the versioned tradition taxonomy.

`tradition_context_refs_any[]` is an OR selector over canonical doctrine/school refs derived from each registered claim. Historical/meta/implementation contexts are not executable tradition selectors.

## 2. Legacy compatibility

A query without typed fields continues to use the v0.1 flat `tradition_tags_any[]` selector and produces a `0.1.0-research` bundle.

The legacy path exists only to preserve migration regression. New research routes should use v0.2 typed contexts.

## 3. Preconditions

Missing required L2 or L3 refs fails closed:

```text
retrieval_status = precondition_failed
```

The selector must not infer or invent missing facts or policies.

## 4. Exact selection behavior

A claim is considered only when all required filters pass:

```text
claim_type match
tradition context overlap (v0.2) OR legacy tag overlap (v0.1)
applicability superset match
all source_refs resolve
source admission rule passes
```

There is no fuzzy semantic fallback and no model-memory fallback.

## 5. Typed claim provenance

For v0.2, every selected claim includes:

```text
tradition_context_refs[]
```

These refs are derived through the versioned taxonomy / typed routing adapter rules and must remain visible downstream.

Broad tags such as `classical`, `modern`, or `blended` do not become doctrine selectors unless the taxonomy explicitly provides an admissible canonical doctrine/school mapping.

## 6. Source-admission behavior

All cited sources must either be claim-eligible or satisfy the explicit qualified `REFERENCE_ONLY` opt-in contract.

Possible selected-claim modes remain:

```text
claim_eligible
qualified_reference_only
mixed_claim_eligible_and_reference_only
```

REFERENCE_ONLY participation must never silently become project-canonical authority.

## 7. Conflict and guardrail preservation

Selected claims retain conflict groups. Bundle conflict records preserve:

```text
conflict_group_id
conflict_class
resolution_status
resolution_note
selected_claim_refs[]
external_claim_refs[]
```

Registry `non_admitted_claims[]` are copied into `guardrails[]` when requested.

Conflicts are not averaged into consensus.

## 8. Citation readiness

Each selected claim carries source provenance sufficient for later citation rendering. Missing source locator provenance yields:

```text
retrieval_status = provenance_incomplete
```

All selected sources having non-empty locators yields:

```text
retrieval_status = citation_ready
```

## 9. Typed tradition coverage

For v0.2 bundles, the selector emits:

```text
tradition_provenance:
  requested_tradition_contexts[]
  requested_synthesis_mode
  covered_tradition_contexts[]
  missing_tradition_contexts[]
```

Single-tradition retrieval may legitimately return `no_match`.

For:

```text
synthesis:parallel_comparison
synthesis:explicit_blend
```

any missing requested tradition context produces:

```text
retrieval_status = tradition_coverage_incomplete
```

and adds a guardrail forbidding silent cross-tradition substitution.

## 10. Synthesis provenance

Successful bundles record:

```text
synthesis_provenance:
  l2_fact_refs[]
  l3_policy_refs[]
  claim_refs[]
  conflict_group_refs[]
  tradition_context_refs[]
  synthesis_mode
```

The desired trace is:

```text
L2 fact
→ L3 policy
→ typed tradition context
→ selected L3/L4 claim
→ conflict context
→ source provenance
→ L5 synthesis
```

## 11. Bundle identity

Typed bundle:

```text
schema_name = interpretation_retrieval_provenance_bundle
schema_version = 0.2.0-research
record_status = REFERENCE-ONLY
production_routable = false
```

Legacy bundle remains `0.1.0-research` only when the input route uses the explicit legacy path.

## 12. Retrieval status vocabulary

```text
invalid_query
registry_not_research_safe
precondition_failed
no_match
citation_ready
provenance_incomplete
tradition_coverage_incomplete
```

`tradition_coverage_incomplete` is a typed multi-tradition fail-closed state; it is not permission to substitute a different tradition.

## 13. Direct core integration

`retrieve_interpretation_claims.py` now owns typed filtering and coverage directly.

The older `typed_tradition_pipeline.py` remains a transitional compatibility wrapper during migration, but it is no longer the sole executable path for typed retrieval.

## 14. L5 contract

`compose_interpretation_synthesis.py` accepts v0.2 bundles directly and verifies that:

```text
route tradition refs == synthesis provenance tradition refs
route synthesis mode == synthesis provenance synthesis mode
```

It copies typed provenance into the route snapshot and synthesis units.

If bundle status is `tradition_coverage_incomplete`, L5 composition is blocked as:

```text
blocked_tradition_coverage_incomplete
```

with no synthesis units emitted.

Parallel comparison requires a disclosure to keep traditions visibly separate. Explicit blend requires a disclosure preserving each contributing tradition's provenance and conflicts.

## 15. Privacy / scope

This contract remains research-only. Repository fixtures must not contain real private natal data.

It does not establish scientific validity, predictive validity, clinical validity, production tradition policy, or production user-facing wording.

**Current state: REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE.**
