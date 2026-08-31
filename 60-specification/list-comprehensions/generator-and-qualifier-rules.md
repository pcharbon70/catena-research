---
title: "Generator and Qualifier Rules"
kind: specification
created: "2026-08-31"
status: normative
spec_version: "0.1.39"
tags:
  - comprehensions
  - generators
  - specification
aliases:
  - "Catena qualifier rules"
---

# Generator and Qualifier Rules

## Status and authority

This chapter is the normative Catena 0.1.39 generator, filter,
binding, and scope rule set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It executes C044's generator principle, C045's usefulness relation,
and C031's binding discipline.

The rules apply only to source-language revision `0.1.39`.

## Sources

> **Normative definition.**

A generator's source expression MUST have type `List A` for the
element type `A` the generator pattern matches (`LC-OBL-003`).
Iterators, streams, effectful producers, and generic foldable
sources are excluded from this revision; each requires its own
slice (`LC-OBL-003`). A source of any other type is a typing error.

## Traversal

> **Normative definition.**

Multiple generators compose left-to-right, depth-first
(`LC-OBL-004`): the leftmost source is visited first and, per
element, every later qualifier runs to completion before the next
element of that source. Later generator sources MAY depend on
earlier qualifier bindings. Each source expression is evaluated
exactly once per visit of its enclosing qualifier prefix; an empty
input at any depth yields no elements from that subtree
(`LC-OBL-004`). The result order is this traversal's order.

## Filters

> **Normative definition.**

A `when` filter evaluates its `Bool` expression once per reaching
(`LC-OBL-005`): `false` skips the element and `true` continues. The
filter's effects are visible in the comprehension's effect row and
occur in traversal order. Every failure other than the `false`
value — type mismatches aside, any trap or effect failure —
propagates and abandons the comprehension (`LC-OBL-005`).
Comprehension filters are ordinary effect-typed Boolean
expressions; they are not clause guards and MUST NOT use C003's
guard fragment (`LC-OBL-005`).

## The pattern-generator split

> **Normative definition.**

An ordinary generator's pattern is checked total for the element
type by the C045 usefulness relation; a missing witness is the
non-exhaustive-match diagnostic (`M001` family) at the generator
(`LC-OBL-006`). A `case` generator's pattern may be refutable: a
mismatch alone skips that element, exactly the explicit-failure
class C044 reserved (`LC-OBL-006`). A filtering marker whose
pattern can match nothing is static invalidity (`LCP002`), and a
filtering marker on an already-total pattern is the
`LCP003` advisory (`LC-OBL-006`).

## Scope and rebinding

> **Normative definition.**

Qualifier bindings are visible left-to-right: a qualifier sees
every earlier qualifier's bindings and no later one's
(`LC-OBL-007`). Bindings are non-recursive and do not escape the
comprehension. Rebinding a name introduced in the same
comprehension is static invalidity (`LCP001`) (`LC-OBL-007`).
Shadowing an outer name follows the language's ordinary shadowing
rule. A binding unused by later qualifiers or the yield expression
reports the unused-binding advisory of the binding discipline
(`BS001` family) (`LC-OBL-007`).

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/list-comprehensions.md) grounds the
traversal in the Haskell report's nested depth-first translation,
the explicit filtering marker in EEP 70's silent-data-loss
evidence, and the scope rules in Erlang's fresh-binding hazards.
The map/flatten algebra and its insufficiency for filtering are
recorded there from Wadler's comprehending-monads evidence.
