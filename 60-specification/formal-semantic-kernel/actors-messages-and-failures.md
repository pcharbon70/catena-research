---
title: "Actors, Messages, and Failures"
kind: specification
created: "2026-08-06"
status: normative
spec_version: "0.1.8"
tags:
  - concurrency
  - failure-semantics
  - specification
aliases:
  - "Catena typed process calculus"
---

# Actors, Messages, and Failures

## Global configuration

A running kernel program is a global configuration containing a finite map of
logical process identities to local expressions, typed mailboxes, and status;
the next fresh identity; and an observation trace.

> **Normative definition.**

```text
G ::= < processes, mailboxes, next, trace >
status ::= running(e) | waiting(receive-clauses) | terminated | trapped(reason)
mailbox ::= [(sender, message)]
label ::= handle | request | resume | effect-return
        | spawn | send | receive | return | trap
```

One global step nondeterministically selects one runnable process and applies
one local step or one process transition. Logical identities in the definition
exist to state freshness and traces; a program cannot inspect their spelling.

## Spawn and self

`spawn P(arguments)` evaluates arguments left to right in the parent. It then
allocates a fresh local process, initializes an empty mailbox of P's declared
type, starts P with the values, and returns its `Process M` handle to the
parent. The child does not inherit lexical handlers or capabilities. Its only
ambient capability is its fresh reserved Process capability.

`self` returns the current handle and has no other observation. A process
handle may be sent as first-order data. No equality, order, conversion,
registration, node query, liveness query, or string representation is a Catena
operation in 0.1.8.

## Send

`send target message` evaluates the target and message, then returns Unit. If
the target is live, the message is appended to its mailbox. If it has already
terminated or trapped, the message is discarded and send still returns Unit.
The operation never reports target liveness.

Messages from one sender to one receiver are enqueued in send order. Messages
from different senders may interleave in any order allowed by the global
steps. The semantic message is an immutable first-order value. Physical copy
or sharing does not change its meaning.

## Selective receive

Receive scans the mailbox from oldest to newest. For each message it tests
clauses in source order. Structural rejection or a false portable condition
leaves that message in its position and continues scanning. The first
accepted message is removed exactly once, its bindings enter the selected
body, and later mailbox order is preserved.

If no message is accepted, the process becomes waiting and takes no local
step until a later send makes a clause acceptable. Receive has no timeout,
after clause, cancellation point, or fallback that consumes and re-enqueues a
message.

The semantic work of one receive attempt is proportional to the messages and
clauses actually examined. No fairness rule prevents an earlier repeatedly
accepted message or scheduler choice from starving other work.

## Completion and trap

A process entry returning Unit terminates normally and discards unread
messages. A process reaching `trap(reason)` terminates abnormally and discards
its mailbox. Neither transition sends an exit message, affects its spawner, or
becomes observable through a Catena handle. The external conformance harness
may record return and trap labels.

When every live process is waiting with no acceptable message, the
configuration is quiescent. Quiescence is a specified suspension, not an
invalid core state and not a promise that later progress occurs.

## Opaque process identity

> **Normative unspecified presentation.**

Process-handle spelling is bounded unspecified presentation. Diagnostic and
conformance tools MAY choose any logical spelling that remains stable within
one run. That spelling cannot affect scheduling, acceptance, message order,
runtime values, effects, trap identity, interface identity, or artifact bytes.

## Deliberately absent process facilities

Links, monitors, exit trapping, completion handles, deadlines, timers,
cancellation, structured tasks, supervision, priorities, remote nodes,
delivery across nodes, partitions, serialization, and code upgrade are not
0.1.8 operations. Their absence cannot be bypassed through a foreign value
because this kernel has no foreign-value boundary.
