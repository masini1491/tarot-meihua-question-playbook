# Astrology Query Resolution / Routing Contract Draft

Status: **REFERENCE-ONLY / RESEARCH DRAFT / NOT PRODUCTION-ROUTABLE**

Schema name: `astrology_query_resolution`

Current schema version: `0.2.0-research`

Legacy compatibility version: `0.1.0-research`

This contract defines the boundary between natural-language question understanding and deterministic Astrology interpretation retrieval. It does not authorize free-form astrology interpretation, production routing, private-motive inference, clinical claims, or high-stakes prediction.

## 1. Pipeline

```text
user question
→ query-resolution stage
→ validated query-resolution envelope
→ deterministic interpretation-claim selector
→ retrieval provenance bundle
→ L5 synthesis envelope
→ user-facing prose renderer
```

The query resolver may understand language, but it must not invent L1/L2 facts, L3 policy, L4 meanings, source admission, or final L5 prose.

## 2. Version policy

### `0.2.0-research`

Typed tradition routing is canonical for resolved routes.

A resolved route must carry:

```text
tradition_resolution_status
requested_tradition_contexts[]
requested_synthesis_mode

route.tradition_context_refs_any[]
route.synthesis_mode
```

The validator requires the versioned Astrology tradition taxonomy and accepts only `doctrinal_lineage` or `interpretive_school` contexts as executable tradition selectors.

### `0.1.0-research`

Retained only as an executable compatibility contract for existing regression fixtures. Its flat:

```text
tradition_tags_any[]
```

selector is not the canonical contract for new typed research routes.

The same schema version must never silently change meaning; this is why typed routing is versioned as `0.2.0-research` rather than retrofitted invisibly into `0.1.0-research`.

## 3. Envelope identity

Required research envelope:

```text
schema_name = astrology_query_resolution
schema_version = 0.2.0-research
record_status = REFERENCE-ONLY
production_routable = false
```

Core fields:

```text
query_id
user_question
resolution_status
question_risk_class
target_registry_record_id
tradition_resolution_status
requested_tradition_contexts[]
requested_synthesis_mode
route
routing_assumptions[]
unresolved_slots[]
clarification_question
unsupported_reason
reference_only_justification
```

## 4. Resolution statuses

```text
resolved
needs_clarification
unsupported
```

`resolved` may proceed only when all material route fields are grounded and the request is `normal_symbolic`.

`needs_clarification` must not emit an executable route.

`unsupported` must not be weakened into a symbolic route merely to produce an answer.

## 5. Risk boundary

Research risk vocabulary:

```text
normal_symbolic
private_motive_inference
clinical_or_diagnostic
high_stakes_external_outcome
```

Only `normal_symbolic` may resolve into Astrology retrieval.

The contract must not establish another person's hidden motives, diagnosis/trauma as fact, guaranteed relationship or external outcomes, medical/legal/investment outcomes, or predictive certainty.

## 6. Typed deterministic route

For `0.2.0-research`, a resolved `route` contains:

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

`tradition_tags_any[]` may remain as an empty compatibility field, but a non-empty legacy flat selector is invalid under v0.2.

The route must preserve the same `query_id` as the resolution envelope.

## 7. Typed tradition invariants

Executable tradition contexts are limited to taxonomy dimensions:

```text
doctrinal_lineage
interpretive_school
```

Historical context, meta perspective, synthesis mode, and implementation mode are not doctrine selectors.

Required invariants:

```text
requested_tradition_contexts == route.tradition_context_refs_any
requested_synthesis_mode == route.synthesis_mode
tradition_resolution_status ∈ explicit | inferred_from_named_school
```

Cardinality:

```text
synthesis:single_tradition   → exactly 1 context
synthesis:parallel_comparison → at least 2 contexts
synthesis:explicit_blend      → at least 2 contexts
```

There is no silent default tradition and no cross-tradition substitution on retrieval miss.

## 8. Explicit blend boundary

`synthesis:explicit_blend` is not a fallback for unresolved or conflicting traditions.

It requires explicit provenance from:

```text
user_text
or
research_fixture
```

A generic research-policy default is insufficient to prove that blending was explicitly requested.

## 9. Material uncertainty fails closed

If L2 facts are required:

```text
requires_l2_facts = true
→ l2_fact_refs[] must be non-empty
```

If L3 policy is required:

```text
requires_l3_policy = true
→ l3_policy_refs[] must be non-empty
```

The resolver must not invent fact refs, policy refs, traditions, applicability, or source families to avoid clarification.

## 10. Routing provenance

Every populated semantic route field requires a matching `routing_assumptions[]` record.

For v0.2 the semantic route fields are:

```text
claim_types
tradition_context_refs_any
synthesis_mode
applies_to_all
```

Candidate assumption shape:

```text
field
basis
evidence_spans[]
evidence_refs[]
```

Basis vocabulary:

```text
user_text
upstream_context
research_fixture
research_policy
```

`user_text` spans must literally occur in `user_question`; `upstream_context` requires explicit evidence refs.

## 11. Registry and REFERENCE_ONLY boundary

A resolved envelope names exactly one `target_registry_record_id`.

`allow_reference_only_qualified` defaults false. If enabled, `reference_only_justification` is required. This widens research evidence admission only; it does not upgrade any source or claim to project doctrine.

## 12. Clarification and unsupported contracts

`needs_clarification` requires:

```text
unresolved_slots[] != []
clarification_question
route = null | omitted
```

`unsupported` requires:

```text
unsupported_reason
route = null | omitted
```

## 13. Validator

`validate_astrology_query_resolution.py` supports both v0.2 typed and v0.1 legacy compatibility.

For v0.2 it checks:

```text
schema / REFERENCE-ONLY / production guards
risk-class gating
registry target
route/query identity
L2/L3 preconditions
REFERENCE_ONLY opt-in justification
taxonomy validity
typed context existence + dimension
tradition route/request parity
synthesis-mode parity + cardinality
legacy selector rejection
routing provenance coverage
explicit-blend provenance
clarification / unsupported invariants
```

The validator does not claim the upstream natural-language semantic mapping is objectively correct.

## 14. L5 boundary

Successful validation authorizes only deterministic retrieval, not free-form interpretation.

The sequence remains:

```text
validated resolution
→ deterministic selector
→ retrieval provenance bundle
→ deterministic synthesis envelope
→ constrained user-facing prose
```

Any semantic assertion must remain traceable to registered claims or clearly labeled synthesis. Registered conflicts, cautions, source-admission status, tradition provenance, and guardrails must survive downstream composition.

## 15. Privacy

Repository fixtures must remain synthetic, fictional, public, or otherwise non-identifying. Do not commit real private natal data or private user conversations as regression fixtures.

## 16. Compatibility boundary

`0.1.0-research` remains executable so older query/retrieval/L5 regressions do not break during migration.

New research fixtures should target `0.2.0-research` unless their explicit purpose is legacy compatibility regression.

The compatibility path is temporary evidence of migration safety, not a second canonical tradition-routing policy.

## 17. Non-goals

This contract does not establish:

```text
production NLU quality
production routing
scientific predictive validity
clinical validity
truth of source interpretations
full privacy detection
canonical user-facing wording
```

**Current state: REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE.**
