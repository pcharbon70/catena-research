---
title: "Principal Inference and Generalization"
kind: specification
created: "2026-08-01"
status: normative
spec_version: "0.1.1"
tags:
  - catena
  - principal-types
  - specification
  - type-inference
aliases:
  - "Catena 0.1.1 Algorithm W contract"
---

# Principal Inference and Generalization

## Declarative judgment

The principal core uses the judgment `C ; Γ ⊢ e : t ! efx`, where `C` is a
set of row and trait constraints, `Γ` maps names to schemes, `t` is the value
type, and `efx` is the effect row. Variables instantiate schemes with fresh
metavariables. Application unifies the callee with
`argument_type ->{latent_effect} result_type`. Evaluation effects compose by
duplicate-row union in source evaluation order.

The core rules, with fresh variables chosen away from `Γ`, are:

> **Normative definition.**

```text
(VAR)  x : forall a. C => t in Γ      S = [fresh/a]
       ------------------------------------------------
       S(C) ; Γ ⊢ x : S(t) ! {}

(ABS)  C ; Γ, x:a ⊢ body : b ! e
       ---------------------------------
       C ; Γ ⊢ fn x -> body : a ->{e} b ! {}

(APP)  C1 ; Γ ⊢ f : tf ! e1     C2 ; Γ ⊢ x : tx ! e2
       mgu(tf, tx ->{e3} r) = S
       -------------------------------------------------
       S(C1 ∪ C2) ; S(Γ) ⊢ f(x) : S(r) ! S(e1 ⊎ e2 ⊎ e3)

(LET)  C1 ; Γ ⊢ value : t1 ! e1     scheme = close(Γ, C1, t1, e1)
       C2 ; Γ, x:scheme ⊢ body : t2 ! e2
       ---------------------------------------------------------
       C2 ; Γ ⊢ let x = value; body : t2 ! (e1 ⊎ e2)
```

`⊎` is duplicate effect-row union. `close` applies the generalization rule
below; it does not quantify variables when its side condition fails.

Literals, variables, lambdas, application, tuples, and non-recursive `let`
MUST follow Algorithm W with kinded, occurs-checked unification. The result
substitution is applied to the environment before later premises. A successful
principal-core inference MUST return a scheme at least as general as every
other declaratively valid scheme for the same environment.

## Generalization

Catena uses an effect-aware hybrid rule. A non-recursive binding may generalize
metavariables not free in the environment when either:

- its right-hand side is non-expansive; or
- its inferred evaluation effect row is provably empty and it allocates no
  affine capability or resumption token.

Lambdas, constructors fully applied to non-expansive arguments, literals, and
immutable tuples or records of non-expansive terms are non-expansive.
Application, request performance, handler installation, process operations,
and unknown calls are expansive. If purity cannot be proved, the binding stays
monomorphic. Latent effects inside a lambda do not by themselves prevent
generalizing the lambda value.

Constraints mentioning a generalized variable are retained in its qualified
scheme. Constraints mentioning only monomorphic variables remain at the
binding site. Generalization MUST reject ambiguity as defined in
[Type Language and Kinds](type-language-and-kinds.md).

## Recursive bindings and signatures

A mutually recursive unannotated group is inferred monomorphically within the
group and generalized only after all definitions unify. This provides
monomorphic recursion. Polymorphic recursion requires explicit signatures for
the affected bindings and is checked, not inferred.

An annotated binding is checked by skolemizing explicit universal binders,
checking the body, discharging or retaining permitted constraints, and then
testing subsumption. A skolem MUST NOT escape its signature scope.

## Determinism and failure

Fresh variable names and constraint presentation MAY differ, but alpha-equivalent
input and irrelevant solver work-list order MUST yield alpha-equivalent
schemes and equivalent typed core. The implementation MUST reject infinite
types, kind mismatches, unresolved ambiguity, and unsatisfied constraints with
the diagnostic families in
[Diagnostics and Conformance](diagnostics-and-conformance.md).

The classic foundation is documented in
[Principal Type-Schemes for Functional Programs](../../30-sources/damas-and-milner-1982-principal-type-schemes.md);
Catena's effect-aware restriction is an explicitly narrower synthesis.
