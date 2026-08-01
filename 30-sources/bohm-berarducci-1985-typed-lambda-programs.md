---
title: "Automatic Synthesis of Typed Lambda-Programs on Term Algebras"
kind: source
created: "2026-08-01"
authors:
  - "Corrado Böhm"
  - "Alessandro Berarducci"
published: 1985
citation_key: "bohmBerarducci1985TypedLambdaPrograms"
container: "Theoretical Computer Science 39: 135–154"
edition: null
isbn: null
doi: "10.1016/0304-3975(85)90135-5"
url: "https://arpi.unipi.it/handle/11568/7450"
accessed: "2026-08-01"
tags:
  - algebraic-data-types
  - lambda-calculus
  - polymorphism
  - program-synthesis
aliases:
  - "Böhm–Berarducci encoding paper"
---

# Automatic Synthesis of Typed Lambda-Programs on Term Algebras

## Reference

Corrado Böhm and Alessandro Berarducci, “Automatic Synthesis of Typed
Lambda-Programs on Term Algebras,” *Theoretical Computer Science* 39 (1985):
135–154. [DOI](https://doi.org/10.1016/0304-3975(85)90135-5) and
[University of Pisa record](https://arpi.unipi.it/handle/11568/7450).

## Research question

Can elements and iteratively defined functions over heterogeneous term
algebras be represented uniformly in a second-order typed lambda calculus
without primitive conditionals or recursive constructs?

## Method

The authors characterize iterative functions by finite equation systems,
translate term-algebra elements and their iterators into second-order typed
lambda terms, state a completeness result for a bounded type degree, introduce
a program-equivalence congruence, and illustrate the construction with
integers, lists, and trees.

## Findings

- Constructor-built data can be represented by its polymorphic elimination
  behavior: an encoded value accepts one handler for each constructor and
  produces the handler result.
- Iterative functions then become ordinary applications of that elimination
  interface rather than uses of primitive recursion or case analysis.
- The representation connects a term algebra with a family of typed lambda
  programs and gives a uniform synthesis scheme for its iterators.
- The paper's completeness and equivalence results concern its selected typed
  lambda fragment and formal notion of iterative program.

## Relevance

The Böhm–Berarducci perspective explains why a fold is more than a convenient
helper: it is a complete constructor-handler interface for the corresponding
positive algebraic shape under the paper's assumptions. Catena can use this
idea to specify generated eliminators and to test representation-independent
APIs.

It should not replace Catena's nominal ADTs with lambda encodings by default.
Native constructors preserve nominal identity, pattern diagnostics, coverage
checking, and representation optimization more directly. The encoding is a
semantic bridge and possible compilation technique, not the required surface
representation.

## Limits

The result is formulated for second-order typed lambda programs and iterative
term-algebra functions. It does not establish runtime efficiency, source
ergonomics, separate compilation, pattern coverage, effects, general
recursion, or nominal abstraction for Catena. The accessible institutional
record supports the contribution and examples but does not substitute for a
new empirical evaluation.

## Derived work

- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
- [Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
- [Combinators for Algebraic Data and Categorical Programming map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md)
