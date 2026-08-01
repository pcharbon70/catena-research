---
title: "Combinators for Algebraic Data and Categorical Programming"
kind: note
created: "2026-08-01"
maturity: developing
tags:
  - algebraic-data-types
  - category-theory
  - catena
  - combinator-libraries
  - functional-programming
  - language-design
aliases:
  - "Combinators for Catena"
  - "ADT and categorical combinators"
---

# Combinators for Algebraic Data and Categorical Programming

## Executive conclusion

A combinator earns its place when it creates a stable seam between programs:
it lets a caller assemble behavior from smaller pieces while depending only on
their types, laws, and operational contract. Algebraic data types and category
theory provide an unusually rich supply of such seams:

- functions compose through identity, composition, currying, and application;
- products compose producers through pairing and route computations through
  `first`, `second`, split, and fanout;
- sums compose consumers through case analysis and route functions through
  either side;
- an ADT declaration determines constructor handlers, mapping, folding, and—
  for suitable shapes—traversal and unfolding;
- the agreed categorical classes determine a small primitive method set and a
  larger derived vocabulary; and
- domain libraries can assign those operations concrete meanings for parsers,
  optics, validation, dataflow, syntax, and analyzable computations.

Catena should not respond by placing every named combinator in the language or
every historical abstraction in one prelude. The initial policy should have
five layers:

1. **Universal function and data routing.** Provide plainly named `identity`,
   `compose`, `curry`, `uncurry`, product pairing, and sum case analysis as
   ordinary functions, with a small amount of pipeline syntax if desired.
2. **One minimal class dictionary.** Keep the agreed seventeen classes at
   their minimal operations and implement derived conveniences once in the
   standard library rather than independently in every instance.
3. **Datatype-derived structure.** Generate or derive `map`, `bimap`,
   constructor-complete `fold`, `fold_map`, and `traverse` only when the
   datatype's variance, positivity, regularity, and field order justify them.
4. **Explicit advanced libraries.** Put generic recursion schemes, optics,
   parser combinators, sum-of-functor syntax, free structures, and selective
   branching in named packages whose stronger typing and cost models are
   visible.
5. **Internal compiler combinators.** Treat combinatory-logic or categorical
   IR as compilation strategies, not as evidence that users should program in
   an `S`/`K` basis or see generated categorical plumbing in diagnostics.

The crucial semantic split is between **pure structural combinators** and
**ambiently effectful callbacks**. A categorical `map` should accept a pure
`A -> B`. If visiting elements performs effects, the API should say so through
`traverse`, an explicit effect row, or a domain protocol. Otherwise functor
laws appear to authorize transformations that duplicate, discard, or reorder
observable work.

Every public combinator therefore needs two contracts:

- an **extensional contract**: type, required structure, equations, and
  compatibility with parent operations; and
- an **operational contract**: evaluation order, callback multiplicity,
  short-circuit behavior, allocation, stack use, streaming, concurrency,
  cancellation, and asymptotic cost where relevant.

The practical rule is:

> Standardize the weakest lawful combinator that exposes useful program
> structure; qualify it by its datatype or class; and never let an algebraic
> law stand in for an execution contract.

This is a fresh synthesis for the language developed in this archive. It does
not use a specification, implementation, or summary from another Catena
repository.

## Scope, terminology, and evidence

### What “combinator” means here

In the broad library sense, a combinator is a function or typed operation whose
purpose is to assemble values, functions, or computations from smaller pieces.
It works through a published interface rather than inspecting hidden
representation. Examples include:

```text
compose : (B -> C) -> (A -> B) -> A -> C
map     : (A -> B) -> F A -> F B
fold    : Algebra F R -> Fix F -> R
apply   : F (A -> B) -> F A -> F B
chain   : M A -> (A -> M B) -> M B
```

In the strict combinatory-logic sense, a combinator is a lambda term with no
free variables. A fixed basis such as `S` and `K` can represent arbitrary
lambda terms. [Turner 1979](../30-sources/turner-1979-applicative-language-implementation.md)
uses that fact as a compiler implementation technique.

This note distinguishes four uses of the word:

| Use | Example | Primary audience | Governing evidence |
| --- | --- | --- | --- |
| Function combinator | `compose`, `flip`, `curry` | all programmers | function semantics and types |
| Structural/library combinator | `fold`, `traverse`, parser choice | library users | laws plus domain execution contract |
| Categorical combinator | `identity`, arrow `first`, coKleisli composition | generic library authors | class laws and coherent dictionaries |
| Compiler combinator | `S`, `K`, categorical IR nodes | compiler implementers | translation correctness and backend cost |

Confusing these levels produces bad design arguments. The fact that lambda
terms can compile to combinatory logic does not make `S` a good standard
library API. Conversely, the fact that a parser's `chain` is a useful source
combinator does not imply the compiler should preserve a monadic representation
to machine code.

### Inclusion standard

A candidate standard combinator should answer all of these questions:

1. **Type:** What can it compose, and which kinds and constraints occur?
2. **Minimum structure:** Is `Functor` enough, or does it truly need
   `Applicative`, `Chain`, `Monad`, `Arrow`, or a concrete datatype?
3. **Laws:** Which equations distinguish the intended operation from another
   inhabitant of the same type?
4. **Coherence:** If a stronger interface derives the operation, must it agree
   with the weaker dictionary?
5. **Effects:** Are function arguments pure, effect-row-polymorphic, or values
   representing explicit computations?
6. **Order and multiplicity:** In what order, and how many times, are arguments
   evaluated or callbacks invoked?
7. **Failure and control:** Can it skip, backtrack, abort, resume, or run both
   alternatives?
8. **Cost:** Does it allocate, retain input, recurse on the stack, stream,
   parallelize, or admit fusion?
9. **Diagnostics:** Can errors name the source combinator and required
   structure instead of an elaborated dictionary term?
10. **Demonstrated use:** Does a representative corpus become clearer or more
    analyzable than with direct matching and ordinary functions?

[Hughes 1989](../30-sources/hughes-1989-why-functional-programming-matters.md)
provides the motivating standard: composition matters because the available
glue determines how a problem can be decomposed. The remaining sources test
which glue is lawful and what information it preserves.

## The universal function layer

### Identity, composition, and pipeline

The smallest reusable vocabulary is:

```text
identity : A -> A

compose : (B -> C) -> (A -> B) -> A -> C
compose(g, f, x) = g(f(x))

pipe : A -> (A -> B) -> B
pipe(x, f) = f(x)
```

`identity` and `compose` satisfy the category laws. `pipe` changes argument
order for readability but adds no semantic power. Catena may give pipeline a
surface operator while keeping `compose` as the law-bearing function.

For effect-row function types, composition exposes the union or sequencing of
ambient effects rather than hiding it:

```text
f : A ->{e1} B
g : B ->{e2} C

compose(g, f) : A ->{e1 + e2} C
```

The exact row operation belongs to the effect calculus. The key point is that
ordinary function composition remains available; programmers do not need a
monad merely because the composed functions perform native Catena effects.

### Argument and function-shape adapters

These adapters are definable once and useful at API boundaries:

```text
constant : A -> B -> A
flip     : (A -> B -> C) -> B -> A -> C
curry    : ((A, B) -> C) -> A -> B -> C
uncurry  : (A -> B -> C) -> (A, B) -> C
```

`curry` and `uncurry` witness the product/exponential correspondence. `flip`
is convenient but can obscure domain meaning when used repeatedly; a named
lambda is often clearer. `constant` is useful for discarding a mapped result,
but its use should not conceal an effectful computation whose result is being
ignored.

The classical `S`, `K`, and `I` basis is mathematically sufficient for lambda
abstraction, but only `I` corresponds to an independently clear public
operation (`identity`). Catena should keep the rest in theory or an internal
IR unless a concrete metaprogramming use appears.

## Products and sums are routing combinators

### Products combine observations

Given `f : X -> A` and `g : X -> B`, pairing produces both observations:

```text
pair_with : (X -> A) -> (X -> B) -> X -> (A, B)
pair_with(f, g, x) = (f(x), g(x))
```

Other canonical product adapters are:

```text
first  : (A -> B) -> (A, C) -> (B, C)
second : (A -> B) -> (C, A) -> (C, B)
split  : (A -> B) -> (C -> D) -> (A, C) -> (B, D)
swap   : (A, B) -> (B, A)
```

For ordinary pure functions, `pair_with(f, g)` evaluates both functions over
the same already evaluated input value. If `f` and `g` have ambient effects,
Catena must specify left-to-right sequencing; an optimizer cannot assume they
commute. For an abstract `Arrow`, the corresponding `fanout` and split
combinators depend on the arrow's product operations and laws.

### Sums combine alternatives

The universal sum consumer is case analysis:

```text
either : (A -> C) -> (B -> C) -> Either A B -> C
```

Derived routing includes:

```text
map_left  : (A -> C) -> Either A B -> Either C B
map_right : (B -> D) -> Either A B -> Either A D
bimap     : (A -> C) -> (B -> D) -> Either A B -> Either C D
```

`either(f, g)` runs exactly one branch after inspecting the real constructor.
This is different from an applicative combination that evaluates both
effectful arguments and from a parser choice that may try or return both
alternatives.

The empty type supplies the unique eliminator:

```text
absurd : Empty -> A
```

It executes no branch because no completed `Empty` value exists. Divergence
while evaluating an `Empty` expression remains divergence.

### Structural rearrangements

Associativity, symmetry, and distributivity give canonical conversions:

```text
associate_product : ((A, B), C) -> (A, (B, C))
associate_sum     : Either (Either A B) C -> Either A (Either B C)
distribute        : (A, Either B C) -> Either (A, B) (A, C)
factor            : Either (A, B) (A, C) -> (A, Either B C)
```

These are valuable inside generic libraries and compiler elaboration. A flat
domain record or named ADT is usually clearer at an application boundary.
Catena should provide them in a structural module rather than flood the default
namespace.

