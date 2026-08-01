---
title: "Why Functional Programming Matters"
kind: source
created: "2026-08-01"
authors:
  - "John Hughes"
published: 1989
citation_key: "hughes1989WhyFunctionalProgrammingMatters"
container: "The Computer Journal 32(2): 98–107"
edition: null
isbn: null
doi: "10.1093/comjnl/32.2.98"
url: "https://academic.oup.com/comjnl/article-abstract/32/2/98/543535"
accessed: "2026-08-01"
tags:
  - combinator-libraries
  - functional-programming
  - modularity
  - recursion-schemes
aliases:
  - "Hughes on functional-programming glue"
---

# Why Functional Programming Matters

## Reference

John Hughes, “Why Functional Programming Matters,” *The Computer Journal* 32,
no. 2 (1989): 98–107. [DOI and publisher record](https://doi.org/10.1093/comjnl/32.2.98)
and [author-revised paper](https://www.classes.cs.uchicago.edu/archive/2010/spring/22300-1/papers/whyfp.pdf).

## Research question

Which properties of functional programming provide new ways to decompose a
problem and recombine independently useful solutions, rather than merely
removing assignment and side effects?

## Method

Hughes develops examples over lists and trees, numerical approximation, and
game-tree search. He repeatedly factors a specialized recursive program into a
general higher-order producer or consumer plus small problem-specific
functions, then uses lazy evaluation to separate generation from selection.

## Findings

- The ways a program can be decomposed depend on the available ways to compose
  its parts. Module boundaries and separate compilation do not themselves
  provide new conceptual “glue.”
- Abstracting the constructor cases from list recursion produces `reduce`—a
  list fold—from which `sum`, `product`, `all`, `append`, and `map` can be built
  by supplying different algebras.
- The analogous tree reduction packages a datatype's recurring recursion
  pattern and supports reusable tree maps and consumers.
- Higher-order functions make these recursion patterns first-class library
  components instead of control structures copied into each function.
- In a lazy language, a producer and consumer may communicate through an
  incremental list or tree without constructing all of it. This enables
  modular generator/selector designs whose demand behavior determines cost.

## Relevance

The paper supplies the practical motivation for Catena combinators: a
combinator is useful when it creates a new seam at which programs can be split
and recombined. Its `reduce` examples connect ordinary ADT eliminators directly
to higher-order library design. Catena can adopt that factoring even though its
default evaluator is strict.

The lazy examples also impose a warning. A strict Catena needs an explicit
`Iterator`, `Stream`, fusion pass, or producer/consumer protocol before it can
claim the same allocation and termination behavior.

## Limits

The paper argues through examples rather than controlled usability or
performance studies. Several cost claims depend on non-strict evaluation and
do not transfer automatically to a strict language. It predates type classes,
applicatives, modern effect systems, optimizer validation, and current
diagnostic expectations.

## Derived work

- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
- [Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
- [Combinators for Algebraic Data and Categorical Programming map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md)
