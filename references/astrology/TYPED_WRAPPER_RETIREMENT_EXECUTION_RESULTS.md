# Typed Tradition Wrapper Retirement Execution Results

Status: **REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE**

Exact audited main: `9645c8206d61085c4047eb53375a7548975e75de`

Runtime: `Python 3.13.5`

## Purpose

This record supplies the execution evidence required by `TYPED_WRAPPER_RETIREMENT_READINESS.md` before deleting the deprecated `typed_tradition_pipeline.py` facade.

The test environment was reconstructed from GitHub-connector reads at the exact audited commit. Repository acquisition did not use raw `git clone` or `curl`.

## Exact-blob identity

The isolated regression bundle contained only the minimum local modules, tests, and JSON fixtures needed by the dedicated typed-contract regressions. Before execution, every reconstructed file was verified against its Git blob SHA from exact main.

| File | Git blob SHA | Result |
|---|---|---|
| `compose_interpretation_synthesis.py` | `b3c4e6aa9a6a4d6992716c70c9bb0a361c1fa020` | match |
| `retrieve_interpretation_claims.py` | `8bdfde934cc7e93b61d3f29853f88ec87e571794` | match |
| `validate_astrology_query_resolution.py` | `de6eeb1d1d56b5352ccfb38ef1c443810c5cb8db` | match |
| `typed_tradition_routing.py` | `257a87e45f27889fc24850c946fac456e3c7f221` | match |
| `typed_tradition_pipeline.py` | `16534b9e55032c52e969d020cd1ee546b7cac20a` | match |
| `test_typed_contract_v0_2.py` | `92d97fb014804af076d04b66a1290755a38326bc` | match |
| `test_registry_typed_context_migration.py` | `4a713b2d10fa3125adb7cec83a9449eb2a419873` | match |
| `test_typed_tradition_pipeline.py` | `451de946115814017b0695a2e82a6202f5d0e643` | match |
| `tradition_taxonomy_example.json` | `741ee2f9fa8446f58fd408770e06698457213394` | match |
| `saturn_moon_aspect_claim_family_registry.json` | `2e039281d901e456c42b95634eb68f4f171509c1` | match |
| `domicile_claim_family_registry.json` | `01634167ed5b20ee16f4119adb6af2482b1d266e` | match |

Result:

```text
ALL_BLOBS_MATCH = True
```

## Pre-retirement execution

Executed command:

```text
python3 -m unittest -v \
  test_typed_contract_v0_2.py \
  test_registry_typed_context_migration.py \
  test_typed_tradition_pipeline.py
```

Results:

```text
test_typed_contract_v0_2.py                 10 / 10 PASS
test_registry_typed_context_migration.py    11 / 11 PASS
test_typed_tradition_pipeline.py            11 / 11 PASS
--------------------------------------------------------
combined                                      32 / 32 PASS
```

Combined unittest result:

```text
Ran 32 tests
OK
```

The earlier per-file execution also returned process status `0` for all three files.

## Post-retirement direct-core simulation

After the pre-retirement parity run, the isolated sandbox copies of:

```text
typed_tradition_pipeline.py
test_typed_tradition_pipeline.py
```

were removed to simulate the proposed repository state. The two maintained direct-core regression files were then executed again:

```text
python3 -m unittest -v \
  test_typed_contract_v0_2.py \
  test_registry_typed_context_migration.py
```

Result:

```text
test_typed_contract_v0_2.py                 10 / 10 PASS
test_registry_typed_context_migration.py    11 / 11 PASS
--------------------------------------------------------
post-retirement maintained suite             21 / 21 PASS
```

Combined unittest result:

```text
Ran 21 tests
OK
```

This confirms the maintained direct-core regressions do not import or require the retired wrapper.

## Retirement gate assessment

The execution evidence establishes, immediately before retirement, that:

- native v0.2 query validation / retrieval / L5 behavior passes its direct-core regression;
- real migrated registries pass their typed-context migration regression through the core selector;
- the deprecated wrapper matches the direct core for validation, retrieval, composition, single-tradition, parallel-comparison, incomplete-coverage, and explicit-blend cases;
- the wrapper still rejects the obsolete pre-v0.2 typed hybrid fixture;
- the explicit v0.1 flat-tag core compatibility regression remains present and passes independently of wrapper existence;
- after removing the wrapper from the isolated sandbox, the maintained direct-core suite still passes `21 / 21`.

A fresh repository caller audit at exact main found no maintained executable consumer outside the wrapper's own parity test.

Therefore the dependency and execution-evidence gates for wrapper retirement are satisfied.

## CI boundary

The repository root `Validate Playbook` workflow still does **not** automatically execute these dedicated Astrology tests.

Therefore:

```text
32 / 32 pre-retirement parity result = independently executed exact-blob evidence
21 / 21 post-retirement direct result = independently executed wrapper-free evidence
green root CI                         != proof of dedicated Astrology test execution
```

These statements must remain distinguishable.

## Scope boundary

Wrapper retirement does not change:

- v0.2 core semantics;
- v0.1 legacy core compatibility;
- tradition taxonomy doctrine;
- interpretation claim meanings;
- source admission or confidence;
- conflict handling;
- root routing or production authority;
- Palmistry files.

No real birth data is present in these fixtures.

**Conclusion: typed wrapper retirement execution gate satisfied — 32 / 32 pre-retirement parity PASS and 21 / 21 wrapper-free direct-core PASS.**
