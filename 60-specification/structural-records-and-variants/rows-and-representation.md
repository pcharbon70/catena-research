---
title: "Rows and Representation"
kind: specification
created: "2026-08-29"
status: normative
spec_version: "0.1.36"
tags:
  - records
  - rows
  - specification
aliases:
  - "Catena row model"
---

# Rows and Representation

## Status and authority

This chapter is the normative Catena 0.1.36 row-typing and
representation contract for structural records and variants. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the row types of the kernel's type
module and the semantic-map rule of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md),
under the representation freedom of
[The Observability Model](../resource-observability/the-observability-model.md).

The rules apply only to source-language revision `0.1.36`.

## The row model

> **Normative definition.**

- A record literal or variant injection has a **closed row**: its
  field set is complete at the expression (`SR-OBL-003`).
- `extend` and `restrict` produce closed rows over closed inputs;
  no expression produces an open row.
- **Open tails exist only in type positions** — signatures, type
  variables, and their substitution — never from an expression.
  Row-polymorphic behavior is exactly this composition: a signature
  with an open tail instantiates over any closed record whose field
  set satisfies it (`SR-OBL-004`).
- `select`, `update`, `extend`, and `restrict` address one label;
  the addressed label's presence or absence is a static fact, and the
  missing-label operations are statically unreachable
  (`SR-OBL-003`).

No open-record literal exists, and none may arrive except through a
slice that extends the expression grammar explicitly — a gated
arrival, never a compatible addition.

## The representation clause

> **Normative definition.**

A record is a **semantic finite unique-label-to-value map**. Written
field order controls evaluation order (C030) and never equality,
comparison, or row identity (C035/C037) (`SR-OBL-005`). Record-map
sharing, copying, and representation — map, tuple, unboxed — are not
observable Catena values (C037); the BEAM backend's map lowering is
one permitted representation among invisible equals. A structural
variant's runtime form carries its semantic label and payload and
nothing else.

## Determinism

Equal closed records and equal operations produce equal results,
effects, and traces on every conforming target (`SR-OBL-008`).

## Deliberately separate work

G042's collection construction and update are distinct work: maps
and sets are G101 library types under C040's classification, not
structural records. Representation-adjacent guarantees remain C037's
exclusions, unchanged.

## Rationale and evidence (non-normative)

The [records synthesis](../../20-notes/catena-structural-records.md)
records why closed literals with type-position tails are the honest
model the kernel already fixed. The [topic
map](../../10-maps/structural-records.md) routes the decision.
