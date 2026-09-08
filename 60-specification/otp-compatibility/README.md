---
title: "OTP Compatibility"
kind: map
created: "2026-09-08"
tags:
  - specification
  - compatibility
aliases: []
---

# OTP Compatibility (`60-specification/otp-compatibility`)

## Purpose

The C099 toolchain compatibility contract at `0.1.57`, governed by the
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Tested runtime rows, required feature probes, binary provenance, rebuilds
and support lifecycle. Source syntax and live upgrade are separate contracts.

## Index

### Subdirectories

None yet.

### Documents

- [OTP Support, Probes and Artifact Compatibility](support-probes-and-artifacts.md) —
  tested matrix, required checks, loading and support-lifecycle obligations.

## Variability register

No new implementation-defined language choice or presentation allowance.
The exact tested target set is explicit. Compilation, artifacts, probes and
allocation inherit standing implementation limits; no new runtime capacity
floor or scheduler guarantee is introduced.

## Maintaining this index

Keep this complete inventory, authority, version registry, evidence and
traceability synchronized with changes to the contract.
