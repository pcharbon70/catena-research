---
title: "Pattern Contexts"
kind: map
created: "2026-08-31"
tags:
  - archive-navigation
  - patterns
  - refutability
  - catena
aliases:
  - "P044 refutability route"
---

# Pattern Contexts

## Purpose

This map routes the P044 question — which pattern contexts admit
refutable patterns and what happens on mismatch — through the
archive's decision trail. The normative answer will be revision
`0.1.38` in the [Pattern Contexts
Specification](../60-specification/pattern-contexts/README.md).

## The route

1. **The boundary that reserved the question.** [Construction and
   Pattern Typing](../60-specification/data-and-patterns/construction-and-pattern-typing.md)
   fixes C002's refutability boundary: patterns in match clauses;
   no implicit runtime match exception in any future binding
   context.
2. **The exhaustive context.** [Match Semantics and
   Coverage](../60-specification/data-and-patterns/match-semantics-and-coverage.md)
   and C045's usefulness relation keep their authority unchanged —
   match stays the only context that demands coverage.
3. **The plain binders that exist today.** [Binding Structure and
   Scope](../60-specification/bindings-and-sequencing/binding-structure-and-scope.md)
   keeps `let` a plain value name; [Deep Handlers and Affine
   Resumptions](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
   keeps handler clauses on plain parameters plus the resumption
   binder. Both become irrefutable-only on arrival.
4. **The synthesis that proposed the answer.** [Algebraic Data
   Types](../20-notes/algebraic-data-types.md) (refutability
   conclusions) and [List Comprehensions](../20-notes/list-comprehensions.md)
   (the total/filtering generator split) supply the principle the
   contract fixes.
5. **The failure taxonomy that closes exception clauses.** [The
   Six Categories](../60-specification/runtime-failure-taxonomy/the-six-categories.md)
   makes `trap` terminal and typed failure a value — there is no
   exception mechanism to hang clauses on.
6. **The contract.** The [Pattern Contexts
   Specification](../60-specification/pattern-contexts/README.md):
   the three classes, the per-context rules, the public-receive
   reservation, the D046 exclusion, and conformance.
7. **The reasoning and decision record.** [Catena Pattern
   Contexts](../20-notes/catena-pattern-contexts.md) argues the
   classification; the [resolved
   inquiry](../40-inquiries/which-pattern-contexts-admit-refutable-patterns.md)
   preserves the forks.

## Related maps

- [Algebraic Data Types map](algebraic-data-types.md) — the C002
  pattern machinery this slice complements.
- [List Comprehensions map](list-comprehensions.md) — where the
  generator principle is consumed.
