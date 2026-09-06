---
title: "Catena Selective Receive"
kind: note
created: "2026-09-01"
maturity: developing
tags:
  - catena
  - receive
  - processes
  - language-design
aliases:
  - "the selective receive rule set"
---

# Catena Selective Receive

## Executive conclusion

Selective receive was promoted at `0.1.46` as a fixed rule set plus four
routed interfaces. P086 is now reopened because the normative starvation
statement conflicts with the scan-continuation rule. The delivered rules —
FIFO scan from the oldest message,
rejected messages preserved, one-time removal, one closed message
type, an effect-free receive form, portable conditions only —
already ran in C003's harness; `0.1.46` states them as the
language-level contract and routes what cannot be fixed
today: public syntax to P109, timeouts and cancellation to G088
(with the timeout clause named as C044's explicit total fallback),
protocol typing to P087, send-side semantics to P085. The
existing evidence distinguishes selection beyond a rejected prefix from
waiting when every queued message is rejected. It does not establish the
claim that any rejected prefix starves the receive.

## Scope, method, and definitions

This note preserves the archive's reasoning for the historical 0.1.46
promotion and the completion audit that reopened P086. It reads C003's
receive harness chapter, C044's
public-receive reservation, C010's mailbox preservation and
`Selective` process fixture, and C042's cost-honesty precedent;
it invents no syntax.

- **Rejected prefix** — the queued messages a receive attempt
  scans and rejects before selecting (or exhausting) — the unit
  the cost statement prices.

## Reopened starvation boundary

The normative [Rules](../60-specification/selective-receive/the-receive-rule-set.md#the-rules)
require scanning to continue after a rejected message. The same chapter's
[Starvation and Cost](../60-specification/selective-receive/the-receive-rule-set.md#starvation-and-cost)
instead says that a receive rejecting a prefix starves while that prefix
stands (`RC-OBL-004`). A prefix alone does not establish the absence of a
later matching message. C010's [Selective
Receive](../60-specification/formal-semantic-kernel/actors-messages-and-failures.md#selective-receive)
defines waiting when no message is accepted.

The [promotion journal](../50-journal/2026-09-01-c086-receive.md#observations)
records two distinct observations: the C010 fixture selects `Some 1` after
rejecting `Some 0`, and a blocked holder retains both messages when its
guard rejects both. The second observation cannot justify starvation for
every rejected prefix. The [completion
audit](../50-journal/2026-09-06-checklist-completion-audit.md) records the
current discrepancy without replacing normative language through observed
compiler behavior.

Under [Conflict Resolution](../SPECIFICATION-AUTHORITY.md#conflict-resolution),
the disputed conformance claim remains blocked. Closure requires an explicit
normative resolution distinguishing skipped messages, a receive with no
acceptable message, and scheduler fairness, followed by aligned evidence and
conformance reporting. The existing specification version and historical
promotion remain recorded; this note does not amend their rules.

## What was already true

C003's harness carried the semantics: rejected messages remain
and scanning continues per BEAM selective semantics; selection
removes exactly once; the closed message type and portable
condition set are enforced; or-patterns reject as `CND006` because
the native backend cannot guarantee shared one-time condition
evaluation. C010's fixture made it run, and mailbox preservation
stands as metatheory. What was missing was the language-level
statement and the interfaces the neighboring gaps design against. The audit
found that the added starvation wording did not consistently preserve the
scan rule.

## Why routing rather than resolving

Public syntax cannot ship (the frozen frontends), timeouts belong
to G088's time-and-cancellation program, protocols to P087, and
the send side to P085. Declaring those interfaces now is what
the historical slice attempted: state the receive rule set and every
neighbor's obligation where their designs will meet it. Those interfaces
remain useful while the starvation wording is unresolved. The timeout clause
deserves its emphasis:
it is not merely a G088 feature but the explicit total fallback
C044's reservation requires of every public receive.

## Tradeoffs, limitations, falsification

Scan order and preservation have delivered rules and witnesses. The disputed
starvation statement must not be treated as an established guarantee or as
a demonstrated property. Timeout and cancellation races remain G088's;
scheduler fairness belongs to the scheduling contract. Counterexamples to
the delivered scan rules include consuming a rejected message, removing a
selected message twice, or stopping at a rejected prefix despite a later
acceptable message. Cost evidence must distinguish messages and clauses
examined from any stronger asymptotic or fairness promise.

## Route to sources

- The [Selective Receive Specification](../60-specification/selective-receive/README.md)
  contains the delivered `0.1.46` rules and disputed starvation statement.
- [Clause Contexts and Receive](../60-specification/clause-conditions/clause-contexts-and-receive.md)
  — C003's harness this slice elevates.
- [Context Rules and Reservations](../60-specification/pattern-contexts/context-rules-and-reservations.md)
  — C044's public-receive reservation.
- [The Complexity Exclusion](../60-specification/collection-construction-and-update/miss-as-value-and-complexity.md)
  — the cost-honesty precedent.
- The [reopened inquiry](../40-inquiries/how-does-selective-receive-complete.md)
  preserves the decision route and the remaining closure criteria.
