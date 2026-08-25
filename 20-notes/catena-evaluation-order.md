---
title: "Catena Evaluation Order"
kind: note
created: "2026-08-25"
maturity: developing
tags:
  - catena
  - language-design
  - evaluation-order
aliases:
  - "Catena order model"
---

# Catena Evaluation Order

## Executive conclusion

Catena's evaluation order at `0.1.26` is one closed table plus one
entry rule. The table elevates the kernel's ordered-forms list
verbatim — calls, tuple and record fields, constructor fields, record
bases and replacement values, variant payloads, match scrutinees,
operation arguments, spawn arguments, send-target-then-message, trap
reasons, binary-left-first, the `and`/`or` skips C029 gated, `let`
right-hand-side-to-value before substitution, and sequence
first-then-second — and completes it with the typed-core forms the
kernel list lacks: **curried multi-argument application is repeated
unary left-to-right; a trait call evaluates its subject then its
arguments (consummating C004's traversal rule); a handler installs
before its body evaluates (C005); annotate is order-transparent.**

The entry rule mirrors C029's: any future compound form —
collections, interpolation, every G040 type's compound forms —
declares its order in its own normative slice. Order never widens
silently.

Order is **observable semantics**: a conforming implementation's
effect-request trace must equal the declared order's trace. This
generalizes rules the corpus already shipped — C004's "MUST NOT
reorder, duplicate, or drop" for trait traversal, C005's "handler
order is observable" — rather than inventing a new observability
class. The evidence template is C005's dual agreement: the same
effect-ordering corpus through the kernel stepper and through
compiled BEAM execution, equal traces on both.

The deliverable is trace-witness evidence with **no new public module
and zero new diagnostic families** — the traces are the oracle, the
same definitional stance as C029.

## Scope and method

The operational target is independent agreement on the ordered-forms
table, the typed-core completions, the entry rule, the
order-versus-structure boundary against G031/G032, and observability —
made executable through dual-target trace evidence. Primary evidence
is internal: the [kernel's order rules](../60-specification/formal-semantic-kernel/sequential-dynamics.md),
[C002's scrutinee and field order](../60-specification/data-and-patterns/README.md),
[C003's pattern-and-condition order](../60-specification/clause-conditions/README.md),
[C004's trait traversal](../60-specification/traits-and-categorical-operations/operational-semantics.md),
[C005's handler order](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md),
and [C029's strictness invariant](../60-specification/values-and-evaluation/README.md).
Source claims stay distinct from Catena proposals below.

## Relation to the current corpus

The [kernel's paragraph](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
is the backbone: strict call-by-value, written left-to-right, one
explicit form list, left-first binaries, the two skips. Frozen at
0.1.8 inside the S-expression boundary — this slice elevates it
without touching it, exactly as C029 elevated its value paragraph.

The fragments complete the backbone where the kernel calculus has no
form: C002 fixes single-scrutinee evaluation and source-order
constructor fields for the whole language; C003 fixes
pattern-before-condition, exactly one condition evaluation, lazy
left-to-right Boolean composition, false fallthrough, irreversible
commitment, and shared or-pattern continuations; C004 fixes trait
subject order and callback positions; C005 makes handler order
observable and fixes resumed prefixes at ordinary order. The table's
role is *consolidation*: each fragment keeps its home, and the table
is the one language-level place that says when every existing compound
evaluates.

[C029's invariant](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
— at most once, value-or-trap, before use — sits above the table:
the invariant is the principle, the table is the per-form schedule,
and the same edition-record gate covers any future exception to
either.

The typed-core completions are the new content: the kernel's calculus
has unary application only, so multi-argument calls need their
language-level statement (repeated unary, left-to-right — the curly
`f a b` of the retained JSON frontend already lowers this way); trait
calls carry C004's rule into the call form itself; handler
installation ordering is C005's clause generalized to the expression;
annotate wraps without touching order.

## Comparative evidence and inference

### Why observability is forced, not chosen

C004 and C005 already shipped observable-order language. A conforming
implementation that reordered pure subexpressions would still satisfy
the letter of those fragments but break the corpus's spirit — and,
practically, the trace-agreement conformance evidence. Declaring
order advisory for pure forms would retract shipped rules; the only
coherent consolidation is trace-observable order for every form in
the table. The freedom implementations retain is *within* a step —
register allocation, environment representation, and every other
unobservable choice — which is exactly the boundary C010's trace
semantics already draws.

### Why the evidence needs both targets

The stepper is the definitional machine, but conformance obligations
run against shipped compilers: a rule only "observable" on the
reference machine is advisory in practice. C005 solved this with
reference/BEAM trace agreement, and that pattern is reused verbatim:
one corpus, two executions, equal request traces. The corpus programs
are constructed so order is the only discriminating variable — every
subexpression performs a distinct request, so any reordering changes
the trace.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### The ordered-forms table (summary)

| Form | Order |
| --- | --- |
| Call (curried) | callee, then arguments left-to-right as repeated unary |
| Tuple / record / constructor fields, variant payloads | written order |
| Record update | base, then replacement value |
| Match scrutinee | once, before any clause test |
| Operation arguments | written order |
| Spawn arguments, send | arguments, then target-then-message |
| Trap reason | before the trap terminal |
| Binary operator | left, then right (exactly once each) |
| `and` / `or` | left; right only when not skipped (the C029 exceptions) |
| `let` | right-hand side to a value, then substitution |
| Sequence | first to a value, then second |
| Trait call | subject, then arguments |
| Handler | installs, then body |
| Annotate | transparent — the wrapped form's order |

### The entry rule

A compound form not in the table has no order until its own slice
declares one. Collections, interpolation, and every G040 compound
enter with their order stated where they are introduced.

### Rejected alternatives

- **General rule only** — looser than predecessor chapters; conflicts
  with the gated exceptions.
- **Table without entry rule** — silent widening at G040.
- **Advisory pure-form order** — retracts shipped observability.
- **Descriptive `Catena.Order` module** — no executable force.
- **Fold G031 in** — scope creep.
- **Normative-only** — rejected pattern.

## What C030 adds to the design

Section 4's evaluation core completes: values (C029) and order (C030)
give every later item — G031 bindings, G032 calls, G033 branching — a
fixed schedule to slot forms into rather than a fresh question each.
G040 gains its entry rule; C005's dual-agreement evidence pattern
gains its general statement; and the widened-P109 grammar exercise
gains an order table to keep faithful when surface syntax lands.

## Remaining questions and falsification criteria

G031–G033 own the structure of the forms the table schedules; P035
equality, G036 failure, and G037 observability own adjacent questions;
G040 owns each new form's table entry; P109 owns surface syntax; G088
owns cancellation mid-order.

The model should be revisited if G088-era cancellation needs
partially-evaluated compound semantics (the remedy is a cancellation
chapter that composes with the table, not per-form exceptions), or if
a future optimization proves an entry-rule-ordered form's declared
order wrong for performance (the remedy is an edition record, the
same gate C029 fixed).

## Connections

- The [resolved order inquiry](../40-inquiries/when-does-each-subexpression-evaluate.md)
  records the question, hypotheses, and outcome.
- The [Evaluation Order map](../10-maps/evaluation-order.md) routes
  through the kernel backbone, the shipped fragments, and the future
  owners.
- The [Evaluation Order Specification](../60-specification/evaluation-order/README.md)
  defines the candidate — then normative at promotion — `0.1.26`
  contract this note argues for.
- [Catena Values and Evaluation](catena-values-and-evaluation.md)
  fixes the invariant above this table.
- The [Values and Evaluation map](../10-maps/values-and-evaluation.md)
  is the trilogy's first stop; G031 will be the third.

## Sources

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
- [Operational Semantics](../60-specification/traits-and-categorical-operations/operational-semantics.md)
- [Deep Handlers and Affine Resumptions](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
- [Strictness and Terminal Outcomes](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
- [Actors, Messages, and Failures](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
