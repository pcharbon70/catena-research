---
title: "Deadlines, Waits and Cancellation"
kind: specification
created: "2026-09-08"
status: normative
spec_version: "0.1.53"
tags:
  - specification
  - actors
aliases: []
---

# Deadlines, Waits and Cancellation

## Status and authority

This chapter defines C088 at exact `0.1.53`, edition `0.1`, without previews.
The [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation-limit policy](../../IMPLEMENTATION-LIMITS.md) apply.

It extends the [owned lifetime target](../process-lifetimes/owned-tasks-and-managed-relationships.md#status-and-authority)
with local deadlines, relative sleep, absolute waiting and total timed receive.
For this exact target it fills the earlier
[receive timeout reservation](../selective-receive/the-routed-interfaces.md#timeouts-and-cancellation-g088)
and replaces the lifetime target's exclusion of general time. Earlier exact
targets keep their admission boundaries. No source keywords, final time-library
names, old interfaces or signed formats are changed (`TM-OBL-001`).

## Durations and local origins

A duration is an exact nonnegative integer count of nanoseconds. Its value is
not a floating approximation or wall-clock timestamp. A statically non-integer
expression is invalid; a negative runtime integer produces the terminal
`invalid_duration` trap. No wrapping or silent clamping is permitted.
Arithmetic retains the standing exact-integer domain and runtime-capacity
classification (`TM-OBL-002`).

Native waits round the remaining duration upward to whole milliseconds. An
individual BEAM wait is at most 4,294,967,295 milliseconds; larger allowances
use successive finite intervals against the original deadline. This native
interval is not a maximum language duration. Interval renewal never resets the
budget. Monotonic deadlines are local to one runtime; wall-clock adjustment
cannot change their meaning (`TM-OBL-002`, `TM-OBL-008`).

A deadline is an opaque value associated with a live owned scope. Creation
checks that scope and evaluates its duration once, then records the local
monotonic instant plus the duration. A deadline's type includes its scope
identity; the runtime value also carries the owning scope's dynamic origin.
The absolute host integer is not exposed as a portable language timestamp.

Deadline handles cannot escape their scope, enter a closure, cross a message
boundary or acquire meaning in another runtime. A foreign owner, expired scope
or invalid origin produces a terminal origin violation before waiting. Reusing
a valid deadline preserves the original instant and budget (`TM-OBL-004`).

## Relative and absolute waiting

Relative sleep requires an explicit live owned scope. Its duration is evaluated
once and its deadline is based on the instant that the wait is established.
Absolute waiting validates its supplied deadline and uses that deadline's
existing instant. A zero or already expired wait is immediately eligible for
completion, subject to the cancellation boundary below (`TM-OBL-002`,
`TM-OBL-004`, `TM-OBL-005`).

The reference uses explicit nondecreasing virtual nanosecond time. Reversing
the clock is invalid. No transition can expire before its own deadline.
Reference evaluator fuel, scheduler reductions and host wall time are not this
clock. A deadline grants eligibility, not a realtime scheduling guarantee.
Repeated waits against an expired deadline do not allocate a new positive
allowance (`TM-OBL-002`, `TM-OBL-004`).

Sleep consumes no user message. Completion and cancellation leave unrelated
messages in their original order. Native timeout implementation introduces no
ordinary timer reply into the user's mailbox (`TM-OBL-008`).

## Timed selective receive

Timed receive is admitted in managed process entries. It has ordinary checked
receive clauses and a fallback with the same result type, allowing a terminal
bottom branch. Relative form supplies a duration expression; absolute form
supplies a local deadline expression. The ordinary mailbox, sendability,
pattern and guard rules still apply (`TM-OBL-001`, `TM-OBL-003`).

The relative duration or absolute deadline expression is evaluated exactly
once, before scanning candidate messages. Its validation also precedes the
scan. A queued match cannot suppress a negative-duration trap. A rejected
candidate or a renewed native wait interval does not repeat that expression
or its effects (`TM-OBL-003`).

The receiver scans queued candidates using ordinary oldest-match and clause
ordering. Rejected messages remain in the mailbox. Even at zero duration or
an already expired absolute deadline, a queued matching candidate is eligible
before fallback selection. If no candidate matches and the deadline is due,
fallback is selected. Otherwise the receiver suspends until another eligible
message, deadline or control event permits progress (`TM-OBL-003`,
`TM-OBL-006`).

Selection commits one message branch or fallback. A late reply cannot replace
a selected fallback, and timeout cannot also select fallback after a message
branch has won. Fallback preserves every unselected message. Neither form
implements receive by consuming and reinserting rejected user messages.
Unread messages are disposed only when ordinary process termination requires
it (`TM-OBL-003`, `TM-OBL-006`, `TM-OBL-008`).

## Cancellation and completion choices

Cancellation follows explicit owned scopes. It is not an ambient ability to
interrupt retained pure evaluation. The
[lifetime ownership and outcome rules](../process-lifetimes/owned-tasks-and-managed-relationships.md#structured-lifetime-transitions)
continue to govern child registration, sibling cancellation and joining.

Admitted safe points include function/recursive entry, generated continuation
entry and blocking lifetime/receive boundaries. The time target checks again
after a completed wait before proceeding through its continuation. A request
is not an instruction-level interruption. A process with no admitted owned
context gains no ambient cancellation source (`TM-OBL-005`).

A pending eligible control event can terminate a wait before a message or
fallback branch is selected. After branch selection, cancellation can still
interrupt subsequent computation at the next safe point; it cannot select a
second receive branch or revive an earlier wait. Message, deadline and control
races follow actual eligible transition order, not wall-clock arrival
comparisons or a retroactive cancellation preference (`TM-OBL-005`,
`TM-OBL-006`).

Managed linked failure selected before worker publication remains the primary
managed outcome when that worker subsequently returns normally. A terminal
trap retains its precedence. A worker that has already published completion
cannot be completed again by a later signal (`TM-OBL-006`).

An explicit owned scope inside an otherwise raw actor also observes its own
child failure while blocked in receive. This adds no relationship to raw spawn
itself. Private control clauses require the live scope or worker token and
remain separate from legal user payloads. Nested receives have distinct private
bindings, so entering a new scope cannot reuse an outer scope's stale context
(`TM-OBL-005`, `TM-OBL-008`).

## Masking, expiry and foreign boundaries

The [resource release contract](../resource-scopes/owned-lifetime-and-mandatory-cleanup.md#local-cancellation-exit-and-deadlines)
continues to mask cooperative cancellation during mandatory bounded release.
Repeated requests cannot run a release twice, interrupt it as ordinary
cancellation, or hide a mandatory release-expiry trap. Remaining registered
releases retain their required ordering (`TM-OBL-007`).

Task shutdown expiry and release expiry have distinct owners and deadlines.
A shutdown bound can force process loss while cleanup is incomplete; that
outcome does not claim successful release. Completion already selected cannot
be replaced by later expiry. Expiry already selected cannot be reversed by a
late worker reply (`TM-OBL-006`, `TM-OBL-007`).

Noncooperative foreign work, external process kill and VM loss have no prompt
cancellation or successful-unwind promise. The selected language target admits
no foreign frame adapter or process-affine foreign ownership. Host obstruction
witnesses exercise the named forced-shutdown boundary, not a claim that an
arbitrary foreign function is safely interruptible (`TM-OBL-007`).

## Diagnostics, artifacts and conformance

Wrong exact target selection uses `EDN001`; invalid duration type, deadline
scope or escape uses `T002`; invalid receive context uses `PRC003`.
Inconsistent typed evidence uses `I001`; an open artifact entry uses `EFX003`.
Runtime invalid duration and deadline origin are terminal traps. Standing
finite-resource refusals retain their separate limit categories.

The production backend independently verifies the core, applies source and
generated-code arity limits, and requires a closed zero-argument main. It emits
a deterministic `0.1.53` BEAM artifact with `time-tree-0.1.53` frontend identity.
It produces no interface and widens no old signed format (`TM-OBL-001`).

| Obligation | Required evidence |
| --- | --- |
| TM-OBL-001 | Exact target, independent evidence checking, deterministic artifact and earlier boundary rejection |
| TM-OBL-002 | Exact nonnegative units, large values, upward host conversion and virtual eligibility |
| TM-OBL-003 | Once-before-scan evaluation, zero-time queued match, total fallback and skipped-message preservation |
| TM-OBL-004 | Opaque local deadline origin, no escape and one budget across repeated waits |
| TM-OBL-005 | Owned cancellation during blocking work and at post-wait safe points without ambient raw ownership |
| TM-OBL-006 | One branch/completion winner across reply, deadline, failure and cancellation schedules |
| TM-OBL-007 | Bounded masked cleanup and explicit forced-loss/noncooperative exclusions |
| TM-OBL-008 | No timer-message leak, no rejected-message removal and distinct nested private receive contexts |

## Variability and limits

This area introduces no configurable implementation choice,
presentation allowance or implementation-limit dimension. Durations and graces
are explicit input. Eligible scheduler and deadline races are defined
nondeterminism. Standing runtime capacity, reference fuel and exploration
budgets keep their classifications. The fixed maximum native interval does not
limit the exact language duration domain.

## Lifecycle

The lifecycle record is `change-0-1-53-cancellation-and-time`, predecessor
`0.1.52`, a compatible addition affecting source acceptance, static meaning,
dynamic behavior and artifacts. The new target fills earlier time reservations
only in its explicit compound input. Supervision, distributed clocks and
foreign-call admission remain separate work.

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-08-cancellation-and-time.md)
records choices, witnesses and the publication gate. The
[G088 plan](../../20-notes/language-completion-plan-semantics.md#item-088-cancellation-and-time-g088)
provides the decision baseline. Pinned
[OTP process research](../../30-sources/erlang-otp-29-processes.md) and
[time/process BIF research](../../30-sources/erlang-otp-29-time-and-process-bifs.md)
support the native mapping. Catena's typed ownership, branch selection and
cancellation rules are local language decisions, not guarantees inferred from
those sources alone.
