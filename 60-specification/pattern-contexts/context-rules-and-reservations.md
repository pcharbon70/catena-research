---
title: "Context Rules and Reservations"
kind: specification
created: "2026-08-31"
status: normative
spec_version: "0.1.38"
tags:
  - patterns
  - refutability
  - specification
aliases:
  - "Catena context rules"
---

# Context Rules and Reservations

## Status and authority

This chapter is the normative Catena 0.1.38 per-context rule set.
It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies the classes of
[The Three Context Classes](the-three-context-classes.md) to every
context P044 names and closes D046's exclusion.

The rules apply only to source-language revision `0.1.38`.

## The context table

> **Normative definition.**

| Context | Class | 0.1.38 rule |
| --- | --- | --- |
| Match clauses | exhaustive | unchanged; C045 decides (`PC-OBL-003`) |
| `let` binders | irrefutable-only on arrival | today the binder is a plain value name and pattern binding is not a `let` form (C031); when a pattern form arrives it MUST be proved total or carry an explicit failure construct in its own slice (`PC-OBL-004`) |
| Function parameters | irrefutable-only on arrival | plain names today (C002 reservation); on arrival, proved-total or explicit-failure in its own slice (`PC-OBL-004`) |
| Comprehension generators | split, principle fixed | an ordinary generator's pattern MUST be total for the source element type; a filtering generator MUST request mismatch-as-skip visibly; the comprehension grammar, effects, and lowering are the comprehension area's (`0.1.39`) (`PC-OBL-005`) |
| Public receives | reserved | none exists (the C003 receive is a typed lowering harness); on arrival, a public receive MUST be exhaustive over its message type or carry an explicit total fallback (timeout or default) in its own slice (`PC-OBL-006`) |
| Handler clauses | irrefutable-only on arrival | operation clauses bind plain parameters plus the resumption binder (C005); when patterns arrive they MUST be proved total or carry an explicit failure construct (`PC-OBL-007`) |
| Exception clauses | excluded | no exception mechanism exists or is planned: `trap` is terminal and typed failure is a value (C036); a slice that introduces exception clauses MUST first reopen that taxonomy (`PC-OBL-008`) |

## The programmable-pattern exclusion

> **Normative definition.**

View patterns, pattern synonyms, and active patterns are excluded
(`PC-OBL-009`). Patterns remain pure — no calls, effects,
conversions, or user-defined tests (C002). A future programmable
pattern form MUST arrive in its own slice and MUST state its
effects, totality, coverage obligations, evaluation count, and cost
before existing; this area reserves no hidden conversion semantics
for it.

## Reservation discipline

> **Normative definition.**

A slice that consumes a reservation in this chapter MUST name the
consumed row, MUST place its grammar under its own revision, and
MUST NOT weaken another row's class. A binding position this table
does not name inherits the irrefutable-only default of
[The Three Context Classes](the-three-context-classes.md#the-default)
(`PC-OBL-004`).

## Rationale and evidence (non-normative)

The [pattern-contexts synthesis](../../20-notes/catena-pattern-contexts.md)
carries the context inventory and the argument that reservations
must be narrow — a shipped binding position whose mismatch behavior
this table did not name falsifies the table and requires a new
revision. The [list-comprehensions synthesis](../../20-notes/list-comprehensions.md)
proposes the generator split this chapter fixes as principle; the
[ADT synthesis](../../20-notes/algebraic-data-types.md) supplies the
refutability conclusions.
