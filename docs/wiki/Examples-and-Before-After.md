# Examples and Before/After

This page curates the strongest runtime-facing examples without copying the entire canonical example file.

Canonical source:

- [Full examples.md](https://github.com/August1314/Michael-Polanyi/blob/main/skills/michael-polanyi/examples.md)

## Architecture Judgment

**Prompt**

> “这个架构方案能不能上生产？目前是单体应用，逻辑越来越复杂，但团队只有 3 个人。”

**Weak answer snippet**

> “这取决于系统稳定性、性能和业务需求……建议根据实际情况综合考虑，并持续优化架构。”

**Practitioner answer snippet**

> “我的判断是：可以上生产，但不应该先把主要精力放在拆微服务上……真正要看的不是架构口号，而是三个信号……”

**Why the after version works**

- it takes a position immediately
- it surfaces diagnostic signals
- it names the real trade-off
- it ends with a concrete next step

## Team / Process Judgment

**Prompt**

> “团队推进不动，该怎么处理？”

**Weak answer snippet**

> “先明确目标和分工，拆解任务，加强沟通，并定期同步进度……”

**Practitioner answer snippet**

> “我的判断是：团队推进不动，表面上看像执行问题，实际上更常见的是责任边界不清或优先级并不真的一致……”

**Why the after version works**

- it rejects abstract management advice
- it reframes the issue into an operational diagnosis
- it gives a concrete inspection artifact instead of a slogan

## Incomplete-Information Judgment

**Prompt**

> “我手上信息不完整，但老板现在就要建议，我该怎么答？”

**Weak answer snippet**

> “建议先补充更多资料，再做判断……等信息完整后再给出更准确的建议。”

**Practitioner answer snippet**

> “我的判断是：信息不完整时，不能装作全知，但也不能把‘信息不够’原样退回去。更成熟的答法是：给一个带条件的当前判断。”

**Why the after version works**

- it preserves decisiveness under uncertainty
- it separates known facts, current judgment, and flip conditions
- it recommends a reversible path instead of a vague caution

## Critiquing Inexperienced Answers

**Prompt**

> “为什么这段回答看起来正确，但不像一个真正做过事的人写的？”

**Weak answer snippet**

> “因为它缺少细节和场景，虽然逻辑正确，但不够具体……”

**Practitioner answer snippet**

> “我的判断是：这段话的问题不是‘对错’，而是它只给了显性原则，没有给出真正支撑判断的实践线索。”

**Why the after version works**

- it identifies the failure mode precisely
- it explains what practitioners naturally surface
- it turns critique into a rewrite strategy

## How to Read These Examples

Use these examples to learn the shape of the skill, not to memorize wording.

What should transfer:

- judgment first
- subtle signals
- visible boundaries
- one next step

For the full current runtime example set, see the repo’s [examples.md](https://github.com/August1314/Michael-Polanyi/blob/main/skills/michael-polanyi/examples.md).

If you want the broader maintainer-side guidance on anti-patterns and pseudo-depth drift, use the [workbench guide](https://github.com/August1314/Michael-Polanyi/blob/main/workbench/README.md) instead.
