# Typed Tradition Wrapper Retirement Readiness

Status: **REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE**

Baseline audited: `72fe201c3f04c91771a4e382b5886c86a7ea0354`

Target wrapper:

```text
references/astrology/typed_tradition_pipeline.py
```

## Decision

The wrapper is now **dependency-ready for retirement, but not yet validation-ready for deletion**.

It must remain present until the dedicated Astrology regression files that cover the direct v0.2 core path and wrapper parity have actually been executed in a trustworthy environment.

## Repository caller audit

Search terms audited:

```text
typed_tradition_pipeline
run_typed_pipeline
retrieve_typed_claims
validate_typed_resolution
compose_typed_synthesis
```

### Maintained executable callers before this migration

Two categories existed:

1. `test_typed_tradition_pipeline.py`
   - intentionally tests the deprecated wrapper itself;
   - retained as parity/deprecation coverage until wrapper deletion.

2. `test_registry_typed_context_migration.py`
   - was a real-registry regression that still imported `retrieve_typed_claims` from the wrapper;
   - this was the last maintained external consumer of wrapper behavior.

This migration changes `test_registry_typed_context_migration.py` to call the canonical core selector directly:

```python
retrieve_claims(registry, route, taxonomy)
```

It no longer imports `typed_tradition_pipeline.py`.

### Non-runtime references

The remaining references outside the wrapper parity test are research-history / migration / contract documents. They describe why the wrapper exists or existed; they are not executable dependencies.

Historical research records should not be rewritten merely to erase accurate history.

## Canonical v0.2 execution path

The maintained typed path is now:

```text
validate_astrology_query_resolution.py
→ retrieve_interpretation_claims.py
→ compose_interpretation_synthesis.py
```

with:

```text
schema_version = 0.2.0-research
tradition_context_refs_any[]
synthesis_mode
versioned tradition taxonomy
```

`typed_tradition_pipeline.py` is not a semantic authority.

## Retirement gates

Deletion of `typed_tradition_pipeline.py` and `test_typed_tradition_pipeline.py` is permitted only after all of the following are true:

1. **No maintained external caller**
   - repo search finds no executable import/call outside the wrapper's own parity test.

2. **Direct-core v0.2 regression executed**
   - `test_typed_contract_v0_2.py` is actually run and passes.

3. **Registry migration regression executed**
   - `test_registry_typed_context_migration.py` is actually run and passes using the core selector.

4. **Wrapper parity regression executed before deletion**
   - `test_typed_tradition_pipeline.py` is actually run and passes, proving the wrapper delegates without semantic drift immediately before removal.

5. **Legacy v0.1 compatibility remains independently covered**
   - wrapper deletion must not remove the explicit v0.1 flat-tag compatibility regression in the core contract tests.

6. **Fresh repository search immediately before deletion**
   - repeat the caller audit on current `main`; do not rely on this readiness record if later sessions add new callers.

7. **Scope remains bounded**
   - wrapper retirement must not modify root routing, production admission, claim meanings, source admission, taxonomy doctrine, or Palmistry files.

## Current validation boundary

The repository's current root `Validate Playbook` workflow does not automatically execute the dedicated tests under `references/astrology/`.

Therefore:

```text
green root CI != proof that retirement gates 2–4 have executed
```

This is the only current blocker identified by the retirement audit.

## Recommended next action

Before deleting the wrapper, obtain actual execution evidence for the dedicated Astrology regression set in a bounded environment. If those tests pass and a fresh caller audit remains clean, wrapper deletion can proceed as a separate small PR.

## Non-goals

This readiness decision does not:

- promote Astrology research to production;
- alter tradition taxonomy content;
- change interpretation claims;
- change source admission;
- claim scientific or predictive validity;
- remove v0.1 core compatibility;
- authorize changing repository-level CI without separate scope.

**Current conclusion: dependency-ready, validation evidence pending.**
