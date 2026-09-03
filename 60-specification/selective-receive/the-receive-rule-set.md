---
title: "The Receive Rule Set"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.46"
tags:
  - receive
  - processes
  - specification
aliases:
  - "Catena receive rules"
---

# The Receive Rule Set

## Status and authority

This chapter is the normative Catena 0.1.46 selective-receive rule
set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates the harness semantics of
[Clause Contexts and Receive](../clause-conditions/clause-contexts-and-receive.md)
(C003, unchanged) to language-level rules without amending them.

The rules apply only to source-language revision `0.1.46`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The rules

> **Normative definition.**

Selective receive obeys the following rules (`RC-OBL-002`):

1. **Scan order.** A receive attempt scans its process's mailbox
   from the oldest queued message toward the newest (`RC-OBL-002`).
2. **Preservation.** A message its clauses reject remains queued,
   in position, and scanning continues (`RC-OBL-002`).
3. **One-time removal.** The selected message is removed exactly
   once, before its body runs (`RC-OBL-002`).
4. **Message typing.** A receive requires one explicit closed
   message type containing no free or rigid type variable; its
   clauses are pattern-typed against that type (C003, unchanged)
   (`RC-OBL-003`).
5. **Effects.** The receive form itself performs no effects: no
   capability, no request, no send. Clause bodies carry their own
   effect rows (`RC-OBL-003`).
6. **Conditions.** Only the portable native condition set
   admitted by C003 applies; or-pattern expansion rejects as
   `CND006` (unchanged) (`RC-OBL-003`).

## Starvation and cost

> **Normative definition.**

A receive whose clauses reject a prefix of its mailbox starves
while that prefix stands: no fairness guarantee beyond scan order
exists and none is claimed (`RC-OBL-004`). The cost explanation —
not an asymptotic promise, following C042's exclusion — is: each
receive attempt's scan cost is proportional to the rejected prefix
it examines, and a stable rejected prefix is re-examined by every
subsequent attempt until it is consumed or displaced
(`RC-OBL-004`).

## No hidden semantics

> **Normative definition.**

No receive form consumes, reorders, or duplicates a rejected
message; no receive performs work between examining two
candidates; and no implementation optimizes a scan away unless
every observable outcome — selected value, final mailbox, and
clause effects — is identical (`RC-OBL-002`).

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/catena-selective-receive.md)
argues these rules were already true in the harness and needed
only the language-level statement; the preservation witness
(select `Some 1` while `Some 0` stays queued) demonstrates the
central claim directly. The [resolved
inquiry](../../40-inquiries/how-does-selective-receive-complete.md)
preserves the decision route.
