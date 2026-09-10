---
title: "2026-09-10 Debugging and Observability"
kind: journal
created: "2026-09-10"
tags: [specification, debugging, observability, tooling]
aliases: []
---

# 2026-09-10 Debugging and Observability

## Scope

Execute [G124](../20-notes/language-completion-plan-delivery.md#item-124-debugging-and-observability)
at revision `0.1.89`. CP-124-1..3 retain their recommendations: adapt real
BEAM execution through verified Catena origins, disclose trace perturbation
and loss, and navigate erased evidence externally under default redaction.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| DO-I01 Runtime | A raw BEAM debugger; B Catena adapter over verified sidecars; C custom VM; D simulation only | B: real execution keeps Catena source meaning. |
| DO-I02 Session authority | A global debugger; B owner-bound opaque capability; C ambient process dictionary; D unauthenticated PID | B: control expires with its owner and rejects cross-owner operations. |
| DO-I03 Breakpoint identity | A host line; B verified sidecar node; C function name only; D text search | B: artifact and original-source identity stay bound. |
| DO-I04 Suspension | A arbitrary VM stop; B explicit cooperative checkpoint; C polling; D fake pause | B: the current bootstrap provides deterministic control without a custom VM. |
| DO-I05 Continuation | A auto-resume; B explicit pause token; C restart program; D global continue | B: the owner resumes one exact suspension. |
| DO-I06 Stack mapping | A host frames only; B verified Catena frames with optional technical frames; C guessed paths; D hide stacks | B: useful source stacks keep unknown frames honest. |
| DO-I07 Process identity | A raw PID as portable; B opaque session-local identity; C process name only; D omit actors | B: relations remain visible without promising host identity. |
| DO-I08 Message visibility | A payloads always; B semantic outcome with redacted payload; C no messages; D mailbox dump | B: message behavior stays inspectable without ambient disclosure. |
| DO-I09 Event inventory | A failure only; B closed minimum across calls, handlers, actors, foreign work, cancellation, derivation; C arbitrary strings; D host trace terms | B: admitted semantics receive stable categories. |
| DO-I10 Buffer pressure | A unbounded; B finite drop-oldest with exact loss; C silent loss; D block program forever | B: resource use and incompleteness are explicit. |
| DO-I11 Timing claim | A tracing never perturbs; B declare perturbation and nonsemantic host-relative time; C remove time; D portable latency | B: profiles remain useful without false semantic promises. |
| DO-I12 Profile attribution | A aggregate wall time; B node-and-kind groups with counts and observation interval; C sample profiler only; D source line guesses | B: attribution uses verified origins and bounded evidence. |
| DO-I13 Crash reason | A raw term; B class plus redacted reason, frames, and trace; C stringified exception; D exit silently | B: reports preserve failure class and context without secret leakage. |
| DO-I14 Value disclosure | A always inspect; B redacted default with explicit typed bounded codec; C debugger grants secret access; D hash every value | B: debug authority adds no application authority. |
| DO-I15 Erased declarations | A load for inspection; B external verified locator and digest; C omit all navigation; D reconstruct from BEAM | B: C113 erasure stays intact while source evidence remains navigable. |
| DO-I16 Stripped and generated code | A guess sources; B label unavailable and retain verified derivation links; C pretend generated code is handwritten; D forbid stripped builds | B: source claims match retained evidence. |

## Executed evidence

Compiler [PR 173](https://github.com/pcharbon70/catena/pull/173) merged feature
commit `0e281f4` as merge commit
`76da84f395cf1cdba1a637762e688bdff94c3f17` into `rewrite`.
Compiler [PR 174](https://github.com/pcharbon70/catena/pull/174) then merged
feature commit `154374a` as merge commit
`b4389b41f073efd768a0916610776c9a90d00777`, publishing the closed event
inventory and executable unavailable-value and generated-derivation evidence.
`Catena.Tool.Debugger` verifies the executable and P100 sidecar before opening
an owner-bound session. An actual compiled Catena module pauses at a verified
checkpoint, resumes through its exact pause token, traps, and produces mapped
redacted frames. Additional cases cover two-event overflow, stable event
identity, process pseudonyms, message payload redaction, grouped profiles,
event-size refusal, stripped origins, cross-owner control, owner death, closed
sessions, explicit optimized-value unavailability, generated derivation, and
external evidence lookup.

The complete compiler suite passes with 1,128 tests. Production compilation
with warnings as errors, escript construction, trust-inventory verification,
and `git diff --check` pass. The
[normative contract](../60-specification/debugging-and-observability/source-aware-bounded-debug-sessions.md)
makes G124 complete without adopting P107 vocabulary or P109 grammar.
