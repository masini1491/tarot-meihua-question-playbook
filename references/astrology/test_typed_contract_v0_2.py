#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from compose_interpretation_synthesis import compose_synthesis
from retrieve_interpretation_claims import retrieve_claims
from validate_astrology_query_resolution import validate_query_resolution


class TypedContractV02Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        here = Path(__file__).resolve().parent
        cls.taxonomy = json.loads((here / "tradition_taxonomy_example.json").read_text(encoding="utf-8"))
        cls.saturn = json.loads((here / "saturn_moon_aspect_claim_family_registry.json").read_text(encoding="utf-8"))
        cls.domicile = json.loads((here / "domicile_claim_family_registry.json").read_text(encoding="utf-8"))

    def resolution(self, *, contexts=None, mode="synthesis:single_tradition", claim_types=None, applies=None):
        contexts = contexts or ["school:modern:psychological_astrology"]
        claim_types = claim_types or ["aspect_meaning"]
        applies = applies if applies is not None else ["natal", "Moon-Saturn opposition"]
        return {
            "schema_name": "astrology_query_resolution",
            "schema_version": "0.2.0-research",
            "record_status": "REFERENCE-ONLY",
            "production_routable": False,
            "resolution_status": "resolved",
            "query_id": "typed-v02",
            "user_question": "In psychological astrology compare or interpret Moon-Saturn symbolism.",
            "question_risk_class": "normal_symbolic",
            "target_registry_record_id": self.saturn["record_id"],
            "tradition_resolution_status": "explicit",
            "requested_tradition_contexts": list(contexts),
            "requested_synthesis_mode": mode,
            "route": {
                "query_id": "typed-v02",
                "claim_types": list(claim_types),
                "tradition_tags_any": [],
                "tradition_context_refs_any": list(contexts),
                "synthesis_mode": mode,
                "applies_to_all": list(applies),
                "requires_l2_facts": True,
                "l2_fact_refs": ["fact:moon-saturn-opposition"],
                "requires_l3_policy": True,
                "l3_policy_refs": ["policy:major-aspect-orb-v1"],
                "allow_reference_only_qualified": False,
                "include_registry_guardrails": True,
            },
            "routing_assumptions": [
                {"field": "claim_types", "basis": "research_fixture", "evidence_spans": [], "evidence_refs": []},
                {"field": "tradition_context_refs_any", "basis": "research_fixture", "evidence_spans": [], "evidence_refs": []},
                {"field": "synthesis_mode", "basis": "research_fixture", "evidence_spans": [], "evidence_refs": []},
                {"field": "applies_to_all", "basis": "research_fixture", "evidence_spans": [], "evidence_refs": []},
                {"field": "l2_fact_refs", "basis": "upstream_context", "evidence_spans": [], "evidence_refs": ["fact:moon-saturn-opposition"]},
                {"field": "l3_policy_refs", "basis": "upstream_context", "evidence_spans": [], "evidence_refs": ["policy:major-aspect-orb-v1"]},
            ],
            "unresolved_slots": [],
        }

    def test_v02_resolution_validates_directly(self):
        resolution = self.resolution()
        self.assertEqual(validate_query_resolution(resolution, {self.saturn["record_id"]}, self.taxonomy), [])

    def test_v02_requires_taxonomy(self):
        resolution = self.resolution()
        codes = {item["code"] for item in validate_query_resolution(resolution, {self.saturn["record_id"]})}
        self.assertIn("TAXONOMY_REQUIRED_FOR_TYPED_ROUTE", codes)

    def test_v02_rejects_legacy_flat_selector(self):
        resolution = self.resolution()
        resolution["route"]["tradition_tags_any"] = ["psychological_astrology"]
        codes = {item["code"] for item in validate_query_resolution(resolution, {self.saturn["record_id"]}, self.taxonomy)}
        self.assertIn("LEGACY_TRADITION_SELECTOR_FORBIDDEN_V2", codes)

    def test_v02_rejects_non_doctrine_context(self):
        resolution = self.resolution(contexts=["meta:history_of_astrology"])
        codes = {item["code"] for item in validate_query_resolution(resolution, {self.saturn["record_id"]}, self.taxonomy)}
        self.assertIn("TRADITION_CONTEXT_DIMENSION_INVALID", codes)

    def test_core_retrieval_selects_greene_without_adapter(self):
        resolution = self.resolution()
        bundle = retrieve_claims(self.saturn, resolution["route"], self.taxonomy)
        self.assertEqual(bundle["schema_version"], "0.2.0-research")
        self.assertEqual(bundle["retrieval_status"], "citation_ready")
        self.assertEqual(bundle["selected_claim_ids"], ["claim:greene-moon-saturn-parent-image"])
        self.assertEqual(bundle["tradition_provenance"]["covered_tradition_contexts"], ["school:modern:psychological_astrology"])

    def test_core_composer_preserves_typed_provenance_without_adapter(self):
        resolution = self.resolution()
        bundle = retrieve_claims(self.saturn, resolution["route"], self.taxonomy)
        envelope = compose_synthesis(resolution, bundle)
        self.assertEqual(envelope["schema_version"], "0.2.0-research")
        self.assertEqual(envelope["synthesis_status"], "ready_for_l5")
        self.assertEqual(envelope["route_snapshot"]["tradition_context_refs_any"], ["school:modern:psychological_astrology"])
        self.assertEqual(envelope["synthesis_units"][0]["tradition_context_refs"], ["school:modern:psychological_astrology"])

    def test_parallel_complete_coverage_reaches_l5(self):
        contexts = ["lineage:hellenistic:ptolemaic", "school:modern:psychological_astrology"]
        resolution = self.resolution(
            contexts=contexts,
            mode="synthesis:parallel_comparison",
            claim_types=["historical_doctrine", "aspect_meaning"],
            applies=[],
        )
        bundle = retrieve_claims(self.saturn, resolution["route"], self.taxonomy)
        self.assertEqual(bundle["retrieval_status"], "citation_ready")
        self.assertEqual(bundle["tradition_provenance"]["missing_tradition_contexts"], [])
        envelope = compose_synthesis(resolution, bundle)
        self.assertEqual(envelope["synthesis_status"], "ready_for_l5")
        self.assertTrue(any("visibly separate" in item for item in envelope["required_disclosures"]))

    def test_parallel_partial_coverage_blocks_core_composer(self):
        registry = copy.deepcopy(self.saturn)
        registry["claims"] = [claim for claim in registry["claims"] if claim["claim_id"] != "claim:greene-moon-saturn-parent-image"]
        contexts = ["lineage:hellenistic:ptolemaic", "school:modern:psychological_astrology"]
        resolution = self.resolution(
            contexts=contexts,
            mode="synthesis:parallel_comparison",
            claim_types=["historical_doctrine", "aspect_meaning"],
            applies=[],
        )
        bundle = retrieve_claims(registry, resolution["route"], self.taxonomy)
        self.assertEqual(bundle["retrieval_status"], "tradition_coverage_incomplete")
        self.assertEqual(bundle["tradition_provenance"]["missing_tradition_contexts"], ["school:modern:psychological_astrology"])
        envelope = compose_synthesis(resolution, bundle)
        self.assertEqual(envelope["synthesis_status"], "blocked_tradition_coverage_incomplete")
        self.assertEqual(envelope["synthesis_units"], [])

    def test_ptolemaic_domicile_direct_typed_retrieval(self):
        route = {
            "query_id": "typed-domicile",
            "claim_types": ["policy_configuration"],
            "tradition_tags_any": [],
            "tradition_context_refs_any": ["lineage:hellenistic:ptolemaic"],
            "synthesis_mode": "synthesis:single_tradition",
            "applies_to_all": ["domicile configuration"],
            "requires_l2_facts": True,
            "l2_fact_refs": ["fact:planet-sign-placement"],
            "requires_l3_policy": False,
            "l3_policy_refs": [],
            "allow_reference_only_qualified": False,
            "include_registry_guardrails": False,
        }
        bundle = retrieve_claims(self.domicile, route, self.taxonomy)
        self.assertEqual(bundle["retrieval_status"], "citation_ready")
        self.assertEqual(bundle["selected_claim_ids"], ["claim:domicile-configuration"])

    def test_legacy_v01_path_remains_compatible(self):
        resolution = self.resolution()
        resolution["schema_version"] = "0.1.0-research"
        resolution.pop("tradition_resolution_status")
        resolution.pop("requested_tradition_contexts")
        resolution.pop("requested_synthesis_mode")
        resolution["route"].pop("tradition_context_refs_any")
        resolution["route"].pop("synthesis_mode")
        resolution["route"]["tradition_tags_any"] = ["psychological_astrology"]
        resolution["routing_assumptions"] = [
            item for item in resolution["routing_assumptions"]
            if item["field"] not in {"tradition_context_refs_any", "synthesis_mode"}
        ]
        resolution["routing_assumptions"].append({"field": "tradition_tags_any", "basis": "research_fixture", "evidence_spans": [], "evidence_refs": []})
        self.assertEqual(validate_query_resolution(resolution, {self.saturn["record_id"]}), [])
        bundle = retrieve_claims(self.saturn, resolution["route"])
        self.assertEqual(bundle["schema_version"], "0.1.0-research")
        self.assertEqual(bundle["retrieval_status"], "citation_ready")
        envelope = compose_synthesis(resolution, bundle)
        self.assertEqual(envelope["schema_version"], "0.1.0-research")
        self.assertEqual(envelope["synthesis_status"], "ready_for_l5")


if __name__ == "__main__":
    unittest.main()
