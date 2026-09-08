---
title: "Language Completion: Owned Task Lifetimes"
kind: journal
created: "2026-09-08"
tags:
  - language-design
  - actors
aliases: []
---

# Language Completion: Owned Task Lifetimes

## Scope and predecessor

C080 merged in [research PR 83](https://github.com/pcharbon70/catena-research/pull/83)
and [compiler PR 133](https://github.com/pcharbon70/catena/pull/133). Research
`main` and compiler `rewrite` were synchronized before deleting the local and
remote resource branches. The new branch is `codex/owned-task-lifetimes`.

This executes [P084's plan](../20-notes/language-completion-plan-semantics.md#item-084-process-lifetime-and-relationships-p084)
and the shared [G088 interface](../20-notes/language-completion-plan-semantics.md#item-088-cancellation-and-time-g088).
Neither checklist item is complete merely because its transition model exists.
The [C080 contract](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md)
controls cleanup; raw C010 spawn stays isolated.

## Implementation decisions

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I01 | A: model relationship registration, signal delivery and terminal publication as separate transitions; B: make notification synchronous with death; C: poll host liveness; D: read process status through mutable handles. | **A, recommended and selected.** Explicit delivery exposes the registration/termination and unlink/demonitor races required by CP-084-2/3. |
| OT-I02 | A: use distinct monitor identities and one symmetric link per pair with a fresh generation after unlink/relink; B: identify every relation by its target; C: allow duplicate links; D: reuse removed relation tokens. | **A, recommended and selected.** Independent monitors and idempotent links follow the pinned OTP model; generations prevent an old pending signal from activating a new link. |
| OT-I03 | A: separate typed lifecycle observations from the ordinary user mailbox; B: inject arbitrary OTP tuples into typed messages; C: widen every mailbox to dynamic terms; D: discard all completion evidence. | **A, recommended and selected.** The checked adapter will translate only admitted terminal classifications and preserve the closed message type. |
| OT-I04 | A: request cancellation on owned children and publish terminal completion only after an explicit cleanup acknowledgement; B: equate cancellation request with death; C: kill immediately; D: let detached siblings continue after owner failure. | **A, recommended and selected.** This composes C080's mandatory release with CP-084-5/6 without claiming prompt foreign cancellation. |
| OT-I05 | A: select a pending cancellation only at admitted safe points and keep the first observed terminal cause; B: retroactively override completed results; C: choose by wall-clock timestamps; D: permit multiple completions. | **A, recommended and selected.** CP-088-2/3/7 require one linearized choice, with cleanup failure precedence still governed by C080. |
| OT-I06 | A: begin with an executable reference model, then typed core and BEAM witnesses before reserving 0.1.52; B: immediately mark P084 complete; C: label new behavior 0.1.51; D: expose raw host lifecycle calls as the language interface. | **A, recommended and selected.** This is an implementation order, not a replacement for the full per-item gates. |

## Primary evidence

Read the pinned [OTP 29 process documentation](../30-sources/erlang-otp-29-processes.md)
from its raw source on 2026-09-08, sections Links, Receiving Exit Signals and
Monitors. Local links are symmetric and repeated linking is idempotent;
monitors are independent and observe an already absent process as `noproc`.
Exit handling depends on link activity and the receiver's trapping state when
the signal is received. Catena's typed lifecycle adapter is our design, not an
OTP claim. Model tests will precede the corresponding host probes.

## First reference and host checks

The first **13 tests pass**: eight reference transition cases and five real
OTP process probes. They cover independent monitors, registration after death,
flush isolation, trapping and nontrapping link outcomes, unlink-before-failure,
structured join, first observed child failure and cooperative cancellation.
They do not yet establish checked source adoption or complete P084/G088.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I07 | A: use one private scope manager to register owned workers before starting them, monitor completion, and serialize join/cancellation decisions; B: let every child mutate the owner's state; C: derive ownership from arbitrary host links; D: poll process liveness to infer joins. | **A, recommended and selected.** Atomic registration avoids losing an immediately exiting child; a private manager can preserve typed outcome channels without widening user mailboxes. |
| OT-I08 | A: use explicit finite shutdown grace after cancellation, observe cooperative cleanup first and classify a noncooperative worker still live at expiry as forced external termination; B: wait forever after cancellation; C: kill before requesting cleanup; D: promise every foreign call can be interrupted safely. | **A, recommended and selected.** This is an explicit task boundary, separate from each C080 release allowance; forced expiry cannot falsely claim cleanup completed. The exact typed admission remains to be specified and tested. |
| OT-I09 | A: keep runtime probes experimental until the checked task core inserts safe points at admitted call/backedge and blocking boundaries; B: mark host callbacks as language implementation; C: inject cancellation into every retained pure function; D: poll only at manually written source hooks. | **A, recommended and selected.** Runtime implementation alone cannot satisfy CP-088-7 or the P084 completion gate. |

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I10 | A: instrument function entry, including recursive re-entry and generated closure bodies, for the experimental owned-task lowering only; B: instrument every retained artifact; C: rely on manually written polling loops; D: use reduction counts to interrupt arbitrary instructions. | **A, recommended and selected.** This establishes automatic call/backedge polling while retaining tail position. Outside an explicitly admitted owner/worker context the injected checkpoint is inert; release helpers have no inherited task context. Blocking boundaries still require their own integration. |
| OT-I11 | A: verify the existing checked core before a separate experimental Erlang-form instrumentation pass and emit no selected language artifact; B: forge 0.1.51 artifact metadata around modified behavior; C: bypass core verification; D: declare all task nodes implemented from callback tests. | **A, recommended and selected.** The probe can execute generated code now while preserving the later checked task-node and production-version gates. |

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I12 | A: represent lexical scope and owned-child handles as distinct nonescaping internal types, require child callbacks to be effect-closed, and preserve explicit owner control; B: reuse unrestricted raw PIDs as ownership proof; C: infer ownership from captured variables; D: allow scope handles to outlive their lexical scope. | **A, recommended and selected.** This follows CP-084-4/5 and uses C080's conservative lifetime-capture discipline. These are internal core roles, not final language names. |
| OT-I13 | A: mark normal body completion in the CPS scope callback so enclosing-handler abandonment cancels children before propagating its result; B: treat every callback return as normal completion; C: prohibit all handlers within task scopes; D: detach children on abandonment. | **A, recommended and selected.** The marker distinguishes actual abandonment from normal return without making traps catchable or changing affine resumptions. |

## Checked-core integration checkpoint

Experimental task-scope, owned-start and cancellation nodes now have distinct
static lifetime types and inference-independent verification. Escaping or
captured lifetime handles reject. Existing selected revisions reject the task
nodes, and the production backend rejects the experimental profile. Generated
recursive child code observes cancellation through inserted function-entry
checkpoints, without a manually written source poll.

The runtime now observes child failure at owner safe points, unwinds an owner's
live C080 resource, and rejects late starts through completed scope tokens.
Each cancelled child has its own shutdown deadline; an expired child does not
skip siblings' cooperative cleanup. Late worker results cannot replace a
forced-expiry selection. Explicit private completion markers distinguish CPS
normal return from enclosing-handler abandonment.

Remaining gates include handler-abandonment composition, the independent CEK
owned-process transitions, typed link/monitor observation and exit-trapping
operations, waiting receive/time integration, and complete reference/BEAM race
sets. P084 and G088 remain open; no new semantic patch is registered.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I14 | A: order resource and task scope entries in one dynamic lifetime sequence and unwind that sequence; B: release all resources before joining any child; C: join every child before releasing any resource; D: check only the final result and ignore cleanup order. | **A, recommended and selected.** Nested resource/task scopes require inner resource release, child join, then outer resource release. Captured lifetime frames preserve the same ordering when a real handler abandons its continuation. |

The checked CEK and generated BEAM paths now agree on normal join, cancellation
of recursive child code, actual enclosing-handler abandonment, and a primary
owner trap across mixed resource/task nesting. The mixed witness observes
release payloads **22 then 11**, with the child cancelled and joined between
them. The last whole-suite checkpoint before these final CEK additions passed
**724 tests**; a later full run must supersede it before publication.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I15 | A: introduce explicit scope-authorized sleep with once-evaluated nonnegative integer nanoseconds and a virtual reference deadline; B: use ambient sleep in every pure expression; C: count CEK reductions as elapsed time; D: reevaluate duration after every unrelated message. | **A, recommended and selected.** This is the first G088 blocking boundary. It preserves ordinary messages, uses upward-rounded host waits against one monotonic deadline, and remains experimental until the complete time/receive contract is implemented. |

The first sleep witnesses pass on checked CEK and BEAM code: zero duration,
positive virtual deadline eligibility and negative-duration trapping. Duration
is evaluated as a normal expression exactly once. No user message is a sleep
completion signal, and no host timer message is introduced into the mailbox.
Task shutdown and resource release must share the reference clock before the
combined deadline contract can be promoted.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I16 | A: return a closed structural variant for monitor completion with caller-supplied labels for fixed semantic roles; B: expose arbitrary OTP exit terms; C: encode all outcomes as untyped integers; D: fix final library constructor names now. | **A, recommended and selected.** Completion remains statically distinguishable while the public vocabulary stays undecided. Unknown host failures receive a bounded classification rather than entering the typed value domain. |
| OT-I17 | A: use a private request alias with deactivation and exact-message draining around cancellable relationship waits; B: leave late replies in the user mailbox; C: consume arbitrary mailbox terms after cancellation; D: block cancellation until the observed process exits. | **A, recommended and selected.** The pinned OTP process source describes aliases separately from monitors. A wait must preserve unrelated user messages and cannot leave an active reply destination after abandonment. |

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I18 | A: register a private observer worker with the existing scope manager, distinguish it from owned computation, and cancel the observer when its scope closes; B: make monitoring own the target's lifetime; C: deliver raw DOWN tuples to the typed owner mailbox; D: leave detached observer workers after scope exit. | **A, recommended and selected.** A monitor observes a target; it does not join or cancel that target. The helper's lifecycle is owned by the observer scope and cleanup removes its native monitor. |

## Relationship admission decisions

Typed monitor programs now agree on CEK and generated BEAM completion, including
a process-local integer trap observed as a closed variant. Invalid label maps
and escaped monitor handles reject before execution. Monitoring a raw actor is
read-only and does not grant ownership or suppress structured child failure.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I19 | A: add a distinct managed-process handle for cooperative linked lifetimes while retaining raw Process handles; B: reinterpret every old raw spawn; C: link arbitrary host PIDs and claim cleanup; D: exclude all linked lifetimes. | **A, recommended and selected.** CP-084-1/2 require raw isolation and wider relationships to coexist. Older artifacts cannot be assumed to poll cancellation or protect typed mailboxes from host exit signals. |
| OT-I20 | A: place managed actor identity and native relationships in a private broker which forwards typed payload envelopes and requests worker cleanup; B: deliver raw EXIT tuples to typed receive; C: propagate native kill directly into a resource-owning worker; D: share the worker's mutable process dictionary across actors. | **A, recommended and selected.** This makes native relationship signals distinct from legal user payloads and permits cooperative cleanup before broker termination. It is a new explicit representation boundary, not a reinterpretation of C010's raw PIDs. |
| OT-I21 | A: let explicit unlink remove the logical generation and drain only that peer's queued native exit notices before a future relink; B: reuse generations across relinks; C: flush the whole mailbox; D: treat native link messages as durable user data. | **A, recommended and selected.** The earlier reference race model and pinned unlink guarantee require stale notifications to stay detached from a later relationship. |
| OT-I22 | A: keep managed spawn, identity, send, relationship and receive roles internal to the experimental core until the complete adapter is verified; B: name public language keywords now; C: widen old interface formats first; D: label the broker adapter as ordinary raw spawn. | **A, recommended and selected.** The user's vocabulary hold remains in force, and P093/P097 representation interfaces are established only as needed by M2. |

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I23 | A: require each function that awaits linked-exit observations to establish its own explicit trapping region; B: let a closure silently capture a mutable trapping flag; C: expose the host process flag globally; D: add an unverified implicit effect-row capability during this adapter step. | **A, recommended and selected.** A function boundary does not carry permission from the region where its value was formed. This conservative rule makes the protected operation reviewable and prevents a returned closure from using a region that has ended. |

## Managed reference and cancellation checkpoint

The full compiler regression at this checkpoint passed **743 tests**. Subsequent
focused witnesses also pass for checked managed link failure on both CEK and
BEAM, symmetric failure propagation, and relinking after the other endpoint
removes a native link. Production compilation with warnings treated as errors
passes. These are experimental results; P084 and G088 remain open and no
semantic revision is selected by this checkpoint.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I24 | A: represent managed relationship notifications as separate reference transitions with generation checks; B: inject them into the typed user mailbox; C: equate notification registration with delivery; D: omit managed actors from the reference interpreter. | **A, recommended and selected.** The executable reference now supports managed spawn, send, identity, links, unlink and trapping observation. Terminal notification follows cleanup. The earlier event model remains useful for explicit race exploration. |
| OT-I25 | A: use the existing cancellable alias protocol for task registration as well as observation; B: block indefinitely awaiting registration; C: leave late acknowledgements in the owner mailbox; D: start unregistered children before acquiring ownership. | **A, recommended and selected.** A manager failure or cancellation now interrupts registration waits, and alias deactivation prevents abandoned replies from becoming user messages. |
| OT-I26 | A: route explicit resource exit and cancellation through the same ordered task/resource unwind when task scopes are active; B: release all resources before joining any task; C: ignore task scopes on explicit cancellation; D: reverse only the statically visible scopes. | **A, recommended and selected.** Dynamic acquisition order governs mixed cleanup, including explicit resource operations. Existing ordinary resource behavior retains its previous path when there are no task scopes. |
| OT-I27 | A: recognize native link failures at both endpoints and recheck native membership when registering a link again; B: propagate only from locally registered peers; C: assume a cached active relationship cannot be removed remotely; D: replace symmetric links with one-way monitors. | **A, recommended and selected.** Focused tests found and repaired both one-sided failure propagation and stale cached membership after remote unlink. Native unlink drains only the selected peer's queued exit signals. |

The cross-engine monitor witnesses cover normal and integer-trap outcomes for
both retained raw actors and managed actors. Checked trapping and nontrapping
managed programs also agree. Additional host witnesses prove release payload
**66** is emitted before a peer that did not request the link exits, and that a
link removed by the other endpoint can be established again before fault **77**.

Remaining admission work includes remote unlink/observation races, restoration
of trapping regions on handler abandonment, combined shutdown deadline witnesses,
and the complete receive-timeout contract. No claim of complete process-lifetime
or time semantics follows from the passing helper and adapter tests.

## Timed receive and finalization experiments

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I28 | A: preserve an uncompleted observation at the other endpoint after unlink while removing propagation; B: manufacture a completion event for unlink; C: treat remote unlink as process death; D: leave propagation active despite unlink. | **A, recommended and selected.** Native unlink does not publish a terminal observation. The reference retains the other endpoint's observation separately from the active link. A new local registration invalidates that endpoint's old generation. |
| OT-I29 | A: include trapping-state restoration in captured dynamic cleanup on handler abandonment; B: leave trapping enabled after abandonment; C: reject every handled effect in a trapping region; D: restore only on ordinary return. | **A, recommended and selected.** The checked cross-engine witness abandons a real operation continuation, then observes that a subsequent linked failure terminates the now-nontrapping actor. |
| OT-I30 | A: select cooperative completion or forced shutdown once, with explicit virtual expiry; B: convert expiry into successful cleanup; C: allow expiry to replace already completed cancellation; D: expire solely by CEK step count. | **A, recommended and selected.** The virtual witness rejects early and repeated expiry and preserves a cooperative completion selected before the deadline transition. Forced expiry has its own outcome. |
| OT-I31 | A: add an internal managed timed-receive role with a once-evaluated integer-nanosecond duration and typed fallback; B: reinterpret every existing receive as timed; C: fix public timeout vocabulary now; D: reevaluate duration after each wait interval. | **A, recommended and selected.** The new role remains confined to the experimental core. The earlier raw receive and selected artifact revisions retain their established contract. |
| OT-I32 | A: lower long waits to bounded native receive intervals against one monotonic deadline; B: pass arbitrarily large durations directly to the host timer; C: clamp the language duration to one native interval; D: implement receive by consuming and reinserting arbitrary user messages. | **A, recommended and selected.** Upward conversion avoids early expiry, repeated intervals retain the original deadline, and selective receive preserves unselected messages. The native receive timeout introduces no timer reply into the user mailbox. |
| OT-I33 | A: give a queued matching message precedence when the receive actually selects, then commit either its branch or fallback; B: retroactively replace a selected fallback with a late reply; C: remove every queued message at expiry; D: assume all deadline/reply races are deterministic. | **A, recommended and selected.** Separate virtual schedules witness reply-before-selection and reply-after-selection. Zero duration still scans queued candidates after validating the duration. |
| OT-I34 | A: recognize blocked status itself as a cancellation safe point; B: depend on one incidental saved CEK control shape; C: poll only ordinary calls; D: wait until a timeout before accepting cancellation. | **A, recommended and selected.** The timed-receive cancellation witness exposed a reference busy loop because the saved control was a duration value. The repaired predicate admits cancellation for every blocked receive status. |

Focused checked CEK/BEAM tests now pass for queued matching messages at zero
wait, empty-queue fallback, positive virtual deadline eligibility, invalid
duration before queued-message selection, preservation of skipped messages
through fallback, and cancellation during a long timed receive. The explicit
reference race admits a queued reply before fallback selection, while a late
reply cannot replace the selected fallback. Unread messages are disposed at
process termination, rather than consumed as an extra receive.

The native and reference relationship/timeout work remains experimental. The
remaining publication gate includes a complete normative transition contract,
explicit exclusions and limits, traceability and conformance obligations,
capability/ownership rejection witnesses, deterministic selected artifacts,
and full regression after the latest edits. This entry does not close P084 or
G088 or allocate semantic patch 0.1.52.

The latest complete regression passes **754 tests**. Production compilation
with warnings treated as errors also passes; its first automatic approval
review timed out and the permitted retry succeeded. The
[draft lifetime contract](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md)
now makes the proposed P084 transitions reviewable before artifact admission
and normative promotion. Its proposed version does not register a revision.

## C084 admission and publication

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| OT-I35 | A: retain owned-child outcome evidence at completed join and keep private observer helpers out of that child inventory; B: discard secondary child outcomes; C: expose helper bookkeeping as typed child values; D: replace the first failure with the last outcome. | **A, recommended and selected.** Checked normal-child evidence agrees across the reference and generated code; real sibling failure witnesses retain the first failure and later evidence. |
| OT-I36 | A: treat a completed join acknowledgement as the winning completion and consume the manager's subsequent termination regardless of its later reason; B: wait forever for an exclusively normal manager exit; C: replace verified completed cleanup with an unrelated late manager failure; D: skip manager termination cleanup entirely. | **A, recommended and selected.** This removes a stranded join after a late external manager loss without weakening the acknowledgement's all-children-complete condition. |
| OT-I37 | A: admit the completed lifetime roles through exact `0.1.52` while rejecting general time nodes there; B: publish every experimental time role in the lifetime revision; C: retain only unselected helper artifacts; D: reinterpret the resource `0.1.51` target. | **A, recommended and selected.** `check_selected/3` and the production backend verify the lifetime target independently. The existing experimental checker remains a separate G088 workbench. No earlier interface or signed format is widened. |
| OT-I38 | A: decide trapping behavior at signal delivery and reject later recovery of an ignored terminal signal; B: retroactively recover ignored exits after entering a region; C: make trapping depend on registration time; D: deliver all exits as ordinary messages. | **A, recommended and selected.** Final review found and removed retroactive recovery of an ignored normal exit. The reference witness explicitly changes trapping state after delivery and rejects the old observation. |

Final compiler validation: **760 tests passed**, including exact selected
artifacts, capability inheritance rejection, acquisition-time parent
cancellation, dynamic cleanup, typed monitoring, native link races and retained
revision regression. Production compilation with warnings treated as errors
passes. Archive validation passes with **743 obligations: 648 traced, 74 partial,
and 21 untraced**, including the 12 C084 obligations. The namespace is `OT`;
`PL` already belongs to the prelude and was not reused.

The normative [lifetime contract](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md)
now closes C084. The compiler target is `0.1.52`; the next unused semantic patch
is `0.1.53`. General sleep and timed receive remain unselected G088 experiments,
with their own completion gate still open. They are not admitted by the
selected lifetime target. The checklist now records **91 complete, 31 partial,
17 gaps and 2 deferred** items.

Compiler evidence is pinned at
[`71753b76bd76102d6526ff7170bafdf4c85b2e5d`](https://github.com/pcharbon70/catena/commit/71753b76bd76102d6526ff7170bafdf4c85b2e5d).
The production escript build, formatter check and whitespace check also pass.
