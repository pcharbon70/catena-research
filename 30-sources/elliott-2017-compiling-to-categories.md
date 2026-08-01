---
title: "Compiling to Categories"
kind: source
created: "2026-07-31"
authors:
  - "Conal Elliott"
published: 2017
citation_key: "elliott2017CompilingCategories"
container: "Proceedings of the ACM on Programming Languages 1(ICFP), Article 27: 1–27"
edition: null
isbn: null
doi: "10.1145/3110271"
url: "https://conal.net/papers/compiling-to-categories/"
accessed: "2026-07-31"
tags:
  - cartesian-closed-categories
  - compilers
  - domain-specific-languages
  - program-transformation
aliases:
  - "Elliott on compiling to categories"
---

# Compiling to Categories

## Reference

Conal Elliott, “Compiling to Categories,” *Proceedings of the ACM on
Programming Languages* 1, ICFP, Article 27 (2017): 1–27.
[DOI](https://doi.org/10.1145/3110271),
[author page](https://conal.net/papers/compiling-to-categories/), and
[paper](https://conal.net/papers/compiling-to-categories/compiling-to-categories.pdf).

## Contribution

Elliott turns the correspondence between simply typed lambda calculus and
cartesian closed categories into a compiler technique. Ordinary typed Haskell
functions are transformed into categorical combinators and then interpreted
in a category supplied outside the compiler.

## Method

The paper describes a GHC plugin and several category instances. It translates
lambda abstraction, application, products, and selected sums into structural
combinators, then demonstrates interpretations as hardware circuits,
automatic differentiation, incremental computation, interval analysis, and
compositions of those interpretations.

## Findings

- A compositional source transformation can reuse host-language syntax and
  type checking while changing the denotation of a program.
- The compiler extension need not know every target interpretation. New
  categories are defined through ordinary type-class instances.
- Cartesian structure can expose computation graphs and parallelism; closed
  structure supports higher-order functions, although avoiding closure can
  sometimes yield a better target representation.
- Multiple interpretations can be combined, such as differentiating an
  incrementally evaluated or hardware-targeted computation.

## Relevance

This is concrete evidence that categorical structure can be a compilation
interface rather than surface-language ideology. A future Catena experiment
could translate a restricted pure fragment into typed categorical IR and let
libraries provide circuit, differentiation, or incremental interpretations.

## Limits

The prototype is tied to particular Haskell and GHC mechanisms and does not
establish production-scale ergonomics, compile-time cost, or semantic coverage
for a full effectful language. Recursion, partiality, sums, higher-order
targets, and target-specific cost models complicate the clean CCC story. The
demonstration is a research direction, not evidence that every Catena function
should be compiled this way.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [Which Categorical Abstractions Should Catena Expose?](../40-inquiries/which-categorical-abstractions-should-catena-expose.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
