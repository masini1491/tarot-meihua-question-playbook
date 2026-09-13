# First–Seventh House Axis Execution Results

Status: **REFERENCE-ONLY / RESEARCH EXECUTION EVIDENCE / NOT PRODUCTION-ROUTABLE**

Baseline under test: `8aeb16243e36bd381c4de39183555e69e66aaa4d`

Feature branch head executed: `f487b6e22f2f6645899b3fd6f5eba261926f4138`

PR merge-ref checkout executed by GitHub Actions: `8c0f8743c32708ad42ce379f4d376fd164d95ede`

## 1. Execution environment

GitHub Actions workflow:

```text
Validate Playbook #201
run id: 34750982010
job id: 103707360781
```

Environment reported by the runner:

```text
Ubuntu 24.04.5 LTS
CPython 3.12.14
runner 2.337.0
```

The repository workflow executed:

```text
python -m unittest discover -s tests -v
python tools/playbook_check.py .
```

A temporary root unittest bridge imported the dedicated Astrology modules so they were executed by the existing workflow. The bridge contained no duplicated interpretation or validation logic and was removed after evidence capture.

## 2. New claim-family regression

Module:

```text
references/astrology/test_first_seventh_house_axis_registry.py
```

Result:

```text
8 / 8 PASS
```

Cases executed:

1. v0.2 registry validates against the current research taxonomy.
2. Hellenistic first-house typed route selects only the Valens first-place claim.
3. Hellenistic seventh-house typed route selects only the Valens seventh-place claim.
4. Early-modern discovery selects the Lilly first-house claim without inventing a typed doctrine context.
5. REFERENCE_ONLY modern first-house identity claim is excluded without explicit opt-in.
6. The same REFERENCE_ONLY claim can be included only as qualified evidence with explicit opt-in.
7. A house-axis route that declares required L2 facts fails closed when those refs are absent.
8. Modern reference house claims remain without a silently inferred psychological-school context.

## 3. Related Astrology suites executed in the same run

The bridge also executed the already-maintained registry/retrieval/typed-contract suites:

```text
test_interpretation_claim_registry_validator.py   27 / 27 PASS
test_retrieve_interpretation_claims.py            20 / 20 PASS
test_registry_typed_context_migration.py           11 / 11 PASS
test_typed_contract_v0_2.py                        12 / 12 PASS
```

Together with the new eight cases:

```text
Dedicated Astrology tests in this execution: 78 / 78 PASS
```

## 4. Full repository result

The same workflow log reported:

```text
Ran 108 tests in 0.241s
OK
```

Structural validation then reported:

```text
PASS playbook structure
```

Therefore the new family did not break the root test suite or repository structural checker in this execution.

## 5. What this execution establishes

Within the research contracts tested here, the evidence supports that:

- the new first/seventh-axis registry satisfies the current v0.2 taxonomy-aware registry validator;
- explicit Hellenistic typed retrieval does not silently import Lilly, Houlding, or modern reference wording;
- early-modern material can remain discoverable without being falsely promoted to a Hellenistic typed lineage;
- REFERENCE_ONLY modern framing stays opt-in and qualified;
- existing L2 precondition machinery can fail closed for a house-axis route when required Ascendant/house facts are missing;
- current registry v0.2, retrieval, typed migration, and typed-core regressions remain green alongside the new family.

## 6. What this execution does not establish

It does **not** establish:

- scientific or predictive validity of astrological houses;
- a production house-system policy;
- that registry metadata automatically forces every caller to request L2 house facts;
- that modern identity/projection language belongs to Valens or Lilly;
- that the wvanderen house modules are canonical psychological-school doctrine;
- production Astrology admission.

The generic retrieval engine still enforces the L2 gate only when the route declares `requires_l2_facts=true`. Automatic derivation of required L2 roles from registry metadata remains out of scope.

## 7. Persistent-diff boundary

The root unittest bridge was temporary execution scaffolding and is removed before merge.

Persistent artifacts for this round are limited to:

```text
FIRST_SEVENTH_HOUSE_AXIS_EVIDENCE.md
first_seventh_house_axis_claim_family_registry.json
test_first_seventh_house_axis_registry.py
FIRST_SEVENTH_HOUSE_AXIS_EXECUTION_RESULTS.md
```

All remain under `references/astrology/**`.

Palmistry, root production routing, production method owners, runtime authority and private user data are untouched.
