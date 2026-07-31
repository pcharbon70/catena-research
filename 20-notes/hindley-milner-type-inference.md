---
title: "How Hindley–Milner Type Inference Works"
kind: note
created: "2026-07-31"
maturity: developing
tags:
  - algorithm-w
  - hindley-milner
  - let-polymorphism
  - principal-types
  - type-inference
aliases:
  - "Hindley–Milner type inference"
  - "HM inference"
---

# How Hindley–Milner Type Inference Works

## Executive conclusion

Hindley–Milner inference is four cooperating mechanisms:

1. assign fresh type unknowns to facts not yet known;
2. solve equality requirements with most-general unification;
3. at a `let`, generalize only unknowns not fixed by the surrounding
   environment; and
4. at every use of a polymorphic binding, instantiate its quantified variables
   freshly.

For the classic rank-1 core, Algorithm W is sound and complete and computes a
**principal type scheme**: every other valid type is a substitution instance of
the inferred result. This is a precise theorem about a small language, not a
label that transfers automatically to traits, effects, subtyping, higher-rank
types, or local equality assumptions.

This note is deliberately implementation-independent. It contains no evidence
or constraints imported from any Catena repository. Its role is to establish
the mathematical baseline used by
[A Greenfield Type System for Catena](catena-greenfield-type-system.md).

## Scope and terminology

“Correct inference” separates four properties:

- **soundness** — an inferred typing is derivable in the declarative system;
- **completeness** — every term typable in the promised fragment is accepted;
- **principality** — every other valid typing is an instance of the inferred
  scheme;
- **termination** — inference decides the fragment rather than merely being
  sound when it returns.

[Milner 1978](../30-sources/milner-1978-type-polymorphism.md) supplies the
programming-language discipline and Algorithm W.
[Damas and Milner 1982](../30-sources/damas-and-milner-1982-principal-type-schemes.md)
prove completeness and the principal-type result for the `let` core.
[Hindley 1969](../30-sources/hindley-1969-principal-type-scheme.md) establishes
the earlier principal-scheme foundation in combinatory logic.

The note covers variables, functions, application, nonrecursive `let`,
substitutions, first-order unification, and the standard boundary around
recursive groups. It then identifies additional obligations introduced by
qualified constraints, kinds, rows, effects, and richer polymorphism.

## Formal objects

A minimal presentation distinguishes monotypes from schemes:

```text
monotype  t ::= a | C | t -> t | C t ... t
scheme    s ::= forall a1 ... an. t
context   G ::= name : s
```

- A variable such as `a` is a flexible unification unknown.
- A constructor such as `Int`, `Bool`, or `List` is rigid.
- A monotype contains no nested `forall`.
- A scheme quantifies zero or more variables at the outermost level.
- A typing context maps term names to schemes.

The difference between a free unknown and a quantified variable is semantic.
In `a -> a`, the two appearances must receive the same eventual solution. In
`forall a. a -> a`, each use of the scheme can choose a fresh instance.

For a type-like object `X`, write `ftv(X)` for its free type variables. The
central operations are:

```text
generalize(G, t) = forall (ftv(t) - ftv(G)). t

instantiate(forall a1 ... an. t)
  = [fresh b1/a1, ..., fresh bn/an]t
```

Subtracting `ftv(G)` prevents a local scheme from quantifying an unknown fixed
by an enclosing scope.

## Declarative typing before algorithms

Typing rules state which programs are valid; an inference algorithm searches
for a derivation. A compact declarative core has these essential rules:

| Form | Essential condition |
| --- | --- |
| Variable `x` | Use an instance of `G(x)` |
| Lambda `fn x -> e` | Give `x` a monotype and type `e` under that assumption |
| Application `f x` | The type of `f` must equal `type(x) -> result` |
| Let `let x = e1 in e2` | Type `e1`, generalize relative to `G`, and type `e2` with that scheme |

The declarative relation may permit generalization and instantiation at several
points. Algorithm W makes the process syntax-directed: it instantiates at
variables and generalizes at `let`.

An implementation is sound if every answer corresponds to a declarative
derivation. It is complete if it finds an answer whenever the declarative
system has one. Without a declarative system, tests can compare two programs
but cannot define principality.

