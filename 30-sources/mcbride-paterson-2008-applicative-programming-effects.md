---
title: "Applicative Programming with Effects"
kind: source
created: "2026-07-31"
authors:
  - "Conor McBride"
  - "Ross Paterson"
published: 2008
citation_key: "mcbridePaterson2008Applicative"
container: "Journal of Functional Programming 18(1): 1–13"
edition: null
isbn: null
doi: "10.1017/S0956796807006326"
url: "https://openaccess.city.ac.uk/id/eprint/13222/"
accessed: "2026-07-31"
tags:
  - applicative-functors
  - category-theory
  - effects
  - traversals
aliases:
  - "McBride and Paterson on applicative functors"
---

# Applicative Programming with Effects

## Reference

Conor McBride and Ross Paterson, “Applicative Programming with Effects,”
*Journal of Functional Programming* 18, no. 1 (2008): 1–13.
[DOI](https://doi.org/10.1017/S0956796807006326),
[open repository record](https://openaccess.city.ac.uk/id/eprint/13222/), and
[author manuscript](https://openaccess.city.ac.uk/13222/1/Applicative-final.pdf).

## Contribution

The paper identifies applicative functors as a recurring effectful-programming
pattern weaker than monads. `pure` embeds a value and applicative application
combines an effectful function with an effectful argument while the program's
effectful shape remains fixed.

## Method

McBride and Paterson abstract the interface from sequencing, vector
transposition, and environment-based evaluation. They state laws, derive
generic traversal and accumulation operations, compare the structure with
monads and arrows, and characterize it categorically as a strong lax monoidal
functor for products.

## Findings

- Every monad gives an applicative functor, but applicatives exist that cannot
  support monadic bind.
- Applicative expressions have a canonical form: one pure function applied to
  a fixed sequence of effectful arguments. This exposes structure to static
  analysis and allows independent effects such as validation errors to
  accumulate.
- Monadic bind is strictly more expressive because an earlier value can choose
  the later computation. That power also hides the later structure.
- Applicative functors compose directly even when the corresponding monads do
  not, and they support a generic `Traversable` interface.
- The laws identify the interface with coherent product-preserving effectful
  combination, rather than merely a convenient pair of functions.

## Relevance

This is the main evidence for Catena's “weakest adequate abstraction” rule.
Validation, configuration loading, independent queries, and static analysis
should not require monadic sequencing when their computation graph is fixed.
Datatype-derived traversal also belongs at this layer.

## Limits

The paper does not measure programmer comprehension or real-world optimizer
benefits. Applicative order and parallelism still need an operational
contract: fixed dependency structure does not by itself authorize concurrent
execution or effect reordering.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [Which Categorical Abstractions Should Catena Expose?](../40-inquiries/which-categorical-abstractions-should-catena-expose.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
