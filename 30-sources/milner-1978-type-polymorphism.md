---
title: "A Theory of Type Polymorphism in Programming"
kind: source
created: "2026-07-31"
authors:
  - "Robin Milner"
published: 1978
citation_key: "milner1978TypePolymorphism"
container: "Journal of Computer and System Sciences 17(3): 348–375"
edition: null
isbn: null
doi: "10.1016/0022-0000(78)90014-4"
url: "https://www.sciencedirect.com/science/article/pii/0022000078900144"
accessed: "2026-07-31"
tags:
  - algorithm-w
  - hindley-milner
  - let-polymorphism
  - type-inference
aliases:
  - "Milner 1978"
---

# A Theory of Type Polymorphism in Programming

## Reference

Robin Milner, “A Theory of Type Polymorphism in Programming,” *Journal of
Computer and System Sciences* 17, no. 3 (1978), 348–375.
[DOI and journal record](https://doi.org/10.1016/0022-0000(78)90014-4).

## Contribution

Milner presents an implicitly typed polymorphic discipline for a small
functional language and a compile-time inference procedure, Algorithm W. The
paper's practical aim is to retain the flexibility of parametric polymorphism
while rejecting operations that would go wrong because of type misuse.

## Method

The paper gives a denotational semantics, a formal notion of a well-typed
program, and two inference procedures. The applicative Algorithm W threads a
substitution through a syntax-directed traversal; the more imperative
Algorithm J is presented as an implementation-oriented alternative. Milner
proves semantic soundness of the typing discipline and syntactic soundness of
W.

## Findings

- Type information can be inferred at compile time, without runtime type tags
  and without requiring type annotations on many nontrivial programs.
- A use of a `let`-bound identifier replaces its generic variables with fresh
  variables. Lambda- and fix-bound identifiers retain nongeneric variables.
- Application infers both sides, introduces a fresh result variable, and asks
  unification to make the function type agree with `argument -> result`.
- W must return a substitution as well as a type because constraints discovered
  inside a subexpression can refine nongeneric variables in the surrounding
  environment.
- The paper proves that W only produces derivable typings. The stronger proof
  that W finds a principal type whenever one exists is supplied by later
  Damas–Milner work.

## Relevance

This is the direct algorithmic foundation for a greenfield inference core. Its
substitution-threading discipline is the standard against which environment
application, generalization boundaries, and any effect-aware extension should
be specified and tested.

## Limits

The core language is deliberately small. It does not cover trait predicates,
higher-kinded constructors, row polymorphism, effect handlers, modern module
systems, or high-quality diagnostic recovery. Milner explicitly separates
parametric polymorphism from ad-hoc overloading.

## Derived work

- [Hindley–Milner type inference](../20-notes/hindley-milner-type-inference.md)
- [A greenfield type system for Catena](../20-notes/catena-greenfield-type-system.md)
- [What should a greenfield Catena type system guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
- [Hindley–Milner type inference map](../10-maps/hindley-milner-type-inference.md)
