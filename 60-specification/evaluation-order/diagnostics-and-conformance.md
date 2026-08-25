---
title: "Evaluation Order Diagnostics and Conformance"
kind: specification
created: "2026-08-25"
status: normative
spec_version: "0.1.26"
tags:
  - conformance
  - diagnostics
  - evaluation-order
  - specification
  - testing
aliases:
  - "Catena 0.1.26 evaluation order conformance"
---

# Evaluation Order Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.26 evaluation-order
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Ordered Forms and Entry Rule](ordered-forms-and-entry-rule.md)
and [Observability and Trace Agreement](observability-and-trace-agreement.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`VA`-style
definitional stance, `EO-OBL-001`, `EO-OBL-008`). It accepts no new
input forms and rejects nothing existing, so no new invalid input
exists to diagnose. Every existing diagnostic family keeps its
identity and meaning unchanged.

## Abstract public boundaries

Two shipped boundaries witness the contract; the bootstrap adds no
new public API (`EO-OBL-001`):

- **Kernel stepper traces** — the reference machine's trace of effect
  requests and handler events for a program, whose order is the
  table's definitional reading.
- **Compiled BEAM traces** — the trace-equivalent observation of
  compiled execution, agreeing with the stepper per
  [Observability and Trace Agreement](observability-and-trace-agreement.md).

Implementations MUST NOT use these boundaries to claim binding
structure, arity rules, branch forms, cancellation, or any excluded
machinery (`EO-OBL-008`).

## Determinism

Equal programs produce equal traces under every conforming execution;
trace extraction is order-, locale-, and tool-independent
(`EO-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `EO-OBL-001` | apply order behavior only at exact 0.1.26 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `EO-OBL-002` | fix one declared order for every kernel-listed form, unchanged from the kernel's rules | kernel-form trace tests |
| `EO-OBL-003` | fix the typed-core completions: curried application, trait-call subject-then-arguments, handler installation, annotate transparency | completion-form trace tests |
| `EO-OBL-004` | keep the C002/C003/C004/C005 fragment rules exactly as their areas fixed them | fragment regression traces |
| `EO-OBL-005` | keep the table closed: no form outside it has a declared order; future forms enter with their own entry | closed-set and absence tests |
| `EO-OBL-006` | make declared order observable: equal effect-request traces on the stepper and compiled BEAM for the same program | dual-target trace-agreement tests |
| `EO-OBL-007` | keep the `and`/`or` skips as the only exceptions, under the C029 edition-record gate | skip and absence tests |
| `EO-OBL-008` | keep the contract deterministic, definitional, and outside G031–G033/G040/G088/P109 claims with zero new diagnostic families | repeated-trace and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `EO-OBL-*` set against unknown and
uncovered identifiers before C030 conformance is claimed.

## Required evidence sets

Positive evidence includes, for each table row, an effect-ordering
program whose subexpressions perform distinguishable requests,
executed on the stepper and on compiled BEAM with equal traces
matching the declared order — covering curried calls with requesting
callee and arguments, tuple/record/constructor field order, record
update base-then-value, send target-then-message, trait-call
subject-then-arguments, handler installation, `let` and sequence
schedules, and the `and`/`or` skips; and determinism across repeated
runs.

Negative evidence — in the definitional sense — includes forms outside
the table (collections, interpolation) demonstrating no declared
order exists to observe, and no new diagnostic family appearing.

Exclusion evidence demonstrates that binding structure, arity, and
branching claims are not made; that fragment rules keep their owning
areas' diagnostics; and that predecessor APIs retain their exact
selections and defaults.

## Revision and persistence separation

Revision `0.1.26` adds the ordered-forms table, the typed-core
completions, the entry rule, and order observability; it adds no JSON
AST version, kernel S-expression version, interface version, artifact
version, signature domain, typing rule, runtime behavior, BEAM
representation, manifest field, or diagnostic family, and amends no
retained revision (`EO-OBL-001`, `EO-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.26`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.27`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[order synthesis](../../20-notes/catena-evaluation-order.md), the
[resolved inquiry](../../40-inquiries/when-does-each-subexpression-evaluate.md),
and the [topic map](../../10-maps/evaluation-order.md). The C030
evidence record will preserve the sibling-compiler commands and archive
validation.
