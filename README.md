# Michael Polanyi

[![Release](https://img.shields.io/github/v/release/August1314/Michael-Polanyi)](https://github.com/August1314/Michael-Polanyi/releases)
[![License](https://img.shields.io/github/license/August1314/Michael-Polanyi)](https://github.com/August1314/Michael-Polanyi/blob/main/LICENSE)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-skill-7C3AED)](https://github.com/August1314/Michael-Polanyi)
[![GitHub Repo stars](https://img.shields.io/github/stars/August1314/Michael-Polanyi?style=social)](https://github.com/August1314/Michael-Polanyi)
[![CI](https://github.com/August1314/Michael-Polanyi/actions/workflows/ci.yml/badge.svg)](https://github.com/August1314/Michael-Polanyi/actions/workflows/ci.yml)

A writing skill inspired by Michael Polanyi's ideas of tacit knowledge, personal knowledge, and integrative judgment.

Use it when you want AI responses to sound less like a polished summary and more like an experienced practitioner: grounded, directional, bounded, and practically useful.

> [!IMPORTANT]
> This project is a prompt-engineering distillation inspired by selected ideas in Michael Polanyi's work.
> It does **not** attempt to reproduce his philosophy in full, and it does **not** simulate Michael Polanyi as a person.

## Quick start

Install the skill:

```bash
mkdir -p ~/.claude/skills
cp -R skills/michael-polanyi ~/.claude/skills/
```

If you use the `skills.sh` ecosystem, install it directly from GitHub:

```bash
npx skills add https://github.com/August1314/Michael-Polanyi --skill michael-polanyi
```

Restart your client if it only loads skills at startup.

Then try a prompt like:

```text
Use Michael Polanyi to answer this like someone who has done the work: this project keeps reworking the same features — should I fix process, documentation, or staffing first?
```

A good result should:

- lead with a judgment
- surface practical signals
- show boundaries and failure conditions
- end with one concrete next step

## Why this skill exists

Many model answers are:

- correct but generic
- balanced but evasive
- polished but thin
- "deep" in tone but weak in decision value

This skill pushes answers toward:

- clearer overall judgment
- stronger practical signals
- better fact / interpretation / hypothesis separation
- visible trade-offs, limits, and failure conditions
- one concrete next step

## Before / after

**Weak answer**

> It depends on the situation. You should evaluate the process, team structure, and documentation quality, then decide based on the overall context.

**Stronger answer in this skill's style**

> 我的判断是：先别急着换人，也别先补大文档，先补一层最薄但必须执行的流程。项目总在返工，通常不是“没人努力”，而是目标、边界、验收和拍板责任没有在开工前钉死。先看三个信号：需求是否经常中途改口、不同角色是否理解不一致、做完后是否总出现“不是这个意思”。如果这三点里已经中了两点，问题更像流程前门失守，而不是单点执行力差。下一步建议：先硬上四个最小约束——唯一拍板人、单页需求边界、变更记录、每周短演示——连续看两个迭代，再决定是否要动关键岗位。

## Who this is for

Use Michael Polanyi for:

- experienced advice
- practitioner-style critique
- trade-off analysis
- complex decision support
- ambiguous situations with incomplete information
- responses that should sound like they come from someone who has done the work
- prompts like “正确但很空”, “更像真正做过事的人”, or “avoid pseudo-depth”

Do **not** use it for:

- strict JSON or schema output
- deterministic extraction tasks
- exact code transformation
- legal or compliance wording
- tasks where rigid formatting matters more than judgment

## Compatibility

This repository follows the common file-based skill layout used by Claude Code and Codex-style agent tooling.

- Claude Code: `~/.claude/skills/michael-polanyi/SKILL.md`
- Codex-style setups: `~/.agents/skills/michael-polanyi/SKILL.md`

The public title is **Michael Polanyi**.
The technical skill slug is `michael-polanyi`.

> [!TIP]
> In practice, this skill works best as an **explicitly invoked judgment/writing skill**.
> Do not rely on blind auto-discovery for every prompt. Asking for `Michael Polanyi` by name is the most reliable path.

## Install

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R skills/michael-polanyi ~/.claude/skills/
```

Or, with `skills.sh` / `npx skills`:

```bash
npx skills add https://github.com/August1314/Michael-Polanyi --skill michael-polanyi --agent claude-code
```

Expected result:

```text
~/.claude/skills/michael-polanyi/
  SKILL.md
  examples.md
  polanyi-notes.md
  references/
  scripts/
```

### Codex

```bash
mkdir -p ~/.agents/skills
cp -R skills/michael-polanyi ~/.agents/skills/
```

Or, with `skills.sh` / `npx skills`:

```bash
npx skills add https://github.com/August1314/Michael-Polanyi --skill michael-polanyi --agent codex
```

Expected result:

```text
~/.agents/skills/michael-polanyi/
  SKILL.md
  examples.md
  polanyi-notes.md
  references/
  scripts/
```

If your client only loads skills at startup, restart the session after installation.

## How to use it

### Option 1: Name the skill directly

Ask for the skill by name when you want a more grounded judgment style:

- `Use Michael Polanyi to evaluate whether this architecture should go to production.`
- `Use Michael Polanyi to critique this recommendation and tell me where it sounds inexperienced.`
- `Use Michael Polanyi to answer this with a clear judgment, practical signals, and one next step.`

### Option 2: Ask for the pattern without naming it

You can also request the response contract directly:

- `Give me a directional judgment, not a balanced preamble.`
- `Separate facts, interpretations, and hypotheses.`
- `Surface the subtle practical signals an experienced operator would notice.`
- `Show trade-offs, failure conditions, and what would change your mind.`
- `Avoid pseudo-depth or fake wisdom.`

## 30-second self-check

After installation, try one of these prompts:

- `Use Michael Polanyi to answer this like someone who has done the work: the team is stuck and not shipping.`
- `Use Michael Polanyi to tell me why this answer sounds correct but inexperienced.`

The output should usually contain:

- an upfront judgment
- subtle but practical signals
- explicit boundaries or flip conditions
- a concrete next step

## Maintainer workflow

This repository also includes maintainer tooling under `workbench/`.
If you are iterating on the skill rather than just installing it, start with:

- `workbench/README.md`
- `workbench/evals/protocol.md`
- `registry/skillhub-submission.json` if you are submitting the skill to an external market index such as aghub / skillhub
- `registry/README.md` if you need a skillhub-ready zip package and update manifest

The published GitHub Wiki is versioned in this repository under `docs/wiki/`.

## Troubleshooting

### The skill does not appear to load

Check:

- the directory name is exactly `michael-polanyi`
- `SKILL.md` exists at the top level of that directory
- the `name` field in frontmatter is also `michael-polanyi`
- your client has been restarted if it only loads skills at startup

### The skill is installed but not automatically discovered

That can happen.
This repository is best treated as an explicitly invoked judgment/writing skill.
Use the skill by name when reliability matters.

### The output sounds more literary, not more useful

That is drift, not success.
Re-check the response against the expected traits:

- clearer judgment
- better practical signal density
- sharper boundaries
- stronger next-step usefulness
- less pseudo-depth, not more

## Repository map

```text
skills/michael-polanyi/
  SKILL.md            # main runtime skill entrypoint
  README.md           # runtime package guide
  examples.md         # high-value before/after examples
  polanyi-notes.md    # conceptual grounding
  references/         # deeper runtime references
  scripts/            # runtime/lightweight quality helpers

workbench/
  README.md           # maintainer workflow
  evals/              # prompts, rubric, eval set, protocol
  agents/             # blind comparison and grading prompts
  scripts/            # assertion and benchmark helpers
  eval-viewer/        # HTML review generator

registry/
  skillhub-submission.json  # minimal market/registry submission record
  README.md                 # package + submission notes

docs/wiki/
  *.md                # versioned source for the published GitHub Wiki
```

## Evaluation

Do not judge this project by branding alone. Judge it by output quality.

Use:

- `workbench/evals/prompts.md` for prompt sets
- `workbench/evals/rubric.md` for scoring
- `workbench/evals/protocol.md` for the actual test method

A good "after" answer should become:

- more grounded
- more directional
- more bounded
- more useful

It should **not** merely become:

- more literary
- more philosophical
- more confident without grounds

## Limitations

This project is:

- a prompt-engineering skill
- a judgment and writing pattern
- a practical distillation, not an academic reconstruction

This project is **not**:

- Michael Polanyi simulated as a persona
- a universal answer improver for all tasks
- a guarantee of automatic skill discovery
- a tool for strict structured output or compliance-sensitive wording

## Language note

The repository README is written mainly in English.
Several examples and eval prompts are currently in Chinese because they were developed around Chinese judgment-style test cases.
The pattern itself is not language-specific.

## Contributing

See:

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `CHANGELOG.md`

## Why the name

The project uses **Michael Polanyi** as the public-facing name because the skill is explicitly inspired by Polanyi's ideas of tacit knowledge and responsible judgment.

The implementation is practical, not academic:
it translates selected ideas into prompt-engineering rules for more experienced-sounding, more useful output.
