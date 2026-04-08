# Michael Polanyi Workbench

This directory contains **maintainer-only** tooling for evaluating and refining the Michael Polanyi skill.

## Directory map

- `agents/` - blind comparison and grading prompts
- `evals/` - eval set, prompt list, rubric, and protocol
- `scripts/` - assertion and benchmark helpers
- `eval-viewer/` - HTML review generator

## Standard iteration loop

1. Edit one runtime-facing asset:
   - `skills/michael-polanyi/SKILL.md`
   - `skills/michael-polanyi/examples.md`
   - `skills/michael-polanyi/polanyi-notes.md`
   - `skills/michael-polanyi/references/*`
2. Run the eval checks described in `workbench/evals/protocol.md`.
3. Review assertions, blind comparison, and generated review output.
4. Decide whether the change improved the skill, regressed it, or needs revision.
5. Commit only after the updated runtime docs and workbench checks agree.

## Core commands

Validate eval JSON:

```bash
python3 - <<'PY'
import json
with open('workbench/evals/evals.json') as f:
    data = json.load(f)
assert 'evals' in data and data['evals'], 'evals.json missing evals'
print(f"OK: {len(data['evals'])} evals")
PY
```

Generate the HTML review page:

```bash
python3 workbench/eval-viewer/generate_review.py
```

Run lightweight fluff detection against the examples:

```bash
python3 skills/michael-polanyi/scripts/detect_fluff.py skills/michael-polanyi/examples.md
```
