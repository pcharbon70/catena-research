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
contracts. Its standard library should begin with the complete seventeen-class
hierarchy developed below: `Setoid`, `Ord`, `Semigroup`, `Monoid`, `Foldable`,
`Functor`, `Bifunctor`, `Apply`, `Applicative`, `Traversable`, `Chain`, `Monad`,
`Semigroupoid`, `Category`, `Arrow`, `Extend`, and `Comonad`.

Starting with the complete vocabulary does not turn class names into proofs.
Catena should **not** grant compiler optimizations merely because an instance
is named `Functor` or `Monad`, nor add profunctor-optic syntax, generalized
recursion-scheme syntax, or categorical compilation before their separate
requirements are demonstrated.

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

A class in the agreed initial hierarchy becomes implementable only when all of
the following can be supplied:

- **Concrete role:** representative datatypes and functions demonstrate why
  the weaker class is independently useful.
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

The class membership is a design commitment. This standard determines whether
its semantics and implementation are ready, and intentionally rejects “it is a
well-known category” as a substitute for that work.

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

## The initial type-class hierarchy

Catena should ship the following seventeen type classes from the beginning.
Here *type class* names the user-facing algebraic interface; the eventual
surface keyword may still be `trait`. The classes are grouped by kind and
operation rather than presented as one misleading linear ladder.

```text
values
  Setoid -> Ord
  Semigroup -> Monoid

unary constructors, F : Type -> Type
  Functor -> Apply -> Applicative --\
                   -> Chain ------+-> Monad
  Functor -> Extend -> Comonad
  Functor --\
             +-> Traversable
  Foldable --/

binary constructors, P : Type -> Type -> Type
  Semigroupoid -> Category -> Arrow
  Bifunctor
```

`Bifunctor` is conceptually the two-argument counterpart of `Functor`, and
fixing either argument of a bifunctor yields a unary functor. It should not
literally inherit one ambiguous `Functor` dictionary: `P : Type -> Type -> Type`
and `F : Type -> Type` have different kinds, and the compiler would not know
which argument a unary `map` targets. Catena should derive explicit `map_first`
and `map_second` operations from `bimap`, or expose partially applied
constructor views when the type language can express them.

The hierarchy deliberately preserves unitless structures. `Apply` has
contextual application without `pure`; `Chain` has value-dependent sequencing
without `pure`; `Extend` has context-dependent extension without `extract`;
`Semigroup` and `Semigroupoid` have associative composition without identities.
These are not incomplete mistakes. They let generic code request no more
power than it uses and admit types for which no lawful identity or injection
exists.

[The algebraic interoperability specification](../30-sources/fantasy-land-algebraic-specification.md)
provides the operation-and-law vocabulary for most of the weak/strong splits;
[Hughes](../30-sources/hughes-2000-generalising-monads-arrows.md) supplies the
arrow interface and laws.
[Wadler and Blott](../30-sources/wadler-blott-1989-ad-hoc-polymorphism.md)
provide the type-class mechanism; Catena's coherence restrictions continue to
come from the qualified-type work already adopted by the type-system design.
[Rivas and Jaskelioff](../30-sources/rivas-jaskelioff-2017-notions-computation-monoids.md)
show why value monoids, applicatives, monads, and arrows can share algebraic
patterns without becoming the same interface.

### Summary matrix

