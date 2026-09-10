---
title: "Hot Code Upgrade"
kind: map
created: "2026-09-10"
tags: [specification, concurrency, runtime, compatibility]
aliases: []
---

# Hot Code Upgrade (`60-specification/hot-code-upgrade`)

## Purpose

Checked state migration, bounded code coexistence, activation, rollback, and
distributed-version admission under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Normative rules for replacing a running Catena upgrade unit without changing
the meaning of live closures, capabilities, resumptions, owned resources, or
external history.

## Index

### Subdirectories

None yet.

### Documents

- [Checked Migration and Activation](checked-migration-and-activation.md) —
  C092's descriptor, quiescence, migration, coexistence, and rollback contract.

## Variability register

Implementations select migration time and state-byte limits up to their
published ceilings. Deployment coordination and OTP release packaging remain
implementation mechanisms. No bounded unspecified presentation is admitted.

## Maintaining this index

Keep compatibility, task/resource lifecycle, distribution, OTP adapter,
machine-profile, traceability, and checklist evidence synchronized.
