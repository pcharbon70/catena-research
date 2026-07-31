---
title: "Complete and Easy Bidirectional Typechecking for Higher-Rank Polymorphism"
kind: source
created: "2026-07-31"
authors:
  - "Jana Dunfield"
  - "Neelakantan R. Krishnaswami"
published: 2013
citation_key: "dunfieldKrishnaswami2013Bidirectional"
container: "ICFP '13: Proceedings of the 18th ACM SIGPLAN International Conference on Functional Programming"
edition: "2021 corrected author-hosted version"
isbn: null
doi: "10.1145/2500365.2500582"
url: "https://research.cs.queensu.ca/home/jana/papers/bidir/Dunfield13_bidir.pdf"
accessed: "2026-07-31"
tags:
  - bidirectional-typing
  - higher-rank-types
  - polymorphism
  - type-checking
aliases:
  - "Complete and Easy"
---

# Complete and Easy Bidirectional Typechecking for Higher-Rank Polymorphism

## Reference

Jana Dunfield and Neelakantan R. Krishnaswami, “Complete and Easy
Bidirectional Typechecking for Higher-Rank Polymorphism,” *ICFP '13* (2013).
[DOI](https://doi.org/10.1145/2500365.2500582) and
[author-hosted corrected paper](https://research.cs.queensu.ca/home/jana/papers/bidir/Dunfield13_bidir.pdf).

## Contribution

The paper gives declarative and algorithmic bidirectional systems for
predicative higher-rank polymorphism. It explains where type information must
flow from an annotation into an expression and where an expression can
synthesize its own type, then proves the algorithm sound and complete with
respect to the declarative system.

## Method

The authors derive the typing rules from proof-theoretic principles. Their
algorithm uses an ordered context containing rigid variables, term variables,
and existential variables that accumulate partial information. Soundness and
completeness are organized around a context-extension relation.

## Findings

- Higher-rank polymorphism can remain decidable and predictable when the
  language checks annotated terms bidirectionally instead of attempting
  unrestricted global inference.
- Introduction forms naturally check against known types, while variables,
  annotations, and eliminations can synthesize types. A separate application
  judgment instantiates quantifiers until a function type is exposed.
- In the presented calculus, annotations are required at polymorphic reducible
  expressions; ordinary normal forms need fewer annotations.
- Ordered contexts make variable scope and incremental existential solutions
  explicit, avoiding search and backtracking in the algorithm.
- The completeness result is for predicative System F. It is not a claim that
  arbitrary impredicative polymorphism can be inferred.

## Relevance

The paper supplies a disciplined escape hatch beyond rank-1 HM. A greenfield
Catena can retain principal implicit inference for ordinary code while allowing
explicit `forall` types at annotated boundaries through a separate checking
mode. Richer polymorphism then does not have to weaken the promise made by the
inference core.

## Limits

The formal language is intentionally small and omits qualified constraints,
effects, records, variants, modules, and `let` generalization. Integrating those
features requires a new declarative system and cannot be inferred from the
paper's metatheory alone.

## Derived work

- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
- [What Should a Greenfield Catena Type System Guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
- [Catena Type-System Design](../10-maps/catena-type-system-design.md)
