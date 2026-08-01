---
title: "Combinators for Algebraic Data and Categorical Programming"
kind: map
created: "2026-08-01"
tags:
  - algebraic-data-types
  - category-theory
  - catena
  - combinator-libraries
  - language-design
aliases:
  - "Combinators research map"
  - "ADT and categorical combinators map"
---

# Combinators for Algebraic Data and Categorical Programming

## Scope

This map routes through combinators as source-level glue for functions,
products, sums, algebraic datatypes, categorical classes, and focused domain
libraries. It also preserves the boundary between public library combinators
and combinator-based compiler representations.

## Start here

- [Combinators for Algebraic Data and Categorical Programming](../20-notes/combinators-for-algebraic-data-and-categorical-programming.md)
  is the main synthesis and proposed layered Catena vocabulary.
- [Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md)
  turns the proposal into law, derivation, execution, library, corpus, and
  compiler experiments.
- [Algebraic Data Types](../20-notes/algebraic-data-types.md) defines the
  constructor, matching, derivation, abstraction, and representation boundary.
- [Category Theory for Programming](../20-notes/category-theory-for-programming.md)
  defines the agreed seventeen-class hierarchy and its evidence policy.

## Trails

### Understand combinators as program glue

1. [Why Functional Programming Matters](../30-sources/hughes-1989-why-functional-programming-matters.md)
   argues that higher-order functions and lazy producer/consumer boundaries
   are modularity mechanisms, not merely concise notation.
2. [Lambek 1972](../30-sources/lambek-1972-deductive-systems-categories-iii.md)
   gives composition and identity their proof-theoretic and categorical
   setting.
3. Keep source combinators distinct from the variable-free compiler basis in
   [Turner 1979](../30-sources/turner-1979-applicative-language-implementation.md)
   and the categorical compilation proposal in
   [Elliott 2017](../30-sources/elliott-2017-compiling-to-categories.md).

### Route functions through products and sums

1. Begin with identity, composition, currying, pairing, projections, and sum
   elimination as ordinary typed functions.
2. Use [Reynolds 1983](../30-sources/reynolds-1983-types-abstraction-parametric-polymorphism.md)
   and [Wadler 1989](../30-sources/wadler-1989-theorems-for-free.md) to test
   which uniform behaviors follow from polymorphic types.
3. Separate pure structural equations from evaluation order, callback
   multiplicity, effects, strictness, and cost.

### Derive consumers from algebraic data

1. [Böhm and Berarducci 1985](../30-sources/bohm-berarducci-1985-typed-lambda-programs.md)
   represents term algebras through typed constructor eliminators.
2. [Burstall 1969](../30-sources/burstall-1969-structural-induction.md)
   connects finite constructor structure to induction.
3. [Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire](../30-sources/meijer-et-al-1991-functional-programming-bananas.md)
   derives catamorphisms, anamorphisms, hylomorphisms, and fusion for recursive
   fixed points.
4. Distinguish a constructor-complete eliminator, a recursive catamorphism,
   and a `Foldable` element reduction; all are called “fold” in practice but
   have different inputs, laws, and costs.

### Build the seventeen-class derived vocabulary

1. Use the exact hierarchy in
   [Category Theory for Programming](../20-notes/category-theory-for-programming.md):
   `Setoid`, `Ord`, `Semigroup`, `Monoid`, `Foldable`, `Functor`, `Bifunctor`,
   `Apply`, `Applicative`, `Traversable`, `Chain`, `Monad`, `Semigroupoid`,
   `Category`, `Arrow`, `Extend`, and `Comonad`.
2. [Semigroups and Monoids](../30-sources/rivas-jaskelioff-2017-notions-computation-monoids.md)
   clarifies when associative combination is value algebra rather than effect
   sequencing.
3. [Applicative Programming with Effects](../30-sources/mcbride-paterson-2008-applicative-programming-effects.md)
   separates fixed effectful structure from value-dependent sequencing.
4. [Notions of Computation and Monads](../30-sources/moggi-1991-notions-computation-monads.md)
   and [Monads for Functional Programming](../30-sources/wadler-1995-monads-functional-programming.md)
   ground monadic sequencing and Kleisli composition.
