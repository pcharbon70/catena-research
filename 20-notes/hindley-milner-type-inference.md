---
title: "How Hindley–Milner Type Inference Works"
kind: note
created: "2026-07-31"
maturity: developing
tags:
  - algorithm-w
  - catena
  - effect-rows
  - hindley-milner
  - principal-types
  - trait-constraints
aliases:
  - "Hindley–Milner type inference"
  - "HM inference"
---

# How Hindley–Milner Type Inference Works

## Executive conclusion

Hindley–Milner inference is best understood as four cooperating mechanisms:

1. Traverse the syntax and assign fresh unknowns to facts not yet known.
2. Use **unification** to solve equality requirements imposed by application
   and other syntax.
3. At a `let` boundary, **generalize** only the unknowns not fixed by the
   surrounding environment.
4. At each use of a polymorphic binding, **instantiate** its quantified
   unknowns freshly.

The result is stronger than “the compiler found a type.” For the classic
rank-1 core, Algorithm W is sound and complete and computes a **principal type
scheme**: every other valid type of the term is a substitution instance of the
inferred one. Hindley established the principal-scheme idea for combinatory
logic; Milner gave the practical programming-language discipline and Algorithm
W; Damas and Milner proved W's completeness and principality for the
`let`-polymorphic core. See the reading trail beginning with
[Hindley 1969](../30-sources/hindley-1969-principal-type-scheme.md),
[Milner 1978](../30-sources/milner-1978-type-polymorphism.md), and
[Damas–Milner 1982](../30-sources/damas-and-milner-1982-principal-type-schemes.md).

Catena should keep this core as a deliberately small trusted kernel, then state
separate guarantees for traits, kinds, and effect rows. Those features can fit
an HM-shaped algorithm, but their solver properties and generalization rules
are additional proof obligations. The current implementation contains most of
the named mechanisms; it does not yet expose one obvious, unified invariant
from which principal type-and-effect inference follows.

## Question and scope

This note asks:

> How does Hindley–Milner inference work mechanically and theoretically, and
> where does Catena's trait-, higher-kinded-, and effect-aware system extend or
> constrain the classic model?

“Works” has four operational meanings here:

- **soundness** — inferred typings are valid in the declarative type system;
- **completeness** — if the designated core can type a term, inference succeeds;
- **principality** — a successful result is at least as general as every other
  valid typing;
- **termination** — type inference and every attached solver decide their
  obligations for the accepted language fragment.

The deep dive covers rank-1 `let` polymorphism, substitutions, unification,
Algorithm W, recursive bindings, qualified constraints, kinds, and effect rows.
It does not attempt a proof for the full Catena language or prescribe a
higher-rank type system.

## The formal objects

A minimal HM presentation distinguishes **monotypes** from **type schemes**:

```text
monotype  τ ::= α | C | τ -> τ | C τ ... τ
scheme    σ ::= ∀ α1 ... αn. τ
context   Γ ::= name ↦ σ
```

- A type variable such as `α` is a unification unknown.
- A constructor such as `Integer`, `Boolean`, or `List` is rigid.
- A monotype may contain unknowns but no nested `forall`.
- A scheme quantifies zero or more variables at the outside only.
- The environment maps program variables to schemes, not directly to
  monotypes.

The distinction between a free unknown and a quantified variable is semantic.
In `α -> α`, the same unresolved `α` must be chosen consistently. In
`∀α. α -> α`, each use may choose a new instance.

For any type-like object `X`, `ftv(X)` is its set of free type variables. The
two central operations are:

```text
generalize(Γ, τ) = ∀(ftv(τ) − ftv(Γ)). τ
instantiate(∀α1...αn. τ) = [fresh β1/α1, ..., fresh βn/αn]τ
```

The subtraction in `generalize` prevents inference from quantifying an unknown
that belongs to an enclosing scope. This rule is one of the system's primary
soundness and principality boundaries.

## Declarative typing before algorithms

It helps to separate the language's typing rules from the procedure that finds
a derivation. A compact declarative core is:

