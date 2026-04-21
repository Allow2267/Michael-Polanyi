# Subagent Workflow

This page describes how maintainers can use Claude subagents to implement isolated, verifiable tasks in this repository.

## When to Use This Workflow

This workflow is appropriate when:

- the task is **well-scoped**: one file or a tightly-coupled set of files
- the task is **verifiable**: you can check success with a script, test, or simple inspection
- the task is **low-context**: does not require deep project history or ongoing conversation state
- the task is **non-interactive**: the implementer does not need to ask clarifying questions mid-execution

Examples that fit:

- fix a bug in `workbench/scripts/aggregate_benchmark.py`
- add a new assertion helper in `workbench/scripts/`
- update a specific section of `SKILL.md` with clear before/after criteria

**Good targets in this repo**:
- Small workbench tooling fixes (scripts in `workbench/scripts/`)
- Eval/doc sync tasks (keeping benchmark results aligned with current skill behavior)
- Narrow maintainer-facing documentation updates (single wiki page or guide section)

Examples that do not fit:

- "improve the skill overall" (too vague)
- "refactor the eval system" (high-context, needs iteration)
- anything requiring live user feedback during execution

## Responsibilities

### Controller / Leader (Maintainer)

You are responsible for:

1. **Task definition**: Write a self-contained prompt that specifies exactly what to change and how to verify it.
2. **Execution engine mindset**: Treat Claude `-p` as a precise execution engine, not an autonomous finisher. It executes the task; you own the outcome.
3. **Two-stage gate**: After the subagent returns, review in two stages:
   - **Spec compliance** (Stage 1): Does the output match the task specification exactly? Did it touch only allowed files? Did it skip forbidden ones?
   - **Code quality** (Stage 2): Are the changes correct, minimal, and idiomatic? Only evaluate quality after confirming spec compliance.
4. **Verification**: Run the verification yourself after both stages. Do not trust the subagent's self-report alone.
5. **Result acceptance**: Decide whether the change is good enough, needs revision, or should be discarded.

### Claude Implementer (Subagent)

The implementer is responsible for:

1. **Execute the task**: Make the specified changes within the allowed file scope.
2. **Run the smallest relevant checks**: Execute only the verification command that was specified in the task. Do not run a full test suite or unrelated linters.
3. **Report what changed**: State which files were modified and the outcome of the verification check.
4. **Stay in scope**: Do not add improvements, refactorings, or documentation beyond what was requested.

## Task Shape

Good tasks for this repo have this shape:

```
Target: <single file or tightly-coupled set>
Change: <specific modification>
Verify: <command or inspection method>
Allowed: <files that may be modified>
Forbidden: <files that must not be touched>
```

Keep tasks **small and isolated**. If a task needs more than 3-4 files, split it.

## Verification Loop

After the subagent returns:

1. **Stage 1 — Spec compliance**: Run `git diff` to confirm scope. Check that only allowed files were touched and the change matches the specification.
2. **Stage 2 — Code quality**: Read the diff. Are the changes correct, minimal, and idiomatic?
3. Run the verification command specified in the task.
4. If the result is not acceptable at either stage, either:
   - Revise and re-run the subagent with tighter constraints
   - Take over and finish manually

**Do not merge or commit until you have personally verified the result.**

## Execution Boundary on This Machine

Claude `-p` with `--dangerously-skip-permissions` can enter a long execution path. Known behaviors:

- It may take 60-180 seconds for even small changes.
- It may not return cleanly if it encounters ambiguity.
- It may silently expand scope if the task is under-specified.

**Mitigation**: Set a controller-side timeout (e.g., 180 seconds). If the subagent times out, review what was changed and either continue manually or re-dispatch with a narrower task.

## Example: Benchmark Aggregator Fix (a8aac0b)

**Task**: Fix `workbench/scripts/aggregate_benchmark.py` to handle reingestion of its own output.

**Problem**: Running `aggregate_benchmark.py` on a directory containing `benchmark.json` (its own output) would fail because the output format uses a dict for `evals` instead of a list.

**Solution**:
- Added a check: `if not isinstance(evals, list): continue`
- Skip files that do not have `evals` as a list.
- Also added `sorted()` for deterministic file ordering.

**Verification**:
- Added `test_aggregate_benchmark.py` with cases for both valid and invalid inputs.
- Ran the script on a fixture directory containing both result files and `benchmark.json`.
- Confirmed the script skips its own output and processes only valid result files.

**Why this task fit the workflow**:
- Single file target.
- Clear bug with clear fix.
- Verifiable with a test script.
- No conversation context required.

## Related

- [Maintainer Guide](Maintainer-Guide) — overall maintainer workflow
- [Evaluation Workflow](Evaluation-Workflow) — how to verify skill changes
- [Repository Architecture](Repository-Architecture) — what lives where
