---
title: "Isolated Seeded and Scoped Runs"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.84"
tags: [specification, testing, conformance, tooling]
aliases: []
---

# Isolated Seeded and Scoped Runs

## Status and authority

C122 defines revision `0.1.84` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It completes the
[G122 plan](../../20-notes/language-completion-plan-delivery.md#item-122-testing-tools)
over C006 governed evidence, C010 semantic boundaries, C121 builds, and C133
reference observations. It introduces no public language or test vocabulary;
P109 and P107 retain that decision (`TT-OBL-001`).

## Plans, subjects, and identities

A test suite MUST have a nonempty stable identifier, exact language-contract
revision, explicit nonnegative seed, positive host deadline, exact 256-bit
subject digest, and at least one test case. Test identifiers within a suite MUST
be unique (`TT-OBL-002`).

The canonical plan identity MUST bind suite identity, contract, subject digest,
seed, host deadline, ordered case identities, result kinds, declared effects,
and case bounds. Executable callbacks are local mechanisms and MUST NOT enter
the portable plan identity (`TT-OBL-003`).

A runner MUST refuse a plan when its supplied subject digest differs from the
plan subject, when the canonical plan has changed, or when an identity or bound
is malformed. It MUST NOT run zero tests as a successful empty observation
(`TT-OBL-004`).

## Result kinds and evidence scope

The result kinds are `unit`, `law`, `property`, `model`, `concurrency`, and
`specification`. A report MUST preserve each kind and MUST NOT collapse them
into one undifferentiated Boolean claim (`TT-OBL-005`).

A report MUST identify the plan and subject, retain the explicit suite seed,
list every case result in plan order, state its finite observation scope, and
carry a canonical report digest. Passing observations MUST NOT be labelled as
proof (`TT-OBL-006`).

Evidence MUST use portable finite values. A process identifier, reference,
port, executable function, floating-point value, unsafe integer, or another
host-only carrier in evidence makes that case invalid rather than silently
serializing an implementation detail (`TT-OBL-007`).

A `specification` result MUST carry the exact tested subject digest. Missing or
different subject identity is stale governed evidence and MUST fail the case
(`TT-OBL-008`).

## Seeds, generation, and shrinking

Property generation MUST derive each case and observation seed
deterministically from the explicit suite seed, stable case identity, and
observation index. Repeating an unchanged plan and subject MUST reproduce the
same generated observations and report (`TT-OBL-009`).

A generated value MUST satisfy its declared domain predicate before the
property runs. An out-of-domain generated value is an invalid generator result,
not a counterexample (`TT-OBL-010`).

After a property failure, the runner MUST examine shrink candidates in a stable
order and MUST discard candidates outside the declared domain. Every reported
counterexample MUST therefore remain in the admitted generated domain
(`TT-OBL-011`).

Shrinking MUST have a positive explicit or profiled step limit. When another
failing in-domain candidate exists at that limit, the runner MUST report
`shrink_bound`, preserve the best counterexample found, and mark it nonminimal.
It MUST NOT claim minimality merely because tool resources ended
(`TT-OBL-012`).

## Isolation, effects, and cleanup

Each case MUST execute in a distinct runner-owned task scope. Children created
through that scope MUST be terminated before the runner returns the case
result, including after failure, exhaustion, crash, or host timeout
(`TT-OBL-013`).

Cases MUST declare the effects they intend to observe through the runner
context. The report MUST preserve observed effects in order. An observed effect
outside the declaration MUST fail the case (`TT-OBL-014`).

> **Implementation-defined choice.** The runner context accounts for effects
> and owns children created through its supplied interfaces. Revision `0.1.84`
> does not claim that arbitrary host callbacks are sandboxed; deployments MUST
> treat those callbacks as trusted test code (`TT-OBL-015`).

## Bounds and outcomes

Semantic-fuel exhaustion, schedule exploration exhaustion, shrink exhaustion,
and a host wall-clock deadline are distinct outcomes. A host timeout MUST NOT be
reported as language divergence, a trap, semantic-fuel exhaustion, or schedule
exhaustion (`TT-OBL-016`).

> **Implementation-defined choice.** Implementations publish positive maximum
> host milliseconds, property observations, generator size, and shrink steps.
> Reports retain the applied value for every relevant bound, and partial
> evidence survives exhaustion (`TT-OBL-017`).

## Diagnostics and conformance

Conformance tests MUST cover every result kind; deterministic reproduction;
typed generation and shrinking; minimal and explicitly nonminimal
counterexamples; zero-test refusal; stale and tampered subjects; invalid and
stale evidence; declared and undeclared effects; runner-owned child cleanup;
semantic-fuel, schedule, shrink, and host bounds; lifecycle registration;
conformance disclosure; and trust classification (`TT-OBL-018`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-testing-tools.md)
records the planned forks, additional four-way decisions, compiler identity,
and verification. The [reference evaluator](../reference-evaluator/README.md)
supplies common semantic observations; P134 will consume this runner for
systematic differential evidence without changing the result-kind or proof
boundary.
