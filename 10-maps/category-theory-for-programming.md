---
title: "Category Theory for Programming"
kind: map
created: "2026-07-31"
tags:
  - category-theory
  - catena
  - functional-programming
  - language-design
aliases:
  - "Categorical programming map"
---

# Category Theory for Programming

## Scope

This map routes through category theory as a practical language-design,
library-design, semantic, and compilation tool. It starts from typed
composition, then follows the structures that have concrete programming uses:
parametric mapping, datatype recursion, computational dependency, data
accessors, effects, and alternate interpretations.

The route is deliberately selective. It does not try to inventory category
theory or treat every categorical construction as a candidate Catena feature.

## Start here

- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
  is the main synthesis. It separates categorical laws from operational cost
  and proposes a staged Catena design.
- [Which Categorical Abstractions Should Catena Expose?](../40-inquiries/which-categorical-abstractions-should-catena-expose.md)
  turns the provisional boundary into prototype, proof, corpus, diagnostic,
  and performance questions.
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
  supplies the higher-kinded, coherent-trait, pure/effectful, and inference
  boundaries within which the categorical library would have to fit.

## Trails

### From typed functions to categorical structure

1. [Lambek 1972](../30-sources/lambek-1972-deductive-systems-categories-iii.md)
   relates cartesian closed categories, typed deduction, and combinatory logic.
   Read it for the semantic meaning of identity, composition, products,
   functions, currying, beta, and eta—not as a surface-syntax proposal.
2. [Compiling to Categories](../30-sources/elliott-2017-compiling-to-categories.md)
   turns that correspondence into a modular compiler transformation with
   circuit, differentiation, incremental, and analysis interpretations.

### Why generic functions have laws

1. [Reynolds 1983](../30-sources/reynolds-1983-types-abstraction-parametric-polymorphism.md)
   gives the relational abstraction theorem that makes uniform polymorphism a
   semantic constraint.
2. [Wadler 1989](../30-sources/wadler-1989-theorems-for-free.md) derives
   programmer-facing equations from polymorphic types and exposes their
   assumptions.
3. Return to the synthesis's lawfulness ladder to distinguish a type, a
   promise, a property test, a derivation, a parametricity result, and a proof.

### Calculate over algebraic data

1. [Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire](../30-sources/meijer-et-al-1991-functional-programming-bananas.md)
   develops folds, unfolds, hylomorphisms, and laws from datatype fixed points.
2. Compare its general calculus with the synthesis's smaller recommendation:
   derive ordinary `map`, `fold`, and `traverse` operations, and leave generalized
   recursion schemes in a library until they improve a real corpus.

### Choose a computational dependency structure

1. [Moggi 1991](../30-sources/moggi-1991-notions-computation-monads.md)
   separates values from computations and gives monadic sequencing its
   semantic foundation.
2. [Wadler 1995](../30-sources/wadler-1995-monads-functional-programming.md)
   applies that structure to evaluators, state-like programs, and parsers.
3. [McBride and Paterson 2008](../30-sources/mcbride-paterson-2008-applicative-programming-effects.md)
   show why a fixed computation graph deserves a weaker applicative interface
   and how traversal follows from it.
4. [Hughes 2000](../30-sources/hughes-2000-generalising-monads-arrows.md)
   handles libraries that must preserve static structure unavailable through
   an unrestricted host-language function.
5. [Uustalu and Vene 2005](../30-sources/uustalu-vene-2005-essence-dataflow-programming.md)
   model context-dependent stream computation with comonads and coKleisli
   composition.

The structures overlap, but each retains different information. Follow the
weakest interface that supports the program rather than choosing by hierarchy.

### Compose data access

1. [Profunctor Optics](../30-sources/pickering-et-al-2017-profunctor-optics.md)
   unifies lenses, prisms, and traversals under ordinary composition with
   structural profunctor constraints.
2. The open Catena question is representational: begin with derived concrete
   field and variant optics, then measure whether the profunctor encoding
   improves mixed composition enough to justify its higher-rank trait errors
   and specialization needs.

### Connect categorical effects to direct handlers

1. [Plotkin and Power 2003](../30-sources/plotkin-power-2003-algebraic-operations-generic-effects.md)
   characterize algebraic operations for strong monads and relate operations
   to generic effects through an enriched Yoneda argument.
2. [Plotkin and Pretnar 2009](../30-sources/plotkin-pretnar-2009-handlers-algebraic-effects.md)
   interpret handlers as models and handling as the homomorphism induced from
   a free computation.
3. [Algebraic Effects and Handlers](algebraic-effects-and-handlers.md) continues
   from those foundations to Catena's operational choices: effect rows,
   lexical capability identity, deep handling, affine resumptions, scoped
   computations, cleanup, and runtime representation.

This trail prevents a false choice. Monads can represent explicit
computational data while native handlers provide direct language effects.

## Open questions

- Which Catena fragment admits the relational parametricity theorem required
  for naturality and free-theorem tooling?
- Can the proposed higher-kinded traits retain principal inference and useful
  errors under real `Functor`, `Applicative`, `Monad`, and `Traversable` code?
- How should promised, tested, derived, trusted, and proved laws differ in the
  elaborated core and optimizer?
- Which datatype shapes can derive maps, folds, and traversals, and what
  evaluation order do those derivations promise?
- Does the applicative/monad boundary enable enough analysis, validation, or
  concurrency structure to justify the added vocabulary?
- Do generated concrete optics cover Catena's data-access needs, or does mixed
  composition justify a profunctor representation?
- Can a categorical compiler interpretation preserve source diagnostics and
  coexist with effectful, control-flow, and machine-oriented IRs?
- Which categorical equations remain contextual equivalences in Catena's
  strict, recursive, effectful semantics?

Track the experiments and decision criteria in
[Which Categorical Abstractions Should Catena Expose?](../40-inquiries/which-categorical-abstractions-should-catena-expose.md).
