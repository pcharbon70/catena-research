---
title: "How Does Selective Receive Complete?"
kind: inquiry
created: "2026-09-01"
status: resolved
tags:
  - catena
  - receive
  - processes
  - language-design
aliases:
  - "P086 selective receive inquiry"
---

# How Does Selective Receive Complete?

## Purpose

P086 asks the checklist question: "Connect public syntax, effect
and protocol typing, timeouts, mailbox scan order, starvation,
cancellation, and cost explanations in one normative rule."
C003's typed lowering harness already fixed the core (one closed
message type, portable inlined conditions, rejected messages
preserved, one-time removal, `CND006`), C044 reserved the
public-receive contract, and the kernel `Selective` process
provides standing executable evidence. Two of the seven
connections are blocked by ownership: public syntax belongs to
P109's frozen-frontends reality and timeouts to G088. The
completion is therefore a rule set plus routed interfaces.

## Operational definitions

- **Selective receive** — a receive whose clauses may reject
  candidate messages, which remain queued, until one selects.
- **Routed interface** — a stated obligation a named owning gap
  must discharge when its slice arrives.
- **Rejected prefix** — the queued messages a receive attempt
  scans and rejects before its selection (or exhaustion).

## Hypotheses

1. A new area `selective-receive` at `0.1.46` (code `SR`) carries
   the completion as a rule-set-and-interfaces slice.
   *(Recommended: the comprehension precedent.)*
2. **The fixed rule set**: FIFO scan from the oldest message;
   rejected messages preserved, scanning continues; selected
   message removed exactly once before its body runs; one explicit
   closed message type with no free or rigid variables; the
   receive form performs no effects (bodies carry their own rows);
   conditions restricted to the portable native set (C003
   unchanged, `CND006` included); and **starvation stated
   honestly** — a receive whose clauses reject a prefix starves
   while that prefix stands, scan cost is proportional to the
   rejected prefix per attempt, no fairness guarantee beyond FIFO
   scan order.
3. **The routed interfaces**: public syntax → P109 (semantic
   contract now, tokens at adoption, with the timeout clause named
   as C044's explicit total fallback); timeouts and cancellation →
   G088 (evaluation order, races, and the fallback obligation
   stated as G088's to discharge); protocol typing → G087;
   send-side message semantics → G085.
4. **The preservation witness**: a process sent `Some 0` then
   `Some 1` whose guarded receive (`message > 0`) selects `Some 1`
   while `Some 0` remains queued, asserted through the stepper's
   exposed mailboxes with the BEAM twin agreeing on the selected
   value — plus `CND006`, the closed-type requirement, and the
   C010 fixture re-pinned.

## Paths explored

- **Full feature including timeout syntax now** — rejected: the
  frozen frontends have no timeout form and G088 owns time.
- **Defer to the process era** — rejected: leaves the seven
  connections unstated while G085/G087/G088 are designed against
  an unspecified receive rule.
- **Fairness or bounded-starvation guarantee** — rejected: nothing
  in the corpus or BEAM supports one.
- **Re-pin only, no new witness** — rejected: rejected-message
  preservation is P086's central claim and deserves its own
  witness.

## Findings

All four hypotheses held; the developer chose the recommended
option on all four forks (no overrides). The decisive corpus
facts: C003's harness already carries the semantics; C044's
reservation supplies the public-receive contract this slice
consumes; and C042's cost-honesty precedent fits the starvation
statement exactly.

## Outcome

Resolved as C086 at revision `0.1.46`: the contract will live in
`60-specification/selective-receive/`, the reasoning in
[Catena Selective Receive](../20-notes/catena-selective-receive.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G085, G087,
G088, and P109 own their routed interfaces; Section 9 advances to
5/8.
