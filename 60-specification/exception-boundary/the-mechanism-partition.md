---
title: "The Mechanism Partition"
kind: specification
created: "2026-09-01"
status: candidate
spec_version: "0.1.47"
tags:
  - failure
  - effects
  - specification
aliases:
  - "Catena exception partition"
---

# The Mechanism Partition

## Status and authority

This chapter is the normative Catena 0.1.47 exception-boundary
partition. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It restates as routing rows the standing rules of
[The Six Categories](../runtime-failure-taxonomy/the-six-categories.md)
(C036), [Context Rules and Reservations](../pattern-contexts/context-rules-and-reservations.md)
(C044), [Deep Handlers and Affine Resumptions](../effects-and-handlers/deep-handlers-and-affine-resumptions.md)
(C005), and C010's process-local trap evidence — amending none.

The rules apply only to source-language revision `0.1.47`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The partition

> **Normative definition.**

Failure handling in edition `0.1` is a partition into three
visibly distinct mechanisms, and no language exception form exists
(`XB-OBL-002`):

1. **Typed failure is a value** (`XB-OBL-002`): `Option`- and
   `Result`-shaped failures are ordinary first-class values,
   produced and consumed by ordinary code; their contents remain
   G103's.
2. **Exception-style catching is the effect pattern**
   (`XB-OBL-003`): a request whose handler declines to resume is a
   one-shot escape to that handler's result — visible in the
   effect row, catchable only by an enclosing handler, and a
   library idiom over C005's unchanged semantics (`XB-OBL-003`).
   This statement is descriptive; it adds no rule.
3. **Fatal failure is `trap(reason)`** (`XB-OBL-002`): the one
   terminal mechanism — kinded, local to its process, never
   catchable (C036, unchanged).

No construct blurs the classes, and no construct converts one
into another silently: converting an abort to a trap is a
handler's explicit choice to trap instead of resuming; converting
a trap to a value is impossible (`XB-OBL-002`).

## Panic classification

> **Normative definition.**

A programmer panic **is** a `trap` carrying the reserved
assertion/panic kind, entering with its producer under C036's
per-producer gate (`XB-OBL-004`). No separate panic construct
exists, and none is planned; a future producer (an assert form, a
checked-arithmetic fault) arrives with its kind, its visibility,
and its diagnostics in its own revision (`XB-OBL-004`).

## The routing table

> **Normative definition.**

| Mechanism | Classification | Owner |
| --- | --- | --- |
| Process exits | a distinct mechanism: process death, not language exceptions; C010's local-trap/spared-spawner stands | G084 |
| Foreign failures | map to `trap(reason)` (C036 standing), typed at the visible foreign boundary | G095/G096 (with C067's rule) |
| Cancellation | its own time-and-cancellation program, interacting with the pattern per its own slice | G088 |
| Library faults (arithmetic, division) | kinded traps or typed values per producer | G105 |
| Outcome types | value-shaped failure contents | G103 |

(`XB-OBL-005`.)

## The door

> **Normative definition.**

A language exception form (raise, catch, try, rescue, exception
clauses) does not exist and arrives only by a revision that first
reopens C036's taxonomy and states its catch semantics, its
visibility, and its evidence interaction — C044's arrival
condition, restated as the only amendment route (`XB-OBL-006`).

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/catena-exception-boundary.md)
argues why every candidate answer already had a home and what a
universal `catch` would cost the three-way partition. The
[resolved inquiry](../../40-inquiries/are-exceptions-an-effect-a-trap-or-a-value.md)
preserves the decision route.
