---
title: "Which Categorical Abstractions Should Catena Expose?"
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
  - "Catena categorical abstractions inquiry"
  - "How much category theory should Catena expose?"
---

# Which Categorical Abstractions Should Catena Expose?

## Why this matters

Category theory offers Catena several different things: a semantic model for
typed functions, reusable interfaces for mapping and sequencing, canonical
folds for datatypes, composable data accessors, and possible alternate compiler
interpretations. Treating all of these as one “category theory feature” would
either underuse the theory or flood the language with vocabulary.

The [category-theory synthesis](../20-notes/category-theory-for-programming.md)
proposes a narrow policy: make the basic composition structures direct, ship a
small functor/applicative/monad/traversable library, derive common datatype
operations, and leave arrows, comonads, profunctor optics, generalized
recursion schemes, and categorical compilation to evidence-driven libraries or
experiments.

That boundary is provisional. It has not yet been tested against a Catena
inferencer, real library corpus, operational semantics, or compiler. In
particular, higher-kinded traits and convenient law notation may interact with
the principality and coherence goals of the
[greenfield type system](../20-notes/catena-greenfield-type-system.md).

This inquiry is independent of any Catena repository outside this archive.

## Operational question

Can one Catena prototype and representative library corpus establish all of
the following?

- A rigid higher-kinded kind `Type -> Type` permits principal rank-1 inference
  for the intended `Functor`, `Applicative`, `Monad`, and `Traversable` uses.
- Coherent, non-overlapping trait evidence selects one instance without making
  explicit alternate interpretations awkward.
- Code can state the weakest required interface, and doing so exposes useful
  static information or reuse compared with accepting `Monad` everywhere.
- Law declarations have an explicit evidence status—promised, tested, derived,
  trusted, or proved—and ordinary user laws cannot cause unsound optimization.
- The pure fragment has a relational parametricity theorem strong enough to
  justify the naturality and free-theorem claims exposed by tooling.
- Datatype-derived `map`, `fold`, and `traverse` reject unsupported shapes with
  source-level explanations and preserve a documented order and strictness.
- Native algebraic effects and explicit monadic data coexist without two
  competing, implicit meanings of sequencing.
- A generated concrete optic API handles ordinary field and variant access;
  a profunctor representation is added only if mixed composition proves a
  material advantage.
- One categorical-IR experiment preserves source results and source locations
  without turning target-specific constraints into the dominant programming
  model.
- Every algebraic interface has a separate operational contract for evaluation
  order, effects, concurrency, allocation, and stack behavior.

“Establish” means more than compiling demonstrations. It requires a declarative
typing judgment, inference and elaboration rules, law-evidence semantics,
executable reference implementations, differential/property tests, diagnostic
snapshots, and measurements on the agreed corpus.

## Working hypotheses

1. **The pure typed core should embody categorical structure without naming
   it.** Functions, composition, products, sums, unit, empty types, and
   algebraic data cover the broadly useful part.
2. **Rigid higher-kinded parameters are sufficient for the initial hierarchy.**
   General type-level lambdas and reduction are not needed to express the
   target interfaces and would weaken inference and termination guarantees.
3. **`Functor`, `Applicative`, `Monad`, and `Traversable` form the smallest
   defensible standard layer.** The hierarchy should preserve weaker
   constraints rather than making `Monad` the default effect abstraction.
4. **Laws should begin as documentation, reusable property tests, and trusted
   compiler derivations.** Optimizer use of arbitrary user-declared equations
   should require explicit trusted or proof-carrying evidence.
5. **Parametricity should be stated for a delimited fragment.** General
   recursion, runtime type analysis, unsafe casts, effects, and foreign calls
   must not silently inherit free-theorem claims.
6. **Datatype derivation should be constructor oriented.** Category theory
   justifies the operators, but public signatures and diagnostics should use
   ordinary `map`, constructor cases, and traversal order.
7. **Monads complement native effects.** They are appropriate when a
   computation is explicit data to inspect or interpret; direct operations and
   handlers are appropriate for native effect requests.
8. **Arrows, comonads, and profunctors are library abstractions until repeated
   examples demand syntax or compiler support.** Mathematical generality alone
   is insufficient evidence.
9. **A categorical IR should remain an opt-in interpretation boundary.** It
   should not replace operational IRs that retain control flow, sharing,
   effects, and machine costs.

## Paths to explore

### Parametricity and law evidence

- Define a pure System-F-like or rank-1 fragment and prove a logical-relations
  abstraction theorem following
  [Reynolds](../30-sources/reynolds-1983-types-abstraction-parametric-polymorphism.md).
- Derive the candidate naturality equations for `map`, `traverse`, and
  polymorphic transformations using the method of
  [Wadler](../30-sources/wadler-1989-theorems-for-free.md).
- Add features one at a time—general recursion, strictness, effect rows,
  handlers, runtime type information—and record which theorem or side
  condition changes.
- Give law evidence a core representation. Confirm that property-tested laws
  cannot enter optimizer reasoning and that compiler-derived evidence is
  invalidated if the derivation algorithm changes.
- Generate counterexample instances that type-check while violating functor,
  applicative, monad, traversal, category, and optic laws.

### Higher-kinded inference and traits

