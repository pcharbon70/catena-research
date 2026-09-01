---
title: "Aliases and Newtypes"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - type-system
  - catena
aliases:
  - "G062 aliases and newtypes route"
---

# Aliases and Newtypes

## Purpose

This map routes the G062 question — aliases, opaque types, and
newtypes — through the archive's decision trail. The normative
answer will be revision `0.1.41` in
`60-specification/aliases-and-newtypes/`.

## The route

1. **The authority vocabulary that closes the opaque third.**
   [Authority and Representation
   Exclusions](../60-specification/abstraction-boundaries/authority-and-representation-exclusions.md)
   fixes C023's complete binary vocabulary (transparent|abstract)
   and the sanctioned smart-constructor idiom — opaque types are
   C022's `abstract` mode, routed not redefined.
2. **The identity spine.** [Declarations and Nominal
   Identity](../60-specification/data-and-patterns/declarations-and-nominal-identity.md)
   anchors type identity in declarations — the pillar the alias
   exclusion defends.
3. **What a wrapper gets.** [The Comparable
   Set](../60-specification/equality-and-ordering/the-comparable-set.md)
   compares through declared structure; [Laws, Derivation, and
   Testing](../60-specification/traits-and-categorical-operations/laws-derivation-and-testing.md)
   gives explicit-target derivation — instances never flow through
   a wrapper.
4. **The precedent for refusing promises.** [The Complexity
   Exclusion](../60-specification/collection-construction-and-update/miss-as-value-and-complexity.md)
   excludes what representation invisibility cannot support — the
   same reason newtypes make no cost promises.
5. **The contract.** The Aliases and Newtypes Specification
   (`60-specification/aliases-and-newtypes/`): the alias exclusion
   with arrival conditions, the newtype form and its rules, and
   conformance.
6. **The reasoning and decision record.** [Catena Aliases and
   Newtypes](../20-notes/catena-aliases-and-newtypes.md) argues the
   mapping; the [resolved
   inquiry](../40-inquiries/should-catena-admit-type-aliases-and-newtypes.md)
   preserves the forks.

## Related maps

- [Abstraction Boundaries map](abstraction-boundaries.md) — the
  authority vocabulary this slice routes to.
- [Numeric Relationships map](numeric-relationships.md) — the
  preceding Section 7 closure.
