# Changelog

All notable changes to this project will be documented in this file.

## [0.5.3] - 2026-04-19

### Added

- **registry/skillhub-submission.json**: added a minimal submission record for aghub / skillhub-style registries
- **registry/README.md**: documented the packaging workflow for skillhub-style release assets
- **scripts/build_skill_package.py**: added a dedicated runtime package builder that emits installable zip assets and update manifests

### Changed

- **scripts/build_skill_package.py**: added a `--release` mode so formal GitHub release assets use a clean version number and predictable download URLs

## [0.5.2] - 2026-04-10

### Changed

- **workbench/evals/evals.json**: each eval now binds to explicit fixture files under `workbench/evals/fixtures/`
- **workbench/scripts/check_assertions.py**: added fixture suite mode, stronger eval structure validation, and machine-readable JSON output
- **workbench/eval-viewer/generate_review.py**: added `--results` input and explicit `spec-only` vs result rendering
- **.github/workflows/ci.yml**: fixture suite now gates eval validation, example balance check matches actual headings, and report generation uses suite results
- **.gitignore**: evaluation artifact ignores now match `workbench/evals/results/`
- **workbench/README.md** and **docs/wiki/Evaluation-Workflow.md**: documented canonical fixture workflow and separated spec review from result review

### Added

- **workbench/evals/fixtures/**: canonical fixture set for all 10 eval cases

### Fixed

- Removed the false-green path where example balance could pass as `0/0`
- Removed the ambiguous workflow where assertions could be run against `examples.md` instead of formal fixtures
- Removed the ambiguity where the HTML page could be mistaken for a real result report without suite output

## [0.5.1] - 2026-04-07

### Fixed

- CI: Fixed heredoc variable expansion in validate-evals job

---

## [0.5.0] - 2026-04-07

### Added

- **.github/workflows/ci.yml**: Complete CI pipeline with 6 jobs:
  - validate-structure: Check required files and frontmatter
  - markdown-lint: Markdown syntax and link validation
  - validate-evals: JSON syntax and required fields
  - code-quality: Python syntax and formatting
  - content-quality: SKILL.md length, fluff patterns, examples balance
  - generate-report: Auto-generate HTML review page

### Changed

- README.md: Added CI badge

---

## [0.4.0] - 2026-04-07

### Added

- **eval-viewer/generate_review.py**: simple HTML review page generator for evals
- **scripts/aggregate_benchmark.py**: aggregate statistics from multiple eval runs
- **agents/comparator.md**: blind A/B comparison agent for quality evaluation

### Changed

- Updated "When to Read What" table with new scripts and agents

---

## [0.3.0] - 2026-04-07

### Changed

- **SKILL.md**: streamlined from 340 lines to 122 lines, moved detailed
  quality checks and anti-pattern detection to separate reference files
- Updated "When to Read What" table with new reference file paths

### Added

- **references/quality-checks.md**: detailed quality verification patterns,
  common pitfalls with fixes, and verification checklist
- **references/anti-patterns.md**: comprehensive AI-generic detection patterns
  with 8 categories, rewrite strategies, and detection script usage

### Removed

- Detailed Quality Checks section from SKILL.md (moved to references/)
- Anti-Generic Advice Detection table from SKILL.md (moved to references/)

---

## [0.2.0] - 2026-04-07

### Changed

- **SKILL.md**: restructured response framework into 6-step core sequence,
  optimized trigger description with explicit patterns, added anti-generic
  detection table and quality check red flags
- **examples.md**: added comparison analysis tables for all 5 examples,
  included pattern summary and anti-patterns reference
- **polanyi-notes.md**: restructured concepts into concept→implication pattern,
  added quick reference table

### Added

- **scripts/detect_fluff.py**: AI-generic pattern detection tool supporting
  Chinese and English, covers 8 pattern categories
- **scripts/check_assertions.py**: assertion checker for eval validation,
  supporting text_pattern, not_contains, and min_count types
- **evals/evals.json**: 10 test cases with 3-4 assertions each, covering
  8 trigger scenarios and 2 non-trigger exclusion tests
- **references/response-patterns.md**: extended reference with 6 response
  patterns, 4 deep anti-pattern analyses, and 4 domain-specific patterns
- **skills/README.md**: skill overview, file structure, quick start guide

### Fixed

- CI markdown lint false-positive caused by broken grep pipe logic
- Frontmatter validation corrected from `grep -q` pipeline to `grep -c` count
- Fluff detection made non-fatal for examples.md which intentionally contains
  anti-pattern reference examples

---

## [0.1.0] - 2026-04-07

### Added

- initial Michael Polanyi skill scaffold
- `SKILL.md` with response contract and discoverability-oriented description
- supporting notes distilled from Polanyi-inspired concepts
- before/after examples for architecture judgment, team stall, incomplete-information judgment, critique, and anti pseudo-depth pressure tests
- evaluation prompt set and rubric
- README with installation and usage guidance for Claude Code and Codex-style setups
- public release support files: MIT license, contribution guide, code of conduct, security policy, and GitHub templates

### Changed

- refined README for public-facing onboarding
- improved skill discoverability wording for Claude Code search
