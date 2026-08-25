---
title: "Observability and Trace Agreement"
kind: specification
created: "2026-08-25"
status: candidate
spec_version: "0.1.26"
tags:
  - evaluation-order
  - specification
  - observability
aliases:
  - "Catena order observability"
---

# Observability and Trace Agreement

## Status and authority

This chapter is the normative Catena 0.1.26 order-observability
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It generalizes, without amending, the observable-order rules of
[Operational Semantics](../traits-and-categorical-operations/operational-semantics.md)
and
[Deep Handlers and Affine Resumptions](../effects-and-handlers/deep-handlers-and-affine-resumptions.md).

The rules apply only to source-language revision `0.1.26`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## Order is observable semantics

Declared order is semantic and observable, not advisory
(`EO-OBL-006`):

> **Normative definition.**

```text
For a program whose subexpressions perform distinguishable effect
requests, the sequence of requests a conforming implementation
produces MUST equal the sequence the ordered-forms table determines.
```

- The observable is the **effect-request trace** — the sequence of
  requests an evaluation performs. Two executions with equal traces
  agree on the order of every effect-performing subexpression.
- This generalizes rules the corpus already shipped: C004's
  `MUST NOT reorder, duplicate, or drop` for trait traversal and
  C005's "handler order is observable" — it invents no new
  observability class.
- Implementations retain every **unobservable within-step freedom** —
  register allocation, environment representation, evaluation
  strategy inside one step — exactly the boundary the kernel's trace
  semantics draws. Only the request sequence is claimed.

## Dual-target agreement

A conforming compiler's generated code and the reference machine agree
on order (`EO-OBL-006`): for the same program, compiled BEAM execution
and the kernel stepper produce equal effect-request traces. This is
C005's reference/BEAM agreement pattern stated at the language level;
it is the conformance evidence route, not a new runtime obligation on
programs.

## Determinism

Equal programs and inputs produce equal traces under every conforming
execution (`EO-OBL-006`), by composition of this chapter with the
kernel's deterministic step relation and C029's terminal contract.

## Deliberately separate work

What a request *does* — handler dispatch, resumption behavior, the
operations themselves — remains C005's. Cancellation and deadlines
mid-evaluation remain G088's. Allocation observability beyond the
trace remains G037's. Debugging and tracing tools remain G124's.

## Rationale and evidence (non-normative)

The [order synthesis](../../20-notes/catena-evaluation-order.md)
records why observability is forced by shipped rules rather than
chosen, and why dual-target evidence is the only way order is real for
a compiler. The [topic map](../../10-maps/evaluation-order.md) routes
the decision.
