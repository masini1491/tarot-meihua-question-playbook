#!/usr/bin/env python3
"""Deprecated compatibility facade for the Astrology typed-tradition research path.

Typed routing is now owned by the core v0.2 query-resolution, retrieval, and L5
contracts. This module preserves the earlier public helper names so existing
research callers do not fail imports, but it must not implement independent
validation, claim filtering, coverage, or synthesis semantics.

Status: REFERENCE-ONLY / DEPRECATED TRANSITIONAL WRAPPER / NOT PRODUCTION-ROUTABLE.
"""
from __future__ import annotations

from typing import Any

from compose_interpretation_synthesis import compose_synthesis
from retrieve_interpretation_claims import retrieve_claims
from validate_astrology_query_resolution import validate_query_resolution

WRAPPER_STATUS = "DEPRECATED_TRANSITIONAL"
REQUIRED_TYPED_SCHEMA_VERSION = "0.2.0-research"


def validate_typed_resolution(
    resolution: Any,
    taxonomy: dict[str, Any],
    available_registry_ids: set[str] | None = None,
) -> list[dict[str, str]]:
    """Delegate typed resolution validation to the core v0.2 validator."""
    if isinstance(resolution, dict) and resolution.get("schema_version") != REQUIRED_TYPED_SCHEMA_VERSION:
        return [{
            "code": "TYPED_WRAPPER_REQUIRES_V02",
            "path": "$.schema_version",
            "message": "deprecated typed wrapper only delegates the canonical 0.2.0-research typed contract",
        }]
    return validate_query_resolution(resolution, available_registry_ids, taxonomy)


def retrieve_typed_claims(
    registry: dict[str, Any],
    resolution: dict[str, Any],
    taxonomy: dict[str, Any],
) -> dict[str, Any]:
    """Delegate typed claim retrieval to the core selector."""
    route = resolution.get("route", {}) if isinstance(resolution, dict) else {}
    return retrieve_claims(registry, route, taxonomy)


def compose_typed_synthesis(
    resolution: dict[str, Any],
    bundle: dict[str, Any],
) -> dict[str, Any]:
    """Delegate typed synthesis packaging to the core composer."""
    return compose_synthesis(resolution, bundle)


def run_typed_pipeline(
    registry: dict[str, Any],
    resolution: dict[str, Any],
    taxonomy: dict[str, Any],
    available_registry_ids: set[str] | None = None,
) -> dict[str, Any]:
    """Compatibility facade over the canonical core v0.2 typed pipeline."""
    errors = validate_typed_resolution(resolution, taxonomy, available_registry_ids)
    if errors:
        return {
            "pipeline_status": "invalid_resolution",
            "wrapper_status": WRAPPER_STATUS,
            "errors": errors,
        }

    bundle = retrieve_typed_claims(registry, resolution, taxonomy)
    envelope = compose_typed_synthesis(resolution, bundle)
    return {
        "pipeline_status": "complete" if envelope.get("synthesis_status") == "ready_for_l5" else "blocked",
        "wrapper_status": WRAPPER_STATUS,
        "retrieval": bundle,
        "synthesis": envelope,
    }
