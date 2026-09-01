---
title: "Dynamic and Unsafe Boundaries"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - type-system
  - catena
aliases:
  - "G067 unsafe boundaries route"
---

# Dynamic and Unsafe Boundaries

## Purpose

This map routes the G067 question — casts, runtime type
inspection, unchecked operations, compiler intrinsics, and
visible unsafety — through the archive's decision trail. The
normative answer will be revision `0.1.43` in
`60-specification/dynamic-and-unsafe-boundaries/`.

## The route

1. **The guard vocabulary (anchor one).** [Syntax and
   Safety](../60-specification/clause-conditions/syntax-and-safety.md)
   already rejects the dynamic-test, reflection, and unchecked-cast
   forms where they were ever tempted.
2. **Erasure (anchor two).** [Artifacts, Erasure, and
   CLI](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md)
   keeps type and specification material out of runtime artifacts
   — nothing to inspect at runtime.
3. **The failure taxonomy (anchor three).** [The Six
   Categories](../60-specification/runtime-failure-taxonomy/the-six-categories.md)
   fixes `trap(reason)` with kinded reasons and no cast-failure
   kind; foreign raises already map to `trap(reason)`.
4. **A visible host boundary in kind.** The [BEAM float
   probes](../50-journal/2026-08-31-beam-float-boundary-probes.md)
   record the term format refusing non-finite payloads — refusal
   as visibility, the precedent the foreign edges inherit.
5. **The contract.** The Dynamic and Unsafe Boundaries
   Specification (`60-specification/dynamic-and-unsafe-boundaries/`):
   the five intralanguage exclusions with arrival conditions, the
   foreign visibility routing to G095/G096/G098, and conformance.
6. **The reasoning and decision record.** [Catena Dynamic and
   Unsafe Boundaries](../20-notes/catena-dynamic-and-unsafe-boundaries.md)
   argues the three-anchor reading; the [resolved
   inquiry](../40-inquiries/should-catena-have-dynamic-or-unsafe-boundaries.md)
   preserves the forks.

## Related maps

- [Name Resolution map](name-resolution.md) — the preceding
  Section 7 closure.
- [Runtime Failure Taxonomy map](runtime-failure-taxonomy.md) —
  the taxonomy a future cast form must amend.
