---
title: "Performance Envelope"
kind: map
created: "2026-09-10"
tags: [specification, performance, conformance, benchmarking]
aliases: []
---

# Performance Envelope (`60-specification/performance-envelope`)

## Purpose

The normative supported-host measurement and regression policy under
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for workload-family coverage, reproducible host identity, semantic
baseline gates, cold and warm measurements, memory and code-size evidence,
timeouts, retained negative results, and relative regression decisions.

## Index

### Subdirectories

None yet.

### Documents

- [Supported-Host Workloads and Regression Policy](supported-host-workloads-and-regression-policy.md) — G138's revision 0.1.88 workload, measurement, semantic-gate, and comparison contract.

## Variability register

Implementations may choose repetitions and regression thresholds within their
published bounded profile and may report additional workloads. They must cover
the required families and must not score a semantic mismatch, failure, or
timeout as a performance result.

## Maintaining this index

Keep the benchmark runner, raw supported-host reports, P108 operation contract,
P129 limits, P135 optimizer modes, lifecycle profile, and traceability map in
sync.

