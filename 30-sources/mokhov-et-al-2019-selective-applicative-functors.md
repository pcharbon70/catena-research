---
title: "Selective Applicative Functors"
kind: source
created: "2026-08-01"
authors:
  - "Andrey Mokhov"
  - "Georgy Lukyanov"
  - "Simon Marlow"
  - "Jeremie Dimino"
published: 2019
citation_key: "mokhovEtAl2019SelectiveApplicativeFunctors"
container: "Proceedings of the ACM on Programming Languages 3(ICFP), Article 90: 1–29"
edition: null
isbn: null
doi: "10.1145/3341694"
url: "https://eprints.ncl.ac.uk/258640"
accessed: "2026-08-01"
tags:
  - applicative-functors
  - combinator-libraries
  - effects
  - static-analysis
aliases:
  - "Mokhov et al. on selective functors"
---

# Selective Applicative Functors

## Reference

Andrey Mokhov, Georgy Lukyanov, Simon Marlow, and Jeremie Dimino, “Selective
Applicative Functors,” *Proceedings of the ACM on Programming Languages* 3,
ICFP, Article 90 (2019): 1–29. [DOI](https://doi.org/10.1145/3341694) and
[open institutional record](https://eprints.ncl.ac.uk/258640).

## Research question

Can an effectful interface allow runtime values to select which statically
visible effects execute, occupying a useful point between fixed applicative
structure and unrestricted monadic dependency?

## Method

The paper adds `select` to an applicative interface, derives conditional and
branching combinators, states laws and relationships with applicatives and
monads, constructs execution and static-analysis instances, and evaluates the
abstraction through Dune and Haxl case studies. A free construction supports
embedded languages whose possible effects remain inspectable.

## Findings

- `select : F (Either A B) -> F (A -> B) -> F B` always evaluates the first
  computation and may skip the second when the first already supplies a `B`.
- `when`, `if`, binary branch, Boolean conjunction/disjunction, and traversed
  `any`/`all` operations can be derived from the small interface.
- The computation graph remains statically visible even though execution can
  skip a branch dynamically. This permits analyses unavailable through an
  opaque function passed to monadic bind.
- Different lawful interpretations may over-approximate all possible effects,
  under-approximate definitely executed effects, or perform concrete dynamic
  execution. The core laws intentionally do not require every unnecessary
  effect to be skipped.
- Multiway branching can improve static information and execution cost, but
  unbounded value-dependent branching approaches monadic power and may make
  static analysis non-terminating or uninformative.
- The Dune and Haxl examples demonstrate build-dependency analysis and
  speculative parallel execution, while also exposing operational choices not
  fixed by the abstract laws.

## Relevance

Selective branching is a credible future Catena combinator layer for build
graphs, validation, remote requests, and analyzable workflows. It uses ordinary
sums, products, functors, and applicatives and demonstrates the “weakest
adequate structure” rule.

Catena's agreed initial seventeen-class hierarchy does not contain
`Selective`. The paper is therefore evidence for an experiment, not permission
to silently revise that hierarchy. Concrete libraries can first expose
`select`-like operations; a new class should require corpus evidence, kinding,
coherence, laws, diagnostics, and operational documentation.

## Limits

The abstraction adds a subtle law and execution model. Its laws permit
different effect-skipping behavior, so users need to know whether an instance
is an analyzer, executor, or both. The industrial cases do not establish broad
usability, and multiway selection, cancellation, resource cleanup, exception
behavior, and integration with native algebraic handlers require further work.

## Derived work

- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
- [Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
- [Combinators for Algebraic Data and Categorical Programming map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md)