## An ADT determines eliminators

### Constructor handlers are the complete consumer interface

For:

```text
type Option A = None | Some A
```

the constructor-complete eliminator is:

```text
Option.fold : R -> (A -> R) -> Option A -> R
```

For:

```text
type Result E A = Err E | Ok A
```

it is:

```text
Result.fold : (E -> R) -> (A -> R) -> Result E A -> R
```

These functions are named, first-class versions of exhaustive pattern
matching. They are especially useful when passing behavior to another
function, protecting an abstract representation through an exported eliminator,
or calculating with a common result type.

[Böhm and Berarducci 1985](../30-sources/bohm-berarducci-1985-typed-lambda-programs.md)
show the stronger representation idea: suitable term-algebra values can be
encoded by their polymorphic behavior for every constructor-handler result
type. Informally:

```text
Option A  ~=  forall R. R -> (A -> R) -> R
```

Catena should use this as a semantic and API-design bridge, not as its default
runtime representation. Native nominal constructors preserve coverage,
diagnostics, abstraction identity, and layout freedom more directly.

### Mapping preserves the constructor skeleton

For a covariant parameter, `map` changes payload values without changing which
constructors occur:

```text
Option.map : (A -> B) -> Option A -> Option B
Result.map : (A -> B) -> Result E A -> Result E B
Tree.map   : (A -> B) -> Tree A -> Tree B
```

For two covariant positions, `bimap` changes both:

```text
Result.bimap : (E -> F) -> (A -> B) -> Result E A -> Result F B
```

The compiler may derive these only when the selected parameters do not occur
contravariantly. Phantom parameters yield a lawful map that ignores its
function. Negative occurrences reject derivation with a source-located
diagnostic.

### Three meanings of fold must remain distinct

The word `fold` commonly names three related operations:

1. **Constructor-complete eliminator:** one handler for every constructor of a
   particular ADT.
2. **Recursive catamorphism:** replace one recursive constructor layer with an
   algebra after recursively folding its children.
3. **Element fold:** consume the selected `A` positions of a `Foldable T` in a
   documented order.

Catena should distinguish them through qualification and names:

```text
Option.fold(...)
Tree.fold(...)
Foldable.fold_map(...)
Foldable.fold_left(...)
Foldable.fold_right(...)
```

An unqualified `reduce` is worse: it often means a partial nonempty fold, a
parallel tree reduction, or a collection operation with unspecified order.
Use `combine_all`, `combine_all1`, or an explicit left/right fold instead.

### Recursive folds, unfolds, and hylomorphisms

For a positive regular shape functor `F` and fixed point `Fix F`:

```text
cata : (F R -> R) -> Fix F -> R
ana  : (S -> F S) -> S -> Fix F
hylo : (F R -> R) -> (S -> F S) -> S -> R
```

- `cata` consumes recursive data by replacing constructors with an algebra.
- `ana` produces recursive data by repeatedly applying a coalgebra.
- `hylo` composes production and consumption without making the intermediate
  fixed point part of its abstract meaning.

A paramorphism additionally gives an algebra both the recursive result and the
original substructure. It supports functions such as suffixes or operations
that need to retain a subtree:

```text
para : (F (Fix F, R) -> R) -> Fix F -> R
```

[Meijer, Fokkinga, and Paterson 1991](../30-sources/meijer-et-al-1991-functional-programming-bananas.md)
develop these schemes and their calculation laws. Catena should derive a
direct per-datatype `fold` and, where productive semantics are clear, `unfold`.
Generic `Fix`, `cata`, `ana`, `hylo`, and `para` belong in an advanced
recursion-schemes library.

The restriction matters. Negative, nested, indexed, abstract, cyclic, and
coinductive types do not all share the simple positive regular interface.

### Fusion is conditional

A familiar equation suggests eliminating an intermediate map:

```text
fold_map(g, map(f, xs)) == fold_map(g compose f, xs)
```

Parametricity and functor/fold laws support the extensional equation in the
appropriate pure fragment. They do not automatically establish equal
termination, allocation, strictness, exceptions, or effect order in full
Catena. A fusion optimization needs:

- a theorem for Catena's strict semantics and bottom behavior;
- purity or a proved effect-preservation condition;
- assurance that callback multiplicity and order are unchanged;
- a cost model showing that fusion is beneficial; and
- preservation of source-level debugging and diagnostics.

Hughes's lazy generator/selector examples demonstrate the modular benefit but
also depend on non-strict demand. A strict Catena needs explicit iterators,
streams, builders, or compiler fusion to obtain comparable space behavior.

## The combinator vocabulary of the seventeen classes

The existing
[category-theory synthesis](category-theory-for-programming.md) fixes the
initial class set and its minimal operations. This section identifies the
derived programming vocabulary. Derived functions should be implemented once
against the minimal interface.

