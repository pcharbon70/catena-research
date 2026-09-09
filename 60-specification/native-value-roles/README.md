---
title: "Native Value Roles"
kind: map
created: "2026-09-09"
tags: [specification, foreign-boundary, beam-vm]
aliases: []
---

# Native Value Roles (`60-specification/native-value-roles`)

## Purpose

The normative C097 native-kind admission inventory at exact `0.1.62`, following
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Typed mappings for immutable native data, opaque process/reference roles,
callback admission, explicit port exclusions, and ownership/equality/transfer rules.
G098 separately owns native package loading, scheduler and finalization policy.

## Index

### Subdirectories

None yet.

### Documents

- [Typed Admission and Native Identity](typed-admission-and-native-identity.md) —
  the complete native-kind inventory and registered role contract.

## Variability register

Conversion, operation and release bounds are explicit inputs inherited from
C095 and the P096 adapter milestone. Native grant count is at most the supplied
operation maximum, whose default is 1,024. Native sends consume that same
operation budget. Ordinary allocation limits retain the standing policy.

## Maintaining this index

Update this inventory, the conformance map, journal and checklist together.
An additional native role or wider transport permission requires its own
semantic revision and executable evidence.
