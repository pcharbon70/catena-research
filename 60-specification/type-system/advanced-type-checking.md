---
title: "Advanced Type Checking"
kind: specification
created: "2026-08-01"
status: normative
spec_version: "0.1.1"
tags:
  - algebraic-data-types
  - catena
  - specification
  - type-inference
aliases:
  - "Catena 0.1.1 annotation-directed profile"
---

# Advanced Type Checking

## Entry boundary

The annotation-directed advanced profile is entered only through an enclosing
signature. Nested polymorphism is explicit and predicative: a polymorphic
value may be checked against `forall`, but a metavariable is never solved with
a polymorphic type. Higher-rank types are not inferred.

Checking is bidirectional. Introductions check against expected types;
eliminations synthesize where possible. An explicit annotation may switch from
checking to synthesis. Instantiation introduces monotypes, and checking a
universal type introduces rigid skolems whose scope is the checked term.

The controlling rules are:

> **Normative definition.**

```text
(FORALL-I) Γ, a rigid ⊢ expression ⇐ body
           --------------------------------
           Γ ⊢ expression ⇐ forall a. body

(FORALL-E) Γ ⊢ expression ⇒ forall a. body     m is a fresh monotype
           ---------------------------------------------------------
           Γ ⊢ expression ⇒ [m/a]body

(ANNOT)    Γ ⊢ expression ⇐ signature
           ---------------------------------
           Γ ⊢ (expression : signature) ⇒ signature
```

`FORALL-E` is predicative because `m` cannot itself contain `forall`.

## GADT patterns

A generalized constructor may return a refined instance of its datatype. A
function that matches such a constructor MUST have an enclosing signature.
Selecting a constructor introduces its equality assumptions only inside that
branch. The branch body is checked under those local equalities, and the
equalities MUST NOT refine sibling branches or the surrounding environment.

Existential constructor variables MUST be written explicitly in the data
declaration. Pattern matching introduces them as rigid skolems. They may be
used abstractly in the branch but MUST NOT escape through the branch result,
an exported value, a stored closure whose type outlives the branch, or a
generalized binding.

Bindings whose inferred types mention local GADT equalities or branch skolems
MUST NOT be generalized. A local signature may be used to establish a smaller
safe scope, but it cannot make a rigid variable escape.

## Affine resumptions

Handler resumptions have an affine type in the static core: a branch may
abandon or consume a resumption once, never duplicate it. Resumption values are
branch scoped and are not first class in containers or exported interfaces.
The runtime representation MUST also carry a consumed token and reject a
second resume, preserving the invariant if unchecked foreign code or a
compiler defect bypasses static checking.

## Explicit exclusions

Catena 0.1.1 excludes impredicative instantiation, inferred higher rank,
first-class existential packages beyond declared constructors, general linear
types, dependent types, unrestricted type families, higher-kinded
polymorphism over arbitrary kinds, and unrestricted GADT inference. Rejection
of one of these forms MUST identify the profile boundary rather than report an
unrelated unification failure.

The higher-rank algorithm is grounded by
[Complete and Easy Bidirectional Typechecking for Higher-Rank Polymorphism](../../30-sources/dunfield-krishnaswami-2013-bidirectional-typechecking.md),
while the GADT boundary follows the constraints described in
[Simple Unification-Based Type Inference for GADTs](../../30-sources/peyton-jones-et-al-2006-gadt-inference.md).
