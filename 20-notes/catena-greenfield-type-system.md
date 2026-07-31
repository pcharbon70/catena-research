---
title: "A Greenfield Type System for Catena"
kind: note
created: "2026-07-31"
maturity: developing
tags:
  - bidirectional-typing
  - catena
  - effect-rows
  - language-design
  - principal-types
  - trait-constraints
  - type-inference
aliases:
  - "Greenfield Catena type system"
  - "What Catena should have been"
---

# A Greenfield Type System for Catena

## Executive conclusion

Catena should have been an inference-first, statically typed functional
language with a deliberately small semantic promise:

> Ordinary programs receive complete, principal rank-1 type inference. Richer
> programs remain sound and predictable by crossing explicit annotation
> boundaries, never by silently weakening that promise.

That points to a layered type system:

1. a strict, immutable-by-default core with algebraic data, pattern matching,
   parametric polymorphism, and principal Hindley–Milner inference;
2. structural records and variants through kinded rows with explicit lacks
   constraints, not nominal subtyping;
3. coherent traits represented as qualified types and elaborated to explicit
   evidence;
4. nominal algebraic effects tracked by a distinct effect-row theory, with
   lexical effect capabilities, deep affine resumptions, and effect-directed
   generalization;
5. higher-rank polymorphism available only through explicit `forall` types and
   bidirectional checking;
6. public module signatures as stable contracts, even when private definitions
   are inferred.

The design should exclude implicit subtyping, overlapping instances, local
instances, inferred polymorphic recursion, unrestricted type-level functions,
and first-class resumptions from its initial language. Each creates ambiguity,
coherence, termination, or generalization obligations disproportionate to its
early value.

This is not a retrofit. It intentionally uses no specification, source code,
test, or design constraint from another Catena repository. “Catena” is treated
here as an unused language name.

## Research reset and decision standard

The evidence trail is restricted to independent primary works. Classic HM
supplies the principal rank-1 core; qualified types and functional dependencies
bound trait inference; row calculi motivate structural data; Koka supplies one
worked effect-row design; bidirectional typing supplies an annotation-directed
path to higher-rank types; and OutsideIn(X) shows where local assumptions make
apparently natural inference lose principal results.

Recommendations are evaluated against five criteria:

- **semantic safety** — accepted programs satisfy a declarative type-and-effect
  system with an explicit dynamic semantics;
- **predictability** — inference returns one principal result in its promised
  fragment and annotations have a documented, local role elsewhere;
- **composability** — library authors can state abstractions without exposing
  implementation choices or solver order;
- **diagnosability** — failures retain enough constraint provenance to explain
  the relevant program relationship;
- **implementability** — each solver has a terminating algorithm and a testable
  contract before its feature enters the language.

“Expressive” is not an independent license to add mechanisms. A feature earns
its place when it solves repeated programming problems without making the
language's guarantees conditional on undocumented heuristics.

## The language at a glance

Catena's semantic center should be expression-oriented and strict:

```text
values       immutable by default
data         nominal algebraic data plus structural rows
functions    A ->{e} B, with A -> B as the pure abbreviation
polymorphism implicit rank 1; explicit predicative forall at signatures
overloading  coherent traits, elaborated to dictionaries
effects      nominal operations, lexical capabilities, and deep open handlers
modules      explicit public signatures; inferred private bodies
```

An ordinary function should look lightweight:

```text
let id = fn x -> x
-- id : forall a. a -> a
```

Effects should remain visible in higher-order types without burdening pure
code:

```text
map : forall a b e. (a ->{e} b) -> List a ->{e} List b
```

Traits should express capability requirements rather than trigger hidden type
choices:

```text
sort : forall a. Ord a => List a -> List a
```

A higher-rank boundary should be explicit:

```text
apply_to_both : (forall a. a -> a) -> (Int, Bool)
```

The language can infer calls to these declarations, but checking a term against
the nested `forall` is guided by the annotation.

## Guarantee matrix

The manual and compiler should publish a feature matrix rather than use
“supports inference” as an undifferentiated claim.

