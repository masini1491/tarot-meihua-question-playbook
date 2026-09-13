# Astrology Interpretation Claim Registry Schema Draft

Status: **REFERENCE-ONLY / RESEARCH SCHEMA / NOT PRODUCTION-ROUTABLE**

Schema name: `interpretation_claim_registry`

Current schema version: `0.2.0-research`

Legacy supported version: `0.1.0-research`

This contract governs sourced L3/L4 Astrology interpretation claim-family registries. It does not choose a production tradition, doctrine, orb policy, scientific-validity position, or predictive authority.

## 1. Version boundary

`0.1.0-research` froze canonical source/claim/conflict/provenance fields. Later research added typed tradition contexts to real registries and to query/retrieval/L5 contracts. Because those typed fields now affect deterministic retrieval semantics, they are no longer treated as an invisible optional extension of 0.1.

```text
0.1.0-research
→ canonical source / claim / conflict / privacy / production guards
→ legacy flat tradition tags remain compatible

0.2.0-research
→ all 0.1 canonical requirements
+ taxonomy-aware typed context contract
+ retrieval preflight must validate the registry before claim selection
```

The same schema version must not silently change meaning.

## 2. Top-level record

Required canonical shape:

```text
schema_name
schema_version
record_status
record_kind
record_id
production_routable
sources[]
claims[]
conflict_groups[]
privacy
```

Required research guards:

```text
schema_name = interpretation_claim_registry
schema_version = 0.2.0-research   # current registries
record_status = REFERENCE-ONLY
record_kind = interpretation_claim_family_registry
production_routable = false
privacy.contains_real_birth_data = false
```

Optional family metadata may include `claim_family`, `subject`, `lineage_rules`, `research_result`, `non_admitted_claims`, `retrieval_contract`, and notes.

## 3. Source record

Minimum canonical fields:

```text
source_id
source_role
admission_status[]
storage_mode[]
independence_status
```

Recommended provenance fields when known:

```text
title
author_or_org
source_kind
tradition_tags[]
publication_or_release_date
edition
immutable_revision
locator
language
license_status
license_identifier
copyright_status
verification_status[]
admission_scope[]
excluded_scope[]
upstream_source_refs[]
derivative_relationship
notes[]
```

Versioned registries use canonical field names; legacy `author`, `revision`, and `admission_state` aliases are not accepted in versioned records.

Accepted source roles remain:

```text
PRIMARY_TEXT
SCHOLARLY_SECONDARY
PRACTITIONER_REFERENCE
REFERENCE_IMPLEMENTATION
UNVERIFIED_WEB_SOURCE
PROJECT_SYNTHESIS
```

`PRODUCTION_ADMITTED` is forbidden by the research validator. `UNVERIFIED_WEB_SOURCE` cannot be promoted into claim/policy/production admission.

## 4. Claim record

Minimum canonical fields:

```text
claim_id
layer
claim_type
normalized_statement
source_refs[]
confidence_status
support_status
conflict_group_ids[]
```

The registry covers L3/L4 only. L1/L2 deterministic astronomy facts belong to Structured Astrology Fact. L5 synthesis is not stored as source evidence.

Accepted confidence labels:

```text
supported
qualified
provisional
conflicted
unsupported
```

Accepted support labels:

```text
single_source_supported
multi_source_supported
tradition_bounded
qualified
conflicted
historical_only
architecture_only
unsupported
```

Repeated downstream copies do not create independent evidence. `REFERENCE_ONLY` sources cannot self-promote an unqualified supported claim.

## 5. Typed context contract — v0.2

Every v0.2 claim must explicitly declare:

```text
tradition_context_refs[]
```

An empty array is meaningful and valid: it means the claim deliberately has no admitted doctrinal-lineage / interpretive-school selector.

The validator requires the current research taxonomy and checks every ref before retrieval.

### 5.1 Doctrine / school refs

`tradition_context_refs[]` may reference only taxonomy contexts whose dimension is:

```text
doct rinal_lineage
interpretive_school
```

Unknown refs, duplicate refs, historical contexts, meta contexts, synthesis modes, and implementation modes are invalid in this array.

### 5.2 Historical refs

When present:

```text
historical_context_refs[]
```

may reference only:

```text
historical_context
```

### 5.3 Meta refs

When present:

```text
meta_context_refs[]
```

may reference only:

```text
meta_perspective
```

A history-of-astrology marker therefore cannot be smuggled into `tradition_context_refs[]` merely to make a claim selectable as doctrine.

### 5.4 No silent repair

Malformed explicit typed refs invalidate the registry. Retrieval must not silently:

```text
drop the bad ref
fall back to legacy tags for that claim
select the remaining valid subset
substitute another tradition
```

This is the main semantic reason for the 0.2 version boundary.

## 6. Taxonomy dependency

A v0.2 registry cannot be fully validated without `tradition_taxonomy_example.json` or another taxonomy satisfying the same research taxonomy contract.

Validator behavior:

```text
v0.2 registry + no taxonomy
→ TAXONOMY_REQUIRED_FOR_REGISTRY_V2
→ invalid

v0.2 registry + invalid taxonomy
→ TAXONOMY_INVALID_FOR_REGISTRY_V2
→ invalid

v0.1 registry
→ remains structurally valid without taxonomy
```

This means legacy query compatibility does not imply that a v0.2 registry may bypass its own taxonomy dependency.

## 7. Retrieval preflight

`retrieve_interpretation_claims.py` must validate the registry before claim selection.

```text
query validation
→ registry schema/version gate
→ full registry validation
→ only then claim selection
```

For v0.2 registries, the same taxonomy supplied to typed retrieval is also used to validate registry typed refs.

If registry validation fails:

```text
retrieval_status = registry_not_research_safe
selected_claim_ids = []
```

A malformed typed ref therefore becomes an explicit registry failure rather than a misleading `no_match`.

## 8. Conflict, privacy, and production guards

Conflict groups preserve incompatible doctrines/scopes without averaging them into false consensus.

Every versioned registry must keep:

```text
record_status = REFERENCE-ONLY
production_routable = false
privacy.contains_real_birth_data = false
```

The validator also rejects explicit production authority or scientific predictive-validity promotion in research-result metadata.

## 9. Compatibility policy

Supported states:

```text
unversioned early research fixtures
→ bounded alias compatibility

0.1.0-research
→ canonical legacy registry shape
→ no taxonomy requirement
→ legacy flat-tag retrieval remains available

0.2.0-research
→ canonical typed registry shape
→ taxonomy required
→ explicit typed-context invariants enforced
```

Current real registries are migrated to v0.2. Historical validation documents describing their earlier v0.1 state remain historical records and are not rewritten.

## 10. Migration rule

0.1 → 0.2 migration may:

```text
change schema_version
retain existing explicit tradition_context_refs[]
add explicit empty tradition_context_refs[] where doctrine selection is intentionally absent
retain historical_context_refs[] / meta_context_refs[] in their own dimensions
```

Migration must not:

```text
invent a doctrine ref from an ambiguous legacy tag
upgrade source admission
upgrade confidence/support
resolve conflicts
create predictive/clinical authority
alter normalized claim meaning
```

## 11. Current decision

The registry contract is now aligned with the typed query/retrieval/L5 architecture:

```text
explicit typed claim contexts
→ taxonomy-aware registry validation
→ fail-closed retrieval preflight
→ typed query selection
→ provenance-preserving L5 synthesis
```

**Current state: REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE.**
