---
title: "Hindley–Milner Type Inference"
kind: map
created: "2026-07-31"
tags:
  - hindley-milner
  - principal-types
  - type-inference
aliases:
  - "HM map"
---

# Hindley–Milner Type Inference

## Scope

This map isolates the independent mathematical foundation of principal rank-1
type inference and the points where additional features require new evidence.
It contains no trail through an existing Catena specification or compiler.

## Start here

- [How Hindley–Milner Type Inference Works](../20-notes/hindley-milner-type-inference.md)
  explains substitutions, unification, Algorithm W, principality, and the
  boundary of the classic theorem.
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
  applies the foundation to a language designed from a blank slate.

## Trails

### Principal schemes and Algorithm W

1. [Hindley 1969](../30-sources/hindley-1969-principal-type-scheme.md)
   establishes the principal-scheme property in combinatory logic.
2. [Milner 1978](../30-sources/milner-1978-type-polymorphism.md) gives the
   programming-language discipline and Algorithm W.
3. [Damas and Milner 1982](../30-sources/damas-and-milner-1982-principal-type-schemes.md)
   prove completeness and principality for the `let`-polymorphic core.
4. [Typing Haskell in Haskell](../30-sources/jones-1999-typing-haskell-in-haskell.md)
   turns substitutions, kinds, schemes, predicates, and binding groups into an
   executable specification.

### Qualified extensions

- [A Theory of Qualified Types](../30-sources/jones-1994-theory-of-qualified-types.md)
  adds predicates and evidence while exposing ambiguity and coherence as
  additional obligations.
- [Type Classes with Functional Dependencies](../30-sources/jones-2000-functional-dependencies.md)
  shows how multi-parameter relations need explicit determination information.
- [Extensible Records and Variants](../30-sources/gaster-jones-1996-extensible-records-variants.md)
  uses row kinds and lacks predicates for unique-label structural data.

### Effects and richer checking

- [Simple Imperative Polymorphism](../30-sources/wright-1995-simple-imperative-polymorphism.md)
  explains why strict effects constrain `let` generalization.
- [Koka's row-polymorphic effects](../30-sources/leijen-2014-koka-row-polymorphic-effects.md)
  presents an HM-shaped effect system with duplicate labels and
  effect-directed generalization.
- [Complete and Easy Bidirectional Typechecking](../30-sources/dunfield-krishnaswami-2013-bidirectional-typechecking.md)
  provides an annotation-directed path to predicative higher-rank types.
- [OutsideIn(X)](../30-sources/vytiniotis-et-al-2011-outsidein.md) explains why
  local assumptions require scoped constraints and can eliminate principal
  types.

## Open questions

- Which extensions preserve a unitary, terminating solver?
- Where should generalization stop in a strict effectful language?
- Which programs deserve complete inference, and which should require
  annotations?
- How can evidence coherence be tested independently of deterministic search?

The greenfield decision workbench is
[What Should a Greenfield Catena Type System Guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md).
