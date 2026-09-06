---
title: "How Does Selective Receive Complete?"
kind: inquiry
created: "2026-09-01"
status: open
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
historical completion was therefore a rule set plus routed interfaces.
The [2026-09-06 completion
audit](../50-journal/2026-09-06-checklist-completion-audit.md) reopens P086
because `RC-OBL-004` states starvation for any rejected prefix while the
same normative chapter requires scanning to continue to a later match.

## Operational definitions

- **Selective receive** — a receive whose clauses may reject
  candidate messages, which remain queued, until one selects.
- **Routed interface** — a stated obligation a named owning gap
  must discharge when its slice arrives.
- **Rejected prefix** — the queued messages a receive attempt
  scans and rejects before its selection (or exhaustion).

## Historical hypotheses and decisions

The following records the forks posed for the 0.1.46 slice. The starvation
claim in hypothesis 2 is retained as provenance, not as a current finding.

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
   stated as G088's to discharge); protocol typing → P087;
   send-side message semantics → P085.
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
  connections unstated while P085/P087/G088 are designed against
  an unspecified receive rule.
- **Fairness or bounded-starvation guarantee** — rejected: nothing
  in the corpus or BEAM supports one.
- **Re-pin only, no new witness** — rejected: rejected-message
  preservation is P086's central claim and deserves its own
  witness.

## Findings

The developer chose the recommended option on all four historical forks
(no overrides). C003's harness carries the scan and preservation semantics;
C044 supplies the public-receive reservation; C042 distinguishes a cost
explanation from an asymptotic promise. These facts supported the original
promotion but do not establish hypothesis 2's starvation claim.

The normative [Rules](../60-specification/selective-receive/the-receive-rule-set.md#the-rules)
require a rejected message to remain in place while scanning continues.
[Starvation and Cost](../60-specification/selective-receive/the-receive-rule-set.md#starvation-and-cost)
says a receive rejecting a prefix starves while the prefix stands. C010's
[Selective Receive](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#selective-receive)
instead makes the receive wait when no message is accepted.

The [promotion journal](../50-journal/2026-09-01-c086-receive.md#observations)
records selection of `Some 1` beyond rejected `Some 0`, separately from a
blocked holder whose guard rejects both messages. The latter establishes
waiting and retention when no message matches; it cannot establish that a
rejected prefix blocks later eligible messages. Under [Conflict
Resolution](../SPECIFICATION-AUTHORITY.md#conflict-resolution), neither test
behavior nor this inquiry resolves the normative discrepancy.

## Closure criteria

1. Explicitly resolve the normative starvation statement against the scan
   rule, distinguishing indefinitely retained rejected messages, waiting
   when no message matches, and scheduler fairness.
2. Align the conformance obligation and its evidence with that resolution.
   Retain witnesses for selecting a later matching message beyond a rejected
   prefix, preserving rejected messages in order, and waiting when no
   queued message matches; do not infer fairness from bounded examples.
3. Update the connected specification, explanations, traceability, and any
   affected compiler evidence through the [repair
   workflow](../SPECIFICATION-AUTHORITY.md#repair-and-promotion-workflow),
   then validate before restoring the completion claim.

## Outcome

Historically promoted as C086 at revision `0.1.46`; reopened as P086 by the
2026-09-06 audit. The contract lives in the
[Selective Receive Specification](../60-specification/selective-receive/README.md),
the reasoning in
[Catena Selective Receive](../20-notes/catena-selective-receive.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). P085, P087,
G088, and P109 retain their routed interfaces. Completion remains open and
conformance for the disputed starvation rule is not claimed.
