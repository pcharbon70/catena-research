---
title: "How Should Catena Specify Its Initial Categorical Hierarchy?"
kind: inquiry
created: "2026-07-31"
status: open
tags:
  - category-theory
  - catena
  - language-design
  - parametricity
  - trait-constraints
aliases:
  - "Which Categorical Abstractions Should Catena Expose?"
  - "Catena categorical abstractions inquiry"
  - "Catena initial type-class hierarchy inquiry"
---

# How Should Catena Specify Its Initial Categorical Hierarchy?

## Why this matters

The membership question is settled for the initial Catena standard library.
It will contain `Semigroupoid`, `Category`, `Arrow`, `Semigroup`, `Monoid`,
`Setoid`, `Ord`, `Foldable`, `Functor`, `Traversable`, `Apply`, `Applicative`,
`Chain`, `Monad`, `Bifunctor`, `Extend`, and `Comonad`.

What remains open is whether these names can be turned into one precise,
lawful, inferable, and operationally honest design. The
[category-theory synthesis](../20-notes/category-theory-for-programming.md)
defines the intended hierarchy and programming roles. This inquiry tests its
kinds, method sets, parent relationships, evidence semantics, instance rules,
derivation support, diagnostics, and runtime contracts.

The breadth of the starting set makes this work more important, not less.
Several pairs deliberately separate an associative operation from its unit:
`Semigroup`/`Monoid`, `Semigroupoid`/`Category`, `Apply`/`Applicative`,
`Chain`/`Monad`, and `Extend`/`Comonad`. `Bifunctor` and the arrow branch also
operate at a different kind from ordinary unary constructor classes. A loose
translation of names into traits could therefore create incoherent parents,
ambiguous methods, or solver behavior that undermines the
[greenfield type-system guarantees](what-should-a-greenfield-catena-type-system-guarantee.md).

This inquiry is independent of any Catena repository outside this archive.

## Operational question

Can a Catena calculus, reference implementation, and representative corpus
establish all of the following?

- The class parameters have explicit kinds: value classes consume `Type`,
  unary constructor classes consume `Type -> Type`, and `Bifunctor`,
  `Semigroupoid`, `Category`, and `Arrow` consume
  `Type -> Type -> Type`.
- The type system supports those rigid constructor variables while retaining
  principal rank-1 inference for ordinary use and terminating trait solving.
- `Bifunctor` has unambiguous two-position mapping and derived `map_first` and
  `map_second`; it does not fake inheritance from one unspecified unary
  `Functor` view.
- Every class has one canonical minimal method set, named laws, standard
  derived operations, and a documented relationship to its parents.
- Multiple parents share one coherent ancestor dictionary. In particular,
  the `Apply` inherited through `Applicative` agrees with the one inherited
  through `Chain` in a `Monad`.
- The unitless classes admit useful lawful instances and let APIs express a
  genuinely weaker requirement than their unit-bearing descendants.
- Coherent, non-overlapping evidence selects one implicit instance while
  wrappers or explicit dictionaries support alternate monoids, orders, and
  evaluation policies.
- Law declarations distinguish promised, tested, compiler-derived, trusted,
  and proved evidence; ordinary user promises cannot authorize optimizer
  rewrites.
- `Setoid` and `Ord` state their coherence with hashing, pattern matching,
  exceptional floating-point values, and partial orders without conflating
  those separate concepts.
- `Foldable` and `Traversable` specify element cardinality, visitation order,
  multiplicity, strictness, short-circuiting, and stack behavior. Derived
  traversal visits each position exactly once by construction.
- `Apply`, `Applicative`, `Chain`, `Monad`, `Arrow`, `Extend`, and `Comonad`
  keep equational laws separate from evaluation order, concurrency,
  cancellation, allocation, and native effect behavior.
- Derived instances reject unsupported datatype variance or recursion with
  source-level explanations and produce evidence tied to a versioned
  derivation algorithm.

