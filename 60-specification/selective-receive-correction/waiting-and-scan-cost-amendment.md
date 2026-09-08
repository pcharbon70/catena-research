---
title: "Selective Receive Waiting and Scan Cost Amendment"
kind: specification
created: "2026-09-08"
status: normative
spec_version: "0.1.49"
tags: [receive, processes, specification, conformance]
aliases: []
---

# Selective Receive Waiting and Scan Cost Amendment

## Status and authority

This normative amendment is governed by [Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
Under [C008 compatibility](../editions-and-feature-lifecycle/feature-lifecycle-and-compatibility.md#compatibility-dimensions),
it introduces the stable `selective-receive-correction` feature at exact
revision `0.1.49` in edition `0.1`.

For selection `0.1.49`, this chapter explicitly replaces
[Starvation and cost](../selective-receive/the-receive-rule-set.md#starvation-and-cost) and
`RC-OBL-004` from the exact `0.1.46` contract. It adopts the remaining
[receive rules](../selective-receive/the-receive-rule-set.md#the-rules),
[no hidden semantics](../selective-receive/the-receive-rule-set.md#no-hidden-semantics),
[routed interfaces](../selective-receive/the-routed-interfaces.md), and
[diagnostic obligations](../selective-receive/diagnostics-and-conformance.md#stable-diagnostics)
unchanged for the amended contract. Later same-edition selections inherit
this correction under C008 unless explicitly replaced. Historical selections
and persisted artifacts are not reinterpreted; the original `0.1.46` text
remains available, including its disputed statement.

## Waiting and selection

A rejected prefix does not prevent selecting a later matching message.
The receive selects the oldest message for which a clause succeeds, removes
that message exactly once before its body runs, and preserves every other
message in its original relative order (`RC-OBL-002`, `RC-OBL-004`).

When no queued message matches, including an empty mailbox, the receive
suspends without consuming any message. A subsequent matching arrival
makes selection possible; this is not a guarantee that the scheduler runs
the process within a particular time (`RC-OBL-004`).

A message that never matches can remain queued indefinitely while other
messages are selected. This message starvation is distinct from suspension
of the whole receive. Repeated receives obey oldest-matching selection each
time; they do not repeatedly select a previously removed message. No
scheduler fairness, bounded waiting time or timeout semantics are introduced.

## Scan work

The [C010 abstract cost](../formal-semantic-kernel/actors-messages-and-failures.md#selective-receive)
counts the candidates and clauses actually examined. A longer examined
rejected prefix adds abstract scan work. There is no requirement to rescan
every previously rejected message on every runtime wakeup, and no universal
constant-time, proportional wall-clock or asymptotic bound is introduced
(`RC-OBL-004`).

> **Normative unspecified presentation.**

Internal scan caching and scheduling of scan work are bounded unspecified
presentation choices within the following observational equivalence class. They preserve the selected message, remaining mailbox, clause
effects and every other language-observable outcome required by
[no hidden semantics](../selective-receive/the-receive-rule-set.md#no-hidden-semantics).
They do not establish a portable runtime wakeup or rescan count.

This chapter adds no implementation limit or diagnostic family.

## Lifecycle and migration

The lifecycle change `change-0-1-49-selective-receive-correction` has predecessor
`0.1.48`, target `0.1.49`, classification `compatible-correction`, and affected
dimension `static-meaning`. It repairs an inconsistent language claim to agree
with retained C003/C010 selection; it changes no accepted source, executable
kernel representation or runtime receive implementation (`RC-OBL-001`).

To adopt the correction, select `0.1.49` for the language contract. Existing
C010 executable witnesses continue to select exactly `0.1.8`; they provide
evidence for the corrected rule without becoming a new frontend. The
source-text decoder additionally accepts `0.1.49`. JSON, kernel, interface,
artifact and signed-format version lists remain unchanged. No automatic
source rewrite, new vocabulary, public receive API or final grammar is added.

## Conformance obligations

For the amended contract, `RC-OBL-001` requires exact revision/lifecycle
registration and unchanged persisted format boundaries. `RC-OBL-004` requires
no-match suspension, rejected-prefix bypass, honest examined-candidate cost
and absence of fairness promises. The other `RC-OBL-*` obligations remain as
adopted above.

Required witnesses on both the reference evaluator and BEAM are: empty and
wholly rejected mailboxes waiting with unchanged contents; two successive
receives selecting the oldest matching messages behind a rejected prefix;
and exact preservation of the remaining mailbox after one-time removals.
The selection witness records both selected values, not only termination.
An arrival trace alone is not evidence of clause selection. A test timeout
alone is not evidence of semantic suspension.

## Rationale and evidence (non-normative)

The [completion plan](../../20-notes/language-completion-plan-semantics.md)
compared four alternatives for each of the amendment, versioning, evidence,
and cost decisions. The [implementation journal](../../50-journal/2026-09-08-capability-kernel-integration.md)
records executable witnesses and validation. The [inquiry](../../40-inquiries/how-does-selective-receive-complete.md)
preserves why the old completion claim was reopened.
