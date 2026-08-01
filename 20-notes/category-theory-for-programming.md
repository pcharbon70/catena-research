---
title: "Category Theory for Programming"
kind: note
created: "2026-07-31"
maturity: developing
tags:
  - category-theory
  - catena
  - functional-programming
  - language-design
  - program-semantics
aliases:
  - "Category theory applied to programming"
  - "A categorical design vocabulary for Catena"
---

# Category Theory for Programming

## Executive conclusion

Category theory contributes to programming when it identifies **what composes,
which structure composition preserves, and which equations make the
composition predictable**. Its most useful programming applications are not
analogies. They are reusable interfaces and semantic correspondences:

- typed functions form the motivating category of programs, with identity and
  composition;
- products, sums, and functions are characterized by universal properties,
  giving a structural account of algebraic data and higher-order code;
- functors describe uniform mapping over structure, while natural
  transformations describe representation-independent conversions;
- applicatives, monads, comonads, and arrows distinguish different shapes of
  computational dependency;
- initial algebras and final coalgebras explain datatype folds and unfolds;
- profunctors give lenses, prisms, and traversals a common composition
  language; and
- a typed lambda term can sometimes be translated into categorical
  combinators and interpreted as a circuit, derivative, incremental program,
  analysis, or other domain-specific target.

These benefits come with a strict boundary. Category theory is deliberately
insensitive to internal representation. That is precisely why it supports
abstraction, but it also means the structure alone does **not** determine:

- evaluation order, strictness, termination, or behavior at bottom;
- allocation, asymptotic complexity, locality, or parallel speedup;
- whether a programmer-defined instance obeys its advertised laws;
- which effects may be reordered or run concurrently;
- resource lifetime, cancellation, exception cleanup, or foreign calls; or
- whether categorical vocabulary produces an understandable public API.

For a greenfield Catena, category theory should therefore be a design and
verification vocabulary, not a surface-language theme. The initial language
should make composition easy; provide products, sums, functions, algebraic
data, higher-kinded parameters, and coherent traits; derive common structural
operations from datatypes; and expose laws as documented and testable
contracts. It should **not** grant compiler optimizations merely because an
instance is named `Functor` or `Monad`, nor add arrows, comonads, profunctor
optics, recursion-scheme syntax, or categorical compilation before concrete
libraries prove the need.

The practical rule is:

> Choose the weakest lawful structure that expresses the program, preserve
> the static information that structure exposes, and specify operational cost
> separately.

This is a fresh synthesis for the language imagined in this archive. It does
not use a Catena specification, implementation, or summary from another
repository.

## Scope, method, and decision standard

This note asks three questions:

1. What does category theory say precisely about typed programs?
2. Which categorical structures have demonstrated programming uses?
3. Which of those structures should affect Catena's core, standard library,
   derivation system, compiler, or only its research agenda?

The evidence base is a set of primary papers spanning categorical semantics,
parametricity, functional program calculation, computational effects,
combinator libraries, dataflow, optics, and compiler interpretation. Formal
papers establish correspondences and laws under stated assumptions. Example-
driven papers establish expressibility and architectural leverage. Neither
kind, by itself, establishes usability or runtime performance.

A categorical abstraction earns a place in Catena only when all of the
following can be supplied:

- **Concrete problem:** at least two credible libraries need the same
  composition pattern.
- **Minimal interface:** each operation is necessary for those examples.
- **Named laws:** equations are stated with evaluation and effect assumptions.
- **Evidence boundary:** the language says whether laws are proved, derived,
  checked, tested, or merely promised.
- **Coherent resolution:** one visible type does not silently select observably
  different dictionaries.
- **Operational contract:** order, strictness, concurrency, failure, and cost
  are specified separately from extensional laws.
- **Diagnostics:** errors refer to the programmer's abstraction and source
  expression, not only to an elaborated categorical term.
- **Measured benefit:** genericity, analyzability, optimization, or API
  composition is demonstrated against a simpler design.

This standard intentionally rejects “it is a well-known category” as a
language-design argument.

## The minimum categorical model

### A category is typed composition

A category has:

- objects `A`, `B`, and `C`;
- arrows `f : A -> B`;
- an identity `id_A : A -> A`; and
- composition `g ∘ f : A -> C` when `f : A -> B` and `g : B -> C`.

The equations are:

