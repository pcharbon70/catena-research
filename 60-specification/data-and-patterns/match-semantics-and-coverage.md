---
title: "Match Semantics and Coverage"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.2"
tags:
  - algebraic-data-types
  - pattern-matching
  - program-semantics
  - specification
aliases:
  - "Catena match coverage"
---

# Match Semantics and Coverage

## Dynamic semantics

The canonical form is:

> **Non-normative example.**

```catena
match value with
| Option.None -> fallback
| Option.Some item -> use(item)
```

Evaluation MUST:

1. evaluate the scrutinee exactly once;
2. test clauses from top to bottom;
3. structurally test the pattern without effects;
4. evaluate the guard only after a successful structural match;
5. select the first structurally matching clause whose guard evaluates to
   `true`; and
6. evaluate only that clause body.

A `false` guard resumes with the next clause. Guards and bodies therefore
retain source order. Clause bodies MUST have one unifiable result type; the
match expression has that type. Effects of the scrutinee, guards, and selected
body are accounted for by the surrounding effect system, while patterns add
none.

No well-typed 0.1.2 program may reach an implicit match-failure exception.
Failure at a foreign or corrupted representation boundary is an internal or
dynamic-boundary failure, not source match semantics.

## Usefulness model

The compiler MUST determine both exhaustiveness and redundancy from one
typed-pattern usefulness relation. Coverage analysis MUST be independent of
backend match lowering.

For each clause, usefulness is tested against prior clauses whose guards are
proved true. A useless clause is invalid. After all clauses, usefulness of a
wildcard candidate determines whether a value remains uncovered. A missing
case is invalid and MUST include a deterministic concrete witness when the
defined witness language can express one.

`or` patterns are semantically the union of their alternatives. An
implementation SHOULD share their pattern matrix rather than eagerly copy
large submatrices, but sharing MUST NOT change usefulness results.

## Type domains

Coverage treats:

- a transparent or local nominal ADT as its visible finite constructor
  signature;
- Boolean as the finite constructors `false` and `true`;
- a tuple as one product constructor;
- integer literals as points in an infinite domain, requiring a wildcard or
  binder for exhaustive coverage;
- an imported abstract type as an open domain with no visible constructors,
  so only a wildcard or binder can close coverage; and
- a GADT constructor as possible only when its refined result is compatible
  with the scrutinee indices.

String, range, structural-variant, list-syntax, and binary coverage are outside
0.1.2 rather than approximated silently.

## Empty and recursive types

Implementations MUST calculate a terminating three-valued inhabitation fact:

> **Normative definition.**

```text
inhabited | empty | unknown
```

The calculation is the least fixed point over a mutually recursive group.
Primitive integers, Booleans, and function values are inhabited. A product is
empty when any component is proven empty, inhabited when every component is
proven inhabited, and otherwise unknown. A datatype is inhabited when some
constructor payload is inhabited, unknown when no constructor is proven
inhabited but one may be, and empty otherwise.

Only a proven-empty scrutinee permits a match with no clauses. Unknown is
treated conservatively. Type parameters and imported abstract types normally
contribute unknown.

## Guards and coverage facts

Coverage consumes only this guard classification:

- **proved true** — the clause contributes its structural pattern;
- **proved false** — the clause is redundant; or
- **unknown** — the clause contributes nothing to exhaustiveness.

The literal guards `true` and `false` supply the first two facts. Any other
well-typed Boolean guard is unknown unless a separately specified certified
oracle proves otherwise. C002 does not infer coverage from arbitrary user
functions or effects. The normative
[0.1.3 clause-condition specification](../clause-conditions/README.md) defines
one such separately checked oracle, exact safe expression set, and receive
harness. The 0.1.3 clause-condition specification explicitly replaces this
conservative condition boundary for accepted conditions and certified coverage
facts; the 0.1.2 structural pattern rules remain applicable.

## Deterministic implementation limit

Coverage MUST terminate. A conforming 0.1.2 implementation MUST support at least
20,000 usefulness steps for one match. If its deterministic budget is
exhausted, it MUST report `M004` as an implementation limit. It MUST NOT label
the source program semantically non-exhaustive or redundant merely because
analysis ran out of budget.

## Decision representation

Accepted clauses elaborate to an ordered acyclic decision representation that
shares the evaluated scrutinee and fallback continuation. Backend lowering
MUST preserve source order, guard fallthrough, and bindings. The typed-core
verifier MUST reject a decision representation not marked exhaustive or not
corresponding to its checked clauses.

## Diagnostics and evidence

`M001` reports non-exhaustiveness and a witness. `M002` reports the first
redundant clause. `M004` reports only deterministic analysis exhaustion.

## Evidence route (non-normative)

The usefulness model is based on the evidence route through
[Maranget 2007](../../30-sources/maranget-2007-warnings-pattern-matching.md).
The executable corpus includes Boolean, integer, nested constructor,
empty-type, abstract-type, guard, `or`, and GADT cases.
