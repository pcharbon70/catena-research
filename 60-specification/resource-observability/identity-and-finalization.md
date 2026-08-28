---
title: "Identity and Finalization"
kind: specification
created: "2026-08-26"
status: normative
spec_version: "0.1.33"
tags:
  - observability
  - identity
  - finalization
  - specification
aliases:
  - "Catena identity rule"
---

# Identity and Finalization

## Status and authority

This chapter is the normative Catena 0.1.33 identity and finalization
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the identity rules of
[Actors, Messages, and Failures](../formal-semantic-kernel/actors-messages-and-failures.md),
and closes the deferrals of
[Closures and Tail Calls](../functions-and-calls/closures-and-tail-calls.md)
and [The Comparable Set](../equality-and-ordering/the-comparable-set.md).

The rules apply only to source-language revision `0.1.33`.

## The two-clause identity rule

> **Normative definition.**

1. **Process identity is the only identity-bearing value.** Each
   spawn allocates one fresh identity; a handle observes it through
   exactly the operations the kernel fixes (`send`, and `self`
   returning the current handle), its spelling follows the kernel's
   opaque-presentation rule
   ([Actors, Messages, and Failures](../formal-semantic-kernel/actors-messages-and-failures.md#opaque-process-identity)),
   and it is **never comparable**
   (`RO-OBL-004`) — C035's exclusion is permanent contract.
2. **Every other value has semantic identity only.** Equal values are
   interchangeable; closure allocation identity, record sharing, and
   message copying are unobservable (`RO-OBL-005`). Two closures from
   two evaluations of the same `fn` are as equal as their behaviors;
   two separately constructed equal records are one value twice.

Clause 2 closes the deferrals: C032's "allocation identity is G037's
exclusion" and C029's uniform-first-classness exclusions resolve as
statements about semantic identity, and no debugging demand can reopen
them inside the language (below).

## Finalization

> **Normative definition.**

No destructor, finalizer, at-exit hook, or cleanup form exists at
0.1.33, and none may arrive except through a slice that ships its own
finalization semantics — the resource-scope era (G080s/G084) or the
foreign boundary (G095) (`RO-OBL-006`). Resource release before 0.1.33
is unobservable by construction: GC is invisible, handles release
nothing programs can see, and a trap's mailbox discard (C036) is a
failure side effect, not finalization.

## The debugging channel (non-normative)

The non-observability rules constrain what **programs** may observe.
Tools — debuggers, tracers, profilers — observe the **implementation**
from outside program semantics and are not bound by observational
equivalence: they may inspect real addresses, stack frames, and
closures precisely because the language never promises programs that
view. The language supplies the deterministic anchors such tools
consume: external-harness return and trap recording (C010/C036),
effect-request traces (C030), and process identities and traces
(C010). G124 owns the tooling; nothing it builds needs in-language
observability, and any future in-language identity (interning,
memoization) arrives as its own gated slice, never as an `equal`
amendment (`RO-OBL-008`).

## Deliberately separate work

G080s/G084 resource scopes and cleanup; G085 copy mechanics; G095
foreign finalization; G124 tools.

## Rationale and evidence (non-normative)

The [observability synthesis](../../20-notes/catena-resource-observability.md)
records why identity survives exactly where meaning requires it
(message routing) and why the debugging channel is relocation rather
than sacrifice. The [topic map](../../10-maps/resource-observability.md)
routes the decision.