| Class | Minimal operation | High-value derived combinators |
| --- | --- | --- |
| `Setoid` | `equivalent` | `not_equivalent`, equality-based membership with an explicit relation |
| `Ord` | `compare` | `<`, `<=`, `>`, `>=`, `min`, `max`, `clamp`, `comparing` |
| `Semigroup` | `combine` | `combine_all1`, nonempty intercalation, repetition with a positive count |
| `Monoid` | `empty` | `combine_all`, `fold_map`, endomorphism builders |
| `Foldable` | `fold_map` | `fold_left`, `fold_right`, `to_list`, `length`, `any`, `all`, `find` subject to strictness |
| `Functor` | `map` | `replace`, `void`, composition over nested functors |
| `Bifunctor` | `bimap` | `map_first`, `map_second` |
| `Apply` | `apply` | `product`, `lift2`, `lift3`, contextual tuple construction |
| `Applicative` | `pure` | arbitrary `liftN`, `sequence`, fixed-shape validation and collection |
| `Traversable` | `traverse` | `sequence`, effectful map, stateful accumulation via a suitable applicative |
| `Chain` | `chain` | `flatten`, unitless Kleisli composition, value-dependent sequencing |
| `Monad` | parent operations | Kleisli pipelines, `filterM`, dynamic replication, explicit workflow combinators |
| `Semigroupoid` | `compose` | directionally named pipeline aliases |
| `Category` | `identity` | generic identity pipelines and categorical reassociation helpers |
| `Arrow` | `lift`, `first` | `second`, split, fanout, pre/post composition |
| `Extend` | `extend` | `duplicate`, context-dependent mapping helpers |
| `Comonad` | `extract` | coKleisli composition and focused/contextual evaluation |

This table is a starting API, not a promise that every function can be derived
with the desired operational behavior.

### Value algebra combinators

`Semigroup` and `Monoid` justify regrouping, not reordering:

```text
combine(combine(x, y), z) == combine(x, combine(y, z))
```

`combine_all` may use a balanced tree for performance only if it preserves the
documented encounter order. Parallel evaluation additionally needs proof that
observable effects are absent and that the combining operation or scheduler
preserves required ordering. Commutativity is a distinct property not present
in the initial hierarchy.

`Ord.comparing(project)` should construct an explicit comparator or wrapper
instead of installing a second incoherent global `Ord` instance for the same
type. Likewise additive and multiplicative numeric monoids need explicit
wrappers or dictionaries.

### `Foldable` needs a short-circuit story

`fold_map` is elegant but, under strict evaluation, it does not automatically
make `any`, `all`, or `find` stop early. Catena needs one of:

```text
fold_while : (State -> A -> Control State Result)
          -> State
          -> T A
          -> Result

type Control S R = Continue S | Break R
```

or a documented iterator protocol. Encoding short-circuiting through lazy
monoids would reintroduce demand semantics indirectly and make costs harder to
read. The standard `Foldable` conveniences should say whether they traverse
the entire structure.

### Functor composition should be explicit

If both `F` and `G` are functors, `F (G A)` supports nested mapping:

```text
map_compose(f, x) = map(map(f), x)
```

A lightweight `Compose F G A` wrapper can carry the derived instance when
generic constraints require it. Catena should avoid implicit higher-kinded
instance synthesis that makes dictionary selection or error messages
unpredictable.

### Apply, Applicative, Chain, and Monad preserve different information

The signatures show a progression:

```text
apply : F (A -> B) -> F A -> F B
pure  : A -> F A
chain : M A -> (A -> M B) -> M B
```

- `Apply` combines contexts already present.
- `Applicative` can construct a context and describes a fixed computation
  graph.
- `Chain` lets an earlier value choose the later computation but has no unit.
- `Monad` supplies both unit and dynamic sequencing.

The standard library should place combinators at their weakest constraint:

```text
lift2    : Apply F => (A -> B -> C) -> F A -> F B -> F C
sequence : Applicative F => List (F A) -> F (List A)
flatten  : Chain M => M (M A) -> M A
```

Requesting `Monad` for `lift2` needlessly hides static independence and rejects
valid `Apply` instances.

### Traversal is the effectful structural map

For categorical laws, `Functor.map` should take a pure function:

```text
map : (A -> B) -> T A -> T B
```

An effectful visit uses:

```text
traverse : Applicative F => (A -> F B) -> T A -> F (T B)
```

or an explicit native-effect operation with its row and order visible:

```text
for_each : (A ->{e} Unit) -> T A ->{e} Unit
```

A compiler-derived traversal should visit every selected position exactly
once in declaration order. The generic `Traversable` laws do not, by
themselves, transparently guarantee every operational aspect of visitation;
[Gibbons and Oliveira 2009](../30-sources/gibbons-oliveira-2009-essence-iterator-pattern.md)
make that limitation explicit.

### Kleisli and coKleisli composition

For a monad:

```text
kleisli_compose : (A -> M B) -> (B -> M C) -> A -> M C
kleisli_compose(f, g, x) = chain(f(x), g)
```

