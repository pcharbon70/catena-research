---
title: "How Can Catena Complete Its Language Definition?"
kind: inquiry
created: "2026-09-06"
status: open
tags:
  - catena
  - language-design
  - specification
  - conformance
aliases: []
---

# How Can Catena Complete Its Language Definition?

## Why this matters

The [completion ledger](../00-inbox/language-specification-completeness-checklist.md)
contains strong bounded contracts alongside missing public-runtime,
interoperability, library and delivery work. An implementable language needs
these parts to compose, and its public vocabulary remains deliberately
unselected by the current work request.

## Operational question

Can every admitted checklist boundary obtain explicit normative meaning,
working compiler/reference behavior, positive and negative conformance
evidence, and measured practical integration, without premature vocabulary
decisions or inflated completion claims?

The [implementation plan](../20-notes/language-completion-plan.md) gives the
per-item work and dependencies. Its decisions are recommended agent selections
under user delegation; they are proposals until the appropriate normative
and implementation gates make them durable.

## Working hypotheses

1. The retained kernel and JSON interfaces can establish functional semantics
   before the final parser. This is testable with integrated data, effects,
   resources, actors and checked foreign adapters over those inputs.
2. Extensional laws and operational contracts need separate evidence.
   Effect-order traces and failure prefixes can falsify a supposedly lawful
   implementation even when its pure values agree.
3. Runtime, foreign and tool interfaces can be staged without dependency
   deadlock by specifying their shared semantic contracts before layering
   public APIs or grammar on them.
4. A complete list of theorem targets does not imply a proof of composition.
   The formal-validation program must either discharge the remaining lemma
   or state its exact release disposition without claiming proved soundness.

## Paths to explore

- Execute the plan's M1 comprehension evidence repair against
  [the current conformance contract](../60-specification/list-comprehensions/diagnostics-and-conformance.md#required-evidence-sets).
- Resolve [selective receive's conflict](how-does-selective-receive-complete.md)
  by explicit normative applicability and behavioral witnesses.
- Use [effects research](../20-notes/algebraic-effects-and-handlers.md) and
  [the kernel](../60-specification/formal-semantic-kernel/README.md) to
  define resource/cancellation/process composition before foreign adapters.
- Maintain an integrated corpus and the
  [formal-validation inquiry](what-should-a-greenfield-catena-type-system-guarantee.md#outcome)
  through every admission, rather than delaying assurance to a final phase.

## Findings

The [baseline audit](../50-journal/2026-09-06-checklist-completion-audit.md)
established the initial scope and four reopened claims. The
[execution journal](../50-journal/2026-09-06-language-completion-plan.md)
records subsequent planning checks and experiments. A planned direction is
not evidence of feature completion.

The first implementation establishes locally handled comprehension traces
and exposes a limit to the retained-input hypothesis: general C005-style
escaping-effect rows need an explicitly versioned refinement of the C010
target. Independently valid call/handler backend repairs can proceed while
that normative dependency remains open. The journal distinguishes these
two outcomes and retains partial checklist status.

## Outcome

Open. Closure requires all admitted semantic and implementation boundaries,
public adoption after the user's vocabulary hold is released, integrated
validation and an honest readiness report. Self-hosting retains its separate
late-0.x gate; deferred features require explicit scoped dispositions.
