---
title: "Which Combinators Should Catena Provide and Derive?"
kind: inquiry
created: "2026-08-01"
status: open
tags:
  - algebraic-data-types
  - category-theory
  - catena
  - combinator-libraries
  - language-design
aliases:
  - "Catena combinator inquiry"
  - "Which combinators belong in Catena?"
---

# Which Combinators Should Catena Provide and Derive?

## Why this matters

Combinators are the joints of a functional language: they determine which
program fragments can be assembled without exposing representation. A useful
joint can make laws, effects, dependency structure, or optimization
opportunities visible. A poorly specified one can hide evaluation order,
duplicate work, create incoherent instances, or burden ordinary programs with
an abstraction stronger than they need.

The question is therefore not how many familiar names Catena can collect. It
is whether a deliberately small primitive vocabulary, a larger derived
library, and conditional datatype generation can serve the agreed seventeen
categorical classes and ordinary algebraic datatypes without compromising
principal inference, coherent evidence, explicit effects, predictable cost,
or useful diagnostics.

## Operational question

Can Catena specify and implement a combinator system in which:

- the prelude supplies only universal function and product/sum routing;
- each categorical class has a minimal law-bearing dictionary and its
  conveniences are derived once in the standard library;
- `map`, `bimap`, constructor elimination, `fold_map`, and `traverse` are
  generated only when datatype variance, positivity, regularity, and field
  order justify them;
- categorical callbacks remain pure while effectful visits are represented by
  traversal, iterators, or explicit effect rows;
- class laws and operational guarantees are documented separately;
- order, callback multiplicity, short-circuiting, stack use, allocation,
  concurrency, and cancellation remain observable parts of the contract;
- parsers, optics, modular syntax, recursion schemes, and selective branching
  can grow as focused libraries rather than distort the core hierarchy; and
- compiler combinators remain an internal lowering choice with source-level
  debugging and semantics preserved?

## Working hypotheses

1. `identity`, `compose`, `curry`, `uncurry`, pairing, projections, and sum
   elimination are sufficient as the universal source-level layer; an `S`/`K`
   basis belongs only in compiler experiments.
2. Minimal class dictionaries plus one derived standard library improve
   coherence, law testing, documentation, and diagnostics over large
   instance-defined method sets.
3. A categorical `map` must receive a pure function. Ambiently effectful
   element visits should use `traverse`, an explicitly effectful operation, or
   a domain protocol so functor laws do not silently authorize effect changes.
4. Ordinary ADTs can derive constructor-complete eliminators and, when shape
   analysis succeeds, lawful `map`, `bimap`, `fold_map`, and `traverse` in the
   same typed core used for user programs.
5. A strict language needs an explicit `fold_while` or iterator protocol for
   early termination and stack-safe consumption; `Foldable` laws alone do not
   establish either property.
6. Applicative effect order, fold direction, choice policy, failure
   accumulation, backtracking, and callback multiplicity are operational
   commitments rather than consequences of algebraic laws.
7. Competing lawful behaviors should use named datatypes or wrappers—for
   example fail-fast `Result` and accumulating `Validation`—rather than
   competing implicit dictionaries for one type constructor.
8. Word names and qualified modules should be the default public notation;
   operators should be a small readability layer rather than the primary API.
9. Concrete generated lenses and prisms, explicit modular-syntax injections,
   and a concrete parser library should precede highly encoded generic APIs.
10. `Selective` is a useful experiment for statically inspectable conditional
    computations, but evidence does not yet justify adding it to the agreed
    initial class hierarchy.
11. Explicit computation values remain valuable for inspection and alternate
    interpretation even when ordinary control effects use native algebraic
    handlers.
12. Combinatory-logic and categorical intermediate representations should be
    evaluated as backend strategies independently of the source library.

## Paths to explore

### API inventory and corpus

- Build representative programs using `Option`, `Result`, validation, lists,
  trees, syntax, parsers, build graphs, remote queries, optics, and effectful
  resource processing.
- Record each repeated assembly pattern together with the weakest structure it
  needs; reject candidates that merely shorten one call site.
- Compare qualified words, methods, pipelines, and a small operator layer for
  readability, discovery, partial application, error locations, and teaching.
- Measure whether the proposed tiering keeps ordinary APIs concrete while
  allowing generic libraries to express their actual constraints.

### Formal laws and effect semantics

- State laws for every primitive class method and derived combinator in a
  typed core that distinguishes pure arrows, ambient effect rows, and explicit
  computation values.
- State parent-coherence laws: `Applicative` application must agree with
  `Apply`, monadic application with `Applicative`, and categorical operations
  inherited through the hierarchy.
- Define exactly which laws are observational when callbacks may diverge,
  allocate, raise effects, capture continuations, or inspect identity.
- Separate algebraic equality from order, multiplicity, discard, concurrency,
  cancellation, and resource-safety guarantees.

### Datatype derivation

- Implement variance, positivity, regularity, and parameter-role analysis over
  constructor payloads.
- Generate constructor eliminators for every ordinary ADT and derive
  categorical operations only for justified parameter occurrences.
- Publish constructor precedence, field order, constraints, effect order, and
  stack behavior in generated signatures and documentation.
- Check generated code in the normal typed core, retain its source provenance,
  and test both its laws and its agreement with user-written instances.
