---
title: "2026-09-10 Scheduler Observability"
kind: journal
created: "2026-09-10"
tags: [specification, concurrency, runtime, implementation-limits]
aliases: []
---

# 2026-09-10 Scheduler Observability

## Scope

Execute [P090](../20-notes/language-completion-plan-semantics.md#item-090-scheduler-observability-p090)
from compiler C085 merge `2a5592f73d1488a7b9ddda0b7bbdb286e476f61a`.
Revision `0.1.78` is covered by the user's session-wide approval. CP-090-1..3
retain their recommended selections.

## Implementation decisions

| Decision | Four alternatives | Recommended and selected |
| --- | --- | --- |
| SC-I01 Schedule contract | A deterministic; B round-robin fair; C nondeterministic permitted transitions; D expose host order | C: it matches the kernel and keeps liveness claims honest. |
| SC-I02 Reduction visibility | A exact counts; B ratios; C no program observation; D one count per expression | C: backend accounting can evolve without changing values or artifacts. |
| SC-I03 Preemption | A fixed source-step threshold; B runtime-defined documented boundaries; C no preemption; D wall-clock language rule | B: implementations disclose behavior while preserving semantics. |
| SC-I04 Priorities | A absent; B deployment classes without semantic guarantees; C deterministic order; D payload-selected | B: operational tuning remains explicit and cannot alter typing or message order. |
| SC-I05 Work taxonomy | A all preemptible; B preemptible/scheduled-blocking/unsafe-unbounded; C foreign equals unsafe; D infer from duration | B: each admitted route receives an actionable exact class. |
| SC-I06 Unknown work | A normal scheduler; B refuse; C run and warn; D unlimited thread | B: missing declarations cannot silently create scheduler starvation. |
| SC-I07 Trusted BEAM | A normal caller; B owned process; C dirty NIF; D inline callback | B: the existing adapter isolates waits and owns cancellation. |
| SC-I08 Native services | A one class; B port OS process and NIF dirty CPU under signed declarations; C raw NIF; D forbid both | B: existing C098 packaging and cleanup remain binding. |
| SC-I09 Worker capacity | A unbounded; B explicit 1..1,024; C global hidden; D block admissions forever | B: exhaustion is observable and does not start work. |
| SC-I10 Capacity tokens | A decrement by caller claim; B fresh tokens and exact one release; C timeout inference; D no release | B: forged or repeated release cannot create capacity. |
| SC-I11 Explorer | A one canonical schedule; B bounded exhaustive choices; C random only; D runtime trace only | B: multiple outcomes and incomplete bounds stay explicit. |
| SC-I12 Blocking evidence | A timing benchmark; B owned blocking call plus independent runnable signal; C code inspection only; D sleep on main process | B: it directly shows isolation while making no fairness or latency claim. |

## Verification route

Exercise exact profile validation and false fairness mutation; Catena, trusted
foreign, port, NIF, unknown and unsafe work classes; exact one-worker exhaustion;
valid, forged and repeated release; independent progress beside a blocking
foreign worker; multiple reference schedules and evidence-bound exhaustion;
retained local message ordering and native service tests.

## Results

The compiler adds an exact scheduler profile and a bounded pure policy model.
Five focused scheduler tests pass with retained kernel, message, foreign, native,
resource, lifecycle, version, and trust evidence as part of the complete compiler
suite: 1,057 tests pass. Production compilation with warnings as errors,
escript construction, and the reviewed trust-boundary audit also pass. The
[normative contract](../60-specification/scheduler-observability/policy-classes-and-visible-limits.md)
promotes P090 to C090 without a deterministic schedule or universal liveness
claim. Compiler pull request
[160](https://github.com/pcharbon70/catena/pull/160) merged feature commit
`8fc5d6e578c9417a865ec5fdb1699ab411182c5c` as
`747d6340c271f8d60a15dcf15f71d3be37e54823` into `rewrite`.