| Class | Parameter kind | Parent classes | Minimal new operation | Defining obligation |
| --- | --- | --- | --- | --- |
| `Setoid` | `Type` | None | `equivalent` | Reflexive, symmetric, transitive |
| `Ord` | `Type` | `Setoid` | `compare` or `less_or_equal` | Total, transitive order coherent with equivalence |
| `Semigroup` | `Type` | None | `combine` | Associativity |
| `Monoid` | `Type` | `Semigroup` | `empty` | Left and right identity |
| `Foldable` | `Type -> Type` | None | `fold_map` | Structural order/cardinality and monoid coherence |
| `Functor` | `Type -> Type` | None | `map` | Identity and composition |
| `Bifunctor` | `Type -> Type -> Type` | Kind-aware analogue of `Functor` | `bimap` | Identity and composition in both positions |
| `Apply` | `Type -> Type` | `Functor` | `apply` | Associative contextual application |
| `Applicative` | `Type -> Type` | `Apply` | `pure` | Identity, homomorphism, interchange, parent compatibility |
| `Traversable` | `Type -> Type` | `Functor`, `Foldable` | `traverse` | Naturality, identity, composition, structural visitation |
| `Chain` | `Type -> Type` | `Apply` | `chain` | Associative value-dependent sequencing and `apply` compatibility |
| `Monad` | `Type -> Type` | `Applicative`, `Chain` | No additional primitive | Left and right sequencing identity and parent compatibility |
| `Semigroupoid` | `Type -> Type -> Type` | None | `compose` | Associativity of typed composition |
| `Category` | `Type -> Type -> Type` | `Semigroupoid` | `identity` | Left and right identity |
| `Arrow` | `Type -> Type -> Type` | `Category` | `lift`, `first` | Preserve pure composition and interact coherently with products |
| `Extend` | `Type -> Type` | `Functor` | `extend` | Associativity of context-dependent extension |
| `Comonad` | `Type -> Type` | `Extend` | `extract` | Left and right extension identity and parent compatibility |

The matrix gives minimal *new* operations, not the complete usable API.
Derived conveniences should be standardized once, outside each instance, so
that law-equivalent implementations do not fragment calling conventions.

### `Setoid`: programmable equivalence

```text
trait Setoid A {
  equivalent : A -> A -> Bool
}
```

The required laws are:

```text
equivalent(x, x)
equivalent(x, y) == equivalent(y, x)
equivalent(x, y) && equivalent(y, z) implies equivalent(x, z)
```

A setoid is a type equipped with an equivalence relation. The relation need
not be representation identity: case-insensitive names, normalized paths, and
values modulo a unit conversion may have useful domain equivalences.

Catena must not silently make `Setoid` the semantics of pattern matching,
hashing, or compiler type equality. Those operations need separate contracts.
If a hash table accepts `Setoid`, it must also require a hash function coherent
with `equivalent`; equal values receiving unrelated hashes would break lookup.

### `Ord`: total order compatible with equivalence

```text
trait Ord A : Setoid A {
  compare : A -> A -> Ordering
}
```

`Ordering` has `Less`, `Equal`, and `Greater`. A lawful instance is total and
transitive, and:

```text
compare(x, y) == Equal  iff  equivalent(x, y)
```

Antisymmetry is stated through the parent equivalence, not representation
identity. `Ord` supports sorting, ordered maps, ranges, minimum/maximum, and
lexicographic derivation. Partial orders—dependency relations or subset
inclusion—must use a different future class; forcing them into `Ord` would
make sorting algorithms unsound.

Derived comparison predicates should call `compare` so they cannot disagree.
Floating-point exceptional values require an explicit policy or a wrapper
type rather than a dishonest total-order instance.

### `Semigroup`: associative combination

```text
trait Semigroup A {
  combine : A -> A -> A
}
```

Its single law is:

```text
combine(combine(x, y), z) == combine(x, combine(y, z))
```

Examples include concatenating nonempty sequences, accumulating validation
errors, merging logs in a fixed order, composing endomorphisms, and selecting
the first or last value through explicit wrappers. Associativity permits
regrouping and tree reduction; it does not permit reordering. Parallel
reduction additionally requires commutativity or a scheduler that preserves
the documented order.

### `Monoid`: a semigroup with an identity

```text
trait Monoid A : Semigroup A {
  empty : A
}
```

The added laws are:

```text
combine(empty, x) == x
combine(x, empty) == x
```

Lists under concatenation, numbers under addition, booleans under conjunction
or disjunction, maps under a specified merge, and endomorphisms under
composition are common examples. The operation is part of the instance:
numbers do not have one privileged monoid, so additive and multiplicative
wrappers or explicit dictionaries avoid incoherent global choices.

Monoids power generic folds, builders, summaries, writer-style accumulation,
and balanced reduction. [Rivas and Jaskelioff](../30-sources/rivas-jaskelioff-2017-notions-computation-monoids.md)
also show that the same composition-plus-unit pattern appears one level higher
in applicatives, monads, and arrows.

### `Foldable`: consume every structural element

