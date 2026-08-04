---
title: "Effect Capabilities, Rows, and Selection"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.5"
tags:
  - algebraic-effects
  - effect-rows
  - specification
  - type-inference
aliases:
  - "Catena 0.5 capability rows"
---

# Effect Capabilities, Rows, and Selection

## Lexical capability identity

Each `handle` application creates a fresh lexical identity for one nominal
effect-family instantiation. Each named `uses` entry introduces an abstract
capability parameter. Alpha-renaming a binder preserves meaning; moving a
request across a binder or changing the selected identity may change meaning.

Selection is static. For an unqualified request the compiler filters visible
capabilities by nominal family, type arguments, and operation. Zero matches is
an unbound request. More than one is ambiguous and reports every candidate.
An explicit qualifier must resolve to exactly one compatible binder. Runtime
nesting order never repairs a failed static selection.

## Hybrid row equality

An effect row is unordered and may have an open tail. Its concrete projection
is a set of capability identities: the same capability requested repeatedly
coalesces. Its family projection is a multiset: two distinct capabilities for
the same nominal family remain two occurrences.

Consequently:

> **Normative definition.**

```text
{left: State[Int]} union {left: State[Int]} = {left: State[Int]}
{left: State[Int]} union {right: State[Int]}
  = {left: State[Int], right: State[Int]}
```

An abstract family occurrence without a fixed identity occupies one multiset
slot until unification selects or quantifies its capability. Normalization may
sort entries for stable output but MUST preserve distinct identities and
family multiplicity.

## Union, unification, and subtraction

Sequential evaluation unions rows in source order and then normalizes by the
equality above. Row unification aligns concrete identities first, aligns
remaining family-compatible abstract slots without collapsing multiplicity,
and unifies open tails with an occurs check. The solver must return a
most-general substitution for the supported rank-1 fragment or reject the
program.

Tail binder spelling is alpha-insensitive. A callee tail may be instantiated
by a differently named caller tail, and a closed inferred body may satisfy an
explicitly open declaration when every written capability occurrence is used.
Uniting two open tails creates one shared residual constraint; it does not make
their source-level names observable.

Handling subtracts exactly the freshly bound capability identity from the
handled expression's row. It does not subtract every occurrence of the family
and does not alter unrelated entries or the open tail. Effects performed by
handler arguments, the return clause, or operation clauses are unioned into
the result row under their outer capabilities.

## Scope and abstraction

A locally fresh capability MUST NOT appear in a public scheme, returned data,
stored closure, interface effect row, or other value escaping its `handle`.
Named `uses` capabilities may be quantified at module boundaries. An unnamed
family requirement cannot be used to intercept an effect introduced solely by
an effect-polymorphic callback; such authority requires a named capability in
the signature.

Version 0.5 admits closed effect-free function values as operation arguments
but no effect-polymorphic operation arguments. This narrow rule makes the
higher-order accidental-capture case unrepresentable in the initial request
surface while retaining ordinary predicates and pure transformations.

## Relationship to 0.1

This chapter refines the 0.1 duplicate-family rule: multiplicity belongs to
distinct or still-abstract capability slots, not to repeated requests through
one known identity. C077 remains unchanged—selection is lexical and handling
removes the statically selected occurrence.

## Connections (non-normative)

The identity and principality risks remain falsifiable questions in
[Which Algebraic-Effect Semantics Should Catena Adopt?](../../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md).
