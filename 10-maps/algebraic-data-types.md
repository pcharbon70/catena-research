---
title: "Algebraic Data Types"
kind: map
created: "2026-07-31"
tags:
  - algebraic-data-types
  - catena
  - language-design
  - pattern-matching
aliases:
  - "Algebraic data types map"
  - "ADT research map"
---

# Algebraic Data Types

## Scope

This map routes through algebraic data types as a whole-language feature. It
connects constructor-defined values to structural reasoning, HM inference,
match coverage, module abstraction, generic derivation, runtime representation,
structural variants, and GADTs.

## Start here

- [Algebraic Data Types](../20-notes/algebraic-data-types.md) is the main
  synthesis and initial Catena design proposal.
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
  turns that proposal into declaration, inference, coverage, module,
  derivation, representation, and corpus work.
- [Combinators for Algebraic Data and Categorical Programming](combinators-for-algebraic-data-and-categorical-programming.md)
  follows constructor elimination into mapping, folding, traversal, iteration,
  recursion schemes, optics, and modular syntax.
- [A Greenfield Type System for Catena](../20-notes/catena-greenfield-type-system.md)
  supplies the wider principal-inference, row, trait, GADT, and module
  boundaries.

## Trails

### From constructors to a language feature

1. [HOPE](../30-sources/burstall-et-al-1980-hope.md) combines disjoint
   user-defined constructors, parametric datatype constructors, recursive
   pattern equations, higher-order iterators, and hidden representations.
2. [The Definition of Standard ML](../30-sources/milner-et-al-1997-definition-standard-ml.md)
   makes fresh nominal identity, recursive scope, constructor schemes,
   constructor status, ordered matching, and abstraction formally precise.
3. Compare both with the synthesis's proposed uniform-result ordinary ADT
   calculus and transparent-versus-abstract module interface.

### From recursive shape to reasoning

1. [Burstall 1969](../30-sources/burstall-1969-structural-induction.md)
   derives proof cases from finite constructor-built structure and explains
   the well-founded constituent relation.
2. [Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire](../30-sources/meijer-et-al-1991-functional-programming-bananas.md)
   develops folds, unfolds, and fusion laws from positive recursive datatype
   fixed points.
3. Separate ordinary recursive matching from checked structural termination,
   positive regular derivation, nested recursion, cyclic graphs, and codata.

### Make pattern matching total and useful

1. [Warnings for Pattern Matching](../30-sources/maranget-2007-warnings-pattern-matching.md)
   reduces exhaustiveness and redundancy to usefulness over typed pattern
   matrices and generates missing-case witnesses.
2. Extend that route with explicit rules for empty types, guards, visible and
   hidden constructors, open variant rows, or-patterns, and later GADT
   equalities.
3. Keep semantic coverage independent of the backend's decision-tree or
   backtracking match compilation.

### Preserve abstraction

1. HOPE demonstrates that modules can hide algebraic constructors and expose
   invariant-preserving operations.
2. [Reynolds 1983](../30-sources/reynolds-1983-types-abstraction-parametric-polymorphism.md)
   supplies the representation-independence foundation for abstract types and
   uniform clients.
3. [Views](../30-sources/wadler-1987-views-pattern-matching.md) attempts to
   recover pattern-shaped interfaces without exposing the concrete
   representation.
4. Begin with smart constructors and ordinary observers; evaluate views only
   after specifying conversion totality, effects, cost, coverage, and trust.

### Separate semantics from representation

1. [Unboxed Objects and Polymorphic Typing](../30-sources/leroy-1992-unboxed-objects.md)
   uses typed coercions to combine specialized representation with uniform
   polymorphic and abstract boundaries.
2. Evaluate tags, boxes, niches, payload packing, wrapper erasure, recursion
   indirection, GC metadata, and debugging behind a layout-opaque source type.
3. Treat stable native ABI, foreign ABI, and wire schema as explicit contracts
   rather than accidental consequences of constructor syntax.

### Keep extension mechanisms distinct

1. [A Polymorphic Type System for Extensible Records and Variants](../30-sources/gaster-jones-1996-extensible-records-variants.md)
   gives structural open variants a row-and-lacks-predicate account different
   from closed nominal families.
2. [Simple Unification-Based Type Inference for GADTs](../30-sources/peyton-jones-et-al-2006-gadt-inference.md)
   shows how refined constructor results introduce scoped type equalities and
   an annotation discipline.
3. [OutsideIn(X)](../30-sources/vytiniotis-et-al-2011-outsidein.md) gives the
   broader implication-constraint architecture for local assumptions.
4. Preserve ordinary ADTs as the principal fragment; require explicit
   conversions for row variants and an explicit checked boundary for GADTs.

### Derive lawful categorical structure

1. Follow the ADT synthesis's positivity, variance, regularity, and
   traversal-order
   conditions for `Setoid`, `Ord`, `Functor`, `Bifunctor`, `Foldable`,
   `Traversable`, and folds.
2. [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
   distinguishes constructor elimination, recursive catamorphisms, element
   folds, effectful traversals, early-stopping iteration, and advanced schemes.
3. [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
   supplies the laws and evidence boundary for Catena's initial hierarchy.
4. [The combinator inquiry](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
   tests generated operations, execution contracts, focused libraries, and
   representative use.
5. [The categorical hierarchy inquiry](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
   asks how derived dictionaries interact with kinding, coherence, testing,
   and optimizer trust.

## Open questions

- Should the first declaration checker accept negative and nested recursive
  payloads without derivation, or begin with positive regular recursion only?
- What terminating inhabitation analysis is precise enough for empty and
  recursively empty datatype coverage?
- Are non-exhaustive matches always errors, and is any explicit partial escape
  hatch worth having outside unsafe code?
- Does the first module system need separate construct and match visibility,
  or are transparent and abstract datatype signatures sufficient?
- Which view or pattern-synonym semantics can preserve abstraction without
  effect, coverage, evaluation-count, or cost surprises?
- Which derived instances are canonical, and how are laws, constraints, field
  order, and constructor precedence exposed? The
  [specification and governance map](language-integrated-specifications-and-governance.md)
  develops typed invariant, property, evidence, and evolution records.
- Which datatype shapes justify generated eliminators, maps, folds,
  traversals, unfolds, optics, and recursion schemes, and which should remain
  explicit library code?
- What source and binary evolution rules follow from closed matching,
  `non_exhaustive` markers, derived ordering, and explicit layout schemas?
- Where should explicit conversion connect nominal ADTs and structural open
  variants?
- What smallest GADT annotation boundary preserves predictable errors and
  ordinary HM behavior for programs that do not use refinements?
- Do `variant type`, `variant`, `payload`, and `match` communicate the ADT model
  accurately without hiding derivation, coverage, or representation costs?

Track experiments and resolution criteria in
[How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md).
The public terminology and derivation diagnostics are tested in
[How Should Catena Expose Mathematical Structure Without Mathematical Jargon?](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md).