```text
trait Foldable T {
  fold_map : Monoid M => (A -> M) -> T A -> M
}
```

`fold_map` exposes the most algebraic minimal interface: transform each
element into a monoid and combine the results in the structure's documented
order. `fold_left`, `fold_right`, `to_list`, `length`, `any`, and `all` can be
derived, subject to strictness and short-circuiting contracts.

A `Foldable` instance must state which elements occur, in what order, and with
what multiplicity. Associativity makes parenthesization irrelevant, but a
noncommutative monoid still observes order. A search tree may fold in-order;
a hash table cannot promise a stable order unless its representation does.

`Foldable` does not imply `Functor`: a structure may expose elements for
consumption without supporting a shape-preserving replacement of their type.
It also does not imply safe early termination in a strict language; that is an
operational property of the derived fold.

### `Functor`: map while preserving shape

```text
trait Functor F {
  map : (A -> B) -> F A -> F B
}
```

The identity and composition laws are:

```text
map(identity, x) == x
map(g compose f, x) == map(g, map(f, x))
```

Lists, optional values, trees, one side of `Result E`, environments, and many
syntax trees are examples. The laws say mapping changes the varying values
without adding, deleting, duplicating, or reordering structure in an
observable way.

Parametricity often supports these equations, but a user-defined dictionary
can still violate them. `Functor` is therefore the first major test of
Catena's distinction between a method type and law evidence.

### `Bifunctor`: map two covariant positions

```text
trait Bifunctor P {
  bimap : (A -> C) -> (B -> D) -> P A B -> P C D
}
```

The laws are identity and componentwise composition:

```text
bimap(identity, identity, x) == x
bimap(f2 compose f1, g2 compose g1, x)
  == bimap(f2, g2, bimap(f1, g1, x))
```

Pairs, `Result Error Value`, validation results, and syntax nodes with two
varying parameter roles are typical instances. `map_first` and `map_second`
are derived by using identity for the untouched side.

Both arguments must be covariant. Function input is contravariant, so ordinary
function arrows are profunctors rather than bifunctors. Catena should use kind
checking to reject accidental attempts to treat every two-parameter type as a
`Bifunctor`.

### `Apply`: combine contexts without inventing one

```text
trait Apply F : Functor F {
  apply : F (A -> B) -> F A -> F B
}
```

`Apply` combines an effectful/contextual function with an effectful/contextual
argument, but provides no `pure : A -> F A`. It is equivalently a strong
semigroupal functor: from two inhabited contexts it can construct a context of
pairs, coherently and associatively, without promising a context for an
arbitrary standalone value.

The key law is associative contextual composition. For appropriately typed
`u`, `v`, and `w`:

```text
apply(apply(map(compose, u), v), w)
  == apply(u, apply(v, w))
```

Equivalently, in product form, with `product` derived from `map` and `apply`:

```text
map(associate, product(product(x, y), z))
  == product(x, product(y, z))
```

This class matters both for genuinely unitless structures and for generic
functions that need combination but not injection. It preserves a more honest
constraint than demanding `Applicative` everywhere. It still needs an
operational order: `apply` does not imply parallel or commutative effects.

### `Applicative`: `Apply` with pure injection

```text
trait Applicative F : Apply F {
  pure : A -> F A
}
```

Adding `pure` supplies the unit missing from `Apply`. Its laws make pure values
the left and right unit for contextual product and, in application form,
require identity, homomorphism, and interchange. In particular:

```text
apply(pure(identity), v) == v
apply(pure(f), pure(x)) == pure(f(x))
apply(u, pure(y)) == apply(pure(f -> f(y)), u)
```

Applicative programs have a fixed effectful shape: earlier values may
contribute to the final pure function, but cannot select which later
computation exists. This supports independent validation, static query or
parser analysis, and generic traversal. The deeper evidence is in
[McBride and Paterson](../30-sources/mcbride-paterson-2008-applicative-programming-effects.md).

The parent dictionary must be compatible: its `map` and `apply` must agree
with the operations derivable from `pure` and contextual application.

### `Traversable`: map and accumulate in one structural pass

```text
trait Traversable T : Functor T, Foldable T {
  traverse : Applicative F => (A -> F B) -> T A -> F (T B)
}
```

The laws are:

- **naturality:** changing the applicative representation before or after a
  traversal agrees;
- **identity:** traversing through the identity applicative is ordinary
  mapping; and
- **composition:** traversing through composed applicatives agrees with two
  coherent traversals.

[Gibbons and Oliveira](../30-sources/gibbons-oliveira-2009-essence-iterator-pattern.md)
show that traversal combines the mapping and accumulation aspects of an
iterator. They also expose an important limit: the familiar three laws alone
do not transparently rule out every definition that duplicates visits.
Catena-derived traversals should therefore guarantee by construction that
each structural position is visited exactly once, in a documented order.

`sequence : T (F A) -> F (T A)` and effectful mapping are derived. The class
does not authorize concurrent traversal; a parallel applicative or separate
effect evidence must do that.

### `Chain`: associative value-dependent sequencing without a unit

```text
trait Chain M : Apply M {
  chain : M A -> (A -> M B) -> M B
}
```

The associativity law is:

```text
chain(chain(m, f), g)
  == chain(m, x -> chain(f(x), g))
```

Unlike `Apply`, `Chain` lets an earlier value choose the entire later
computation. Unlike `Monad`, it does not promise `pure`. This unitless form is
also useful as the weakest constraint for generic sequencing functions, even
when their concrete instances happen to be full monads.

Because `Chain` extends `Apply`, the supplied `apply` must equal the definition
derived by chaining the contextual function and mapping it over the contextual
argument. This compatibility law prevents two contradictory notions of
sequencing inside one instance.

### `Monad`: applicative injection plus lawful chaining

```text
trait Monad M : Applicative M, Chain M {
  // no additional primitive
}
```

The added identity laws are:

```text
chain(pure(x), f) == f(x)
chain(m, pure) == m
```

Associativity comes from `Chain`; fixed-shape application and injection come
from `Applicative`. All inherited `map` and `apply` operations must agree with
their definitions from `chain` and `pure`.

Monads model dynamic data-dependent computation. They remain useful for
explicit plans, parsers, workflows, and embedded languages even when Catena's
native effects use direct operations and handlers. [Moggi](../30-sources/moggi-1991-notions-computation-monads.md)
supplies the semantic separation of values and computations, while
[Wadler](../30-sources/wadler-1995-monads-functional-programming.md) supplies
the practical library pattern.

### `Semigroupoid`: associative typed composition

```text
trait Semigroupoid P {
  compose : P A B -> P B C -> P A C
}
```

Composition is associative whenever the intermediate types align:

```text
compose(compose(f, g), h) == compose(f, compose(g, h))
```

The interface describes typed pipelines for which composition exists but a
generic identity might not. Nonempty transformations, version migrations,
restricted parsers, and subcategories whose identity representation is absent
can use the weaker constraint.

This is the arrow-shaped analogue of `Semigroup`: both provide associative
composition without a unit, but a semigroupoid's inputs and outputs may have
different types.

### `Category`: a semigroupoid with typed identities

```text
trait Category P : Semigroupoid P {
  identity : P A A
}
```

The identity laws are:

```text
compose(identity, f) == f
compose(f, identity) == f
```

Pure functions form the motivating instance. Kleisli arrows of a monad,
isomorphisms, relations, transformations between schemas, and several compiler
representations may form other categories when their composition and identity
obey the laws.

`Category` belongs in the initial standard hierarchy, but function composition
should remain direct syntax or a normal function. Programmers should need the
class only when abstracting over a non-function arrow type.

### `Arrow`: a category supporting pure functions and products

```text
trait Arrow P : Category P {
  lift  : (A -> B) -> P A B
  first : P A B -> P (A * C) (B * C)
}
```

`lift` must preserve identity and composition. `first` must preserve
composition and interact coherently with product projections, reassociation,
and untouched values. Representative equations, using the `compose` order
defined above, are:

```text
lift(identity) == identity
compose(lift(f), lift(g)) == lift(g compose f)
first(identity) == identity
first(compose(f, g)) == compose(first(f), first(g))
compose(first(f), lift(first_projection))
  == compose(lift(first_projection), f)
```

The remaining product naturality and reassociation equations prevent `first`
from inspecting or changing the untouched component. These are the standard
arrow laws developed by
[Hughes](../30-sources/hughes-2000-generalising-monads-arrows.md).

