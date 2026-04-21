# Maintainer Guide

This page is the operational guide for maintainers and contributors.

Canonical sources:

- [Workbench guide](https://github.com/August1314/Michael-Polanyi/blob/main/workbench/README.md)
- [Runtime package guide](https://github.com/August1314/Michael-Polanyi/blob/main/skills/michael-polanyi/README.md)
- [Contributing guide](https://github.com/August1314/Michael-Polanyi/blob/main/CONTRIBUTING.md)

## What to Edit for Each Goal

Edit the runtime package based on intent:

- `SKILL.md` → trigger logic and minimum response contract
- `examples.md` → target output shape and before/after teaching value
- `polanyi-notes.md` → conceptual grounding
- `references/` → anti-patterns, quality checks, response-pattern guidance
- `workbench/evals/*` → evaluation logic, scoring, and test prompts

## Standard Iteration Loop

1. choose one runtime-facing change to test
2. update the smallest relevant file set
3. run the eval workflow
4. review assertions, comparison, and generated review artifacts
5. decide whether the change improved the skill or caused drift
6. only keep changes that improve decision value rather than style inflation

## Validation Checklist

Maintainers should be able to answer:

- did the skill become more grounded, directional, bounded, and useful?
- did the next step get stronger?
- did the answer avoid pseudo-depth?
- did the change improve the right prompts without broadening the skill too far?

Operational checks live in:

- `workbench/evals/protocol.md`
- `workbench/evals/rubric.md`
- `workbench/scripts/`
- `workbench/eval-viewer/`

## Contribution Expectations

Good contributions usually improve one of these:

- install clarity
- response quality
- example quality
- eval quality
- discoverability and trigger precision

Avoid contributions that:

- add inflated or mystical language
- make the repository heavier without validation value
- change wording without improving examples or evals

## Subagent-Driven Development

For isolated, verifiable tasks, maintainers can use a controller/subagent workflow. See [Subagent Workflow](Subagent-Workflow) for when this is appropriate and how to use it.

## Current Follow-Up Issues

The current focused follow-up queue is:

- [Issue #3 — Trim examples.md to a minimum high-value runtime set](https://github.com/August1314/Michael-Polanyi/issues/3)
- [Issue #4 — Refine SKILL.md discoverability and trigger surface](https://github.com/August1314/Michael-Polanyi/issues/4)

These are intentionally separate:

- issue #3 is about runtime example surface area
- issue #4 is about trigger/discoverability tuning

If you need project-level context before choosing one, see [Roadmap and Open Questions](Roadmap-and-Open-Questions).
