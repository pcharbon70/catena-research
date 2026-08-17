---
title: "Erlang/OTP 29 Runtime Resource Controls"
kind: source
created: "2026-08-17"
authors:
  - "Ericsson AB"
published: "OTP 29"
citation_key: "erlangOtp2026runtimeResourceControls"
container: "Erlang/OTP ERTS Reference Manual"
edition: "29.0.4"
isbn: null
doi: null
url: "https://www.erlang.org/doc/apps/erts/erlang.html"
accessed: "2026-08-17"
tags:
  - actors
  - beam-vm
  - erlang
aliases:
  - "OTP 29 process resource controls"
---

# Erlang/OTP 29 Runtime Resource Controls

## Reference

Ericsson AB. “`erlang`.” *Erlang/OTP ERTS Reference Manual*, OTP 29.0.4.
[Canonical module documentation](https://www.erlang.org/doc/apps/erts/erlang.html),
with supporting [`erl` emulator flags](https://www.erlang.org/doc/apps/erts/erl_cmd.html),
accessed 2026-08-17.

## Research question

Can Catena promise a portable mailbox size, and how should runtime heap and
message-queue controls relate to language-level delivery and ordering rules?

## Findings

ERTS exposes per-process and system defaults for maximum heap size. The size is
measured in words at garbage collection and can include process stacks,
messages held on the heap, and collector working memory. A deployment can kill
a process at the threshold or merely report it, and can include or exclude
shared off-heap binaries from the calculation.

`message_queue_data` independently selects on-heap or off-heap message storage.
The documentation recommends off-heap storage for processes that can accumulate
many messages because scanning and collecting a large on-heap queue can be
expensive. The emulator also exposes distribution-buffer limits whose
exhaustion can suspend senders. These are interacting memory, collection, and
transport policies rather than one stable count of messages accepted by every
mailbox.

## Relevance

The evidence argues against inventing a numeric Catena mailbox floor in C012.
The [root policy](../IMPLEMENTATION-LIMITS.md#runtime-and-mailbox-capacity)
instead classifies mailbox capacity as deployment-defined while preserving the
language's per-sender ordering and targeting observations. Concrete quotas,
process death, supervision, and backpressure remain with G068 and G129.

## Limits

ERTS controls do not by themselves define Catena's message-delivery contract.
Heap checks occur at garbage collection rather than at a fixed message count,
messages differ in size and sharing, and node or operating-system termination
can occur outside the language model. Distribution and priority messages also
extend beyond the current local C010 actor kernel.

## Derived work

- [Catena Implementation Limits and Portability](../20-notes/catena-implementation-limits-and-portability.md)
- [Implementation Limits and Portability map](../10-maps/implementation-limits-and-portability.md)
- [C012 Implementation Limits](../50-journal/2026-08-17-c012-implementation-limits.md)
