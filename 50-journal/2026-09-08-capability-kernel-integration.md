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

## M1 capability binding and instantiation decisions

C086 publication completed: research PR #79 merged as `c87fd88`, compiler
PR #129 merged as `234ddea`. Both integration branches were synchronized
before local and remote feature branches were deleted. The next slice uses
`codex/comprehension-capability-kernel`; no continuation is active.

These new choices implement C005's
[lexical identity and hybrid equality](../60-specification/effects-and-handlers/capabilities-rows-and-selection.md#lexical-capability-identity)
without admitting new source syntax or silently changing exact C010.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| CK-I08 | A: derive slot keys by canonical encoding of origin, owner and numeric binder path, excluding display names; B: concatenate slash-separated strings, which can collide; C: use fresh random keys, losing reproducibility; D: use display-name hashes, breaking alpha-renaming and shadowing. | **A, recommended and selected.** The structural path belongs to resolved syntax; origin and owner qualify it. Formation checks reject empty identity components and invalid paths. |
| CK-I09 | A: select from an explicitly supplied lexical-visible environment, reject zero or multiple compatible candidates, and require explicit qualifiers to identify one compatible slot; B: choose the innermost matching handler dynamically; C: choose the first sorted compatible slot; D: collapse all same-family slots before lookup. | **A, recommended and selected.** Selection remains static and ambiguity preserves all candidates. The surrounding resolver remains responsible for computing visibility and operation membership; this component never claims to implement that outer boundary. |
| CK-I10 | A: instantiate rows with simultaneous descriptor-checked slot substitution followed by normalization; B: recursively follow substitutions, allowing cycles or accidental capture; C: rename only slot strings without family/type checks; D: forbid two formal slots from selecting the same concrete capability. | **A, recommended and selected.** One-step substitution preserves caller identities, permits same-actual coalescing, and rejects descriptor mismatches and unknown source slots. Type-argument unification must occur before this boundary; open rows remain unsupported. |

These components remain integration prerequisites until the new parser,
checker, verifier, runtime capability environment and comprehension worker
rows consume them. No gap completion is inferred from their unit tests.

## Capability binding checkpoint

Implemented `lib/catena/kernel/capability_binding.ex` in the sibling compiler:
structural slot identity with checked origin/owner/path, and static selection
from the caller's already resolved visible environment. Added simultaneous
`CapabilityRow.instantiate/2`: targets are descriptor-checked, unknown formals
reject, shared actuals normalize, and target keys are never recursively chased.
This is not lexical visibility construction, type unification, escape checking,
operation-membership checking or the new kernel frontend itself.

`test/catena/kernel_capability_binding_test.exs` adds five focused tests for
identity determinism/collision resistance over structural components, malformed
identities, order-independent ambiguity and qualifier compatibility, shared
versus distinct actuals, simultaneous cyclic-name substitution, and forged
substitutions. The focused binding/row/historical-kernel set passes **12 tests**;
`mix test --seed 0` passes **638 tests**. Formatting and production compilation
with warnings as errors pass; both repositories pass diff checks. Archive
validation passes: 584 documents, 61 directories, 6634 local links and the
unchanged 713 traceability obligations.

These changes remain uncommitted on `codex/comprehension-capability-kernel`.
They do not close P050/P053/P057 and therefore do not trigger another per-gap
PR yet. Next work must integrate identity-bearing schemes, request/handler
selection and independent verifier evidence into an explicitly versioned
kernel, then thread comprehension fragment rows and run enclosing-handler
abort and general escaping-effect witnesses. No continuation is configured
or resumed by this active-session work.

## Closed capability-kernel integration decisions

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| CK-I11 | A: integrate an explicitly experimental closed-slot kernel model before registering a language revision; B: change exact C010 row equality in place; C: claim a new stable frontend before its verifier and artifact boundaries exist; D: postpone all execution until a general open-row solver exists. | **A, recommended and selected.** Generated comprehension workers need statically selected closed capabilities. The experimental model is visibly separate from the retained frontend; normative promotion and broader row-polymorphic support remain separate gates. |
| CK-I12 | A: use explicit slot-to-family bindings, preserve a checked structural identity and verify same-family operation descriptors agree; B: identify capabilities only by family; C: infer authority from nearest runtime handler; D: accept arbitrary duplicate-family descriptors. | **A, recommended and selected.** Same-family distinct slots remain distinguishable; the resolver must reject ambiguous or inconsistent authority rather than rely on runtime nesting. |
| CK-I13 | A: bind definition-signature slots abstractly, require visible slots at requests/global references, bind a fresh slot at handling, and reject escaping latent slots; B: allow ambient access to every declared slot; C: allow handled closures to escape; D: forbid all effectful higher-order values. | **A, recommended and selected.** The bounded model preserves lexical authority and admits generated recursive functions under their selected enclosing handler. Reusing an already visible slot for a fresh handler is rejected. |
| CK-I14 | A: retain shared type rules but distinguish identity-bearing row entries and independently rederive their rows in the verifier; B: duplicate the entire checker and verifier; C: trust elaborator annotations; D: validate effects only at runtime. | **A, recommended and selected.** Old ordinary occurrences keep multiplicity. Capability entries coalesce by exact identity only in the experimental profile, with a verifier gate preventing them from entering retained 0.1.8 evidence. |

This stage does not register 0.1.50 or emit historical persisted artifacts with
new semantics. Tests can lower verified experimental core to BEAM directly;
the production artifact boundary remains a subsequent gate.

## Experimental comprehension row integration

CP-I01 and CP-I02 are now resumed for the explicitly experimental closed-slot
model. Qualifier `uses`, `yield_uses`, and optional fourth context-tuple rows
remain the selected metadata shape; each fragment is checked in a standalone
nonrecursive probe before generated worker signatures are changed.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| CK-I15 | A: add a separate experimental typed-core comprehension entry using the existing pure elaborator for tree shape and independently checked fragment rows; B: silently route the old elaborate API to new semantics; C: infer rows from the recursive worker only; D: generate untyped BEAM loops directly. | **A, recommended and selected.** Retained inputs keep their old execution boundary. The new entry returns experimental core, not a misleading historical source or artifact. |
| CK-I16 | A: put each worker's suffix row on its final executed arrow, keep closure creation/reversal pure, and union source/qualifier/yield rows at the entry; B: use the aggregate row on every arrow; C: leave arrows pure; D: charge source effects only after iteration begins. | **A, recommended and selected.** A worker's own source has already been evaluated by its caller. Independent probes reject understated or overstated fragment rows before recursive equations can mask annotation errors. |
| CK-I17 | A: render explicit enclosing handlers around the entry before final parsing/checking; B: move handlers into each fragment; C: wrap only the yielded value; D: execute a separate host-side interpreter for each fragment. | **A, recommended and selected.** Preserving the entire traversal continuation is necessary for abort and lexical scope. Generated source positions come from reparsing the wrapper, avoiding invented or colliding spans. |

Context probes admit earlier context entries only; this experimental boundary
rejects recursive/forward context dependencies rather than trusting them as
nonrecursive evidence. This does not narrow the retained elaborate API.

## Promotion boundary decisions

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| CK-I18 | A: register 0.1.50 for the closed capability-tree carrier and its typed core, keeping the old S-expression decoder as an explicitly quoted syntax component of the new compound input; B: make bare 0.1.8 programs silently select capability semantics; C: invent final comprehension source tokens now; D: leave passing effect traversal permanently experimental. | **A, recommended and selected.** The new boundary is the explicit qualifier tree plus slot/family map and enclosing-handler list. Standalone old source retains old meaning. This amends the dormant target only, not the public vocabulary or the retained parser. |
| CK-I19 | A: emit a distinct 0.1.50 BEAM artifact through the existing deterministic OTP production boundary, with no new interface or signed format; B: stamp new semantics as a 0.1.8 artifact; C: expand old interface decoding to accept capability rows without versioning; D: use a test-only compiler path as the shipped implementation. | **A, recommended and selected.** Core compilation must verify first and require a closed, fully handled main entry. The new artifact cannot masquerade as an old importable interface; package/interface adoption remains separately gated. |
| CK-I20 | A: expose malformed lexical capability scope as EFX003 during checking and retain verifier rejection for forged core; B: report user scope errors as an internal compiler defect; C: discard unknown capability evidence; D: allow a request to fall through to a runtime nearest-family search. | **A, recommended and selected.** The existing EFX003 category covers invalid or escaping capability variables; independent verification still rechecks the same invariant without trusting type inference. |

The integrated nested fixture initially exposed a missing capability-row case
in CPS classification: the first source ran but recursive workers lost handler
routing on BEAM. Extending the checked ordinary-effect predicate to explicit
capability entries repaired it without changing old effect entries. The 15-test
reference/BEAM fixture set then passed, including all failure prefixes and
whole-comprehension abort. Distinct-slot and forged-core checks supplement it.

## Intrinsic process preservation

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| CK-I21 | A: preserve intrinsic Process at the closed artifact entry and pass module ownership through definition lowering so private local spawners remain local calls; B: reject all Process use in the new target; C: export every private spawner; D: claim preservation using reference execution alone. | **A, recommended and selected.** Process is not an ordinary capability slot. The BEAM regression exposed missing module ownership in existing value-definition lowering; repairing that routing preserves abstraction without widening exports. |

## C050 acceptance at the promoted target

The closed compound input, checker, independent verifier, reference execution
and production BEAM boundary now select exact `0.1.50`. Old standalone
`0.1.8` parsing and bag rows remain unchanged; interface and signed-format
sets remain unchanged. The normative target amendment records eight CK
obligations and explicitly excludes general open rows and public grammar.

C050 is complete: escaping filter requests, false-filter observations,
first/last traps, whole-traversal abort and a handler changing the whole result
type agree on reference and production BEAM. Fragment metadata is checked
before recursive worker annotation. Distinct same-family slots remain distinct;
forged rows, identities, scope and artifact revisions reject. Intrinsic Process
also executes on both targets, including a private local spawner.

Final compiler verification: `mix test --seed 0` passes **662 tests**;
`mix format --check-formatted`, production compilation with warnings as errors,
production escript construction and `git diff --check` pass. Existing warnings
in historical test fixtures do not affect the production warnings gate.
Archive validation passes with **586 documents, 62 directories, 176 normative
or draft specification chapters and 721 obligations (624 traced, 76 partial,
21 untraced)**. Maps, the inquiry, directory indexes, decision execution links
and the checklist now identify C050 completion. P053 and P057 remain separate
acceptance passes rather than being inferred from this filter closure.

This change is prepared for the authorized C050 PR pair on research `main`
and compiler `rewrite`. Publication and integration-branch synchronization
precede feature-branch deletion; no scheduled continuation is used.
