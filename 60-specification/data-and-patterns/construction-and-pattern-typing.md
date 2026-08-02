---
title: "Construction and Pattern Typing"
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
  - "Catena constructor and pattern typing"
---

# Construction and Pattern Typing

## Construction

A positional construction supplies exactly the constructor arity:

```catena
Option.Some(7)
```

A named construction supplies every declared field exactly once:

```catena
DeliveryStatus.InTransit { tracking_id: id }
```

Named fields MAY be written in any order. Field expressions MUST evaluate
once, left to right in written order. The resulting semantic payload is
ordered by declaration order. A compiler MAY choose another physical layout
only when it preserves both observations.

Construction instantiates the constructor scheme freshly, checks each field,
and returns the instantiated nominal result. Positional and named constructor
styles MUST NOT be interchanged implicitly.

## Complete 0.2 pattern grammar

Version 0.2 supports exactly these pattern forms:

```text
pattern ::=
    _
  | lower_name
  | integer_literal
  | true | false
  | (pattern, ...)
  | Type.Constructor(pattern, ...)
  | Type.Constructor { field: pattern, ... }
  | Type.Constructor { field: pattern, ..., .. }
  | pattern as lower_name
  | pattern | pattern
```

The final line denotes an `or` pattern within one clause, not a new match
clause. Parenthesization MUST disambiguate combinations where layout alone is
insufficient.

List, structural-record, row-variant, map, binary, string, range, view,
active, and pattern-synonym forms are unsupported in 0.2 and MUST produce
`M005`. A later list type may use ordinary nominal constructors without
retroactively adding list-pattern syntax here.

## Binding rules

A wildcard binds nothing. A binder binds the complete value at its expected
type. An `as` pattern first checks its inner pattern and then binds the same
complete value.

A variable name MUST occur at most once in a single pattern. Equality between
two payload fields must be written as a guard or body expression; repeated
names do not mean equality constraints.

Every alternative of an `or` pattern MUST bind exactly the same names at the
same types and MUST establish the same GADT refinements. The bindings become
available only once, in the containing clause.

## Structural pattern typing

Pattern typing is a checking judgment against an already inferred scrutinee
type. It does not independently synthesize an unrelated type.

- Integer and Boolean patterns require their respective primitive type.
- A tuple pattern requires the same tuple arity and checks elements left to
  right.
- A constructor pattern resolves a visible constructor, freshly instantiates
  it for pattern use, unifies or refines its result against the scrutinee, and
  checks payload patterns against the instantiated field types.
- A positional pattern supplies the exact field count.
- A named pattern without `..` supplies every field exactly once.
- A named pattern with `..` may omit fields but may not name an unknown field.

Patterns themselves are pure and perform no calls, effects, conversions, or
user-defined tests. Successful checking elaborates every pattern to a typed
core node containing resolved nominal and constructor identity, declaration
field order, bindings, and local equality evidence.

## Refutability boundary

All 0.2 pattern forms may occur in match clauses. The executable 0.2 grammar
does not place patterns in function parameters or `let` bindings. When those
contexts are specified, they MUST either admit only patterns proven
irrefutable or define an explicit failure construct. They MUST NOT inherit an
implicit runtime match exception.

Receive clauses, handlers, exception clauses, and comprehensions retain their
own selection and failure rules. This is why checklist item P044 remains
partial even though match-clause refutability is complete.

## Diagnostics and evidence

Invalid bindings, arity, field use, or alternative agreement use `M003`;
unsupported pattern forms use `M005`. Inaccessible constructors use `A004`.

The pattern restrictions and pure boundary follow the
[ADT synthesis](../../20-notes/algebraic-data-types.md). Coverage meaning is
defined separately in [Match Semantics and Coverage](match-semantics-and-coverage.md).