| Form | Essential condition |
| --- | --- |
| Variable `x` | Instantiate the scheme `Γ(x)` |
| Lambda `fn x -> e` | Give `x` a fresh **monomorphic** type and type `e` |
| Application `f x` | `f` must have a type compatible with `type(x) -> β` |
| Let `let x = e1 in e2` | Type `e1`, generalize relative to `Γ`, then type `e2` with the resulting scheme |

The declarative system may be written with explicit generalization and
instantiation rules that can appear at several points in a derivation.
Algorithm W makes the same discipline syntax-directed: instantiation happens
at variables and generalization happens at `let`.

This separation matters. An implementation is **sound** if its answers are
derivable; it is **complete** if it can find an answer whenever a declarative
derivation exists. Without a declarative system, tests can show consistency
between implementations but cannot define principality on their own.

## Unification is the constraint solver

Application does not guess a concrete type. It generates an equality problem.
If `f : τf`, `x : τx`, and the result has a fresh type `β`, then:

```text
τf ~ τx -> β
```

A unifier is a substitution making both sides equal. A **most general unifier**
(MGU) commits only to structure forced by the equation, so every other unifier
can be expressed as an additional substitution after it. The MGU property is
what lets W retain principal types.

A first-order unifier repeatedly applies a small set of ideas:

- identical types need no substitution;
- matching constructors decompose into equations between their arguments;
- distinct rigid constructors fail;
- an unknown `α` may be bound to `τ` if `α` does not occur inside `τ`;
- substitutions discovered earlier must be applied before solving later
  equations.

The **occurs check** rejects an infinite equation such as:

```text
α ~ α -> β
```

Without recursive types, no finite type can satisfy it. The term
`fn x -> x x` creates exactly this equation: `x` must be both the function and
its own argument.

Substitution composition order is observable. If `S1` was learned first and
`S2` later under `S1`, the combined substitution must satisfy:

```text
apply(S2 ∘ S1, τ) = apply(S2, apply(S1, τ))
```

Reversing this order can leave stale variables in results or environments.
[Typing Haskell in Haskell](../30-sources/jones-1999-typing-haskell-in-haskell.md)
is an executable primary reference for these implementation invariants,
including occurs and kind checks.

## Algorithm W, case by case

Write `W(Γ, e) = (S, τ)` for inference of expression `e` under environment
`Γ`, producing substitution `S` and monotype `τ`.

### Variable

```text
W(Γ, x):
  σ = lookup Γ x
  return (identity, instantiate σ)
```

Instantiation must create fresh variables every time. Reusing quantified
variables would accidentally make separate uses monomorphic.

### Lambda

```text
W(Γ, fn x -> e):
  α = fresh()
  (S1, τbody) = W(Γ[x ↦ α], e)
  return (S1, apply(S1, α) -> τbody)
```

The parameter gets a monotype, not a scheme. Classic HM therefore rejects:

```text
fn f -> (f 1, f true)
```

Both uses share the same parameter type. Supporting a polymorphic `f` here
requires higher-rank polymorphism and usually annotations or bidirectional
checking; it is not ordinary HM.

### Application

```text
W(Γ, f x):
  (S1, τf) = W(Γ, f)
  (S2, τx) = W(apply(S1, Γ), x)
  β = fresh()
  S3 = mgu(apply(S2, τf), τx -> β)
  return (S3 ∘ S2 ∘ S1, apply(S3, β))
```

The environment passed to the argument has already absorbed `S1`. The
function type is also updated by `S2` before unification. These details keep
the returned substitution and type mutually consistent.

### Let

```text
W(Γ, let x = e1 in e2):
  (S1, τ1) = W(Γ, e1)
  Γ1 = apply(S1, Γ)
  σ = generalize(Γ1, apply(S1, τ1))
  (S2, τ2) = W(Γ1[x ↦ σ], e2)
  return (S2 ∘ S1, τ2)
```

The substituted environment `Γ1` is essential. Damas–Milner's closure is
formed relative to the assumptions after the constraints from `e1` have been
applied.

## Worked examples

### Let polymorphism

Consider:

```text
let id = fn x -> x in (id 1, id true)
```

1. Give `x` a fresh type `α`; the body returns `x`, so the lambda has
   `α -> α`.
