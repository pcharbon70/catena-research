---
title: "How Should Catena Specify List Comprehensions?"
kind: inquiry
created: "2026-08-01"
status: open
tags:
  - catena
  - comprehensions
  - language-design
aliases:
  - "Catena list comprehension design"
---

# How Should Catena Specify List Comprehensions?

## Why this matters

A list comprehension appears to be compact collection syntax, but it fixes a
large operational boundary. Its meaning includes pattern failure, nested
traversal, binding scope, effect repetition, output order, failure timing,
allocation, and the relationship between language syntax and categorical
operations.

Catena's architecture makes these choices unusually consequential:

- algebraic data patterns are exhaustive by default;
- clause guards use a total effect-free fragment;
- ordinary effects remain visible in type rows;
- categorical `map` remains pure and law-bearing;
- the BEAM rewards tail-recursive fused list loops; and
- approachable syntax should not require programmers to infer semantics from
  monad vocabulary or punctuation.

The [synthesis](../20-notes/list-comprehensions.md) proposes a narrow initial
contract. This inquiry remains open because the exact surface, effect boundary,
binding qualifier, and evidence for later generalization still need testing.

## Operational question

Can one list-comprehension design let programmers correctly predict:

1. source and result types;
2. nested versus lockstep traversal;
3. total versus intentionally filtering patterns;
4. left-to-right scope and evaluation;
5. the count and order of effects;
6. failure propagation and partial effects;
7. result order and cardinality; and
8. BEAM cost;

without learning category-theory terminology or inspecting generated
`map`/`flat_map` calls?

The design is ready to stabilize only when it has:

- a grammar integrated with the complete expression syntax;
- declarative typing and effect rules;
- a small-step or executable dynamic account;
- a typed qualifier-tree elaboration;
- coverage and scope diagnostics;
- a reference evaluator and BEAM differential suite;
- representative usability evidence; and
- benchmark evidence for allocation and stack behavior.

## Working hypotheses

1. **Lists should be the only initial source and result carrier.** One concrete
   shape gives the feature a stable order, emptiness, builder, and failure
   contract.
2. **Ordinary generator patterns should be total.** An unintended partial
   pattern should be a compile error rather than data loss or a runtime match
   failure.
3. **Refutable filtering should be explicit.** A word-level marker such as
   `case` will communicate intent more reliably than a punctuation change.
4. **Filters should be typed `Bool`, not truthy values.** Non-Boolean results
   are static errors and ordinary failures propagate.
5. **Comprehension filters need not be clause guard-safe.** Effect rows and an
   exact execution order can make repeated effects visible without conflating
   filtering with coverage or selective receive.
6. **Multiple generators should be nested and depth-first.** Zip remains an
   explicit `zip_exact` or `zip_shortest` operation until dedicated syntax
   proves necessary.
7. **The semantic target should be a typed qualifier tree.** Pure equations
   with `map` and `flat_map` aid reasoning, but open trait dispatch should not
   define execution.
8. **The backend should fuse into tail-recursive workers.** A reversed
   accumulator plus one final reverse should preserve order without
   intermediate mapped and filtered lists.
9. **Generic monad comprehensions should be deferred.** Monad structure does
   not supply filtering zero, evaluation order, effect multiplicity, or output
   policy.
10. **Streams, binaries, maps, reduction, and parallel traversal need separate
    contracts.** Adding them as options would obscure resource and failure
    boundaries.

## Paths to explore

### Surface comprehension studies

Compare at least these schematic forms with programmers who do not know
Haskell or Scala:

```text
for
  item in items
  when item.active
yield item.name
```

```text
collect item.name
from item in items
when item.active
```

```text
[item.name | item in items, item.active]
```

Measure:

- time to identify source and result;
- predicted order and cardinality;
- predicted effect count;
- interpretation of pattern mismatch;
- confusion with imperative loops; and
- repair success after a compiler diagnostic.

### Pattern-intent study

Test ordinary and explicitly filtering patterns over `Option`, `Result`, and
sum types:

```text
Some(value) in values
case Some(value) in values
matching Some(value) in values
```

Determine whether `case`, `matching`, or another task word best communicates
“skip nonmatching elements” and whether users understand the total-pattern
error.

### Effect study

Construct programs with effects in:

