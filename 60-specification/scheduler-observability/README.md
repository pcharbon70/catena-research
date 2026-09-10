---
title: "Scheduler Observability"
kind: map
created: "2026-09-10"
tags: [specification, concurrency, runtime, implementation-limits]
aliases: []
---

# Scheduler Observability (`60-specification/scheduler-observability`)

## Purpose

Scheduler nondeterminism, priorities, preemption, foreign-work classes, and
capacity disclosure under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

The boundary between observable program behavior and deployment-controlled
runnable-process selection, latency, reductions, priorities, and blocking work.

## Index

### Subdirectories

None yet.

### Documents

- [Policy Classes and Visible Limits](policy-classes-and-visible-limits.md) —
  C090's nondeterminism, work-admission, and disclosure contract.

## Variability register

Implementations select scheduling algorithms, reduction/preemption details,
runtime priority effects, runnable-process order, and worker-pool sizes within
the normative boundaries. Profiles disclose supported priority names and
foreign-worker ceilings. No bounded unspecified presentation is admitted.

## Maintaining this index

Keep scheduler classification, foreign/native declarations, implementation
limits, explorer evidence, profile validation, traceability, lifecycle, and the
completion checklist synchronized.
