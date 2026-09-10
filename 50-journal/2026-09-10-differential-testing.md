---
title: "2026-09-10 Differential Testing"
kind: journal
created: "2026-09-10"
tags: [specification, testing, conformance, semantics]
aliases: []
---

# 2026-09-10 Differential Testing

## Scope

Execute [P134](../20-notes/language-completion-plan-delivery.md#item-134-differential-testing)
at revision `0.1.85`. CP-134-1..3 retain their recommended selections. The
`0.1.50` closed capability-kernel and comprehension target already restored
C050, C053, and C057, so no prerequisite repair remained. C122 supplies the
runner and C133 supplies the observation schema. Public source remains held by
P109.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| DF-I01 Scenario representation | A source strings; B portable semantic descriptors; C BEAM instructions; D executable closures | B: descriptors are stable and do not pre-empt P109. |
| DF-I02 Oracle independence | A reuse lowering; B independent reference adapters; C compare two compiler modes; D snapshots | B: correlated backend defects do not define expected behavior. |
| DF-I03 Generated domains | A bytes; B typed kernel and comprehension descriptors; C every feature immediately; D fixed fixtures only | B: admitted valid programs exercise composition without inventing syntax. |
| DF-I04 Boundary coverage | A randomize host resources; B retained deterministic boundary scenarios; C omit boundaries; D mock only production | B: effects, schedules, resources, foreign values, and cancellation keep explicit models. |
| DF-I05 Observation shape | A printed output; B declared C133 projection; C internal states; D final value only | B: compare exactly the behavior promised by the owning rules. |
| DF-I06 Deterministic comparison | A fuzzy equality; B exact canonical equality; C retry mismatches; D normalize all order away | B: promised value and order differences remain visible. |
| DF-I07 Nondeterminism | A exact host schedule; B finite allowed observation set; C accept any result; D retry until match | B: permitted alternatives remain bounded by normative semantics. |
| DF-I08 Terminal classes | A collapse to failure; B preserve rejection, trap, exhaustion, timeout, unsupported; C compare messages; D ignore terminal | B: tooling limits cannot masquerade as language outcomes. |
| DF-I09 Invalid probes | A mix into valid generation; B separate named mutations; C discard; D compile random terms | B: generator soundness and hostile comparator testing answer different questions. |
| DF-I10 Seeds | A wall clock; B C122-derived deterministic seeds; C global RNG; D one hard-coded program | B: unchanged subjects replay the same ordered corpus. |
| DF-I11 Mutation families | A value only; B value, event order, callback count, cancellation; C source whitespace; D performance only | B: the four families target distinct observable contracts. |
| DF-I12 Shrinking | A host term size; B stable domain-preserving shrink; C no shrink; D invalid smaller terms | B: minimized witnesses remain programs in the claimed domain. |
| DF-I13 Corpus identity | A filename; B source/toolchain/scenario/observation digests; C timestamp; D issue URL | B: a witness stays attributable and tamper-evident. |
| DF-I14 Corpus lifecycle | A delete after repair; B retain minimized regressions; C retain every run; D overwrite latest | B: repaired defects remain executable distinguishing cases. |
| DF-I15 Bounds | A one timeout; B separate generation, fuel, schedule, shrink, host limits; C unbounded; D retry budget | B: every partial result states why exploration stopped. |
| DF-I16 Unsupported scope | A silently skip; B explicit unsupported outcome; C count as pass; D infer support | B: coverage gaps stay observable. |
| DF-I17 Proof wording | A agreement proves compiler; B finite-evidence disclaimer; C imply preservation; D omit scope | B: testing does not discharge C132's proof obligation. |
| DF-I18 Public vocabulary | A invent syntax; B internal descriptors pending P109; C adopt Elixir AST; D expose kernel syntax as final | B: semantic validation proceeds without freezing the language surface. |

## Results

Compiler [PR 168](https://github.com/pcharbon70/catena/pull/168) merged feature
commit `1083d18` as merge commit
`75a330b93954d9b26fbb74331422d2139b86ca08` into `rewrite`.
`Catena.Reference.Differential` compares exact projections and allowed finite
sets, detects four injected fault families, verifies a digest-bound retained
corpus, and runs deterministic typed generation through C122. The test support
uses independent C010 stepper and production BEAM adapters for kernel and
comprehension descriptors.

Nine focused tests cover retained cross-feature and foreign boundaries, 64
seeded generated programs, all mutation families, nondeterministic schedule
sets, unsupported scope, domain-preserving shrinking, corpus tampering, and
lifecycle/profile disclosure. The complete suite passes 1,106 tests. Production
compilation with warnings as errors, production escript construction, trust
inventory audit, and diff checks pass. The
[normative contract](../60-specification/differential-testing/generated-and-adversarial-agreement.md)
promotes P134 to C134 without a proof claim or public syntax selection.
