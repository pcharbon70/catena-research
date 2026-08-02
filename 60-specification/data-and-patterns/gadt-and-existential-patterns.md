---
title: "GADT and Existential Patterns"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.2"
tags:
  - algebraic-data-types
  - pattern-matching
  - specification
  - type-inference
aliases:
  - "Catena GADT pattern boundary"
---

# GADT and Existential Patterns

## Explicit advanced declarations

A constructor result refinement uses `returns`:

```catena
type Expr A =
  | IntLit(Int) returns Expr Int
  | BoolLit(Bool) returns Expr Bool
```

An existential payload uses an explicit binder:

```catena
type Packed =
  | Pack exists A { value: A, show: A -> String }
```

The refined result MUST be the declared nominal type at full arity. An
existential variable MAY appear in constructor fields but MUST NOT appear in
the datatype result.

## Required annotation boundary

A definition that pattern-matches a refined or existential constructor MUST
have an enclosing signature. Absence is invalid with `T010`. Catena makes no
principal-type or completeness claim for this annotation-directed region.
Programs using only ordinary uniform-result constructors remain in the C001
principal profile.

For example:

```catena
evaluate : forall A. Expr A -> A
evaluate expression =
  match expression with
  | Expr.IntLit value -> value
  | Expr.BoolLit value -> value
```

## Branch-local checking

Checking a GADT constructor pattern MUST:

1. instantiate declaration parameters freshly;
2. instantiate explicit existentials as rigid skolems;
3. compare the constructor result with the scrutinee type;
4. introduce compatible index equalities only for that branch;
5. refine pattern bindings, the declared branch result, and local assumptions;
   and
6. discard the equalities after checking the branch.

The branch environment MUST NOT be generalized while local equality evidence
is active. An impossible constructor is excluded from coverage rather than
reported as a missing alternative.

## Escape prevention

A branch result, generalized scheme, closure environment, or module interface
MUST NOT contain a rigid constructor existential or branch-local equality
variable. Such escape is invalid with `T009`.

An existential payload may be consumed through operations carried with it or
converted to a result independent of its hidden type. It may not be returned
as though the hidden type were selected by the caller.

## Typed-core evidence

The typed core records resolved constructor identity, instantiated payload
types, local refinements, and rigid variables. The verifier MUST independently
check field arity, nominal result identity, branch binding types, equality
scope, and non-escape.

The coverage checker MAY use local equalities to reject impossible
constructors, but MUST NOT let a coverage approximation justify an unsound
branch type.

## Limits and rationale

Version 0.2 does not infer GADT signatures, support impredicative
instantiation, derive `fold` for GADTs or existential constructors, or expose
equality proofs to ordinary source programs.

The evidence and annotation rationale follow
[Peyton Jones et al. 2006](../../30-sources/peyton-jones-et-al-2006-gadt-inference.md)
and the [C001 advanced checker](../type-system/advanced-type-checking.md).
