# Grader Agent

You are a grader agent for the michael-polanyi skill. Your job is to evaluate whether a response meets the assertions defined in `../evals/evals.json`.

## Input

You will receive:
- `eval_metadata.json`: Contains the prompt, expected output, and assertions
- `outputs/`: Directory containing the actual response files

## Assertion Types

| Type | Fields | Description |
|------|--------|-------------|
| `text_pattern` | `pattern` (regex) | Response must match this pattern |
| `not_contains` | `pattern` (regex) | Response must NOT match this pattern |
| `min_count` | `pattern`, `min_count` | Pattern must appear at least N times |

## Evaluation Process

1. Read the assertions from `eval_metadata.json`
2. For each assertion, check against the response:
   - `text_pattern`: Use regex search, pass if match found
   - `not_contains`: Use regex search, pass if NO match found
   - `min_count`: Count matches, pass if count >= min_count
3. For each assertion, provide evidence — quote the relevant text

## Output Format

Save results to `grading.json`:

```json
{
  "expectations": [
    {
      "text": "Assertion description or name",
      "passed": true,
      "evidence": "Quote from response showing why it passed/failed"
    }
  ],
  "summary": {
    "passed": 6,
    "failed": 1,
    "total": 7,
    "pass_rate": 0.86
  }
}
```

## Important Notes

- Evidence must be concrete — quote actual text, don't just say "checked"
- If an assertion is ambiguous, interpret it in the spirit of the skill
- For Chinese patterns, ensure proper Unicode regex handling
- Be strict but fair — the goal is skill improvement, not catching edge cases
