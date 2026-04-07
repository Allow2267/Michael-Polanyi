# Michael Polanyi — Practitioner Judgment Skill

## What This Skill Does

Produces answers that feel like they come from an experienced practitioner — grounded, holistic, and practically useful — for ambiguous, trade-off-heavy scenarios where generic AI answers sound correct but useless.

## When to Use

| Scenario | Examples |
|----------|----------|
| Architecture decisions | "能不能上生产？", "要不要拆微服务？" |
| Team dynamics | "团队推进不动", "项目返工" |
| Career choices | "职业选择的隐性成本", "两份offer怎么选" |
| Incomplete information | "信息不够但老板现在就要建议" |
| Tacit knowledge | "调试手感是什么", "行业潜规则" |
| Critique of answers | "为什么这段回答看起来不像做过事的人写的" |

## File Structure

```
michael-polanyi/
├── SKILL.md                      # Main skill definition (auto-triggered)
├── examples.md                   # Before/after demonstrations
├── polanyi-notes.md              # Core concept reference
├── scripts/
│   └── detect_fluff.py           # AI-generic pattern detector
└── references/
    └── response-patterns.md      # Extended patterns and deep analysis
```

## Quick Start

Just describe your situation naturally. The skill will auto-trigger when it detects:
- Requests for practitioner judgment
- Ambiguous decisions with trade-offs
- Tacit knowledge questions
- Critiques of generic AI answers

## Design Philosophy

This skill is inspired by Michael Polanyi's concepts of **tacit knowledge** and **personal knowledge**. Key principles:

1. **Lead with judgment** — Start with a position, not a preamble
2. **Surface signals** — Name what experienced practitioners notice
3. **Articulate trade-offs** — Every judgment has conditions
4. **End with action** — One concrete next step, not a menu

## Testing

```bash
# Run fluff detection on any response
python scripts/detect_fluff.py <response-file>

# Test with examples
python scripts/detect_fluff.py examples.md
```