| Fragment | User contract | Required boundary |
| --- | --- | --- |
| Rank-1 functions, products, nominal algebraic data, nonrecursive `let` | Sound, complete, terminating, principal inference | None |
| Mutually recursive binding groups | Principal monomorphic inference inside the group; generalization after the group | Signature required for polymorphic recursion |
| Unique-label record and variant rows | Principal qualified inference if row solving is unitary and terminating | Annotation when a row constraint remains ambiguous |
| Single-parameter traits | Principal qualified types and coherent evidence | Reject ambiguous or overlapping evidence |
| Multi-parameter traits | Sound, terminating improvement only for declared dependencies | Explicit dependency declaration and coverage checks |
| Algebraic effect rows | Principal type-and-effect inference for the specified row theory | Effectful expansive bindings are not generalized; instance identity and resumption multiplicity remain explicit |
| Higher-rank predicative polymorphism | Sound and complete bidirectional checking | Explicit `forall` annotation at polymorphic boundaries |
| GADTs or local equality assumptions | Sound annotation-directed checking only | Signature at the enclosing binding; no promised local generalization |
| Type-level computation or associated type equations | Not in the initial language | Future design requires a terminating, confluent solver |

This partition is the core design. It lets the simple language remain genuinely
simple even after expert-only features arrive.

## 1. Principal rank-1 inference is the default

The implicit fragment should use ordinary type schemes:

```text
monotype  t ::= a | C | t ->{e} t | C t ... t | Record r | Variant r
scheme    s ::= forall q1 ... qn. P => t
context   G ::= name : s
```

`q` ranges over kinded variables, including value types and rows. `P` contains
only the trait and row predicates allowed by the relevant solver.

For the unqualified core, the essential boundary remains:

```text
generalize(G, t) = forall (ftv(t) - ftv(G)). t
```

The actual operation must receive the substituted environment and substituted
result. Each variable use instantiates quantified variables freshly. Function
parameters remain monomorphic. A recursive strongly connected component gets
fresh monomorphic placeholders, is inferred as a unit, and is generalized only
after leaving the component.

These rules are not implementation preferences. They are the conditions under
which the classic result described in
[How Hindley–Milner Type Inference Works](hindley-milner-type-inference.md)
provides a principal scheme.

### Public signatures

Private definitions may rely on inference. Every exported definition should
have a signature, checked against its implementation. This gives modules three
properties that global inference cannot:

- a stable API that does not change when private code is refactored;
- separate compilation without re-inferring downstream modules;
- an intentional place for higher-rank quantification, effect abstraction, and
  trait constraints.

The compiler may suggest the inferred signature, but source control should
record the author's accepted interface.

## 2. Kinds keep solver domains separate

Catena should distinguish at least:

```text
Type
Type -> Type
RecordRow
VariantRow
EffectRow
```

Every flexible variable carries a kind, and every substitution preserves it.
This keeps value types, type constructors, structural rows, and effect rows
from being accidentally unified just because their runtime representation is
similar.

Higher-kinded parameters such as `f : Type -> Type` can remain compatible with
first-order inference when type constructor application is rigid and the type
language has no unrestricted lambdas or reduction. Catena should therefore
support higher-kinded variables before it supports general type-level
computation.

## 3. Structural data uses rows, not subtyping

Catena should combine nominal algebraic data with structural records and
variants. Nominal data gives domain concepts stable identities; structural rows
make adapters and data plumbing compositional.

Representative types are:

```text
{ name : String, age : Int | r }
< Ready : Unit, Failed : Error | v >
```

Records and variants use different row kinds even if they share unification
infrastructure. Labels are unique. Extending row `r` with `name` therefore
generates a predicate stating that `r` lacks `name`, following
[Gaster and Jones](../30-sources/gaster-jones-1996-extensible-records-variants.md).

Catena should not add implicit width or depth subtyping on top of rows. Row
polymorphism already expresses “has at least these fields” while preserving an
equality-based inference story. Explicit conversion functions are clearer when
data representation really changes.

