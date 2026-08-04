---
title: "Type Language and Kinds"
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
  - "Catena 0.1.1 type syntax"
---

# Type Language and Kinds

## Type grammar

The abstract type language is:

> **Normative definition.**

```text
k ::= Type | Row(record) | Row(variant) | Row(effect) | k -> k
t ::= a | C | t t | (t1, ..., tn) | { r } | < r >
    | t1 ->{ e } t2 | forall a:k. t | t requires q1, ..., qn
q ::= Trait t1 ... tn | label absent r | t1 ~ t2
```

`A -> B` is sugar for `A ->{} B`. Function arrows associate to the right.
Type application associates to the left. `requires` has the lowest precedence.
Quantification inside a type is always written with `forall`.

A top-level signature implicitly quantifies free variables at its outermost
level. Thus `id : a -> a` means `id : forall a:Type. a -> a`. Nested or
higher-rank quantification MUST be explicit. An implementation MUST print the
explicit form when ambiguity about binder scope is possible.

## Rows and kinds

Record, variant, and effect rows have distinct kinds and cannot unify across
kind boundaries. Record and variant rows contain unique labels and may carry
`label absent r` constraints. Effect rows are finite duplicate-label
multisets with an optional tail. Row equality ignores written order but, for
effects, preserves multiplicity and lexical capability identity.

Type constructors have declared kinds. Application `t u` is well kinded only
when `t : k1 -> k2` and `u : k1`. All term-level types must ultimately have
kind `Type`. Unification MUST perform an occurs check and a kind check before
binding a metavariable.

## Constraints

Trait predicates are ordered only for stable presentation; their logical
meaning is conjunction. Equality predicates created by a GADT pattern are
scoped to its branch and are not general signature constraints. Lacks
predicates apply only to unique record or variant rows.

A scheme is ambiguous when a quantified variable appears in its constraints
but is not determined by the result type, effect, or the declared functional
dependencies of those constraints. Ambiguous schemes are invalid. Catena 0.1.1
has no numeric or other type defaulting.

## Signatures and exports

Every exported value MUST declare a signature. The implementation checks the
definition against that signature using skolemization and subsumption; it does
not merely compare pretty-printed inferred types. Every recursively
polymorphic definition and every advanced-profile definition also requires an
enclosing signature.

Type aliases MUST be expanded for equality but preserved where possible in
diagnostics. Nominal types are equal only by declared identity. There is no
implicit subtyping or implicit coercion in this slice.

The inference behavior for these types is specified by
[Principal Inference and Generalization](principal-inference-and-generalization.md),
and row equality by [Rows, Traits, and Effects](rows-traits-and-effects.md).
