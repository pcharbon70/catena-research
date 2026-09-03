---
title: "Selective Receive"
kind: map
created: "2026-09-01"
tags:
  - archive-navigation
  - receive
  - processes
  - catena
aliases:
  - "P086 selective receive route"
---

# Selective Receive

## Purpose

This map routes the P086 question — connecting public syntax,
typing, timeouts, scan order, starvation, cancellation, and cost
for selective receive — through the archive's decision trail. The
normative answer is revision `0.1.46` in the [Selective Receive
Specification](../60-specification/selective-receive/README.md).

## The route

1. **The harness that carried the semantics.** [Clause Contexts
   and Receive](../60-specification/clause-conditions/clause-contexts-and-receive.md)
   fixes C003's typed lowering harness — rejected messages
   preserved, one-time removal, `CND006`, the native-only rule —
   whose "explicitly unresolved" list P086 answers.
2. **The public-receive reservation.** [Context Rules and
   Reservations](../60-specification/pattern-contexts/context-rules-and-reservations.md)
   (C044) requires every public receive to be exhaustive or carry
   an explicit total fallback — the contract this slice consumes
   by naming the timeout clause as that fallback.
3. **The running evidence.** The C010 kernel fixture's
   `Selective` process and [Kernel
   Metatheory](../60-specification/formal-semantic-kernel/metatheory.md)
   mailbox preservation stand as the execution and theorem sides.
4. **The cost-honesty precedent.** [The Complexity
   Exclusion](../60-specification/collection-construction-and-update/miss-as-value-and-complexity.md)
   (C042) fixes how starvation and scan cost may be stated:
   explanation, not asymptotic promise.
5. **The contract.** The [Selective Receive
   Specification](../60-specification/selective-receive/README.md):
   the rule set, the four routed interfaces (P109, G088, G087,
   G085), and conformance.
6. **The reasoning and decision record.** [Catena Selective
   Receive](../20-notes/catena-selective-receive.md) argues the
   routing; the [resolved
   inquiry](../40-inquiries/how-does-selective-receive-complete.md)
   preserves the forks.

## Related maps

- [Clause Guards map](clause-guards.md) — the condition fragment
  receive reuses.
- [Runtime Failure Taxonomy map](runtime-failure-taxonomy.md) —
  the process-failure side G088 will connect.