- Extend the reference inferencer with rigid constructor variables and the
  four proposed single-parameter traits.
- Test partial application, explicit type application, nested applicatives,
  composed functors, and polymorphic public signatures.
- Measure ambiguous variables, required annotations, solver steps, and error
  origin quality against per-datatype functions.
- Test explicit dictionary passing for alternate validation orders or
  interpretations without enabling overlapping or local implicit instances.
- Determine whether `Traversable T` is expressible as a single-parameter trait
  under the proposed system without hidden multi-parameter constraints.

### Weakest adequate abstraction corpus

Build paired implementations of:

- accumulating configuration validation;
- parser descriptions with static and value-dependent grammars;
- independent and dependent query plans;
- AST analyses and effectful rewrites;
- resource-safe workflows;
- streaming/dataflow transforms; and
- serializable deployment plans.

For each pair, compare `Applicative` with `Monad`, ordinary functions with
`Arrow`, and direct effects with explicit monadic data. Record what static
information, generic code, or optimization each weaker interface actually
enables.

### Datatypes and recursion

- Formalize which positive regular datatype declarations determine a functor
  and traversal.
- Cover nested, mutually recursive, phantom, invariant, negative, and
  nonuniform parameters with explicit accept/reject examples.
- Compare generated constructor-oriented folds with a public fixed-point and
  recursion-schemes library based on
  [Meijer, Fokkinga, and Paterson](../30-sources/meijer-et-al-1991-functional-programming-bananas.md).
- Specify traversal order, stack behavior, strictness, sharing, and exception
  timing.
- Differentially test any fusion rule under pure values, divergence, abortive
  effects, mutation, and large inputs.

### Optics

- Generate concrete field lenses and variant prisms, including readable
  getter/update APIs and their laws.
- Implement the same mixed field/variant/traversal examples using
  [profunctor optics](../30-sources/pickering-et-al-2017-profunctor-optics.md).
- Compare type signatures, error size, compile time, runtime specialization,
  discoverability, and ability to compose different optic kinds.
- Do not choose the profunctor representation unless the mixed-composition
  advantage survives those measurements.

### Categorical compilation

- Translate a deliberately small pure Catena fragment to cartesian or
  cartesian-closed combinators following
  [Elliott](../30-sources/elliott-2017-compiling-to-categories.md).
- Choose one target with a clear oracle, such as forward automatic
  differentiation or interval interpretation.
- Test functions, products, sums, sharing, recursion rejection, source maps,
  and target capability errors.
- Compare against a conventional dedicated IR for implementation effort,
  generated code, diagnostics, and extension by a third-party target.

### Operational contracts

- Define a standard documentation schema for law, evaluation order,
  strictness, effect order, concurrency, complexity, allocation, and stack
  safety.
- Connect reordering permission to effect rows, capability disjointness, or an
  explicit commutativity proof; never infer it from `Applicative` alone.
- Reconcile monadic sequencing with the lexical capability and affine
  resumption design in the
  [algebraic-effect inquiry](which-algebraic-effect-semantics-should-catena-adopt.md).

## Findings

The literature establishes several boundaries that the prototype should treat
as prior evidence:

- [Lambek](../30-sources/lambek-1972-deductive-systems-categories-iii.md)
  supports a structural semantics for the simply typed pure core, but not its
  operational cost or a full effectful language.
- [Reynolds](../30-sources/reynolds-1983-types-abstraction-parametric-polymorphism.md)
  and [Wadler](../30-sources/wadler-1989-theorems-for-free.md) make uniformity a
  semantic premise for naturality claims; polymorphic notation alone is not
  enough.
- [McBride and Paterson](../30-sources/mcbride-paterson-2008-applicative-programming-effects.md)
  demonstrate that fixed computation structure is useful and strictly weaker
  than monadic dependency. They do not authorize parallel effects.
- [Moggi](../30-sources/moggi-1991-notions-computation-monads.md) and
  [Wadler](../30-sources/wadler-1995-monads-functional-programming.md) justify
  monadic computation as both semantics and program structure, without making
  it the sole user-facing effect mechanism.
- [Hughes](../30-sources/hughes-2000-generalising-monads-arrows.md) and
  [Uustalu and Vene](../30-sources/uustalu-vene-2005-essence-dataflow-programming.md)
  show real computations outside the ordinary monadic-library interface, but
  their specialized case studies do not justify core syntax.
- [Pickering, Gibbons, and Wu](../30-sources/pickering-et-al-2017-profunctor-optics.md)
  prove useful representation equivalences for composable optics; ergonomic
  and specialization evidence remains language dependent.
- [Elliott](../30-sources/elliott-2017-compiling-to-categories.md) demonstrates
  modular alternate interpretation in a compiler plugin; production coverage
  and operational integration remain open.

No local prototype evidence exists yet. The synthesis is therefore a design
hypothesis, not a resolved Catena feature set.

## Outcome

Open. Resolve this inquiry only after the prototype artifacts establish which
abstractions improve real Catena programs and after the type-system,
parametricity, law-evidence, and operational contracts agree. Promote settled
language and library decisions into the
[category-theory synthesis](../20-notes/category-theory-for-programming.md) and
link the evidence through the
[Category Theory for Programming map](../10-maps/category-theory-for-programming.md).
