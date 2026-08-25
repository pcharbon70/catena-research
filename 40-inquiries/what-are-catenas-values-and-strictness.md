---
title: "What Are Catena's Values and Strictness?"
kind: inquiry
created: "2026-08-24"
status: resolved
tags:
  - catena
  - values
  - evaluation
  - strictness
  - language-design
aliases:
  - "P029 values and evaluation inquiry"
---

# What Are Catena's Values and Strictness?

## Purpose

P029 asks the checklist question: "State precisely that the language
is strict and define which forms are values." The C010 kernel already
fixes a value grammar and strict call-by-value order — but frozen
inside the exact 0.1.8 kernel S-expression boundary, and written
before Float existed (C018). P029 is the elevation of that calculus to
a language-level invariant, completed for post-kernel forms, without
amending any retained revision.

## Operational definitions

- **Value** — a fully evaluated, storable, first-class form: integer,
  Boolean, Unit, Float, tuple of values, closure, nominal constructor
  value, record of values, variant injection carrying a value, or
  opaque process handle.
- **Non-value** — a form that is deliberately never a value: evidence,
  handler declarations, capability names, resumptions (affine), traps,
  effect rows, and signatures.
- **Strict** — every subexpression evaluates at most once, to a value
  or a terminal trap, before it is used.
- **Terminal outcome** — a completed evaluation is a value or a trap; a
  suspended algebraic request is neither, being a pending continuation
  owned by the handler calculus.

## Hypotheses

1. A new area `values-and-evaluation` at `0.1.25` (code `VA`) carries
   the contract; the kernel chapters stay frozen at 0.1.8. *(Recommended:
   extending them would amend a retained revision.)*
2. A closed value grammar — the kernel's nine forms plus Float — with
   the non-value list carried up and completed, is truthful over the
   current language; G040 adds each future type with its own value
   status. *(Recommended: P035 equality and C028 compatibility need a
   decidable closed list.)*
3. All values are uniformly first-class — bindable, passable,
   returnable, storable — with observability of storing process
   handles named as G037/G085's exclusion, not a tier here.
4. Strictness elevates to a language invariant with the kernel's
   `and`/`or` short-circuits as the named exceptions, and any future
   lazy or short-circuit form gated behind a C008 edition record.
5. A total classifier (`Catena.Values.value?/1`) over typed-core and
   kernel terms plus property tests over the shipped stepper is the
   executable deliverable; a definitional slice adds zero new
   diagnostic families.

## Paths explored

- **Extend the kernel chapters in place** — rejected: amends
  normative 0.1.8, breaking the immutable-revision discipline.
- **Open canonical-forms grammar** ("any inhabited type's canonical
  inhabitant") — rejected: looser than everything else in the corpus;
  equality and compatibility need decidable membership.
- **Kernel list verbatim, Float unclassified** — rejected: floats
  demonstrably exist (C018); the list would be knowingly incomplete.
- **Tiered first-classness (passable vs storable)** — rejected:
  pre-decides G037/G085 observability questions this slice need not
  answer.
- **Merge with P030's per-form order** — rejected: the value-grammar
  half should not wait on binding and operator details.
- **Normative-only deliverable** — the archive's rejected pattern.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (five of five, no overrides). Two corpus facts shaped the
design: the stepper's terminal contract already distinguishes exactly
`{:value, …}` and `{:trap, …}`, so the invariant's executable witness
exists in shipped machinery; and typed-core forms carry inference
shapes as maps rather than fixed tags, so the classifier keys on
canonical form tags exactly as C027's result rendering does.

## Outcome

Resolved as C029 at revision `0.1.25`: the contract will live in
`60-specification/values-and-evaluation/`, the reasoning in
[Catena Values and Evaluation](../20-notes/catena-values-and-evaluation.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G031–G033 bindings
and branching, P030 per-form order, P035 equality, G036 failure
taxonomy, G037 observability, G038 compile-time evaluation, and G040's
future types remain open with their owners.
