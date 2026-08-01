---
title: "The Essence of the Iterator Pattern"
kind: source
created: "2026-07-31"
authors:
  - "Jeremy Gibbons"
  - "Bruno César dos Santos Oliveira"
published: 2009
citation_key: "gibbonsOliveira2009EssenceIterator"
container: "Journal of Functional Programming 19(3–4): 377–402"
edition: null
isbn: null
doi: "10.1017/S0956796809007291"
url: "https://www.cs.ox.ac.uk/publications/publication1409-abstract.html"
accessed: "2026-07-31"
tags:
  - applicative-functors
  - folds
  - traversals
  - type-classes
aliases:
  - "Gibbons and Oliveira on traversals"
---

# The Essence of the Iterator Pattern

## Reference

Jeremy Gibbons and Bruno César dos Santos Oliveira, “The Essence of the
Iterator Pattern,” *Journal of Functional Programming* 19, nos. 3–4 (2009):
377–402. [DOI](https://doi.org/10.1017/S0956796809007291),
[official bibliographic record](https://www.cs.ox.ac.uk/publications/publication1409-abstract.html),
and [author manuscript](https://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/iterator-msfp.pdf).

## Research question

Which functional abstraction captures both mapping over a collection and
accumulating effects during an iteration, and which laws distinguish a valid
single traversal from an arbitrary function of the same type?

## Method

The paper relates the imperative iterator pattern to applicative traversal. It
develops `traverse`, states naturality, identity, and composition laws, and
uses examples such as word counting and `repmin` to illustrate mapping,
accumulation, and traversal fusion.

## Findings

- Mapping changes elements while preserving shape; folding accumulates a
  summary while discarding shape. Traversal combines both aspects.
- An applicative parameter captures effects accumulated during a structurally
  determined visit.
- Naturality makes traversal independent of a particular applicative
  representation; identity preserves the original structure; composition
  permits nested effects to be traversed coherently.
- The usual three laws do not by themselves express every intended
  “visit each position exactly once” condition. The paper discusses bogus
  definitions and an additional indexing-style criterion.

## Relevance

This is the main evidence for including both `Foldable` and `Traversable` in
Catena's initial hierarchy. It also shows why the `Traversable` contract needs
more than a method signature and why the language must document visit order
and cardinality in addition to abstract laws.

## Limits

The examples and laws assume a pure functional setting and do not settle a
strict Catena implementation's exception timing, early termination, parallel
scheduling, or stack behavior. The difficulty of ruling out duplicate visits
means automatic derivation needs a syntactic construction guarantee, not only
property tests for the standard three traversal laws.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
- [Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
- [Combinators research map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md)