“Establish” requires declarative kinding and typing judgments, inference and
elaboration rules, executable class dictionaries, law and diagnostic tests,
representative instances, and measurements. Compiling one example per class
is not enough.

## Working hypotheses

1. **The hierarchy should be kind-indexed rather than linear.** Value, unary
   constructor, and binary constructor classes form related branches but do
   not share one uniform parameter shape.
2. **The unitless classes are first-class constraints.** They should not be
   aliases or undocumented fragments of their stronger descendants.
3. **Minimal definitions and derived operations should be canonical.** One
   primitive set per class reduces law ambiguity and keeps instance authors
   from supplying operations that silently disagree.
4. **Superclass diamonds require evidence sharing and compatibility laws.** A
   `Monad` should elaborate to compatible `Applicative`, `Chain`, `Apply`, and
   `Functor` views rather than unrelated dictionaries that merely have the
   same types.
5. **Class laws and operational contracts are distinct.** Associativity does
   not imply reordering, and applicative shape does not imply concurrency.
6. **Rigid higher-kinded parameters should be sufficient.** The initial set
   should not require unrestricted type lambdas, arbitrary type-level
   reduction, or higher-rank inference.
7. **Global coherence should be the implicit default.** Alternate algebraic
   meanings should use explicit wrappers or dictionaries, especially for
   numeric monoids and domain-specific equivalences or orders.
8. **Datatype derivation should cover only structurally justified instances.**
   Positivity, variance, field order, and recursion shape determine what can
   be generated; a requested name does not make the instance lawful.
9. **The classes should remain library interfaces.** Their initial inclusion
   does not require specialized syntax or optimizer trust.

## Paths to explore

### Specify the class kernel

- Write kinded declarations for all seventeen classes and make every inherited
  dictionary path explicit.
- Define canonical primitives and derived operations, including comparison
  predicates, monoidal folds, `map_first`, `map_second`, contextual product,
  `join`, arrow product operations, and coKleisli composition.
- State each law over Catena's equality relation and record the purity,
  totality, and extensionality assumptions required by that equality.
- Test parent compatibility separately from each parent's internal laws.
- Decide whether classes with no new `Monad` primitive are represented as
  conjunctions, marker dictionaries, or dictionaries containing canonical
  derived operations.

### Test kinding, inference, and elaboration

- Extend the reference inferencer with rigid variables of kinds `Type -> Type`
  and `Type -> Type -> Type` plus kind-correct partial application.
- Exercise every class alone, every parent edge, the `Monad` diamond,
  `Traversable`'s two parents, and `Bifunctor` mappings in both positions.
- Measure inferred constraints, ambiguous variables, annotations, solver
  steps, compile time, and error origin quality against direct per-datatype
  functions.
- Elaborate implicit constraints to explicit dictionaries and verify that all
  paths to a shared parent reuse the same evidence.
- Test explicit alternate dictionaries without enabling overlapping local
  implicit instances.

### Build an instance and API corpus

- Cover lists, nonempty collections, optional values, results, validation,
  trees, functions, parsers, query plans, streams, environments, stateful
  contexts, and typed pipelines.
- Require at least two meaningful consumers of each unitless class. Record
  whether weakening a constraint improves applicability, testing, static
  analysis, or instance coverage.
- Include intentionally unlawful instances for every class and verify that
  generated property suites find useful counterexamples.
- Exercise multiple lawful structures on one representation through wrappers,
  including additive/multiplicative numbers and first/last selection.
- Compare class-constrained APIs with direct functions for discoverability,
  signatures, diagnostics, and runtime specialization.

### Prove and test laws at explicit trust levels

- Follow [Wadler and Blott](../30-sources/wadler-blott-1989-ad-hoc-polymorphism.md)
  to give constrained polymorphism an evidence-passing interpretation.
- Use [Reynolds](../30-sources/reynolds-1983-types-abstraction-parametric-polymorphism.md)
  and [Wadler](../30-sources/wadler-1989-theorems-for-free.md) to delimit which
  functorial or naturality results follow from uniform polymorphism.
