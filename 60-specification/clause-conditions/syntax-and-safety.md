---
title: "Clause Condition Syntax and Safety"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.3"
tags:
  - pattern-matching
  - program-semantics
  - specification
  - type-inference
aliases:
  - "Catena condition-safe fragment"
---

# Clause Condition Syntax and Safety

## Clause form

The version 0.3 surface shape is:

> **Normative definition.**

```text
pattern when condition -> body
```

An omitted `when` is equivalent for selection and coverage to the literal
condition `true`, but implementations need not materialize that literal. A
condition reads bindings established by its clause pattern and surrounding
immutable lexical scope. It introduces no binding.

The bootstrap JSON AST 0.3 represents unary and binary operations explicitly
and represents multi-clause definitions as one signed definition with a
nonempty, common-arity clause list. Earlier AST versions MUST reject 0.3
condition declarations, operators, and multi-clause definition encoding.

## Static judgment

The checking judgment is conceptually:

> **Normative definition.**

```text
K ; Γ ; P ⊢condition e : Bool ⇒ c ; deps
```

`K` is the verified condition-predicate catalog, `Γ` contains immutable values,
`P` contains pattern bindings, `c` is normalized condition core, and `deps` is
the set of referenced predicate identities. Success requires:

- the inferred result is exactly `Bool`;
- the inferred effect is empty;
- every operation belongs to the closed 0.3 set;
- every operation is total for every value of its admitted type;
- every predicate call is direct, fully applied, and resolves to verified
  condition evidence;
- the dependency graph is acyclic; and
- normalization and transitive inlining stay inside the deterministic budget.

There is no truthiness conversion. A value of type `Int` is not a condition.

## Exact initial expression set

The 0.3 fragment admits only:

| Form | Type and meaning |
| --- | --- |
| `true`, `false` | Boolean literals |
| immutable variable | a value already typed as `Bool` or `Int` where the enclosing operation requires it |
| `not a` | total Boolean negation |
| `a and b` | lazy Boolean conjunction; evaluate `b` only when `a` is true |
| `a or b` | lazy Boolean disjunction; evaluate `b` only when `a` is false |
| `a == b`, `a != b` | exact equality or inequality, with both operands either `Bool` or `Int` |
| `a < b`, `a <= b`, `a > b`, `a >= b` | integer order |
| `-a` | total mathematical-integer negation |
| `a + b`, `a - b`, `a * b` | total mathematical-integer arithmetic |
| `predicate(args...)` | direct, fully applied call to a verified condition predicate |

`Int` in this version 0.3 slice is the unbounded mathematical integer already
used by the bootstrap model. A future fixed-width or foreign integer type MUST
state overflow and comparison rules separately.

Equality is exact: a Boolean is never numerically equal to an integer, and no
coercion or defaulting occurs. Trait or method resolution does not participate
in 0.3 condition operators.

## Excluded forms

The checker MUST reject:

- an ordinary function call, even when its current implementation appears
  pure;
- a partial or domain-restricted primitive, including division and remainder;
- a lambda, returned function, partial application, or higher-order argument;
- a local `let`, recursive binding, local match, or construction expression;
- a foreign call, dynamic test, reflection operation, or unchecked cast;
- an algebraic effect operation or handler;
- an implicitly selected trait method; and
- recursive or mutually recursive condition predicates.

The exclusion of local `let` is a version boundary, not a claim that immutable
bindings are inherently unsafe. It keeps normalization, evidence, and cost
accounting small enough to audit before widening the fragment.

## Evaluation

Evaluation is strict except for `and` and `or`, whose right operands are
conditional and evaluated left to right. Every admitted arithmetic and
comparison form terminates and returns normally for every value of its typed
operands. The language MUST NOT convert an invalid operation, exception, or
foreign fault into `false`; such an operation is rejected before BEAM
generation.

VM termination, resource exhaustion outside the declared compiler budget, and
compiler defects are not ordinary condition results.

## No body refinement

A successful condition does not change the Hindley–Milner type of a binding
or add a proposition to the body environment. The coverage checker may consume
verified truth facts to decide whether the set of clauses is complete, but
body typing uses only the structural pattern's bindings and type equalities.

## Connections (non-normative)

Reusable predicate and evidence rules are in
[Condition Predicates and Interfaces](condition-predicates-and-interfaces.md).
Clause evaluation order is fixed by
[Guard Tree Semantics](guard-tree-semantics.md).
