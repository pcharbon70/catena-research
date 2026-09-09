---
title: "Trusted Computing Base"
kind: map
created: "2026-09-09"
tags: [specification, conformance, security]
aliases: []
---

# Trusted Computing Base (`60-specification/trusted-computing-base`)

## Purpose

C126's guarantee-specific trust disclosure under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Guarantee dependencies, residual compiler/host trust, maintained source/data
boundaries and falsifiable mutation evidence without unearned proof claims.

## Index

### Subdirectories

None yet.

### Documents

- [Guarantees, Assumptions, and Boundary Checks](guarantees-assumptions-and-boundary-checks.md) —
  graph obligations, independent-check limits, executable inventory and reviewed maintenance.

## Variability register

The supported graph and inventory scope are fixed. New profiles require explicit
reviewed changes. Parsed sources cap at 2,000,000 bytes after reading; actual
source/call/data counts are disclosed observations. Existing semantic limits remain
with their owners, and residual trust is not a language-behavior allowance.

## Maintaining this index

Update the graph, compiler source/data inventory, journal, conformance map and
checklist atomically. Keep detected and undetected fault classes separate.
