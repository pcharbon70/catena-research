---
title: "The Observability Model"
kind: specification
created: "2026-08-26"
status: normative
spec_version: "0.1.33"
tags:
  - observability
  - specification
aliases:
  - "Catena observability model"
---

# The Observability Model

## Status and authority

This chapter is the normative Catena 0.1.33 observability-model
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the resource-observability rules of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md)
and the identity and message rules of
[Actors, Messages, and Failures](../formal-semantic-kernel/actors-messages-and-failures.md),
under the value grammar of
[Value Forms and First-Classness](../values-and-evaluation/value-forms-and-first-classness.md).

The rules apply only to source-language revision `0.1.33`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The six-way classification

The checklist's six categories classify as (`RO-OBL-002`):

> **Normative definition.**

| Category | Program observability at 0.1.33 |
| --- | --- |
| Allocation addresses | **none** |
| Sharing (record maps, message copy vs alias) | **none** — semantic identity |
| Garbage collection | **none** |
| Object identity | **process identity only** |
| Stack use | completion versus the proper-tail-call guarantee only (C032/C034) |
| Finalization | **none** — declared absent ([Identity and Finalization](identity-and-finalization.md)) |

Allocation addresses, closure identity, record-map sharing, garbage
collection, stack-frame shape outside the proper-tail-call guarantee,
and physical copying are not observable Catena values — the kernel's
sentence, elevated verbatim (`RO-OBL-003`).

## Semantic identity

> **Normative definition.**

```text
Equal values are interchangeable. Physical representation —
copy or share, boxed or unboxed, moved or pinned — never
changes a program's meaning.
```

- The message rule rides the same principle: a message is an
  immutable first-order value whose physical copy or sharing does not
  change its meaning (C010).
- Storing a value — a handle included — observes nothing beyond the
  value itself; C029's uniform-first-classness exclusions resolve
  here (`RO-OBL-003`).
- Implementations retain every representation freedom as a
  consequence: sharing, unboxing, deduplication, CPS transformation,
  and GC movement are unobservable by construction, which is the
  freedom C030's within-step grant already prices (`RO-OBL-008`).

## Stack use

The proper-tail-call guarantee
([Closures and Tail Calls](../functions-and-calls/closures-and-tail-calls.md))
is the **only** stack-related promise: a call in tail position
consumes no unbounded Catena stack. Outside that guarantee, stack use
— depth, frame shape, growth — is not observable: programs may infer
only completion versus non-completion, and non-tail recursion's
legality (C034) carries no conformance claim about stack
(`RO-OBL-002`).

## Deliberately separate work

Handle operations beyond the kernel's remain G084's;
message-copy mechanics beyond semantic irrelevance remain G085's;
resource scopes and cleanup remain the G080s era; foreign
finalization remains G095's; debugging tools remain G124's.

## Rationale and evidence (non-normative)

The [observability synthesis](../../20-notes/catena-resource-observability.md)
records the three returns that justify non-observability — semantic
sufficiency (`equal` is complete; no `eq` is needed), compiler
freedom, and determinism/portability — and why the debugging channel
observes the implementation from outside program semantics. The
[resolved inquiry](../../40-inquiries/what-may-programs-observe-of-resources.md)
and [topic map](../../10-maps/resource-observability.md) preserve the
decision route.
