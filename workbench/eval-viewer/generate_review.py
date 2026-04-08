#!/usr/bin/env python3
"""Generate a simple HTML review page for Michael Polanyi eval results.

Reads evals.json and generates a self-contained HTML page for reviewing
eval results. Much simpler than skill-creator's full viewer.

Usage:
    python generate_review.py [--evals PATH] [--output PATH]

Defaults:
    --evals ../evals/evals.json
    --output review.html
"""

import argparse
import json
from pathlib import Path


def generate_html(evals_data: dict, output_path: Path) -> None:
    """Generate a simple standalone HTML review page."""
    
    skill_name = evals_data.get("skill_name", "michael-polanyi")
    evals = evals_data.get("evals", [])
    
    # Build eval cards HTML
    eval_cards = []
    for e in evals:
        eval_id = e.get("id", "?")
        eval_name = e.get("eval_name", "unnamed")
        prompt = e.get("prompt", "")
        expected = e.get("expected_output", "")
        assertions = e.get("assertions", [])
        
        # Build assertions HTML
        assertion_rows = []
        for a in assertions:
            name = a.get("name", "?")
            desc = a.get("description", "")
            a_type = a.get("type", "text_pattern")
            pattern = a.get("pattern", "")
            
            assertion_rows.append(f"""
                <tr>
                    <td><code>{name}</code></td>
                    <td>{desc}</td>
                    <td><span class="type-badge">{a_type}</span></td>
                    <td><code>{pattern[:50]}{'...' if len(pattern) > 50 else ''}</code></td>
                </tr>
            """)
        
        assertions_html = "\n".join(assertion_rows)
        
        eval_cards.append(f"""
        <div class="eval-card">
            <div class="eval-header">
                <span class="eval-id">#{eval_id}</span>
                <span class="eval-name">{eval_name}</span>
            </div>
            <div class="eval-body">
                <div class="field">
                    <label>Prompt</label>
                    <div class="prompt-text">{prompt}</div>
                </div>
                <div class="field">
                    <label>Expected Output</label>
                    <div class="expected-text">{expected}</div>
                </div>
                <div class="field">
                    <label>Assertions ({len(assertions)})</label>
                    <table class="assertions-table">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Description</th>
                                <th>Type</th>
                                <th>Pattern</th>
                            </tr>
                        </thead>
                        <tbody>
                            {assertions_html}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        """)
    
    evals_html = "\n".join(eval_cards)
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{skill_name} - Eval Review</title>
    <style>
        :root {{
            --bg: #faf9f5;
            --surface: #ffffff;
            --border: #e8e6dc;
            --text: #141413;
            --text-muted: #888;
            --accent: #d97757;
            --header-bg: #141413;
            --header-text: #faf9f5;
        }}
        
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
        }}
        
        .header {{
            background: var(--header-bg);
            color: var(--header-text);
            padding: 1.5rem 2rem;
        }}
        
        .header h1 {{
            font-size: 1.5rem;
            font-weight: 600;
        }}
        
        .header .subtitle {{
            opacity: 0.7;
            font-size: 0.875rem;
            margin-top: 0.25rem;
        }}
        
        .main {{
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        .summary {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 2rem;
        }}
        
        .summary h2 {{
            font-size: 1rem;
            margin-bottom: 1rem;
        }}
        
        .stats {{
            display: flex;
            gap: 2rem;
        }}
        
        .stat {{
            text-align: center;
        }}
        
        .stat-value {{
            font-size: 2rem;
            font-weight: 600;
            color: var(--accent);
        }}
        
        .stat-label {{
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
        }}
        
        .eval-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 8px;
            margin-bottom: 1.5rem;
            overflow: hidden;
        }}
        
        .eval-header {{
            background: var(--bg);
            padding: 0.75rem 1rem;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        
        .eval-id {{
            background: var(--accent);
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        
        .eval-name {{
            font-weight: 500;
        }}
        
        .eval-body {{
            padding: 1rem;
        }}
        
        .field {{
            margin-bottom: 1rem;
        }}
        
        .field:last-child {{
            margin-bottom: 0;
        }}
        
        .field label {{
            display: block;
            font-size: 0.75rem;
            font-weight: 500;
            color: var(--text-muted);
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }}
        
        .prompt-text, .expected-text {{
            background: var(--bg);
            padding: 0.75rem 1rem;
            border-radius: 4px;
            font-size: 0.875rem;
        }}
        
        .assertions-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.8rem;
        }}
        
        .assertions-table th {{
            text-align: left;
            padding: 0.5rem;
            background: var(--bg);
            border-bottom: 1px solid var(--border);
            font-weight: 500;
        }}
        
        .assertions-table td {{
            padding: 0.5rem;
            border-bottom: 1px solid var(--border);
        }}
        
        .assertions-table code {{
            background: #f0f0f0;
            padding: 0.125rem 0.25rem;
            border-radius: 2px;
            font-size: 0.75rem;
        }}
        
        .type-badge {{
            display: inline-block;
            padding: 0.125rem 0.5rem;
            border-radius: 4px;
            font-size: 0.7rem;
            font-weight: 500;
            background: #e0e0e0;
        }}
    </style>
</head>
<body>
    <header class="header">
        <h1>{skill_name}</h1>
        <div class="subtitle">Eval Review — {len(evals)} test cases</div>
    </header>
    
    <main class="main">
        <div class="summary">
            <h2>Summary</h2>
            <div class="stats">
                <div class="stat">
                    <div class="stat-value">{len(evals)}</div>
                    <div class="stat-label">Total Evals</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{sum(len(e.get('assertions', [])) for e in evals)}</div>
                    <div class="stat-label">Total Assertions</div>
                </div>
                <div class="stat">
                    <div class="stat-value">{len([e for e in evals if 'no-trigger' in e.get('eval_name', '')])}</div>
                    <div class="stat-label">Non-Trigger Tests</div>
                </div>
            </div>
        </div>
        
        {evals_html}
    </main>
</body>
</html>
"""
    
    output_path.write_text(html)
    print(f"✓ Generated: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate eval review HTML")
    parser.add_argument(
        "--evals", "-e",
        type=Path,
        default=Path(__file__).parent.parent / "evals" / "evals.json",
        help="Path to evals.json"
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path(__file__).parent / "review.html",
        help="Output HTML path"
    )
    args = parser.parse_args()
    
    if not args.evals.exists():
        print(f"Error: {args.evals} not found", flush=True)
        raise SystemExit(1)
    
    evals_data = json.loads(args.evals.read_text())
    generate_html(evals_data, args.output)


if __name__ == "__main__":
    main()
