---
title: "Catena Functions and Calls"
kind: note
created: "2026-08-25"
maturity: developing
tags:
  - catena
  - language-design
  - functions
  - currying
  - tail-calls
aliases:
  - "Catena function model"
---

# Catena Functions and Calls

## Executive conclusion

Catena's function model at `0.1.28` is **semantic-unary curried**,
elevated from what every target already does. Every function takes
exactly one argument. A multi-parameter definition desugars to nested
unary functions; a multi-argument call is repeated unary application
under C030's order (callee first, then arguments left-to-right).
There is no fixed arity to check and therefore no arity error to
diagnose — under- and over-application are impossible states, not
invalid inputs.

**Partial application is free**: applying a multi-parameter function
to a prefix of its arguments yields a closure value — first-class,
storable, and callable later, exactly as the shipped compiled evidence
(`choose_first` used as a curried value) already demonstrates.

**Closures capture lexically and immutably**: a closure carries its
defining environment by value — the kernel's
`{closure, parameter, body, environment}` form — and captured
bindings are values that cannot change. What closure *allocation*
lets a program observe remains G037's exclusion.

**The local-function form is the let-bound closure**: `let f = fn x ->
…; …` — non-recursive per C031, lexically captured, first-class.
C031's deferred "named local function" question closes with zero new
machinery. Local recursion stays definitions-only; any future
local-recursion form enters through the edition-record gate.

**Tail calls carry the kernel guarantee, elevated verbatim**: a call
in tail position — including after pattern or handler selection and a
process loop after receive — consumes no unbounded Catena stack. The
witness is a deep tail recursion on compiled BEAM (one million
iterations, dispatched by match selection) completing with the right
value; BEAM's last-call optimization is the native implementation of
exactly this guarantee.

The deliverable is witness evidence with **zero new diagnostic
families and no new public module** — the definitional stance of
C029/C030.

## Scope and method

The operational target is independent agreement on the arity model,
partial application, capture, local functions, and the tail guarantee
— made executable through evaluator/BEAM witnesses. Primary evidence
is internal: the [kernel's closure and tail rules](../60-specification/formal-semantic-kernel/sequential-dynamics.md),
the [backend's tail preservation](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md),
[C030's application-order rows](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md),
[C031's binding discipline](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md),
and the curried-value compiler evidence. Source claims stay distinct
from Catena proposals below.

## Relation to the current corpus

The [kernel's paragraph](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
fixes closures as values, one-argument substitution, repeated unary
application, and the proper-tail-call guarantee — frozen at 0.1.8.
C032 elevates without touching it, as C029–C031 elevated their
paragraphs.

[C010's backend chapter](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md)
states both lowering paths preserve proper tail position — the
elevated guarantee's implementation license, cited rather than
restated.

[C030](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md)
fixed *when* a curried call evaluates; C032 fixes *what it means*:
the arity model, the desugaring, and the value-ness of prefixes. The
two chapters compose without overlap.

[C031](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md)
left "named local functions" explicitly to G032. The answer — the
let-bound closure — inherits C031's non-recursion and shadowing rules
verbatim; nothing here reopens them.

[C002's typed core](../60-specification/data-and-patterns/README.md)
already carries the `{:function, parameter, result}` type constructor
— unary, matching the model; the interface's scheme encoding is the
compatibility surface C028's matrix already classifies.

## Comparative evidence and inference

### Why semantic-unary is an elevation, not a choice

The kernel applies one argument per step; the evaluator builds nested
closures; the compiled evidence returns a curried two-parameter
function as a callable BEAM value. A fixed-arity model would make
shipped behavior nonconformant and would require new arity
diagnostics, new inference cases, and new interface content — a
behavior change dressed as a definition. Elevating semantic-unary
costs one sentence and zero machinery.

### Why the tail witness goes deep on BEAM

A stack-growth bug cannot hide behind a shallow recursion — any
implementation passes 1,000 iterations. The witness runs one million
iterations of a match-dispatched counting recursion — the kernel
guarantee's strongest clause (a call after pattern selection) — where
any per-call stack retention would exhaust BEAM's stack within a
fraction of the depth. Completing with the correct value is
existence-proof-grade evidence; the stepper witnesses termination at
a moderate depth within its own budget, keeping the definitional
machine honest without a million-step run.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### Arity and application

```text
fn (x) -> body                    -- anonymous: one parameter
def name (p1, ..., pn) = ...      -- desugars to nested unary fns
f a1 a2 ... an                    -- repeated unary application
```

- Every function is semantically unary; multi-parameter spellings are
  sugar over nested unary functions.
- Application order is C030's curried-call row.
- Any prefix application is a value (partial application).

### Closures

A closure captures its defining environment by value; captured
bindings are immutable. Allocation identity is G037's.

### Local functions

`let f = fn x -> …; body` — the let-bound closure is the local
function form, with all of C031's rules.

### Tail calls

A call in tail position — after pattern or handler selection, in a
process loop after receive, or as a definition's final value — MUST
NOT cause unbounded growth of the Catena call stack.

### Rejected alternatives

As enumerated in the resolved inquiry: fixed arity, hybrid arity,
by-reference capture, explicit captures, local recursion now, new
sugar forms, tail deferral, arity diagnostics, normative-only.

## What C032 adds to the design

Section 4's expression core is nearly whole: values, order, bindings,
and now functions. G033's branch forms return values through this
model; the stdlib era's combinators (`map`, `and_then`) are curried
by construction; and the widened-P109 grammar gains the application
and parameter spelling decisions with semantics fixed.

## Remaining questions and falsification criteria

G033 owns branch forms; P034 owns termination beyond the tail
guarantee; G037 owns closure allocation and identity observability;
G084 owns process-entry tails beyond C010's clause; P109 owns all
surface spellings.

The model should be revisited if the surface era's ergonomics demand
multi-parameter *native* forms (the remedy is a P109 spelling with
this desugaring as its semantics, not an arity change), or if
optimization work wants uncurried calling conventions (the remedy is
G094's calling-convention slice under this model's semantics).

## Connections

- The [resolved function-model inquiry](../40-inquiries/what-is-catenas-function-and-call-model.md)
  records the question, hypotheses, and outcome.
- The [Functions and Calls map](../10-maps/functions-and-calls.md)
  routes through the kernel rules, the shipped contracts, and the
  future owners.
- The [Functions and Calls Specification](../60-specification/functions-and-calls/README.md)
  defines the normative `0.1.28` contract this note argued for.
- [Catena Bindings and Sequencing](catena-bindings-and-sequencing.md)
  fixes the discipline local functions inherit.
- [Catena Evaluation Order](catena-evaluation-order.md) fixes the
  application schedule this model rides.

## Sources

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
- [BEAM Diagnostics and Conformance](../60-specification/formal-semantic-kernel/beam-diagnostics-and-conformance.md)
- [Ordered Forms and Entry Rule](../60-specification/evaluation-order/ordered-forms-and-entry-rule.md)
- [Binding Structure and Scope](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md)
