#!/usr/bin/env python3
"""Aggregate benchmark results from multiple eval runs.

Reads multiple result files and produces aggregated statistics.
Useful for tracking skill quality over time.

Usage:
    python workbench/scripts/aggregate_benchmark.py <results-dir> [--output benchmark.json]

Example:
    python workbench/scripts/aggregate_benchmark.py ./results/ --output benchmark.json
"""

import argparse
import json
from datetime import datetime
from pathlib import Path


def aggregate_results(results_dir: Path) -> dict:
    """Aggregate all result files in the directory."""
    
    result_files = list(results_dir.glob("*.json"))
    if not result_files:
        return {"error": "No result files found"}
    
    all_results = []
    for f in result_files:
        try:
            data = json.loads(f.read_text())
            all_results.append({
                "file": f.name,
                "timestamp": datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
                "data": data
            })
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: Failed to read {f}: {e}")
    
    if not all_results:
        return {"error": "No valid result files"}
    
    # Aggregate by eval_id
    eval_stats = {}
    for result in all_results:
        data = result.get("data", {})
        evals = data.get("evals", [])
        
        for e in evals:
            eval_id = e.get("id", "?")
            eval_name = e.get("eval_name", "unnamed")
            passed = e.get("passed", 0)
            total = e.get("total", 0)
            
            if eval_id not in eval_stats:
                eval_stats[eval_id] = {
                    "eval_name": eval_name,
                    "runs": [],
                    "total_runs": 0,
                    "total_passed": 0,
                    "total_assertions": 0
                }
            
            eval_stats[eval_id]["runs"].append({
                "file": result["file"],
                "timestamp": result["timestamp"],
                "passed": passed,
                "total": total,
                "rate": passed / total if total > 0 else 0
            })
            eval_stats[eval_id]["total_runs"] += 1
            eval_stats[eval_id]["total_passed"] += passed
            eval_stats[eval_id]["total_assertions"] += total
    
    # Calculate aggregate stats
    for eval_id, stats in eval_stats.items():
        stats["avg_pass_rate"] = stats["total_passed"] / stats["total_assertions"] if stats["total_assertions"] > 0 else 0
    
    # Overall summary
    total_runs = len(all_results)
    total_evals = len(eval_stats)
    overall_passed = sum(s["total_passed"] for s in eval_stats.values())
    overall_assertions = sum(s["total_assertions"] for s in eval_stats.values())
    
    return {
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total_runs": total_runs,
            "total_evals": total_evals,
            "overall_passed": overall_passed,
            "overall_assertions": overall_assertions,
            "overall_pass_rate": overall_passed / overall_assertions if overall_assertions > 0 else 0
        },
        "evals": eval_stats
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate benchmark results")
    parser.add_argument(
        "results_dir",
        type=Path,
        help="Directory containing result JSON files"
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("benchmark.json"),
        help="Output benchmark JSON path"
    )
    args = parser.parse_args()
    
    if not args.results_dir.is_dir():
        print(f"Error: {args.results_dir} is not a directory", flush=True)
        raise SystemExit(1)
    
    benchmark = aggregate_results(args.results_dir)
    
    args.output.write_text(json.dumps(benchmark, indent=2, ensure_ascii=False) + "\n")
    print(f"✓ Generated: {args.output}")
    
    # Print summary
    summary = benchmark.get("summary", {})
    print(f"\n  Summary:")
    print(f"  ─────────────────────────────")
    print(f"  Total runs:       {summary.get('total_runs', 0)}")
    print(f"  Total evals:      {summary.get('total_evals', 0)}")
    print(f"  Overall pass rate: {summary.get('overall_pass_rate', 0):.1%}")


if __name__ == "__main__":
    main()
