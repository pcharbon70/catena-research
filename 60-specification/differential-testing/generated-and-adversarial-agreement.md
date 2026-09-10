---
title: "Generated and Adversarial Agreement"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.85"
tags: [specification, testing, conformance, semantics]
aliases: []
---

# Generated and Adversarial Agreement

## Status and authority

C134 defines revision `0.1.85` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[P134 plan](../../20-notes/language-completion-plan-delivery.md#item-134-differential-testing)
over C010 semantics, C122 testing tools, and C133 reference observations. The
closed comprehension target at `0.1.50` already repaired P050, P053, and P057.
This chapter introduces no public source vocabulary; P109 retains that decision
(`DF-OBL-001`).

## Differential scenarios

A differential scenario MUST bind an exact language contract, a portable
semantic descriptor, a nonempty declared observation projection, a comparison
mode, and positive execution bounds. Unsupported descriptors MUST produce an
explicit unsupported outcome and MUST NOT be omitted or counted as agreement
(`DF-OBL-002`).

The reference path and production path MUST be structurally independent at the
operation under comparison. A generator MUST NOT obtain expected behavior from
production lowering, generated BEAM, or the production result
(`DF-OBL-003`).

The admitted generated domains at this revision are typed-kernel arithmetic and
bounded list-comprehension filtering and mapping. Retained scenarios cover
effects, schedules, resource lifetimes, foreign values, cancellation, and
cross-feature programs. Public-source generation remains unsupported until
P109 supplies a grammar (`DF-OBL-004`).

## Declared observations

Before execution, each scenario MUST declare which common C133 fields it
compares. The comparison MUST use canonical portable values for status, value,
kinded terminal, ordered events, lifetime state, or bound outcome as applicable;
it MUST NOT compare presentation strings or internal machine states
(`DF-OBL-005`).

Deterministic semantics MUST use exact equality over the declared projection.
An implementation MUST NOT weaken a deterministic mismatch into permitted
variability (`DF-OBL-006`).

A nondeterministic scenario MAY use a finite allowed-observation set only when
the governing normative semantics permit every member. An observed value
outside that set is a mismatch; absence of an observed permitted alternative is
not evidence that the alternative is impossible (`DF-OBL-007`).

Comparison MUST preserve kinded distinctions among rejection, trap, semantic
fuel exhaustion, schedule exhaustion, shrink exhaustion, host timeout, and an
unsupported model (`DF-OBL-008`).

## Generation and adversarial mutation

Every generated descriptor MUST pass its typed and effect-aware domain
predicate before either execution path runs. Invalid boundary probes MUST be
identified as mutations and MUST NOT be presented as valid generated programs
(`DF-OBL-009`).

Generation MUST be reproducible from the C122 plan identity and explicit seed.
An unchanged subject and plan MUST reproduce the same ordered descriptors and
observations (`DF-OBL-010`).

The adversarial suite MUST include distinguishable mutations of returned value,
ordered events, callback multiplicity, and cancellation outcome. A comparator
that accepts one of those injected mismatches is nonconforming
(`DF-OBL-011`).

Generated failures MUST shrink through stable candidates that remain inside the
original semantic domain. Exhausted shrinking MUST retain the best witness and
state that it is nonminimal (`DF-OBL-012`).

## Retained counterexamples

Every detected mismatch selected for the retained corpus MUST store its
minimized descriptor, mutation family, expected comparison mode, exact source
identity, toolchain digest, scenario digest, and observation digest
(`DF-OBL-013`).

Corpus verification MUST recompute every identity and reject altered, duplicate,
malformed, unminimized, or unknown-family entries. A repaired defect MUST retain
its counterexample as a regression witness (`DF-OBL-014`).

## Bounds, scope, and proof claims

> **Implementation-defined choice.** An implementation publishes positive
> maxima for generated cases, descriptor size, semantic fuel, explored
> schedules, shrink steps, and host milliseconds. Reports preserve the applied
> values and partial evidence when a bound is reached (`DF-OBL-015`).

Generated agreement establishes only the finite declared observations for the
tested subject, seeds, domains, retained cases, and bounds. It MUST NOT be
reported as a proof of compiler correctness, semantic completeness, progress,
preservation, or schedule fairness (`DF-OBL-016`).

An implementation claiming C134 MUST publish its admitted generated domains,
retained boundary families, comparison modes, adversarial mutation families,
counterexample limit, public-source status, and proof disclaimer in its
machine-readable conformance profile (`DF-OBL-017`).

## Diagnostics and conformance

Conformance evidence MUST cover deterministic cross-feature agreement; seeded
typed generation; empty and nested comprehensions; a checked foreign-value
boundary; allowed-set schedule comparison and rejection; all four adversarial
families; domain-preserving minimization; unsupported scenarios; corpus identity
and tampering; lifecycle selection; trust inventory; and finite evidence scope
(`DF-OBL-018`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-differential-testing.md)
records the planned forks, additional four-way decisions, compiler identity,
and verification. Compiler PR 168 implements the common comparator, independent
semantic generators, retained counterexample corpus, and nine focused cases;
the complete compiler suite contains 1,106 passing tests.
