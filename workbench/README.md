# Michael Polanyi Workbench

This directory contains **maintainer-only** tooling for evaluating and refining the Michael Polanyi skill.

The published GitHub Wiki is versioned in the main repository under `docs/wiki/`.

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
2. Run the fixture suite described in `workbench/evals/protocol.md`.
3. Review suite assertions, blind comparison, and generated result report.
4. Decide whether the change improved the skill, regressed it, or needs revision.
5. Commit only after the updated runtime docs and workbench checks agree.

## Core commands

Run the fixture suite:

```bash
python3 workbench/scripts/check_assertions.py \
  --suite \
  --output workbench/evals/results/latest.json
```

Generate the HTML review page from the latest suite run:

```bash
python3 workbench/eval-viewer/generate_review.py \
  --results workbench/evals/results/latest.json \
  --output workbench/evals/results/review.html
```

Run lightweight fluff detection against the examples:

```bash
python3 skills/michael-polanyi/scripts/detect_fluff.py skills/michael-polanyi/examples.md
```

Important maintenance rule:

- `workbench/evals/fixtures/` is the canonical eval input set.
- Do not point assertion checks at the whole `skills/michael-polanyi/examples.md`; that file is teaching material, not the formal suite input.

## Pattern Summary

### What Generic Answers Have in Common

1. **No position taken** — "这取决于", "综合考虑", "建议根据实际情况"
2. **Abstract principles** — "明确目标", "加强沟通", "持续优化"
3. **No signals** — Nothing an experienced practitioner would notice
4. **No boundaries** — No failure conditions, no "when I'd change my mind"
5. **No concrete next step** — Vague directions instead of specific actions

### What Practitioner Answers Have in Common

1. **Clear judgment first** — One sentence, directional, no hedging
2. **Frame the whole** — What's the governing tension
3. **Surface 2-3 signals** — Things practitioners notice
4. **Name trade-offs** — What's being traded off, when judgment would change
5. **One next step** — Specific, actionable, not a menu

---

## Anti-Patterns to Avoid

| Pattern                    | Why It Fails                      | Example                               |
| -------------------------- | --------------------------------- | ------------------------------------- |
| Mysticism                  | Replaces clarity with atmosphere  | "只可意会不可言传"                    |
| Balance as evasion         | Sounds fair but takes no position | "各有利弊，需要综合考虑"              |
| Principle inventory        | Lists correct but useless advice  | "第一明确目标，第二加强沟通，第三..." |
| Confidence without grounds | Sounds sure but says nothing      | "相信你们一定能找到最佳方案"          |
| Decorative warmth          | Adds friendliness but no clarity  | "这是一个很好的问题，值得深入思考"    |