- Use rejected derivations to test whether diagnostics point to the precise
  negative, invariant, nested, or otherwise obstructing occurrence.

### Strict execution, iteration, and fusion

- Specify `fold_left`, `fold_right`, `fold_map`, `fold_while`, iterator pull,
  and any stream producer/consumer protocol independently.
- Test empty inputs, infinite or codata-like sources, early exit, callback
  counts, exceptions/effects, resource finalization, and cancellation.
- Compare direct matching, per-datatype loops, generic recursion schemes, and
  iterators for allocation, stack depth, fusion, code size, and diagnostics.
- Allow fusion only when purity, strictness, termination, and evaluation-order
  preconditions are established by the transformation.

### Focused domain prototypes

- Build a parser-combinator package with explicit input-consumption,
  commitment, progress, failure-merging, error-location, and backtracking
  semantics; compare it with a generated parser.
- Generate concrete lenses and prisms for ordinary products and sums, then
  compare them with a profunctor representation on mixed composition,
  specialization, compile time, and error messages.
- Prototype sums of functors and free syntax with explicit injection evidence,
  avoiding overlapping or incoherent instance search.
- Test selective branching on a build graph or remote-query DSL, recording
  which possible effects remain statically visible and which branches may be
  skipped dynamically.
- Test how explicit computation combinators and direct algebraic handlers
  interoperate without creating two unexplained effect semantics.

### Compiler representation

- Translate a restricted typed core to combinatory logic and separately to a
  categorical IR.
- Prove or differentially test translation correctness, including effects and
  evaluation order where supported.
- Compare code size, simplification opportunities, optimization proof burden,
  generated diagnostics, source maps, and backend performance with the
  ordinary typed representation.
- Do not expose backend combinator bases in source APIs unless a separate
  language-level use is demonstrated.

## Findings

The current synthesis is
[Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md).
The evidence so far supports these boundaries:

- [Hughes 1989](../30-sources/hughes-1989-why-functional-programming-matters.md)
  shows that higher-order and lazy glue can change program decomposition, but
  a strict Catena needs explicit iteration or streaming contracts rather than
  inheriting lazy producer/consumer behavior by analogy.
- [Böhm and Berarducci 1985](../30-sources/bohm-berarducci-1985-typed-lambda-programs.md)
  makes constructor elimination a semantic account of term algebras; it does
  not require function encodings to become Catena's runtime representation.
- [Meijer, Fokkinga, and Paterson 1991](../30-sources/meijer-et-al-1991-functional-programming-bananas.md)
  supports folds, unfolds, and fusion for positive recursive shapes while also
  making their preconditions more specific than an undifferentiated `fold`.
- [McBride and Paterson 2008](../30-sources/mcbride-paterson-2008-applicative-programming-effects.md),
  [Moggi 1991](../30-sources/moggi-1991-notions-computation-monads.md),
  and [Wadler 1995](../30-sources/wadler-1995-monads-functional-programming.md)
  distinguish independent effectful application from value-dependent
  sequencing; APIs should retain the weakest useful constraint.
- [Hutton and Meijer 1998](../30-sources/hutton-meijer-1998-monadic-parsing.md)
  demonstrates expressive parser assembly while leaving consumption,
  backtracking, errors, and efficiency as domain contracts that a modern
  package must specify.
- [Swierstra 2008](../30-sources/swierstra-2008-data-types-a-la-carte.md)
  demonstrates modular syntax from functor coproducts and folds, but its
  inferred injection mechanism is not a safe default for Catena's coherent
  initial trait system.
- [Mokhov et al. 2019](../30-sources/mokhov-et-al-2019-selective-applicative-functors.md)
  establishes a meaningful point between applicative and monadic dependency;
  it remains an experiment because the agreed initial hierarchy deliberately
  excludes it.
- [Turner 1979](../30-sources/turner-1979-applicative-language-implementation.md)
  and [Elliott 2017](../30-sources/elliott-2017-compiling-to-categories.md)
  support combinator-based lowering as compiler research, not as a reason to
  expose generated plumbing to programmers.

These findings justify a reference library and prototypes, not a frozen
surface API.

## Outcome

Open. Resolve the initial combinator system only when the archive contains:

1. exact primitive and derived signatures for the seventeen classes, with
   kind, purity, constraint, and parent-coherence rules;
2. an extensional and operational contract matrix covering laws, order,
   multiplicity, short-circuiting, allocation, stack use, concurrency, and
   cancellation;
3. a reference standard library generated from the minimal dictionaries and
   checked in the ordinary typed core;
4. conditional ADT derivation with diagnostics and generated-code law tests;
5. an iterator or `fold_while` design tested for strict evaluation, early
   termination, resource safety, and large structures;
6. a representative usage corpus and discoverability study for names,
   qualification, methods, pipelines, and any operators;
7. benchmarked parser, optic, modular-syntax, and selective prototypes with
   their domain-specific operational semantics written down;
8. interoperability tests between native algebraic effects, traversal,
   iterators, parsers, and explicit computations; and
9. an independent decision on whether a combinatory or categorical compiler
   IR improves the backend without degrading source behavior.

Evidence routes are collected in the
[Combinators for Algebraic Data and Categorical Programming map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md).
