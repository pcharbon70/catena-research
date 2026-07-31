---
title: "Handlers in Action"
kind: source
created: "2026-07-31"
authors:
  - "Ohad Kammar"
  - "Sam Lindley"
  - "Nicolas Oury"
published: 2013
citation_key: "kammarLindleyOury2013Handlers"
container: "Proceedings of ICFP 2013: 145–158"
edition: null
isbn: null
doi: "10.1145/2500365.2500590"
url: "https://www.cs.ox.ac.uk/people/ohad.kammar/publications/kammar-lindley-oury-handlers-in-action.pdf"
accessed: "2026-07-31"
tags:
  - algebraic-effects
  - effect-handlers
  - effect-polymorphism
aliases:
  - "Kammar, Lindley, and Oury on handlers"
---

# Handlers in Action

## Reference

Ohad Kammar, Sam Lindley, and Nicolas Oury, “Handlers in Action,” in
*Proceedings of the 18th ACM SIGPLAN International Conference on Functional
Programming* (ICFP 2013), 145–158.
[DOI](https://doi.org/10.1145/2500365.2500590) and
[author manuscript](https://www.cs.ox.ac.uk/people/ohad.kammar/publications/kammar-lindley-oury-handlers-in-action.pdf).

## Research question

Can algebraic-effect handlers support modular, practical effect composition
across concrete programming settings, and what core operational account
explains that behavior?

## Method

The paper develops examples in a Haskell handler library, gives a simply typed
effect-handler calculus with operational semantics and type-safety arguments,
relates handlers to free monads and continuation encodings, and compares
several implementation approaches on example workloads.

## Findings

- Client computations can remain abstract over interpretation while handlers
  implement state, logging, nondeterminism, I/O, and other behaviors.
- Open handlers interpret a selected subset of operations and automatically
  forward all others. This is the key mechanism for modular partial
  interpretation.
- Handler order can change program meaning. A handler that consumes an
  operation can prevent an outer handler from observing it, while orthogonal
  handlers may commute for a particular program.
- The formal calculus gives operation clauses access to a delimited
  continuation and proves the expected progress and preservation properties
  for its simply typed setting.
- Open-handler types naturally invite effect polymorphism; the paper outlines
  row polymorphism as a smoother native account than its Haskell type-class
  encoding.
- Deep handlers correspond to folds over free computations. The paper also
  sketches shallow handlers by changing whether the resumption reinstalls the
  handler.
- The reported implementation comparison is highly representation-dependent:
  the continuation encoding performs far better than the free-monad variants
  on the paper's state benchmark under GHC.

## Relevance

This source grounds the synthesis's forwarding rule and its warning that
handler composition is not commutativity. It also supplies a bridge between
the abstract free-model account and practical libraries: an open effect row is
the type-level description of operations a handler forwards.

## Limits

The Haskell library relies on encodings and generated boilerplate that a native
language need not inherit. The core calculus is simply typed, and the paper
leaves a full row-polymorphic system to future work. Its small benchmarks do
not establish a general ranking among runtime strategies.

## Derived work

- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
- [Algebraic Effects and Handlers map](../10-maps/algebraic-effects-and-handlers.md)
