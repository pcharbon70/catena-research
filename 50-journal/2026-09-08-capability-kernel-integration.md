---
title: "Language Completion: Capability Kernel Integration"
kind: journal
created: "2026-09-08"
tags: [catena, effects, conformance, testing, decision-log]
aliases: []
---

# Language Completion: Capability Kernel Integration

## Scope and baseline

Resume the [completion plan](../20-notes/language-completion-plan.md) under
the user's instruction to implement the remaining gaps and notify them as
each gap is remediated. Both repositories retain the uncommitted first slice
recorded in [the earlier journal](2026-09-06-language-completion-plan.md).
The implementation belongs in the sibling `catena` repository. No existing
changes are discarded, committed or published by this work.

The immediate dependency is CP-I05: preserve exact C010 while adding a
C005-compatible capability-aware kernel target before completing
P050/P053/P057. New public vocabulary and the final grammar remain held.
Notifications follow actual completion gates, not planned or partially
implemented work. An attempted hourly continuation was rejected by automatic
approval review because scheduled repository edits require explicit user
permission; no automation was created by that attempt. The user subsequently
answered **Authorize hourly continuation**. The heartbeat was created and
later **paused at the user's request**. The subsequent implementation request
explicitly prohibits continuation and authorizes committing, opening and
merging a PR after each completed gap, then syncing the integration branch
before deleting the feature branch. Work now runs only in active sessions.

## Decisions made before implementation

These selections refine the already delegated plan. Each recommendation is
agent-selected, not a separately reviewed user choice.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| CK-I01 | A: build a strict closed capability-row component with explicit slot identities and checked descriptors, then integrate resolution and open-tail constraints; B: reuse the bootstrap row helper unchanged, which silently keeps the first conflicting descriptor for a duplicate identity; C: keep ordinary family bags, preserving C010 but preventing general recursive escaping effects; D: use sets of family names, permitting recursion but collapsing distinct capabilities. | **A, recommended and selected.** Validate the algebraic prerequisite independently without changing exact C010 or pretending that the existing bootstrap helper supplies all new verifier obligations. |
| CK-I02 | A: use immutable structural identities supplied by lexical resolution, with family identity and type arguments checked for consistency; B: generate random identities, making output nondeterministic; C: use only display names, conflating shadowed or imported identities; D: use positions without module/owner qualification, permitting cross-owner collisions. | **A, recommended and selected.** The initial component accepts canonical nonempty string identities from its caller; the future resolver must derive them from origin, owner and binder slot, never source vocabulary or runtime authority values. |
| CK-I03 | A: return existing structured typing diagnostics for malformed or conflicting rows and reject missing subtraction targets; B: silently discard conflicts, making validation order-dependent; C: expose unchecked exceptions at the public component boundary, weakening diagnostic handling; D: choose the lexicographically first descriptor, deterministic but unsound. | **A, recommended and selected.** Successful normalization cannot hide a forged family/type association; exact handling consumes one named slot and preserves every other identity. |
| CK-I04 | A: keep the new component explicitly closed-row and reject unsupported open-tail input until its solver is specified; B: choose one of two tails by spelling, dropping a constraint; C: erase tails at serialization, changing meaning; D: claim general row inference from finite closed-row tests. | **A, recommended and selected.** This is a tested integration prerequisite, not general C005 row unification or completion of a checklist item. |

| CK-I05 | A: execute the independently scoped CP-086 receive repair while the larger capability-kernel integration remains open; B: block all other M1 work on the new kernel; C: jump to unrelated later milestones; D: mark receive complete from the old tag inventory. | **A, recommended and selected.** Receive uses the retained C010 process machinery and does not depend on the new ordinary-capability representation. This is an explicit M1 sequencing adjustment, not completion of P050/P053/P057. |
| CK-I06 | A: use self-enqueued fixture messages, an explicit result message after two selections, and inspect the live residual mailbox; B: infer selection from BEAM arrival traces, which record arrival rather than clause acceptance; C: assert only a returned unit; D: infer no-match waiting from a timeout alone. | **A, recommended and selected.** The reference stepper exposes selected messages and residual mailboxes. On BEAM, an acknowledgement proves both receives completed; explicit waiting state and exact mailbox snapshots witness empty/all-rejected suspension without claiming scheduler fairness. Tests terminate and monitor fixture processes before unloading code. |

| CK-I07 | A: give the correction its own specification area with an indexed explicit link to retained C086; B: relax the validator to allow arbitrary mixed versions in one area; C: rewrite every old chapter to the new version; D: hide the amendment in a nested directory outside the area-version check. | **A, recommended and selected.** Archive validation found the established one-version-per-area invariant. A separate correction area preserves that invariant and historical authority without weakening validation. |

## Execution evidence

Added `lib/catena/kernel/capability_row.ex` and
`test/catena/kernel_capability_row_test.exs` in the sibling compiler.
The component checks closed rows, coalesces repeated concrete identities,
preserves distinct same-family identities, rejects conflicting descriptors,
and subtracts exactly the selected identity. Type arguments remain opaque
already-resolved values; this component does not replace type formation,
lexical resolution or open-row constraint solving.

