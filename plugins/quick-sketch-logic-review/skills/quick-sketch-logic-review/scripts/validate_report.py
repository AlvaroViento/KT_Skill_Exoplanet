#!/usr/bin/env python3
"""Validate the review contract with no third-party dependency."""

from __future__ import annotations

import json
import sys
from pathlib import Path

MODES = {"text_concept", "board_draft", "final_sheet"}
GOALS = {"develop", "revise", "retrospective", "benchmark"}
VISIBILITY = {"explicit", "inferred", "unreadable", "absent"}
SEVERITY = {"fatal": 0, "major": 1, "minor": 2}
CATEGORIES = {"fact_error", "logic_break", "paper_gap", "hard_bug", "unreadable", "strength"}
STATUSES = {"pass", "weak", "broken", "insufficient_information"}
CONFIDENCE = {"high", "medium", "low"}
VAGUE_FIXES = {"加强调研", "完善用户研究", "丰富用户画像", "完善技术方案", "完善方案"}
ROOT_FIELDS = {
    "input_mode",
    "review_goal",
    "mode_basis",
    "scheme_model",
    "visible_evidence",
    "overall_judgment",
    "findings",
    "external_fact_checks",
    "next_actions",
    "mode_specific",
}
MODE_FIELDS = {
    "text_concept": {"minimum_sheet_evidence", "priority_logic_chain", "facts_to_verify"},
    "board_draft": {"readable", "absent", "unreadable", "minimum_additions", "compress_or_delete"},
    "final_sheet": {"reading_path", "failures", "redraw_priority", "reusable_strengths"},
}
SCHEME_FIELDS = {
    "problem": {"subject", "context", "obstacle", "consequence", "current_workaround", "gap"},
    "target_user": {"identity", "recurring_context", "current_behavior", "constraints", "conflict", "distinction"},
    "strategy": {"premise", "evidence_type", "intervention", "mechanism", "proximal_change", "boundary"},
    "implementation": {"actors", "core_flow", "technical_principle", "inputs", "processing", "outputs", "claimed_effect"},
    "effect": {"proximal", "distal"},
}
FACT_STATUSES = {"supported", "partially_supported", "conflicted", "unsupported", "not_verified"}


def validate_report(report: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(report, dict):
        return ["report must be an object"]

    missing = ROOT_FIELDS - report.keys()
    if missing:
        errors.append(f"missing root fields: {', '.join(sorted(missing))}")
    if "total_score" in report:
        errors.append("total_score is prohibited")

    mode = report.get("input_mode")
    if mode not in MODES:
        errors.append("invalid input_mode")
    if report.get("review_goal") not in GOALS:
        errors.append("invalid review_goal")
    if not isinstance(report.get("mode_basis"), str) or not report.get("mode_basis", "").strip():
        errors.append("mode_basis must be non-empty")
    if not isinstance(report.get("overall_judgment"), str) or not report.get("overall_judgment", "").strip():
        errors.append("overall_judgment must be non-empty")

    scheme = report.get("scheme_model")
    if not isinstance(scheme, dict):
        errors.append("scheme_model must be an object")
    else:
        for section, fields in SCHEME_FIELDS.items():
            value = scheme.get(section)
            if not isinstance(value, dict):
                errors.append(f"scheme_model.{section} must be an object")
            elif missing_fields := fields - value.keys():
                errors.append(f"scheme_model.{section} missing: {', '.join(sorted(missing_fields))}")

    evidence = report.get("visible_evidence", [])
    if not isinstance(evidence, list):
        errors.append("visible_evidence must be an array")
        evidence = []
    evidence_ids: set[str] = set()
    for index, item in enumerate(evidence):
        prefix = f"visible_evidence[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        evidence_id = item.get("id")
        if not isinstance(evidence_id, str) or not evidence_id:
            errors.append(f"{prefix}.id must be non-empty")
        elif evidence_id in evidence_ids:
            errors.append(f"{prefix}.id is duplicated")
        else:
            evidence_ids.add(evidence_id)
        if item.get("visibility") not in VISIBILITY:
            errors.append(f"{prefix}.visibility is invalid")
        confidence = item.get("confidence")
        if not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not 0 <= confidence <= 1:
            errors.append(f"{prefix}.confidence must be 0..1")

    fact_checks = report.get("external_fact_checks", [])
    if not isinstance(fact_checks, list):
        errors.append("external_fact_checks must be an array")
        fact_checks = []
    for index, check in enumerate(fact_checks):
        prefix = f"external_fact_checks[{index}]"
        if not isinstance(check, dict):
            errors.append(f"{prefix} must be an object")
            continue
        if check.get("status") not in FACT_STATUSES:
            errors.append(f"{prefix}.status is invalid")
        if not isinstance(check.get("sources"), list):
            errors.append(f"{prefix}.sources must be an array")

    source_ids = {
        source.get("id")
        for check in fact_checks
        if isinstance(check, dict)
        for source in check.get("sources", [])
        if isinstance(source, dict) and source.get("id")
    }

    findings = report.get("findings", [])
    if not isinstance(findings, list):
        errors.append("findings must be an array")
        findings = []
    previous_rank = -1
    for index, finding in enumerate(findings):
        prefix = f"findings[{index}]"
        if not isinstance(finding, dict):
            errors.append(f"{prefix} must be an object")
            continue
        severity = finding.get("severity")
        if severity not in SEVERITY:
            errors.append(f"{prefix}.severity is invalid")
        else:
            rank = SEVERITY[severity]
            if rank < previous_rank:
                errors.append("findings are not ordered fatal -> major -> minor")
            previous_rank = rank
        if finding.get("category") not in CATEGORIES:
            errors.append(f"{prefix}.category is invalid")
        if finding.get("status") not in STATUSES:
            errors.append(f"{prefix}.status is invalid")
        if finding.get("confidence") not in CONFIDENCE:
            errors.append(f"{prefix}.confidence is invalid")
        refs = finding.get("evidence_refs", [])
        if not isinstance(refs, list) or any(ref not in evidence_ids for ref in refs):
            errors.append(f"{prefix}.evidence_refs must reference visible evidence")
        external_refs = finding.get("external_source_refs", [])
        if not isinstance(external_refs, list) or any(ref not in source_ids for ref in external_refs):
            errors.append(f"{prefix}.external_source_refs must reference external sources")
        fix = finding.get("minimal_fix", "")
        if severity in {"fatal", "major"} and (not isinstance(fix, str) or not fix.strip()):
            errors.append(f"{prefix}.minimal_fix is required")
        if isinstance(fix, str) and fix.strip() in VAGUE_FIXES:
            errors.append(f"{prefix}.minimal_fix is vague")

    mode_specific = report.get("mode_specific")
    if not isinstance(mode_specific, dict):
        errors.append("mode_specific must be an object")
    elif mode in MODE_FIELDS:
        missing_mode = MODE_FIELDS[mode] - mode_specific.keys()
        if missing_mode:
            errors.append(f"mode_specific missing: {', '.join(sorted(missing_mode))}")
    actions = report.get("next_actions")
    if not isinstance(actions, list) or any(not isinstance(action, str) or not action.strip() for action in actions):
        errors.append("next_actions must be an array of non-empty strings")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_report.py REPORT.json", file=sys.stderr)
        return 2
    report = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors = validate_report(report)
    if errors:
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
