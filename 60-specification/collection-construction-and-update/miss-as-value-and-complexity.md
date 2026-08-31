---
title: "Miss as Value and Complexity"
kind: specification
created: "2026-08-31"
status: candidate
spec_version: "0.1.37"
tags:
  - collections
  - failure
  - complexity
  - specification
aliases:
  - "Catena miss and complexity"
---

# Miss as Value and Complexity

## Status and authority

This chapter is the normative Catena 0.1.37 bounds-failure and
complexity contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies the taxonomy of
[The Six Categories](../runtime-failure-taxonomy/the-six-categories.md)
and the observability of
[The Observability Model](../resource-observability/the-observability-model.md)
to collection lookups.

The rules apply only to source-language revision `0.1.37`.

## Miss as value

> **Normative definition.**

A collection lookup that finds no value is **typed failure as a
value**: normal termination with a domain answer — the shape an
Option-typed return gives — never a trap, never an undefined
outcome (`CO-OBL-004`). Collections stay total: no lookup operation
introduces an abnormal-termination path. The concrete miss type is
the declaring library's (G101/G105); the language contract fixes
the classification and the totality, nothing more.

This is G036's mapping executed: typed failure is a value, so a
miss is a value; an implementation MUST NOT use this area's
boundary to claim a trapping lookup.

## The complexity exclusion

> **Normative definition.**

No complexity bound is a language-level promise (`CO-OBL-005`).
Complexity documentation is G101's library-level contract, stated
per operation, clearly separated from language semantics.

The rationale is architectural, and closing: representation is
invisible ([The Observability Model](../resource-observability/the-observability-model.md))
— collections are libraries over invisible representations — and
nominal data is representation-independent (C002). A language-level
complexity promise would make representation observable the moment
a conforming implementation chose a different one, amending C037
and narrowing C002. The language promises values, effects, and
totals; libraries document costs.

Implementations MUST NOT claim complexity conformance from this
area, and no complexity measurement is a language-level observation
(`CO-OBL-008`).

## Determinism

Equal collections, keys, and operations produce equal answers and
traces on every conforming target (`CO-OBL-008`).

## Deliberately separate work

Miss-type contents and collection libraries remain G105's; G101
owns the declared collections and their complexity documentation;
runtime performance observability remains G124's tool-side channel.

## Rationale and evidence (non-normative)

The [collections synthesis](../../20-notes/catena-collection-operations.md)
records why the exclusion is forced by the corpus's own architecture
rather than chosen, and why libraries may still document costs. The
[topic map](../../10-maps/collection-construction-and-update.md)
routes the decision.
