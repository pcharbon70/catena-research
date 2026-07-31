---
title: "Shallow Effect Handlers"
kind: source
created: "2026-07-31"
authors:
  - "Daniel Hillerström"
  - "Sam Lindley"
published: 2018
citation_key: "hillerstromLindley2018ShallowHandlers"
container: "Programming and Software Engineering, APLAS 2018, LNCS 11275: 415–435"
edition: null
isbn: "978-3-030-02767-4"
doi: "10.1007/978-3-030-02768-1_22"
url: "https://www.research.ed.ac.uk/en/publications/shallow-effect-handlers/"
accessed: "2026-07-31"
tags:
  - algebraic-effects
  - effect-handlers
  - resumptions
aliases:
  - "Deep versus shallow handlers"
---

# Shallow Effect Handlers

## Reference

Daniel Hillerström and Sam Lindley, “Shallow Effect Handlers,” in
*Programming and Software Engineering: APLAS 2018*, LNCS 11275, 415–435.
[DOI](https://doi.org/10.1007/978-3-030-02768-1_22),
[author manuscript](https://www.pure.ed.ac.uk/ws/portalfiles/portal/76099718/shallow_effect_handlers.pdf),
and [official bibliographic record](https://www.research.ed.ac.uk/en/publications/shallow-effect-handlers/).

## Research question

What is the formal and implementation-theoretic account of shallow handlers,
and how do they relate in expressive power to the traditional deep handlers
defined as folds over computation trees?

## Method

The paper defines shallow handlers as case splits rather than folds, develops
translations between deep and shallow handlers, supplies an abstract machine
and continuation-passing translation for shallow handling, and implements the
approaches in Links. The implementation evaluation specifically checks for
unwarranted memory retention.

## Findings

- A deep resumption automatically continues under the same handler; a shallow
  resumption exposes the remainder without reinstalling it.
- Deep handlers are naturally folds over computation trees, while shallow
  handlers are one-layer case analyses.
- Each form can simulate the other up to the paper's stated administrative
  reductions, so neither has a simple absolute expressiveness advantage.
- The forms differ substantially in programming structure. Shallow handlers
  directly support cases where the next continuation should be interpreted by
  a different handler, including stream-like and mutually recursive control
  patterns.
- The abstract machine and CPS translations provide concrete implementation
  accounts, and the evaluated Links implementations do not introduce the
  memory leaks the study was designed to detect.

## Relevance

This paper makes handler depth a first-class Catena design axis. The
simulation result supports choosing one small primitive initially, while the
programming differences warn against describing shallow handling as a mere
surface alias for deep handling.

## Limits

Simulation up to administrative reduction does not establish equal
performance, diagnostics, resource behavior, or ergonomics in a new language.
The empirical scope is Links and memory behavior for the presented
implementations, not a general benchmark of native runtimes.

## Derived work

- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
- [Algebraic Effects and Handlers map](../10-maps/algebraic-effects-and-handlers.md)
