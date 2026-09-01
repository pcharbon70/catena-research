---
title: "Name Resolution"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - name-resolution
  - type-system
  - catena
aliases:
  - "G066 name resolution route"
---

# Name Resolution

## Purpose

This map routes the G066 question — whether field, method,
constructor, literal, and operator resolution may depend on
inferred types — through the archive's decision trail. The
normative answer is revision `0.1.42` in the [Name Resolution
Specification](../60-specification/name-resolution/README.md).

## The route

1. **The scope-structural model (pillar one).** [Namespaces and
   Shadowing](../20-notes/namespaces-and-shadowing.md) and C021's
   area fix resolution as a function of scope structure alone,
   rejecting the order-dependent open-re-shadowing model.
2. **Spelling decides literals (pillar two).** [Numeric Types and
   Literal Typing](../60-specification/numeric-literal-semantics/numeric-types-and-literal-typing.md)
   bans constraint generation and expected-type adaptation.
3. **Evidence settles before calls (pillar three).**
   [Declarations, Instances, and
   Coherence](../60-specification/traits-and-categorical-operations/declarations-instances-and-coherence.md)
   rejects ambiguity at the instance, never at the call site.
4. **No name choice for operators (pillar four).** [The Closed-Set
   Instantiation
   Rule](../60-specification/numeric-relationships/the-closed-set-instantiation-rule.md)
   fixes one rule per operator over {Int, Float}.
5. **The contract.** The [Name Resolution
   Specification](../60-specification/name-resolution/README.md):
   the invariant, the five-way classification table, the
   evidence-selection carve-out, the exclusions with arrival
   conditions, and conformance.
6. **The reasoning and decision record.** [Catena Name
   Resolution](../20-notes/catena-name-resolution.md) argues the
   roof-over-pillars reading; the [resolved
   inquiry](../40-inquiries/may-name-resolution-depend-on-inferred-types.md)
   preserves the forks.

## Related maps

- [Namespaces and Shadowing map](namespaces-and-shadowing.md) —
  the scope model the invariant rests on.
- [Aliases and Newtypes map](aliases-and-newtypes.md) — the
  preceding Section 7 closures.
