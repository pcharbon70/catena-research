---
title: "Numeric Relationships"
kind: map
created: "2026-08-31"
tags:
  - archive-navigation
  - numerics
  - catena
aliases:
  - "G061 numeric relationships route"
---

# Numeric Relationships

## Purpose

This map routes the G061 question — how `Int` and `Float` relate
across operators — through the archive's decision trail. The
normative answer will be revision `0.1.40` in
`60-specification/numeric-relationships/`.

## The route

1. **The exclusions already frozen.** [Numeric Types and Literal
   Typing](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md)
   rejects defaulting, implicit coercion, and literal constraints
   (`NM-OBL-005`/`NM-OBL-006`), collapsing G061's five options to
   one real fork.
2. **The routing that named this slice.** [Precedence and
   Associativity](../60-specification/operators-and-punctuation/precedence-and-associativity.md)
   leaves operator dispatch to G061 and division/remainder to
   G105/G061.
3. **The pattern already in force.** [The Comparable
   Set](../60-specification/equality-and-ordering/the-comparable-set.md)
   types ordering same-type over `Int`/`Float`; C018's negation is
   total over both — the instantiation rule this slice generalizes.
4. **The classification that fixes the closed set.** [The Twelve-Way
   Classification](../60-specification/built-in-data-model/the-twelve-way-classification.md)
   makes `Int` and `Float` the numeric runtime types of the data
   model.
5. **The contract.** The Numeric Relationships Specification
   (`60-specification/numeric-relationships/`): the closed-set
   instantiation rule, the dispatch exclusion, float arithmetic,
   and the G105 routings.
6. **The reasoning and decision record.** [Catena Numeric
   Relationships](../20-notes/catena-numeric-relationships.md)
   argues the rule; the [resolved
   inquiry](../40-inquiries/how-should-int-and-float-relate-across-operators.md)
   preserves the forks.

## Related maps

- [Numeric literal semantics map](numeric-literal-semantics.md) —
  the literal half of the numeric program.
- [Built-In Data Model map](built-in-data-model.md) — the closed
  set's home.
