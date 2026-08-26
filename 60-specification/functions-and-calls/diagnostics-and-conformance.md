---
title: "Functions and Calls Diagnostics and Conformance"
kind: specification
created: "2026-08-25"
status: candidate
spec_version: "0.1.28"
tags:
  - conformance
  - diagnostics
  - functions
  - specification
  - testing
aliases:
  - "Catena 0.1.28 functions conformance"
---

# Functions and Calls Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.28 functions diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Arity and Application](arity-and-application.md) and
[Closures and Tail Calls](closures-and-tail-calls.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`FC-OBL-001`,
`FC-OBL-008`). The semantic-unary model admits no arity mismatch, and
every other rule elevates shipped behavior: no new invalid input
exists to diagnose. Every existing family keeps its identity and
meaning unchanged; `T001` remains the unbound-name rejection and
`BS001` the unused-binding warning that let-bound closures can
provoke.

## Abstract public boundaries

Three shipped boundaries witness the contract; the bootstrap adds no
new public API (`FC-OBL-001`):

- **Reference evaluator** — nested closure construction and prefix
  application as values, agreeing with compiled BEAM.
- **Kernel stepper** — termination of tail-recursive definitions
  within its budget, on the definitional machine.
- **Compiled BEAM execution** — deep tail recursion completing under
  the native last-call optimization, and curried values callable
  across the boundary.

Implementations MUST NOT use these boundaries to claim fixed-arity
checking, mutable capture, local recursion, calling-convention
stability, or any excluded machinery (`FC-OBL-008`).

## Determinism

Equal applications produce equal values and traces on every target;
witnesses are order- and tool-independent (`FC-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `FC-OBL-001` | apply function-model behavior only at exact 0.1.28 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `FC-OBL-002` | fix the semantic-unary model: multi-parameter desugaring and repeated unary application with no arity diagnostics | curried-application witness tests |
| `FC-OBL-003` | make any prefix application a value: free partial application, first-class and callable | partial-application value tests |
| `FC-OBL-004` | enforce lexical immutable capture: two applications observe the same captured values | capture-agreement tests |
| `FC-OBL-005` | make the let-bound closure the local-function form under all of C031's rules | local-closure value tests |
| `FC-OBL-006` | keep the proper-tail-call guarantee: deep tail recursion completes without unbounded stack growth | deep BEAM recursion and stepper termination tests |
| `FC-OBL-007` | keep named functions as definitions with C031's recursion environment and C022's export rules | named-definition witness tests |
| `FC-OBL-008` | keep the model deterministic and outside G033/P034/G037/G094/P109 claims with zero new diagnostic families | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `FC-OBL-*` set against unknown and
uncovered identifiers before C032 conformance is claimed.

## Required evidence sets

Positive evidence includes a multi-parameter definition desugared and
applied across arguments with evaluator/BEAM agreement; a prefix
application yielding a callable closure value on both targets; a
closure whose captured binding feeds two applications agreeing on
values; a let-bound closure passed, stored, and invoked as a value; a
named recursive definition running; a deep tail-recursive definition —
match-dispatched, one million iterations — completing on compiled BEAM
with the correct value; and the stepper terminating a tail recursion
within its budget.

Negative evidence — in the definitional sense — includes no arity
diagnostic existing to provoke, and let-bound closures provoking only
existing families (`T001`, `BS001`).

Exclusion evidence demonstrates no fixed-arity claim, no mutable
capture, no local-recursion form, no calling-convention stability
claim, and predecessor APIs retaining their exact selections and
defaults.

## Revision and persistence separation

Revision `0.1.28` adds the arity model, the desugaring semantics,
partial application, capture discipline, the local-function form, and
the elevated tail guarantee; it adds no JSON AST version, kernel
S-expression version, interface version, artifact version, signature
domain, typing rule, runtime behavior, BEAM representation, manifest
field, public API name, or diagnostic family, and amends no retained
revision (`FC-OBL-001`, `FC-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.28`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.29`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[functions synthesis](../../20-notes/catena-functions-and-calls.md),
the [resolved inquiry](../../40-inquiries/what-is-catenas-function-and-call-model.md),
and the [topic map](../../10-maps/functions-and-calls.md). The C032
evidence record will preserve the sibling-compiler commands and archive
validation.
