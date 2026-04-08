#!/usr/bin/env python3
"""Check assertions against a text file.

Reads ../evals/evals.json and checks each assertion against the provided text.
Designed to work with the Michael Polanyi skill evaluation framework.

Usage:
    python workbench/scripts/check_assertions.py <text-file> <eval-id>
    python workbench/scripts/check_assertions.py response.txt 1
"""

import json
import re
import sys
from pathlib import Path

DEFAULT_EVALS_PATH = Path(__file__).resolve().parent.parent / "evals" / "evals.json"


def load_evals(path: Path = DEFAULT_EVALS_PATH) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def check_assertion(text: str, assertion: dict) -> dict:
    """Check a single assertion against text. Returns result dict."""
    name = assertion["name"]
    desc = assertion["description"]
    a_type = assertion.get("type", "text_pattern")
    pattern = assertion.get("pattern", "")

    if a_type == "text_pattern":
        found = bool(re.search(pattern, text))
        return {
            "name": name,
            "description": desc,
            "passed": found,
            "evidence": f"Pattern '{pattern[:40]}...' {'found' if found else 'not found'}"
        }

    elif a_type == "not_contains":
        found = bool(re.search(pattern, text))
        return {
            "name": name,
            "description": desc,
            "passed": not found,
            "evidence": f"Pattern '{pattern[:40]}...' {'found (FAIL)' if found else 'not found (PASS)'}"
        }

    elif a_type == "min_count":
        matches = re.findall(pattern, text)
        count = len(matches)
        min_count = assertion.get("min_count", 1)
        return {
            "name": name,
            "description": desc,
            "passed": count >= min_count,
            "evidence": f"Found {count} matches (need >= {min_count})"
        }

    return {
        "name": name,
        "description": desc,
        "passed": False,
        "evidence": f"Unknown assertion type: {a_type}"
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: python workbench/scripts/check_assertions.py <text-file> <eval-id>")
        sys.exit(1)

    text_file = sys.argv[1]
    eval_id = int(sys.argv[2])

    text = Path(text_file).read_text(encoding="utf-8")
    evals = load_evals()

    target_eval = None
    for e in evals["evals"]:
        if e["id"] == eval_id:
            target_eval = e
            break

    if not target_eval:
        print(f"Eval ID {eval_id} not found")
        sys.exit(1)

    print(f"Checking eval {eval_id}: {target_eval.get('eval_name', 'unnamed')}")
    print(f"Prompt: {target_eval['prompt']}")
    print(f"Assertions: {len(target_eval['assertions'])}")
    print("-" * 60)

    results = []
    for assertion in target_eval["assertions"]:
        result = check_assertion(text, assertion)
        results.append(result)
        status = "PASS" if result["passed"] else "FAIL"
        print(f"  [{status}] {result['name']}: {result['evidence']}")

    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    print("-" * 60)
    print(f"Result: {passed}/{total} passed ({passed/total*100:.0f}%)")

    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
