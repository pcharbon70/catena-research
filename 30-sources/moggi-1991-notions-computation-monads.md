---
title: "Notions of Computation and Monads"
kind: source
created: "2026-07-31"
authors:
  - "Eugenio Moggi"
published: 1991
citation_key: "moggi1991NotionsComputation"
container: "Information and Computation 93(1): 55–92"
edition: null
isbn: null
doi: "10.1016/0890-5401(91)90052-4"
url: "https://person.dibris.unige.it/moggi-eugenio/ftp/ic91.pdf"
accessed: "2026-07-31"
tags:
  - category-theory
  - denotational-semantics
  - effects
  - monads
aliases:
  - "Moggi on computational monads"
---

# Notions of Computation and Monads

## Reference

Eugenio Moggi, “Notions of Computation and Monads,” *Information and
Computation* 93, no. 1 (1991): 55–92.
[DOI](https://doi.org/10.1016/0890-5401(91)90052-4),
[author manuscript](https://person.dibris.unige.it/moggi-eugenio/ftp/ic91.pdf),
and [author publication index](https://person.dibris.unige.it/moggi-eugenio/publications.html).

## Research question

How can equational reasoning distinguish values from computations while
remaining general across partiality, nondeterminism, state, exceptions,
continuations, and interactive behavior?

## Method

Moggi gives a categorical semantics and associated calculi. A type `A`
denotes values, while `T A` denotes computations that may produce `A`. A
Kleisli triple—equivalently, under the stated conditions, a monad—provides the
unit that embeds values and the extension operation that sequences
computations. The paper instantiates the structure for several notions of
computation and studies soundness and completeness properties.

## Findings

- Ordinary beta-eta equality treats programs as total functions from values
  to values and is unsound as a universal model of effectful computation.
- Separating `A` from `T A` makes the computational behavior explicit in the
  semantics.
- Kleisli composition gives typed sequencing: the output computation of one
  program feeds the next while preserving the chosen notion of computation.
- One interface can model several effects, but each model has its own
  equations. The word *monad* names the shared composition structure, not one
  universal operational behavior.
- Strength is required to combine ordinary values with computations in the
  higher-order language modeled by the paper.

## Relevance

This is the semantic reason Catena should distinguish pure results from
effectful computations. It also corrects two common design shortcuts: a monad
is not merely a container with `flatMap`, and adopting monadic syntax does not
settle which effects exist or how they execute.

Catena's proposed algebraic handlers may be more direct for native effects,
but monads remain useful for explicit computation descriptions, embedded
languages, parsers, transactional plans, and alternative semantics.

## Limits

The paper supplies semantic calculi, not a modern surface language, inference
algorithm, optimizer, or performance comparison. A single monad does not
automatically compose independently chosen effects, and the framework does
not erase operational questions such as evaluation order, resource lifetime,
or cancellation.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
- [Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
- [Combinators research map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md)
