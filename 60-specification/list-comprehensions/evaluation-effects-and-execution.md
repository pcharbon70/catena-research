---
title: "Evaluation Effects and Execution"
kind: specification
created: "2026-08-31"
status: normative
spec_version: "0.1.39"
tags:
  - comprehensions
  - evaluation-order
  - effects
  - specification
aliases:
  - "Catena comprehension execution"
---

# Evaluation Effects and Execution

## Status and authority

This chapter is the normative Catena 0.1.39 comprehension
execution, effect, and ordering rule set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies the ordered-forms discipline of C030 and rides the
effect rows of C005.

The rules apply only to source-language revision `0.1.39`.

## Exact order

> **Normative definition.**

Traversal follows source order exactly (`LC-OBL-008`): qualifier by
qualifier, left to right, and within a generator source, element by
element in the source list's order. Each element's qualifier suffix
runs to completion — including the yield — before the next element
of the same source (`LC-OBL-008`). Boolean filters do not
short-circuit their own evaluation: the expression is evaluated
once per reaching and its effects occur even when the value is
`false`; what `false` skips is the suffix, not the test
(`LC-OBL-008`).

## Failure timing

> **Normative definition.**

A failure at any qualifier abandons the whole comprehension at that
point: no further elements are visited and no partial result
exists (`LC-OBL-008`). Traps follow C036; effect failures follow
their handlers; a filtering generator's pattern mismatch is not a
failure (it skips).

## Effect rows

> **Normative definition.**

The comprehension's effect row is the union of its sources',
filters', bindings', and yield expression's effect rows; each
repeated evaluation repeats its effects, so a filter or yield under
a generator performs its effects once per emitted candidate
element (`LC-OBL-008`). The comprehension itself performs no hidden
effects and requests no capability none of its parts request.

## Sequential execution is normative

> **Normative definition.**

Execution is sequential: the observable trace is exactly the
single-threaded source-order trace above on every conforming
target (`LC-OBL-012`). Parallel traversal is excluded from this
revision; any future parallel form requires its own syntax, its own
effect and cancellation rules, and structured-concurrency
obligations in its own slice (`LC-OBL-012`). An implementation
MUST NOT parallelize qualifiers, generators, or yields, and MUST
NOT reorder effectful evaluations, even where purity analysis
suggests it is safe — reordering is observable through effects
(`LC-OBL-012`).

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/list-comprehensions.md) argues why
"effects are allowed but not hidden": pure-only comprehensions
force generic `map` to pretend effectfulness, while silent effect
repetition is the classical comprehension hazard. C030's
reference/BEAM trace agreement supplies the witnessing discipline.
