---
title: "Numeric Library"
kind: map
created: "2026-09-09"
tags: [specification, numerics, conformance]
aliases: []
---

# Numeric Library (`60-specification/numeric-library`)

## Purpose

C105's exact 0.1.67 library operations under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Checked arithmetic, explicit conversions, decimal contexts, deterministic formatting,
mathematical-function admission and executable adoption without public vocabulary.

## Index

### Subdirectories

None yet.

### Documents

- [Checked Arithmetic and Explicit Rounding](checked-arithmetic-and-explicit-rounding.md) —
  numeric meaning, failure classes, precision, costs and exact artifact obligations.

## Variability register

Nearest-even finite binary64 operations, Euclidean division and exact decimal
printing are fixed. Decimal modes and scale/precision are explicit. Scale ranges
-1024..1024, coefficient precision 1..4096 digits, parser input at most 4096 bytes
and pipelines at most 253 operations. C095 budgets and inherited source/runtime
limits apply. Transcendental functions require NL-T01 before admission.

## Maintaining this index

Update the chapter, decision journal, conformance map and checklist atomically.
Keep library role labels separate from the held public vocabulary.