2. The outer environment does not contain `α`, so generalize `id` to
   `∀α. α -> α`.
3. The first use instantiates the scheme as `β -> β`; unification with the
   integer argument makes `β = Integer`.
4. The second use instantiates it independently as `γ -> γ`; unification with
   `true` makes `γ = Boolean`.
5. The pair has type `(Integer, Boolean)`.

The polymorphism belongs to the `let`-bound name, not to the original
unification variable. Fresh instantiation is what prevents the integer use from
constraining the Boolean use.

### Why environment variables are not generalized

Consider the body of a lambda:

```text
fn y -> let keep = fn x -> y in keep
```

Suppose `y : α` in the environment. The inner function has type `β -> α`.
Generalization may quantify `β`, but not `α`, because `α ∈ ftv(Γ)`. The scheme
is therefore `∀β. β -> α`. Quantifying `α` would incorrectly sever the result
type of `keep` from the actual captured value `y`.

### Why the occurs check matters

For `fn x -> x x`, let `x : α`. Application requires the left occurrence to
have type `α -> β`, but it already has type `α`. Unification asks for
`α ~ α -> β`; the occurs check rejects the recursive occurrence of `α`.

## What “principal” guarantees—and what it does not

A scheme `σp` is principal for `e` under `Γ` when:

1. `Γ ⊢ e : σp`; and
2. every other valid scheme for `e` under `Γ` is an instance of `σp`.

For example, `∀α. α -> α` is more general than `Integer -> Integer` and
`Boolean -> Boolean`. Principality gives a stable compiler–programmer contract:
inference does not arbitrarily choose one specialization and annotations can be
checked as instances of the inferred result.

Principality does not imply:

- that the program's behavior is correct for its domain;
- that error messages identify the programmer's intended repair;
- that inference is cheap for every program or representation;
- that every useful typed term is expressible in rank-1 HM;
- that arbitrary extensions preserve a most-general result.

Soundness, completeness, and principality are distinct. Milner proves the
soundness direction for W; Damas–Milner proves the corresponding completeness
and principal-type results for the specified core.

## The expressiveness boundary of classic HM

Classic HM makes a valuable trade: complete annotation-free inference for a
restricted form of polymorphism.

- Quantification is rank 1: `forall` appears only around schemes stored in the
  environment, not inside arbitrary argument or result types.
- Lambda parameters are monomorphic.
- `let` introduces polymorphism; ordinary application does not.
- Recursive definitions are normally inferred monomorphically within each
  strongly connected binding group, then generalized outside the group.
- Polymorphic recursion is not inferred in general; it needs a declaration or
  a more expressive checking system.
- There is no subtyping in the classic core.
- Ad-hoc overloading is outside Milner's original parametric system.

These restrictions are not accidental omissions. They preserve decidable,
principal inference with first-order unification.

## Strict evaluation, effects, and generalization

Pure HM can generalize any `let` right-hand side. In a strict language with
shared references or control effects, that rule can be unsound: the type system
may treat separate uses as independently instantiated even though evaluation
created one shared stateful or control-bearing object.

