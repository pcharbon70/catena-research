---
title: "Local Protocol Contract Implementation"
kind: journal
created: "2026-09-08"
tags:
  - language-design
  - actors
aliases: []
---

# Local Protocol Contract Implementation

## Starting point

C103 is merged through [compiler PR 136](https://github.com/pcharbon70/catena/pull/136)
and [research PR 86](https://github.com/pcharbon70/catena-research/pull/86).
Compiler `rewrite` at `dd08710ab5b09fc5863e8118f63b52cde3b8736c` and research
`main` at `74fff33096b03c130d64625df5daca3b7b8c03e4` were synchronized and clean
before the feature branches were deleted. Work continues on
`codex/local-protocol-contracts` without a scheduled continuation.

The original [CP-087 decisions](../20-notes/language-completion-plan-semantics.md#item-087-typed-protocol-contracts-p087)
select explicit library state machines over closed payload types, correlated
terminal outcomes and exact schema agreement. The
[outcome contract](../60-specification/outcome-contracts/values-sequencing-and-validation.md)
provides expected failure values; the
[time contract](../60-specification/cancellation-and-time/deadlines-waits-and-cancellation.md)
provides deadline and cancellation ordering. P085's remote facet remains open
until G091. The early workbench below records the experiments leading to the completed local contract.

## Decisions during implementation

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| LP-I01 | A: independent explicit-event lifecycle model before runtime implementation; B: infer protocol semantics from one native execution; C: use metadata assertions alone; D: require a new session-type system. | **A.** A bounded permutation test can distinguish reply, cancellation and expiry winners without claiming scheduler fairness or static session fidelity. |
| LP-I02 | A: a monotonic correlation counter scoped to one live session; B: reuse the caller process ID; C: match replies by arrival order; D: recycle terminal correlation IDs immediately. | **A.** Concurrent requests remain distinct and old replies cannot name a later request. This is correlation, not an authentication or remote exactly-once guarantee. |
| LP-I03 | A: an explicit outstanding-request bound returning overload before request transmission; B: silently drop live messages; C: block raw send at an undisclosed quota; D: promise a universal mailbox count floor. | **A.** This is protocol admission above C010 send, not a change to local mailbox semantics. P085/P129 still own deployment capacity and host-fatal pressure. |
| LP-I04 | A: bind protocol identity/version/role schema to a verified exported process interface and digest; B: compare display names only; C: accept any wider variant; D: inspect arbitrary host terms dynamically. | **A.** The schema consumes existing closed-mailbox checks and rejects incompatible peers before application payload exchange. Exact agreement is deliberately conservative. |
| LP-I05 | A: remove a pending request on its first selected terminal event and reject later events; B: overwrite replies when a timeout arrives later; C: retain two terminal results; D: retry automatically. | **A.** The model retains one outcome per request; the later LP-I07 decision specifies observation as the credit-release point. No application retry is implicit. |
| LP-I06 | A: peer loss completes all still-pending local requests and closes the session; B: reopen all completed requests; C: leave waiters indefinitely pending; D: reinterpret peer loss as successful empty replies. | **A.** Already delivered replies stay terminal and subsequent requests need a new negotiated session. Remote uncertainty remains a later transport contract. |

## Initial model evidence

Five `protocol_model_test.exs` cases pass: schema rejection before payload
exchange; interleaved request correlation and admission recovery; every
permutation of reply/cancel/expiry selecting one completion; peer loss after a
prior reply; and monotonic non-resetting virtual deadlines. These tests are
local model evidence only.

The experimental `Catena.Protocol.Contract` adapter checks the existing
kernel interface decoder, derives request/reply roles from the exported
closed mailbox type, and binds schema identity to the interface digest.
At this initial stage, native execution, owned lifetime integration, typed
application witnesses, full regression and normative publication were still pending.

## Completed implementation decisions

These decisions extend the original register's CP-087 choices without replacing
its historical recommendations.

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| LP-I07 | A: retain admission credit until observation; B: release at completion while retaining unlimited results; C: discard unread results; D: block raw send globally. | **A.** Both pending and unobserved completions count against the explicit bound. This corrects the initial completion-release interpretation and prevents unread-result accumulation. |
| LP-I08 | A: own a private worker under C084 and bracket its response aliases; B: detach it; C: reuse the caller's application mailbox for envelopes; D: make process links the protocol identity. | **A.** Cancellation and exceptional exit join the worker; exact alias disposal prevents later application receives seeing private results. |
| LP-I09 | A: exact checked finite application builder over existing pure payload producers; B: invent public syntax; C: call untyped host helpers sufficient completion; D: add affine session types. | **A.** A concrete compiler boundary verifies payloads and emits a selected artifact without adopting vocabulary or claiming static session fidelity. General surface elaboration remains P109. |
| LP-I10 | A: exact 0.1.55 application selection; B: silently widen retained 0.1.8 artifacts; C: retag every historical interface; D: omit selection metadata. | **A.** Old interface and signed formats remain unchanged; generated metadata identifies the new boundary and rejects retagged checked evidence. |
| LP-I11 | A: require the owning interface digest for nominal producers; B: compare type spellings; C: accept equal constructor arities; D: erase nominal identity. | **A.** The conservative owner check rejects an independently identified same-name datatype. Structural primitive producers can be separate modules. |
| LP-I12 | A: embed checked atom wire labels in compiled arguments; B: assume the compiler VM interned them forever; C: create atoms from received messages; D: use string envelopes unlike ordinary variants. | **A.** Loading the artifact links its validated constants; native typed actor envelopes share ordinary representation without incoming-message atom creation. |
| LP-I13 | A: fix task/managed observation representation to ordinary atom-label variants; B: special-case monitor patterns; C: weaken the checker; D: declare strings and atoms interchangeable globally. | **A.** An actual typed match failed in the independent stepper before this repair. Both reference adapters and native lowering now use ordinary labels; selected execution and time regressions pass. |
| LP-I14 | A: model protocol events independently and evaluate producers through the kernel stepper; B: use the native broker as its own oracle; C: test only schema metadata; D: claim exhaustive native scheduling. | **A.** Event permutations and model/native outcomes are evidence with explicit scope. The model does not execute the peer actor; a separate compiled-client/compiled-actor witness covers that boundary. |

## Verification and interpretation

The implementation now consists of a canonical interface-bound contract,
independent lifecycle model, scope-owned native session, exact checked
application compiler and independent application evaluator. Five dedicated
application tests cover deterministic artifacts, checked producer rejection,
explicit overload/cancellation/duplicate observation, exact historical selection
and nominal owner separation. Native tests additionally exercise a compiled
Catena client against a separately compiled Catena actor.

A monitor composition regression first failed with
`verified_match_reached_no_clause` because typed observation produced a string
label while ordinary variant patterns matched atom labels. The correction
changes both independent task/managed adapters and BEAM lowering. Sixteen
selected monitor/time tests passed after the fix; the regression consumes the
monitor result through an ordinary exhaustive typed match.

The [normative chapter](../60-specification/local-protocol-contracts/schemas-sessions-and-outcomes.md)
records this local explicit-library completion. P085 remains partial: the local
admission policy adds no universal mailbox floor and does not implement G091's
remote transport. No public language vocabulary has been adopted.

## Final verification and immutable implementation

Compiler commit [`4609bc83c1303472dce474af1106f42bcc8abc89`](https://github.com/pcharbon70/catena/commit/4609bc83c1303472dce474af1106f42bcc8abc89)
contains the implementation and witnesses. From the compiler repository:
`mix test` passed **806 tests**; `MIX_ENV=prod mix compile --warnings-as-errors`,
`mix escript.build`, `mix format --check-formatted` and `git diff --check` passed.
Expected trap-process logs and retained test-only warnings do not change those
results. The full local test transcript is `/tmp/catena-protocol-regression.log`.

Archive validation passed before publication; the checklist now records
**94 complete, 29 partial, 16 gaps and 2 deferred**. Eight LP obligations link
rules to executable witnesses. C087 consumes `0.1.55`; the next unused semantic
patch is `0.1.56`. No automation or scheduled continuation was used.
