---
title: "Which Values Compare, and How?"
kind: inquiry
created: "2026-08-26"
status: resolved
tags:
  - catena
  - equality
  - ordering
  - values
  - language-design
aliases:
  - "P035 equality and ordering inquiry"
---

# Which Values Compare, and How?

## Purpose

P035 asks the checklist question: "Define their general expression
forms and floats including NaN, strings, binaries, functions,
references, processes, mixed numeric types, traits, and coercions" —
generalizing C003's fragment-level equality (Bool and mathematical
Int, integer order) to the whole expression language. The general
`equal`/ordering operators exist from C019's inventory but currently
reject everything but Int/Bool (`CND003` in the general path) and
order only Int — Float, a value since C018/C029, has no comparison at
all. This inquiry fixes the comparable set and its semantics.

## Operational definitions

- **Comparable** — admits the equality operators; the closed set is
  fixed by this slice.
- **Orderable** — admits the ordering operators; a subset of the
  comparable set.
- **Bit-exact float equality** — two binary64 values are equal iff
  their 64-bit patterns are equal; `−0.0 ≠ 0.0`.
- **Structural equality** — composite equality, recursive over
  components.

## Hypotheses

1. A new area `equality-and-ordering` at `0.1.30` (code `EQ`) carries
   the contract; C003's clause-conditions stays frozen with its
   Int/Bool guard fragment. *(Recommended: one-version-per-area.)*
2. Float equality is **bit-exact with `−0.0 ≠ 0.0`** and ordering is
   total with `−0.0 < 0.0`; no NaN exists (C018's finite-only
   contract), so the checklist's "including NaN" resolves as an
   elevation of C018's guarantee. *(Recommended: total, zero special
   cases; the OTP-compatibility note records OTP 27 itself moving
   `0.0 =:= -0.0` to false.)*
3. The comparable set is **primitives plus structural recursion** over
   the closed composite grammar (tuples, records, variant injections,
   constructor values) — elevating the kernel's existing
   record-equality fact; **ordering admits Int and Float only** (Bool
   equality-only); **closures and process handles are never
   comparable** (G037/G084 identity exclusions).
4. Comparison is **monomorphic**: `equal` unifies both operands to one
   type; Int-vs-Float is the existing type error — elevating C018's
   no-coercion stance to operators. Strings/binaries don't exist
   (G040 entry rule).
5. Primitive operators are **non-overloadable built-ins**; an Eq/Ord
   trait layer is G101+/G061 library work; any overloading enters
   through the edition-record gate.
6. The deliverable extends `Catena.Values` with the comparable-set
   classification, widens the general operator typing (guard fragment
   untouched — verified independently enforced by `Condition`'s
   `core_type`), adds `EQN001` for non-comparable operands, and
   witnesses on evaluator and BEAM.

## Paths explored

- **IEEE `−0.0 = 0.0`** — rejected: equal-but-distinct values
  complicate structural equality for convention's sake.
- **Defer Float equality to G061** — rejected: leaves C029's tenth
  value form without the most basic operation on it.
- **Primitives only, no structural** — rejected: declines to elevate
  the kernel's existing record-equality fact.
- **Identity equality for closures/handles** — rejected: the exact
  overreach C029 declined.
- **Exact heterogeneous Int↔Float comparison** — rejected as
  primitive; better as a G061-era library function.
- **Trait overloading now** — rejected: drags G061/G101 in
  prematurely.
- **Reuse CND003 for the widened rule** — rejected: muddies family
  ownership; guards keep C003's family, general expressions get their
  own.
- **Normative-only** — rejected pattern.

## Findings

All six hypotheses held; the developer chose the recommended option on
every fork (six of six, no overrides). Planning-time source inspection
resolved all three implementation risks: the guard fragment is
independently enforced (`Condition.core_type` accepts only Int/Bool,
so widening `infer` cannot leak into guards); the BEAM lowering
already lowers `:equal` to `=:=`, which distinguishes the signed zeros
on OTP 27+; and `=:=` gives structural tuple/map equality natively —
the work is typing and evaluator agreement, where the evaluator must
compare floats bit-wise (Elixir `==` equates the signed zeros).

## Outcome

Resolved as C035 at revision `0.1.30`: the contract will live in
`60-specification/equality-and-ordering/`, the reasoning in
[Catena Equality and Ordering](../20-notes/catena-equality-and-ordering.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G037 identity
observability, G040 strings/binaries entries, G061/G101 Eq/Ord trait
layers, and P109 spellings remain open with their owners.
