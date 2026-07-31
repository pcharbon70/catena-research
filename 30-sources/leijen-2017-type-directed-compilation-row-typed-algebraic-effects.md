---
title: "Type Directed Compilation of Row-Typed Algebraic Effects"
kind: source
created: "2026-07-31"
authors:
  - "Daan Leijen"
published: 2017
citation_key: "leijen2017TypeDirectedEffects"
container: "Proceedings of POPL 2017: 486–499"
edition: null
isbn: null
doi: "10.1145/3009837.3009872"
url: "https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/algeff.pdf"
accessed: "2026-07-31"
tags:
  - algebraic-effects
  - compilers
  - effect-rows
aliases:
  - "Koka selective CPS compilation"
---

# Type Directed Compilation of Row-Typed Algebraic Effects

## Reference

Daan Leijen, “Type Directed Compilation of Row-Typed Algebraic Effects,” in
*Proceedings of the 44th ACM SIGPLAN Symposium on Principles of Programming
Languages* (POPL 2017), 486–499.
[DOI](https://doi.org/10.1145/3009837.3009872),
[author manuscript](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/algeff.pdf),
and [Microsoft Research record](https://www.microsoft.com/en-us/research/?p=337556).

## Contribution

The paper presents an end-to-end account of algebraic effects in Koka:
row-polymorphic type inference, a direct operational semantics, an explicitly
typed core, and a type-directed selective continuation-passing translation for
ordinary target platforms.

## Method

Leijen defines a formal source calculus and effect-row inference algorithm,
gives a direct operational semantics for handlers, elaborates into an annotated
System F-like core, and defines a selective CPS translation. The implementation
uses inferred effects to decide where a continuation calling convention is
required and treats polymorphic effect variables specially.

## Findings

- Row-typed algebraic effects can be integrated with ML-shaped inference while
  retaining a direct-style source semantics.
- Type information can drive selective CPS: functions whose types cannot
  perform handled effects keep their ordinary calling convention.
- A standard monomorphic selective CPS translation is insufficient when an
  effect variable may later be instantiated with either a handled or an
  unhandled effect.
- Koka addresses that representation uncertainty with duplicated polymorphic
  code paths that select the appropriate runtime representation.
- Effect-type simplification has compilation consequences as well as prettier
  types. In the reported Koka core library, simplification reduced the set of
  CPS-translated functions by more than 80%.
- The explicitly typed core makes inferred effects and handler identities
  available to the backend rather than asking runtime stack search to recover
  every decision.

## Relevance

This is direct evidence for a portable Catena implementation route. It also
shows that effect polymorphism is not just a front-end concern: open row
variables can force calling-convention choices or code duplication. The typed
core proposed for Catena should therefore preserve effect evidence needed by
the backend.

## Limits

The quantitative result concerns one compiler and core library and is not a
general performance guarantee. Selective CPS changes code size and calling
conventions, and the paper's solution to polymorphic representation is one
point in a larger design space. A Catena calculus with lexical instances and
affine resumptions would require a new correctness argument.

## Derived work

- [Algebraic Effects and Handlers](../20-notes/algebraic-effects-and-handlers.md)
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
- [Which Algebraic-Effect Semantics Should Catena Adopt?](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
- [Algebraic Effects and Handlers map](../10-maps/algebraic-effects-and-handlers.md)
