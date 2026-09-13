#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from typed_tradition_routing import ALLOWED_SYNTHESIS_MODES, TRADITION_DIMENSIONS, validate_taxonomy

SCHEMA_NAME = "astrology_query_resolution"
SCHEMA_VERSION = "0.2.0-research"
LEGACY_SCHEMA_VERSION = "0.1.0-research"
SUPPORTED_SCHEMA_VERSIONS = {LEGACY_SCHEMA_VERSION, SCHEMA_VERSION}
RISK_CLASSES = {
    "normal_symbolic",
    "private_motive_inference",
    "clinical_or_diagnostic",
    "high_stakes_external_outcome",
}
BASIS = {"user_text", "upstream_context", "research_fixture", "research_policy"}
LEGACY_SEMANTIC_ROUTE_FIELDS = {"claim_types", "tradition_tags_any", "applies_to_all"}
TYPED_SEMANTIC_ROUTE_FIELDS = {"claim_types", "tradition_context_refs_any", "synthesis_mode", "applies_to_all"}
EXECUTABLE_TRADITION_STATUSES = {"explicit", "inferred_from_named_school"}


def add(errors: list[dict[str, str]], code: str, path: str, message: str) -> None:
    errors.append({"code": code, "path": path, "message": message})


def _string_array(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def _context_index(taxonomy: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        row.get("context_id"): row
        for row in taxonomy.get("contexts", [])
        if isinstance(row, dict) and isinstance(row.get("context_id"), str)
    }


def _validate_typed_tradition(
    data: dict[str, Any],
    route: dict[str, Any],
    taxonomy: dict[str, Any] | None,
    errors: list[dict[str, str]],
) -> None:
    typed_refs = route.get("tradition_context_refs_any")
    if not _string_array(typed_refs):
        add(errors, "ROUTE_STRING_ARRAY_REQUIRED", "$.route.tradition_context_refs_any", "must be a string array")
        typed_refs = []

    legacy_tags = route.get("tradition_tags_any", [])
    if not _string_array(legacy_tags):
        add(errors, "ROUTE_STRING_ARRAY_REQUIRED", "$.route.tradition_tags_any", "legacy compatibility field must be a string array when present")
        legacy_tags = []
    if legacy_tags:
        add(errors, "LEGACY_TRADITION_SELECTOR_FORBIDDEN_V2", "$.route.tradition_tags_any", "0.2 resolved routes must use typed tradition contexts, not legacy flat tags")

    requested = data.get("requested_tradition_contexts")
    if not _string_array(requested) or not requested:
        add(errors, "REQUESTED_TRADITION_CONTEXTS_REQUIRED", "$.requested_tradition_contexts", "0.2 resolved route requires at least one typed tradition context")
        requested = []
    if typed_refs != requested:
        add(errors, "TRADITION_CONTEXT_ROUTE_MISMATCH", "$.requested_tradition_contexts", "requested_tradition_contexts must exactly match route.tradition_context_refs_any")

    tradition_status = data.get("tradition_resolution_status")
    if tradition_status not in EXECUTABLE_TRADITION_STATUSES:
        add(errors, "TRADITION_RESOLUTION_NOT_EXECUTABLE", "$.tradition_resolution_status", "resolved 0.2 route requires explicit or inferred_from_named_school status")

    mode = data.get("requested_synthesis_mode")
    if mode not in ALLOWED_SYNTHESIS_MODES:
        add(errors, "SYNTHESIS_MODE_INVALID", "$.requested_synthesis_mode", "unsupported typed synthesis mode")
    if route.get("synthesis_mode") != mode:
        add(errors, "SYNTHESIS_MODE_ROUTE_MISMATCH", "$.route.synthesis_mode", "route synthesis_mode must match requested_synthesis_mode")

    if mode == "synthesis:single_tradition" and len(typed_refs) != 1:
        add(errors, "SINGLE_TRADITION_CARDINALITY_INVALID", "$.route.tradition_context_refs_any", "single-tradition synthesis requires exactly one tradition context")
    if mode in {"synthesis:parallel_comparison", "synthesis:explicit_blend"} and len(typed_refs) < 2:
        add(errors, "MULTI_TRADITION_CARDINALITY_INVALID", "$.route.tradition_context_refs_any", "parallel comparison or explicit blend requires at least two tradition contexts")

    if taxonomy is None:
        add(errors, "TAXONOMY_REQUIRED_FOR_TYPED_ROUTE", "$.taxonomy", "0.2 typed route validation requires the versioned tradition taxonomy")
        return
    if validate_taxonomy(taxonomy):
        add(errors, "TAXONOMY_INVALID", "$.taxonomy", "taxonomy failed deterministic validation")
        return

    contexts = _context_index(taxonomy)
    for index, ref in enumerate(typed_refs):
        row = contexts.get(ref)
        if row is None:
            add(errors, "TRADITION_CONTEXT_UNKNOWN", f"$.route.tradition_context_refs_any[{index}]", f"unknown tradition context: {ref}")
        elif row.get("dimension") not in TRADITION_DIMENSIONS:
            add(errors, "TRADITION_CONTEXT_DIMENSION_INVALID", f"$.route.tradition_context_refs_any[{index}]", "typed tradition selector must resolve to doctrinal_lineage or interpretive_school")


def validate_query_resolution(
    data: Any,
    available_registry_ids: set[str] | None = None,
    taxonomy: dict[str, Any] | None = None,
) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    if not isinstance(data, dict):
        return [{"code": "RESOLUTION_OBJECT_REQUIRED", "path": "$", "message": "resolution must be an object"}]

    if data.get("schema_name") != SCHEMA_NAME:
        add(errors, "SCHEMA_NAME_INVALID", "$.schema_name", f"must equal {SCHEMA_NAME}")
    version = data.get("schema_version")
    if version not in SUPPORTED_SCHEMA_VERSIONS:
        add(errors, "SCHEMA_VERSION_INVALID", "$.schema_version", f"must equal one of {sorted(SUPPORTED_SCHEMA_VERSIONS)}")
    if data.get("record_status") != "REFERENCE-ONLY":
        add(errors, "RECORD_STATUS_INVALID", "$.record_status", "must remain REFERENCE-ONLY")
    if data.get("production_routable") is not False:
        add(errors, "PRODUCTION_ROUTABLE_FORBIDDEN", "$.production_routable", "must explicitly be false")

    status = data.get("resolution_status")
    if status not in {"resolved", "needs_clarification", "unsupported"}:
        add(errors, "RESOLUTION_STATUS_INVALID", "$.resolution_status", "unsupported resolution status")
    if not isinstance(data.get("query_id"), str) or not data.get("query_id"):
        add(errors, "QUERY_ID_REQUIRED", "$.query_id", "non-empty query_id required")

    question = data.get("user_question")
    if not isinstance(question, str) or not question.strip():
        add(errors, "USER_QUESTION_REQUIRED", "$.user_question", "non-empty user_question required")
        question = ""

    risk = data.get("question_risk_class")
    if risk not in RISK_CLASSES:
        add(errors, "RISK_CLASS_INVALID", "$.question_risk_class", "unsupported risk class")
    if status == "resolved" and risk != "normal_symbolic":
        add(errors, "RISK_CLASS_CANNOT_RESOLVE", "$.question_risk_class", "non-normal risk class must not resolve to astrology retrieval")

    registry_id = data.get("target_registry_record_id")
    if status == "resolved":
        if not isinstance(registry_id, str) or not registry_id:
            add(errors, "TARGET_REGISTRY_REQUIRED", "$.target_registry_record_id", "resolved route requires target registry")
        elif available_registry_ids is not None and registry_id not in available_registry_ids:
            add(errors, "TARGET_REGISTRY_UNKNOWN", "$.target_registry_record_id", "target registry is not available")
    elif registry_id not in (None, "") and available_registry_ids is not None and registry_id not in available_registry_ids:
        add(errors, "TARGET_REGISTRY_UNKNOWN", "$.target_registry_record_id", "target registry is not available")

    route = data.get("route")
    if status == "resolved":
        if not isinstance(route, dict):
            add(errors, "ROUTE_REQUIRED", "$.route", "resolved status requires route object")
            route = {}
        if route.get("query_id") != data.get("query_id"):
            add(errors, "ROUTE_QUERY_ID_MISMATCH", "$.route.query_id", "route query_id must match resolution query_id")

        array_keys = ["claim_types", "applies_to_all", "l2_fact_refs", "l3_policy_refs"]
        if version == LEGACY_SCHEMA_VERSION:
            array_keys.append("tradition_tags_any")
        elif version == SCHEMA_VERSION:
            array_keys.append("tradition_context_refs_any")
        for key in array_keys:
            if not _string_array(route.get(key)):
                add(errors, "ROUTE_STRING_ARRAY_REQUIRED", f"$.route.{key}", "must be a string array")
        if not isinstance(route.get("claim_types"), list) or not route.get("claim_types"):
            add(errors, "ROUTE_CLAIM_TYPES_REQUIRED", "$.route.claim_types", "at least one claim type required")

        for key in ("requires_l2_facts", "requires_l3_policy", "allow_reference_only_qualified", "include_registry_guardrails"):
            if not isinstance(route.get(key), bool):
                add(errors, "ROUTE_BOOLEAN_REQUIRED", f"$.route.{key}", "must be boolean")
        if route.get("requires_l2_facts") is True and not route.get("l2_fact_refs"):
            add(errors, "ROUTE_L2_REFS_REQUIRED", "$.route.l2_fact_refs", "required L2 facts need explicit refs")
        if route.get("requires_l3_policy") is True and not route.get("l3_policy_refs"):
            add(errors, "ROUTE_L3_REFS_REQUIRED", "$.route.l3_policy_refs", "required L3 policy needs explicit refs")
        if route.get("allow_reference_only_qualified") is True:
            reason = data.get("reference_only_justification")
            if not isinstance(reason, str) or not reason.strip():
                add(errors, "REFERENCE_ONLY_JUSTIFICATION_REQUIRED", "$.reference_only_justification", "explicit justification required when opting into REFERENCE_ONLY evidence")
        if version == SCHEMA_VERSION:
            _validate_typed_tradition(data, route, taxonomy, errors)
    elif route not in (None, {}):
        add(errors, "ROUTE_FORBIDDEN_WHEN_UNRESOLVED", "$.route", "unresolved/unsupported status must not emit executable route")

    unresolved = data.get("unresolved_slots", [])
    if not isinstance(unresolved, list) or not all(isinstance(item, str) and item for item in unresolved):
        add(errors, "UNRESOLVED_SLOTS_INVALID", "$.unresolved_slots", "must be string array")
        unresolved = []
    if status == "needs_clarification" and not unresolved:
        add(errors, "UNRESOLVED_SLOTS_REQUIRED", "$.unresolved_slots", "clarification status requires at least one unresolved slot")
    if status == "resolved" and unresolved:
        add(errors, "UNRESOLVED_SLOTS_FORBIDDEN", "$.unresolved_slots", "resolved route cannot retain unresolved slots")
    if status == "needs_clarification":
        clarification = data.get("clarification_question")
        if not isinstance(clarification, str) or not clarification.strip():
            add(errors, "CLARIFICATION_QUESTION_REQUIRED", "$.clarification_question", "clarification status requires a question")
    if status == "unsupported":
        reason = data.get("unsupported_reason")
        if not isinstance(reason, str) or not reason.strip():
            add(errors, "UNSUPPORTED_REASON_REQUIRED", "$.unsupported_reason", "unsupported status requires a reason")

    assumptions = data.get("routing_assumptions", [])
    if not isinstance(assumptions, list):
        add(errors, "ROUTING_ASSUMPTIONS_ARRAY_REQUIRED", "$.routing_assumptions", "must be an array")
        assumptions = []

    mapped_fields: set[str] = set()
    assumption_by_field: dict[str, list[dict[str, Any]]] = {}
    for index, item in enumerate(assumptions):
        path = f"$.routing_assumptions[{index}]"
        if not isinstance(item, dict):
            add(errors, "ROUTING_ASSUMPTION_OBJECT_REQUIRED", path, "must be an object")
            continue
        field = item.get("field")
        basis = item.get("basis")
        if not isinstance(field, str) or not field:
            add(errors, "ROUTING_ASSUMPTION_FIELD_REQUIRED", path + ".field", "field required")
            continue
        mapped_fields.add(field)
        assumption_by_field.setdefault(field, []).append(item)
        if basis not in BASIS:
            add(errors, "ROUTING_ASSUMPTION_BASIS_INVALID", path + ".basis", "unsupported basis")

        spans = item.get("evidence_spans", [])
        refs = item.get("evidence_refs", [])
        if not isinstance(spans, list) or not all(isinstance(value, str) and value for value in spans):
            add(errors, "EVIDENCE_SPANS_INVALID", path + ".evidence_spans", "must be string array")
            spans = []
        if not isinstance(refs, list) or not all(isinstance(value, str) and value for value in refs):
            add(errors, "EVIDENCE_REFS_INVALID", path + ".evidence_refs", "must be string array")
            refs = []
        if basis == "user_text":
            if not spans:
                add(errors, "USER_TEXT_EVIDENCE_REQUIRED", path + ".evidence_spans", "user_text basis requires evidence span")
            else:
                for span in spans:
                    if span not in question:
                        add(errors, "EVIDENCE_SPAN_NOT_IN_QUESTION", path + ".evidence_spans", f"span not found in user_question: {span}")
        if basis == "upstream_context" and not refs:
            add(errors, "UPSTREAM_CONTEXT_REF_REQUIRED", path + ".evidence_refs", "upstream_context basis requires evidence refs")

    if status == "resolved" and isinstance(route, dict):
        semantic_fields = LEGACY_SEMANTIC_ROUTE_FIELDS if version == LEGACY_SCHEMA_VERSION else TYPED_SEMANTIC_ROUTE_FIELDS
        for field in semantic_fields:
            if route.get(field) and field not in mapped_fields:
                add(errors, "ROUTE_FIELD_UNGROUNDED", f"$.route.{field}", "non-empty semantic route field requires routing_assumption provenance")
        if version == SCHEMA_VERSION and data.get("requested_synthesis_mode") == "synthesis:explicit_blend":
            blend_assumptions = assumption_by_field.get("synthesis_mode", [])
            if not any(item.get("basis") in {"user_text", "research_fixture"} for item in blend_assumptions):
                add(errors, "EXPLICIT_BLEND_PROVENANCE_REQUIRED", "$.requested_synthesis_mode", "explicit blend requires user_text provenance or an explicit research fixture")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a research Astrology query-resolution envelope.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--registry-id", action="append", default=[], dest="registry_ids")
    parser.add_argument("--taxonomy", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
        taxonomy = json.loads(args.taxonomy.read_text(encoding="utf-8")) if args.taxonomy else None
    except (OSError, json.JSONDecodeError) as exc:
        errors = [{"code": "RESOLUTION_LOAD_ERROR", "path": "$", "message": str(exc)}]
    else:
        catalog = set(args.registry_ids) if args.registry_ids else None
        errors = validate_query_resolution(data, catalog, taxonomy)
    if args.as_json:
        print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    else:
        print("PASS" if not errors else "FAIL")
        for error in errors:
            print(f"  {error['code']} {error['path']}: {error['message']}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
