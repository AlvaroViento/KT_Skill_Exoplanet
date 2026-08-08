#!/usr/bin/env python3
"""Run the six contract and rule baseline cases."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_report import validate_report  # noqa: E402


def main() -> int:
    cases = json.loads((Path(__file__).with_name("cases.json")).read_text(encoding="utf-8"))
    failures: list[str] = []
    for case in cases:
        report = case["report"]
        errors = validate_report(report)
        expected = case["expected"]
        findings = report["findings"]
        if errors:
            failures.append(f'{case["id"]}: ' + "; ".join(errors))
            continue
        if report["input_mode"] != expected["input_mode"]:
            failures.append(f'{case["id"]}: wrong input_mode')
        if report["review_goal"] != expected["review_goal"]:
            failures.append(f'{case["id"]}: wrong review_goal')
        for required in expected.get("required_findings", []):
            if not any(all(finding.get(key) == value for key, value in required.items()) for finding in findings):
                failures.append(f'{case["id"]}: missing finding {required}')
        if expected.get("requires_unreadable") and not any(
            item["visibility"] == "unreadable" for item in report["visible_evidence"]
        ):
            failures.append(f'{case["id"]}: unreadable evidence missing')
        if expected.get("requires_strength") and not any(
            finding["category"] == "strength" for finding in findings
        ):
            failures.append(f'{case["id"]}: strength missing')
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"{len(cases)}/{len(cases)} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
