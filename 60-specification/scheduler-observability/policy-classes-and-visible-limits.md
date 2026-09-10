---
title: "Policy Classes and Visible Limits"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.78"
tags: [specification, concurrency, runtime, implementation-limits]
aliases: []
---

# Policy Classes and Visible Limits

## Status and authority

C090 defines revision `0.1.78` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[reviewed scheduler plan](../../20-notes/language-completion-plan-semantics.md#item-090-scheduler-observability-p090)
through checked internal policy and profile APIs without selecting public source
vocabulary (`SC-OBL-001`).

## Observable schedule semantics

Runnable-process selection is nondeterministic. Every execution must be one
permitted C010 transition sequence, preserve C085 per-sender message order, and
preserve each applicable effect, resource, cancellation, and failure rule.
Scheduling policy cannot change a value, retarget or mutate a message, duplicate
an effect, revive a terminal process, or bypass authority (`SC-OBL-002`).

No conforming program can observe or depend on a runtime reduction counter,
timeslice boundary, run-queue position, scheduler identifier, migration event,
or physical core. Those details do not enter value equality, traces, interface
identity, or artifact identity (`SC-OBL-003`).

The language promises neither deterministic scheduling nor fairness,
starvation-freedom, bounded latency, progress for every runnable process, or a
fixed interleaving. Quiescence means that the modeled configuration has no
runnable process; it does not prove that an external service will respond or
that a deployment will remain alive (`SC-OBL-004`).

## Preemption and priorities

The runtime can use reductions, elapsed work, allocation, explicit yields, or
other internal signals to preempt execution. A conforming implementation must
eventually yield at every operation that it documents as a preemption boundary,
but the numeric threshold and exact instruction accounting are not language
observations (`SC-OBL-005`).

> **Implementation-defined choice.** The bootstrap supports deployment priority
> classes `low`, `normal`, and `high`; the default is `normal`. Implementations
> disclose supported classes and their relative scheduling policy. Priority can
> affect opportunity and latency but cannot weaken typing, authority, message
> order, cleanup, capacity, or delivery outcomes. No priority class receives a
> fairness or deadline guarantee (`SC-OBL-006`).

## Foreign-work classes

Every admitted execution unit has exactly one scheduler class:

| Class | Required behavior |
| --- | --- |
| `preemptible` | Verified Catena work remains under the ordinary runtime scheduler and its documented preemption points. |
| `scheduled_blocking` | Work executes through a declared owned process, dirty scheduler, or isolated OS process under an explicit finite admission capacity. |
| `unsafe_unbounded` | Work lacks an adequate preemption, isolation, or finite admission contract and is refused by the supported profile. |

An unknown or malformed declaration has no default class and is refused before
execution. A label supplied by an application payload cannot classify its own
work (`SC-OBL-007`).

C096 trusted BEAM calls use `scheduled_blocking` through owned worker processes
with cooperative cancellation. C098 ports use isolated OS processes and NIFs
use their required dirty CPU scheduler. Their signed package/declaration,
scheduler, trust, timeout, work-unit, cancellation, and cleanup checks remain
mandatory. Classification does not make host code safe or truthful
(`SC-OBL-008`).

## Capacity and blocking isolation

Scheduled blocking work consumes one slot in an explicit positive worker
capacity before starting. At the configured limit, further work returns
`foreign_worker_capacity_exhausted` and does not start. Releasing a valid token
returns one slot; forged and repeated release are refused (`SC-OBL-009`).

An owned blocking worker does not make unrelated runnable Catena processes wait
for the foreign result. Its caller can remain awaiting the explicit foreign
outcome while another runnable process advances. This is isolation from the
blocking call, not a fairness or maximum-latency promise (`SC-OBL-010`).

> **Implementation-defined choice.** The bootstrap accepts between 1 and 1,024
> scheduled foreign workers per explicit policy. A deployment selects its
> positive capacity and priority class. Invalid options are refused rather than
> silently replaced (`SC-OBL-011`).

## Reference exploration and evidence

Bounded exhaustive exploration enumerates every runnable-process choice until
quiescence or an explicit transition/configuration evidence bound. Reaching an
evidence bound returns `exhausted`, not a language failure and not proof that
other schedules do not exist. Exploration preserves multiple permitted
cross-sender outcomes and makes no fairness claim (`SC-OBL-012`).

Empirical runtime traces can demonstrate supported behavior or expose a defect;
one run cannot establish that a different permitted schedule is impossible.
Absolute timings, runtime reduction counts, or observed priority ratios are
deployment evidence rather than portable semantic constants (`SC-OBL-013`).

## Diagnostics and conformance

The machine profile MUST disclose revision, deterministic-scheduling and
fairness status, reduction-preemption and observability status, supported
priorities, priority semantics, the three work classes, unsafe-unbounded
admission, and the foreign-worker ceiling. Tests MUST cover profile mutation,
multiple explored schedules, evidence-bound exhaustion, exact foreign/native
classification, unknown and unsafe refusal, worker-capacity exhaustion, token
release, independent progress beside a blocking worker, and retained message
order (`SC-OBL-014`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-scheduler-observability.md)
records twelve four-way decisions and executable evidence. The
[OTP runtime-control note](../../30-sources/erlang-otp-29-runtime-resource-controls.md)
grounds the separation among reductions, message storage, scheduler classes,
and deployment limits. The reference explorer enumerates bounded semantic
choices; the BEAM witnesses test implementation behavior without promoting one
observed schedule into a universal theorem.
