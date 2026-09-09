---
title: "Value Boundaries"
kind: map
created: "2026-09-08"
tags:
  - specification
  - representation-independence
aliases: []
---

# Value Boundaries (`60-specification/value-boundaries`)

## Purpose

The normative C093 representation and checked-conversion contract at
`0.1.58`. It follows the
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Semantic carriers, representation ownership, verified conversion, and explicit
validation budgets. Final vocabulary and general foreign callbacks remain
separate work.

## Index

### Subdirectories

None yet.

### Documents

- [Value Carriers and Checked Conversion](carriers-and-checked-conversion.md) —
  representation matrix, integrated pure value-tree boundary,
  conversion invariants and conformance obligations.

## Variability register

No new implementation-defined language choice is proposed. Existing nominal
layout selection preserves the governing representation-independence contract.
Compiler literal, arity and artifact limits are inherited. Explicit per-call
conversion budgets count visited values and scalar payload bytes; they do not
promise a physical-memory ceiling or change source validity.

## Maintaining this index

Keep the inventory, normative status, evidence and conformance gates synchronized.
Keep exact-revision and retained-format evidence synchronized with the rules.
