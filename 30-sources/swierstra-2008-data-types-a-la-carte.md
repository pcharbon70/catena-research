---
title: "Data Types à la Carte"
kind: source
created: "2026-08-01"
authors:
  - "Wouter Swierstra"
published: 2008
citation_key: "swierstra2008DataTypesALaCarte"
container: "Journal of Functional Programming 18(4): 423–436"
edition: null
isbn: null
doi: "10.1017/S0956796808006758"
url: "https://www.cambridge.org/core/journals/journal-of-functional-programming/article/data-types-a-la-carte/14416CB20C4637164EA9F77097909409"
accessed: "2026-08-01"
tags:
  - algebraic-data-types
  - combinator-libraries
  - extensibility
  - recursion-schemes
aliases:
  - "Swierstra's data types à la carte"
---

# Data Types à la Carte

## Reference

Wouter Swierstra, “Data Types à la Carte,” *Journal of Functional Programming*
18, no. 4 (2008): 423–436.
[DOI and publisher record](https://doi.org/10.1017/S0956796808006758) and
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/14416CB20C4637164EA9F77097909409/S0956796808006758a.pdf/data_types_a_la_carte.pdf).

## Research question

Can independently defined constructor families and their functions be
assembled modularly, allowing new cases and new interpretations without
recompiling or rewriting existing components?

## Method

Swierstra separates one recursive layer of an expression language into functor
components, combines components with a binary coproduct, closes the recursive
type with a fixed point, and defines consumers as folds over modular algebras.
Type-class-directed injections hide coproduct nesting. The construction is then
extended from expression syntax to coproducts of signatures and free monads.

## Findings

- Factoring constructor families into functors makes their coproduct a modular
  sum of syntax components.
- A generic fixed point plus `fold` consumes any assembled signature once each
  component supplies the relevant algebra.
- Smart constructors can hide explicit fixed-point wrapping and coproduct
  injections, giving clients a conventional expression-building API.
- The type-class injection mechanism is convenient but depends on overlapping
  instance selection and can become ambiguous; explicit nesting and duplicate
  components expose limitations.
- Free monads over modular signatures apply the same sum-and-fold structure to
  effect syntax and interpreters.
- The approach handles an important form of the expression problem but does
  not eliminate every extensibility or inference tradeoff.

## Relevance

This paper shows how sum, functor, fixed-point, injection, and fold combinators
can assemble an extensible language from ADT-shaped components. Catena should
make the explicit form expressible in libraries and test whether generated
injection evidence can remain coherent.

It should not import the paper's overlapping instance search into Catena's
initial trait system. Closed nominal ADTs remain the default for domain data;
sum-of-functors encodings are an advanced library technique for deliberately
extensible syntax or effect descriptions.

## Limits

The paper is a compact Haskell functional pearl rather than a performance,
diagnostic, or large-codebase evaluation. Its injection machinery relies on
host-language instance features Catena currently rejects. Boilerplate,
compilation cost, error quality, duplicate signatures, nested datatypes, GADTs,
and runtime representation remain concerns. Native algebraic handlers also
change the case for representing all effects as free monad syntax.

## Derived work

- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
- [Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
- [Combinators for Algebraic Data and Categorical Programming map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md)