This composes functions that return explicit computation values. It is useful
for parsers, state transitions, validation workflows with dependency, and
embedded plans. It is not necessary for composing ordinary Catena functions
whose native effects already appear in effect rows.

For a comonad:

```text
cokleisli_compose : (W A -> B) -> (W B -> C) -> W A -> C
cokleisli_compose(f, g, w) = g(extend(f, w))
```

This composes observations that require context. The concrete `W` determines
whether context means a zipper, history, neighborhood, annotated tree, or
another focused structure. The class name does not establish causality or
memory bounds; the representation and operations do.

### Arrow routing

From `lift` and `first`, an `Arrow P` derives:

```text
second : P A B -> P (C, A) (C, B)
split  : P A B -> P C D -> P (A, C) (B, D)
fanout : P A B -> P A C -> P A (B, C)
```

These operations preserve an analyzable computation representation while
routing product inputs. [Hughes 2000](../30-sources/hughes-2000-generalising-monads-arrows.md)
shows why this matters when an unrestricted host function would hide topology.
Catena's class belongs in the agreed hierarchy, but symbolic arrow notation
should wait until direct combinator use proves unreadable.

Sum routing for abstract arrows is additional structure, often called arrow
choice. Because it is not in the agreed initial hierarchy, sum combinators
should remain concrete or experimental rather than being smuggled into
`Arrow` without new laws.

## Worked ADT combinator families

### `Option`

```text
fold       : R -> (A -> R) -> Option A -> R
map        : (A -> B) -> Option A -> Option B
product    : Option A -> Option B -> Option (A, B)
and_then   : Option A -> (A -> Option B) -> Option B
or_else    : Option A -> (Unit -> Option A) -> Option A
to_result  : E -> Option A -> Result E A
```

`or_else` should take its fallback by thunk or another explicit delayed form
if constructing the fallback may be expensive or effectful. In a strict
language, an eager `Option A` argument would evaluate even when the first value
is `Some`.

### `Result` and validation

```text
fold       : (E -> R) -> (A -> R) -> Result E A -> R
map        : (A -> B) -> Result E A -> Result E B
map_error  : (E -> F) -> Result E A -> Result F A
bimap      : (E -> F) -> (A -> B) -> Result E A -> Result F B
and_then   : Result E A -> (A -> Result E B) -> Result E B
recover    : Result E A -> (E -> Result F A) -> Result F A
```

Two `apply` policies are both useful and must not share one incoherent
instance:

- fail fast at the first `Err`, agreeing with monadic `and_then`; or
- accumulate independent errors through a `Semigroup E`, usually in a
  distinct `Validation E A` wrapper.

The wrapper makes operational and algebraic intent visible. A type class should
not pick between these policies by import order.

### Recursive collections

A sequence-like API should distinguish:

```text
map         -- pure, shape/cardinality preserving
fold_left   -- strict accumulator, left-to-right
fold_right  -- structural right association; strictness documented
fold_map    -- map into a monoid and combine in encounter order
traverse    -- one applicative effect per element in encounter order
unfold      -- produce until the coalgebra returns a stop constructor
zip_exact   -- fail on different lengths
zip_shortest -- stop at the shorter input
```

One unqualified `zip` forces programmers to memorize a truncation policy.
Likewise `sort`, `group`, and `deduplicate` require order or equality evidence
and are algorithms over a concrete sequence, not consequences of `Functor`.

### List comprehensions are a control form, not another class method

An eager list comprehension combines nested iteration, filtering, local
bindings, and construction under one ordered evaluation contract. Its
list-to-list kernel can be explained with mapping, flattening, and empty-list
filtering, but that explanation does not justify a generic `Monad` surface:
filtering additionally needs a choice or zero operation, while generic carrier
methods would make effect order, cardinality, failure, and allocation harder to
see.

Catena should therefore elaborate a typed qualifier tree directly and keep
ordinary `map`, `flat_map`, `filter`, `traverse`, and explicit zip functions as
separate library operations. The proposed boundary and its algebraic evidence
are developed in [List Comprehensions](list-comprehensions.md).

## Domain combinator libraries

### Parser combinators: laws do not specify parsing policy

[Hutton and Meijer 1998](../30-sources/hutton-meijer-1998-monadic-parsing.md)
represent a parser as a function from input to possible `(value, remainder)`
results. `pure`, bind, failure, choice, and recursion then derive:

```text
satisfy, character, string
many, many1
separated_by
chain_left, chain_right
token, whitespace
```

This is compelling evidence for small combinator bases. It is also evidence
against specifying a parser only as “a Monad.” A production `Parser` must say:

- whether choice tries both branches, the first successful branch, or the
  second only before input is committed;
- whether ambiguity is preserved;
- how farthest errors, expected tokens, and source spans combine;
- whether a successful empty parser passed to `many` is rejected to prevent
  non-progress loops;
- how left recursion, memoization, streaming, and incremental input work; and
- the time and memory consequences of backtracking.

Catena should first build parser combinators on a concrete `Parser` type and
then expose the weakest categorical instances it genuinely satisfies.