Arrows support computations whose input and output are explicit but whose
representation is not an ordinary host-language function. Static parsers,
circuits, dataflow graphs, and analyzable reactive networks are the motivating
cases. Including the class initially supplies the vocabulary; specialized
arrow notation should still wait for evidence that ordinary combinators are
unusable.

### `Extend`: context-dependent mapping without extraction

```text
trait Extend W : Functor W {
  extend : (W A -> B) -> W A -> W B
}
```

`extend` evaluates a context-dependent observation at every position while
preserving the outer contextual shape. Its associativity law is:

```text
extend(f, extend(g, w))
  == extend(x -> f(extend(g, x)), w)
```

The derived `duplicate = extend(identity)` exposes the context of contexts.
There is no promise that a bare `A` can be extracted. As with `Chain`, this
unitless class is useful both for genuinely weaker structures and for generic
functions that do not need the stronger operation.

### `Comonad`: extend with a distinguished local value

```text
trait Comonad W : Extend W {
  extract : W A -> A
}
```

The identity laws are:

```text
extend(extract, w) == w
extract(extend(f, w)) == f(w)
```

The inherited `map` must agree with:

```text
map(f, w) == extend(f compose extract, w)
```

Zippers, nonempty focused structures, annotated syntax, cellular
neighborhoods, and history-aware dataflow are representative uses.
[Uustalu and Vene](../30-sources/uustalu-vene-2005-essence-dataflow-programming.md)
show how coKleisli composition structures stream/dataflow computation and why
the chosen context—not the class name—determines causality.

### The hierarchy is laws plus compatibility

Superclass inclusion alone is insufficient. Whenever a stronger class can
derive a parent operation, Catena must require the supplied parent dictionary
to agree with that derivation:

- `Applicative.map` agrees with `apply(pure(f), x)`;
- `Chain.apply` agrees with sequencing a contextual function and mapping it;
- `Monad` uses one `map` and `apply`, not competing applicative and chain
  interpretations;
- `Comonad.map` agrees with extension plus extraction; and
- `Traversable` agrees with both its functorial mapping and fold order.

These coherence equations are part of law testing and future proof evidence.
They must not be inferred merely because the constraint graph has an edge.

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

The source-language declaration, pattern, abstraction, representation, and
inference sides of this topic are developed separately in
[Algebraic Data Types](algebraic-data-types.md). This section isolates the
positive regular shapes for which categorical folds and unfolds are justified.

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
| Apply | combine existing contextual values | Associative combination without injection | Nonempty validation and unitless combination |
| Applicative | combine fixed effectful arguments | Static dependency graph and order | Validation, independent queries, traversal |
| Chain | choose the next context from a value | Dynamic dependency without injection | Nonempty dependent workflows |
| Monad | choose the next computation from a value | Dynamic value-dependent control | Parsers, explicit effects, workflows |
| Arrow | compose abstract input/output computations | Static structure unavailable through host functions | Circuits, analyzable parsers, dataflow |
| Extend | recompute from surrounding context | Context dependence without extraction | Nonempty neighborhoods and histories |
| Comonad | extend context-dependent observation | Neighborhood or history context | Streams, cellular/dataflow computation |

These rows are landmarks within the complete hierarchy, not mutually
exclusive alternatives. `Applicative`, `Monad`, and `Comonad` add units to
`Apply`, `Chain`, and `Extend`; a suitable arrow yields applicatives by fixing
its input; Kleisli arrows arise from monads; and ordinary functions are arrows.
The design question is which interface a function *requires*, because that
determines what generic callers are allowed to assume. Optimizers need
separate trusted law evidence before using any such assumption as a rewrite.

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

No built-in `Category` or `Arrow` syntax is needed. Ordinary function
composition remains the direct common case. The initial `Semigroupoid`,
`Category`, and `Arrow` classes let libraries abstract over other binary
constructors without making categorical notation part of everyday Catena.

### Initial standard hierarchy

