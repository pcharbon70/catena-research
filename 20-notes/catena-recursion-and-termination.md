---
title: "Catena Recursion and Termination"
kind: note
created: "2026-08-26"
maturity: developing
tags:
  - catena
  - language-design
  - recursion
  - termination
aliases:
  - "Catena recursion model"
---

# Catena Recursion and Termination

## Executive conclusion

Catena separates recursion from termination by **layer**, at `0.1.31`
as everywhere else. The program layer's recursion is **unrestricted**:
any named definition may call itself — tail or non-tail — and general
recursion may reduce forever. Divergence is **non-termination**, a
terminal non-outcome C029's contract already names: never a trap,
never undefined behavior, never a failed conformance claim. The
proper-tail-call guarantee (C032) remains the only stack-related
promise. No expression-level totality checking exists or is planned;
if a future era wants one, it enters as an edition-record-gated
**opt-in analysis**, never as a validity change.

The meta layer — every evaluator that runs during compilation — is
**total-or-bounded by its own shipped mechanism**: conditions are
acyclic first-order with recursion rejected as `CND004` (C003);
specification examples check under a fixed 20,000-step pure budget
(C006); laws check with bounded samples (C004). One classification
table cites each regime; nothing is amended.

The **entry rule** hands G038 its precondition: any recursive-total
fragment — recursive conditions, law evaluators, compile-time
evaluation — MUST ship with its totality-or-boundedness regime in the
same slice that admits it. No meta-level evaluator may arrive
unbounded.

The deliverable is witness evidence with **zero new diagnostic
families**: non-tail recursion completing (unrestricted recursion is
usable, not merely tolerated), the stepper's `budget_exhausted`
outcome as the executable divergence witness, tail recursion
terminating, `CND004` rejecting recursive conditions, and the 20,000-
step budget intact.

## Scope and method

The operational target is independent agreement on the program stance,
the separation table, and the G038 gate — made executable through the
witness set. Primary evidence is internal: the [kernel's recursion
sentence](../60-specification/formal-semantic-kernel/sequential-dynamics.md),
[C003's `CND004`](../60-specification/clause-conditions/diagnostics-and-conformance.md),
[C006's 20,000-step checker](../60-specification/specifications-and-governance/claims-examples-and-checking.md),
[C004's bounded laws](../60-specification/traits-and-categorical-operations/README.md),
[C029's non-termination clause](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md),
and [C031's definitions-only boundary](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md).
Source claims stay distinct from Catena proposals below.

## Relation to the current corpus

The [kernel](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
fixes "general recursion may reduce forever" with the signed
definition environment and proper tail calls — frozen at 0.1.8.
C034 elevates the sentence without touching it, exactly as C029–C033
elevated their paragraphs.

[C031](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md)
fixed recursion as definitions-only — *where* recursion lives. C034
fixes *what it means*: unrestricted at the program layer, with the
meta layer's separate discipline. The two chapters compose.

[C032](../60-specification/functions-and-calls/closures-and-tail-calls.md)
elevated the tail guarantee — the one stack promise. C034 adds the
complement: non-tail recursion consumes stack without bound and is
nevertheless legal; nothing about it is a conformance claim.

[C029](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
already wrote the divergence clause inside the strictness invariant —
"reduces forever, which is non-termination, not an exception". C034
generalizes that clause from evaluation order to the whole program
layer and gives it an executable witness.

[C003](../60-specification/clause-conditions/diagnostics-and-conformance.md)
(`CND004`), [C006](../60-specification/specifications-and-governance/claims-examples-and-checking.md)
(20,000 steps), and [C004](../60-specification/traits-and-categorical-operations/README.md)
(bounded laws) are the separation table's three shipped rows — cited,
not restated; their regimes are frozen.

[G038's checklist entry](../00-inbox/language-specification-completeness-checklist.md)
asks whether constants, attributes, derivations, or macros execute
code during compilation and under which totality and determinism
restrictions — P034's entry rule answers the *restriction* half in
advance: whatever G038 admits arrives bounded or total, or not at
all.

## Comparative evidence and inference

### Why unrestricted is an elevation, not a choice

Every shipped machine permits general recursion, C032's witness
*runs* deep recursion, and C029 already classifies divergence as
non-termination. A totality requirement would contradict the kernel's
explicit permission and invalidate shipped evidence — a behavior
change dressed as a definition. Elevation costs one sentence.

### Why the gate matters more than the table

The table records what is; the gate constrains what arrives. Without
it, a compile-time evaluator admitted as a "compatible addition"
could hang the compiler on a divergent user program — the exact
regression C008's change-classification discipline exists to prevent.
The entry rule is the deliverable G038 inherits.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### Program recursion (the stance)

```text
Any named definition may recurse; general recursion may reduce
forever. Divergence is non-termination — never a trap, never
undefined behavior. The proper-tail-call guarantee is the only
stack promise. No expression-level termination checking exists;
any future checker is an edition-record-gated opt-in analysis.
```

### The separation table

| Meta evaluator | Regime | Home |
| --- | --- | --- |
| Conditions | acyclic first-order; recursion rejected as `CND004` | C003 |
| Specification examples | fixed 20,000-step pure checker | C006 |
| Laws | bounded law checks and bounded samples | C004 |
| Compile-time evaluation | MUST ship total-or-bounded, in its admitting slice | G038 (gated) |

### The entry rule

A recursive-total fragment enters only through a slice that proves
its totality or fixes its budget. No meta-level evaluator may arrive
unbounded.

### Rejected alternatives

As enumerated in the resolved inquiry.

## What C034 adds to the design

Section 4's partials close one more. G038 receives its precondition;
the P109 grammar exercise receives recursion's confirmed freedom; and
the divergence witness settles, executably, that a non-terminating
program is a *running* program — the honest default the corpus chose
over speculative checking.

## Remaining questions and falsification criteria

G038 owns compile-time evaluation design under the gate; P109 owns
syntax; G036 owns the failure taxonomy (divergence explicitly outside
it); G084 owns process-loop termination beyond the kernel's receive
clause; G088 owns cancellation of long evaluations.

The model should be revisited if the 1.0 era's ecosystem demands
whole-program termination assurance (the remedy is a gated opt-in
analysis service, never a validity change), or if G038's design shows
budgets inadequate (the remedy is a richer regime in G038's own
slice, under the gate).

## Connections

- The [resolved recursion inquiry](../40-inquiries/how-does-catena-separate-recursion-from-termination.md)
  records the question, hypotheses, and outcome.
- The [Recursion and Termination map](../10-maps/recursion-and-termination.md)
  routes through the shipped regimes and the gated future.
- The [Recursion and Termination Specification](../60-specification/recursion-and-termination/README.md)
  defines the candidate — then normative at promotion — `0.1.31`
  contract this note argues for.
- [Catena Functions and Calls](catena-functions-and-calls.md) fixes
  the tail guarantee this stance complements.
- [Catena Bindings and Sequencing](catena-bindings-and-sequencing.md)
  fixes where recursion lives.

## Sources

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
- [Clause Conditions Diagnostics](../60-specification/clause-conditions/diagnostics-and-conformance.md)
- [Claims, Examples, and Checking](../60-specification/specifications-and-governance/claims-examples-and-checking.md)
- [Strictness and Terminal Outcomes](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
- [Binding Structure and Scope](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md)
