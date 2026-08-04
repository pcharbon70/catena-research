---
title: "Declarations and Nominal Identity"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.1.2"
tags:
  - algebraic-data-types
  - modules
  - specification
  - type-inference
aliases:
  - "Catena datatype declarations"
---

# Declarations and Nominal Identity

## Surface form

An ordinary datatype has this canonical shape:

> **Non-normative example.**

```catena
type Option A =
  | None
  | Some A

type DeliveryStatus =
  | Queued
  | InTransit { tracking_id: TrackingId }
```

Parameters and explicit existential binders MUST carry kinds in the resolved
syntax. The 0.1.2 executable slice accepts only `Type`-kinded parameters, while
the general kind grammar remains controlled by C001.

Each constructor has exactly one payload product. A nullary constructor has
the unit product; positional fields form an ordered product; named fields are
labels on that product. Named constructor fields are not structural row
records and do not acquire row-polymorphic selection or update.

## Nominal generation

Each declaration MUST generate a fresh nominal type identity. Its compilation
identity is the triple:

> **Normative definition.**

```text
{canonical package/build origin, module, type name}
```

Two declarations with identical constructors are distinct when any identity
component differs. Renaming the origin, module, or type is identity-breaking.
An alias, if later introduced, MUST be a different declaration form and MUST
NOT silently generate a new identity.

Constructor identity combines the nominal type identity with its constructor
name. Constructor ordinal is declaration order and is metadata, not source
identity.

## Recursive groups

A mutually recursive group elaborates in three phases:

1. allocate every nominal header and parameter kind;
2. check every constructor field and refined result in the complete header
   environment; and
3. publish all declarations only if the complete group succeeds.

A failure MUST publish none of the group. Duplicate type, constructor, or
field names are invalid.

Any well-kinded recursive payload is accepted, including nested and negative
occurrences. Acceptance does not assert positivity, termination, induction,
or functoriality. The compiler MUST calculate positivity and regularity before
allowing a later operation whose meaning depends on either property.

## Constructor schemes

For an ordinary declaration

> **Non-normative example.**

```catena
type Result E A =
  | Error E
  | Okay A
```

the constructors have rank-1 schemes equivalent to:

> **Normative definition.**

```text
Error : forall E A. E -> Result E A
Okay  : forall E A. A -> Result E A
```

Every ordinary constructor MUST return the declared type applied to its
parameters in declaration order. Adding such schemes to the value environment
MUST preserve the C001 principal-core guarantee.

An explicit `returns` clause selects the GADT rule rather than weakening this
ordinary rule:

> **Non-normative example.**

```catena
type Expr A =
  | IntLit(Int) returns Expr Int
```

Its result MUST still be the declared nominal type at the correct arity.

## Visibility and names

A public datatype interface is exactly one of:

- **transparent** — exports the nominal type and its complete constructor
  family; or
- **abstract** — exports only nominal identity and kind.

Code inside the declaring module may use all local constructors. A client may
construct or match only constructors present in a transparent imported
interface. Version 0.1.2 has no separate construct-only or match-only authority.

The canonical source reference is `Type.Constructor` locally and
`Module.Type.Constructor` across modules. Imported constructors remain
qualified unless an explicit constructor import supplies an unqualified name
or alias. Wildcard constructor imports are not part of 0.1.2. Ambiguous or
duplicate aliases are invalid.

## Diagnostics and evidence

Ill-kinded declarations use `A001`; duplicate identities use `A002`; invalid
payloads or results use `A003`; inaccessible constructors use `A004`; nominal
identity disagreement uses `A005`.

## Rationale and evidence (non-normative)

The elaboration and abstraction rationale follows the
[ADT synthesis](../../20-notes/algebraic-data-types.md). Executable cases cover
empty, phantom, nested, negative, and mutually recursive declarations plus
transparent and abstract cross-module use.
