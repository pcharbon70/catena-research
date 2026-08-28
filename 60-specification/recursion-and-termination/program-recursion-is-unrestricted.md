---
title: "Program Recursion Is Unrestricted"
kind: specification
created: "2026-08-26"
status: normative
spec_version: "0.1.31"
tags:
  - recursion
  - termination
  - specification
aliases:
  - "Catena recursion stance"
---

# Program Recursion Is Unrestricted

## Status and authority

This chapter is the normative Catena 0.1.31 program-recursion stance.
It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the recursion rules of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md),
the divergence clause of
[Strictness and Terminal Outcomes](../values-and-evaluation/strictness-and-terminal-outcomes.md),
the definitions-only boundary of
[Binding Structure and Scope](../bindings-and-sequencing/binding-structure-and-scope.md),
and the tail guarantee of
[Proper Tail Calls](../functions-and-calls/closures-and-tail-calls.md).

The rules apply only to source-language revision `0.1.31`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The stance

> **Normative definition.**

```text
Any named definition may recurse. General recursion may reduce
forever. Divergence is non-termination — never a trap and never
an undefined outcome.
```

- **Recursion is free at the program layer** (`RT-OBL-002`): tail
  recursion keeps the
  [proper-tail-call guarantee](../functions-and-calls/closures-and-tail-calls.md#proper-tail-calls);
  non-tail recursion consumes stack without bound and is nevertheless
  legal — no conformance claim attaches to stack use outside the tail
  guarantee, exactly as the kernel fixes.
- **Divergence is non-termination** (`RT-OBL-003`): a computation that
  reduces forever is a running computation. It is not a failure under
  the
  [trap taxonomy](../formal-semantic-kernel/actors-messages-and-failures.md),
  never an undefined outcome, and never a conformance defect.
  Reference machines report it as budget exhaustion; production
  runtimes simply keep running.
- **No totality checking exists** (`RT-OBL-004`): no expression-level
  termination analysis gates validity at 0.1.31, and none is planned.
  Any future termination checker enters as an **edition-record-gated
  opt-in analysis** — a tool that reports, never a rule that rejects;
  validity changes are forever out of scope for such a checker.

## What is not promised

Nothing here promises completion, stack depth, memory bounds, or
cancellation: those belong to G084 (runtime limits), G088
(cancellation), and the
[implementation limits](../../IMPLEMENTATION-LIMITS.md) policy. The
stance is the *absence* of a termination obligation, stated once at
the language level.

## Deliberately separate work

Where recursion lives (definitions-only) remains C031's. The tail
guarantee remains C032's. Compile-time evaluation remains G038's,
under
[The Separation Table](the-separation-table.md)'s gate. The failure
taxonomy remains G036's — divergence is explicitly outside it.
Process-loop termination beyond the kernel's receive clause remains
G084's.

## Rationale and evidence (non-normative)

The [recursion synthesis](../../20-notes/catena-recursion-and-termination.md)
records why unrestricted is an elevation (every shipped machine
permits general recursion; C032's witness runs it) and why the
analysis-only gate protects the stance. The [resolved
inquiry](../../40-inquiries/how-does-catena-separate-recursion-from-termination.md)
and [topic map](../../10-maps/recursion-and-termination.md) preserve
the decision route.
