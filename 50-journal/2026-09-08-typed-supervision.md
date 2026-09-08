---
title: "Typed Supervision Workbench"
kind: journal
created: "2026-09-08"
tags:
  - language-design
  - actors
aliases: []
---

# Typed Supervision Workbench

## Starting point

C087 merged through [compiler PR 137](https://github.com/pcharbon70/catena/pull/137)
and [research PR 87](https://github.com/pcharbon70/catena-research/pull/87).
Compiler `rewrite` synchronized at `9cb699c9cf19a1c83c0ec168cfdc69d5ecbfb640`;
research `main` synchronized at `1f57ceb0c403d38c6f8cfa6a14f806f7451f83f6`.
Both feature branches were deleted after synchronization. This work begins on
`codex/typed-supervision`; G089 remains open. Next unused semantic patch is
`0.1.56`, not yet admitted by these experiments.

## Decisions during implementation

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| SU-I01 | A: independently model the full selected strategy/policy matrix; B: use OTP as its own oracle; C: test only permanent children; D: add core supervision syntax. | **A.** Explicit model generations reject stale exits and policy commands expose ordered stop/start behavior. |
| SU-I02 | A: inspect the installed OTP 29.0.4 source; B: rely on a moving latest page; C: infer window semantics from wall-clock sleeps; D: omit exact boundary evidence. | **A.** The implementation's integer-second window includes the threshold timestamp. This is pinned host evidence awaiting a Catena policy choice. |
| SU-I03 | A: link the existing managed broker before acknowledging child startup; B: start detached and link afterward; C: supervise its user worker directly; D: reuse raw spawn as a hidden supervisor. | **A.** The narrow adapter preserves managed cleanup and closes the start/link race. The typed description and artifact boundary remain separate work. |
| SU-I04 | A: count a sibling-triggered restart as one policy event and exclude temporary children; B: restart temporary children anyway; C: count each restarted sibling independently; D: silently change all policies to permanent. | **A.** This matches the selected OTP policy matrix while preserving declared child order. |

## Evidence so far

The [pinned primary source note](../30-sources/erlang-otp-29-supervision.md)
records the consulted documentation and implementation. Four independent-model
tests pass: strategy stop/start order, temporary/transient policies, stale
generations, exact restart-window threshold, storm termination, explicit stop
and malformed descriptions. The model is experimental and is not language
admission.

Native experiments add a linked managed startup path and narrow supervisor
callback. Typed child-description checking, generation-local capability
provisioning, deterministic artifact generation, startup/restart failure,
bounded nested-tree shutdown, full regression and normative publication remain
required before closing the [planned G089 gate](../20-notes/language-completion-plan-semantics.md#item-089-supervision-g089).

## Checked description and native progress

Three native OTP tests pass for the strategy matrix and ordered cleanup,
temporary/transient completion, and restart storms. Two description tests pass:
a verified Catena actor compiles to deterministic child specifications and
restarts after a typed trap; malformed signatures, duplicate IDs, captured
provisioning and invalid shutdown budgets are rejected before compilation.
The checked-description compiler is still explicitly experimental and does not
register a semantic revision or claim complete G089 admission.

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| SU-I05 | A: begin with zero-argument checked process entries and explicit fresh-empty provisioning; B: persist arbitrary host closures; C: inherit active scope handles across restarts; D: cast an arbitrary function to an OTP child. | **A.** Each generation evaluates the checked process body in its own new managed context. Wider checked provisioning remains a deliberate extension; inherited handles are rejected. |
| SU-I06 | A: use cancellation-instrumented managed actor bodies; B: compile plain raw receives; C: forward supervisor messages into the user mailbox; D: force-kill every child immediately. | **A.** Existing function-entry and managed-receive checkpoints compose with cleanup before the bounded shutdown fallback. |
| SU-I07 | A: require explicit positive native shutdown budget strictly above cooperative grace; B: inherit OTP defaults; C: allow indefinite child shutdown; D: treat resource exhaustion as successful cleanup. | **A.** Both budgets are visible and validated. The scheduler cannot promise a hard wall-clock completion bound; forced termination must retain its classification. |

Startup rollback and forced-shutdown experiments follow these passing cases.
No feature branch has been committed, published or merged for G089 yet.

## Managed ownership integration

The native adapter now starts supervisors from the managed broker, so a tree's
exit reaches the existing relationship observation or cooperative stop path
instead of killing the user worker directly. Broker completion joins owned
supervisors first. A regression exposed `gen_server.stop` exiting with the bare
`noproc` atom for an already-dead supervisor; joining now accepts that exact
terminal condition without replacing the owner's result. Explicit test handshakes
also ensure observation begins while the managed owner is live.

The selected native cases now include startup rollback, immediate repeated
startup failure, zero-grace forced termination of a noncooperative worker,
managed observation of tree loss and child cleanup before owner completion.
These remain experimental ownership evidence; integration with entry/package
metadata and exact selected artifact admission is still outstanding.

## Final implementation decisions

| Decision | Four alternatives explored | Recommended and selected |
| --- | --- | --- |
| SU-I08 | A: attach roots to the managed broker; B: link the user worker directly; C: detach every root; D: treat root failure as an algebraic effect. | **A.** Existing trapping/observation and cooperative stop paths retain failure ownership. |
| SU-I09 | A: join owned roots before owner completion using bounded static worker shutdowns; B: publish owner completion immediately; C: race a second root timer against child cleanup; D: silently leave roots alive. | **A.** The root join itself introduces no competing cutoff; each worker has an explicit finite budget. Arbitrary nested supervisor callbacks are excluded. |
| SU-I10 | A: support static managed workers and enumerate excluded OTP facilities; B: accept arbitrary nested child-spec maps; C: add dynamic callbacks without typing; D: reject supervision until every OTP facility is modelled. | **A.** This delivers the selected restart matrix with a concrete cleanup contract. Nested supervisor descriptions, significant children, registration and hot upgrades require later admission. |
| SU-I11 | A: extend the existing entry validator with the supervised-process role and bind origin/core/description/artifact digests; B: trust module display names; C: accept any exported zero-arity host function; D: alter existing signed interface formats. | **A.** Checked artifact loading rejects mismatched provenance and bytes while retaining historical formats. Capability checks inspect the entry boundary, not locally handled rows inside the body. |
| SU-I12 | A: exact 0.1.56 descriptor selection; B: retag the producer core; C: silently widen 0.1.52 source; D: omit artifact selection. | **A.** Producers stay at their verified managed-task revisions and generated supervision artifacts identify the new boundary. |
| SU-I13 | A: verify the manifest against deterministic regeneration before loading; B: trust a supplied hash alone; C: trust filenames; D: treat the build manifest as a signed proof. | **A.** This is a pinned build binding, not authenticity or remote serialization. |

The [normative contract](../60-specification/typed-supervision/checked-trees-and-lifecycle.md)
now states the supported inventory and eight traced obligations. The earlier
workbench sections preserve the sequence of experiments; their pending statements
are historical. General foreign calls and callbacks remain incomplete: the narrow
OTP lifecycle admission earns P096 partial status, not completion. No public
source or library vocabulary was adopted.

## Final verification and immutable implementation

Compiler commit [`36a668d3808885d1e6e9c6b2af5381bb0969f7f1`](https://github.com/pcharbon70/catena/commit/36a668d3808885d1e6e9c6b2af5381bb0969f7f1)
contains the implementation and tests. `mix test` passed **823 tests**;
`MIX_ENV=prod mix compile --warnings-as-errors`, `mix escript.build`,
`mix format --check-formatted` and `git diff --check` passed. The local transcript
is `/tmp/catena-supervision-regression.log`; retained test warnings and deliberate
trap-process logs remain expected.

Archive validation passed with 606 documents, 68 directories, 120 source notes,
182 specification chapters and 775 obligations. The checklist records
**95 complete, 30 partial, 14 gaps and 2 deferred**. C089 consumes `0.1.56`;
P096 now records its completed narrow lifecycle prerequisite while general
foreign calls/callbacks remain open. The next semantic patch is `0.1.57`.
No automation or scheduled continuation was used.