### Optics: compose access without exposing representation

Concrete lenses, prisms, and traversals can provide:

```text
view    : Lens S A -> S -> A
set     : Lens S A -> A -> S -> S
over    : Lens S A -> (A -> A) -> S -> S
preview : Prism S A -> S -> Option A
review  : Prism S A -> A -> S
compose : Optic S A -> Optic A B -> Optic S B
```

Records naturally derive lenses; public ADT constructors naturally derive
prisms when visibility permits. Profunctor optics can make mixed optic kinds
compose through ordinary function composition, as shown by
[Pickering, Gibbons, and Wu 2017](../30-sources/pickering-et-al-2017-profunctor-optics.md).

The initial Catena strategy should generate concrete, discoverable accessors.
Adopt a profunctor encoding only if specialization removes abstraction
overhead and higher-rank diagnostics remain understandable.

### Modular sums of functors: powerful but not the nominal default

[Swierstra 2008](../30-sources/swierstra-2008-data-types-a-la-carte.md)
assembles expression syntax from:

```text
component functors
  + coproduct of components
  + fixed point
  + injection smart constructors
  + fold algebras
```

This can add new syntax cases and new interpretations modularly. The explicit
construction should be expressible in Catena. Automatic injection resolution
is harder: the paper's Haskell technique uses overlapping instance search and
has ambiguity around duplicate or nested components, conflicting with
Catena's coherent initial traits.

Use this encoding for deliberately extensible syntax and free computation
descriptions, not as a replacement for ordinary closed nominal domain ADTs.
Measure boilerplate and diagnostics before adding compiler-generated injection
evidence.

### Selective branching: a credible experiment outside the initial hierarchy

[Mokhov et al. 2019](../30-sources/mokhov-et-al-2019-selective-applicative-functors.md)
introduce:

```text
select : F (Either A B) -> F (A -> B) -> F B
```

The first computation decides whether the second is needed, but both possible
effects remain visible in the static program. Derived combinators include
`when`, `if`, branch, Boolean conjunction/disjunction, and effectful `any` and
`all`.

This is useful when an interpreter needs both dynamic skipping and static
analysis, such as build dependencies or remote-request graphs. It also has a
subtle contract: lawful analysis instances may deliberately record an effect
that concrete execution skips. “Selective” does not universally mean “lazy
second argument.”

The agreed seventeen-class Catena hierarchy does not contain `Selective`.
Concrete libraries should experiment first. A later class requires evidence
that `Applicative` is too weak, `Monad` hides valuable structure, and the
additional laws and diagnostics pay for themselves.

### Explicit computations alongside native handlers

Native algebraic effects do not make applicative, monadic, arrow, or free
combinator libraries obsolete. The two layers solve different problems:

- direct effect operations make ordinary effectful functions readable and
  track ambient capabilities;
- explicit computation values can be stored, analyzed, transformed, batched,
  interpreted more than once, or sent elsewhere.

A parser, query plan, build graph, or workflow may therefore be a `Monad` or
`Arrow` value even when executing it performs handled Catena effects. The API
must state when construction is pure and when interpretation performs effects.

## Evaluation and effect semantics

### Callback purity is part of the law

The usual functor law:

```text
map(g compose f) == map(g) compose map(f)
```

can change observable effect interleaving if `f` and `g` perform ambient
effects. Catena should state categorical laws over pure functions. An API that
accepts an effectful callback should expose and document the row:

```text
map_effectful : (A ->{e} B) -> T A ->{e} T B
```

and must not use the pure functor equation as an optimizer license.

The same applies to comparators, equivalence relations, fold algebras, optic
updates, parser semantic actions, and arrow lifting. The trait method may
construct an explicit effect value purely; interpreting that value is a
separate event.

### Order, multiplicity, and discard

Every higher-order combinator should document:

| Question | Example where it matters |
| --- | --- |
| Is the callback invoked once per position? | traversal, validation, logging |
| In what order are positions visited? | noncommutative applicatives, diagnostics |
| Can a branch be skipped? | `or_else`, parser choice, selective execution |
| Can work be duplicated? | backtracking parsers, fanout over computations |
| Can results be discarded while effects remain? | `void`, `replace`, failed alternatives |
| Can independent work run concurrently? | applicative queries, arrow graphs |
| What happens on cancellation or failure? | remote requests, resources, handlers |

Associativity usually permits regrouping an abstract operation. It does not
permit reordering, duplicate execution, speculative effects, or lost cleanup.

### Stack safety and large ADTs

A recursive fold expressed elegantly in source may overflow the machine stack
on a long strict list or skewed tree. Generated combinators need an explicit
implementation contract:

- which folds are tail recursive;
- whether tree traversals use an explicit work stack;
- maximum retained path or frontier;
- whether callbacks can suspend and resume;
- whether an iterator version streams; and
- whether compiler transformations preserve source stack traces.

“Derived by the compiler” should strengthen predictability, not exempt the
operation from cost documentation.

## Naming, placement, and elaboration