The standard abstraction layer should ship all seventeen classes specified in
[the initial hierarchy](#the-initial-type-class-hierarchy):

- value relations and aggregation: `Setoid`, `Ord`, `Semigroup`, and `Monoid`;
- unary structure and computation: `Foldable`, `Functor`, `Apply`,
  `Applicative`, `Traversable`, `Chain`, `Monad`, `Extend`, and `Comonad`;
- binary mapping: `Bifunctor`; and
- typed composition: `Semigroupoid`, `Category`, and `Arrow`.

They should be ordinary library traits over the language's supported kinds,
not seventeen new keywords. Packages may import focused branches, but every
program should use the same canonical definitions and law names so instance
evidence composes across libraries.

The weak/strong boundaries must stay visible: code that needs only `Apply`,
`Chain`, or `Extend` should not acquire `pure` or `extract`, and code requiring
only `Functor` should not demand `Monad`. Each class should provide one
canonical minimal operation set plus standardized derived functions. Every
effect-combining class must specify evaluation order. A separate `Parallel`
wrapper or future trait can express commutative or concurrent combination
rather than overloading one instance with incompatible behavior.

The corresponding minimal methods, derived operations, ADT-generated
operations, and execution contracts are developed in
[Combinators for Algebraic Data and Categorical Programming](combinators-for-algebraic-data-and-categorical-programming.md).

The complete initial hierarchy is still a boundary, not an invitation to
import every named categorical structure. `Contravariant`, `Profunctor`,
specialized monoidal variants, generalized recursion schemes, and categorical
compiler interfaces remain evidence-driven additions.

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

### “A broad initial hierarchy makes every categorical abstraction core”

Shipping the selected seventeen classes does not make every categorical
construction a keyword, optimizer axiom, or standard dependency. Even a
mathematically coherent hierarchy has costs in vocabulary, inference paths,
laws, documentation, and instance choices. The initial set needs corpus and
solver evidence; structures outside it still need a demonstrated programming
role.

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
- The complete seventeen-class graph causes solver search, instance lookup, or
  diagnostics to degrade materially compared with its focused branches.
- `Apply`, `Chain`, `Extend`, or `Semigroupoid` have no representative lawful
  instances or APIs that benefit from their missing unit operation.
- Parent compatibility cannot prevent a nominal `Monad`, `Applicative`, or
  `Comonad` from exposing mutually inconsistent inherited operations.
- Kind-aware `Bifunctor` and arrow constraints require type-level machinery
  that breaks the intended inference and termination boundary.
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
3. **Prototype the complete initial hierarchy.** Measure kind checking,
   inference, evidence elaboration, parent compatibility, diagnostics, and
   reuse across all seventeen classes, including the value, unary-constructor,
   and binary-constructor branches.
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
[How Should Catena Specify Its Initial Categorical Hierarchy?](../40-inquiries/how-should-catena-specify-its-initial-categorical-hierarchy.md).
The focused library and datatype API workbench is
[Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md).

## Evidence route

### Typed structure and abstraction

- [Lambek 1972](../30-sources/lambek-1972-deductive-systems-categories-iii.md)
  — cartesian closed categories, typed deduction, combinatory logic, and the
  structural meaning of functions and products.
- [Reynolds 1983](../30-sources/reynolds-1983-types-abstraction-parametric-polymorphism.md)
  — relational parametricity and representation independence.
- [Wadler 1989](../30-sources/wadler-1989-theorems-for-free.md) — programmer-
  facing equations derived from polymorphic types.
- [Wadler and Blott 1989](../30-sources/wadler-blott-1989-ad-hoc-polymorphism.md)
  — type classes as a systematic account of constrained polymorphism and
  dictionary evidence.

### Class hierarchy and laws

- [Fantasy Land Algebraic Specification](../30-sources/fantasy-land-algebraic-specification.md)
  — operation signatures, parent relationships, and laws for most of the
  selected weak and strong algebraic interfaces.
- [Rivas and Jaskelioff 2017](../30-sources/rivas-jaskelioff-2017-notions-computation-monoids.md)
  — a monoidal account that unifies the recurring composition-plus-unit shape
  of monoids, applicatives, monads, and arrows without identifying them.

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
- [Gibbons and Oliveira 2009](../30-sources/gibbons-oliveira-2009-essence-iterator-pattern.md)
  — traversal as shape-preserving iteration with accumulation, including the
  limits of the familiar traversal laws.
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
