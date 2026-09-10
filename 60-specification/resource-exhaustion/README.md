---
title: "Resource Exhaustion"
kind: map
created: "2026-09-10"
tags: [specification, conformance, implementation-limits, runtime]
aliases: []
---

# Resource Exhaustion (`60-specification/resource-exhaustion`)

## Purpose

Aggregate compiler budgets and explicit runtime admission under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Compiler transaction accounting, pre-publication refusal, bounded runtime
queues, overload outcomes, cancellation, diagnostics, and residual host-fatal
resource limits.

## Index

### Subdirectories

None yet.

### Documents

- [Aggregate Budgets and Runtime Admission](aggregate-budgets-and-runtime-admission.md)
  — C129's compiler and runtime resource-exhaustion contract.

## Variability register

Implementations may configure aggregate compiler bounds above the portable
minima. A runtime queue selects its positive message and encoded-byte bounds
within the published implementation ceiling and selects either rejection or
termination as its overload policy. All selected values and outcomes are
explicit; no bounded unspecified presentation is admitted.

## Maintaining this index

Update the central implementation-limit policy, compiler profile, tests,
traceability, lifecycle records, and checklist with this chapter.
