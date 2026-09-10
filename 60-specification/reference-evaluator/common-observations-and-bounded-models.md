---
title: "Common Observations and Bounded Models"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.83"
tags: [specification, formal-semantics, conformance, testing]
aliases: []
---

# Common Observations and Bounded Models

## Status and authority

C133 defines revision `0.1.83` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[P133 plan](../../20-notes/language-completion-plan-delivery.md#item-133-reference-evaluator)
over C010's formal kernel, C132's stated proof targets, and every presently
admitted semantic boundary. It introduces no public language vocabulary and does
not claim the outstanding composition proof (`RE-OBL-001`).

## Observation contract

A reference observation records an exact format revision, engine, status, value
or reason, ordered events, lifetime summary, and the bounds used for that run.
Absent fields remain explicit empty or null values rather than changing the
record shape (`RE-OBL-002`).

The statuses are `completed`, `trapped`, `exited`, `cancelled`, `quiescent`,
`budget_exhausted`, `host_timeout`, `rejected`, and `unsupported`. A consumer
cannot equate statuses or infer one from another (`RE-OBL-003`).

The common layer adapts existing independently structured machines. It cannot
call generated BEAM output as its reference oracle, replace layer-specific
validation, or require equality of internal implementation states
(`RE-OBL-004`).

## Semantic engines

The expression engine reports the resulting value and exact evaluation steps
under a semantic fuel limit. Exhausting fuel reports `budget_exhausted`; an
unknown definition or malformed expression reports `rejected` (`RE-OBL-005`).

The effect engine preserves the ordered handler trace, including handle,
request, clause, resume, and return observations. A harness host deadline reports
`host_timeout` and is not evidence of semantic divergence (`RE-OBL-006`).

The kernel engine preserves value or kinded terminal reason, actor trace, process
lifetime states, and semantic step count. Waiting actors produce `quiescent`;
fuel exhaustion cannot be relabelled as a trap or completed value
(`RE-OBL-007`).

The schedule engine reports the complete distinct outcome set reached within
published transition and configuration limits. Reaching either bound reports
`budget_exhausted` with the partial explored set and cannot imply that an
unobserved schedule is impossible (`RE-OBL-008`).

## Boundary models

The resource engine explores enabled lifecycle transitions and reports terminal
scope phases, resource states, primary outcomes, cleanup results, and owner-loss
status. It does not execute production cleanup callbacks or erase release
failures (`RE-OBL-009`).

The foreign engine passes native values through the declared C095 checked codec
and its depth, node, and byte limits. An invalid carrier or exceeded limit reports
`rejected`; successful conversion returns the semantic value without granting
foreign authority (`RE-OBL-010`).

External time, randomness, network, process, and filesystem responses use an
explicit finite response catalog. A missing request is `unsupported`; declared
traps, exits, host deadlines, and values retain distinct statuses
(`RE-OBL-011`).

## Source and model coverage

The source engine can elaborate the retained formal-kernel syntax through its
checked boundary and then invoke the kernel engine. Malformed retained source is
`rejected` (`RE-OBL-012`).

> **Implementation-defined choice.** Public-source evaluation is `unsupported`
> while P109 remains held. A future source adapter must use the shared approved
> parser and elaborator and produce the same observation schema; it cannot invent
> grammar through the reference layer (`RE-OBL-013`).

An unknown engine or a known engine with malformed input produces explicit
`unsupported` or refusal. The harness cannot silently skip a requested model,
drop a failed case, or substitute a production-only result (`RE-OBL-014`).

## Bounds, evidence, and proof status

> **Implementation-defined choice.** An implementation publishes maximum
> semantic fuel, host deadline, schedule transitions, schedule configurations,
> resource events, and external responses. Every observation reports the applied
> bounds, and exhaustion preserves available partial evidence (`RE-OBL-015`).

Coverage spans the retained data, condition, effect, process, resource, task,
foreign-value, failure, and schedule machines through their existing checked
cores and adapters. Later public syntax extends only the source route; it does
not reopen the model observation contract (`RE-OBL-016`).

Agreement among a reference observation, another model, and generated BEAM is
bounded conformance evidence. It cannot discharge C132's composition lemma or
turn a tested finite schedule into a universal theorem (`RE-OBL-017`).

## Diagnostics and conformance

Tests MUST cover pure values and fuel exhaustion; handled-effect event order;
kernel values, traps, quiescence, and malformed core; complete and exhausted
schedule exploration; successful and failed resource cleanup; valid and invalid
foreign values; abstract values, traps, exits, host deadlines, and absent
external responses; retained source acceptance and rejection; the P109 public
source hold; lifecycle registration; conformance reporting; and trust
classification (`RE-OBL-018`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-reference-evaluator.md)
records the planned forks, additional four-way decisions, implementation, and
verification. The [formal-kernel map](../../10-maps/formal-semantic-kernel.md)
and [progress-and-preservation map](../../10-maps/progress-and-preservation.md)
connect these finite observations to their operational rules and separate proof
obligations.
