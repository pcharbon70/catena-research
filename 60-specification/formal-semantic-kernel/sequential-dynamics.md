---
title: "Kernel Sequential Dynamics"
kind: specification
created: "2026-08-06"
status: normative
spec_version: "0.1.8"
tags:
  - evaluation-order
  - formal-semantics
  - specification
aliases:
  - "Catena kernel reduction semantics"
---

# Kernel Sequential Dynamics

## Values and evaluation contexts

Values are integers, Booleans, Unit, tuples of values, closures, nominal
constructor values, records of values, variant injections carrying a value,
and opaque process handles. Evidence, handler declarations, capability names,
resumptions, and traps are not values.

The kernel is strict call by value. Subexpressions evaluate once from left to
right in their written order. This applies to calls, tuple and record fields,
constructor fields, record bases and replacement values, variant payloads,
match scrutinees, operation arguments, spawn arguments, send
target then message, and trap reasons. Every binary operator evaluates its
left operand first. `and` skips its right operand when the left value is false,
and `or` skips its right operand when the left value is true; every other
binary operator then evaluates its right operand exactly once.

> **Normative definition.**

```text
e -> e'                 ordinary sequential step
e -> request(c, op, values, E)  suspended algebraic request
e -> trap(reason)       explicit terminal failure
```

The evaluation context `E` identifies exactly one next subexpression. For a
closed expression without a process operation, at most one ordinary
sequential step applies.

## Functions, bindings, and branching

Applying a closure substitutes one evaluated argument. Calls with several
arguments are repeated unary application. `let x = value; body` substitutes
only after its right-hand side becomes a value. A binding whose name is unused
remains valid and preserves evaluation of its right-hand side.

Named recursive calls use the signed definition environment. General
recursion may reduce forever. A call in tail position, including a call after
pattern or handler selection and a process loop after receive, MUST NOT cause
unbounded growth of the Catena call stack.

Match evaluates its scrutinee once, tests clauses in source order, tests a
condition once after structural success, and commits irreversibly to the
selected body. A condition false result continues with later clauses.

## Record and variant reduction

Records are semantic finite label-to-value maps. Written field order controls
effects but not value equality or row identity.

> **Normative definition.**

```text
select({..., l = v, ...}, l)       -> v
update({fields, l = old}, l, v)    -> {fields, l = v}
extend({fields}, l, v)             -> {fields, l = v}
restrict({fields, l = v}, l)       -> {fields}
inject(l, v)                       is a value
```

Static typing makes the missing-label cases unreachable. Variant matching
tests the semantic label and then matches its payload.

## Traits and handlers

Trait evidence application reduces to the selected implementation and
preserves ordinary argument order. Evidence and laws do not schedule work.
Erasing evidence after specialization preserves values, effects, traps, and
tail position.

An ordinary request evaluates its arguments and suspends with its effect and
operation identity plus the current continuation. The statically selected
nearest installed handler for that effect receives it. Resuming reinstalls
that same handler around the captured continuation, so handling is deep.
Abandoning a resumption performs no step from the discarded continuation.
Verified 0.1.8 core contains at most one syntactic use of each resumption.

If evaluation reaches a request without an installed handler, the current
computation becomes `trap(unhandled-effect(effect, operation))`. This is an
explicit terminal runtime failure, not permission for arbitrary execution.

## Trap dynamics

`trap reason` first evaluates `reason`. Once it is a sendable value, the
current computation becomes `trap(reason)` and takes no ordinary step. A
handler cannot intercept it, a match cannot catch it, and no discarded
continuation or pending branch runs afterward.

## Resource observability

Allocation addresses, closure identity, record-map sharing, garbage
collection, stack-frame shape outside the proper-tail-call guarantee, and
physical copying are not observable Catena values. Process identity is the
only identity-bearing runtime value in this kernel, and its operations are
limited by the process chapter.

[Metatheory](metatheory.md) states the preservation and progress obligations
for these transitions, including explicit traps as specified terminal states.