## Unification is the equality solver

Application generates an equation rather than guessing a concrete type. If
`f : tf`, `x : tx`, and `b` is a fresh result unknown, inference requires:

```text
tf ~ tx -> b
```

A unifier is a substitution making both sides equal. A **most general unifier**
(MGU) commits only to structure forced by the equations; every other unifier
can be expressed by applying a further substitution to it. This property is a
key ingredient of principal inference.

A first-order unifier repeatedly applies a small set of rules:

- identical types need no work;
- applications of the same rigid constructor decompose componentwise;
- distinct rigid constructors fail;
- a variable `a` may bind to `t` only if `a` does not occur in `t`;
- each new substitution is applied to the remaining equations.

The occurs check rejects an infinite equation such as:

```text
a ~ a -> b
```

Without recursive types, no finite type satisfies it. The term `fn x -> x x`
creates exactly this equation.

Substitution composition order matters. If `S1` was learned first and `S2`
later under `S1`, composition must satisfy:

```text
apply(S2 after S1, t) = apply(S2, apply(S1, t))
```

The same substitution operation must act consistently on types, schemes,
constraints, and contexts while avoiding quantified variables. The executable
presentation in
[Typing Haskell in Haskell](../30-sources/jones-1999-typing-haskell-in-haskell.md)
is useful for these invariants, even when designing a non-Haskell language.

## Algorithm W

Write `W(G, e) = (S, t)` for inference of `e` under context `G`, producing a
substitution and monotype.

### Variable

```text
W(G, x):
  return (identity, instantiate(G[x]))
```

Fresh instantiation is required at every occurrence. Reusing the quantified
variables would accidentally make a polymorphic binding monomorphic.

### Lambda

```text
W(G, fn x -> body):
  a = fresh()
  (S1, tbody) = W(G[x : a], body)
  return (S1, apply(S1, a) -> tbody)
```

Lambda parameters are monomorphic. This is what makes the system rank 1.

### Application

```text
W(G, f arg):
  (S1, tf) = W(G, f)
  (S2, ta) = W(apply(S1, G), arg)
  b = fresh()
  S3 = unify(apply(S2, tf), ta -> b)
  return (S3 after S2 after S1, apply(S3, b))
```

The substitution learned from the function must reach the context before
inferring the argument. The final unifier must see the already-substituted
function type.

### Nonrecursive let

```text
W(G, let x = e1 in e2):
  (S1, t1) = W(G, e1)
  G1 = apply(S1, G)
  s = generalize(G1, apply(S1, t1))
  (S2, t2) = W(G1[x : s], e2)
  return (S2 after S1, t2)
```

Generalization is relative to the **substituted** context. Constraints learned
while inferring `e1` may have refined unknowns captured from the surrounding
scope.

## Worked examples

### Let polymorphism

```text
let id = fn x -> x in (id 1, id true)
```

1. The lambda has type `a -> a` for fresh `a`.
2. `a` is not free in the outer context, so `id` receives
   `forall a. a -> a`.
3. The first occurrence instantiates the scheme with fresh `b`; applying it to
   `1` solves `b = Int`.
4. The second occurrence instantiates independently with fresh `c`; applying it
   to `true` solves `c = Bool`.
5. The pair has type `(Int, Bool)`.

The scheme is reusable because uses are fresh. The original unification
variable is not mutated into two types.

### Captured variables are not generalized

```text
fn y -> let keep = fn x -> y in keep
```

Assume `y : a` in the context. The inner function has type `b -> a`.
Generalization may quantify `b`, but it must not quantify `a` because
`a` is free in the context. The local scheme is `forall b. b -> a`.

### The occurs check

For `fn x -> x x`, give `x` fresh type `a`. Application requires `x` to have
type `a -> b`, but it already has type `a`. Solving `a ~ a -> b` fails the
occurs check.

## What principal means

A scheme `sp` is principal for expression `e` under context `G` when:

1. `G` derives `e : sp`; and
2. every other valid scheme for `e` is an instance of `sp`.

For example, `forall a. a -> a` is more general than both `Int -> Int` and
`Bool -> Bool`. Principality makes inference stable: the compiler does not
arbitrarily choose a specialization, and a user annotation can be checked
against the most-general result.

