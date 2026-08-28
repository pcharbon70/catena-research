---
title: "Recursion and Termination Diagnostics and Conformance"
kind: specification
created: "2026-08-26"
status: normative
spec_version: "0.1.31"
tags:
  - conformance
  - diagnostics
  - recursion
  - termination
  - specification
  - testing
aliases:
  - "Catena 0.1.31 recursion conformance"
---

# Recursion and Termination Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.31 recursion diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Program Recursion Is Unrestricted](program-recursion-is-unrestricted.md)
and [The Separation Table](the-separation-table.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`RT-OBL-001`,
`RT-OBL-008`). Divergence is non-termination, not invalidity — no
program is rejected for recursing; recursive conditions already reject
as C003's `CND004`; budget exhaustion reports keep their owning areas'
identities. Nothing new becomes invalid here.

## Abstract public boundaries

Three shipped boundaries witness the contract; the bootstrap adds no
new public API (`RT-OBL-001`):

- **Kernel stepper** — non-tail recursion completing, tail recursion
  terminating, and the `budget_exhausted` outcome as the definitional
  divergence witness.
- **Compiled BEAM execution** — non-tail and tail recursion
  completing at depths the reference budget cannot cover, proving the
  stance holds on the production target.
- **Condition/specification checkers** — `CND004` and the 20,000-step
  budget, unchanged from C003 and C006.

Implementations MUST NOT use these boundaries to claim termination
checking, an unbounded compile-time evaluator, or any excluded
machinery (`RT-OBL-008`).

## Determinism

Equal programs run and diverge identically under every conforming
target up to its declared budgets (`RT-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `RT-OBL-001` | apply recursion behavior only at exact 0.1.31 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `RT-OBL-002` | keep program recursion unrestricted: non-tail recursion runs and completes alongside tail recursion | non-tail completion tests |
| `RT-OBL-003` | keep divergence non-termination: budget exhaustion on the stepper, never a trap diagnostic | divergence witness tests |
| `RT-OBL-004` | keep totality checking absent: no validity gate on recursion, analysis-only through the edition gate | absence tests |
| `RT-OBL-005` | keep every meta-level evaluator total-or-bounded per its cited regime | regime regression tests |
| `RT-OBL-006` | enforce the entry rule: no unbounded meta-level evaluator may be claimed | absence and registry-shape tests |
| `RT-OBL-007` | keep recursive conditions rejecting as `CND004` unchanged | condition regression tests |
| `RT-OBL-008` | keep the classification deterministic and outside G036/G038/G084/G088/P109 claims with zero new families | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `RT-OBL-*` set against unknown and
uncovered identifiers before C034 conformance is claimed.

## Required evidence sets

Positive evidence includes non-tail recursion (a stack-consuming
recursive sum at depth 10,000) completing on compiled BEAM and at a
budget-compatible depth on the stepper; tail recursion terminating
(the C032 shape); and determinism across repeated runs.

Negative evidence — in the definitional sense — includes an infinite
loop reporting `{:budget_exhausted, _}` on the stepper under an
explicit small budget, with no trap diagnostic; a recursive or
mutually-recursive condition declaration rejecting as `CND004`; and
no new family appearing for any recursion shape.

Exclusion evidence demonstrates no termination-check entry points, no
unbounded meta-level evaluator entry points, unchanged `CND004` and
checker-budget identities, and predecessor APIs retaining their exact
selections and defaults.

## Revision and persistence separation

Revision `0.1.31` adds the stance, the separation table, and the entry
rule; it adds no JSON AST version, kernel S-expression version,
interface version, artifact version, signature domain, typing rule,
runtime behavior, BEAM representation, manifest field, public API
name, or diagnostic family, and amends no retained revision
(`RT-OBL-001`, `RT-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.31`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.32`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[recursion synthesis](../../20-notes/catena-recursion-and-termination.md),
the [resolved inquiry](../../40-inquiries/how-does-catena-separate-recursion-from-termination.md),
and the [topic map](../../10-maps/recursion-and-termination.md). The
C034 evidence record will preserve the sibling-compiler commands and
archive validation.
