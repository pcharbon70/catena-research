---
title: "Equality and Ordering Diagnostics and Conformance"
kind: specification
created: "2026-08-26"
status: normative
spec_version: "0.1.30"
tags:
  - conformance
  - diagnostics
  - equality
  - ordering
  - specification
  - testing
aliases:
  - "Catena 0.1.30 equality conformance"
---

# Equality and Ordering Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.30 equality diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Comparable Set](the-comparable-set.md) and
[Float Equality and Semantics](float-equality-and-semantics.md).

## Stable diagnostics

This area introduces **one** diagnostic family (`EQ-OBL-001`,
`EQ-OBL-004`):

| ID | Required meaning |
| --- | --- |
| `EQN001` | an equality or ordering operand is not comparable: a closure, a process handle, or a composite containing one |

All other failures reuse existing families unchanged: mixed
`Int`/`Float` comparison is the existing type-unification error;
guard-fragment violations keep C003's `CND` families; the operator
inventory keeps C019's diagnostics (`EQ-OBL-007`).

## Abstract public boundaries

Three boundaries gain equality wiring; the bootstrap adds the
classifier functions (`EQ-OBL-001`):

- **Value classification** — `Catena.Values` gains `comparable?/1`
  and `orderable?/1`: total, recursive over both carriers, implementing
  the closed sets.
- **Inference** — the general binary rule admits the comparable set
  for equality and the orderable set for ordering, rejecting
  non-comparable operands as `EQN001`; guard checking keeps the frozen
  fragment through the independent condition checker.
- **Evaluation and lowering** — the reference evaluator compares
  floats bit-exactly (raw 64-bit patterns, never `==`); BEAM lowering
  rides `=:=` and `<`-family operators, which distinguish the signed
  zeros on OTP 27+ and give structural tuple/map equality natively.

Implementations MUST NOT use these boundaries to claim identity
equality for closures or handles, heterogeneous comparison, NaN
semantics, trait overloading, or any excluded machinery (`EQ-OBL-008`).

## Determinism

Equal operands produce equal comparison results on every target;
comparison is order-, locale-, and tool-independent, total over the
closed set (`EQ-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `EQ-OBL-001` | apply equality behavior only at exact 0.1.30 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `EQ-OBL-002` | fix the comparable set with structural recursion and bit-exact float equality (`−0.0 ≠ 0.0`) | comparable-matrix and signed-zero tests |
| `EQ-OBL-003` | fix the orderable set (Int, Float) with total float ordering (`−0.0 < 0.0`) | ordering tests on both targets |
| `EQ-OBL-004` | reject closure, handle, and containing-composite comparisons as `EQN001` | exclusion tests |
| `EQ-OBL-005` | keep comparison monomorphic: mixed Int/Float is the existing type error | monomorphism rejection tests |
| `EQ-OBL-006` | keep the sets closed: no outside type compares; future types enter with their own entry | closed-set absence tests |
| `EQ-OBL-007` | keep the guard fragment frozen: guards reject Float comparisons via C003's families; general expressions admit them | guard-vs-general split tests |
| `EQ-OBL-008` | keep comparison deterministic and outside G036/G037/G040/G061/P109 claims, reusing existing families | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `EQ-OBL-*` set against unknown and
uncovered identifiers before C035 conformance is claimed.

## Required evidence sets

Positive evidence includes `−0.0 ≠ 0.0` and `−0.0 < 0.0` agreeing on
evaluator and BEAM; ordinary Float equality and ordering on both
targets; structural equality on tuples, records, variants, and
constructor values agreeing across targets (records compared
semantically, field order irrelevant); Int/Bool equality in general
expressions; and determinism across repeated runs.

Negative evidence includes closure and handle comparisons rejecting
as `EQN001` (directly and inside composites); mixed Int/Float
comparison rejecting as the existing type error; a Float comparison
in a guard rejecting via C003's `CND` families while the same
expression type-checks as a general expression; and no new family
appearing for any other shape.

Exclusion evidence demonstrates no identity equality, no NaN
semantics, no trait overloading, unchanged C003/C019 diagnostic
identities, and predecessor APIs retaining their exact selections and
defaults.

## Revision and persistence separation

Revision `0.1.30` adds the comparable set, float comparison
semantics, the classifier functions, the widened general operator
typing, and `EQN001`; it adds no JSON AST version, kernel
S-expression version, interface version, artifact version, signature
domain, runtime behavior beyond comparison results, BEAM
representation, or manifest field, and amends no retained revision —
C003's fragment and C019's inventory stay frozen (`EQ-OBL-001`,
`EQ-OBL-008`). The widened operator typing is a C028-minor
(additive) interface change.

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.30`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.31`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[equality synthesis](../../20-notes/catena-equality-and-ordering.md),
the [resolved inquiry](../../40-inquiries/which-values-compare-and-how.md),
and the [topic map](../../10-maps/equality-and-ordering.md). The C035
evidence record will preserve the sibling-compiler commands and archive
validation.
