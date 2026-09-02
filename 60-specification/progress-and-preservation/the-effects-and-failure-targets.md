---
title: "The Effects and Failure Targets"
kind: specification
created: "2026-09-01"
status: candidate
spec_version: "0.1.45"
tags:
  - metatheory
  - effects
  - specification
aliases:
  - "Catena effects metatheory"
---

# The Effects and Failure Targets

## Status and authority

This chapter is the normative Catena 0.1.45 effects-and-failure
target set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It extends the target programs of
[Metatheory](../data-and-patterns/metatheory.md) (C002) and
C003's [metatheory](../clause-conditions/metatheory.md) to the
shipped handler calculus of C005 and the failure terminal of
[The Six Categories](../runtime-failure-taxonomy/the-six-categories.md),
using the witnessing discipline of
[Observability and Trace Agreement](../evaluation-order/observability-and-trace-agreement.md).

The rules apply only to source-language revision `0.1.45`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The targets

> **Normative definition.**

For the shipped effect calculus — lexical effects, named deep
handlers, and affine branch-scoped resumptions (C005, unchanged) —
the following targets hold (`PP-OBL-002`):

1. **Installation preservation.** Installing a handler over a
   request-performing computation preserves the computation's type
   modulo the handler's declared input-to-output rows; a handled
   term has the handler's output type (`PP-OBL-002`).
2. **Resume-once preservation.** An operation clause's body runs
   under the resumption's declared result type, and the affine
   discipline (C005) guarantees the resumption is consumed at most
   once per branch; duplication rejects statically and the runtime
   consumed-token check rejects a second resume (`PP-OBL-002`).
3. **Return-clause preservation.** The handler's return clause
   receives the body's value at the input type and produces the
   output type; normal completion preserves the output type
   (`PP-OBL-002`).
4. **Effect progress.** A closed, well-typed handled term is a
   value, performs an operation (dispatched to the innermost
   matching handler), or returns through its handler — it is never
   stuck (`PP-OBL-003`).
5. **Trap terminality.** `trap(reason)` is the failure terminal:
   a trapping evaluation preserves the trap's kinded reason to its
   observer (kernel-verbatim per C036), makes no further
   observable step, and does not disturb any other process's
   world (`PP-OBL-003`).

## Evidence obligations

> **Normative definition.**

Each target carries executable evidence (`PP-OBL-004`): handler
programs agreeing on the reference stepper and compiled BEAM for
values and traces (installation, resume-once, return clause); the
C036 process-context fixture (trapping child, spared spawner) as
the trap-terminal witness; and the C030 dual-agreement methodology
as the standing discipline.

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/catena-progress-and-preservation.md)
records why these statements stop at the shipped calculus: the
open handler-calculus completeness the type-system inquiry names is
not claimed here, and no target extends beyond C005's discipline.
The [resolved
inquiry](../../40-inquiries/what-progress-and-preservation-targets-remain.md)
preserves the decision route.
