# Astrology Registry v0.2 Execution Results

Status: **REFERENCE-ONLY / RESEARCH EXECUTION EVIDENCE / NOT PRODUCTION-ROUTABLE**

## Scope

This record closes the dedicated-execution evidence gap left after the `interpretation_claim_registry@0.2.0-research` hardening merge.

Audited canonical baseline:

```text
main = 524e6dff589743c2710521e8cba5ce4046fffd3e
```

The executed Astrology regression modules were:

```text
references/astrology/test_interpretation_claim_registry_validator.py
references/astrology/test_retrieve_interpretation_claims.py
references/astrology/test_registry_typed_context_migration.py
references/astrology/test_typed_contract_v0_2.py
```

No Palmistry test or research file was added to this execution scope.

## Execution method

The repository's existing GitHub Actions workflow normally executes only:

```text
python -m unittest discover -s tests -v
python tools/playbook_check.py .
```

To obtain direct execution evidence without permanently expanding root CI ownership, PR #25 temporarily added a single unittest bridge under `tests/`.

The bridge:

- added `references/astrology/` to `sys.path`;
- imported exactly the four existing Astrology regression modules listed above;
- delegated test discovery to their existing `unittest.TestCase` definitions;
- did not duplicate or rewrite Astrology test logic.

The temporary bridge is removed before final merge. It is execution scaffolding only and is not a new canonical test owner.

## Infrastructure retry boundary

The first workflow attempt was:

```text
Validate Playbook run #196
run id: 34748414902
head: 5a414dcf59cdc0589c26bf98deb77f96d5358e4a
```

GitHub reported the job as failed, but the job had:

```text
steps = []
runner_id = 0
```

No checkout, Python setup, unittest command, or repository code executed. This attempt is therefore classified as **runner infrastructure failure**, not a regression failure, and is not counted as execution evidence.

A no-semantic-change bridge retry produced a second workflow run.

## Successful execution

Canonical execution evidence:

```text
Validate Playbook run #197
run id: 34748471666
job id: 103700640184
PR: #25
branch head: a2cfc1590fbc497ec5c1cc56a0dd18e8e29f291a
PR merge-ref checkout: 61f80960a3cc6fb72f10cf83ba7c95a4f3791e09
base main: 524e6dff589743c2710521e8cba5ce4046fffd3e
conclusion: success
```

Execution environment reported by GitHub Actions:

```text
runner image: ubuntu-24.04
OS: Ubuntu 24.04.5 LTS
Python: CPython 3.12.14
```

The workflow executed:

```text
python -m unittest discover -s tests -v
```

Observed overall result:

```text
Ran 100 tests in 0.230s
OK
```

No skip, expected-failure, failure, or error summary was reported.

## Dedicated Astrology result

The temporary bridge caused exactly the following dedicated Astrology suites to be included in the 100-test run.

### 1. Registry validator

```text
test_interpretation_claim_registry_validator.py
27 tests
27 PASS
```

This includes explicit v0.2 coverage for:

- taxonomy required;
- current real registries are v0.2 and validate;
- explicit empty `tradition_context_refs[]` is valid;
- missing typed context field fails;
- unknown typed context ref fails;
- duplicate typed context ref fails;
- meta context in doctrine selector fails;
- historical/meta context dimensions are checked;
- v0.1 compatibility remains valid without taxonomy;
- source/conflict/privacy/production guards remain enforced.

### 2. Retrieval regressions

```text
test_retrieve_interpretation_claims.py
20 tests
20 PASS
```

This includes both synthetic v0.1 compatibility and current v0.2 real-registry retrieval cases.

### 3. Real-registry typed-context migration

```text
test_registry_typed_context_migration.py
11 tests
11 PASS
```

This confirms the two real registries retain their intended doctrine/non-doctrine projections and typed selection behavior after v0.2 hardening.

### 4. Native typed v0.2 core contract

```text
test_typed_contract_v0_2.py
12 tests
12 PASS
```

This includes the new fail-closed assertion that a malformed v0.2 registry is rejected before claim selection, plus v0.1 legacy-path compatibility.

Dedicated Astrology total:

```text
27 + 20 + 11 + 12 = 70
70 / 70 PASS
```

## Root structural validation

The same workflow then executed:

```text
python tools/playbook_check.py .
```

Observed result:

```text
PASS playbook structure
```

This is recorded separately from the 70-test Astrology execution evidence; structural validation does not substitute for the dedicated regressions.

## Evidence interpretation

This execution supports the bounded claim that, at the audited v0.2 baseline:

```text
registry v0.2 taxonomy-aware validation
+
retrieval preflight
+
real-registry typed-context migration
+
native typed query/retrieval/L5 core path
+
legacy v0.1 compatibility
```

are mutually regression-compatible under the executed test fixtures.

It does **not** establish:

- scientific or predictive validity of Astrology;
- production method admission;
- correctness of every future claim family;
- completeness of historical source coverage;
- production routing authority;
- automatic cross-validation with Tarot, Meihua, Liuyao, or Palmistry.

## Current decision

The dedicated execution gap identified in `REGISTRY_V0_2_TYPED_CONTEXT_HARDENING_RESULTS.md` is now closed for the audited baseline:

```text
Astrology registry v0.2 dedicated regressions = 70 / 70 PASS
root unit-test suite with temporary bridge = 100 / 100 PASS
root structural checker = PASS
```

The temporary execution bridge is intentionally not retained in `main`.

**Current state: REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE.**
