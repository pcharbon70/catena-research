---
title: "Data and Pattern Metatheory"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.2"
tags:
  - algebraic-data-types
  - pattern-matching
  - program-semantics
  - specification
aliases:
  - "C002 metatheory targets"
---

# Data and Pattern Metatheory

## Judgment boundary

The 0.1.2 model adds these judgment families to C001:

> **Normative definition.**

```text
Δ ⊢ group ok ⇒ Δ'
Δ ; Γ ⊢ constructor(args) : T ⇒ e
Δ ; T ⊢ pattern ⇒ Γp ; Q ; p
Δ ; Γ ⊢ match : T ! ε ⇒ e
Δ ; Q ⊢ matrix useful(pattern) ⇒ result
Σ ⊢ core ok
Σ ; layout ⊢ core ⇒ ErlangForms
```

`Δ` contains kinds, nominal identities, constructors, and visibility. `Γp`
contains pattern bindings. `Q` contains branch-local equalities. `Σ` contains
verified semantic constructor and layout metadata.

## Required claims

The normative design targets these claims:

1. **Nominal generativity.** Distinct origin/module/type triples do not unify
   without an explicit future identity-preserving operation.
2. **Declaration atomicity.** A failed recursive group adds no usable nominal
   or constructor identity.
3. **Ordinary conservativity.** Adding uniform rank-1 constructor schemes does
   not change the inferred principal scheme of a C001 term that uses no data
   syntax.
4. **Pattern substitution.** Values bound by a successful typed pattern have
   the types recorded in its binding environment.
5. **Preservation.** Construction, selected match reduction, and generated
   fold dispatch preserve their declared result type.
6. **Exhaustive progress.** A closed, well-typed match over a value produced by
   typed construction selects a clause or continues through a false guard; it
   does not become stuck on missing structure.
7. **Usefulness soundness.** A reported redundant clause cannot be selected
   after prior proved-true clauses, and an accepted exhaustive matrix covers
   every value in the modeled domain.
8. **GADT scope.** Equality evidence refines only one branch, existential
   skolems do not escape, and local assumptions are not generalized.
9. **Decision equivalence.** The ordered decision representation selects the
   same clause and bindings as the source semantics while evaluating the
   scrutinee once.
10. **Fold validity.** A generated fold dispatches exactly one declared
    handler and passes exactly that constructor's fields in declaration order.
11. **Representation independence.** Uniform and compact lowering are
    contextually equivalent for typed Catena observations.

## Proof status (non-normative)

These claims are written metatheory targets, not machine-checked theorems. The
current evidence consists of:

- executable declaration and type elaboration;
- an inference-independent typed-core verifier;
- a usefulness checker shared by exhaustiveness and redundancy;
- a pure semantic evaluator;
- bounded finite coverage enumeration;
- negative corruption tests; and
- differential compile, load, and execution under two layouts.

Those observations can falsify implementations and examples but cannot prove
the claims for all programs. In particular, the current reference evaluator
does not cover effects, processes, foreign values, structural variants, or
all future primitive domains.

## Falsification criteria

C002 must be revised or its implementation rejected if any typed test can:

- confuse two nominal origins;
- observe a partially published recursive group;
- bind one variable at two incompatible types in an accepted pattern;
- reach the backend's invalid-value fallback using only typed construction;
- accept a missing or redundant finite constructor case;
- leak a GADT equality or existential type;
- cause reference, uniform, and compact execution to select different source
  results; or
- observe runtime layout through a public `.cati.json` interface.

## Evidence route (non-normative)

The formal basis and limitations are developed through
[Standard ML](../../30-sources/milner-et-al-1997-definition-standard-ml.md),
[Maranget's usefulness analysis](../../30-sources/maranget-2007-warnings-pattern-matching.md),
[GADT inference](../../30-sources/peyton-jones-et-al-2006-gadt-inference.md),
and [typed representation changes](../../30-sources/leroy-1992-unboxed-objects.md).
The wider unresolved proof obligations remain in checklist item P132.
