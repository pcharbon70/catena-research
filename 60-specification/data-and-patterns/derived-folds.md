---
title: "Derived Folds"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.2"
tags:
  - algebraic-data-types
  - combinators
  - specification
aliases:
  - "Catena constructor-complete fold derivation"
---

# Derived Folds

## Explicit request

Version 0.2 supports exactly one datatype derivation:

```catena
type Option A =
  | None
  | Some A
  derives fold
```

Generation is opt-in. The public generated operation is `Option.fold`; its
identity belongs to the declaring module and type.

Unknown derivations are invalid with `A001`. GADTs and constructors with
existential binders are ineligible with `A003`.

## Signature

For constructors `C1` through `Cn`, the generated fold takes one handler per
constructor in declaration order, followed by the datatype value. A nullary
constructor handler is a result value. A payload constructor handler is a
curried function receiving fields in declaration order.

For `Option`:

```text
Option.fold : forall A R. R -> (A -> R) -> Option A -> R
```

For `Pair A B = Pair A B`:

```text
Pair.fold : forall A B R. (A -> B -> R) -> Pair A B -> R
```

The selected handler is invoked exactly once. Unselected handlers are not
invoked. Payload values are passed without recursive traversal.

## Meaning and limits

This operation is constructor-complete case elimination. It is not
automatically a recursive catamorphism, collection fold, short-circuiting
iterator, or categorical `Foldable` implementation.

Negative and nested recursive payloads do not invalidate this nonrecursive
eliminator. The compiler still records positivity, variance, and regularity so
later recursive or categorical derivations can enforce their own conditions.
Version 0.2 generates no mapping, traversal, ordering, equality, optics, or
type-class dictionaries.

## Generated evidence

Generated code MUST:

- carry `compiler-derived` provenance;
- be represented in typed core rather than injected as unchecked BEAM forms;
- be rejected when constructor count, field order, scheme, eligibility, or
  provenance is inconsistent; and
- be present in the public interface only when the datatype's constructors are
  transparent.

The backend MAY lower the verified fold directly to a constructor dispatch,
provided both required layouts have identical source observations.

## Rationale and evidence

This narrow derivation supplies useful, predictable elimination without
claiming the laws or traversal behavior of later categorical classes. The
distinctions are developed in
[Combinators for Algebraic Data and Categorical Programming](../../20-notes/combinators-for-algebraic-data-and-categorical-programming.md).
Broader trait derivation is specified independently by normative
[C073](../traits-and-categorical-operations/laws-derivation-and-testing.md);
that later contract does not retroactively make this C002 fold a categorical
operation.