Focused command: `mix test test/catena/kernel_capability_row_test.exs
test/catena/kernel_effect_row_boundary_test.exs --seed 0` — **7 tests passed**.
Five new tests include exhaustive semilattice-law checks over the powerset of
three identities, conflict checks in both operand orders, exact subtraction,
and malformed/open-row rejection. Two historical kernel boundary tests
confirm ordinary effect multiplicity remains unchanged at exact `0.1.8`.
No gap has been marked complete by the new component alone.

Reviewed CP-086-1 through CP-086-4 and the C086 rule set: the retained
`0.1.46` starvation paragraph conflicts with scan-past-prefix preservation.
The current C086 test with two rejected messages demonstrates only no-match
waiting; it does not test the disputed bypass. The independent C010 launch
fixture demonstrates bypass but does not expose the BEAM residual mailbox.
No receive amendment or semantic version has yet been applied. The next
unused semantic patch remains `0.1.49`; the planned correction needs explicit
applicability, lifecycle registration, and stronger cross-target evidence.

## Regression checkpoint

On Elixir 1.20.2 / OTP 29.0.4, `mix format --check-formatted`,
`mix compile --warnings-as-errors`, and `mix test --seed 0` passed:
**629 tests passed**, including the five new row-component tests. Existing
warnings in older test modules remain; production compilation passed with
warnings treated as errors. Both repositories passed `git diff --check`.
Archive validation passed with **582 completed documents**, 60 directories,
6601 local links and 713 traceability obligations. The checklist stays at
85 complete, 36 partial, 18 gaps and two deferred items; this checkpoint
adds a prerequisite, not a new completion claim. Changes remain uncommitted.

## Receive correction execution and completion

Executed CP-086-1 through CP-086-4 using the CK-I05 sequencing adjustment.
The normative amendment lives in
[its own 0.1.49 area](../60-specification/selective-receive-correction/README.md),
preserving the original 0.1.46 paragraph. It adopts the remaining receive
rules and routed interfaces explicitly, replaces RC-OBL-004, registers a
`compatible-correction` and specifies migration without reinterpreting
historical selections or persisted formats. The next unused patch is now
**0.1.50**. New public vocabulary and grammar remain held.

The sibling adds `test/catena/c086_receive_completion_test.exs` (four tests):
exact correction registration with explicit old selection; two successive
oldest-matching selections on stepper and BEAM; empty mailbox waiting; and
all-rejected mailbox waiting. The selection fixture queues `[0, 2, -1, 1, 3]`,
selects `2` then `1`, and retains `[0, -1, 3]` in order. The live BEAM worker
acknowledges the pair before its mailbox is inspected. Waiting checks inspect
explicit VM state, not timeout expiry; every worker is killed and monitored
down before its module is deleted and purged. Stepper send/receive traces and
mailboxes provide the independent reference observation. No production
receive algorithm change was necessary: both targets already scan past
rejected messages.

`lib/catena/language_version.ex` registers 0.1.49 as source-text only;
`lib/catena/language_lifecycle.ex` records the correction separately from
compatible additions and supplies migration guidance. Cumulative frontend
inventories and default-revision tests advance; retained exact revision
assertions remain. The C086 tag inventory includes both files and states that
it is not semantic proof. The receive guide and conformance account explain
waiting correctly.

Initial validation caught an incorrect explicit-selection test option,
outdated default-revision expectations, and the one-version-per-area archive
invariant. Those were corrected without weakening the tests or validator.
Final `mix test --seed 0`: **633 passed**. Formatting, warnings-as-errors
production compilation, escript build, and both repositories' diff checks
passed. Final archive validation passed: 584 completed documents, 61
directories, 6633 local links, 175 specification chapters and 713 obligations. Existing older test-module warnings remain as before.

Updated the checklist to **86 complete, 35 partial, 18 gaps, two deferred**;
C086 is restored for this bounded rule set and P085/P087/G088/P109 retain
their own obligations. Updated the receive map, synthesis, inquiry, plan
checkpoint, decision execution links, area/root inventories and traceability.
RC coverage is now eight traced obligations; total traceability is 615 traced,
77 partial, 21 untraced. Changes remain uncommitted and unpublished.

## Next gates

1. Specify lexical slot binding/instantiation, capability substitution and
   independently checked request/handler identity evidence.
2. Implement the new kernel target, preserving the historical 0.1.8 parser,
   row behavior and artifact boundaries.
3. Integrate independently checked comprehension fragment rows and workers.
4. Execute enclosing-handler, same-family/distinct-capability, abort and
   nested-generator witnesses before updating P050/P053/P057.
5. Receive conflict resolution is complete at 0.1.49. Continue later
   milestones after the remaining M1 capability-kernel/comprehension gates.

## Publication preparation under the revised instruction

The user authorized the per-gap commit, PR, merge, sync and branch-cleanup
workflow. The first handoff includes the already completed C086 correction,
the previously uncommitted completion plan, and tested M1 prerequisites.
Those prerequisites do not change P050/P053/P057 completion status.
The compiler origin uses `rewrite` as its default branch; `main` has unrelated
history and no merge base with this work. The user explicitly selected **Use rewrite for compiler PRs**; compiler
merges and post-merge synchronization therefore use `rewrite`, while research
uses `main`. No unrelated-history migration is authorized or performed.
