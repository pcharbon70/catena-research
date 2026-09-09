---
title: "Collection Protocols"
kind: map
created: "2026-09-09"
tags: [specification, collections, conformance]
aliases: []
---

# Collection Protocols (`60-specification/collection-protocols`)

## Purpose

C102's explicit finite families and owned pull contracts at `0.1.65`, under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Lawful collection families, deterministic keys, explicit builders, ordered
traversal, checked callbacks, owned pulls and operation-specific costs.

## Index

### Subdirectories

None yet.

### Documents

- [Finite Families and Owned Pulls](finite-families-and-owned-pulls.md) —
  ordinary package roles and checked finite/pull execution without public syntax.

## Variability register

Explicit C095 node/byte/depth budgets govern conversion. Pull timeout defaults
to 1000 milliseconds, range 1–1,000,000; step cap defaults to 1024, range
1–1,000,000; collection item caps range 0–1,000,000. Public waits add 100
milliseconds. Release allows twice the timeout plus 200 milliseconds and uses a
private reply wait of twice the timeout plus 100 milliseconds. Descriptor,
traversal and closed-law choices are explicit; source and runtime limits retain
the governing policy. There is no variable key iteration order.

## Maintaining this index

Keep the chapter, collection map, conformance register, journal and checklist
consistent with executable evidence and every changed bound.
