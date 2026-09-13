# Registry Typed Context Migration Results

Status: **REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE**

Baseline: `masini1491/ai-divination-playbook@f34c9350d4c5e18ce329e30e2ed0cef607a73d4a`

## Scope

This migration adds explicit typed Astrology context fields only to the two current real interpretation claim-family registries:

- `domicile_claim_family_registry.json`
- `saturn_moon_aspect_claim_family_registry.json`

It preserves existing `tradition_tags[]` as source-local / legacy discovery metadata.

No production routing, root governance, Palmistry file, source admission status, normalized claim statement, confidence status, support status, or conflict resolution was changed.

## Migration rule

The migration follows a conservative parity rule:

```text
if legacy tag projection already resolves to a canonical doctrine/school context
→ write the same explicit tradition_context_refs[]

if the claim is historical/meta rather than reading doctrine
→ tradition_context_refs = []
→ add historical_context_refs[] / meta_context_refs[] only when the taxonomy has a canonical mapping

if legacy tags are ambiguous or conditional for doctrine routing
→ tradition_context_refs = []
→ do not guess a doctrine/school
```

Explicit empty arrays are intentional. They freeze the fail-closed state instead of allowing broad tags such as `classical`, `modern`, or `blended` to become doctrine selectors by accident.

## Domicile registry

### Canonical doctrine projection

The following claims now carry:

```text
tradition_context_refs:
- lineage:hellenistic:ptolemaic
```

Claims:

- `claim:domicile-configuration`
- `claim:ptolemaic-seasonal-rationale`

This matches the prior deterministic legacy projection from the `ptolemaic` tag.

### Historical/meta claim

`claim:southern-hemisphere-reversal-debate` now carries:

```text
tradition_context_refs: []
historical_context_refs:
- context:early_modern
meta_context_refs:
- meta:history_of_astrology
```

This preserves the source as historical scholarship about doctrine disagreement without turning scholarship into a natal-reading tradition.

### Ambiguous practitioner claim

`claim:modern-practitioner-domicile-capacity` now carries:

```text
tradition_context_refs: []
```

The existing `modern_practitioner` + `classical` tags do not identify one canonical doctrine/school in the current taxonomy, so no typed doctrine was invented.

## Saturn–Moon registry

### Ptolemaic claims

These claims now carry:

```text
tradition_context_refs:
- lineage:hellenistic:ptolemaic
```

- `claim:ptolemy-major-aspect-geometry`
- `claim:ptolemy-moon-configured-planets-soul`
- `claim:ptolemy-saturn-regards-moon-maternal-context`

### Historiography claim

`claim:campion-classical-astrology-diversity` now carries:

```text
tradition_context_refs: []
meta_context_refs:
- meta:history_of_astrology
```

It remains scholarship about historical diversity and source interpretation, not an interpretation school.

### Psychological astrology claims

These claims now carry:

```text
tradition_context_refs:
- school:modern:psychological_astrology
```

- `claim:greene-moon-saturn-parent-image`
- `claim:reference-opposition-polarity`

Both already had a legacy `psychological_astrology` tag whose deterministic taxonomy mapping resolves to that school.

### Ambiguous blended implementation claims

These claims now carry explicit empty doctrine refs:

```text
tradition_context_refs: []
```

- `claim:reference-conjunction-fusion`
- `claim:reference-square-friction`

Their existing `modern` and `blended` tags are not canonical doctrine selectors. `blended` is a synthesis mode, not a reading tradition.

## Regression fixture

`test_registry_typed_context_migration.py` contains 11 deterministic cases covering:

- legacy-projection parity for Ptolemaic claims;
- legacy-projection parity for psychological-astrology claims;
- historical/meta claims remaining non-doctrine;
- ambiguous practitioner/blended claims remaining non-doctrine;
- every non-empty explicit tradition ref resolving to a taxonomy context whose dimension is `doctrinal_lineage` or `interpretive_school`;
- typed retrieval of the actual domicile Ptolemaic claim;
- typed retrieval of the actual Greene Moon–Saturn opposition claim.

## Validation boundary

The repository's current GitHub Actions workflow runs root `tests/` discovery plus `tools/playbook_check.py`. It does not automatically discover `references/astrology/test_registry_typed_context_migration.py`.

Therefore:

- a green repository CI result demonstrates the existing repository validation remained green;
- it must **not** be reported as proof that the 11 dedicated migration tests executed unless a runtime actually runs that file;
- the migration fixture remains deterministic executable research evidence for a later dedicated Astrology validation step.

## Result

The two real claim registries now have explicit typed routing metadata where current evidence supports it, while legacy discovery tags remain intact and ambiguous/meta-only claims remain fail-closed.

No production authority is granted.

**Current state: REFERENCE-ONLY / RESEARCH / NOT PRODUCTION-ROUTABLE.**
