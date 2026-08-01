---
title: "QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs"
kind: source
created: "2026-08-01"
authors:
  - "Koen Claessen"
  - "John Hughes"
published: 2000
citation_key: "claessenHughes2000quickCheck"
container: "Proceedings of ICFP 2000"
edition: null
isbn: "1-58113-202-6"
doi: "10.1145/351240.351266"
url: "https://doi.org/10.1145/351240.351266"
accessed: "2026-08-01"
tags:
  - property-based-testing
  - specification
  - testing
aliases:
  - "QuickCheck"
---

# QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs

## Reference

Koen Claessen and John Hughes. “QuickCheck: A Lightweight Tool for Random
Testing of Haskell Programs.” In *Proceedings of ICFP 2000*, 268–279.
[DOI](https://doi.org/10.1145/351240.351266).

## Contribution

QuickCheck represents executable properties as ordinary functions, generates
random inputs, supports custom generators, and reports counterexamples. The
approach turns general behavioral claims into reusable test drivers rather than
enumerating examples by hand.

## Method

The paper presents the property and generator interfaces, their implementation,
and case studies covering unification, circuits, theorem proving, pretty
printing, and data-structure libraries. It also discusses generator design,
coverage monitoring, and sources of false confidence.

## Findings

- A property declaration can generate many concrete checks when the language
  also exposes composable generators for its input domain.
- Conditional properties and poorly distributed generators can silently test
  too little; coverage information is part of interpreting a run.
- Random testing is effective at finding witnesses to failure, but a successful
  finite sample is not a universal proof.

## Relevance

Catena’s approachable `property` feature can be executable without pretending
to be deductive verification. Evidence should record seed, generator,
discarded cases, distribution or coverage, run count, environment, and the
smallest available counterexample.

## Limits

Results depend on generator quality, oracle correctness, sample size, and
observability. Rare cases may remain undiscovered, and shrinking a failure does
not establish why the property failed. The original work does not address
authorization, signed provenance, or concurrent temporal behavior.

## Derived work

- [Language-Integrated Specifications and Governance](../20-notes/language-integrated-specifications-and-governance.md)
- [Language-Integrated Specifications and Governance map](../10-maps/language-integrated-specifications-and-governance.md)
