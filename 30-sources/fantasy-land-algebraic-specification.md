---
title: "Fantasy Land Algebraic Specification"
kind: source
created: "2026-07-31"
authors:
  - "Fantasy Land contributors"
published: null
citation_key: "fantasyLandAlgebraicSpecification"
container: "Official interoperability specification"
edition: "Living specification"
isbn: null
doi: null
url: "https://github.com/fantasyland/fantasy-land"
accessed: "2026-07-31"
tags:
  - algebraic-structures
  - lawfulness
  - type-classes
aliases:
  - "Fantasy Land specification"
---

# Fantasy Land Algebraic Specification

## Reference

Fantasy Land contributors, *Fantasy Land Algebraic Specification*, living
interoperability specification.
[Official repository](https://github.com/fantasyland/fantasy-land), accessed
2026-07-31.

## Contribution

The specification defines a language-neutral vocabulary of common algebraic
interfaces through required operations, superclass relationships, and
equational laws. Of particular relevance here, it keeps several structures
that are often collapsed in typed standard libraries separate: `Apply` from
`Applicative`, `Chain` from `Monad`, and `Extend` from `Comonad`.

## Method

Each algebra is presented as a structural interface. The specification gives
the operation shape, required parent algebras, and equations over arbitrary
values and functions. It also records which methods can be derived from
stronger structures. The document is normative for interoperability, not a
formal proof or empirical comparison.

## Findings

- `Setoid` requires an equivalence relation; `Ord` adds a total order relative
  to that equivalence.
- `Semigroupoid` provides associative typed composition, while `Category` adds
  left and right identities.
- `Semigroup` provides an associative same-type combination, while `Monoid`
  adds a two-sided identity.
- `Functor` preserves identity and composition. `Bifunctor` maps both varying
  positions with corresponding identity and composition laws.
- `Apply` is a functor with associative contextual application but no way to
  inject an arbitrary pure value. `Applicative` adds that injection and its
  identity, homomorphism, and interchange laws.
- `Chain` adds associative value-dependent sequencing without requiring an
  injection. `Monad` combines `Applicative` and `Chain` and adds left and right
  identity for sequencing.
- `Extend` provides associative context-dependent extension without an
  extraction operation. `Comonad` adds extraction and two identity laws.
- `Traversable` combines `Functor` and `Foldable`, and its traversal must obey
  naturality, identity, and composition across applicatives.

## Relevance

The specification provides precise names for many of the weak and strong
interfaces in Catena's selected initial hierarchy. It helps prevent
`Applicative`, `Monad`, and `Comonad` from swallowing their useful unitless
substructures. Its laws are inputs to Catena's design; they still need Catena
syntax, kinding, evidence, operational order, and diagnostics. The initial
`Arrow` class requires separate evidence.

## Limits

The specification targets structural interoperability in a dynamically typed
host and includes algebras outside Catena's selected set. It does not address
principal inference, dictionary coherence, proof status, evaluation effects,
or compiler optimization. Some inheritance choices also need kind-aware
reinterpretation in Catena: a binary `Bifunctor` cannot literally be a unary
`Functor` dictionary without fixing one argument.

## Derived work

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
- [How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
- [Category Theory for Programming map](../10-maps/category-theory-for-programming.md)
