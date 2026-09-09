---
title: "Calling Conventions"
kind: map
created: "2026-09-09"
tags:
  - specification
  - functions
aliases: []
---

# Calling Conventions (`60-specification/calling-conventions`)

## Purpose

The normative C094 call-boundary contract for exact revision `0.1.59`. It follows
the [authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Exact call/artifact identity, direct and curried call shapes, typed callback
boundaries, retained process/lifecycle adapters, source-frame provenance and
conformance evidence. General foreign declarations, asynchronous callback
transport and final public spelling retain their separate checklist owners.

## Index

### Subdirectories

None yet.

### Documents

- [Checked Calls and Artifact Identity](checked-calls-and-artifact-identity.md) —
  normative admission matrix, identity checks, staging, lifetime and trace rules.

## Variability register

No new implementation-defined choice or presentation allowance is introduced.
Validation budgets and the closure-handle bound are explicit adapter inputs;
the default handle bound is 1,024. Compiler arity, module-size and allocation
limits inherit the standing policy. Missing source spans and unmapped technical
frames are retained as missing evidence, not invented source locations.

## Maintaining this index

Keep the complete inventory, implementation journal, conformance map and
checklist synchronized. A semantic extension requires its own explicit
revision, conformance evidence and compatibility record.
