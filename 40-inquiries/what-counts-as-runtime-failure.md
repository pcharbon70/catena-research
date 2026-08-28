---
title: "What Counts as Runtime Failure?"
kind: inquiry
created: "2026-08-26"
status: resolved
tags:
  - catena
  - failure
  - traps
  - taxonomy
  - language-design
aliases:
  - "G036 failure taxonomy inquiry"
---

# What Counts as Runtime Failure?

## Purpose

G036 asks the checklist question: "Distinguish typed failure, explicit
panic or crash, arithmetic faults, failed assertions, foreign
exceptions, and VM termination." The kernel already answers the core:
`trap(reason)` is the single terminal abnormal outcome, with fixed
side effects. This inquiry fixes the taxonomy at the language level —
one outcome with kinded reasons — and maps the checklist's six
categories honestly, most of whose producers do not exist yet.

## Operational definitions

- **Runtime failure** — abnormal termination of an evaluation or
  process: the `trap(reason)` terminal outcome.
- **Kind** — a classification of a trap's reason by its producer
  (explicit trap, arithmetic fault, assertion, foreign raise).
- **Typed failure** — a domain value (Option/Result-shaped) returned
  by an ordinary function; a non-failure by classification.
- **VM termination** — operational death of a process or runtime
  outside program semantics.

## Hypotheses

1. A new area `runtime-failure-taxonomy` at `0.1.32` (code `FT`)
   carries the contract; the kernel, C029, and C034 stay frozen and
   cited. *(Recommended: one-version-per-area.)*
2. **One outcome, kinded reasons**: `trap(reason)` is the single
   runtime failure outcome — the checklist's six categories are
   reason kinds within it. *(Recommended: elevation of the kernel's
   exact stance; multiple outcome classes would amend frozen
   grammar.)*
3. The six-way mapping: explicit panic = the kernel `trap`
   expression, elevated; typed failure = ordinary values (G105
   returns rather than traps); VM termination = operational, outside
   program semantics (G084/G092/G121); arithmetic faults,
   assertions, and foreign exceptions = **reserved kinds** entering
   with their producers.
4. Trap observability elevates the kernel verbatim: abnormal
   termination discards the mailbox, sends no exit signal, affects
   no spawner, is unobservable through Catena handles — witnessed on
   the stepper (process context) and BEAM (trap agreement).
5. The entry rule (per producer): arithmetic faults enter with the
   first faulting operator, assertions with the first assert form,
   foreign exceptions with G095/G096 — each classified as
   `trap(reason)` on arrival; no producer, no kind; no second
   outcome class ever.

## Paths explored

- **Multi-class outcomes** (trap + fault + exit) — rejected: amends
  the kernel's frozen status grammar and C029's terminal contract.
- **All six defined now** — rejected: five of six producers don't
  exist; defining their semantics would be invention.
- **Pre-defined reason spellings** — rejected: identities no producer
  mints.
- **Trap only, mapping deferred** — rejected: leaves the checklist's
  explicit distinction undelivered.
- **Classification without side-effect rules** — rejected: what a
  trap *does* is most of its meaning.
- **Link/monitor exit semantics** — rejected: G084's machinery,
  frozen out of the kernel by C010.
- **Classification module / normative-only** — rejected patterns.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (six of six, no overrides). One witness-shape
refinement: the process-context witness composes two shipped shapes —
a spawner and a trapping child (C010 fixture territory) — asserting
the spawner's outcome is unaffected and the child's mailbox is
discarded, rather than inventing new process machinery; and the BEAM
trap agreement asserts the *reason value's identity*, not merely that
both targets trap.

## Outcome

Resolved as C036 at revision `0.1.32`: the contract lives in the
[Runtime Failure Taxonomy Specification](../60-specification/runtime-failure-taxonomy/README.md),
the reasoning in
[Catena Runtime Failure Taxonomy](../20-notes/catena-runtime-failure-taxonomy.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G105 library
contents, G095/G096 foreign calls, G084 process death, G092 VM-level
termination, G088 cancellation, and P109 assert/panic spellings
remain open with their owners.
