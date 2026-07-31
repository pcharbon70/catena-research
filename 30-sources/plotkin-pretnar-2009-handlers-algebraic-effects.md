---
title: "Handlers of Algebraic Effects"
kind: source
created: "2026-07-31"
authors:
  - "Gordon Plotkin"
  - "Matija Pretnar"
published: 2009
citation_key: "plotkinPretnar2009Handlers"
container: "Programming Languages and Systems, ESOP 2009, LNCS 5502: 80–94"
edition: null
isbn: null
doi: "10.1007/978-3-642-00590-9_7"
url: "https://www.research.ed.ac.uk/en/publications/handlers-of-algebraic-effects/"
accessed: "2026-07-31"
tags:
  - algebraic-effects
  - denotational-semantics
  - effect-handlers
aliases:
  - "Plotkin and Pretnar on handlers"
---

# Handlers of Algebraic Effects

## Reference

Gordon Plotkin and Matija Pretnar, “Handlers of Algebraic Effects,” in
*Programming Languages and Systems: ESOP 2009*, LNCS 5502, 80–94.
[DOI](https://doi.org/10.1007/978-3-642-00590-9_7),
[author manuscript](https://www.pure.ed.ac.uk/ws/portalfiles/portal/17909848/Plotkin_Pretnar_2009_Handlers_of_Algebraic_Effects.pdf),
and [official bibliographic record](https://www.research.ed.ac.uk/en/publications/handlers-of-algebraic-effects/).

## Contribution

The paper gives handlers a general denotational account. An algebraic effect is
presented by operations and equations; a handler supplies an interpretation of
those operations in a model, and handling is the homomorphism induced from the
free model of the computation.

## Method

Plotkin and Pretnar develop a typed calculus with values and computations,
operation calls, handler values, and handling. They give a set-theoretic
semantics based on models of algebraic theories and relate the semantic
homomorphism to equations for handler execution. Examples include exceptions,
nondeterminism, state, I/O, and parameter passing.

## Findings

- A handler is not merely a map from operation names to callbacks. Its return
  clause and operation clauses define a model into which the handled free
  computation is interpreted.
- The unique homomorphism from a free model accounts for recursive handling of
  the continuation, providing the semantic foundation for what later
  operational literature calls a deep handler.
- Handler clauses can choose whether and how to use the operation continuation,
  which accounts for aborting exceptions, state threading, and branching
  nondeterminism in one framework.
- Common effects such as exceptions, nondeterminism, interactive I/O, and
  mutable state admit algebraic operations. Continuations remain a prominent
  effect outside the ordinary algebraic account.
- Equations matter: when an effect theory contains equations, a model of that
  theory and the induced homomorphism must respect them.

## Relevance

This is the conceptual basis for Catena's proposed deep handler. It explains
why the operation continuation is reinterpreted by the same handler and why a
handler may change the result domain of a computation. It also supports a
lawless free-signature starting point: allowing arbitrary handlers while
assuming undocumented equations would be inconsistent.

## Limits

The paper's core is not a complete modern language design. It does not settle
row-polymorphic inference, multiple instances, accidental higher-order capture,
one-shot implementation, scoped higher-order operations, or interactions with
linear resources. The semantic model supports handler meaning but leaves those
orthogonal choices to later work.

## Derived work

- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
- [Algebraic Effects and Handlers map](../10-maps/algebraic-effects-and-handlers.md)
