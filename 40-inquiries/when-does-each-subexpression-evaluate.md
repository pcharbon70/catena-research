---
title: "When Does Each Subexpression Evaluate?"
kind: inquiry
created: "2026-08-25"
status: resolved
tags:
  - catena
  - evaluation-order
  - language-design
aliases:
  - "P030 evaluation order inquiry"
---

# When Does Each Subexpression Evaluate?

## Purpose

P030 asks the checklist question: fix evaluation order for "general
function and operator arguments, collections, traits, interpolation,
and other forms" beyond the fragments already shipped. The order rules
exist — the kernel fixes strict left-to-right for an explicit list,
and C002, C003, C004, and C005 each fixed their fragment — but they
are scattered across five areas and two boundaries, and the typed-core
forms outside the kernel list (curried application, trait calls,
handler installation) have no consolidated language-level account.
This inquiry elevates and completes that account.

## Operational definitions

- **Ordered form** — a compound expression whose subexpression
  evaluation sequence the language fixes: written left-to-right,
  strictly, with named skips.
- **Effect-request trace** — the observable sequence of effect
  requests an evaluation performs; two evaluations with equal traces
  agree on order for every effect-performing subexpression.
- **Dual-target agreement** — the same program run through the kernel
  stepper and through compiled BEAM execution produces equal traces.
- **Entry rule** — any future compound form declares its order in its
  own normative slice; order never widens silently.

## Hypotheses

1. A new sibling area `evaluation-order` at `0.1.26` (code `EO`)
   carries the contract, completing a trilogy: values (C029, *what*),
   order (C030, *when*), bindings (G031, *structure*).
   *(Recommended: extending C029's three-day-old area would amend
   normative chapters; extending the kernel breaks retained-revision
   immutability.)*
2. One closed ordered-forms table — the kernel's list elevated
   verbatim plus the typed-core completions (curried multi-argument
   application as repeated unary left-to-right, trait-call subject
   then arguments, handler installation before body, annotate
   order-transparent) — with a future-form entry rule, is the right
   account shape. *(Recommended: mirrors C029's closed-grammar +
   entry-rule pattern.)*
3. The G031/G032 boundary is order-versus-structure: P030 owns *when*
   every existing compound evaluates (including the kernel-fixed `let`
   RHS-before-body and sequence order); G031 owns binding structure;
   G032 owns arity and currying as typing concerns.
4. Order is observable semantics: a conforming implementation's
   effect-request trace must equal the declared order's trace,
   generalizing C005's handler-order observability and C004's trait
   traversal rules. *(Recommended: advisory order for pure forms would
   contradict shipped observable-order language.)*
5. Dual-target trace-witness tests — the same effect-ordering corpus
   through the stepper and through BEAM, asserting equal traces — are
   the executable deliverable; no new public module, zero new
   diagnostic families.

## Paths explored

- **General rule only** ("written left-to-right, strictly") — rejected:
  looser than every predecessor chapter and silently conflicts with
   the C029-gated `and`/`or` exceptions.
- **Table without entry rule** — rejected: widens silently when G040
  lands.
- **Advisory order for pure subexpressions** — rejected: contradicts
  C004/C005 observable-order rules and makes trace conformance
  unsound.
- **New `Catena.Order` descriptive module** — rejected: descriptive
  only, no executable force.
- **Fold binding structure in (G031's items)** — rejected: scope creep
  without need.
- **Normative-only** — the archive's rejected pattern.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (five of five, no overrides). One boundary fact
confirmed during planning: the observable-order language already
shipped — C004's "MUST NOT reorder, duplicate, or drop" for trait
traversal and C005's "handler order is observable" — so the
trace-equality requirement generalizes shipped rules rather than
inventing a new observability class. The C005 reference/BEAM
trace-agreement tests are the proven evidence template.

## Outcome

Resolved as C030 at revision `0.1.26`: the contract lives in the
[Evaluation Order Specification](../60-specification/evaluation-order/README.md),
the reasoning in
[Catena Evaluation Order](../20-notes/catena-evaluation-order.md), and
the forks in the [design decision
register](../20-notes/design-decision-register.md). G031 bindings,
G032 calls, G033 branching, P035 equality, G036 failure, G040
collections and interpolation entry, and P109 syntax remain open with
their owners.