Principality does not imply:

- that the program computes the intended domain result;
- that every useful typed program is expressible;
- that diagnostics identify the intended repair;
- that arbitrary extensions preserve a most-general result;
- that a solver terminates unless termination is part of the theorem.

Soundness, completeness, principality, and termination must be claimed
separately.

## The classic expressiveness boundary

Classic HM makes a deliberate trade:

- quantification is rank 1 and occurs only in context schemes;
- function parameters are monomorphic;
- `let` introduces polymorphism;
- recursive names are monomorphic while their binding group is inferred;
- polymorphic recursion requires an annotation;
- there is no subtyping in the core;
- ad-hoc overloading is outside the original system.

These are not accidental omissions. They preserve decidable, principal
inference through first-order equality unification.

## Strict evaluation and generalization

Pure HM can generalize every `let` right-hand side. In a strict language where
evaluation may create shared references or capture control, that rule can be
unsound: separate type instantiations describe one shared runtime object as if
it were independently created.

[Wright 1995](../30-sources/wright-1995-simple-imperative-polymorphism.md)
uses a syntactic value restriction: only value right-hand sides generalize.
This is simple and sound but rejects some effect-free computations.

[Leijen 2014](../30-sources/leijen-2014-koka-row-polymorphic-effects.md)
uses inferred effects to admit more generalization while preserving the safety
condition in its chosen calculus. The important general lesson is not one
specific rule: generalization must be justified by the evaluation semantics
and the effect discipline.

## Qualified types and traits

Qualified types extend a scheme to:

```text
forall a. P => t
```

where `P` contains predicates such as `Eq a`. An HM-shaped algorithm now
synthesizes predicates as well as substitutions and types:

- variable use instantiates both type variables and predicates;
- application substitutes through and combines predicate sets;
- `let` decides which predicates belong in the scheme and which remain in the
  enclosing scope;
- a solver simplifies, retains, rejects, or discharges predicates;
- elaboration supplies evidence such as method dictionaries.

[Jones 1994](../30-sources/jones-1994-theory-of-qualified-types.md) proves
principal qualified typings under properties of predicate entailment. Two new
questions remain beyond ordinary unification:

- **termination** — does instance search and predicate simplification end?
- **coherence** — do different valid evidence derivations preserve meaning?

A scheme may also be ambiguous when a constrained variable is not determined
by the visible type. Storing constraints in a scheme is therefore necessary
but not sufficient for a sound trait design.

## Kinds and higher-kinded variables

Kinds classify types and type constructors:

```text
Type
Type -> Type
(Type -> Type) -> Type
```

Kinds do not imply higher-rank term polymorphism. They do require substitutions
and unification bindings to preserve kind. Inference can remain first-order
when constructor applications are rigid and the type language excludes
unrestricted type-level reduction.

This is a useful separation: a language can accept a parameter
`f : Type -> Type` while still restricting term schemes to rank 1.

## Rows are additional solving domains

Rows can describe structural records, variants, or effects, but the word “row”
does not determine one universal equality theory.

Unique-label records and variants naturally generate lacks predicates when a
field or alternative is extended. The system in
[Gaster and Jones 1996](../30-sources/gaster-jones-1996-extensible-records-variants.md)
uses qualified row types for this purpose.

An effect-aware function can instead use:

```text
A ->{<IO, State | e>} B
```

Koka permits duplicate effect labels so handler removal retains a
most-general solution without separate lacks constraints. Set-like effect rows
usually need another mechanism, such as lacks constraints or presence flags.
The row theory says which requests may escape; handler selection, resumption
depth and multiplicity, effect-instance identity, and scoped computations are
separate obligations developed in
[Algebraic Effects and Handlers](algebraic-effects-and-handlers.md).

For any row domain to participate in principal inference, it needs:

- a declarative equality and predicate theory;
- a terminating, most-general solver;
- kind-preserving substitution everywhere rows occur;
- generalization and fresh instantiation of row variables;
- an ambiguity policy for residual row predicates.

Sharing an implementation data structure does not prove these properties for
two different row theories.

## Beyond rank 1

Higher-rank types place `forall` inside function arguments or results. General
implicit inference is no longer Algorithm W's problem. A language can retain a
small inference core while checking richer types bidirectionally at annotated
boundaries.

