#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from compose_interpretation_synthesis import compose_synthesis
from retrieve_interpretation_claims import retrieve_claims
from typed_tradition_pipeline import (
    WRAPPER_STATUS,
    compose_typed_synthesis,
    retrieve_typed_claims,
    run_typed_pipeline,
    validate_typed_resolution,
)
from validate_astrology_query_resolution import validate_query_resolution


class TypedTraditionPipelineParityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        here = Path(__file__).resolve().parent
        cls.taxonomy = json.loads((here / "tradition_taxonomy_example.json").read_text(encoding="utf-8"))
        cls.registry = json.loads((here / "saturn_moon_aspect_claim_family_registry.json").read_text(encoding="utf-8"))
        cls.registry_ids = {cls.registry["record_id"]}

    def resolution(self):
        return {
            "schema_name": "astrology_query_resolution",
            "schema_version": "0.2.0-research",
            "record_status": "REFERENCE-ONLY",
            "production_routable": False,
            "resolution_status": "resolved",
            "query_id": "typed-psych-opposition",
            "user_question": "In psychological astrology, what does a natal Moon-Saturn opposition mean?",
            "question_risk_class": "normal_symbolic",
            "target_registry_record_id": self.registry["record_id"],
            "tradition_resolution_status": "inferred_from_named_school",
            "requested_tradition_contexts": ["school:modern:psychological_astrology"],
            "requested_synthesis_mode": "synthesis:single_tradition",
            "route": {
                "query_id": "typed-psych-opposition",
                "claim_types": ["aspect_meaning"],
                "tradition_tags_any": [],
                "tradition_context_refs_any": ["school:modern:psychological_astrology"],
                "synthesis_mode": "synthesis:single_tradition",
                "applies_to_all": ["natal", "Moon-Saturn opposition"],
                "requires_l2_facts": True,
                "l2_fact_refs": ["fact:moon-saturn-opposition"],
                "requires_l3_policy": True,
                "l3_policy_refs": ["policy:major-aspect-orb-v1"],
                "allow_reference_only_qualified": False,
                "include_registry_guardrails": True,
            },
            "routing_assumptions": [
                {"field": "claim_types", "basis": "user_text", "evidence_spans": ["what does"], "evidence_refs": []},
                {"field": "tradition_context_refs_any", "basis": "user_text", "evidence_spans": ["psychological astrology"], "evidence_refs": []},
                {"field": "synthesis_mode", "basis": "research_policy", "evidence_spans": [], "evidence_refs": []},
                {"field": "applies_to_all", "basis": "user_text", "evidence_spans": ["natal Moon-Saturn opposition"], "evidence_refs": []},
                {"field": "l2_fact_refs", "basis": "upstream_context", "evidence_spans": [], "evidence_refs": ["fact:moon-saturn-opposition"]},
                {"field": "l3_policy_refs", "basis": "upstream_context", "evidence_spans": [], "evidence_refs": ["policy:major-aspect-orb-v1"]},
            ],
            "unresolved_slots": [],
        }

    def comparison_resolution(self):
        resolution = self.resolution()
        refs = ["lineage:hellenistic:ptolemaic", "school:modern:psychological_astrology"]
        resolution["query_id"] = "typed-parallel-comparison"
        resolution["user_question"] = "Compare Ptolemaic and psychological astrology Moon-Saturn meanings."
        resolution["tradition_resolution_status"] = "explicit"
        resolution["requested_tradition_contexts"] = refs
        resolution["requested_synthesis_mode"] = "synthesis:parallel_comparison"
        resolution["route"]["query_id"] = resolution["query_id"]
        resolution["route"]["claim_types"] = ["historical_doctrine", "aspect_meaning"]
        resolution["route"]["tradition_context_refs_any"] = refs
        resolution["route"]["synthesis_mode"] = "synthesis:parallel_comparison"
        resolution["route"]["applies_to_all"] = []
        resolution["route"]["requires_l2_facts"] = False
        resolution["route"]["l2_fact_refs"] = []
        resolution["route"]["requires_l3_policy"] = False
        resolution["route"]["l3_policy_refs"] = []
        resolution["routing_assumptions"] = [
            {"field": "claim_types", "basis": "research_fixture", "evidence_spans": [], "evidence_refs": []},
            {"field": "tradition_context_refs_any", "basis": "user_text", "evidence_spans": ["Ptolemaic", "psychological astrology"], "evidence_refs": []},
            {"field": "synthesis_mode", "basis": "user_text", "evidence_spans": ["Compare"], "evidence_refs": []},
        ]
        return resolution

    def direct_pipeline(self, registry, resolution):
        errors = validate_query_resolution(resolution, self.registry_ids, self.taxonomy)
        if errors:
            return {"pipeline_status": "invalid_resolution", "errors": errors}
        bundle = retrieve_claims(registry, resolution["route"], self.taxonomy)
        envelope = compose_synthesis(resolution, bundle)
        return {
            "pipeline_status": "complete" if envelope.get("synthesis_status") == "ready_for_l5" else "blocked",
            "retrieval": bundle,
            "synthesis": envelope,
        }

    def test_wrapper_is_explicitly_deprecated_transitional(self):
        result = run_typed_pipeline(self.registry, self.resolution(), self.taxonomy, self.registry_ids)
        self.assertEqual(result["wrapper_status"], WRAPPER_STATUS)
        self.assertEqual(WRAPPER_STATUS, "DEPRECATED_TRANSITIONAL")

    def test_wrapper_validation_matches_core(self):
        resolution = self.resolution()
        self.assertEqual(
            validate_typed_resolution(resolution, self.taxonomy, self.registry_ids),
            validate_query_resolution(resolution, self.registry_ids, self.taxonomy),
        )

    def test_wrapper_retrieval_matches_core(self):
        resolution = self.resolution()
        wrapped = retrieve_typed_claims(self.registry, resolution, self.taxonomy)
        direct = retrieve_claims(self.registry, resolution["route"], self.taxonomy)
        self.assertEqual(wrapped, direct)
        self.assertEqual(wrapped["selected_claim_ids"], ["claim:greene-moon-saturn-parent-image"])

    def test_wrapper_composer_matches_core(self):
        resolution = self.resolution()
        bundle = retrieve_claims(self.registry, resolution["route"], self.taxonomy)
        self.assertEqual(compose_typed_synthesis(resolution, bundle), compose_synthesis(resolution, bundle))

    def test_single_school_full_pipeline_matches_core(self):
        resolution = self.resolution()
        wrapped = run_typed_pipeline(self.registry, resolution, self.taxonomy, self.registry_ids)
        direct = self.direct_pipeline(self.registry, resolution)
        self.assertEqual(wrapped["pipeline_status"], direct["pipeline_status"])
        self.assertEqual(wrapped["retrieval"], direct["retrieval"])
        self.assertEqual(wrapped["synthesis"], direct["synthesis"])
        self.assertEqual(wrapped["pipeline_status"], "complete")

    def test_invalid_mixed_selector_parity(self):
        resolution = self.resolution()
        resolution["route"]["tradition_tags_any"] = ["psychological_astrology"]
        wrapped = validate_typed_resolution(resolution, self.taxonomy, self.registry_ids)
        direct = validate_query_resolution(resolution, self.registry_ids, self.taxonomy)
        self.assertEqual(wrapped, direct)
        self.assertIn("LEGACY_TRADITION_SELECTOR_FORBIDDEN_V2", {error["code"] for error in wrapped})

    def test_invalid_non_doctrine_context_parity(self):
        resolution = self.resolution()
        resolution["requested_tradition_contexts"] = ["meta:history_of_astrology"]
        resolution["route"]["tradition_context_refs_any"] = ["meta:history_of_astrology"]
        wrapped = validate_typed_resolution(resolution, self.taxonomy, self.registry_ids)
        direct = validate_query_resolution(resolution, self.registry_ids, self.taxonomy)
        self.assertEqual(wrapped, direct)
        self.assertIn("TRADITION_CONTEXT_DIMENSION_INVALID", {error["code"] for error in wrapped})

    def test_parallel_complete_coverage_matches_core(self):
        resolution = self.comparison_resolution()
        wrapped = run_typed_pipeline(self.registry, resolution, self.taxonomy, self.registry_ids)
        direct = self.direct_pipeline(self.registry, resolution)
        self.assertEqual(wrapped["retrieval"], direct["retrieval"])
        self.assertEqual(wrapped["synthesis"], direct["synthesis"])
        self.assertEqual(wrapped["retrieval"]["tradition_provenance"]["missing_tradition_contexts"], [])

    def test_parallel_partial_coverage_matches_core(self):
        registry = copy.deepcopy(self.registry)
        registry["claims"] = [
            claim for claim in registry["claims"]
            if claim["claim_id"] != "claim:greene-moon-saturn-parent-image"
        ]
        resolution = self.comparison_resolution()
        wrapped = run_typed_pipeline(registry, resolution, self.taxonomy, self.registry_ids)
        direct = self.direct_pipeline(registry, resolution)
        self.assertEqual(wrapped["retrieval"], direct["retrieval"])
        self.assertEqual(wrapped["synthesis"], direct["synthesis"])
        self.assertEqual(wrapped["pipeline_status"], "blocked")
        self.assertEqual(wrapped["synthesis"]["synthesis_status"], "blocked_tradition_coverage_incomplete")

    def test_explicit_blend_parity(self):
        resolution = self.comparison_resolution()
        resolution["requested_synthesis_mode"] = "synthesis:explicit_blend"
        resolution["route"]["synthesis_mode"] = "synthesis:explicit_blend"
        resolution["routing_assumptions"][-1] = {
            "field": "synthesis_mode",
            "basis": "research_fixture",
            "evidence_spans": [],
            "evidence_refs": [],
        }
        wrapped = run_typed_pipeline(self.registry, resolution, self.taxonomy, self.registry_ids)
        direct = self.direct_pipeline(self.registry, resolution)
        self.assertEqual(wrapped["retrieval"], direct["retrieval"])
        self.assertEqual(wrapped["synthesis"], direct["synthesis"])
        self.assertEqual(wrapped["synthesis"]["tradition_provenance"]["requested_synthesis_mode"], "synthesis:explicit_blend")

    def test_wrapper_rejects_pre_v02_typed_fixture(self):
        resolution = self.resolution()
        resolution["schema_version"] = "0.1.0-research"
        errors = validate_typed_resolution(resolution, self.taxonomy, self.registry_ids)
        self.assertEqual({error["code"] for error in errors}, {"TYPED_WRAPPER_REQUIRES_V02"})


if __name__ == "__main__":
    unittest.main()
