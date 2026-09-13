#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from retrieve_interpretation_claims import retrieve_claims
from typed_tradition_routing import canonical_tradition_refs_for_claim


class RegistryTypedContextMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        here = Path(__file__).resolve().parent
        cls.taxonomy = json.loads((here / "tradition_taxonomy_example.json").read_text(encoding="utf-8"))
        cls.domicile = json.loads((here / "domicile_claim_family_registry.json").read_text(encoding="utf-8"))
        cls.saturn_moon = json.loads((here / "saturn_moon_aspect_claim_family_registry.json").read_text(encoding="utf-8"))

    def _legacy_projection(self, claim):
        legacy = copy.deepcopy(claim)
        legacy.pop("tradition_context_refs", None)
        return canonical_tradition_refs_for_claim(legacy, self.taxonomy)

    def _explicit_projection(self, claim):
        return canonical_tradition_refs_for_claim(claim, self.taxonomy)

    def _claim(self, registry, claim_id):
        return next(claim for claim in registry["claims"] if claim["claim_id"] == claim_id)

    def test_domicile_ptolemaic_claims_preserve_legacy_projection(self):
        for claim_id in (
            "claim:domicile-configuration",
            "claim:ptolemaic-seasonal-rationale",
        ):
            claim = self._claim(self.domicile, claim_id)
            self.assertEqual(self._legacy_projection(claim), {"lineage:hellenistic:ptolemaic"})
            self.assertEqual(self._explicit_projection(claim), self._legacy_projection(claim))

    def test_domicile_historical_conflict_remains_non_doctrine(self):
        claim = self._claim(self.domicile, "claim:southern-hemisphere-reversal-debate")
        self.assertEqual(self._legacy_projection(claim), set())
        self.assertEqual(self._explicit_projection(claim), set())
        self.assertEqual(claim["historical_context_refs"], ["context:early_modern"])
        self.assertEqual(claim["meta_context_refs"], ["meta:history_of_astrology"])

    def test_domicile_ambiguous_practitioner_claim_remains_non_doctrine(self):
        claim = self._claim(self.domicile, "claim:modern-practitioner-domicile-capacity")
        self.assertEqual(self._legacy_projection(claim), set())
        self.assertEqual(self._explicit_projection(claim), set())

    def test_saturn_moon_ptolemaic_claims_preserve_legacy_projection(self):
        for claim_id in (
            "claim:ptolemy-major-aspect-geometry",
            "claim:ptolemy-moon-configured-planets-soul",
            "claim:ptolemy-saturn-regards-moon-maternal-context",
        ):
            claim = self._claim(self.saturn_moon, claim_id)
            self.assertEqual(self._legacy_projection(claim), {"lineage:hellenistic:ptolemaic"})
            self.assertEqual(self._explicit_projection(claim), self._legacy_projection(claim))

    def test_saturn_moon_historiography_remains_non_doctrine(self):
        claim = self._claim(self.saturn_moon, "claim:campion-classical-astrology-diversity")
        self.assertEqual(self._legacy_projection(claim), set())
        self.assertEqual(self._explicit_projection(claim), set())
        self.assertEqual(claim["meta_context_refs"], ["meta:history_of_astrology"])

    def test_saturn_moon_psychological_claim_preserves_legacy_projection(self):
        claim = self._claim(self.saturn_moon, "claim:greene-moon-saturn-parent-image")
        expected = {"school:modern:psychological_astrology"}
        self.assertEqual(self._legacy_projection(claim), expected)
        self.assertEqual(self._explicit_projection(claim), expected)

    def test_reference_blended_claims_stay_unresolved_when_no_school_tag_exists(self):
        for claim_id in (
            "claim:reference-conjunction-fusion",
            "claim:reference-square-friction",
        ):
            claim = self._claim(self.saturn_moon, claim_id)
            self.assertEqual(self._legacy_projection(claim), set())
            self.assertEqual(self._explicit_projection(claim), set())

    def test_reference_opposition_keeps_psychological_school_projection(self):
        claim = self._claim(self.saturn_moon, "claim:reference-opposition-polarity")
        expected = {"school:modern:psychological_astrology"}
        self.assertEqual(self._legacy_projection(claim), expected)
        self.assertEqual(self._explicit_projection(claim), expected)

    def test_all_explicit_tradition_refs_are_known_doctrine_or_school_contexts(self):
        context_dimensions = {
            item["context_id"]: item["dimension"] for item in self.taxonomy["contexts"]
        }
        allowed = {"doctrinal_lineage", "interpretive_school"}
        for registry in (self.domicile, self.saturn_moon):
            for claim in registry["claims"]:
                for ref in claim.get("tradition_context_refs", []):
                    self.assertIn(ref, context_dimensions)
                    self.assertIn(context_dimensions[ref], allowed)

    def test_typed_retrieval_selects_domicile_ptolemaic_claim(self):
        route = {
            "query_id": "migration-domicile",
            "claim_types": ["policy_configuration"],
            "tradition_context_refs_any": ["lineage:hellenistic:ptolemaic"],
            "applies_to_all": ["domicile configuration"],
            "requires_l2_facts": False,
            "l2_fact_refs": [],
            "requires_l3_policy": False,
            "l3_policy_refs": [],
            "allow_reference_only_qualified": False,
            "include_registry_guardrails": True,
            "synthesis_mode": "synthesis:single_tradition",
        }
        bundle = retrieve_claims(self.domicile, route, self.taxonomy)
        self.assertEqual(bundle["selected_claim_ids"], ["claim:domicile-configuration"])

    def test_typed_retrieval_selects_psychological_saturn_moon_claim(self):
        route = {
            "query_id": "migration-saturn-moon",
            "claim_types": ["aspect_meaning"],
            "tradition_context_refs_any": ["school:modern:psychological_astrology"],
            "applies_to_all": ["natal", "Moon-Saturn opposition"],
            "requires_l2_facts": False,
            "l2_fact_refs": [],
            "requires_l3_policy": False,
            "l3_policy_refs": [],
            "allow_reference_only_qualified": False,
            "include_registry_guardrails": True,
            "synthesis_mode": "synthesis:single_tradition",
        }
        bundle = retrieve_claims(self.saturn_moon, route, self.taxonomy)
        self.assertEqual(bundle["selected_claim_ids"], ["claim:greene-moon-saturn-parent-image"])


if __name__ == "__main__":
    unittest.main()
