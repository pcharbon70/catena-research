---
title: "Exception Boundary"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - failure
  - effects
  - catena
aliases:
  - "G081 exception boundary route"
---

# Exception Boundary

## Purpose

This map routes the G081 question — whether exceptions are an
effect, process exits, foreign failures, programmer panics, or
several distinct mechanisms — through the archive's decision
trail. The normative answer will be revision `0.1.47` in
`60-specification/exception-boundary/`.

## The route

1. **The taxonomy that fixed failure.** [The Six
   Categories](../60-specification/runtime-failure-taxonomy/the-six-categories.md)
   (C036) fixes the single terminal `trap(reason)` with kinded
   reasons and the reserved kinds — the partition's fatal edge.
2. **The door that closed language exceptions.** [Context Rules
   and Reservations](../60-specification/pattern-contexts/context-rules-and-reservations.md)
   (C044) excludes exception clauses permanently, with reopening
   C036's taxonomy as the arrival condition.
3. **The discipline that makes the pattern work.** [Deep Handlers
   and Affine
   Resumptions](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
   (C005) — a handler may decline to resume: the one-shot escape.
4. **The locality evidence.** C010's process-local trap (trapping
   child, spared spawner) — the standing witness that process
   exits are a distinct, routed mechanism (G084).
5. **The contract.** The Exception Boundary Specification
   (`60-specification/exception-boundary/`): the partition, the
   blessed pattern, panic-as-trap-kind, the routing table, and
   conformance.
6. **The reasoning and decision record.** [Catena Exception
   Boundary](../20-notes/catena-exception-boundary.md) argues the
   partition; the [resolved
   inquiry](../40-inquiries/are-exceptions-an-effect-a-trap-or-a-value.md)
   preserves the forks.

## Related maps

- [Runtime Failure Taxonomy map](runtime-failure-taxonomy.md) —
  the fatal edge of the partition.
- [Selective Receive map](selective-receive.md) — the preceding
  Section 9 closure.
