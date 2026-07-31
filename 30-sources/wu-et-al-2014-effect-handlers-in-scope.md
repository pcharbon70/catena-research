---
title: "Effect Handlers in Scope"
kind: source
created: "2026-07-31"
authors:
  - "Nicolas Wu"
  - "Tom Schrijvers"
  - "Ralf Hinze"
published: 2014
citation_key: "wuSchrijversHinze2014Scope"
container: "Proceedings of the 2014 ACM SIGPLAN Symposium on Haskell: 1–12"
edition: null
isbn: null
doi: "10.1145/2633357.2633358"
url: "https://research-information.bris.ac.uk/en/publications/effect-handlers-in-scope/"
accessed: "2026-07-31"
tags:
  - algebraic-effects
  - effect-handlers
  - scoped-effects
aliases:
  - "Scoped effect handlers"
---

# Effect Handlers in Scope

## Reference

Nicolas Wu, Tom Schrijvers, and Ralf Hinze, “Effect Handlers in Scope,” in
*Proceedings of the 2014 ACM SIGPLAN Symposium on Haskell*, 1–12.
[DOI](https://doi.org/10.1145/2633357.2633358),
[author manuscript](https://people.cs.kuleuven.be/~tom.schrijvers/Research/papers/haskell2014.pdf),
and [official bibliographic record](https://research-information.bris.ac.uk/en/publications/effect-handlers-in-scope/).

## Research question

How can handlers model operations whose meaning scopes over a
subcomputation—such as exception handling, nondeterministic pruning, or
threading—when ordinary algebraic signatures are first order?

## Method

The authors examine examples that expose scoping failures in conventional
free-monad encodings. They compare a first-order representation with explicit
syntax delimiters against a higher-order representation in which operation
constructors can contain genuine program arguments, and develop handler
encodings for the latter.

## Findings

- Ordinary first-order operations can carry values but cannot directly expose
  the syntax or structure of a scoped subcomputation to a handler.
- Adding first-order begin/end delimiter operations is insufficient in general,
  especially when operations themselves accept computations.
- A higher-order syntax representation gives scoped operations genuine program
  arguments and lets handlers interpret their nested computations.
- The distinction appears in practical cases including pruning a
  nondeterministic search, dynamically scoped exception handling, and
  multithreading constructs.
- Scoped effects are therefore not just ordinary operations with cosmetic
  block syntax; their signatures and folds have additional structure.

## Relevance

The paper is direct evidence against presenting Catena's first-order algebraic
effects as a universal account of `local`, `catch`, `bracket`, timeouts, or
structured concurrency. It motivates reserving a separate scoped or
higher-order mechanism and specifying its resumption and cleanup laws
independently.

## Limits

The work is expressed through Haskell embeddings and does not provide Catena's
desired row-polymorphic inference, native operational semantics, lexical effect
instances, or resource-safe cancellation protocol. It establishes the
representational gap, not one mandatory surface design for closing it.

## Derived work

- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
- [Algebraic Effects and Handlers map](../10-maps/algebraic-effects-and-handlers.md)