### Prefer words before punctuation

Research languages often accumulate operators such as `<$>`, `<*>`, `>=>`,
`***`, `&&&`, and `=<<`. They are concise after memorization but hostile to
search, speech, diagnostics, and unfamiliar readers.

Catena should begin with word names:

```text
map, apply, pure, traverse, chain
compose, identity, lift, first
extend, extract
```

One pipeline operator and perhaps one composition operator may earn special
syntax through broad use. Specialized packages can add local aliases without
making punctuation the normative documentation vocabulary.

### Qualify overloaded structural words

Use module or trait qualification when names carry different semantics:

```text
Option.fold
Tree.fold
Foldable.fold_map
Parser.apply
Apply.apply
Arrow.first
Tuple.first
```

Method resolution may permit concise calls when the type is obvious, but error
messages and documentation should preserve the qualified origin.

### Derived functions are not dictionary methods

Minimal dictionaries improve coherence and instance authoring. For example,
`Bifunctor` needs only `bimap`; `map_first` and `map_second` are library
functions. `Arrow` needs `lift` and `first`; `second`, split, and fanout are
derived once.

An instance may supply an optimized override only if the language can require
it to agree with the canonical definition. Otherwise two operations with the
same advertised law may silently diverge.

### Elaboration should preserve source combinators

Constraint solving turns a generic call into dictionary selection. The typed
core should retain:

- the source combinator identity;
- selected instance and derivation evidence;
- callback effect row;
- source datatype and field-order metadata; and
- any specialization or fusion decision.

This provenance lets diagnostics say “`traverse` requires `Applicative
Validation`” rather than exposing only a failed generated dictionary
application.

## Compiler combinators are a separate experiment

[Turner 1979](../30-sources/turner-1979-applicative-language-implementation.md)
eliminates bound variables into combinatory code. [Compiling to Categories](../30-sources/elliott-2017-compiling-to-categories.md)
translates typed functions into categorical combinators that can be interpreted
as circuits, derivatives, incremental programs, or analyses.

Both demonstrate that combinators can be a powerful IR boundary. Neither
justifies compiling the full initial Catena through one categorical form.
Experiments must measure:

- semantic coverage of recursion, effects, sums, higher-order values, and
  foreign calls;
- code-size growth from abstraction elimination;
- specialization and inlining requirements;
- preservation of source errors and debugging;
- equivalence with the ordinary backend; and
- target-specific escape hatches.

Source-level class design and backend IR selection should inform one another
without being coupled.

## Proposed Catena library tiers

### Tier 0: prelude

Provide universally readable operations:

```text
identity, compose, pipe
constant, curry, uncurry
pair_with, either, absurd
```

Keep `flip`, structural association, distribution, and similar adapters in a
discoverable structural module unless corpus evidence shows prelude-level use.

### Tier 1: categorical standard library

For the agreed seventeen classes:

- expose the minimal methods already selected;
- implement derived combinators once;
- state class and parent-compatibility laws;
- restrict the categorical law story to pure callbacks;
- publish evaluation order and multiplicity separately; and
- use explicit wrappers where one type supports several lawful dictionaries.

### Tier 2: datatype-derived modules

For each public nominal ADT, conditionally generate:

- constructor-complete `fold`;
- `map` or `bimap` for covariant parameters;
- `fold_map` and `traverse` for selected element positions;
- regular recursive `fold` and perhaps `unfold`;
- concrete lenses for public record fields; and
- concrete prisms for public constructors.

Generated names live under the type's module. Each derivation records field
order, positivity, regularity, and visibility assumptions.

### Tier 3: focused packages

Prototype separately:

- recursion schemes (`Fix`, `cata`, `ana`, `hylo`, `para`);
- parser combinators with explicit commit and error semantics;
- optics and possible profunctor representation;
- modular sums of functors and explicit injections;
- free applicative, selective, monadic, or arrow computation descriptions;
- dataflow and coKleisli libraries; and
- iterator/stream protocols for strict producer-consumer composition.

### Tier 4: compiler research

Keep combinatory-logic lowering and categorical compilation behind typed IR
experiments. They must not change source semantics or surface vocabulary.

## Worked selection guide

Choose by the dependency the program actually needs:

| Need | Weakest likely operation |
| --- | --- |
| Transform every payload without changing shape | `map` |
| Transform both error and success positions | `bimap` |
| Combine two already-present independent contexts | `apply` / `lift2` |
| Introduce a pure value into that context | `pure` |
| Visit an ADT while accumulating fixed-shape effects | `traverse` |
| Let an earlier explicit result choose the later computation | `chain` |
| Compose typed non-function computations | semigroupoid `compose` |
| Lift functions and route paired inputs through an analyzable graph | arrow combinators |
| Compute from a focused neighborhood or history | `extend` / coKleisli composition |
| Consume every constructor recursively | datatype `fold` / `cata` |
| Produce a regular recursive value from a seed | `unfold` / `ana` |
| Access or update nested data compositionally | lens/prism/traversal |
| Try grammar alternatives with domain-specific failure | parser choice, not generic sum `either` |
| Skip a statically visible possible effect | experimental `select` |

