---
title: "What May Programs Observe of Resources?"
kind: inquiry
created: "2026-08-26"
status: resolved
tags:
  - catena
  - observability
  - identity
  - resources
  - language-design
aliases:
  - "G037 resource observability inquiry"
---

# What May Programs Observe of Resources?

## Purpose

G037 asks the checklist question: "State which allocation, sharing,
object identity, garbage collection, stack use, and finalization
behaviors programs may observe." The kernel's resource-observability
paragraph already fixes the model — non-observability of
representation, process identity as the sole identity-bearing value —
and four shipped slices deferred their exclusions here. This inquiry
elevates the model, classifies the six categories, and closes the
deferrals.

## Operational definitions

- **Observable** — a behavior a conforming *program* can distinguish
  through the language's values, outcomes, and traces.
- **Semantic identity** — equal values are interchangeable; physical
  representation (copy vs share) never changes meaning.
- **Identity-bearing value** — a value whose identity, not just its
  content, carries meaning.
- **Finalization** — code running at resource death.

## Hypotheses

1. A new area `resource-observability` at `0.1.33` (code `RO`)
   carries the contract, completing the deferred-exclusion sweep
   (C029, C032, C034, C035). *(Recommended: one-version-per-area.)*
2. The model is **kernel verbatim with the six-way classification**:
   allocation addresses, sharing, GC, and object identity (except
   process identity) non-observable; stack use observable only
   through completion vs the tail guarantee; finalization declared
   absent. Values carry semantic identity.
3. Finalization is **declared absence with a gate**: no destructor,
   finalizer, or cleanup form exists; any arrival goes through the
   resource-scope era (G080s/G084) or the foreign boundary (G095),
   each shipping its own semantics.
4. The identity rule is **two clauses**: process identity is the only
   identity-bearing value — fresh per spawn, observable only through
   the kernel's handle operations, never comparable; every other
   value has semantic identity only, closing C032's closure-identity
   and C035's identity-comparison deferrals.
5. The deliverable is witnesses with zero new diagnostic families:
   semantic-identity agreement on evaluator and BEAM, the
   process-identity witness on the stepper, allocation
   non-observability absences, and finalization absence.

## Paths explored

- **Admit observables now** (closure identity for debugging) —
  rejected: contradicts the frozen kernel paragraph; and unnecessary,
  because debugging observes the *implementation* from outside program
  semantics (G124's channel: external harness traces, effect-request
  traces, trap reasons).
- **List-only model** — rejected: loses the one-place six-way answer.
- **Design cleanup scopes now** — rejected: G080's territory.
- **Reserve finalizer spellings** — rejected: no semantics to spell.
- **Defer closure identity** — rejected: leaves C032's and C035's
  deferrals open after the slice they named as owner.
- **Handle identity equality** — rejected: amends C035's just-shipped
  exclusion.
- **Identity helpers / normative-only** — rejected patterns.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (five of five, no overrides). One rationale refined
during planning, worth recording: the non-observability stance is
what *buys* the compiler its freedom budget (sharing, unboxing,
deduplication, CPS, GC movement — the optimizations the
deterministic-bytes and dual-target evidence rely on) and what makes
C035's structural equality sufficient — observable sharing would
force an `eq` beside `equal` and make "sameness" depend on allocation
choices programs never made. Debugging is relocated, not sacrificed:
tools observe the implementation; programs observe semantics.

## Outcome

Resolved as C037 at revision `0.1.33`: the contract lives in the
[Resource Observability Specification](../60-specification/resource-observability/README.md),
the reasoning in
[Catena Resource Observability](../20-notes/catena-resource-observability.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G080s resource
scopes, G084 handle operations, G095 foreign finalization, and G124
debugging tools remain open with their owners.
