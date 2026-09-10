---
title: "Checked Rewrites and Observation Preservation"
kind: specification
created: "2026-09-10"
status: normative
spec_version: "0.1.86"
tags: [specification, optimization, semantics, conformance]
aliases: []
---

# Checked Rewrites and Observation Preservation

## Status and authority

C135 defines revision `0.1.86` under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[P135 plan](../../20-notes/language-completion-plan-delivery.md#item-135-optimizer-validity)
over C004 law evidence, C010 verified core, C030 evaluation order, C133
observations, and C134 differential comparison. It introduces no public source
vocabulary; P109 retains that decision (`OZ-OBL-001`).

## Transformation inventory and selection

An implementation MUST publish each transformation that can alter a checked
program between elaboration and execution, its owner, and whether it is a
semantic optimizer rule. Revision `0.1.86` classifies package specialization,
layout selection, condition lowering, comprehension expansion, and backend
lowering as separately verified elaboration or representation paths rather than
law-driven optimizer rules (`OZ-OBL-002`).

Optimization is disabled unless checked mode is explicitly selected. Disabled
mode MUST preserve the verified core exactly and MUST emit no rewrite
certificate (`OZ-OBL-003`).

Checked mode admits exactly `fold_integer_literals` and
`right_integer_identity`. An unknown, duplicate, or unavailable requested rule
MUST be rejected before transformation (`OZ-OBL-004`).

## Admitted rules and premises

`fold_integer_literals` replaces an `Int` addition, subtraction, or
multiplication whose two operands are integer literals with the exact
mathematical integer result. Its premises are verified typing, pure removed
literal evaluation, total integer operation, and preserved left-to-right order
(`OZ-OBL-005`).

`right_integer_identity` replaces `x + 0` or `x * 1` with `x`. The removed
right operand MUST be the checked literal, and the replacement MUST retain the
whole expression's recorded type, effect row, and source observation. The rule
does not remove, duplicate, or reorder evaluation of `x` (`OZ-OBL-006`).

The optimizer MUST traverse children before their parent and MUST apply rules
in the published stable order. Repeating an unchanged checked input, mode, and
rule set MUST produce the same output, certificates, refusals, and digests
(`OZ-OBL-007`).

A rule MUST NOT derive permission from a promised or tested categorical law
alone. C004 law observations are evidence about sampled values; they are not a
proof of purity, totality, termination, or contextual equivalence
(`OZ-OBL-008`).

## Verification and certificates

The inference-independent kernel verifier MUST accept the input before any
rewrite and the output after all rewrites. A failed input or output check makes
optimization fail without lowering (`OZ-OBL-009`).

Every applied rewrite MUST carry its rule, stable core path, input and output
expression digests, exact premise identifiers, and certificate digest. The
certificate sequence MUST replay from the original core to the claimed output
(`OZ-OBL-010`).

Certificate verification MUST recompute every digest and every local rewrite,
then reverify the replayed output. Missing, reordered, altered, unknown, or
inapplicable certificates MUST be rejected (`OZ-OBL-011`).

The compiler MUST lower only the replayed and independently reverified output.
When optimizer selection is explicit, build metadata MUST preserve mode, rule
set, input/output digests, certificates, and refusals (`OZ-OBL-012`).

## Refusal and observation preservation

Integer annihilation such as `0 * x` or `x * 0` is not admitted at this
revision when it would remove a nonliteral expression. The optimizer MUST
retain the expression and record that machine-checked purity and totality are
missing (`OZ-OBL-013`).

An enabled rewrite MUST preserve C133's declared value, kinded terminal,
ordered events, lifetime state, and termination or exhaustion behavior. It MUST
NOT remove or duplicate calls, callbacks, traps, requests, sends, resource
operations, cancellation, or potentially divergent evaluation
(`OZ-OBL-014`).

Debug provenance MUST remain attributable to the transformed whole expression.
Optimization MUST NOT fabricate a source span or treat generated code as user
source (`OZ-OBL-015`).

Large admitted expression trees MUST use the same stable rule and certificate
semantics as small trees. Implementation resource exhaustion is distinct from
a program trap or divergence and MUST NOT yield a partial executable
(`OZ-OBL-016`).

## Profile and evidence scope

An implementation claiming C135 MUST publish the modes, enabled and refused
rules, required premise classes, separate transformation inventory,
public-source status, and proof disclaimer in its machine-readable profile
(`OZ-OBL-017`).

Conformance evidence MUST cover disabled identity; positive literal and
right-identity rewrites; certificate replay and tampering; exact reference and
BEAM results before and after optimization; annihilation refusal with a trap or
call witness; exact-once call preservation; deterministic large trees; invalid
modes and rules; lifecycle selection; trust classification; and finite evidence
scope. Passing tests MUST NOT be reported as a general optimizer proof
(`OZ-OBL-018`).

## Rationale and evidence (non-normative)

The [implementation journal](../../50-journal/2026-09-10-optimizer-validity.md)
records the planned forks, additional four-way decisions, compiler identity,
and verification. Compiler PR 169 implements the checked path and nine focused
cases; the resulting complete compiler suite contains 1,115 tests.
