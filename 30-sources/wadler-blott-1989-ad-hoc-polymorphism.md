---
title: "How to Make Ad-Hoc Polymorphism Less Ad Hoc"
kind: source
created: "2026-07-31"
authors:
  - "Philip Wadler"
  - "Stephen Blott"
published: 1989
citation_key: "wadlerBlott1989AdHocPolymorphism"
container: "POPL '89: 60–76"
edition: null
isbn: "0-89791-294-2"
doi: "10.1145/75277.75283"
url: "https://www.research.ed.ac.uk/en/publications/how-to-make-ad-hoc-polymorphism-less-ad-hoc/"
accessed: "2026-07-31"
tags:
  - ad-hoc-polymorphism
  - type-classes
  - type-inference
aliases:
  - "Wadler and Blott on type classes"
---

# How to Make Ad-Hoc Polymorphism Less Ad Hoc

## Reference

Philip Wadler and Stephen Blott, “How to Make Ad-Hoc Polymorphism Less Ad
Hoc,” in *POPL '89: Proceedings of the 16th ACM SIGPLAN-SIGACT Symposium on
Principles of Programming Languages* (ACM, 1989), 60–76.
[DOI](https://doi.org/10.1145/75277.75283) and
[official bibliographic record](https://www.research.ed.ac.uk/en/publications/how-to-make-ad-hoc-polymorphism-less-ad-hoc/).

## Contribution

The paper introduces type classes as a disciplined form of ad-hoc
polymorphism integrated with Hindley–Milner typing. A class constrains a type
variable to implementations of named operations, while instances supply the
type-specific behavior.

## Method

Wadler and Blott motivate classes through overloaded equality and arithmetic,
give informal examples, and define class-constrained typing with inference
rules. The system generalizes equality-constrained type variables while
retaining parametric polymorphism for unconstrained variables.

## Findings

- A class constraint is part of a polymorphic type rather than an untyped
  dynamic lookup convention.
- Class declarations organize related overloaded operations; instance
  declarations connect those operations to concrete types.
- Inference can propagate class constraints alongside ordinary
  Hindley–Milner type information.
- Class inclusion supports hierarchies in which a stronger interface makes
  the operations of a weaker one available.
- The type-class mechanism specifies operation availability. Algebraic laws
  remain a semantic contract beyond the method types.

## Relevance

Catena's seventeen categorical concepts are intended as type classes, so their
hierarchy must be reflected in qualified types and explicit dictionary
evidence. This paper supplies the original programming-language mechanism;
[Jones's qualified-type theory](jones-1994-theory-of-qualified-types.md)
supplies later ambiguity and coherence boundaries already adopted by the
greenfield type-system proposal.

## Limits

The original system predates higher-kinded class parameters, modern associated
types, effect rows, and proof-carrying laws. It does not settle coherence for
overlap, termination of unrestricted instance search, or how a binary
constructor class such as `Bifunctor` should interact with a unary one.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
- [How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