```text
id ∘ f = f
f ∘ id = f
h ∘ (g ∘ f) = (h ∘ g) ∘ f
```

For programming, types can play the role of objects and pure total functions
the role of arrows. The type checker enforces the boundary at which
composition is defined. Associativity then lets a pipeline be regrouped
without changing its extensional result.

This simple account already exposes a caveat. Real programs may diverge,
throw, inspect representations, allocate, or perform I/O. A language with
general recursion is not literally the category of sets and total functions.
One can build categories with partial maps, domains, relations, Kleisli
arrows, or other morphisms, but the selected category is part of the semantic
claim. “Types are objects and functions are arrows” is a useful entry point,
not a completed model of a production language.

### Structure is specified by observations, not representation

The categorical contribution begins when a construction is characterized by
how every other program interacts with it.

For products, projections and pairing satisfy:

```text
fst : A * B -> A
snd : A * B -> B

pair(f, g) : X -> A * B
fst ∘ pair(f, g) = f
snd ∘ pair(f, g) = g
```

`pair(f, g)` is the unique arrow with those two observations. A product is
therefore not “some object with two fields”; it is an object satisfying this
universal mapping property. The same distinction matters in programming:
two layouts may implement the same product interface while having different
costs.

The corresponding structures are:

| Categorical structure | Typed-programming reading | Governing observation |
| --- | --- | --- |
| Terminal object `1` | Unit type | Exactly one pure result from every type |
| Product `A * B` | Pair or record-like conjunction | Functions into it are pairs of functions |
| Initial object `0` | Empty type | Eliminates into every result type |
| Coproduct `A + B` | Sum or variant | Functions out are case analyses |
| Exponential `B^A` | Function type `A -> B` | Maps from `X * A` correspond to maps from `X` to `A -> B` |

The product/exponential correspondence is currying:

```text
(X * A -> B)  ~=  (X -> A -> B)
```

Categorically, `(- * A)` is left adjoint to `(A -> -)`. The familiar
programming operation is therefore one instance of an adjunction: a natural,
mutually inverse translation between two families of mappings.

