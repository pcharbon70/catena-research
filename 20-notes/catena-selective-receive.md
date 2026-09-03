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

Selective receive completes as a fixed rule set plus four routed
interfaces. The rules — FIFO scan from the oldest message,
rejected messages preserved, one-time removal, one closed message
type, an effect-free receive form, portable conditions only —
already ran in C003's harness; `0.1.46` states them as the
language-level contract, adds the honest starvation statement
(scan cost is proportional to the rejected prefix; no fairness
guarantee beyond scan order), and routes what cannot be fixed
today: public syntax to P109, timeouts and cancellation to G088
(with the timeout clause named as C044's explicit total fallback),
protocol typing to G087, send-side semantics to G085. The
centerpiece witness shows the central claim directly: a rejected
message stays queued while a later one selects.

## Scope, method, and definitions

This note synthesizes the archive's evidence for closing P086 at
revision `0.1.46`. It reads C003's receive harness chapter, C044's
public-receive reservation, C010's mailbox preservation and
`Selective` process fixture, and C042's cost-honesty precedent;
it invents no syntax.

- **Rejected prefix** — the queued messages a receive attempt
  scans and rejects before selecting (or exhausting) — the unit
  the cost statement prices.

## What was already true

C003's harness carried the semantics: rejected messages remain
and scanning continues per BEAM selective semantics; selection
removes exactly once; the closed message type and portable
condition set are enforced; or-patterns reject as `CND006` because
the native backend cannot guarantee shared one-time condition
evaluation. C010's fixture made it run, and mailbox preservation
stands as metatheory. What was missing was the language-level
statement — scan order as a rule, starvation as an honest cost
claim, and the interfaces the neighboring gaps design against.

## Why routing rather than resolving

Public syntax cannot ship (the frozen frontends), timeouts belong
to G088's time-and-cancellation program, protocols to G087, and
the send side to G085. Declaring those interfaces now is what
"one normative rule" honestly means: the receive rule set is
complete, and every neighbor's obligation is stated where their
designs will meet it. The timeout clause deserves its emphasis:
it is not merely a G088 feature but the explicit total fallback
C044's reservation requires of every public receive.

## Tradeoffs, limitations, falsification

The rule set fixes scan order and preservation but no fairness,
bounded starvation, or timeout races — those are G088's to state
or refuse. Falsification: a rejected message observed consumed, a
second removal of a selected message, a receive form performing
its own effects, or any scanned-prefix cost charged beyond the
rejected prefix would void the rule set.

## Route to sources

- The Selective Receive Specification (candidate, then normative
  at promotion, in `60-specification/selective-receive/`) will
  define the contract this note argues for.
- [Clause Contexts and Receive](../60-specification/clause-conditions/clause-contexts-and-receive.md)
  — C003's harness this slice elevates.
- [Context Rules and Reservations](../60-specification/pattern-contexts/context-rules-and-reservations.md)
  — C044's public-receive reservation.
- [The Complexity Exclusion](../60-specification/collection-construction-and-update/miss-as-value-and-complexity.md)
  — the cost-honesty precedent.
- The [resolved inquiry](../40-inquiries/how-does-selective-receive-complete.md)
  preserves the decision route.
