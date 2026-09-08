---
title: "Language Completion: Resource Lifetime"
kind: journal
created: "2026-09-08"
tags:
  - language-design
  - algebraic-effects
aliases: []
---

# Language Completion: Resource Lifetime

## Scope and authority

This is implementation evidence and proposed design, not language authority.
It executes [CP-080-1 through CP-080-7](../20-notes/language-completion-plan-semantics.md#item-080-cleanup-and-resource-scopes-g080)
and the shared G088 lifecycle boundary. G080 stays open until checked core,
independent reference execution and production BEAM cover the admitted paths.
The next unused semantic patch remains `0.1.51`; this work does not register it.

The [scope research](../20-notes/algebraic-effects-and-handlers.md#scoped-and-higher-order-effects)
separates runtime-owned lifetime from first-order request handling. Retained
C010 raw spawn, C081 terminal traps and C005 affine resumptions remain unchanged.
Foreign ownership and noncooperative foreign frames need explicit future
adapters; this slice cannot infer cleanup guarantees for them.

## Prior publication

C057 was merged through [research PR 82](https://github.com/pcharbon70/catena-research/pull/82)
and [compiler PR 132](https://github.com/pcharbon70/catena/pull/132).
Research `main` and compiler `rewrite` were checked out and synchronized with
origin before local and remote branch deletion. Resource work starts on
`codex/resource-lifetime`. No continuation is scheduled.

## Implementation decisions

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| RL-I01 | A: build an explicit pure event transition model before runtime integration; B: wrap host try/finally first; C: extend ordinary handler clauses to release implicitly; D: count host finalizers as language guarantees. | **A, recommended and selected.** The model separates acquisition, active ownership, release, completion and external loss. It is an oracle for later integration, not completion evidence alone. |
| RL-I02 | A: assign one explicit owner and lexical scope to each unique resource entry, preserve consumed entries for invalid-use checks and permit use only in an active ancestor; B: identify resources by payload equality; C: allow aliases to register separate releases; D: transfer ownership on capture. | **A, recommended and selected.** Identity and lifetime are separate from values. Checked core will still need static escape and capture rejection; runtime checks supplement that boundary. |
| RL-I03 | A: give each mandatory release an explicit finite grace in exact nanoseconds, mask cooperative cancellation during that release and record deadline exhaustion before proceeding to remaining releases; B: wait forever; C: kill on each cancellation; D: share an undocumented host timeout. | **A, recommended and selected.** For a finite admitted resource stack, per-release grace bounds the total release allowance by its sum. Host granularity rounds waits upward in later G088 integration. Exhaustion records failed release, never successful cleanup. |
| RL-I04 | A: preserve the original outcome separately from ordered release errors, retain an original trap, and otherwise make any mandatory release error terminal; B: overwrite the cause with the last error; C: report success with warnings; D: convert traps to recoverable data. | **A, recommended and selected.** Host evidence can retain provenance without creating a language catch mechanism. The earliest release error determines the new terminal reason; all later errors remain ordered secondary evidence. |
| RL-I05 | A: linearize scope completion when closing begins, keep cancellation idempotent and observe it only at explicit active-scope safe points; B: retroactively override a completed outcome; C: deliver repeated cancellation during cleanup; D: permit both normal and cancelled completion. | **A, recommended and selected.** Cancellation during cleanup is masked; an outer active scope may observe the pending request. Deadline versus release-completion schedules remain explicit model transitions. |
| RL-I06 | A: classify external process kill and VM loss as loss with no cleanup promise, and reject foreign registration until an adapter is admitted; B: promise local finalizers survive all failures; C: run arbitrary foreign release code in a helper and claim ownership transfer; D: omit these paths. | **A, recommended and selected.** Executable classification tests establish the exclusion only. Process-exit integration must later distinguish cooperative managed shutdown from externally forced loss. |

## Proposed transition boundary

Opening pushes a lexical scope. Beginning acquisition records a pending entry;
success alone adds it to the scope's release stack. Failed acquisition closes
the scope with its supplied classified outcome but never releases that failed
entry. Closing selects its primary outcome and starts the last acquired entry.
Each release completes once, fails once, or exhausts its finite grace; all
remaining acquired entries are considered in reverse order. Completion removes
the scope from the active stack and records one outcome with its provenance.

Nested scopes close independently, with their owner deciding whether the
result continues normally or propagates outward. A release callback cannot
reenter acquisition or open a scope in the closing frame. A resource from an
active ancestor remains usable in a nested active scope, but cannot be used
from a different owner or after release. The eventual typed-core boundary must
prevent handles from escaping in returned values, closures or messages.

## Evidence and remaining integration

Implementation and verification results will be recorded here. No G080
checkbox or conformance obligation is promoted by the transition model alone.

## Transition model checkpoint

`Catena.Resource.Lifecycle` now models lexical scope opening, pending versus
successful acquisition, ancestor use, reverse release, classified completion,
idempotent cancellation, explicit safe points, virtual time, release deadline
races and external loss. Eight focused tests pass across normal, value failure,
abort, trap, cancellation and cooperative exit outcomes. The model rejects
cross-owner use, duplicate registration, cleanup reentrancy and unadmitted
foreign registration. It retains failed/lost status instead of claiming release.

This is an experimental oracle only. It has no semantic revision, checked
resource-handle type, source entry or production lowering. G080 remains open.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| RL-I07 | A: explore bounded permutations of explicitly supplied transition events, retaining only enabled steps and reporting exhaustion; B: run timing-dependent sleeps; C: sample a single handpicked ordering; D: treat a finite sample as an unbounded proof. | **A, recommended and selected.** Cancellation, completion and deadline races need a permitted outcome set. This event-model explorer is bounded evidence and does not substitute for later actor/core exploration. |

## Scope integration decisions

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| RL-I08 | A: add an explicitly experimental internal scope node with separately checked acquisition, body and release expressions before registering a semantic revision; B: silently extend exact 0.1.50; C: invent public bracket tokens now; D: stop at the event model. | **A, recommended and selected.** Scope cleanup must cross real kernel request/resumption boundaries. The retained frontends and artifact registry stay closed until independent verification and both execution paths agree. |
| RL-I09 | A: require the initial release callback to be closed over admitted immutable values and have an effect-free payload-to-Unit type, with terminal failure still possible; B: admit arbitrary foreign finalizers immediately; C: let release reuse an abandoned resumption; D: ignore the release callback's type. | **A, recommended and selected.** This creates an executable local boundary without claiming foreign ownership or general higher-order control. Resource-handle use and escape checking remain required before G080 closure. |

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| RL-I10 | A: execute the experimental closed pure release callback in a linked monitored helper carrying only its admitted immutable payload, with a finite wait and explicit timeout failure; B: block the owner forever on divergent release; C: transfer arbitrary foreign handles to a helper; D: kill the owner and claim remaining releases succeeded. | **A, recommended and selected.** Scope authority stays with the caller; this is a delegated release computation over sendable local values, not a foreign ownership adapter. Future resources whose cleanup is process-affine require a separate admission path. |
| RL-I11 | A: release at the normal CPS continuation boundary and also on return without resumption or terminal unwind, with an at-most-once runtime token; B: release only after the outer continuation finishes; C: release only on traps; D: register cleanup as an ordinary effect request. | **A, recommended and selected.** Normal cleanup precedes the enclosing suffix, while abort cleanup runs when its suspended continuation is discarded. An already released scope is inert during subsequent unwinding. |

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| RL-I12 | A: give the experimental handle a fresh structural scope identity and an opaque non-sendable type, with an explicit checked read of its immutable payload; B: expose the payload as the ownership token; C: infer ownership from host tuple shape; D: permit unchecked handles in messages. | **A, recommended and selected.** Reading copies an admitted immutable value; it does not transfer the live handle or admit foreign storage. Runtime owner/status checks supplement static lifetime rejection. |
| RL-I13 | A: initially reject closure capture of a live resource handle, even if the closure appears to be used locally; B: implement a full borrow/region solver now; C: track only handles visible in the return type; D: permit capture and rely exclusively on runtime failure. | **A, recommended and selected.** This conservative experimental boundary prevents hidden closure escape without admitting general linear types. A later nonescaping-closure analysis can expand it through an explicit decision. |
| RL-I14 | A: derive scope identities from module origin, owner, definition position and structural scope preorder, rechecking them independently; B: accept caller-provided names as identities; C: generate random identities during checking; D: use source spans alone for inserted nodes. | **A, recommended and selected.** Inserted wrappers can share spans. Structural identity distinguishes nesting deterministically and rejects forged scope evidence. |

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| RL-I15 | A: expose experimental owner-authorized cancellation and release-deadline hooks, preserving a distinct cancelled outcome and letting G088 supply task propagation and clock scheduling later; B: convert cancellation to a catchable exception; C: silently make every retained expression cancellable; D: omit cancellation until after promoting resources. | **A, recommended and selected.** A live scoped handle authorizes the local cancellation hook. Cleanup is mandatory, and release failure becomes terminal; this does not finish general time, sleep, receive races or structured task ownership. |
| RL-I16 | A: let the reference accept explicit monotonic clock advances and eligible release-expiry transitions; B: equate semantic nanoseconds with CEK steps; C: consult wall time in the reference; D: ignore blocked release in the reference. | **A, recommended and selected.** Virtual-clock eligibility remains separate from evaluator fuel, and a completion/deadline race has exactly one selected terminal transition. |

## Checked scope execution checkpoint

The experimental kernel profile now has independent checking/verifying of
acquisition and release callbacks, deterministic scope identities, opaque
non-sendable handles, an immutable-payload read and conservative rejection of
handle escape or closure capture. The production artifact boundary rejects
this profile and cannot label it as a retained revision.

The CEK evaluator retains resource frames across real request/resumption
capture. Normal scope completion releases before its enclosing suffix;
handler abandonment and terminal traps unwind remaining active scopes in
reverse order. Experimental BEAM lowering uses an at-most-once runtime token
and a bounded linked/monitored release helper over the admitted local payload.
Normal return, actual outer-handler abort, failed acquisition, primary trap
plus failing release, and mandatory-release failure have matching executions.
A full intermediate regression run passed **684 tests** before the subsequent
handle/cancellation/deadline cases; final totals will supersede that checkpoint.

Remaining before promotion: complete the cancellation and cooperative-exit
matrix, verify deadline races and release reentrancy, document the exact
admission/exclusion contract and production version, and run final regression
and conformance gates. General task propagation and time remain G088; foreign
process-affine resources still require their explicit future adapter.

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| RL-I17 | A: give cooperative owner exit its own internal hook and outcome, unwind before exit, and keep forced external kill outside that guarantee; B: treat every host exit as a normal resource completion; C: map every exit to a recoverable value; D: assume C010 raw process failure implies cleanup. | **A, recommended and selected.** Managed exit is an explicit local lifetime action. General links, monitors, supervisors and child ownership remain P084/G089; raw spawn is unchanged. |

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| RL-I18 | A: record the selected scope outcome before cleanup and preserve ordered release results as conformance evidence; B: infer the original outcome from the final trap; C: retain only the last cleanup error; D: expose a new catchable aggregate language value. | **A, recommended and selected.** A failed release can replace a non-trap outcome terminally without erasing its original provenance. Instrumentation remains distinct from language-level recovery. |

The [pinned OTP BIF source](../30-sources/erlang-otp-29-time-and-process-bifs.md)
supports monitored release workers, unlink-before-forced-stop and local
monotonic deadline arithmetic. The live
[receive documentation](https://www.erlang.org/doc/system/expressions.html#receive),
read on 2026-09-08 (displaying OTP 29.0.6), confirms millisecond waits and the
finite receive-timeout range; local tests run the installed OTP 29.0.4.
Long release allowances are split into bounded waits against one deadline.

## Promotion decision

| Decision | Four alternatives explored | Selected recommendation |
| --- | --- | --- |
| RL-I19 | A: promote the verified local scope carrier and production BEAM artifact as 0.1.51, retaining exact older targets and leaving general task/time and foreign adapters explicitly unadmitted; B: label the new core as 0.1.50; C: ship only test compilation permanently; D: claim all G088 and foreign work complete with local scopes. | **A, recommended and selected.** The local contract has actual continuation-unwind and owner-lifetime evidence. Promotion still requires the final artifact, conformance and archive checks; it does not expand the public vocabulary. |

## Verified local contract and promotion

The final implementation promotes C080 at exact **0.1.51**. The
[owned lifetime chapter](../60-specification/resource-scopes/owned-lifetime-and-mandatory-cleanup.md)
now controls the admitted scope contract. Deterministic scope identities include
module origin, module name, definition/process role, entry position and scope
preorder; dynamic invocations receive fresh owner tokens.

Final verification in the compiler repository:

- `mix test --seed 0`: **698 tests passed**. Existing test-only warnings remain;
  production compilation below succeeds with warnings treated as errors.
- `MIX_ENV=prod mix compile --warnings-as-errors`, `MIX_ENV=prod mix escript.build`,
  `mix format --check-formatted`, and `git diff --check`: passed.
- The behavioral resource suite includes actual handler resume/abandonment,
  failed and abandoned acquisition, release before an enclosing suffix trap,
  typed failure preservation, original-trap precedence, later releases after
  failure, scoped read and direct/container closure escape rejection, owned
  cancellation and cooperative exit, virtual and BEAM release deadlines,
  reentry rejection, local actor return, forced owner loss, deterministic
  production artifacts and rejection of a residual-capability entry.
- Bounded event exploration checks cancellation/completion and release/deadline
  outcome sets. Exhausting the exploration allowance is explicitly incomplete,
  never evidence for an unbounded theorem.
- Archive validation: **590 documents, 63 directories, 731 obligations
  (636 traced, 74 partial, 21 untraced)**. All ten new RS obligations have
  passing behavioral witnesses; the tag inventory test is not itself proof.

The full regression run exposed stale default-revision assertions, now updated
to 0.1.51 while exact historical selections remain pinned. Fixture corrections
added the typed failure type export and retained operation parameter syntax.
Review also restored the reference handler-abort provenance event. These are
implementation corrections within RL-I18/I19, not new design choices.

C080 is complete for the explicit local admission contract. The checklist is
**90 complete, 32 partial, 17 gaps, 2 deferred**. General task cancellation and
time remain G088; links, monitors and supervision remain P084/G089. No
process-affine foreign adapter or final source vocabulary is claimed. The next
unused semantic patch is **0.1.52**.
