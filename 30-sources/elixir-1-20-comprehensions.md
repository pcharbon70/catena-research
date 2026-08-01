---
title: "Elixir 1.20 Comprehensions"
kind: source
created: "2026-08-01"
published: null
citation_key: null
container: "Elixir Documentation"
edition: "1.20.2"
isbn: null
doi: null
url: "https://elixir.hexdocs.pm/comprehensions.html"
accessed: "2026-08-01"
tags:
  - comprehensions
  - functional-programming
  - language-design
aliases:
  - "Elixir for comprehensions"
---

# Elixir 1.20 Comprehensions

## Reference

Elixir, “Comprehensions,” *Elixir Documentation*, version 1.20.2, accessed
2026-08-01.
[Official documentation](https://elixir.hexdocs.pm/comprehensions.html).

## Research question

How does a widely used BEAM language combine enumeration, pattern filtering,
arbitrary filters, result collection, and effects in one comprehension form?

## Method

The documentation defines the user-facing behavior of the `for` special form
through executable examples over ranges, enumerables, bit strings, maps, and
streams. It is a language guide rather than a formal operational semantics.

## Findings

- A comprehension combines generators, filters, and a result expression. More
  than one generator is evaluated as a nested Cartesian traversal.
- The right side of a regular generator can be any value implementing
  `Enumerable`, not only a list.
- A refutable generator pattern is also a filter: source values that do not
  match are silently ignored.
- Filters use Elixir truthiness. Only `false` and `nil` reject a candidate;
  they are not statically Boolean expressions.
- Qualifiers may contain ordinary assignments and ordinary function calls.
  The examples perform filesystem I/O, making evaluation order and callback
  multiplicity observable.
- Bindings created inside a comprehension do not escape it.
- Bit-string generators can be combined with enumerable generators.
- Results default to lists, but an `into` option can target values implementing
  `Collectable`, including maps, binaries, sets, and streams.
- A stream may be both the input and output, showing that a generic collector
  form can express open-ended effectful processing rather than merely build a
  finite list.

## Relevance

Elixir is the closest ergonomic BEAM comparison. It demonstrates the practical
reach of one compact form, but also shows how quickly list comprehension grows
into a generic iteration-and-collection language. Catena can keep the familiar
`for`/`yield` shape while initially fixing the source and result to eager lists,
using typed Boolean filters, making refutable pattern filtering explicit, and
recording all effects in the comprehension's inferred row.

The examples also show why a Catena comprehension must specify when an inner
source is reevaluated and how often filesystem or other effectful operations
run.

## Limits

The guide is explanatory rather than normative and does not provide a formal
translation, inference rules, or optimizer constraints. Elixir is dynamically
typed, treats truthiness and pattern mismatch differently from Catena's
proposed typed failure model, and does not separate pure categorical `map`
from effectful iteration.

## Derived work

- [List Comprehensions](../20-notes/list-comprehensions.md)
- [How Should Catena Specify List Comprehensions?](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
- [List Comprehensions map](../10-maps/list-comprehensions.md)