When several rows apply, prefer the weakest constraint that retains the
structure a caller or interpreter can exploit.

## Claims to reject

### “Combinator” means point-free code

Point-free style is one possible presentation. A named lambda can be a clearer
use of the same composition. Removing variables is not the goal; exposing a
stable compositional boundary is.

### Every useful helper should become a class method

Large dictionaries duplicate derived behavior, increase coherence obligations,
and burden instance authors. Minimal methods plus standardized derived
functions give one law-bearing definition.

### `map` should allow arbitrary effects because callbacks are functions

That erases the assumptions behind functor laws and hides order and
multiplicity. Pure `map`, applicative `traverse`, and an explicitly effectful
iterator are different contracts.

### Associativity permits parallel execution

Associativity permits regrouping. Parallel execution also needs purity,
resource safety, and either commutativity or an order-preserving schedule.

### Monads are the universal combinator interface

Monad power can hide static structure available through `Apply`,
`Applicative`, selective computation, or `Arrow`. Native effectful functions
also compose without being encoded as monadic values.

### ADTs should be represented by their Church encoding

The elimination representation is semantically illuminating. It is not a
default substitute for nominal identity, constructor visibility, coverage
diagnostics, direct pattern matching, and optimized physical layout.

### Lawful combinators are automatically cheap

Extensional equations do not fix allocation, stack use, input retention,
backtracking, memoization, effect order, or cancellation. Parser combinators
and profunctor optics make this distinction especially visible.

### The agreed hierarchy should immediately add `Selective`

Selective functors supply valuable evidence, but the initial hierarchy is an
existing design commitment. A new class needs its own corpus and coherence
case; concrete experimental operations can proceed without revising the core.

## Tradeoffs and falsification criteria

| Proposal | Evidence that would weaken or falsify it |
| --- | --- |
| Keep the prelude small and word-named | representative code is dominated by verbose structural plumbing that a stable operator vocabulary makes substantially clearer |
| Keep categorical methods pure | an effect-polymorphic law theory preserves the same equations, diagnostics, and optimizer safety without forcing `traverse`-like structure |
| Derive per-ADT folds and traversals | generated APIs are rarely used, are larger than direct matches, or obscure constructor-level errors |
| Put generic recursion schemes in a package | a broad corpus repeatedly reimplements them and direct matching produces worse maintenance and fusion results |
| Keep short-circuiting outside plain `fold_map` | a strict, lawful encoding gives predictable early termination without hidden laziness or extra control structure |
| Use coherent explicit wrappers for competing instances | wrapper noise exceeds ambiguity costs and another resolution discipline proves stable and understandable |
| Keep sum-of-functor encodings advanced | ordinary language-extension code cannot remain modular with nominal ADTs, rows, modules, and generated visitors |
| Experiment with selective operations before adding a class | multiple independent libraries need generic `select`, share laws, and retain materially useful static analysis |
| Generate concrete optics first | mixed optic composition dominates the corpus and the profunctor form specializes well with usable type errors |
| Keep categorical/combinatory IR internal | users need first-class alternate interpretations that cannot be provided by typed library or staged compilation interfaces |

## Research and implementation agenda

1. Specify purity and effect-row quantification for every class method and
   derived higher-order combinator.
2. Implement the seventeen minimal dictionaries and generate the derived
   vocabulary from one reference library.
3. Add conditional ADT derivation for `map`, `bimap`, constructor `fold`,
   `fold_map`, and `traverse`, with positivity and order diagnostics.
4. Define an iterator or `fold_while` protocol for stack-safe early termination
   in the strict language.
5. Build law suites that distinguish class laws, parent compatibility,
   datatype-derived guarantees, and domain operational laws.
6. Measure direct matches, per-datatype folds, generic recursion schemes, and
   iterators on representative list, tree, syntax, and graph-shaped programs.
7. Prototype a parser library with explicit consumption, commitment, error,
   progress, and backtracking contracts; benchmark against a generated parser.
8. Generate concrete lenses and prisms, then compare a profunctor encoding on
   mixed composition, specialization, compile time, and diagnostics.
9. Prototype explicit sum-of-functor syntax without overlapping traits; record
   injection boilerplate and ambiguity.
10. Test selective operations on a build graph or remote-query DSL before
    proposing any change to the seventeen-class hierarchy.
11. Verify that direct algebraic handlers compose predictably with iterator,
    traversal, parser, and explicit computation combinators.
12. Compare the ordinary typed backend with a restricted categorical or
    combinatory IR on code size, optimization, proof burden, and source
    debugging.

The active decision record is
[Which Combinators Should Catena Provide and Derive?](../40-inquiries/which-combinators-should-catena-provide-and-derive.md),
and the evidence trails are organized in the
[Combinators for Algebraic Data and Categorical Programming map](../10-maps/combinators-for-algebraic-data-and-categorical-programming.md).
