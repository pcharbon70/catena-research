---
title: "Principal Type-Schemes for Functional Programs"
kind: source
created: "2026-07-31"
authors:
  - "Luís Damas"
  - "Robin Milner"
published: 1982
citation_key: "damasMilner1982PrincipalTypeSchemes"
container: "POPL '82: Proceedings of the 9th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages, 207–212"
edition: null
isbn: null
doi: "10.1145/582153.582176"
url: "https://doi.org/10.1145/582153.582176"
accessed: "2026-07-31"
tags:
  - algorithm-w
  - hindley-milner
  - principal-types
  - type-inference
aliases:
  - "Damas–Milner 1982"
---

# Principal Type-Schemes for Functional Programs

## Reference

Luís Damas and Robin Milner, “Principal Type-Schemes for Functional
Programs,” in *POPL '82*, 207–212.
[DOI](https://doi.org/10.1145/582153.582176) and
[University of Edinburgh record](https://www.research.ed.ac.uk/en/publications/principal-type-schemes-for-functional-programs/).

## Research question

Does Algorithm W merely find *a* type, or does it succeed whenever the
declarative type system can type the term and return a most-general result?

## Method

The paper defines the ordering between type schemes by generic instantiation,
presents an ML-style assignment system over variables, application,
abstraction, and `let`, and relates its syntax-directed Algorithm W to that
system. The proof relies on the most-general-unifier property and induction on
typing derivations.

## Findings

- W is sound: a successful `(substitution, type)` result corresponds to a
  derivable typing under the substituted assumptions.
- W is complete for the presented rank-1 `let`-polymorphic system: if a term
  has a type, W succeeds.
- The inferred closure is principal: every other valid type scheme is a
  generic instance of it.
- The closure operation quantifies the variables free in the inferred type but
  not free in the substituted assumptions. Applying the inferred substitution
  to the environment before generalization is therefore part of the theorem,
  not an incidental implementation detail.
- Typeability is decidable for the system presented in the paper.

## Relevance

This source supplies the contract behind claims that a compiler “implements
HM” or “infers principal types.” For Catena, the proof shape highlights where
extensions need new evidence: qualified constraints, kinds, and effect rows
must preserve most-general solving and the correct generalization set.

## Limits

The paper is concise and defers detailed proofs to Damas's thesis. Its language
does not include recursive binding groups, type classes, effects, or
higher-rank polymorphism. Principality does not automatically survive adding
those features.

## Derived work

- [Hindley–Milner type inference](../20-notes/hindley-milner-type-inference.md)
- [How should Catena preserve principal inference while extending HM?](../40-inquiries/how-should-catena-preserve-principal-inference.md)
- [Hindley–Milner type inference map](../10-maps/hindley-milner-type-inference.md)
