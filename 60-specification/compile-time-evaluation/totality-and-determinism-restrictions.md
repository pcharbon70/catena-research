---
title: "Totality and Determinism Restrictions"
kind: specification
created: "2026-08-26"
status: candidate
spec_version: "0.1.34"
tags:
  - compile-time-evaluation
  - totality
  - determinism
  - specification
aliases:
  - "Catena compile-time restrictions"
---

# Totality and Determinism Restrictions

## Status and authority

This chapter is the normative Catena 0.1.34 statement of the
totality and determinism restrictions on compile-time evaluation. It
is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consolidates, without amending, the regimes of
[The Separation Table](../recursion-and-termination/the-separation-table.md),
[Clause Conditions Diagnostics](../clause-conditions/diagnostics-and-conformance.md),
[Claims, Examples, and Checking](../specifications-and-governance/claims-examples-and-checking.md),
and the [Traits README](../traits-and-categorical-operations/README.md).

The rules apply only to source-language revision `0.1.34`.

## The restriction table

The complete totality and determinism regime for everything that
executes during compilation at 0.1.34 (`CE-OBL-005`):

> **Normative definition.**

| Evaluator | Regime | Home |
| --- | --- | --- |
| The gate (every present and future evaluator) | total-or-bounded in the admitting slice; no unbounded arrival; determinism inherited | C034 |
| Condition normalization | acyclic first-order; normalization and expansion budgets | C003 |
| Specification examples | fixed 20,000 semantic-step pure checker | C006 |
| Law checking | bounded law checks and bounded extensional samples | C004 |

No row changes its home's rule, budget, or diagnostic; the table is
the one-place answer to G038's restriction clause. Compilation
therefore cannot hang on user-authored code: every machine that runs
is acyclic or budgeted, and every future one arrives gated.

## Determinism

All four rows are deterministic: equal inputs produce equal
normalizations, verdicts, samples, and derived output, on every
conforming target (`CE-OBL-006`). The compiler's own determinism
(byte-identical recompilation) subsumes the derived-output case.

## Deliberately separate work

Budget values themselves remain their owning areas' implementation
limits; G121 owns build-tooling timeouts distinct from these budgets;
G116/P125 own migration engines that consume compilation but are not
compilers.

## Rationale and evidence (non-normative)

The [compile-time synthesis](../../20-notes/catena-compile-time-evaluation.md)
records why the cited-table form follows C030/C033's consolidation
pattern. The [topic map](../../10-maps/compile-time-evaluation.md)
routes the decision.