[Wright's value-restriction work](../30-sources/wright-1995-simple-imperative-polymorphism.md)
generalizes only syntactic values. This is simple and sound but rejects some
pure computations that ordinary HM accepts.

[Koka's effect-row system](../30-sources/leijen-2014-koka-row-polymorphic-effects.md)
shows another route: infer effects and restrict generalization based on the
effect of the bound computation. That design can safely generalize more than a
syntactic value rule, but only because its semantics and effect inference make
the restriction meaningful.

For Catena, first-class resumptions make this question concrete. A resumption
can encode control authority even when no mutable reference appears in source.
The language needs a stated rule for which type, effect-row, and resumption
variables may be generalized after an effectful computation.

## Qualified types: the trait extension

Traits change a scheme from:

```text
∀α. τ
```

to a qualified scheme:

```text
∀α. P => τ
```

where `P` contains obligations such as `Comparable α`. The W-shaped algorithm
now synthesizes `(substitution, predicates, type)`:

- variable use freshly instantiates both the type and its predicates;
- application substitutes through and combines predicate sets;
- `let` generalizes variables across both `P` and `τ`;
- a constraint solver simplifies, retains, defers, rejects, or discharges
  predicates;
- elaboration supplies evidence, commonly a selected dictionary of methods.

[Jones's qualified-type theory](../30-sources/jones-1994-theory-of-qualified-types.md)
proves principal qualified typings under properties of the entailment system.
It also exposes two guarantees that plain unification does not provide:

- **termination** — instance search and superclass expansion must end;
- **coherence** — different valid evidence derivations must not change program
  meaning.

An inferred scheme can be principal yet ambiguous if a constrained variable
appears only in predicates and is not determined by the visible type. Catena's
trait design therefore needs ambiguity and evidence-coherence rules in addition
to constraint storage.

## Kinds and higher-kinded constructors

Kinds classify types and type constructors. A basic system might use:

```text
Type                -- inhabited value types
Type -> Type        -- unary type constructors such as List
(Type -> Type) -> Type
```

Kinds do not require higher-rank *term* polymorphism. They do require every
type substitution and unification binding to preserve kind. Inference can
remain first order when type constructors are rigid applications and the type
language avoids general computation or unrestricted type-level lambdas.

This is a good boundary for Catena: validate higher-kinded applications before
or alongside term inference, attach a kind to every flexible constructor
variable, and reject kind mismatch separately from value-type mismatch. The
executable Jones specification shows why allowing arbitrary reduction or
rewriting in the type language can destroy decidable, unitary unification.

## Effect rows: an additional unification domain

An effect-aware function type can be written:

```text
τ1 ->{ε} τ2
ε ::= <> | <IO, State | μ>
```

Here `μ` is an effect-row variable. A higher-order function such as `map` needs
effect polymorphism because its effect depends on the function passed to it.
The HM skeleton can survive if effect rows have:

- a precise equality theory;
- a terminating, most-general row unifier;
- substitution over row variables everywhere they occur;
- generalization and fresh instantiation of row variables;
- a defined rule for adding, combining, and removing effects;
- a sound relationship to runtime evaluation and handlers.

Row design affects principality. Koka permits duplicate labels so certain
effect-removal equations have a unique most-general solution. Set-like rows
usually require alternatives such as lacks constraints or presence/absence
flags. Catena should choose and document one semantic model; normalization by
deduplication, multiset rows, and lacks constraints are not interchangeable.

## Reading Catena's current implementation

The following is a static reading of Catena at commit
`0f61d16f4f51500e2c27790c0d8c94eaf4784797`. The exact evidence and commands
are in the [implementation-audit journal](../50-journal/2026-07-31-catena-hm-implementation-audit.md),
and the canonical project source is recorded separately in
[Catena Type and Effect System](../30-sources/catena-2026-type-and-effect-system.md).

### What already matches the HM model

- `catena_infer_expr` instantiates schemes at variables, gives lambda
  parameters fresh monotypes, unifies applications, and generalizes
  nonrecursive `let` bindings.
- `catena_infer_unify` applies the current substitution before solving,
  composes new substitutions, performs occurs checks, and decomposes the
  supported type constructors.
- `catena_type_scheme` represents monomorphic and polymorphic schemes, with
  optional trait constraints, and quantifies variables in both type and
  constraint sets relative to free environment variables.
- `catena_infer` substitutes and simplifies accumulated trait constraints and
  resolves them against an instance database.
- Kinds, record rows, effect-row types, and `Resumption k a b e` have explicit
  representation and unification support.

### Boundaries that need an explicit contract or regression test

These observations identify proof and test targets; static inspection alone
does not establish that each one is a user-visible bug.

1. **Substituted environment at `let`.** The expression case substitutes the
   inferred type before generalization, but passes the original environment to
   `generalize`, which computes `ftv(Env)` without first applying the current
   substitution. Standard W forms the closure relative to `SΓ`. A minimal
   captured-variable regression should demonstrate that Catena neither
   over-generalizes nor under-generalizes here.
2. **Constraint ownership.** `generalize` reads all constraints accumulated in
   the inference state. Qualified-type implementations normally distinguish
   predicates belonging to the binding from predicates fixed by or deferred to
   the enclosing scope. Catena needs a local-delta or retained/deferred rule so
   unrelated obligations do not leak into schemes.
3. **Two instantiation paths.** `catena_infer_expr` contains a local
   implementation alongside `catena_type_scheme:instantiate/2`, with a TODO
   acknowledging their behavioral difference. A single canonical invariant
   would reduce semantic drift.
4. **Top-level generalization.** `catena_infer:check_program` stores each
   inferred binding as a monomorphic scheme. Expression-level `let` is
   polymorphic, so module and top-level policy should say whether this
   asymmetry is intentional.
5. **Recursion policy.** `letrec` is inferred through a monomorphic placeholder
   and remains monomorphic in its body. This avoids implicit polymorphic
   recursion, but recursive binding groups and post-group generalization need a
   stated module-level policy.
6. **Effect representation.** Core function types validate concrete
   `{effect_set, ...}` values and core function unification compares those sets
   for equality. Separate modules represent effect variables and row-polymorphic
   schemes, while `teffectrow` has a distinct row unifier. The intended bridge
   among these forms should be canonical and end-to-end.
7. **Effect variables in schemes.** `catena_types:type_vars/1` traverses value
   types and standalone effect-row tails but ignores the effect component of a
   function type. The core scheme generalizer therefore cannot by itself
   quantify a function's separate effect-variable representation.
8. **Lambda effects.** The core lambda case constructs a function with an empty
   effect set (“pure for now”), while the body may update effect state. The
   broader compiler may recover this information elsewhere, but a direct
   higher-order test should show that body effects become latent function
   effects rather than effects of merely constructing the closure.
9. **Constraint solver guarantees.** Built-in resolution exists, along with
   hierarchy and coherence modules. The language contract still needs explicit
   termination, ambiguity, overlap, and evidence-selection rules matching the
   assumptions under which principal qualified types are claimed.

## A proposed architecture for Catena

The conservative design is a layered inference contract:

```text
surface syntax
  -> kind validation
  -> HM equality inference over value types
  -> qualified constraint simplification and evidence selection
  -> effect-row unification and handler constraints
  -> generalized scheme + typed/elaborated core
```

The phases may be interleaved in the implementation, but their invariants
should remain separately stateable.

### 1. Name the guaranteed fragment

Define a small Catena core for which the project intends sound, complete, and
principal inference. State explicitly whether it contains records, variants,
recursive groups, traits, higher-kinded variables, effects, and resumptions.
Features outside the fragment can remain sound but annotation-requiring.

### 2. Use one scheme model

A canonical scheme should quantify variables with their sort or kind and carry
the obligations that survive generalization:

```text
Scheme {
  quantified: [TypeVar | ConstructorVar | RowVar | EffectVar],
  predicates: [TraitPredicate | RowPredicate],
  body: Type
}
```

This does not require one numeric namespace internally, but it does require
capture-free, kind-preserving substitution and fresh instantiation for every
quantified domain.

### 3. Make generalization a boundary operation

Generalization should receive the substituted environment, the binding-local
type and effect, and the binding-local constraints. It should return both the
scheme and predicates deferred outward. The policy should state whether an
effectful or resumption-producing right-hand side may be generalized.

### 4. Separate equality solving from evidence solving

First-order type and row equations should yield most-general substitutions.
Trait entailment should then simplify predicates and select evidence under
declared termination and coherence rules. Allowing instance selection to make
hidden type choices risks losing principality unless improvement rules make
those choices explicit.

### 5. Infer recursive strongly connected components

Bind every name in a recursive component to a fresh monotype, infer the group,
unify the placeholders, then generalize only when leaving the component.
Polymorphic recursion should require a signature and be checked, not guessed.

### 6. Preserve constraint origins

Every equality, trait predicate, kind requirement, and row operation should
carry a source origin and a short reason. Solving can remain mathematically
order-independent while diagnostics use those origins to explain the smallest
useful conflict.

## Verification strategy

A proof-oriented test plan can start before a mechanized proof exists.

### Small executable reference

Build a deliberately slow reference inferencer for the designated Catena core,
modeled after the clarity goal of *Typing Haskell in Haskell*. Differentially
test the production Erlang implementation against it on generated well-scoped
terms.

### Algebraic properties

Test at least:

- substitution identity and composition;
- capture-free scheme substitution;
- fresh instantiations share no quantified variables;
- a unifier makes both inputs equal;
- occurs checks reject cyclic type and row substitutions;
- generalization never quantifies a variable free in `SΓ`;
- inferred annotated types are instances of the principal scheme;
- alpha-renaming term binders does not change the inferred scheme;
- trait resolution is deterministic or produces equivalent evidence;
- handler removal and effect-row normalization obey the chosen row theory.

### Exhaustive small terms

Enumerate small closed terms for the pure core. Compare W's success with a
bounded declarative derivation search and verify that enumerated alternative
types are instances of W's result. This will not replace a proof, but it is
particularly effective at finding substitution-order and generalization-scope
mistakes.

### Semantic checks

For the executable core, evaluate well-typed generated programs and assert the
chosen progress/preservation or “does not go wrong” property. Add targeted
counterexamples for shared state, handlers, one-shot resumptions, and trait
evidence ambiguity.

## Falsification criteria

The claim that Catena preserves HM-like principal inference should be narrowed
or rejected if any of the following holds in the claimed fragment:

- two valid typings exist with no common principal scheme under the defined
  instance relation;
- row unification produces incomparable solutions or depends on traversal
  order;
- inference rejects a declaratively typable unannotated term;
- a scheme quantifies a variable fixed by the substituted environment;
- different valid trait evidence changes observable behavior;
- a well-typed closed program reaches a type- or effect-stuck state;
- inference or instance resolution can diverge on a finite well-formed program.

Finding one of these does not necessarily invalidate the language design. It
means the guarantee must change—for example, to sound but incomplete
inference, annotation-directed checking, or principality only for a smaller
core.

## Research priorities

1. Specify Catena's declarative type-and-effect judgment and the exact fragment
   for which principality is intended.
2. Write captured-environment, constraint-scope, top-level-polymorphism, and
   latent-effect regression tests for the current implementation seams.
3. Choose one canonical effect-row equality and unification model, including
   duplicate-label or lacks semantics.
4. Define the effect/resumption generalization rule for strict evaluation.
5. State and test trait solver termination, ambiguity, overlap, coherence, and
   evidence elaboration.
6. Build the small executable reference and generated differential suite.

The active workbench is
[How should Catena preserve principal inference while extending HM?](../40-inquiries/how-should-catena-preserve-principal-inference.md).

## Source trail

- [Hindley 1969](../30-sources/hindley-1969-principal-type-scheme.md) — the
  principal-scheme property in combinatory logic.
- [Milner 1978](../30-sources/milner-1978-type-polymorphism.md) — the practical
  polymorphic language, semantic soundness, and Algorithm W.
- [Damas and Milner 1982](../30-sources/damas-and-milner-1982-principal-type-schemes.md)
  — completeness and the principal-type theorem for the `let` core.
- [Jones 1994](../30-sources/jones-1994-theory-of-qualified-types.md) —
  principal qualified types, evidence, ambiguity, and coherence.
- [Jones 1999](../30-sources/jones-1999-typing-haskell-in-haskell.md) — an
  executable specification spanning kinds, classes, schemes, and binding
  groups.
- [Wright 1995](../30-sources/wright-1995-simple-imperative-polymorphism.md) —
  why effects constrain generalization.
- [Leijen 2014](../30-sources/leijen-2014-koka-row-polymorphic-effects.md) — an
  HM-shaped effect-row system with explicit principality choices.
- [Current Catena source](../30-sources/catena-2026-type-and-effect-system.md) —
  the project-specific type-and-effect implementation examined here.

## Connections

- [Hindley–Milner type inference map](../10-maps/hindley-milner-type-inference.md)
  provides the shortest reading routes through the foundations, mechanics,
  extensions, and Catena work.
- [Catena HM implementation audit](../50-journal/2026-07-31-catena-hm-implementation-audit.md)
  preserves the exact local revision and static evidence behind the
  implementation observations.
