---
title: "Notions of Computation as Monoids"
kind: source
created: "2026-07-31"
authors:
  - "Exequiel Rivas"
  - "Mauro Jaskelioff"
published: 2017
citation_key: "rivasJaskelioff2017NotionsComputationMonoids"
container: "Journal of Functional Programming 27, e21"
edition: null
isbn: null
doi: "10.1017/S0956796817000132"
url: "https://www.cambridge.org/core/journals/journal-of-functional-programming/article/notions-of-computation-as-monoids/70019FC0F2384270E9F41B9719042528"
accessed: "2026-07-31"
tags:
  - applicative-functors
  - arrows
  - category-theory
  - monads
aliases:
  - "Rivas and Jaskelioff on computational monoids"
---

# Notions of Computation as Monoids

## Reference

Exequiel Rivas and Mauro Jaskelioff, “Notions of Computation as Monoids,”
*Journal of Functional Programming* 27 (2017), e21.
[DOI](https://doi.org/10.1017/S0956796817000132),
[publisher record](https://www.cambridge.org/core/journals/journal-of-functional-programming/article/notions-of-computation-as-monoids/70019FC0F2384270E9F41B9719042528),
and [extended author version](https://www.fceia.unr.edu.ar/~mauro/pubs/Notions_of_Computation_as_Monoids_ext.pdf).

## Research question

Can monads, applicative functors, and arrows be presented as instances of one
abstract construction, and can results proved at that level produce useful
programming constructions for all three?

## Method

The paper identifies each notion of computation with a monoid in an
appropriate monoidal category. It then develops free constructions and Cayley
representations abstractly and instantiates them for monads, applicatives, and
arrows. The common presentation is also used to analyze relationships among
the three structures.

## Findings

- The word *monoid* applies at more than the value level: a notion of
  computation can be a monoid object under a suitable tensor product.
- Monads, applicatives, and arrows share an associative composition-plus-unit
  pattern while differing in their ambient category and therefore in the
  information their operations expose.
- Free monoids and Cayley representations transfer to useful constructions
  for each computational abstraction.
- A shared abstract presentation clarifies relationships without identifying
  the three interfaces or making their programming capabilities equal.

## Relevance

This paper links Catena's value-level `Semigroup`/`Monoid` classes to the
broader computational hierarchy without conflating them. It supports teaching
the initial class set as repeated algebraic patterns—associative composition,
sometimes with identity—while preserving the distinct kinds and operations of
`Monad`, `Applicative`, and `Arrow`.

## Limits

The work is categorical and construction oriented. It does not propose a
surface type-class hierarchy, `Apply` or `Chain` interfaces, inference rules,
law testing, or operational semantics for effects. “A monoid in a monoidal
category” is a semantic unification, not a reason to erase user-facing
distinctions.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
- [Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
- [Combinators research map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md)
