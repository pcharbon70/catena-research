---
title: "Standard Hierarchy and Vocabulary"
kind: specification
created: "2026-08-02"
status: normative
spec_version: "0.4"
tags:
  - category-theory
  - specification
  - trait-constraints
aliases:
  - "Catena 0.4 standard traits"
---

# Standard Hierarchy and Vocabulary

## Canonical public surface

The following table is exhaustive. Public names and method names are the
actual ABI; formal names are explanatory metadata only.

| Public capability | Formal reference | Kind | Direct parent(s) | Minimal method ABI |
| --- | --- | --- | --- | --- |
| `Equatable` | Setoid | `Type` | — | `equals left right` |
| `Orderable` | Ord | `Type` | `Equatable` | `compare left right` |
| `Combiner` | Semigroup | `Type` | — | `combine left right` |
| `EmptyCombiner` | Monoid | `Type` | `Combiner` | `empty` |
| `Reducible` | Foldable | `Type -> Type` | — | `summarize callback initial subject` |
| `Mapper` | Functor | `Type -> Type` | — | `map callback subject` |
| `TwoSlotMapper` | Bifunctor | `Type -> Type -> Type` | — | `map_both first_callback second_callback subject` |
| `MultiMapper` | Apply | `Type -> Type` | `Mapper` | `map2 callback first_subject second_subject` |
| `ValueEmbedder` | Applicative | `Type -> Type` | `MultiMapper` | `from_value value` |
| `CollectingMapper` | Traversable | `Type -> Type` | `Mapper`, `Reducible` | `collect_map callback subject` |
| `Chainable` | Chain | `Type -> Type` | `Mapper` | `and_then callback subject` |
| `Workflow` | Monad | `Type -> Type` | `ValueEmbedder`, `Chainable` | no new method |
| `Composable` | Semigroupoid | `Type -> Type -> Type` | — | `compose first next` |
| `IdentityComposer` | Category | `Type -> Type -> Type` | `Composable` | `identity` |
| `TransformRouter` | Arrow | `Type -> Type -> Type` | `IdentityComposer` | `from_transform transform`, `on_first transform` |
| `ContextualMapper` | Extend | `Type -> Type` | `Mapper` | `map_with_context callback subject` |
| `FocusReader` | Comonad | `Type -> Type` | `ContextualMapper` | `read_focus subject` |

An implementation MUST supply exactly the minimal methods declared by its
trait: missing methods and extra override methods are both rejected. Parent
methods come from parent evidence rather than being copied into the child
implementation.

## Argument convention

Callbacks precede data and the principal subject is last. This convention
makes partial application read from behavior toward data and keeps related
operations predictable. `compose first next` means “run `first`, then run
`next`”; its public order is intentionally left-to-right.

## Reference signatures

Using ordinary type notation, representative method shapes are:

> **Normative definition.**

```text
equals            : a -> a -> Bool
compare           : a -> a -> Ordering
combine           : a -> a -> a
summarize         : (b -> a -> b) -> b -> f a -> b
map               : (a -> b) -> f a -> f b
map_both          : (a -> b) -> (c -> d) -> p a c -> p b d
map2              : (a -> b -> c) -> f a -> f b -> f c
from_value        : a -> f a
collect_map       : ValueEmbedder f, MultiMapper f => (a -> f b) -> t a -> f (t b)
and_then          : (a -> m b) -> m a -> m b
compose           : p a b -> p b c -> p a c
map_with_context  : (w a -> b) -> w a -> w b
read_focus        : w a -> a
```

The `Workflow` marker states the combined parent contract without inventing a
second sequencing primitive. `TwoSlotMapper` stays separate from an arbitrary
unary `Mapper` view, preserving which two positions are transformed.

## Standard delivery

The hierarchy is an ordinary standard-library interface compiled and shipped
with the toolchain. The compiler does not recognize these names as semantic
built-ins. A canonical SHA-256 digest binds the interface used by every 0.4
module; a mismatched digest is rejected before evidence selection.

## Connections (non-normative)

The pedagogical rationale is developed in
[An Approachable Vocabulary for Catena](../../20-notes/approachable-language-vocabulary.md).
The mathematical and programming roles are developed in the
[category-theory synthesis](../../20-notes/category-theory-for-programming.md).
