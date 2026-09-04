---
title: "Are Exceptions an Effect, a Trap, or a Value?"
kind: inquiry
created: "2026-09-01"
status: resolved
tags:
  - catena
  - failure
  - effects
  - language-design
aliases:
  - "G081 exception boundary inquiry"
---

# Are Exceptions an Effect, a Trap, or a Value?

## Purpose

G081 asks the checklist question: "Decide whether exceptions are
an effect, process exits, foreign failures, programmer panics, or
several distinct mechanisms, and how each is typed and caught."
The corpus had already partitioned most of the space — C036's
single terminal `trap(reason)` with kinded reasons, C044's
permanent exclusion of exception clauses with a reopening arrival
condition, C005's calculus where a handler may decline to resume —
so the completion is the partition stated, the pattern blessed,
and the neighbors routed.

## Operational definitions

- **Terminal failure** — an outcome a program cannot intercept:
  `trap(reason)`, kinded, local to its process.
- **Typed failure** — failure as an ordinary value (`Option`-,
  `Result`-shaped), fully first-class.
- **The effect pattern** — exception-style catching expressed with
  C005 machinery: a request whose handler declines to resume is a
  one-shot escape, visible in the effect row, catchable only by an
  enclosing handler.

## Hypotheses

1. A new area `exception-boundary` at `0.1.47` (code `XB`) carries
   the decision as a classification/routing slice. *(Recommended:
   the C044/C067 shape.)*
2. **The partition**: several visibly distinct mechanisms and no
   language exception form — `trap` is the one terminal mechanism
   (never catchable); typed failure is a value (G103's contents);
   exception-style catching is the effect pattern, a library
   idiom, not a mechanism. Mechanisms never blur: typed,
   effectual, and fatal stay distinguishable at every site.
3. **Panics are traps**: the programmer panic is `trap` with the
   reserved assertion/panic kind, entering with its producer under
   C036's per-producer gate — no separate construct.
4. **The pattern is blessed explicitly**: a handler's choice not to
   resume is the sanctioned exception-style escape — descriptive
   of C005's standing semantics, witnessed, adding no rule.

## Paths explored

- **Admit a language exception mechanism** — rejected:
  contradicts C036's terminal trap, C044's exclusion, and
  duplicates what the effect calculus already expresses.
- **A separate panic construct** — rejected: fractures the
  three-way partition and reopens C036 for no gain.
- **Leave the effect-pattern reading unstated** — rejected: G081's
  clause names "an effect" as a candidate answer; the honest
  answer is "yes, as an idiom," and it should be said.
- **Defer to the process era** — rejected: leaves the runtime
  slices designing against an unstated boundary.

## Findings

All four hypotheses held; the developer chose the recommended
option on all four forks (no overrides). The decisive corpus
facts: C036 already kinded the space, C044 already closed the
language-form door with a reopening condition, and C005's affine
resumptions already make non-resume the natural escape — the
partition was standing; only the statement was missing.

## Outcome

Resolved as C081 at revision `0.1.47`: the contract will live in
`60-specification/exception-boundary/`, the reasoning in
[Catena Exception Boundary](../20-notes/catena-exception-boundary.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G084, G088,
G095/G096, G103, and G105 own their routed halves; Section 9
advances to 6/8.
