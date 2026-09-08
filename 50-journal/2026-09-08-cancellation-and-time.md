---
title: "Cancellation and Time Admission"
kind: journal
created: "2026-09-08"
tags:
  - language-design
  - actors
aliases: []
---

# Cancellation and Time Admission

## Starting point

C084 is merged in [compiler PR 134](https://github.com/pcharbon70/catena/pull/134)
and [research PR 84](https://github.com/pcharbon70/catena-research/pull/84).
Compiler `rewrite` and research `main` were checked out and synchronized before
both local and remote feature branches were deleted. This G088 work begins on
`codex/cancellation-and-time` from compiler `7faee960607322ee98feaeb3808ec0fdc71159f6`
and research `23128421f250d250eaa60858e83485d7f27906ad`.

The [C084 journal](2026-09-08-owned-task-lifetimes.md) records the shared
experimental foundation: scope-authorized sleep, once-evaluated relative
receive timeout, exact virtual eligibility, mailbox preservation, cancellation
of blocked waits and the completion/deadline race. Those roles are rejected by
the selected `0.1.52` artifact target. The latest selected validation is 760
passing compiler tests. G088 remains open and the next unused patch is `0.1.53`.

## Execution decisions

The original [CP-088 decisions](../20-notes/language-completion-plan-semantics.md#item-088-cancellation-and-time-g088)
remain selected. The [lifetime contract](../60-specification/process-lifetimes/owned-tasks-and-managed-relationships.md)
and [resource contract](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md)
provide the owned cancellation and masked cleanup boundaries.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| TM-I01 | A: expose absolute deadlines as opaque scope-indexed local values derived from exact durations; B: expose raw host monotonic integers as portable timestamps; C: use wall-clock timestamps; D: omit absolute deadlines and require callers to reset relative waits. | **A, recommended and selected.** It preserves a shared budget across several waits without choosing public vocabulary or allowing a deadline from another owner/runtime to become meaningful accidentally. |
| TM-I02 | A: retain arbitrary exact nonnegative integer nanoseconds and split host waits into supported intervals; B: silently clamp the requested duration; C: use floating seconds; D: wrap overflowing host integers. | **A, recommended and selected.** The existing integer model and standing runtime-capacity classification apply. Conversion rounds waits upward, never expires early and does not reset the original deadline. |
| TM-I03 | A: admit relative and absolute waits through a separate exact target after independent verification; B: widen the merged lifetime target retrospectively; C: mark experimental helpers complete without artifact evidence; D: introduce final time-library names now. | **A, recommended and selected.** Exact `0.1.52` retains its published admission boundary. This work must satisfy G088's full reference/BEAM and artifact gate before promotion. |

## Absolute deadlines and blocking integration

Opaque absolute deadlines now retain one local budget across repeated waits
and selective receive. Checked reference and selected-artifact tests witness
exact virtual eligibility, queued-message priority after expiry, scope escape
rejection and preserved earlier admission boundaries. Host witnesses reject
foreign owners, ended scopes and forged empty origins. A duration larger than
256 bits retains its exact value while individual native waits remain bounded.

The timeout expression can itself receive a message. Its checked witness
observes the receive sequence **1, 0, 0**, proving duration evaluation occurs
once before scanning and is not repeated when candidate **99** is rejected.
Completed waits preserve unrelated messages without leaking timer replies.
Repeated cancellation during a blocked finalizer retains the mandatory
release-expiry trap instead of replacing it with a later cancellation reason.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| TM-I04 | A: retain a managed broker's already selected linked failure when its worker later returns normally; B: overwrite it with normal return; C: ignore linked failure until arbitrary worker instructions notice it; D: publish both outcomes. | **A, recommended and selected.** The reference now mirrors the broker's existing publication rule. This repairs the modeled completion race without adding a second completion or changing raw spawn. |
| TM-I05 | A: include private owned-task control clauses in receives only when their runtime scope/token guards authorize them; B: leave a raw actor's explicit owned scope blocked forever on child failure; C: reinterpret all raw actors as managed; D: consume arbitrary user messages as cancellation. | **A, recommended and selected.** A selected checked witness keeps raw actor identity but opens an explicit owned scope. Child failure interrupts its blocked receive and closes the scope on both engines. |
| TM-I06 | A: thread a deterministic traversal counter through receive lowering to allocate distinct private variables; B: reuse one variable set in every nested receive; C: generate random variable names and lose artifact reproducibility; D: store compiler counters in ambient mutable process state. | **A, recommended and selected.** The new cancellation clauses exposed nested capture of an outer scope map. The repaired lowering is deterministic and nested absolute-deadline artifacts pass again. |
| TM-I07 | A: model an explicit cancellation check after a completed time-target wait; B: inspect only the saved pre-wait control shape; C: retroactively replace a selected receive branch; D: assume cancellation can interrupt any instruction. | **A, recommended and selected.** The new target's post-wait boundary corresponds to generated continuation entry. It does not select a second receive branch or reinterpret reference fuel as time. |

The first complete suite after exact time-target admission passed **767 tests**.
Later blocking-race corrections require a fresh full run before publication.

## C088 publication gate

The final full suite passes **772 tests**. Production compilation with warnings
treated as errors, production escript build, formatter and whitespace checks
pass. Selected relative/absolute time artifacts are deterministic across
repeated production compilation. Eight `TM` obligations connect the normative
contract to behavioral evidence; the tag inventory is not semantic proof.

The [time contract](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md)
is promoted at exact `0.1.53`. Exact `0.1.52` continues to reject time nodes.
The integration also repairs the C084 reference's already-selected managed
failure race and cancellation-aware lowering for raw actors with explicit owned
scopes; these preserve the published ownership contract rather than assigning
implicit ownership to raw spawn. Nested receive variable allocation is now
purely deterministic.

C088 closes with **92 complete, 31 partial, 16 gaps and 2 deferred** checklist
items. The next unused semantic patch is `0.1.54`. Supervision, distribution,
transport/resource capacity and foreign-call admission remain separate work.

Compiler evidence is pinned at
[`e685a2b32e037d28848a3b67de424fcd2f86832b`](https://github.com/pcharbon70/catena/commit/e685a2b32e037d28848a3b67de424fcd2f86832b).
Final archive validation passes with **751 obligations: 656 traced, 74 partial
and 21 untraced**.
