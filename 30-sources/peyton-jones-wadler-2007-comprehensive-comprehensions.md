---
title: "Comprehensive Comprehensions"
kind: source
created: "2026-08-01"
authors:
  - "Simon Peyton Jones"
  - "Philip Wadler"
published: 2007
citation_key: "peytonJonesWadler2007ComprehensiveComprehensions"
container: "Proceedings of the ACM SIGPLAN Workshop on Haskell 2007"
edition: null
isbn: null
doi: "10.1145/1291201.1291209"
url: "https://doi.org/10.1145/1291201.1291209"
accessed: "2026-08-01"
tags:
  - comprehensions
  - language-design
  - program-semantics
aliases:
  - "Comprehensions with order by and group by"
---

# Comprehensive Comprehensions

## Reference

Simon Peyton Jones and Philip Wadler, “Comprehensive Comprehensions,” in
*Proceedings of the ACM SIGPLAN Workshop on Haskell 2007* (2007), 61–72.
[DOI](https://doi.org/10.1145/1291201.1291209).

## Contribution

The paper extends list comprehensions with ordering, grouping, limiting, zip,
parenthesized qualifier scope, and user-provided transformations. It supplies
syntax, typing, translation, and laws for the extension.

## Method

The authors compare ordinary list queries with SQL, develop the proposal
through examples, then give formal qualifier syntax, typing judgments,
desugaring, and equational laws. Parametric types constrain user-provided order
and grouping operations so they cannot inspect compiler-generated record
representations.

## Findings

- Ordinary generators, local bindings, Boolean guards, and Cartesian
  composition can be extended with zip, order, and group qualifiers in one
  calculus.
- Qualifier grouping is semantically significant. Parenthesizing a subset of
  generators before sorting or grouping can change values and even the types
  of variables that remain in scope.
- A group qualifier transforms every in-scope bound value into a collection of
  grouped values. It is therefore not merely a filter or terminal collection
  step.
- User-supplied polymorphic transformations can generalize sorting, grouping,
  filtering, limiting, and reversal while hiding the compiler's internal tuple
  representation.
- The work shows that such rich syntax can still receive formal typing and
  desugaring rules, but the examples also require nontrivial precedence,
  scoping, and type explanations.
- Zip and Cartesian composition are independent qualifier combinators rather
  than alternate readings of the same separator.

## Relevance

The paper demonstrates both the extensibility of comprehension notation and
the resulting semantic pressure. Catena should resist turning its initial list
form into a query sublanguage. Ordering, grouping, limiting, zip, reduction,
and generic target collection already have explicit library operations with
distinct evidence and cost contracts.

The formal treatment supplies a later path if real use cases justify richer
qualifiers: each extension needs its own binder transformation, typing rule,
scope, order, and optimization contract rather than being accepted as harmless
syntax sugar.

## Limits

The proposal is not an empirical usability study and targets lazy Haskell
lists. Its claim of simple implementation concerns desugaring, not the
explanatory burden of the feature, the behavior of effects, or efficient BEAM
lowering.

## Derived work

- [List Comprehensions](../20-notes/list-comprehensions.md)
- [How Should Catena Specify List Comprehensions?](../40-inquiries/how-should-catena-specify-list-comprehensions.md)
- [List Comprehensions map](../10-maps/list-comprehensions.md)