[Dunfield and Krishnaswami 2013](../30-sources/dunfield-krishnaswami-2013-bidirectional-typechecking.md)
give a sound and complete algorithm for a predicative higher-rank calculus.
This supports a layered contract: synthesize ordinary rank-1 code and check
explicit higher-rank declarations.

Local equality assumptions, such as those introduced by GADT patterns, pose a
different challenge. [OutsideIn(X)](../30-sources/vytiniotis-et-al-2011-outsidein.md)
shows that natural typing rules may admit programs without principal types and
that constraint scope must be represented explicitly. A sound advanced checker
may intentionally accept fewer programs than the declarative relation in order
to return predictable principal results.

## Design implications

The evidence supports a disciplined language architecture:

1. Name the fragment receiving complete principal inference.
2. Give every additional solver its own declarative theory and termination
   conditions.
3. Generalize only at documented boundaries using the substituted context and
   a semantics-justified effect rule.
4. Preserve constraint scope rather than pooling every obligation globally.
5. Require annotations for polymorphic recursion, higher-rank types, and local
   equality assumptions.
6. Elaborate implicit polymorphism, predicates, and effects into an explicit
   typed core.
7. Test solver order independence and inferred generality, not only acceptance.

The concrete application of those principles is
[A Greenfield Type System for Catena](catena-greenfield-type-system.md).

## Falsification checklist

A claim of principal HM-like inference must be narrowed if its promised
fragment permits any of the following:

- two valid typings with no common principal scheme;
- a scheme quantifying a variable fixed by the substituted context;
- inference rejecting a declaratively typable unannotated term;
- unification or attached constraint solving diverging;
- solver output depending on traversal order;
- ambiguous evidence with observably different elaborations;
- an effectful generalized binding that breaks type safety.

Finding one does not necessarily invalidate the feature. It means the contract
must change to annotation-directed checking, sound but incomplete inference,
or a smaller principal fragment.

## Source trail

- [Hindley 1969](../30-sources/hindley-1969-principal-type-scheme.md) —
  principal schemes in combinatory logic.
- [Milner 1978](../30-sources/milner-1978-type-polymorphism.md) — Algorithm W
  and the programming-language discipline.
- [Damas and Milner 1982](../30-sources/damas-and-milner-1982-principal-type-schemes.md)
  — completeness and principality for the `let` core.
- [Jones 1994](../30-sources/jones-1994-theory-of-qualified-types.md) —
  predicates, evidence, ambiguity, and coherence.
- [Jones 1999](../30-sources/jones-1999-typing-haskell-in-haskell.md) — an
  executable specification of substitutions, kinds, classes, and groups.
- [Wright 1995](../30-sources/wright-1995-simple-imperative-polymorphism.md) —
  strict effects and the value restriction.
- [Gaster and Jones 1996](../30-sources/gaster-jones-1996-extensible-records-variants.md)
  — unique-label record and variant rows.
- [Jones 2000](../30-sources/jones-2000-functional-dependencies.md) —
  dependencies and ambiguity in multi-parameter classes.
- [Leijen 2014](../30-sources/leijen-2014-koka-row-polymorphic-effects.md) —
  effect-row inference and effect-directed generalization.
- [Dunfield and Krishnaswami 2013](../30-sources/dunfield-krishnaswami-2013-bidirectional-typechecking.md)
  — predicative higher-rank bidirectional checking.
- [OutsideIn(X)](../30-sources/vytiniotis-et-al-2011-outsidein.md) — scoped
  constraints and principality under local assumptions.

## Connections

- [Hindley–Milner Type Inference](../10-maps/hindley-milner-type-inference.md)
  is the focused route through the foundation.
- [Catena Type-System Design](../10-maps/catena-type-system-design.md) connects
  the theory to the independent language proposal.
- [Algebraic Effects and Handlers](../10-maps/algebraic-effects-and-handlers.md)
  follows the effect-row extension into its independent operational and
  resource-safety obligations.
- [What Should a Greenfield Catena Type System Guarantee?](../40-inquiries/what-should-a-greenfield-catena-type-system-guarantee.md)
  tracks the remaining proof and design questions.
