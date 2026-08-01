---
title: "Scala 3.4 For Comprehensions"
kind: source
created: "2026-08-01"
published: null
citation_key: null
container: "Scala 3 Language Specification"
edition: "3.4"
isbn: null
doi: null
url: "https://scala-lang.org/files/archive/spec/3.4/06-expressions.html#for-comprehensions-and-for-loops"
accessed: "2026-08-01"
tags:
  - comprehensions
  - language-design
  - pattern-matching
aliases:
  - "Scala for comprehensions"
---

# Scala 3.4 For Comprehensions

## Reference

Scala, “For Comprehensions and For Loops,” *Scala 3 Language Specification*,
version 3.4, chapter 6.
[Official specification](https://scala-lang.org/files/archive/spec/3.4/06-expressions.html#for-comprehensions-and-for-loops).

## Research question

What does Catena gain and risk by translating a comprehension through methods
provided by the generator's carrier type?

## Method

The specification gives grammar and stepwise translations for generators,
conditional generators, guards, value definitions, result-producing
comprehensions, and result-discarding loops.

## Findings

- A result-producing `for ... yield` and a result-discarding `for` loop share
  the same qualifier grammar but translate differently.
- A plain generator requires an irrefutable pattern. Prefixing the generator
  with `case` explicitly requests filtering by a refutable pattern.
- Qualifiers proceed left to right and may include later generators, Boolean
  guards, and value definitions.
- The translation uses carrier-provided `map`, `flatMap`, `withFilter`, and
  `foreach` methods. A single generator plus `yield` maps; remaining qualifiers
  introduce nested `flatMap`; a following guard uses `withFilter`.
- Because those methods belong to the carrier, the same surface form can
  produce different types and operational behavior for arrays and other
  structures.
- Value definitions require additional translation machinery to retain earlier
  bindings, including generated tuples in the specified scheme.
- The specification makes refutable pattern filtering visible at the surface,
  avoiding the older surprise that an apparently ordinary generator silently
  discards elements.

## Relevance

Scala provides the strongest precedent for Catena's proposed distinction
between a total generator and an explicitly filtering generator. The `case`
marker reuses pattern vocabulary and lets the type checker reject unintended
partial input claims.

Its method-driven translation is a warning for Catena. Catena's `map` is
intended to remain pure, and its category-inspired traits do not by themselves
fix evaluation order, strictness, filtering failure, or output representation.
A list comprehension should therefore elaborate to a dedicated semantic form;
pure extensional equivalences with `map` and `flat_map` can remain available
without making public trait dispatch its definition.

## Limits

The cited edition is Scala 3.4; later Scala releases continue to revise
comprehension desugaring. Scala's method selection, subtyping, overloading, and
effect model differ substantially from Catena's proposed HM core and explicit
effect rows. The specification defines translation, not cross-carrier
lawfulness or performance.

## Derived work

- [List Comprehensions](../20-notes/list-comprehensions.md)
- [How Should Catena Specify List Comprehensions?](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
- [List Comprehensions map](../10-maps/list-comprehensions.md)
