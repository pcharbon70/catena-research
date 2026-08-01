---
title: "Deductive Systems and Categories III"
kind: source
created: "2026-07-31"
authors:
  - "Joachim Lambek"
published: 1972
citation_key: "lambek1972DeductiveSystemsIII"
container: "Toposes, Algebraic Geometry and Logic, Lecture Notes in Mathematics 274: 57–82"
edition: null
isbn: null
doi: "10.1007/BFb0073965"
url: "https://link.springer.com/chapter/10.1007/BFb0073965"
accessed: "2026-07-31"
tags:
  - cartesian-closed-categories
  - category-theory
  - lambda-calculus
  - program-semantics
aliases:
  - "Lambek on cartesian closed categories and logic"
---

# Deductive Systems and Categories III

## Reference

Joachim Lambek, “Deductive Systems and Categories III: Cartesian Closed
Categories, Intuitionist Propositional Calculus, and Combinatory Logic,” in
*Toposes, Algebraic Geometry and Logic*, Lecture Notes in Mathematics 274
(1972), 57–82. [DOI and publisher record](https://doi.org/10.1007/BFb0073965).

## Contribution

Lambek relates typed deductive and combinatory systems to cartesian closed
categories. The connection makes products and function spaces structural
rather than accidental: conjunction-like pairing is categorical product,
implication-like function space is an exponential, substitution is
composition, and the structural rules are expressed by the product machinery.

## Method

The chapter develops translations between formal deductive systems and
categories with finite products and exponentials, and compares equality of
deductions with equality of categorical arrows. It is a mathematical
equivalence of presentations, not an empirical programming study.

## Findings

- A cartesian closed category provides the semantic operations required by a
  simply typed functional core: identity, composition, products, a terminal
  object, exponentials, evaluation, and currying.
- Conversely, the syntax and equations of the corresponding typed calculus
  generate a category. Syntax can therefore be treated as an initial or free
  structured category rather than merely interpreted in one fixed model.
- Beta and eta principles are not isolated rewrite tricks. They express the
  universal property connecting evaluation and currying.
- The correspondence is extensional and equational. It says when two terms
  have the same denotation in the model, not how much time or space either
  term consumes under a chosen evaluator.

## Relevance

This is the foundation for treating Catena's pure typed fragment as a language
of composable arrows. It also explains why the same typed expression can admit
multiple structure-preserving interpretations, the idea later exploited by
[Compiling to Categories](elliott-2017-compiling-to-categories.md).

The practical lesson is narrower than “make category theory the syntax.”
Products, functions, composition, and their equations already carry the
useful structure. Category terminology is optional at the surface.

## Limits

The result concerns a simply typed, extensional setting. General recursion,
bottom, effects, evaluation order, polymorphism, sums, intensional equality,
and resource usage require further structure or a different semantic account.
It cannot by itself justify compiler rewrites in a strict, effectful language.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