- the outer source;
- a dependent inner source;
- a local binding;
- a filter;
- the result expression; and
- failure after earlier effects.

Ask users to predict the trace, then compare pure-only, fully effectful, and
restricted-filter variants. Record whether displayed effect rows plus
multiplicity diagnostics are sufficient.

### Formal model

Define a typed qualifier tree with:

```text
EachTotal
EachCase
Keep
BindTotal
Yield
```

Prove or test:

- type preservation through elaboration;
- lexical scope preservation;
- total-generator match success;
- filtering mismatch as the only implicit skip;
- order and effect-trace preservation;
- equivalence of the pure subset with list `map`, filtering, and `flat_map`;
  and
- semantic preservation of the fused worker lowering.

### Backend experiments

Compare:

1. a qualifier-tree reference interpreter;
2. direct recursive source code;
3. calls to list library operations;
4. fused private workers with reversed accumulation; and
5. native-compatible Erlang/Core Erlang comprehension lowering where safe.

Measure runtime, allocation, reductions, code size, compile time, stack use,
failure traces, and source debugging on empty, long, highly filtered, and
Cartesian inputs.

### Extension pressure

Gather real examples before adding:

- exact or shortest zip qualifiers;
- iterators and lazy streams;
- binary parsing and construction;
- map or set result builders;
- reduction and early termination;
- sorting, grouping, and uniqueness;
- effect-only loops; and
- structured parallel traversal.

For each request, record whether an explicit library operation is clearer and
whether syntax would avoid a measured allocation or diagnostic problem.

## Findings

### Primary language evidence

- The [Haskell report](../30-sources/marlow-2010-haskell-language-report.md)
  gives list comprehensions a nested depth-first translation through
  `concatMap`, with silent generator-pattern skipping and separate local
  declarations.
- The [Erlang reference](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
  demonstrates list, binary, and map targets; strict and relaxed patterns;
  nested and zip traversal; and filter failure tied to syntactic class.
- [EEP 70](../30-sources/erlang-eep-70-strict-and-relaxed-generators.md)
  documents silent data loss as sufficient motivation for an explicit strict
  form in a production language.
- [EEP 73](../30-sources/erlang-eep-73-zip-generators.md) demonstrates that
  lockstep traversal adds length, pattern, evaluation, precedence, diagnostic,
  and allocation decisions.
- [Elixir](../30-sources/elixir-1-20-comprehensions.md) demonstrates the
  convenience and breadth of a generic effectful `Enumerable`/`Collectable`
  form on the BEAM.
- [Scala](../30-sources/scala-3-4-for-comprehensions.md) demonstrates an
  explicit `case` marker for refutable filtering and carrier-provided
  `map`/`flatMap`/`withFilter` translation.

### Formal evidence

- [Wadler](../30-sources/wadler-1992-comprehending-monads.md) shows that
  dependent generator composition has a monadic account but Boolean filtering
  needs an additional zero operation and laws.
- [Peyton Jones and Wadler](../30-sources/peyton-jones-wadler-2007-comprehensive-comprehensions.md)
  show that grouping, ordering, zip, and arbitrary transformations can be
  formalized, while also changing qualifier scope and binder types.

### Current inference

The evidence favors a concrete list feature over a generic abstraction
surface. It also favors separating total and filtering patterns at the source
level. These are cross-source inferences, not conclusions established by any
one comparison language.

## Resolution criteria

Resolve this inquiry only after:

- syntax tests identify a comprehension form and explicit pattern-filter marker
  that users interpret reliably;
- the type/effect calculus and qualifier-tree elaboration are written;
- coverage produces useful total-pattern errors and filtering-pattern
  diagnostics;
- reference and BEAM implementations agree on values, failures, and effects;
- generated loops are stack-safe and allocate linearly in output size;
- diagnostics preserve source qualifiers instead of generated combinator
  frames; and
- the initial exclusion of generic carriers, zip, streams, binaries, builders,
  reduction, and parallelism is recorded in the language reference.

## Outcome

Open. The current provisional direction is an eager list-to-list `for ...
yield` expression with total generators, explicitly filtering `case`
generators, typed Boolean filters, exhaustive local bindings, visible effects,
and depth-first left-to-right execution. Exact syntax and the initial effect
boundary require validation.

The evidence route is curated in the
[List Comprehensions map](../10-maps/list-comprehensions.md).
