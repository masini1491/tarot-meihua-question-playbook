# Astrology L5 Synthesis Envelope Contract Draft

Status: **REFERENCE-ONLY / RESEARCH DRAFT / NOT PRODUCTION-ROUTABLE**

Schema name: `interpretation_synthesis_envelope`

Current typed version: `0.2.0-research`

Legacy compatibility version: `0.1.0-research`

This contract defines the deterministic handoff between retrieval provenance and later user-facing L5 prose. It packages and verifies evidence boundaries; it does not itself generate a reading.

## 1. Pipeline

```text
validated query resolution
→ retrieval provenance bundle
→ deterministic synthesis envelope
→ user-facing prose renderer
```

## 2. Version behavior

A `0.2.0-research` retrieval bundle produces a `0.2.0-research` synthesis envelope and carries typed tradition provenance.

A legacy `0.1.0-research` bundle continues to produce a `0.1.0-research` envelope for migration compatibility.

New research routes should use v0.2.

## 3. Required identity and provenance agreement

Every envelope remains:

```text
record_status = REFERENCE-ONLY
production_routable = false
```

The composer requires agreement across:

```text
query_id
registry_record_id
L2 fact refs
L3 policy refs
selected claim refs
conflict-group refs
```

For v0.2 it additionally requires:

```text
route.tradition_context_refs_any == synthesis_provenance.tradition_context_refs
route.synthesis_mode == synthesis_provenance.synthesis_mode
```

Any mismatch blocks synthesis.

## 4. Accepted retrieval states

Normal composition requires:

```text
retrieval_status = citation_ready
```

Special bounded states:

```text
no_match
→ synthesis_status = no_supported_claims

tradition_coverage_incomplete
→ synthesis_status = blocked_tradition_coverage_incomplete
```

Neither state authorizes model-memory fallback.

## 5. Synthesis units

Each selected claim becomes one synthesis unit carrying:

```text
claim_id
statement
statement_sha256
claim_type
tradition_tags[]
tradition_context_refs[]
applies_to[]
scope
confidence_status
support_status
source_admission_mode
cautions[]
conflict_group_ids[]
citation_source_ids[]
semantic_policy = registered_claim_only
```

`statement` is the registered normalized claim, not new prose. `statement_sha256` detects accidental mutation before rendering.

## 6. Typed tradition provenance

A v0.2 envelope copies:

```text
tradition_provenance:
  requested_tradition_contexts[]
  requested_synthesis_mode
  covered_tradition_contexts[]
  missing_tradition_contexts[]
```

The route snapshot also carries:

```text
tradition_context_refs_any[]
synthesis_mode
```

Each synthesis unit retains the typed contexts of its source claim.

## 7. Multi-tradition boundary

### Parallel comparison

A ready envelope adds a disclosure requiring traditions to remain visibly separate and forbidding averaging into consensus.

### Explicit blend

A ready envelope records that blending was explicitly requested and requires provenance/conflicts for every contributing tradition to remain visible.

### Incomplete coverage

If any requested tradition is missing from a parallel comparison or explicit blend:

```text
synthesis_status = blocked_tradition_coverage_incomplete
synthesis_units = []
```

The envelope must explicitly forbid silent substitution or invention of the missing perspective.

## 8. No hidden semantic expansion

The deterministic composer must not:

```text
invent interpretation
combine claims into a stronger claim
convert symbolism into biography
convert historical doctrine into modern psychology
remove tradition/applicability scope
upgrade confidence or source admission
resolve registered conflicts by averaging
```

## 9. Citation units

Every synthesis unit references `citation_source_ids[]`.

Citation metadata retain:

```text
source_id
title
author_or_org
source_role
admission_status
locator
edition
immutable_revision
publication_or_release_date
license_status
copyright_status
```

Missing locator provenance blocks composition as `blocked_provenance_incomplete`.

## 10. Conflict, caution, guardrail, and REFERENCE_ONLY preservation

Registered conflict records are copied unchanged.

Claim cautions remain attached to their synthesis units.

Registry guardrails remain present when requested.

Qualified `REFERENCE_ONLY` participation adds an explicit disclosure and never changes source admission authority.

## 11. Route snapshot

The envelope stores:

```text
claim_types[]
tradition_tags_any[]
tradition_context_refs_any[]
synthesis_mode
applies_to_all[]
l2_fact_refs[]
l3_policy_refs[]
```

It also preserves `resolution_provenance[]`, `synthesis_provenance`, and for v0.2 `tradition_provenance`.

This permits later audit of both why the route was chosen and why each claim was selected.

## 12. Synthesis status vocabulary

Research statuses include:

```text
ready_for_l5
no_supported_claims
blocked_tradition_coverage_incomplete
blocked_resolution_not_resolved
blocked_bundle_schema
blocked_bundle_not_research_safe
blocked_query_mismatch
blocked_registry_mismatch
blocked_provenance_mismatch
blocked_provenance_incomplete
blocked_retrieval_status
blocked_empty_claims
blocked_claim_statement_missing
```

Only `ready_for_l5` authorizes a later renderer to synthesize from included units.

## 13. Required disclosures

Every envelope starts with:

```text
REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE
Source-backed claims and L5 synthesis must remain distinguishable.
```

Additional disclosures are appended for cautions, conflicts, guardrails, qualified REFERENCE_ONLY provenance, parallel-comparison separation, explicit-blend provenance, and incomplete tradition coverage.

## 14. Rendering boundary

A future renderer may improve readability but must not change evidence authority. It should consume only the validated envelope surfaces and must not use retrieval failure as permission for free-form interpretation.

## 15. Compatibility boundary

`0.1.0-research` remains executable only to preserve legacy regression during migration.

The typed v0.2 core path no longer requires `typed_tradition_pipeline.py`; that wrapper remains transitional until parity and migration evidence are sufficient for safe retirement.

## 16. Non-goals

This contract does not establish final writing style, scientific or clinical validity, production citation UI, production tradition policy, or production routing.

**Current state: REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE.**
