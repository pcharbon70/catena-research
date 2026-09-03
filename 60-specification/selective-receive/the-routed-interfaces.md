---
title: "The Routed Interfaces"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.46"
tags:
  - receive
  - processes
  - specification
aliases:
  - "Catena receive interfaces"
---

# The Routed Interfaces

## Status and authority

This chapter is the normative Catena 0.1.46 receive interface
rule set. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the public-receive reservation of
[Context Rules and Reservations](../pattern-contexts/context-rules-and-reservations.md)
(C044) and states the obligations the neighboring gaps discharge
when their slices arrive.

The rules apply only to source-language revision `0.1.46`.

## Public syntax — P109

> **Normative definition.**

No frozen frontend carries a public receive expression; the rule
set of [The Receive Rule Set](the-receive-rule-set.md) is the
semantic contract the adopting grammar realizes (`RC-OBL-005`).
When P109 adopts the tokens, the public form MUST satisfy C044's
reservation: exhaustive over its closed message type or carrying
an **explicit total fallback** — and the **timeout clause, when
G088 ships it, is that fallback** (`RC-OBL-005`).

## Timeouts and cancellation — G088

> **Normative definition.**

G088's slice owns timeout evaluation and races, deadlines, and
cancellation, and MUST state, for the receive form (`RC-OBL-006`):
when the timeout expression is evaluated relative to the scan;
what a racing message-timeout interleaving may observe; that the
timeout clause is total; and how cancellation of a waiting receive
disposes of nothing it did not enqueue. Until G088 ships, no
timeout form exists and none is claimed.

## Typed protocols — G087

> **Normative definition.**

G087 owns whether mailbox protocols, process handles, and replies
are statically tracked (`RC-OBL-007`). Any protocol typing MUST
compose with the closed-message-type rule: a protocol state refines
the message type; it never widens scan, preservation, or removal.

## Send-side semantics — G085

> **Normative definition.**

G085 owns send results, copying and sharing, and dead-target
behavior (`RC-OBL-007`). The receive rule set assumes only what
C010 fixed: a live mailbox preserves order and content for its
process; every other send-side claim is G085's to make.

## Rationale and evidence (non-normative)

The [synthesis](../../20-notes/catena-selective-receive.md)
argues that declaring interfaces now is what an honest "one
normative rule" means when two of the seven connections are
blocked by ownership — the same posture the comprehension
contract took toward its adopting grammar.
