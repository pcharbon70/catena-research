---
title: "Catena Type-System Design"
kind: map
created: "2026-07-31"
tags:
  - catena
  - language-design
  - type-inference
aliases:
  - "Greenfield Catena map"
---

# Catena Type-System Design

## Scope

This map organizes a greenfield account of Catena's type system. The language
name is the only inherited input: no previous Catena specification,
implementation, or test suite supplies requirements or evidence.

## Start here

- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
  is the main proposal and guarantee matrix.
- [What Should a Greenfield Catena Type System Guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
  tracks the formal obligations and design decisions that remain open.
- [How Hindley–Milner Type Inference Works](../20-notes/hindley-milner-type-inference.md)
  is the independent foundation behind the principal rank-1 core.
- [Algebraic Effects and Handlers](algebraic-effects-and-handlers.md) expands
  the effect-row layer into handler semantics, instance identity, resumption
  multiplicity, scoped computations, and implementation choices.

## Trails

### Build the trusted core

1. [Milner 1978](../30-sources/milner-1978-type-polymorphism.md) supplies
   Algorithm W and the practical implicit-polymorphism discipline.
2. [Damas and Milner 1982](../30-sources/damas-and-milner-1982-principal-type-schemes.md)
   state the completeness and principality contract.
3. [Typing Haskell in Haskell](../30-sources/jones-1999-typing-haskell-in-haskell.md)
   demonstrates a clarity-first executable specification with kinds and
   binding groups.

### Add structured constraints conservatively

1. [Jones 1994](../30-sources/jones-1994-theory-of-qualified-types.md) frames
   traits and row predicates as qualified types with evidence.
2. [Gaster and Jones 1996](../30-sources/gaster-jones-1996-extensible-records-variants.md)
   gives unique-label rows and lacks predicates for structural data.
3. [Jones 2000](../30-sources/jones-2000-functional-dependencies.md) shows why
   multi-parameter traits need declared dependencies and improvement rules.

### Track effects without surrendering inference

1. [Wright 1995](../30-sources/wright-1995-simple-imperative-polymorphism.md)
   establishes the strict-language generalization hazard.
2. [Leijen 2014](../30-sources/leijen-2014-koka-row-polymorphic-effects.md)
   supplies a worked duplicate-label effect-row calculus and a more precise
   effect-directed restriction.
3. [The algebraic-effects map](algebraic-effects-and-handlers.md) continues from
   row inference to operation algebraicity, deep and shallow handlers, lexical
   instances, abstraction safety, affine and multi-shot resumptions, scoped
   effects, and runtime strategies.

### Cross explicit expressiveness boundaries

1. [Dunfield and Krishnaswami 2013](../30-sources/dunfield-krishnaswami-2013-bidirectional-typechecking.md)
   explains higher-rank checking with predictable annotations.
2. [OutsideIn(X)](../30-sources/vytiniotis-et-al-2011-outsidein.md) shows why
   GADT-like local assumptions need scoped constraints and a narrower
   inference promise.

## Open questions

- Do structural variants justify their surface and solver complexity alongside
  nominal algebraic data?
- Can lexical effect capabilities coexist with duplicate-label rows while
  retaining principal inference and higher-order abstraction safety?
- Are affine core resumptions plus a runtime consumed token sufficient, or is
  inferred control-flow linearity required?
- Which trait termination condition is simple enough to teach and strong
  enough to guarantee resolution?
- What prototype corpus will test whether public signatures and higher-rank
  annotations appear at acceptable locations?

Keep conclusions in the [greenfield synthesis](../20-notes/catena-greenfield-type-system.md)
and active work in the [guarantee inquiry](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
and [algebraic-effect inquiry](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md).
