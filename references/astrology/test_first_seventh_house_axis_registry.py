#!/usr/bin/env python3
from __future__ import annotations

import json
import unittest
from pathlib import Path

from retrieve_interpretation_claims import retrieve_claims
from validate_interpretation_claim_registry import validate_registry


class FirstSeventhHouseAxisRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        here = Path(__file__).resolve().parent
        cls.taxonomy = json.loads((here / "tradition_taxonomy_example.json").read_text(encoding="utf-8"))
        cls.registry = json.loads((here / "first_seventh_house_axis_claim_family_registry.json").read_text(encoding="utf-8"))

    def test_registry_validates_under_v02_taxonomy_contract(self):
        self.assertEqual(validate_registry(self.registry, self.taxonomy), [])

    def test_hellenistic_first_house_typed_route_selects_only_valens(self):
        route = {
            "query_id": "axis-hellenistic-first",
            "claim_types": ["historical_doctrine"],
            "tradition_tags_any": [],
            "tradition_context_refs_any": ["lineage:hellenistic"],
            "synthesis_mode": "synthesis:single_tradition",
            "applies_to_all": ["natal", "first house", "Ascendant"],
            "requires_l2_facts": True,
            "l2_fact_refs": ["fact:ascendant", "fact:house-1"],
            "requires_l3_policy": False,
            "l3_policy_refs": [],
            "allow_reference_only_qualified": False,
            "include_registry_guardrails": False,
        }
        result = retrieve_claims(self.registry, route, self.taxonomy)
        self.assertEqual(result["retrieval_status"], "citation_ready")
        self.assertEqual(result["selected_claim_ids"], ["claim:valens-first-place-life-body"])
        self.assertEqual(result["tradition_provenance"]["missing_tradition_contexts"], [])

    def test_hellenistic_seventh_house_typed_route_selects_only_valens(self):
        route = {
            "query_id": "axis-hellenistic-seventh",
            "claim_types": ["historical_doctrine"],
            "tradition_tags_any": [],
            "tradition_context_refs_any": ["lineage:hellenistic"],
            "synthesis_mode": "synthesis:single_tradition",
            "applies_to_all": ["natal", "seventh house", "Descendant", "marriage"],
            "requires_l2_facts": True,
            "l2_fact_refs": ["fact:descendant", "fact:house-7"],
            "requires_l3_policy": False,
            "l3_policy_refs": [],
            "allow_reference_only_qualified": False,
            "include_registry_guardrails": False,
        }
        result = retrieve_claims(self.registry, route, self.taxonomy)
        self.assertEqual(result["retrieval_status"], "citation_ready")
        self.assertEqual(result["selected_claim_ids"], ["claim:valens-seventh-place-marriage"])

    def test_early_modern_discovery_does_not_require_invented_doctrine_context(self):
        route = {
            "query_id": "axis-lilly-first",
            "claim_types": ["historical_doctrine"],
            "tradition_tags_any": ["early_modern"],
            "applies_to_all": ["first house", "Ascendant"],
            "requires_l2_facts": True,
            "l2_fact_refs": ["fact:ascendant", "fact:house-1"],
            "requires_l3_policy": False,
            "l3_policy_refs": [],
            "allow_reference_only_qualified": False,
            "include_registry_guardrails": False,
        }
        result = retrieve_claims(self.registry, route, self.taxonomy)
        self.assertEqual(result["retrieval_status"], "citation_ready")
        self.assertEqual(result["selected_claim_ids"], ["claim:lilly-first-house-native-body"])
        claim = result["claims"][0]
        self.assertEqual(claim["tradition_context_refs"], [])

    def test_reference_only_modern_identity_claim_is_excluded_without_opt_in(self):
        route = {
            "query_id": "axis-modern-first-default",
            "claim_types": ["house_meaning"],
            "tradition_tags_any": ["psychological_language"],
            "applies_to_all": ["first house", "identity"],
            "requires_l2_facts": True,
            "l2_fact_refs": ["fact:ascendant", "fact:house-1"],
            "requires_l3_policy": False,
            "l3_policy_refs": [],
            "allow_reference_only_qualified": False,
            "include_registry_guardrails": False,
        }
        result = retrieve_claims(self.registry, route, self.taxonomy)
        self.assertEqual(result["retrieval_status"], "no_match")
        self.assertEqual(result["selected_claim_ids"], [])
        self.assertIn(
            {"claim_id": "claim:reference-first-house-identity-agency", "reason": "source_admission_insufficient"},
            result["excluded"],
        )

    def test_reference_only_modern_identity_claim_can_be_qualified_opt_in(self):
        route = {
            "query_id": "axis-modern-first-opt-in",
            "claim_types": ["house_meaning"],
            "tradition_tags_any": ["psychological_language"],
            "applies_to_all": ["first house", "identity"],
            "requires_l2_facts": True,
            "l2_fact_refs": ["fact:ascendant", "fact:house-1"],
            "requires_l3_policy": False,
            "l3_policy_refs": [],
            "allow_reference_only_qualified": True,
            "include_registry_guardrails": False,
        }
        result = retrieve_claims(self.registry, route, self.taxonomy)
        self.assertEqual(result["retrieval_status"], "citation_ready")
        self.assertEqual(result["selected_claim_ids"], ["claim:reference-first-house-identity-agency"])
        self.assertEqual(result["claims"][0]["source_admission_mode"], "qualified_reference_only")

    def test_house_axis_route_fails_closed_when_required_l2_refs_are_missing(self):
        route = {
            "query_id": "axis-missing-l2",
            "claim_types": ["historical_doctrine"],
            "tradition_tags_any": [],
            "tradition_context_refs_any": ["lineage:hellenistic"],
            "synthesis_mode": "synthesis:single_tradition",
            "applies_to_all": ["natal", "first house", "Ascendant"],
            "requires_l2_facts": True,
            "l2_fact_refs": [],
            "requires_l3_policy": False,
            "l3_policy_refs": [],
            "allow_reference_only_qualified": False,
            "include_registry_guardrails": False,
        }
        result = retrieve_claims(self.registry, route, self.taxonomy)
        self.assertEqual(result["retrieval_status"], "precondition_failed")
        self.assertIn("l2_fact_refs_required", result["precondition_failures"])
        self.assertEqual(result["selected_claim_ids"], [])

    def test_modern_reference_claims_are_not_silently_typed_as_psychological_school(self):
        claims = {claim["claim_id"]: claim for claim in self.registry["claims"]}
        self.assertEqual(claims["claim:reference-first-house-identity-agency"]["tradition_context_refs"], [])
        self.assertEqual(claims["claim:reference-seventh-house-mirroring-projection"]["tradition_context_refs"], [])


if __name__ == "__main__":
    unittest.main()
