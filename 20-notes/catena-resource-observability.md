---
title: "Catena Resource Observability"
kind: note
created: "2026-08-26"
maturity: developing
tags:
  - catena
  - language-design
  - observability
  - identity
aliases:
  - "Catena observability model"
---

# Catena Resource Observability

## Executive conclusion

Catena's resource observability model at `0.1.33` is the kernel's,
elevated once with the checklist's six categories classified.
**Allocation addresses, sharing, garbage collection, and object
identity are not observable** — except process identity, the one
identity-bearing value, fresh per spawn and observable only through
the handle operations the kernel fixes. **Stack use** is observable
only through completion versus the proper-tail-call guarantee
(C032/C034). **Finalization is declared absent** — no destructor,
finalizer, or cleanup form exists, and any arrival goes through the
resource-scope era or the foreign boundary, each shipping its own
semantics.

The model's backbone: **values have semantic identity**. Equal values
are interchangeable; physical representation — copy or share — never
changes meaning. This is what makes C035's structural equality
sufficient (no `eq` beside `equal`), what buys the compiler its whole
freedom budget (sharing, unboxing, deduplication, CPS transformation,
GC movement — the optimizations the deterministic-bytes and
dual-target-agreement evidence rely on), and what keeps programs
deterministic and portable rather than address-sensitive.

**Debugging is relocated, not sacrificed.** The non-observability
rules constrain what *programs* may observe; tools observe the
*implementation* from outside program semantics. The language supplies
the deterministic anchors a debugger consumes — external-harness trace
recording (C010), effect-request traces (C030), trap reasons (C036) —
and G124 owns the tooling built on them.

This closes the deferred-exclusion sweep: C029's uniform-
first-classness exclusions, C032's closure-allocation identity, and
C035's identity-comparison exclusion all resolve here as the second
identity clause — **every value except a process handle has semantic
identity only**.

## Scope and method

The operational target is independent agreement on the six-way
classification, the two-clause identity rule, the finalization
absence, and the debugging-channel distinction — made executable
through the witness set. Primary evidence is internal: [the kernel's
resource-observability paragraph](../60-specification/formal-semantic-kernel/sequential-dynamics.md),
[the actors chapter's identity and message
semantics](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md),
and the C029/C032/C034/C035 deferrals. Source claims stay distinct
from Catena proposals below.

## Relation to the current corpus

The [kernel's paragraph](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
fixes the non-observables and the process-identity exception — frozen
at 0.1.8. C037 elevates it verbatim, as C029–C036 elevated their
paragraphs.

The [actors chapter](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
supplies the identity mechanics: identities are allocated as the
configuration's next fresh identity; `self` returns the current
handle and has no other observation; messages are immutable
first-order values whose physical copy or sharing does not change
their meaning. All three ride into the two-clause rule unchanged.

[C029](../60-specification/values-and-evaluation/value-forms-and-first-classness.md)
named uniform-first-classness's observability exclusions to G037:
storing a handle lets a program observe *what G037/G085 own*. The
answer: storage observes nothing beyond the value itself.

[C032](../60-specification/functions-and-calls/closures-and-tail-calls.md)
deferred closure allocation identity here; [C035](../60-specification/equality-and-ordering/the-comparable-set.md)
declined closure and handle comparison pending this owner. The second
identity clause closes both: closures have semantic identity only,
and process handles are never comparable — the exclusions are now
permanent contract, not deferral.

[C034](../60-specification/recursion-and-termination/program-recursion-is-unrestricted.md)
fixed the tail guarantee as the only stack promise; the six-way
classification folds stack use into that single observable boundary.

## Comparative evidence and inference

### Why non-observability is the purchase, not the price

Three returns justify the stance. **Semantic sufficiency:** with
representation invisible, `equal` is complete — there is no "same but
not equal" to legislate, and C035's structural recursion closes
without an identity tier. **Compiler freedom:** C030 granted
implementations "every unobservable within-step freedom"; observable
addresses or sharing would foreclose exactly the transformations the
byte-determinism and reference/BEAM agreement depend on. **Determinism
and portability:** addresses and stack shapes are machine artifacts;
observing them makes programs non-deterministic run-to-run and
non-portable across conforming implementations, violating the
corpus-wide guarantee.

### Why the debugging channel needs no observability

A debugger is not a Catena program: it runs outside the language's
semantics and is not bound by observational equivalence. It may see
real addresses, stack frames, and closures precisely because the
language never promises programs that view. The corpus already builds
the tool-side channel — the external harness records return and trap
labels (C010/C036), traces are deterministic (C030) — and G124 turns
that channel into tooling. The one genuine cost is recorded honestly:
if the stdlib era wants in-language identity (interning, memoization),
it needs a gated slice, not a loophole in `equal`.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### The six-way classification

| Category | Program observability |
| --- | --- |
| Allocation addresses | none |
| Sharing (record maps, message copy vs alias) | none — semantic identity |
| Garbage collection | none |
| Object identity | process identity only |
| Stack use | completion vs the tail guarantee only |
| Finalization | none — declared absent, gated |

### The two-clause identity rule

1. Process identity is the only identity-bearing value: fresh per
   spawn, observable only through the kernel's handle operations,
   never comparable.
2. Every other value has semantic identity only: equal values are
   interchangeable; closure allocation identity, record sharing, and
   message copying are unobservable.

### Finalization

Declared absence with a gate: cleanup arrives only through G080s/G084
or G095, each shipping its own semantics in its admitting slice.

### Rejected alternatives

As enumerated in the resolved inquiry.

## What C037 adds to the design

The deferred-exclusion sweep closes — every shipped slice's
"remaining G037's" resolves into one contract. The optimizer's freedom
budget becomes normative boundary rather than implementation courtesy;
G080s/G084/G095 receive a clean predecessor stating what they may
observe and when; and G124's debugging program receives its anchor
inventory.

## Remaining questions and falsification criteria

G080s own resource scopes and cleanup; G084 handle operations beyond
the kernel's; G085 message-copy semantics details; G095 foreign
finalization; G124 debugging tools; G040 any representation-adjacent
entries.

The model should be revisited if the stdlib era demands in-language
identity (the remedy is a gated interned-identity slice, never an
`equal` amendment), or if G124's tooling shows the trace anchors
insufficient (the remedy is richer external instrumentation, which the
model already permits).

## Connections

- The [resolved observability inquiry](../40-inquiries/what-may-programs-observe-of-resources.md)
  records the question, hypotheses, and outcome.
- The [Resource Observability map](../10-maps/resource-observability.md)
  routes through the kernel rules, the deferrals, and the future
  owners.
- The Resource Observability Specification (candidate, then normative
  at promotion, in `60-specification/resource-observability/`) will
  define the contract this note argues for.
- [Catena Equality and Ordering](catena-equality-and-ordering.md)
  fixed the comparison exclusions this contract makes permanent.
- [Catena Functions and Calls](catena-functions-and-calls.md) fixed
  the closure-identity deferral this closes.

## Sources

- [Sequential Dynamics](../60-specification/formal-semantic-kernel/sequential-dynamics.md)
- [Actors, Messages, and Failures](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
- [The Comparable Set](../60-specification/equality-and-ordering/the-comparable-set.md)
- [Closures and Tail Calls](../60-specification/functions-and-calls/closures-and-tail-calls.md)
- [Program Recursion Is Unrestricted](../60-specification/recursion-and-termination/program-recursion-is-unrestricted.md)
