---
title: "Catena Runtime Failure Taxonomy"
kind: note
created: "2026-08-26"
maturity: developing
tags:
  - catena
  - language-design
  - failure
  - traps
aliases:
  - "Catena failure model"
---

# Catena Runtime Failure Taxonomy

## Executive conclusion

Catena's runtime failure model at `0.1.32` is **one outcome with
kinded reasons**. `trap(reason)` is *the* single runtime failure
outcome — C029's terminal contract (`value | trap(reason)`) restated,
unchanged — and the checklist's six categories map to reason *kinds*
within it, most reserved until their producers exist:

| Category | Classification |
| --- | --- |
| Explicit panic or crash | the kernel's `trap` expression — the only user-invoked failure, elevated |
| Typed failure (`Option`/`Result`) | ordinary **values**, non-failures — G105's types return rather than trap |
| Arithmetic faults | reserved — enters with the first faulting operator, as `trap(reason)` |
| Failed assertions | reserved — enters with the first assert form, as `trap(reason)` |
| Foreign exceptions | reserved — enters with G095/G096, a foreign raise mapping to `trap(reason)` |
| VM termination | operational, outside program semantics — G084/G092/G121 |

**Trap observability elevates the kernel verbatim**: a trapping
process terminates abnormally, discards its mailbox, sends no exit
signal, affects no spawner, and is unobservable through Catena
handles. **Divergence is not failure** (C034's exclusion, restated):
a program that runs forever is running, not failed. The **entry
rule** guarantees no producer ever adds a second outcome class: every
arriving failure kind classifies as `trap(reason)` in its admitting
slice.

The deliverable is witness evidence with **zero new diagnostic
families** — trap agreement with stable reason identity on evaluator
and BEAM, the process-context witness on the stepper (mailbox
discard, spawner unaffected), divergence regression, and the
reserved-kind absences.

## Scope and method

The operational target is independent agreement on the single-outcome
stance, the six-way mapping, trap observability, and the entry rule —
made executable through the witness set. Primary evidence is
internal: [C010's completion-and-trap rules](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md),
[C029's terminal contract](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md),
[C034's divergence exclusion](../60-specification/recursion-and-termination/program-recursion-is-unrestricted.md),
[C005's abort clause](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md),
and [C018's arithmetic deferral](../60-specification/numeric-literal-semantics/README.md).
Source claims stay distinct from Catena proposals below.

## Relation to the current corpus

The [kernel](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
fixes `trap(reason)` as the abnormal terminal with exact side effects
— frozen at 0.1.8. C036 elevates without touching it, as C029–C035
elevated their paragraphs.

[C029](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
fixed `value | trap(reason)` as *the* terminal contract — the
single-outcome stance is its direct corollary, stated here as the
taxonomy's backbone.

[C034](../60-specification/recursion-and-termination/program-recursion-is-unrestricted.md)
fixed divergence as non-termination outside this taxonomy; C036
restates the boundary from the failure side, completing the
three-way partition: **values, traps, and running**.

[C005](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
already classifies the abort clause — a handler that declines to
resume — as an ordinary trap: the effect system cannot intercept a
trap, which the kernel also fixes ("a match cannot catch it"). The
taxonomy inherits: traps are unhandleable by construction.

[C018](../60-specification/numeric-literal-semantics/README.md)
deferred the runtime failure taxonomy for arithmetic to G036; the
answer is the entry rule — no faulting operator exists in the closed
inventory today (Elixir integers are arbitrary-precision; `add`,
`subtract`, `multiply` over finite binary64 produce finite values or
were fixed otherwise), so the arithmetic kind is reserved until a
division-like operator arrives.

## Comparative evidence and inference

### Why one outcome is forced, not chosen

The kernel's status grammar has exactly one abnormal terminal; C029's
contract has two outcomes; C033's statement absence means no
`catch`-like form exists; C005 makes traps unhandleable. A second
outcome class would amend four frozen areas to purchase nothing —
every checklist category is expressible as a reason kind.

### Why typed failure is a non-failure

Option/Result types compute answers including "no answer" — they are
values in C029's grammar, comparable per C035's set, returnable per
C031. Classifying them as failures would make ordinary total
functions "failing" — precisely the confusion G036 exists to remove.
The distinction is honest: **failure is abnormal termination; typed
failure is normal termination with a domain value**.

## Selected model

> **Normative definitions (placed in the candidate chapters).**

### The single outcome

```text
outcome ::= value | trap ( reason )
```

Runtime failure is `trap(reason)` — one outcome, kinded reasons, no
second class ever (entry rule).

### Trap observability (kernel verbatim)

Abnormal termination discards the mailbox; sends no exit signal;
affects no spawner; is unobservable through Catena handles; cannot be
intercepted by handlers or matches.

### The mapping and entry rule

As the table above; producers arrive with their kinds classified as
`trap(reason)` in their admitting slices.

### Rejected alternatives

As enumerated in the resolved inquiry.

## What C036 adds to the design

The three-way partition — values, traps, running — is now stated
once at the language level. G105's library types gain their
classification (non-failures); G095/G096 gain their mapping rule
(foreign raise → trap); the runtime era's exit/monitor work (G084)
gains the guarantee that its signals are *additions outside* the
outcome contract, not new outcomes; and the P109 grammar exercise
gains assert/panic spellings with their semantics already fixed.

## Remaining questions and falsification criteria

G105 owns Option/Result contents; G095/G096 foreign calls; G084
process death, links, and monitors; G092 VM termination; G088
cancellation (distinct from failure); G037 allocation observability
of failure paths; P109 spellings.

The model should be revisited if G084's exit-signal work demands a
program-observable death classification (the remedy is an observably
*delivered* signal in G084's slice composing with the unmodified trap
outcome), or if G095's foreign boundary cannot map some exception to
`trap(reason)` faithfully (the remedy is a bounded presentation of
the foreign reason, not a new outcome class).

## Connections

- The [resolved failure inquiry](../40-inquiries/what-counts-as-runtime-failure.md)
  records the question, hypotheses, and outcome.
- The [Runtime Failure Taxonomy map](../10-maps/runtime-failure-taxonomy.md)
  routes through the kernel rules, the terminal contract, and the
  future owners.
- The Runtime Failure Taxonomy Specification (candidate, then
  normative at promotion, in
  `60-specification/runtime-failure-taxonomy/`) will define the
  contract this note argues for.
- [Catena Values and Evaluation](catena-values-and-evaluation.md)
  fixes the terminal contract this elevates.
- [Catena Recursion and Termination](catena-recursion-and-termination.md)
  fixes the divergence exclusion this restates.

## Sources

- [Actors, Messages, and Failures](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md)
- [Strictness and Terminal Outcomes](../60-specification/values-and-evaluation/strictness-and-terminal-outcomes.md)
- [Program Recursion Is Unrestricted](../60-specification/recursion-and-termination/program-recursion-is-unrestricted.md)
- [Deep Handlers and Affine Resumptions](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
- [Numeric Literal Semantics Specification](../60-specification/numeric-literal-semantics/README.md)
