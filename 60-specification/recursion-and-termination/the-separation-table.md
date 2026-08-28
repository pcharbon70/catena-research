---
title: "The Separation Table"
kind: specification
created: "2026-08-26"
status: normative
spec_version: "0.1.31"
tags:
  - recursion
  - termination
  - specification
aliases:
  - "Catena recursion separation table"
---

# The Separation Table

## Status and authority

This chapter is the normative Catena 0.1.31 separation between program
recursion and meta-level evaluation. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consolidates, without amending or displacing, the regimes of
[Clause Conditions Diagnostics](../clause-conditions/diagnostics-and-conformance.md),
[Claims, Examples, and Checking](../specifications-and-governance/claims-examples-and-checking.md),
and the
[Traits README](../traits-and-categorical-operations/README.md).

The rules apply only to source-language revision `0.1.31`.

## The separation

Program recursion is unrestricted (the stance chapter); every
evaluator that runs **during compilation** is total-or-bounded by its
own shipped mechanism (`RT-OBL-005`):

> **Normative definition.**

| Meta evaluator | Regime | Home |
| --- | --- | --- |
| Conditions (guards) | acyclic first-order; recursive or mutually recursive dependencies reject as `CND004` | C003 |
| Specification examples | fixed 20,000 semantic-step pure checker | C006 |
| Laws and extensional samples | bounded law checks and bounded samples | C004 |
| Compile-time evaluation | MUST ship total-or-bounded, in its admitting slice | G038 — gated below |

No row changes its home's rule, budget, or diagnostic. The table is
the one language-level statement of the separation P034 asks for.

## The entry rule

> **Normative definition.**

A recursive-total fragment — recursive conditions, law evaluators,
compile-time evaluation, or any successor that executes user code
during compilation — enters the language **only through a slice that
proves its totality or fixes its budget in the same change**
(`RT-OBL-006`). No meta-level evaluator may arrive unbounded, and no
admission may rely on a promised later budget. An implementation MUST
NOT use this area's boundary to claim an unbounded compile-time
evaluator as a compatible addition.

## Determinism

The table is a classification: equal programs classify identically
under every conforming tool (`RT-OBL-008`).

## Deliberately separate work

G038 owns compile-time evaluation design under the gate. P109 owns
syntax. G036 owns the failure taxonomy, with divergence explicitly
outside it. G088 owns cancellation of long evaluations. G084 owns
runtime resource limits distinct from meta-level budgets.

## Rationale and evidence (non-normative)

The [recursion synthesis](../../20-notes/catena-recursion-and-termination.md)
records why the gate matters more than the table: without it, a
compile-time evaluator admitted as a compatible addition could hang
the compiler on a divergent user program — the regression C008's
classification discipline exists to prevent. The [topic
map](../../10-maps/recursion-and-termination.md) routes the decision.