- Give promised, tested, derived, trusted, and proved laws distinct core
  representations and permissions.
- Generate law suites from declarations, including higher-order function
  generators and shrinkers, while treating test success as evidence rather
  than proof.
- Differentially test any compiler use of laws under strictness, divergence,
  exceptions, native effects, sharing, and resource cleanup.

### Define operational contracts

- Use the focused
  [combinator inquiry](which-combinators-should-catena-provide-and-derive.md)
  to turn minimal class methods into a derived API while keeping law,
  evaluation, effect, and cost claims separate.
- Specify left-to-right or other evaluation order for contextual application,
  sequencing, traversal, folds, arrow products, and extension.
- State complexity, allocation, stack safety, laziness or strictness, early
  termination, cancellation, and concurrency separately from algebraic laws.
- Connect reordering or parallelism to explicit commutativity and effect
  evidence, never to `Applicative` or `Monoid` alone.
- Reconcile explicit `Monad` values with the direct effect-and-handler model in
  the [algebraic-effect inquiry](which-algebraic-effect-semantics-should-catena-adopt.md).

### Derive structural instances

- Formalize how variance, positive occurrence, regular recursion, field order,
  and phantom parameters permit or reject `Functor`, `Bifunctor`, `Foldable`,
  and `Traversable` derivation.
- Specify how `Setoid`, `Ord`, `Semigroup`, and `Monoid` derivations select and
  order fields, and reject declarations without a canonical structure.
- Guarantee exact-once, shape-preserving traversal for compiler-derived
  instances, using the iterator analysis of
  [Gibbons and Oliveira](../30-sources/gibbons-oliveira-2009-essence-iterator-pattern.md).
- Version generated evidence and invalidate optimizer trust when the
  derivation algorithm or relevant operational contract changes.

## Findings

The literature already establishes several boundaries for the prototype:

- [Wadler and Blott](../30-sources/wadler-blott-1989-ad-hoc-polymorphism.md)
  justify type classes as constrained polymorphism elaborated through
  evidence. They do not settle Catena's kind system, coherence policy, or
  operational semantics.
- [The algebraic interface specification](../30-sources/fantasy-land-algebraic-specification.md)
  supplies exact weak/strong splits, parent relations, operations, and laws
  for the selected vocabulary. Its dynamically typed structural inheritance
  needs a kind-aware Catena translation, especially for `Bifunctor`.
- [Rivas and Jaskelioff](../30-sources/rivas-jaskelioff-2017-notions-computation-monoids.md)
  explain why monoids, applicatives, monads, and arrows share a monoidal
  pattern while living in different categories. This supports a connected
  hierarchy without collapsing distinct interfaces.
- [McBride and Paterson](../30-sources/mcbride-paterson-2008-applicative-programming-effects.md)
  establish the programming value of fixed computational shape, but
  applicative laws alone do not authorize concurrent execution.
- [Gibbons and Oliveira](../30-sources/gibbons-oliveira-2009-essence-iterator-pattern.md)
  connect traversal with mapping and accumulation and show why the familiar
  laws need a construction or additional condition to exclude bogus
  traversals.
- [Hughes](../30-sources/hughes-2000-generalising-monads-arrows.md) and
  [Uustalu and Vene](../30-sources/uustalu-vene-2005-essence-dataflow-programming.md)
  provide concrete programming roles for the arrow and comonadic branches.

No local prototype evidence exists yet. The set of initial classes is fixed,
but its exact specification remains a design hypothesis.

## Outcome

Open. Resolve this inquiry when the seventeen classes have kinded declarations,
law and compatibility suites, explicit operational contracts, a coherent
evidence elaboration, representative instances, derivation rules, and measured
inference and diagnostic results. Promote the resulting language and library
contract into the
[category-theory synthesis](../20-notes/category-theory-for-programming.md)
and retain unresolved implementation experiments here.
