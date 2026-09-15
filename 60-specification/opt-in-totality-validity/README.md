---
title: "Opt-In Totality Validity Specification"
kind: map
created: "2026-09-15"
tags:
  - archive-navigation
  - directory-index
  - recursion
  - specification
  - termination
  - totality
aliases:
  - "Catena 0.1.99 totality amendment"
---

# Opt-In Totality Validity Specification (`60-specification/opt-in-totality-validity`)

## Purpose

This directory contains the normative Catena 0.1.99 C034 amendment. It
preserves unrestricted ordinary recursion while replacing the permanent ban on
validity-gating totality analysis with a closed gate for a later explicitly
total declaration.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure and exhaustion.

## What belongs here

Put the explicit-total admission policy, its replacement and lifecycle record,
and `RT-OBL-009`–`RT-OBL-015` here. The exact 0.1.31 recursion stance and
historical obligations remain in the
[Recursion and Termination Specification](../recursion-and-termination/README.md).
P109 owns the later source form, checker, proof representation, diagnostics,
interface adoption, and executable evidence.

## Variability register

The amendment's `MAY` permits a later normative language slice to admit an
explicit-total declaration after satisfying the closed gate. It does not permit
implementation variation. The amendment introduces no implementation-defined
choice, recommendation, bounded unspecified presentation, or implementation
limit. Any later checker limit belongs to its admitting slice.

## Index

### Subdirectories

- None yet.

### Documents

- [Explicit Total Declaration Gate](explicit-total-declaration-gate.md) — the
  normative 0.1.99 replacement, admission contract, lifecycle record, and
  partial conformance obligations.

## Maintaining this index

Preserve 0.1.31 as historical exact-selection authority. Any admitted total
source form must satisfy every gate component in one later versioned slice.
Keep the authority registry, C034/P109 checklist status, traceability map,
compiler evidence, and this inventory synchronized.
