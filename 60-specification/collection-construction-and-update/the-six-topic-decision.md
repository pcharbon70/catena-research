---
title: "The Six-Topic Decision"
kind: specification
created: "2026-08-31"
status: normative
spec_version: "0.1.37"
tags:
  - collections
  - specification
aliases:
  - "Catena collection topics"
---

# The Six-Topic Decision

## Status and authority

This chapter is the normative Catena 0.1.37 six-topic decision. It
is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It executes the classification of
[The Twelve-Way Classification](../built-in-data-model/the-twelve-way-classification.md)
over the boundary of
[The Operation Table](../structural-records-and-variants/the-operation-table.md),
the comparable set of
[The Comparable Set](../equality-and-ordering/the-comparable-set.md),
and the taxonomy of
[The Six Categories](../runtime-failure-taxonomy/the-six-categories.md).

The rules apply only to source-language revision `0.1.37`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The decision

The checklist's six topics resolve as (`CO-OBL-002`):

> **Normative definition.**

| Topic | Decision |
| --- | --- |
| Persistent update | **is** ordinary constructor application and match-based recursion — no dedicated update operator exists at the language level; spellings are P109's |
| Duplicate map keys | a **G101 declaration question**: the declaring slice of any key-carrying collection MUST state its duplicate-key behavior explicitly; the language fixes only the explicitness |
| Ordering | rides **C035's comparable set**: element and key ordering are the entries already shipped — a collection orders when its elements' types order |
| Key equality | keys must be **comparable** under C035 to serve in equality-dependent operations; non-comparable key types are a typing error in those operations |
| Bounds failures | **typed failure as a value** ([Miss as Value and Complexity](miss-as-value-and-complexity.md)) |
| Complexity promises | **excluded from the language layer** ([Miss as Value and Complexity](miss-as-value-and-complexity.md)) |

## Construction is construction

Building a collection value is applying its declared constructors —
`Cons 1 (Cons 2 Nil)` for a declared List, exactly as `Some 7`
builds an Option. Consuming one is matching its constructors. The
witness set exercises both end-to-end on a declared List: no new
machinery exists, was invented, or is needed (`CO-OBL-003`).

## Collections are not records

C041's boundary stands unchanged: structural records are maps with
select/update/extend/restrict; collections are nominal ADTs with
constructors and match. No collection acquires structural
operations, and no record acquires collection semantics (`CO-OBL-003`).

## Deliberately separate work

Collection declarations remain G101's; miss-type contents and
collection libraries G105's; spellings P109's; the comparable set
C035's; structural records C041's.

## Rationale and evidence (non-normative)

The [collections synthesis](../../20-notes/catena-collection-operations.md)
records why update is constructor application rather than an
operator, and why the trilogy's shape (types, records, operations)
completes the Section 5 decision program. The [resolved
inquiry](../../40-inquiries/how-do-collections-construct-and-update.md)
and [topic map](../../10-maps/collection-construction-and-update.md)
preserve the decision route.
