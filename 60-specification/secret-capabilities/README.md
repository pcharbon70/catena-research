---
title: "Secret Capabilities"
kind: map
created: "2026-09-09"
tags: [specification, conformance, security]
aliases: []
---

# Secret Capabilities (`60-specification/secret-capabilities`)

## Purpose

C131's sealed credential values and protected delivery under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Provider and recipient authority, sensitivity lineage, observation protection,
checked compiled entries, bounded cleanup and explicit host trust.

## Index

### Subdirectories

None yet.

### Documents

- [Sealed Values and Protected Delivery](sealed-values-and-protected-delivery.md) —
  revision 0.1.72's credential lifecycle and conformance obligations.

## Variability register

The chapter fixes all exact profile ceilings, supported transports, refusal and
redaction. Inherited adapters own platform-specific execution and cleanup.
The profile promises neither hostile-host secrecy nor secure erasure.

## Maintaining this index

Update the chapter, trust inventory, journal, traceability and checklist together.
