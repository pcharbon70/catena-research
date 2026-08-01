---
title: "List Comprehensions"
kind: map
created: "2026-08-01"
tags:
  - comprehensions
  - language-design
  - program-semantics
aliases:
  - "List comprehension research map"
---

# List Comprehensions

## Scope

This map connects comprehension syntax to the semantic decisions it can hide:
generator pattern failure, nested and lockstep traversal, filters, lexical
bindings, effects, collection targets, desugaring, cost, and BEAM lowering.

The initial Catena question is intentionally narrower than “what can
comprehension notation express?” It asks which list-building form ordinary
programmers can predict without learning mathematical vocabulary or
carrier-specific method conventions.

## Start here

1. [List Comprehensions](../20-notes/list-comprehensions.md) gives the
   comparative synthesis and proposes an eager list-to-list form with total
   generators, explicit filtering patterns, typed Boolean filters, visible
   effects, and dedicated lowering.
2. [How Should Catena Specify List Comprehensions?](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
   turns the remaining syntax, usability, formal, backend, and extension
   questions into resolution criteria.
3. The temporary
   [language-specification checklist](../00-inbox/language-specification-completeness-checklist.md#6-list-comprehensions-generators-and-iteration)
   shows where this deep dive fits within the broader path to a complete
   language reference.

## Trails

### A small list-specific kernel

1. The [Haskell 2010 report](../30-sources/marlow-2010-haskell-language-report.md)
   specifies generator, local declaration, Boolean filter, scope, pattern
   skipping, and `concatMap` translation for lists.
2. [Comprehending Monads](../30-sources/wadler-1992-comprehending-monads.md)
   derives the generator equations from `map`, `unit`, and `join`, then shows
   that filters require an additional zero operation.
3. The [Catena combinator synthesis](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
   separates pure mapping, dependent sequencing, effectful traversal, folds,
   and zip policies. This prevents comprehension syntax from erasing their
   operational differences.

This trail supports pure list equations but not generic `Monad` syntax or
effect-reordering optimizations.

### Pattern mismatch is a design choice

1. [EEP 70](../30-sources/erlang-eep-70-strict-and-relaxed-generators.md)
   documents why silent generator mismatch can hide malformed input and adds
   strict punctuation to an established language.
2. The [Scala 3.4 specification](../30-sources/scala-3-4-for-comprehensions.md)
   instead requires plain generator patterns to be irrefutable and marks
   filtering patterns with `case`.
3. [Algebraic Data Types](../20-notes/algebraic-data-types.md) supplies
   Catena's coverage, usefulness, abstraction, and witness machinery.

This trail supports total ordinary generators plus a visibly requested
filtering generator.

### The BEAM comparison

1. The current [Erlang expression reference](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
   combines list, binary, and map sources and targets with strict, relaxed,
   nested, zip, and two filter-failure regimes.
2. [EEP 73](../30-sources/erlang-eep-73-zip-generators.md) makes lockstep
   length, pattern, error, and allocation policies explicit.
3. [Elixir 1.20](../30-sources/elixir-1-20-comprehensions.md) shows the
   ergonomics and semantic breadth of arbitrary enumerables, effectful
   qualifiers, pattern skipping, and generic collectors.

These sources establish feasibility on the runtime. They do not require Catena
to inherit dynamic truthiness, silent patterns, symbolic strictness, or generic
collection targets.

### Scope expansion and query syntax

1. [Comprehensive Comprehensions](../30-sources/peyton-jones-wadler-2007-comprehensive-comprehensions.md)
   adds zip, grouping, ordering, limiting, and general transformations with
   formal typing and translation.
2. Its grouping rules can change the types of all bindings in scope, showing
   why query qualifiers are not harmless extensions to a list loop.
3. The [Catena synthesis](../20-notes/list-comprehensions.md#result-shape-and-neighboring-features)
   routes maps, sets, binaries, streams, zip, reduction, parallelism, and query
   operations to independent contracts.

### Effects and guards

1. [Clause Guards](../20-notes/clause-guards.md) requires effect-free, total
   conditions because false participates in clause selection and selective
   receive.
2. [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
   makes effects lexical and type-visible, which permits a repeated
   comprehension operation to remain explicit without calling it pure.
3. The [list-comprehension effect contract](../20-notes/list-comprehensions.md#effects-are-allowed-but-not-hidden)
   fixes source-order traces and refuses to redefine categorical `map`.

This trail explains why clause guards and comprehension filters may share a
Boolean surface without sharing a safety judgment.

## Proposed decision route

1. Validate a result-producing `for ... yield` grammar against Catena's full
   expression syntax.
2. Compare `case`, `matching`, and other explicit filtering-pattern markers.
3. Formalize total generators, filtering generators, filters, bindings, scope,
   types, effects, and dynamic order in a typed qualifier tree.
4. Implement a reference evaluator and tail-recursive BEAM worker lowering.
5. Differentially test values, failures, effects, and source traces.
6. Measure whether explicit list operations handle zip, streams, builders, and
   reduction before allocating syntax to them.

## Open questions

- Should filters permit all ordinary effects initially, or should some
  qualifiers have a narrower effect boundary?
- Is a local binding qualifier clearer than an ordinary nested `let`?
- How should outer-name shadowing behave inside a generator?
- Can comprehension and guard IR share infrastructure without sharing safety
  or failure semantics?
- Which source-level cost explanation best communicates Cartesian growth?
- What evidence would justify iterator, stream, zip, binary, builder,
  reduction, query, or parallel extensions?
