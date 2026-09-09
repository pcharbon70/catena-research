---
title: "Native Services"
kind: map
created: "2026-09-09"
tags: [specification, foreign-boundary, beam-vm]
aliases: []
---

# Native Services (`60-specification/native-services`)

## Purpose

C098's separately admitted native package and owned execution contract, under
[authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Native trust, scheduler classes, signed payload identity, bounded ports,
NIF crash boundaries and idempotent resource finalization.

## Index

### Subdirectories

None yet.

### Documents

- [Signed Loading and Owned Native Execution](signed-loading-and-owned-execution.md) —
  exact 0.1.63 semantics and native envelope format 1.

## Variability register

Package payload-byte limits, 1–4,294,967,295 millisecond call timeouts,
positive work units at most 9,007,199,254,740,991, and nonnegative release grace
are explicit inputs. Release grace defaults to 2,000,000,000 nanoseconds;
startup is bounded to 2,000 milliseconds and port close to 1,000 milliseconds.
Float uses one node, eight payload bytes and depth zero. The declared host
facilities and signer attestations are explicit in the chapter.

## Maintaining this index

Update this inventory, conformance evidence and checklist in the same change.
Wider native ABIs or scheduler admission need a separately evidenced revision.