[Lambek's correspondence](../30-sources/lambek-1972-deductive-systems-categories-iii.md)
connects these structures with typed deduction and combinatory logic. It
explains why the simply typed lambda calculus is not merely *represented by*
a cartesian closed category; its syntax and equations generate the free such
structure. Beta and eta laws express the universal relationship between
evaluation and currying.

### What this gives a language designer

Universal properties provide three kinds of leverage:

1. **Interface independence.** Code can rely on observations and equations
   rather than representation.
2. **Uniqueness reasoning.** If two programs satisfy the same universal
   characterization, they are equal in the model.
3. **Canonical operations.** Products determine pairing, sums determine case
   analysis, and datatype fixed points determine folds or unfolds.

They do not choose a syntax, memory layout, calling convention, or optimizer.
Catena should state those as separate design decisions.

## Functors and natural transformations

### A functor is structure-preserving mapping

Given categories `C` and `D`, a functor maps objects and arrows while
preserving identity and composition. In a typed library, an endofunctor-like
interface for a type constructor `F : Type -> Type` is usually presented as:

```text
trait Functor F {
  map : (A -> B) -> F A -> F B
}
```

with laws:

```text
map(id) = id
map(g ∘ f) = map(g) ∘ map(f)
```

The laws say `map` changes element values without changing the surrounding
shape or inventing additional structure. Lists, optional values, trees,
results with a fixed error type, environments, and many syntax trees admit
such a map.

The type of `map` is suggestive but insufficient. A programmer can write an
implementation that drops values, reverses a list, increments a counter, or
otherwise violates the laws if the language permits those observations. The
trait dictionary proves only that a method was supplied.

### Natural transformations are uniform conversions

A natural transformation `eta : F => G` is a family of arrows:

```text
eta_A : F A -> G A
```

that commutes with mapping:

```text
map_G(f) ∘ eta_A = eta_B ∘ map_F(f)
```

In code, the shape is often:

```text
eta : forall A. F A -> G A
```

The equation says converting then mapping is the same as mapping then
converting. It captures an API property programmers often intend by “generic
conversion”: the conversion cannot depend on the identity or representation
of `A`.

That conclusion requires parametricity. [Reynolds's abstraction
theorem](../30-sources/reynolds-1983-types-abstraction-parametric-polymorphism.md)
says a parametric term preserves relations between interpretations of its
types. [Wadler's free-theorem calculus](../30-sources/wadler-1989-theorems-for-free.md)
specializes those relations to derive useful equations from polymorphic types.
The categorical naturality law is therefore not typographic magic; it is a
semantic consequence of uniform polymorphism under the theorem's assumptions.

### The lawfulness ladder

Catena should describe evidence for a law using explicit levels:

| Evidence | What it establishes | What it does not establish |
| --- | --- | --- |
| Method type-checks | Operations have compatible input and output types | Equational laws |
| Instance author promises laws | Reviewable API contract | Truth of the promise |
| Property tests pass | Sampled behavior for selected generators | Universal validity |
| Compiler-derived instance | Correctness relative to derivation algorithm | User-written instances or operational cost |
| Parametricity theorem | A class of equations for all terms in a fragment | Laws involving non-parametric methods or excluded effects |
| Proof-carrying instance | Stated laws in the proof logic | Cost, termination, or properties absent from the statement |

An initial Catena should implement the first four levels. It may later add a
proof layer, but ordinary traits should not pretend to be proofs.

## Yoneda and adjunctions as design tools

### Yoneda asks how a value behaves under every observation

The covariant Yoneda lemma can be read schematically as:

```text
Natural(Hom(A, -), F)  ~=  F A
```

A value of `F A` is equivalent to a uniform way of turning every function
`A -> X` into an `F X`. The dual form describes a value through every
context that consumes it. This principle appears in continuation encodings,
Church encodings, difference structures, and representation theorems for
libraries such as optics.

The important engineering lesson is not to expose `Yoneda` as a fashionable
wrapper. It is to recognize when an API can replace a concrete intermediate
representation by its behavior under all consumers or producers. Such an
encoding can improve composition or fusion, but may worsen errors, inference,
allocation, or specialization. Representation equivalence is not a cost
equivalence.

### Adjunctions organize free construction and interpretation

An adjunction `F ⊣ G` provides a natural correspondence:

```text
Hom(F A, B)  ~=  Hom(A, G B)
```

Currying is one example. Another recurring programming pattern is a free
construction left adjoint to a forgetful operation: generate syntax or an
algebraic structure from raw operations, then interpret it in any target that
supports those operations.

This pattern informs:

- free monads and free algebraic-effect models;
- syntax trees and interpreters;
- folds from initial algebras;
- generic builders and eliminators; and
- compiler intermediate representations whose meaning is supplied by an
  algebra.

Adjunctions help identify canonical interfaces and translations. They do not
guarantee that a free representation is compact or fast. Catena should use
them to design reference semantics and derivations, then compare optimized
representations empirically.

## Algebraic data, folds, and unfolds

### A datatype exposes a shape functor

A regular recursive datatype can be separated into one layer of shape and its
recursive fixed point. For a list of `A`:

```text
ListF A R = Unit + (A * R)
List A     = fix (ListF A)
```

An algebra replaces the recursive hole `R` with a result type `B`:

```text
alg : ListF A B -> B
```

The catamorphism `fold(alg) : List A -> B` is the unique homomorphism from the
initial algebra. In ordinary code, `alg` supplies the empty and cons cases.
The universal property yields the characteristic equation and fusion laws.

Dually, a coalgebra:

```text
coalg : S -> ListF A S
```

can generate a list with an anamorphism or unfold. Composing an unfold with a
fold gives a hylomorphism, often making an intermediate recursive structure
available for equational elimination.

[Meijer, Fokkinga, and Paterson](../30-sources/meijer-et-al-1991-functional-programming-bananas.md)
develop these operators and laws as a calculus for lazy functional programs.
Their expressibility results justify canonical generated consumers and
producers, but do not show that symbolic recursion-scheme syntax belongs in a
general-purpose language.

### Catena should derive structure, not mystique

For a positive regular datatype, Catena can plausibly derive:

- `map`, when the selected parameter occurs covariantly;
- `fold`, from constructor cases;
- `unfold`, where productivity and target representation are meaningful;
- `traverse`, when each parameter position can be visited once in structural
  order; and
- law/property-test scaffolding for the generated operations.

The generated API should use ordinary names, constructor-oriented diagnostics,
and explicit evaluation order. An advanced library can express catamorphisms
and hylomorphisms generically on top.

Automatic fusion should wait. In a strict language, replacing a producer and
consumer by a fused loop can change termination, exception timing, allocation,
sharing, and retained memory. The optimizer needs a language-specific theorem
and operational side conditions, not only a categorical equation.

### Data versus codata

Initial algebras model finite inductive data through constructors and folds.
Final coalgebras model observable, potentially infinite behavior through
destructors and unfolds. This distinction should be explicit if Catena later
adds streams or codata:

- inductive validity is grounded in finite construction;
- coinductive validity is grounded in productive observation; and
- a generic recursion mechanism must not blur termination and productivity.

Category theory clarifies the duality, but a compiler still needs a syntactic
or semantic productivity check.

## A spectrum of computational structure

The popular abstractions are best understood as different information budgets,
not a ladder of sophistication.

| Structure | Core operation shape | Information retained | Typical use |
| --- | --- | --- | --- |
| Functor | map a pure function | One existing shape | Transform values in context |
| Applicative | combine fixed effectful arguments | Static dependency graph and order | Validation, independent queries, traversal |
| Monad | choose the next computation from a value | Dynamic value-dependent control | Parsers, explicit effects, workflows |
| Arrow | compose abstract input/output computations | Static structure unavailable through host functions | Circuits, analyzable parsers, dataflow |
| Comonad | extend context-dependent observation | Neighborhood or history context | Streams, cellular/dataflow computation |

These rows are not mutually exclusive. A monad normally supplies an
applicative; a suitable arrow yields applicatives by fixing its input; Kleisli
arrows arise from monads; and ordinary functions are arrows. The design
question is which interface a function *requires*, because that determines
what generic callers and optimizers are allowed to know.

### Applicative: fixed shape is valuable information

An applicative interface is:

```text
pure  : A -> F A
apply : F (A -> B) -> F A -> F B
```

[McBride and Paterson](../30-sources/mcbride-paterson-2008-applicative-programming-effects.md)
show that every expression can be arranged as one pure function applied to a
fixed sequence of effectful arguments. Earlier results may affect the final
value, but not which later computations exist.

That restriction enables:

- accumulating independent validation errors instead of stopping at the first;
- discovering a parser or query graph before results arrive;
- traversing a datatype with a generic effect;
- composing applicative layers that would not compose as monads; and
- scheduling independent work, **if** the operational contract separately
  permits concurrency.

The last condition matters. Applicative laws preserve a sequencing structure;
they do not say effects commute. A left-to-right applicative for I/O cannot be
parallelized merely because its shape is static.

### Monad: dynamic dependency is the feature

A monad can be presented with:

```text
pure : A -> M A
bind : M A -> (A -> M B) -> M B
```

or categorically as an endofunctor with a unit and associative multiplication.
[Moggi](../30-sources/moggi-1991-notions-computation-monads.md) uses the
structure to distinguish a value `A` from a computation `T A` and to give
several notions of computation sound equational theories.
[Wadler](../30-sources/wadler-1995-monads-functional-programming.md) shows how
the same structure factors evaluator, parser, and state plumbing in functional
programs.

The essential added power is that the value produced by the first computation
selects the second computation. This supports data-dependent parsing,
early exit, dynamically shaped queries, and explicit workflow descriptions.
It also hides the future computation graph from static inspection.

Catena should not equate monads with all effects. Native algebraic handlers can
let functions request operations directly while effect rows record requests.
Monads remain appropriate when the computation itself is useful data: it may
need to be inspected, serialized, replayed, transformed, or interpreted more
than once. The [algebraic-effects synthesis](algebraic-effects-and-handlers.md)
develops the direct effect design and its different handler obligations.

### Arrow: preserve a static representation of computation

Monadic bind receives a host-language function `A -> M B`. Before an `A`
exists, a library cannot inspect that function to discover which computation
will follow. [Hughes's arrows](../30-sources/hughes-2000-generalising-monads-arrows.md)
replace the function with an abstract computation type whose input and output
are both explicit:

```text
arr     : (A -> B) -> P A B
compose : P A B -> P B C -> P A C
first   : P A B -> P (A * C) (B * C)
```

This enables libraries to retain static parser tables, circuit topology, GUI
networks, or other analyzable structure. It is a legitimate abstraction when
ordinary functions reveal too little. It is also heavier than applicative
code and should be introduced only by libraries with such a need.

### Comonad: compute from context

A comonad is the formal dual of a monad, but its programming use is clearer
without starting from duality:

```text
extract   : W A -> A
duplicate : W A -> W (W A)
extend    : (W A -> B) -> W A -> W B
```

`extend` applies a context-dependent observation at every focused position.
[Uustalu and Vene](../30-sources/uustalu-vene-2005-essence-dataflow-programming.md)
use coKleisli arrows to structure stream and dataflow computations. The
selected comonad controls which context is available; a history-only context
can enforce causality that a full two-sided stream would not.

This is a useful semantic and library pattern for contextual computation, not
evidence for a core `Comonad` feature. Memory retention, incremental updates,
scheduling, and distribution remain operational concerns.

## Profunctors and composable data access

A profunctor generalizes a function by mapping its input contravariantly and
its output covariantly:

```text
dimap : (A2 -> A1) -> (B1 -> B2) -> P A1 B1 -> P A2 B2
```

This two-sided structure gives a uniform language for adapting consumers and
producers. [Pickering, Gibbons, and Wu](../30-sources/pickering-et-al-2017-profunctor-optics.md)
use constrained profunctor transformations to represent optics:

- adapters require only profunctorial mapping;
- lenses additionally require product structure;
- prisms require sum structure; and
- traversals require a monoidal way to combine multiple targets.

The representation lets different optics compose with ordinary function
composition while the constraints record the structural power needed. This is
a strong application because it solves an everyday problem: updating or
querying nested compound data without hard-coding one access path.

Catena should approach the problem in two stages. First, derive simple field
lenses and constructor prisms with direct, source-oriented types. Later,
evaluate a profunctor representation after higher-rank polymorphism,
higher-kinded parameters, trait evidence, specialization, and diagnostic
quality are stable. A sophisticated representation that generates unreadable
constraints would lose the practical benefit it was meant to provide.

Optic laws also remain separate obligations. A value named `Lens` does not
prove get-put, put-get, or put-put behavior unless the language derives it from
a known field or carries a proof.

## Categories as compiler targets

The Lambek correspondence suggests a reusable compiler architecture:

```text
typed pure function
  -> categorical combinators
  -> selected interpretation
```

[Elliott's Compiling to Categories](../30-sources/elliott-2017-compiling-to-categories.md)
implements this approach with a GHC plugin. The same source functions receive
interpretations as hardware graphs, differentiable maps, incremental
computations, and interval analyses. A target is defined outside the compiler
as a category with the required product, closed, sum, or other structure.

This has three attractive properties:

1. host-language parsing, binding, type checking, abstraction, and reuse are
   retained;
2. the intermediate vocabulary is small and compositional; and
3. a new interpretation can be added without teaching the compiler all of its
   domain concepts.

For Catena, this should begin as an experimental typed IR for an explicitly
restricted pure fragment. Each translation must record:

- the source constructs accepted;
- the categorical structure required by the target;
- treatment of sums, recursion, sharing, and higher-order functions;
- the equivalence theorem relating source and target;
- generated source locations; and
- target-specific cost and rejection diagnostics.

It should not become the only core IR. SSA, CPS, closure conversion, effect
lowering, ownership, exceptions, and machine layout preserve intensional
information that a purely extensional categorical presentation may omit. A
categorical IR is one interpretation boundary among several.

## Laws meet real language semantics

### Bottom and evaluation order

Category laws are usually written extensionally. A real evaluator can observe
more:

```text
pair(diverge, 1)
```

may diverge immediately in a strict language, retain a thunk in a lazy
language, or be rejected in a total language. Eta expansion can alter
allocation or termination in the presence of strictness primitives. A fold
fusion equation can change which exception occurs first.

Catena therefore needs at least three notions of equality:

- **denotational equality** in a stated model;
- **contextual equivalence** under the language's observable behavior; and
- **optimization refinement**, which may preserve results while improving or
  bounding selected costs.

No rewrite should move from the first to the second without a theorem for the
actual language fragment.

### Effects and commutativity

Composition order is semantic for effects. Two computations may be
applicatively independent in their values while still writing the same file,
mutating the same cell, or racing on cancellation. Monads structure order but
do not explain resource safety. Algebraic handlers explain requests and
interpretation but do not make handlers commute.

If Catena wants to reorder or parallelize computations, it needs additional
evidence such as:

- an empty effect row;
- disjoint capabilities or regions;
- a commutative effect/handler contract;
- an applicative explicitly documented as parallel; or
- a proof in a resource or effect logic.

The abstraction name is not enough.

### Lawful instances and compiler trust

Trait coherence means the compiler chooses one dictionary. It does not mean
the dictionary obeys algebraic laws. Initially, Catena should treat laws as:

- normative documentation for public instances;
- automatically instantiated property suites;
- compiler-proved for derived instances; and
- unavailable as optimizer axioms for arbitrary user instances.

If later optimization needs user laws, Catena can add one of two explicit
mechanisms: a trusted declaration that is unsafe if false, or proof-carrying
evidence checked by the compiler. Silently trusting ordinary instances would
turn a library bug into miscompilation.

### Cost is a second contract

Categorical equivalence intentionally forgets representation. Programmers
still need to know whether `map` is lazy, whether `traverse` allocates, whether
an optic specializes, whether bind is stack safe, and whether a fold retains
the source.

Catena library documentation should therefore place an operational contract
beside algebraic laws:

```text
algebraic:
  map identity
  map composition

operational:
  visits each element once, left to right
  O(n) time, O(1) auxiliary stack for lists
  does not run effects concurrently
  stops after the first raised abortive effect
```

The exact notation is open; the separation is not.

## Proposed Catena design

### Core language

The categorical foundation strengthens choices already made in
[A Greenfield Type System for Catena](catena-greenfield-type-system.md):

- Keep functions, composition, unit, products, sums, algebraic data, and case
  analysis direct and unsurprising.
- Support rigid higher-kinded parameters such as `F : Type -> Type` without
  adding unrestricted type-level computation.
- Keep trait evidence coherent, global, non-overlapping, and explicit in the
  elaborated core.
- Preserve a pure fragment whose observations are narrow enough for a stated
  parametricity theorem.
- Track native effects separately in effect rows; do not encode every language
  effect through one universal monad.
- Maintain an explicit evaluation and cost model alongside extensional
  typing.

No built-in `Category` syntax is needed. Ordinary function composition already
expresses the common case. A library trait for binary constructors can be
added once arrows, parsers, or categorical compiler targets provide real
clients.

### Standard abstraction layer

The first categorical library should be small:

```text
Functor F
  map : (A -> B) -> F A -> F B

Applicative F : Functor F
  pure  : A -> F A
  apply : F (A -> B) -> F A -> F B

Monad M : Applicative M
  bind : M A -> (A -> M B) -> M B

Traversable T : Functor T
  traverse : Applicative F => (A -> F B) -> T A -> F (T B)
```

Names may change after syntax studies, but the substructure should remain
visible: code requiring only `Functor` or `Applicative` must not demand
`Monad`. `Applicative` should specify effect order. A separate `Parallel`
wrapper or trait can express commutative/concurrent combination rather than
overloading the same instance with incompatible behavior.

`Contravariant`, `Bifunctor`, `Profunctor`, `Category`, `Arrow`, and `Comonad`
belong in focused libraries after examples justify them. They should not all
ship merely to complete a taxonomy.

### Datatype derivation

For supported datatype shapes, derive:

```text
derive map
derive fold
derive traverse
derive field_optics
derive variant_optics
```

The compiler must report why a derivation is unavailable—negative occurrence,
nonuniform recursion, inaccessible field, ambiguous traversal order—using the
original declaration. Generated instances are law-trusted only relative to a
tested and specified derivation algorithm.

Generic recursion-scheme operators can live in a library over a public
one-layer representation. The language should not require banana-bracket
notation or point-free programming.

### Laws and tooling

Trait declarations should be able to attach named law schemas as
documentation and test generators:

```text
law map_identity(x):
  map(id, x) == x

law map_composition(f, g, x):
  map(g compose f, x) == map(g, map(f, x))
```

In the initial implementation:

- laws instantiate reusable property tests;
- derived instances may carry compiler-generated evidence;
- public documentation renders the laws and operational contract;
- the optimizer trusts only built-in or compiler-derived evidence; and
- failures identify the instance, law, generated inputs, and shrunk
  counterexample.

A later parametricity tool may derive candidate free theorems from signatures,
but it must print the purity, totality, and representation-opacity assumptions
under which each theorem holds.

### Experimental compilation interface

After the pure core is stable, prototype:

```text
interpret[TargetCategory] pure_function
```

The feature should elaborate through a typed categorical IR and reject source
features the target cannot interpret. Initial targets could be automatic
differentiation, a static dataflow graph, or interval interpretation because
each has a clear alternate meaning and test oracle.

This experiment succeeds only if source programs remain ordinary Catena,
target definitions remain outside the compiler, and differential tests compare
the source and interpreted results. It fails if error messages expose only
combinator plumbing or if target-specific escape hatches dominate ordinary
code.

## Worked design sketches

### Validation should expose independent structure

Suppose a configuration needs three independent fields:

```text
make_config
  <$> read_host(source)
  <*> read_port(source)
  <*> read_credentials(source)
```

An applicative validation can collect all field errors because its structure
is known before values arrive. A monadic version can stop or choose later
parsers dynamically, but that power prevents generic accumulation. Catena's
API should accept the applicative constraint unless a field genuinely changes
which later field is parsed.

The operational contract must still state read order and whether these reads
are pure lookups, sequential effects, or parallel tasks.

### An explicit workflow may deserve a monad even with native effects

A deployment plan may be constructed, inspected, serialized, approved, and
only then executed. Representing it as `Plan A` with monadic composition is
useful because the computation is data. Replacing it with immediate native
effects would destroy the inspection boundary. Conversely, ordinary file I/O
does not need to be wrapped in a user-visible monad merely to keep the
implementation pure; Catena's effect row and handler system can represent the
request directly.

### Generated folds should retain constructor vocabulary

For:

```text
type Expr A =
  | Value A
  | Add (Expr A) (Expr A)
```

derive an operation equivalent to:

```text
fold_expr :
  (A -> B) ->
  (B -> B -> B) ->
  Expr A -> B
```

Diagnostics should say “the `Add` case returned `String`, expected `Int`,” not
“algebra `ExprF Int String -> String` failed to unify.” The categorical model
justifies the operator; the source language should preserve the domain model.

### Optics should begin concrete

A generated field optic for `User.address.city` should compose predictably and
specialize to direct access. The first API can expose readable getters and
updaters. A profunctor encoding becomes attractive only when mixing fields,
variants, and traversals creates repeated adapter code that the uniform
representation actually removes.

## Rejected extremes

### “Category theory is only naming patterns programmers already know”

This misses universal properties, representation theorems, parametricity,
semantic models, and calculational laws. The theory can reveal that two APIs
share a composition structure and can support proofs or generic algorithms
that examples alone would not justify.

### “Every categorical abstraction belongs in the standard library”

A mathematically coherent hierarchy is not automatically a usable library.
Each abstraction adds vocabulary, constraints, inference paths, laws,
documentation, and instance choices. Unused generality is not free.

### “Types enforce the laws”

Ordinary trait types enforce operation shape. Parametricity can derive some
laws for sufficiently polymorphic terms, and derivation or proof systems can
establish others. Arbitrary programmer-written implementations can violate
identity, associativity, optic, or monad laws while type-checking.

### “Categorical equality authorizes optimization”

Denotational equality under a pure total model does not automatically preserve
strictness, effects, exception timing, allocation, or space usage. Compiler
rewrites need contextual-equivalence or refinement results for Catena's actual
semantics.

### “Monads are the categorical form of all effects”

Monads give a powerful semantic and library structure for computation, not one
mandatory user-facing encoding. Algebraic handlers, arrows, comonads,
applicatives, capabilities, and direct operational constructs solve different
problems. Even two monads do not compose automatically.

## Tradeoffs and falsification criteria

The proposal should be revised if any of these observations hold:

- Higher-kinded trait inference makes common `map` and `traverse` calls need
  annotations that a direct per-datatype API avoids.
- Global coherence prevents important domain-specific interpretations that
  explicit dictionary arguments cannot express cleanly.
- Law property suites produce mostly vacuous tests or cannot generate useful
  higher-order functions and recursive values.
- Derived traversals impose an order that surprises users or prevents
  alternative valid traversals from coexisting.
- The applicative/monad distinction does not improve static analysis,
  validation behavior, or API clarity in representative Catena code.
- Profunctor optics increase type-error volume or compilation time without
  making mixed accessors materially easier to build.
- Categorical IR translation rejects so much ordinary code, obscures source
  locations, or needs so many target-specific primitives that a dedicated DSL
  is clearer.
- Optimizations based on derived laws fail differential tests involving
  strictness, effects, sharing, exceptions, or resource cleanup.

Conversely, the design earns confidence only through concrete corpora:
configuration validation, parsers, effectful traversals, compiler AST passes,
stream/dataflow programs, nested record/variant updates, and at least one
alternate interpretation such as differentiation.

## Research priorities

1. **Prove the pure fragment's abstraction theorem.** State exactly which
   Catena features preserve relational parametricity and what free theorems
   follow.
2. **Specify law evidence.** Separate promised, tested, derived, trusted, and
   proved laws in the elaborated core and optimizer.
3. **Prototype the minimal hierarchy.** Measure inference, diagnostics, and
   reuse for `Functor`, `Applicative`, `Monad`, and `Traversable` without
   importing a mature language's entire class ecosystem.
4. **Define datatype derivability.** Formalize positivity, variance,
   nonuniform recursion, traversal order, and generated operation semantics.
5. **Relate laws to effects.** Determine when applicative nodes may commute,
   fuse, or run concurrently under Catena's effect rows and lexical
   capabilities.
6. **Compare optics representations.** Test generated concrete optics against
   profunctor encodings for errors, specialization, mixed composition, and API
   discovery.
7. **Build one categorical IR experiment.** Use a small pure corpus and a
   target with a differential oracle; do not generalize before the experiment
   preserves source behavior and diagnostics.
8. **Document cost contracts.** Give standard abstractions stable traversal,
   order, strictness, allocation, and stack-safety statements.

The active workbench is
[Which Categorical Abstractions Should Catena Expose?](../40-inquiries/which-categorical-abstractions-should-catena-expose.md).

## Evidence route

### Typed structure and abstraction

- [Lambek 1972](../30-sources/lambek-1972-deductive-systems-categories-iii.md)
  — cartesian closed categories, typed deduction, combinatory logic, and the
  structural meaning of functions and products.
- [Reynolds 1983](../30-sources/reynolds-1983-types-abstraction-parametric-polymorphism.md)
  — relational parametricity and representation independence.
- [Wadler 1989](../30-sources/wadler-1989-theorems-for-free.md) — programmer-
  facing equations derived from polymorphic types.

### Data and computation

- [Meijer, Fokkinga, and Paterson 1991](../30-sources/meijer-et-al-1991-functional-programming-bananas.md)
  — folds, unfolds, recursion schemes, and program calculation.
- [Moggi 1991](../30-sources/moggi-1991-notions-computation-monads.md) — values
  versus computations and monadic sequencing semantics.
- [Wadler 1995](../30-sources/wadler-1995-monads-functional-programming.md) —
  monadic structure applied to evaluators, state, and parsing.
- [McBride and Paterson 2008](../30-sources/mcbride-paterson-2008-applicative-programming-effects.md)
  — fixed effectful structure, traversals, and the weakest-adequate-interface
  principle.
- [Hughes 2000](../30-sources/hughes-2000-generalising-monads-arrows.md) —
  abstract computations that retain static structure beyond monadic bind.
- [Uustalu and Vene 2005](../30-sources/uustalu-vene-2005-essence-dataflow-programming.md)
  — comonadic context dependence in stream and dataflow computation.

### Modular interpretation

- [Pickering, Gibbons, and Wu 2017](../30-sources/pickering-et-al-2017-profunctor-optics.md)
  — profunctor representations for composable heterogeneous data access.
- [Elliott 2017](../30-sources/elliott-2017-compiling-to-categories.md) — typed
  functions reinterpreted as circuits, derivatives, incremental computations,
  and analyses.
- [Plotkin and Power 2003](../30-sources/plotkin-power-2003-algebraic-operations-generic-effects.md)
  and [Plotkin and Pretnar 2009](../30-sources/plotkin-pretnar-2009-handlers-algebraic-effects.md)
  — categorical foundations already used by the archive's algebraic-effects
  work, connecting monadic models, algebraic operations, free models, and
  handlers.

Follow the curated route in the
[Category Theory for Programming map](../10-maps/category-theory-for-programming.md).
