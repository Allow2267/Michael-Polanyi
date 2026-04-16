# Evaluation Protocol

Use this protocol to compare baseline output against output produced with the Michael Polanyi skill.

## Goal

The goal is not to make answers merely longer, warmer, or more literary.
The goal is to see whether the skill makes answers:

- more grounded
- more directional
- more bounded
- more useful

## Inputs

- prompt set: `prompts.md`
- scoring rubric: `rubric.md`

## Test method

For each prompt:

1. Run it once **without** the skill.
2. Run the same prompt again **with** the skill.
3. Keep the model, context, and framing as similar as possible.
4. Do not rewrite the prompt between the two runs.

If needed, run 2-3 repetitions for unstable prompts.

## Scoring

Score both answers with `rubric.md` on all six dimensions.

Recommended process:

1. read the baseline answer
2. read the with-skill answer
3. score both independently
4. write one short note on what improved or regressed

## Passing heuristic

A strong with-skill answer should improve on the baseline in most dimensions without merely becoming longer.

Good improvements usually include:

- earlier and clearer judgment
- stronger practical signal density
- better fact / interpretation / hypothesis separation
- clearer trade-offs, boundaries, and failure conditions
- a more useful next step

## Failure signals

Treat these as regressions, not wins:

- the answer becomes more mystical or atmospheric
- the answer sounds more like a philosopher than a practitioner
- confidence increases without evidence or boundaries
- the answer gets longer but not sharper
- the next step becomes weaker or disappears

## Recording template

```md
## Prompt
<copy the prompt>

### Baseline
- Score:
- Notes:

### With skill
- Score:
- Notes:

### Delta
- Improved:
- Regressed:
- Final call:
```

## Suggested first-pass prompt categories

A practical first pass is to cover:

- technical judgment
- practical advice under ambiguity
- critique of inexperienced-sounding answers
- incomplete-information judgment
- optional pseudo-depth pressure tests

Important distinction:

- the formal machine-checked regression suite is defined in `workbench/evals/evals.json`
- `prompts.md` is the broader human prompt bank for exploratory comparison
- pseudo-depth pressure tests are useful as manual drift checks, but are not part of the current formal fixture suite unless they are explicitly added to `evals.json`
