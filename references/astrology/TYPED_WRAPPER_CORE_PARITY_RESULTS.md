# Typed Tradition Wrapper / Core Parity Results

Status: **REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE**

Baseline main: `9bdc14edf53f019c95f221304db6cbfffe243f33`

## Purpose

After typed tradition routing moved into the core `0.2.0-research` query-resolution, retrieval, and L5 contracts, the earlier `typed_tradition_pipeline.py` wrapper still contained an independent copy of validation, claim prefiltering, tradition coverage, and synthesis behavior.

That duplication created a semantic-drift risk. In particular, the old wrapper converted typed routes back into a legacy-shaped compatibility copy before calling the query validator. Once the core validator made taxonomy-backed typed fields mandatory for v0.2, that technique became stale.

This round removes the duplicate execution semantics while preserving import compatibility.

## Decision

`typed_tradition_pipeline.py` is retained as a **deprecated transitional compatibility facade**.

It no longer owns:

- taxonomy validation semantics;
- typed-route validation semantics;
- claim prefiltering;
- tradition coverage calculation;
- incomplete-coverage blocking;
- typed provenance augmentation;
- L5 typed disclosure logic.

Those behaviors are owned only by:

```text
validate_astrology_query_resolution.py
retrieve_interpretation_claims.py
compose_interpretation_synthesis.py
```

The wrapper now delegates directly to those core functions.

## Public compatibility surface retained

The following helper names remain available:

```text
validate_typed_resolution(...)
retrieve_typed_claims(...)
compose_typed_synthesis(...)
run_typed_pipeline(...)
```

This prevents existing research callers from failing imports while making the core contracts the single semantic authority.

The wrapper exposes:

```text
WRAPPER_STATUS = DEPRECATED_TRANSITIONAL
```

and `run_typed_pipeline(...)` reports that status.

## Version boundary

The deprecated typed wrapper accepts only:

```text
schema_version = 0.2.0-research
```

A pre-v0.2 typed envelope returns:

```text
TYPED_WRAPPER_REQUIRES_V02
```

This does **not** remove the real v0.1 legacy compatibility path. Legacy flat-tag fixtures remain supported directly by the core `0.1.0-research` compatibility contract and its dedicated regressions.

The rejected shape is specifically the obsolete hybrid:

```text
0.1 schema identity + typed tradition fields
```

which predates the formal v0.2 typed contract.

## Fixture migration

`test_typed_tradition_pipeline.py` was migrated from the obsolete `0.1 + typed fields` research shape to canonical v0.2 typed envelopes.

The migrated tests compare the deprecated wrapper directly against core execution for the same registry, resolution, and taxonomy.

Authored parity cases cover:

1. wrapper explicitly reports deprecated-transitional status;
2. wrapper validation equals core validation;
3. wrapper retrieval equals core retrieval;
4. wrapper synthesis equals core synthesis;
5. full single-school pipeline parity;
6. mixed legacy/typed selector invalidity parity;
7. non-doctrine typed context invalidity parity;
8. complete parallel-comparison parity;
9. partial parallel-coverage blocking parity;
10. explicit-blend parity;
11. obsolete pre-v0.2 typed fixture rejection.

## Authority result

After this change the execution authority is:

```text
v0.2 typed query-resolution contract
→ core validator
→ core selector
→ core retrieval provenance bundle
→ core composer
→ L5 envelope
```

The deprecated wrapper is only:

```text
legacy caller API
→ thin delegation
→ same core path
```

No second typed routing algorithm remains in the wrapper.

## Scope preserved

This round does not change:

- astrology claim meanings;
- source admission;
- confidence/support status;
- conflict resolution;
- tradition taxonomy content;
- registry typed context mappings;
- root routing;
- Palmistry files;
- production authority.

No real birth data or private user data is introduced.

## Validation boundary

The repository's existing root workflow does not automatically execute dedicated Python tests under `references/astrology/`.

Therefore the 11 parity cases are executable research regressions authored in-repository, but a green root CI run must not be described as proof that these 11 cases executed.

## Retirement criterion

Deletion of `typed_tradition_pipeline.py` is **not** authorized by this round.

A future retirement round should first establish that:

1. no maintained research caller imports the wrapper;
2. all canonical typed fixtures call core v0.2 functions directly;
3. no documentation names the wrapper as the preferred execution path;
4. parity regressions have served at least one stable migration cycle;
5. removal does not break a declared compatibility surface.

Until then, keep the wrapper as a small deprecated facade rather than a duplicate implementation.

**Current state: REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE.**