5. [The Essence of the Iterator Pattern](../30-sources/gibbons-oliveira-2009-essence-iterator-pattern.md)
   connects traversal to applicative effects, while strict early termination
   still requires an operational protocol.
6. Use the [categorical hierarchy inquiry](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md)
   to test minimal dictionaries, parent coherence, law evidence, and instance
   inference.

### Express computational dependency without collapsing abstractions

1. Choose the weakest constraint among `Apply`, `Applicative`, `Chain`, and
   `Monad` that expresses the actual data dependency.
2. Use `traverse` for effectful structure-preserving visits; keep categorical
   `map` pure unless an explicit effectful API states otherwise.
3. [Selective Applicative Functors](../30-sources/mokhov-et-al-2019-selective-applicative-functors.md)
   studies analyzable conditional dependency between applicative and monadic
   interfaces; keep it outside the initial hierarchy pending a Catena
   prototype.
4. [Generalising Monads to Arrows](../30-sources/hughes-2000-generalising-monads-arrows.md)
   exposes static routing for computations whose source language cannot treat
   them as ordinary functions.
5. [Comonads and Dataflow Programming](../30-sources/uustalu-vene-2005-essence-dataflow-programming.md)
   supplies context-dependent extension and coKleisli composition.

### Test focused domain libraries

1. [Monadic Parsing in Haskell](../30-sources/hutton-meijer-1998-monadic-parsing.md)
   demonstrates parsers assembled through pure, bind, failure, choice, item,
   repetition, and token-level combinators; specify modern consumption,
   commitment, error, progress, and backtracking contracts separately.
2. [Profunctor Optics](../30-sources/pickering-et-al-2017-profunctor-optics.md)
   unifies optic composition; begin by testing concrete generated lenses and
   prisms before adopting the most general representation.
3. [Data Types à la Carte](../30-sources/swierstra-2008-data-types-a-la-carte.md)
   combines functor components, coproducts, fixed points, folds, and injection
   for modular syntax; prototype explicit coherent injection evidence.
4. Keep validation accumulation distinct from fail-fast result sequencing with
   named wrappers, and keep explicit computation values available when
   inspection or alternate interpretation is itself the goal.

### Evaluate combinators as compiler IR separately

1. [Turner 1979](../30-sources/turner-1979-applicative-language-implementation.md)
   eliminates variables by bracket abstraction into a combinator basis.
2. [Elliott 2017](../30-sources/elliott-2017-compiling-to-categories.md)
   proposes categorical compilation as a route to alternative semantic
   domains and optimizations.
3. Compare either representation with Catena's ordinary typed core on
   translation correctness, effects, code size, simplification, proof burden,
   source mapping, diagnostics, and runtime performance.

## Open questions

- What exact purity and effect-row contract belongs on every higher-order class
  method and derived combinator, and which evidence method can support each
  claim? Follow the
  [specification and governance map](language-integrated-specifications-and-governance.md).
- Which derived functions materially improve real programs without enlarging
  the law-bearing dictionaries?
- Should early termination use `fold_while`, a pull iterator, an effect, or a
  combination of protocols?
- Which ADT shapes justify automatic `map`, `bimap`, `fold_map`, `traverse`,
  unfold, and recursion-scheme generation?
- How should generated combinators expose constructor order, field order,
  constraints, stack behavior, and code provenance?
- Which operator aliases remain readable when category, parser, optic, and
  effect libraries are imported together?
- Can concrete optics and explicit modular-syntax injection meet ordinary
  needs before more encoded generic interfaces are introduced?
- Does a selective prototype improve static dependency analysis enough to
  justify changing the agreed hierarchy?
- How should explicit computation descriptions interoperate with direct
  algebraic handlers and effect rows?
- Does a combinatory or categorical compiler IR improve optimization enough to
  pay for its translation, proof, debugging, and diagnostic costs?
- Can programmers reliably choose `map`, `map2`, `and_then`, and `collect_map`
  from dependency shape without first learning the formal class names?

Track experiments and resolution criteria in
[Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md).
Vocabulary prediction and transfer are tracked in
[How Should Catena Expose Mathematical Structure Without Mathematical Jargon?](../40-inquiries/how-should-catena-expose-mathematical-structure-without-mathematical-jargon.md).
