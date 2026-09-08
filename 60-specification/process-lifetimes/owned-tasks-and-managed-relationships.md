---
title: "Owned Tasks and Managed Relationships"
kind: specification
created: "2026-09-08"
status: normative
spec_version: "0.1.52"
tags:
  - specification
  - actors
aliases: []
---

# Owned Tasks and Managed Relationships

## Status and authority

This chapter defines C084 at exact `0.1.52`, edition `0.1`, without previews.
The
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation-limit policy](../../IMPLEMENTATION-LIMITS.md) govern it.

This chapter extends the explicit
[resource compound input](../resource-scopes/owned-lifetime-and-mandatory-cleanup.md#compound-input-and-static-semantics).
Retained bare source and exact earlier revisions retain their established
meaning. Public language keywords and standard-library names remain undecided.
Programmatically supplied semantic roles, caller-selected observation labels,
and implementation adapter names are not final source vocabulary.

Raw isolated spawn retains the
[C010 isolation contract](../formal-semantic-kernel/actors-messages-and-failures.md#spawn-and-self).
A raw process is not implicitly owned, linked, supervised or joined. A monitor
observes its target without owning it. A managed link propagates failure
symmetrically. A task scope owns its explicitly registered children. These
relationships are distinct even when one process participates in several.

## Static ownership and capability boundary

An owned task scope binds an opaque scope handle with a structural identity
derived from origin, module, entry role, entry position and scope preorder.
Dynamic entries have fresh tokens. A child handle names exactly one owner and
one dynamic scope. Independent verification rederives static identity.

The initial child callback takes `Unit`, returns `Unit`, and has no residual
latent effect. It can establish explicit local handlers. No parent handler,
resumption, process dictionary or resource authority is inherited. Callback
formation cannot capture a task, monitor or resource handle. The existing
sendability and affine resumption restrictions remain in force.

Scope, child and monitor handles cannot escape their lexical scope, cross a
message boundary or enter a closure. Immutable admitted payloads can be copied
without copying ownership. Child registration completes before the child is
released to run; interruption of registration does not detach a child from its
manager. An invalid, stale or foreign-owner token is a terminal owner violation.

Managed-process handles are distinct from retained raw Process handles and
carry the mailbox type. Managed send requires a matching sendable payload.
Managed spawn selects a checked local process entry with explicit arguments
and finite shutdown grace. The initial target does not import managed entries
through an old interface format. Forged selected-entry evidence rejects.

Self-linking is invalid. Managed identity, linking, unlinking and trapping observations require a
managed process entry. Raw spawn cannot enter a body requiring that context.
Each function that observes linked exits establishes its own trapping region;
a closure does not inherit permission from its creation region.

## Structured lifetime transitions

A scope moves from open to joining to closed. Registration is valid only while
open. Normal body completion waits for every owned child to reach terminal
completion, including its required cleanup. Scope return cannot detach work.
Raw spawns inside admitted code remain independent of this ownership relation.

An observed child failure selects the scope's first observed failure if no
failure has already been selected, requests cancellation of live siblings,
and waits for bounded cleanup. Later child outcomes are secondary evidence.
First observation is schedule-dependent; lexical child order does not decide
which simultaneous failure wins.

Body trap, cancellation, cooperative exit and actual handler abandonment close
owned tasks before returning to the enclosing continuation. Abandonment
preserves the handler result unless mandatory cleanup fails. An original trap
retains its reason; later cleanup failures remain evidence. A child failure
cannot replace an already selected non-normal body outcome.

Resource releases and task joins share dynamic lifetime order. An inner
resource releases before an enclosing task join; an outer resource releases
after that join. Explicit resource cancellation uses this same order. Handler
capture suspends scope frames. Resumption reinstalls them; declining resumption
closes captured lifetimes and restores captured trapping state before the
handler's outer continuation proceeds.

## Monitored completion

Each registration has independent identity, even for the same observer and
target. Registering against an already absent or terminal identity observes
absence. Registering before terminal publication observes that publication.
Each registration supplies at most one terminal observation. Observing one
registration cannot consume another registration's result.

Outcomes form a closed structural variant. The caller supplies distinct valid
labels for the fixed roles: normal completion with `Unit`; integer trap with
its integer reason; integer cancellation with its integer reason; cooperative
exit with `Unit`; absence with `Unit`; bounded runtime failure with `Unit`; and
external loss with `Unit`. Arbitrary host exit terms do not enter this variant.

Managed terminal publication follows worker termination and required cleanup.
External forced loss has no cleanup-success implication. A monitor's private
observer helper belongs to the observer scope. Scope closure cancels that
helper and removes its native monitor, without cancelling or joining the target.
Demonitoring invalidates that registration and any unconsumed private result.
Repeated invalidation does not create another result.

## Linked propagation and trapping

An active link is symmetric and repeated registration while that link remains
active is idempotent. Either endpoint's abnormal terminal publication requests
cooperative termination at the other endpoint, even if only the failing
endpoint explicitly requested a link handle. Normal linked completion leaves
a nontrapping peer running.

Inside an explicit trapping region, a delivered linked terminal signal becomes
a typed observation instead of a termination request. Trapping state at signal
delivery governs this choice. Leaving the region does not retroactively change
an already delivered observation. Normal exit can be observed while trapping.
A link observation is consumed at most once. A terminal signal ignored outside
a trapping region cannot be recovered by entering a region later; observing
that closed registration is invalid.

Unlink removes propagation in both directions and invalidates the caller's
registration. It is not a terminal event and supplies no invented result to the
other endpoint. An outstanding observation there can remain pending until its
own cancellation or scope termination. Re-registration checks actual link
membership and creates a new generation when the old link has ended. A stale
queued signal cannot satisfy a new generation. Unlink drains only private
notifications for the selected relationship, never arbitrary user messages.

User mailbox payloads, cancellation control, monitor results and linked exit
observations occupy separate protocol channels. Selective user receive cannot
mistake a control tuple for a legal message. Termination disposes unread user
messages under the retained actor lifetime rule.

## Cancellation and shutdown bounds

Cancellation is a request followed by observation at an admitted safe point.
Function entry, recursive invocation and blocked lifetime/receive waits are
safe points. No instruction-by-instruction realtime response is promised.
Repeated requests cannot complete a task twice or replace a terminal result.

Mandatory release masks cooperative cancellation and retains its own bounded
release grace. Task shutdown grace starts when cancellation is requested for
that child. At expiry, the manager can select forced loss and stop the child;
it never labels that transition successful cleanup. Expiry and cooperative
completion race by transition order. Once either wins, a late event cannot
revive or complete the child again.

Duration inputs are exact nonnegative integer nanoseconds. Native waits round
up to whole milliseconds and use finite intervals against one local monotonic
deadline. Reference time is explicit, nondecreasing virtual time; reference
fuel is not elapsed time. General sleep and timed-receive admission belongs to
G088 and is not implied by this proposed lifetime patch.

VM loss, external forced process loss and noncooperative foreign execution
cannot receive a local cleanup promise. No foreign frame or process-affine
foreign resource is admitted here. Supervision, distributed identity and
transport capacity remain separate plan items.

## Variability and limits

This contract introduces no configurable implementation choice,
presentation allowance or implementation-limit dimension. Explicit graces are
program input. Scheduling and eligible deadline races are defined
nondeterminism. Standing runtime capacity, reference fuel and exploration
budgets retain their existing classifications and reporting obligations.

## Diagnostics and conformance

The selected compound input is a retained decoded module with explicit family
bindings and programmatically supplied lifetime roles. Wrong exact selection
uses `EDN001`; invalid formation, escape or residual child effects uses `T002`;
invalid managed process context uses `PRC003`. Inconsistent verified evidence
uses `I001`; an open artifact entry uses `EFX003`. Runtime invalid ownership,
inactive observation and stale relationship are named terminal traps.

The backend independently verifies the core, applies standing source and
generated-code arity limits and requires a closed, zero-argument main. It emits
a deterministic `0.1.52` BEAM artifact with `task-tree-0.1.52` frontend identity.
It produces no interface and does not widen old interface or signed-format
sets. General sleep and timed-receive roles remain outside this exact target.

| Obligation | Required evidence |
| --- | --- |
| OT-OBL-001 | Exact selection, independent verification, deterministic selected artifacts and retained boundaries |
| OT-OBL-002 | Structural identities, scoped handles, ownership and escape/capture rejection |
| OT-OBL-003 | Register-before-start and normal structured join without raw-child ownership |
| OT-OBL-004 | First observed child failure, sibling cancellation and secondary outcome evidence |
| OT-OBL-005 | Mixed resource/task order, handler abandonment, mandatory failure and cancellation during acquisition |
| OT-OBL-006 | Independent typed monitors, absent registration, one observation and bounded exit classification |
| OT-OBL-007 | Demonitoring and observer-scope closure preserve user messages without owning targets |
| OT-OBL-008 | Symmetric linked failure, normal nontrapping behavior and cleanup before publication |
| OT-OBL-009 | Unlink, remote unlink and relink generations prevent stale notification reuse |
| OT-OBL-010 | Trapping at delivery, single observation and restoration after handler abandonment |
| OT-OBL-011 | Safe-point cancellation, bounded shutdown, single-winner deadlines and explicit forced-loss exclusion |
| OT-OBL-012 | Raw isolation, explicit child capabilities, managed identity and user/control separation |

## Lifecycle

The lifecycle record is `change-0-1-52-owned-task-lifetimes`, predecessor
`0.1.51`, a compatible addition affecting source acceptance, static meaning,
dynamic behavior and artifacts. It replaces the resource chapter's reservation
for task-tree integration only in this target. It adds no supervision,
distributed transport or public source vocabulary. C027/C082's entry closing
rules remain applicable: the target supplies no ambient handler or authority.

## Rationale and evidence (non-normative)

The [execution journal](../../50-journal/2026-09-08-owned-task-lifetimes.md)
records the decision alternatives, executable witnesses and admission evidence.
The [P084 plan](../../20-notes/language-completion-plan-semantics.md#item-084-process-lifetime-and-relationships-p084)
sets the closure gate. The
[pinned OTP process source](../../30-sources/erlang-otp-29-processes.md)
supports the native mapping, while
[actor research](../../30-sources/agha-1986-actors.md) motivates retaining raw
isolation. Catena's cleanup and typed observation rules remain local language
decisions, rather than claims made by those sources.
