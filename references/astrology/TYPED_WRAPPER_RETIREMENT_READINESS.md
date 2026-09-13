# Typed Tradition Wrapper Retirement Readiness

Status: **REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE**

Baseline audited: `bc75650e5cf0d618a3b8f98f17491b6cb91d277e`

Target wrapper:

```text
references/astrology/typed_tradition_pipeline.py
```

## Decision at readiness audit

The wrapper was **dependency-ready for retirement, but not yet validation-ready for deletion** when this readiness record was created.

It was required to remain present until the dedicated Astrology regression files covering the direct v0.2 core path and wrapper parity were actually executed in a trustworthy environment.

## Repository caller audit

Search terms audited:

```text
typed_tradition_pipeline
run_typed_pipeline
retrieve_typed_claims
validate_typed_resolution
compose_typed_synthesis
```

### Maintained executable callers before migration

Two categories existed:

1. `test_typed_tradition_pipeline.py`
   - intentionally tested the deprecated wrapper itself;
   - retained as parity/deprecation coverage until wrapper deletion.

2. `test_registry_typed_context_migration.py`
   - was a real-registry regression that still imported `retrieve_typed_claims` from the wrapper;
   - this was the last maintained external consumer of wrapper behavior.

The readiness migration changed `test_registry_typed_context_migration.py` to call the canonical core selector directly:

```python
retrieve_claims(registry, route, taxonomy)
```

It no longer imports `typed_tradition_pipeline.py`.

### Non-runtime references

The remaining references outside the wrapper parity test were research-history / migration / contract documents. They described why the wrapper exists or existed; they were not executable dependencies.

Historical research records should not be rewritten merely to erase accurate history.

## Canonical v0.2 execution path

The maintained typed path is:

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

`typed_tradition_pipeline.py` was never a semantic authority after core v0.2 promotion.

## Retirement gates

Deletion of `typed_tradition_pipeline.py` and `test_typed_tradition_pipeline.py` was permitted only after all of the following became true:

1. **No maintained external caller**
   - repo search found no executable import/call outside the wrapper's own parity test.

2. **Direct-core v0.2 regression executed**
   - `test_typed_contract_v0_2.py` actually ran and passed.

3. **Registry migration regression executed**
   - `test_registry_typed_context_migration.py` actually ran and passed using the core selector.

4. **Wrapper parity regression executed before deletion**
   - `test_typed_tradition_pipeline.py` actually ran and passed, proving the wrapper delegated without semantic drift immediately before removal.

5. **Legacy v0.1 compatibility remains independently covered**
   - wrapper deletion does not remove the explicit v0.1 flat-tag compatibility regression in the core contract tests.

6. **Fresh repository search immediately before deletion**
   - caller audit was repeated on current `main` rather than relying only on the earlier readiness record.

7. **Scope remains bounded**
   - wrapper retirement does not modify root routing, production admission, claim meanings, source admission, taxonomy doctrine, or Palmistry files.

## Validation boundary at readiness time

The repository root `Validate Playbook` workflow did not automatically execute the dedicated tests under `references/astrology/`.

Therefore:

```text
green root CI != proof that retirement gates 2–4 executed
```

That was the final blocker identified by the readiness audit.

## Retirement outcome

Immediately before wrapper deletion, an isolated exact-blob regression bundle was reconstructed from audited main:

```text
9645c8206d61085c4047eb53375a7548975e75de
```

All 11 reconstructed source/test/fixture files matched their Git blob SHA from that exact commit.

Execution under Python `3.13.5` produced:

```text
test_typed_contract_v0_2.py                 10 / 10 PASS
test_registry_typed_context_migration.py    11 / 11 PASS
test_typed_tradition_pipeline.py            11 / 11 PASS
combined                                      32 / 32 PASS
```

A fresh caller audit remained clean. Full execution provenance is recorded in:

```text
TYPED_WRAPPER_RETIREMENT_EXECUTION_RESULTS.md
```

Therefore all retirement gates were satisfied, and the deprecated wrapper plus its wrapper-only parity test could be removed while retaining direct-core regression coverage and explicit v0.1 core compatibility.

## Non-goals

This readiness / retirement decision does not:

- promote Astrology research to production;
- alter tradition taxonomy content;
- change interpretation claims;
- change source admission;
- claim scientific or predictive validity;
- remove v0.1 core compatibility;
- authorize changing repository-level CI without separate scope.

**Current conclusion: retirement gates satisfied; deprecated wrapper retirement authorized by exact-blob 32 / 32 regression evidence.**
