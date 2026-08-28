---
title: "How Does Catena Separate Recursion from Termination?"
kind: inquiry
created: "2026-08-26"
status: resolved
tags:
  - catena
  - recursion
  - termination
  - language-design
aliases:
  - "P034 recursion and termination inquiry"
---

# How Does Catena Separate Recursion from Termination?

## Purpose

P034 asks the checklist question: "Separate unrestricted program
recursion from future recursive total fragments used by conditions,
specifications, laws, and compile-time evaluation." The substance
exists — the kernel permits general recursion to reduce forever,
C003 rejects recursive condition predicates (`CND004`), C006 checks
specification examples under a fixed 20,000-step budget, C004 checks
laws with bounded samples — but no language-level statement draws the
line between the program layer, where recursion is unrestricted, and
the meta layer, where every evaluator is total-or-bounded. This
inquiry draws it and gates the future fragments.

## Operational definitions

- **Program recursion** — recursion among named definitions, executed
  as program evaluation.
- **Meta-level evaluator** — machinery that runs during compilation:
  condition evaluation, specification-example checking, law checking,
  and future compile-time evaluation.
- **Total-or-bounded** — either provably terminating or executed
  under an explicit fixed budget.
- **Divergence** — a computation that reduces forever; a terminal
  *non*-outcome, distinct from a trap.

## Hypotheses

1. A new area `recursion-and-termination` at `0.1.31` (code `RT`)
   carries the separation; the kernel, C031, and C032 stay frozen and
   cited. *(Recommended: one-version-per-area.)*
2. Program recursion is **unrestricted, elevated**: no expression-level
   totality checking exists or is planned; divergence is
   non-termination — never a trap, never undefined behavior (C029's
   terminal contract already says so); the tail guarantee is the only
   stack promise; any future termination checker would be an
   edition-record-gated opt-in analysis, never a validity change.
   *(Recommended: the kernel's explicit permission is an elevation,
   not a choice.)*
3. The separation is **one cited classification table**: conditions
   acyclic (`CND004`, C003), specifications bounded (20,000 steps,
   C006), laws bounded (C004) — every meta-level evaluator
   total-or-bounded by its own already-shipped mechanism.
4. Future recursive-total fragments — G038 compile-time evaluation
   foremost — face an **entry rule**: they MUST ship with their
   totality-or-boundedness regime in the admitting slice; no
   meta-level evaluator may arrive unbounded.
5. The deliverable is witnesses with zero new diagnostic families:
   non-tail recursion completing (unrestricted is usable), the
   stepper's `budget_exhausted` outcome as the divergence witness,
   tail recursion terminating, `CND004` rejecting recursive
   conditions, and determinism.

## Paths explored

- **Reserve a termination checker** — rejected: nothing demands it;
  reserving invites speculative design.
- **Require termination now** — rejected: contradicts the kernel's
  explicit "may reduce forever" and C032's witness.
- **Minimal prose without the table** — rejected: loses the one-place
  answer P034 explicitly asks for.
- **Design the recursive-total fragment now** — rejected: G038's and
  C003's territory dragged into a classificatory slice.
- **No gate for G038** — rejected: an unbounded compile-time evaluator
  could arrive as a compatible addition.
- **Analysis module / normative-only** — rejected patterns.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (five of five, no overrides). One witness-shape
refinement: the divergence witness asserts the stepper's
`budget_exhausted` outcome under an explicitly small budget — the
definitional machine's honest report that divergence is divergence,
distinct from a trap — rather than timing out the test itself.

## Outcome

Resolved as C034 at revision `0.1.31`: the contract will live in
`60-specification/recursion-and-termination/`, the reasoning in
[Catena Recursion and Termination](../20-notes/catena-recursion-and-termination.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G038 compile-time
evaluation design, P109 syntax, G036 failure taxonomy, and G088
cancellation remain open with their owners.