First-class labels should wait. Fixed labels cover selection, update,
extension, restriction, injection, and case analysis without adding another
runtime evidence language.

## 4. Traits are coherent qualified types

A trait constraint changes a scheme from `forall a. t` to
`forall a. P => t`. The constraint is part of the type, and compiling it
requires evidence—normally a dictionary containing the selected methods.

The initial trait system should impose all of these rules:

- one principal dispatch type per trait;
- globally non-overlapping instances;
- an instance must be declared with either the trait or the head type, avoiding
  unrelated orphan instances;
- no local instances whose evidence depends on lexical search order;
- superclass expansion and instance reduction must pass a structural
  termination check;
- a constrained variable must be determined by the visible type, or the
  declaration is rejected as ambiguous;
- evidence terms are part of the elaborated core and coherence is a semantic
  property, not merely deterministic compiler behavior.

This is intentionally less permissive than many mature type-class systems.
[Jones's qualified-type theory](../30-sources/jones-1994-theory-of-qualified-types.md)
shows that principal qualified schemes still need ambiguity and coherence
conditions. A deterministic solver can consistently choose the wrong semantic
contract if overlapping evidence was allowed in the first place.

### Multi-parameter traits

Multi-parameter traits should not be present in the first release. When a
repeated library need justifies them, every trait relation must declare which
parameters determine which others:

```text
trait Collection c a | c -> a
```

The solver may then improve types only according to those declared functional
dependencies. Instance consistency, coverage, and termination checks must ship
with the feature. [Jones 2000](../30-sources/jones-2000-functional-dependencies.md)
demonstrates why the dependency is necessary; it is not a proof that an
unrestricted relational trait language will terminate.

Associated type equations, overlapping instances, and user-selected incoherent
resolution should remain outside the language until Catena has a written use
case that outweighs their impact on principality and modularity.

## 5. Effects have their own row theory

The full semantic and implementation design is developed in
[Algebraic Effects and Handlers](algebraic-effects-and-handlers.md). The type
row described here is only one layer: it tracks requests that may escape, but
does not by itself choose a handler, define resumption depth, or make captured
resources safe to duplicate.

Catena should model each algebraic operation as a member of a nominal effect
signature and a function's latent signature occurrences as a row:

```text
A ->{<Console, State s | e>} B
```

Pure functions abbreviate the empty row. Higher-order functions quantify the
tail, so they preserve the effects of callbacks rather than erasing them.

Effect rows should permit duplicate labels and handlers should remove one
occurrence. [Koka's effect-row calculus](../30-sources/leijen-2014-koka-row-polymorphic-effects.md)
shows why this choice can retain a most-general solution for effect elimination
without introducing lacks constraints into every handler type.

This does **not** mean every row in Catena shares multiset semantics:

| Row domain | Equality discipline | Reason |
| --- | --- | --- |
| Records and variants | Unique labels plus lacks predicates | Two fields or alternatives with one name are not meaningful |
| Effects | Duplicate labels permitted; handler removes one occurrence | Open effect elimination otherwise admits incomparable set-row solutions |

The implementation may share traversal, substitution, and kind-checking code,
but the declarative theories remain distinct.

### Generalization in a strict language

Unrestricted `let` generalization is unsound when evaluating the right-hand
side creates shared state or captures control. Catena should use a simple,
effect-aware rule:

1. syntactic values may be generalized because evaluating the binding itself
   performs no effect; a function's body effects remain latent on its arrow;
2. an expansive expression may be generalized only when its inferred immediate
   effect row is provably empty;
3. otherwise the binding remains monomorphic unless the programmer introduces
   an explicit abstraction that makes sharing intentional.

This combines the safety lesson of
[Wright's value restriction](../30-sources/wright-1995-simple-imperative-polymorphism.md)
with the additional precision available from effect inference. “Appears pure”
must mean provably empty in the formal effect system, not absence of a syntactic
operation in one compiler pass.

### Handler identity, depth, and resumptions

An effect declaration should have nominal identity, and each use that requires
distinction—two `State Int` cells, for example—should receive a lexically bound
capability. Surface syntax may infer a unique ambient capability, but two
matching capabilities must be an ambiguity error rather than silently making
handler nesting choose identity. Higher-order code polymorphic in an effect
must not intercept that effect unless its type gives it the corresponding
authority.

Handlers should be open and deep by default. Unmentioned operations forward to
the outer context, while invoking a resumption reinstalls the current handler
for subsequent matching requests. Operations performed directly by a handler
clause follow the documented outer lookup rule; this behavior must appear in
the operational semantics rather than emerge from the backend.

A resumption should exist only as an affine, lexically scoped parameter of an
operation clause. A clause may discard it or invoke it once. It cannot escape,
be stored, be returned, or be generalized as an ordinary value, and a second
invocation must be rejected or trap before duplicated user computation.

First-class, shallow, or multi-shot resumptions could be designed later, but
they need separate answers for control-flow linearity, resource lifetime,
effect masking, continuation copying, and polymorphic generalization. Scoped
operations such as `local`, `catch`, and `bracket` likewise need a higher-order
or structured-scope design rather than being assumed to follow from
first-order effect signatures.

## 6. Higher-rank polymorphism is annotation-directed

Rank-1 inference covers most generic library code but cannot express a
function argument that must itself be polymorphic. Catena should support
predicative higher-rank types using two typing modes:

```text
G |- expression => type    -- synthesize
G |- expression <= type    -- check
```

An explicit annotation introduces and scopes nested `forall` variables.
Applications instantiate as needed; lambdas can check against a known function
type. The approach follows
[Dunfield and Krishnaswami](../30-sources/dunfield-krishnaswami-2013-bidirectional-typechecking.md)
rather than pretending Algorithm W can infer arbitrary System F terms.

The boundary should be visible in the language reference:

- unannotated code synthesizes only rank-1 schemes;
- a higher-rank value is introduced or consumed through a signature;
- quantifiers instantiate only with monotypes in the initial predicative
  system;
- polymorphic recursion requires a signature and is checked, never inferred.

This is a usability feature as much as a theoretical boundary: annotations
appear where local inference needs information, not everywhere.

## 7. GADTs and local equalities are a later checked fragment

Generalized algebraic data types can refine types during pattern matching, but
those local equality assumptions can eliminate principal types. OutsideIn(X)
demonstrates that a natural declarative relation may admit incomparable valid
typings and that arbitrary local `let` generalization becomes difficult to
specify.

Catena should therefore launch with ordinary algebraic data types. If GADTs are
later admitted:

- the enclosing function requires a signature;
- branch-local equalities are represented as scoped implication constraints;
- bindings under local equalities are not implicitly generalized;
- the compiler accepts only cases for which its documented solver produces a
  principal result;
- the manual describes this as annotation-directed checking, not complete
  inference.

[OutsideIn(X)](../30-sources/vytiniotis-et-al-2011-outsidein.md) supports this
boundary but does not require Catena to inherit Haskell's entire constraint
language.

## 8. The compiler elaborates into a small typed core

The surface language should desugar into a typed intermediate language where
all formerly implicit choices are explicit:

- type abstraction and application for generalized variables;
- dictionary parameters and selections for traits;
- row evidence where structural operations require it;
- effect operations and handler boundaries;
- explicit coercions only where the declarative system names one.

An effective pipeline is:

```text
parse and resolve names
  -> kind-check declarations and signatures
  -> generate typed constraints with source origins
  -> solve type equalities
  -> solve record/variant row predicates
  -> simplify trait predicates and construct evidence
  -> solve effect rows and apply the generalization policy
  -> ambiguity and escape checks
  -> elaborate to typed core
  -> verify the elaborated term
```

The implementation may interleave these steps for performance. It must still
be possible to state each solver's inputs, outputs, and invariants separately.
The executable clarity of
[Typing Haskell in Haskell](../30-sources/jones-1999-typing-haskell-in-haskell.md)
is a useful model; its particular Haskell policies are not requirements.

### Constraint provenance

Every generated equality or predicate should retain:

- the source span that generated it;
- the language rule involved, such as application or record selection;
- parent constraints from which it was derived;
- the solver and evidence decision that discharged it.

Diagnostics can then explain relationships rather than dump internal variable
names. Provenance must survive substitution and simplification, because the
final conflicting types are often far from the syntax that connected them.

## Rejected alternatives

### Infer everything

Unrestricted inference for higher-rank polymorphism, local equality
assumptions, type-level equations, and polymorphic recursion is not one coherent
feature. Some combinations are undecidable; others lack principal types or
force compiler-specific heuristics. An explicit annotation boundary gives a
stronger and more honest language.

### Add subtyping for convenience

Subtyping changes inference from equality solving to a constraint problem with
variance and potentially incomparable solutions. Structural rows and explicit
conversion functions cover the initial data-shaping needs while preserving a
clear generality order.

### Make every extension a trait

Traits are appropriate for coherent ad-hoc operations, not arbitrary type-level
computation, record presence, effects, conversions, or implicit values. Giving
each domain its own judgment keeps the solver contracts understandable.

### Use one row representation and one equality for everything

Rows are a representation pattern, not a universal semantics. Unique record
fields and duplicate effect labels solve different problems. Sharing code is
useful; conflating the theories is not.

### Expose resumptions as ordinary values immediately

Unrestricted first-class control values multiply the obligations around
linearity, sharing, and generalization before ordinary handlers are proven
useful. Lexically scoped affine resumptions are a smaller semantic target.

## Development sequence

The type system should be delivered as proofs and executable models before it
is delivered as a large surface language.

### Stage 0 — semantic kernel

- Define the expression calculus, values, evaluation order, and errors.
- Specify declarative rank-1 typing and Algorithm W.
- Prove or mechanize substitution, preservation, progress, soundness,
  completeness, and principality for the pure core.
- Build an intentionally small reference inferencer.

### Stage 1 — language core

- Add nominal algebraic data, patterns, recursive binding groups, and modules.
- Require public signatures and check separate compilation.
- Differentially test a production inferencer against the reference model.
- Stabilize source-origin diagnostics.

### Stage 2 — independent qualified domains

- Add unique-label record and variant rows with lacks predicates.
- Add single-parameter coherent traits and dictionary elaboration.
- Prove termination and ambiguity checks for each solver separately.
- Do not add multi-parameter traits until real library code demonstrates need.

### Stage 3 — effects

- Define the operational semantics of algebraic operations and handlers.
- Add duplicate-label effect rows and prove the chosen unifier most-general.
- Prove the generalization restriction sound for the evaluation semantics.
- Add nominal signatures and lexical instance capabilities, then test the
  handler-selection rule against higher-order accidental capture.
- Keep handlers deep and open, and resumptions lexical and affine.
- Keep scoped resource and concurrency operations outside the first-order
  handler core until cancellation and cleanup are specified.

### Stage 4 — explicit advanced typing

- Add bidirectional higher-rank checking.
- Consider GADTs only with scoped implication constraints and mandatory
  signatures.
- Evaluate any type-level computation as a separate language proposal with its
  own termination and confluence story.

Each stage should ship only after its declarative system, solver contract,
elaboration, negative examples, and property tests agree.

## Verification obligations

At minimum, the project should test and, where feasible, prove:

- substitution identity, composition, and kind preservation;
- unifiers make both inputs equal and are most-general in their domain;
- occurs checks reject cyclic type and row solutions;
- generalization quantifies nothing free in the substituted environment;
- two instantiations of a scheme share no freshly quantified variables;
- inferred rank-1 schemes are invariant under alpha-renaming and irrelevant
  traversal choices;
- every alternative core typing is an instance of the inferred scheme;
- trait resolution terminates and elaborates unambiguous programs to
  observationally equivalent evidence;
- row operations respect uniqueness or duplicate-label semantics according to
  their kind;
- effectful expansive bindings cannot recreate a polymorphic-reference or
  polymorphic-control counterexample;
- handler reduction preserves the declared type and effect;
- a higher-order effect-polymorphic function cannot accidentally intercept its
  callback's effects;
- lexical effect instances cannot escape their handler or become ambiguous by
  nesting order;
- affine resumptions cannot duplicate captured resources or execute twice;
- accepted higher-rank programs check in the declarative bidirectional system;
- typed-core verification succeeds independently of surface inference.

Generated small terms and bounded declarative search are valuable supplements
to proof. They are not substitutes for naming the theorem being tested.

## Falsification criteria

The design should be narrowed if any claimed principal fragment admits:

- two valid typings with no common most-general scheme;
- solver output that changes under constraint or traversal order;
- a typable unannotated term rejected by the promised complete inferencer;
- a quantified variable fixed by the surrounding substituted environment;
- two valid trait evidence terms with observably different behavior;
- row solving that diverges or returns incomparable solutions;
- an effectful binding that is generalized and becomes type unsafe;
- a well-typed closed term that becomes stuck outside a declared runtime error;
- an elaborated core term rejected by the independent core verifier.

The appropriate response is to shrink the implicit fragment or require an
annotation, not to quietly add a solver heuristic.

## What remains open

The architecture is specific enough to guide a prototype, but several choices
still require formal and user-level evaluation:

- exact surface syntax for quantified variables, rows, effects, and handlers;
- whether structural variants earn their complexity alongside nominal data;
- the minimal termination check for trait instance contexts;
- the exact integration of duplicate-label rows with lexical effect-instance
  identities;
- whether affine resumptions require core linear typing, a runtime consumed
  token, or both;
- which scoped computations need higher-order effects and which must be
  structured runtime primitives;
- how much inferred information the compiler should print in public-signature
  suggestions;
- what diagnostic provenance representation survives optimization without
  excessive memory use.

These are tracked in
[What Should a Greenfield Catena Type System Guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
and the focused
[algebraic-effect semantics inquiry](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md).

## Source trail

### Principal inference

- [Hindley 1969](../30-sources/hindley-1969-principal-type-scheme.md) — the
  principal-scheme property.
- [Milner 1978](../30-sources/milner-1978-type-polymorphism.md) — the
  programming-language discipline and Algorithm W.
- [Damas and Milner 1982](../30-sources/damas-and-milner-1982-principal-type-schemes.md)
  — soundness, completeness, and principality for the rank-1 `let` core.

### Qualified and structural extensions

- [Jones 1994](../30-sources/jones-1994-theory-of-qualified-types.md) —
  qualified schemes, evidence, ambiguity, and coherence.
- [Gaster and Jones 1996](../30-sources/gaster-jones-1996-extensible-records-variants.md)
  — record and variant rows with lacks predicates.
- [Jones 2000](../30-sources/jones-2000-functional-dependencies.md) — explicit
  dependencies and improvement for multi-parameter classes.

### Effects and advanced checking

- [Wright 1995](../30-sources/wright-1995-simple-imperative-polymorphism.md) —
  why strict effects constrain generalization.
- [Leijen 2014](../30-sources/leijen-2014-koka-row-polymorphic-effects.md) —
  duplicate-label effect rows and effect-directed generalization.
- [Dunfield and Krishnaswami 2013](../30-sources/dunfield-krishnaswami-2013-bidirectional-typechecking.md)
  — bidirectional higher-rank polymorphism.
- [OutsideIn(X)](../30-sources/vytiniotis-et-al-2011-outsidein.md) — constraint
  scoping and the loss of principal types under local assumptions.

## Connections

- [Catena Type-System Design](../10-maps/catena-type-system-design.md) provides
  the shortest reading paths through the proposal and its evidence.
- [Hindley–Milner Type Inference](../10-maps/hindley-milner-type-inference.md)
  isolates the mathematical foundation from this language-design synthesis.
- [Algebraic Effects and Handlers](../10-maps/algebraic-effects-and-handlers.md)
  routes through the semantic and implementation choices behind Stage 3.
