# Comparator Agent — Blind Comparison

Performs blind A/B comparison between responses to determine which feels more like a practitioner's judgment.

## Purpose

When evaluating skill quality, sometimes assertions aren't enough. This agent compares two responses without knowing which is which, and judges which one:
- Feels more grounded and practical
- Has clearer judgment structure
- Surfaces more useful signals
- Ends with a more actionable next step

## Prompt Template

```
You are a blind comparator. You will see two responses to the same prompt.
You do NOT know which response is from which system.

Your job: Judge which response feels more like it came from an experienced practitioner.

Prompt:
{prompt}

Response A:
{response_a}

Response B:
{response_b}

---

Compare on these dimensions:

1. **Judgment Clarity** — Which starts with a clearer directional judgment?
2. **Practical Signals** — Which surfaces more concrete, observable signals?
3. **Trade-offs** — Which better articulates conditions and failure cases?
4. **Actionability** — Which ends with a more specific next step?
5. **Anti-Generic** — Which avoids AI-generic patterns better?

For each dimension, score A and B from 1-5 (5 = more practitioner-like).

Then provide:
- Overall winner: A or B
- Confidence: high/medium/low
- Key differentiator: What made the winner stand out?
```

## Output Format

```json
{
  "comparison_id": "uuid",
  "prompt_id": "eval-1",
  "scores": {
    "judgment_clarity": {"a": 4, "b": 2},
    "practical_signals": {"a": 3, "b": 3},
    "trade_offs": {"a": 4, "b": 2},
    "actionability": {"a": 5, "b": 1},
    "anti_generic": {"a": 4, "b": 2}
  },
  "total_a": 20,
  "total_b": 10,
  "winner": "A",
  "confidence": "high",
  "key_differentiator": "Response A started with a clear judgment and ended with a specific next step, while B gave a generic 'it depends' answer."
}
```

## Usage

1. Generate responses from two different systems (e.g., with skill vs without)
2. Shuffle and label as A/B randomly
3. Run comparator
4. Record result
5. Reveal which was which after comparison is complete

## Integration with Evals

After running `check_assertions.py`, run blind comparison on any evals where:
- Both responses passed all assertions (tie-breaker)
- One response barely passed (quality check)
- Manual review is needed (edge cases)
