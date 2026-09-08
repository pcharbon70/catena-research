---
title: "Typed Supervision"
kind: map
created: "2026-09-08"
tags:
  - specification
  - actors
aliases: []
---

# Typed Supervision (`60-specification/typed-supervision`)

## Purpose

The C089 typed supervision contract at `0.1.56`, governed by the
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Static checked worker descriptions, restart policies, bounded shutdown,
managed ownership and the narrow OTP lifecycle adapter.

## Index

### Subdirectories

None yet.

### Documents

- [Checked Supervision Trees and Lifecycle](checked-trees-and-lifecycle.md) —
  supported policy inventory, entry/artifact binding and lifecycle obligations.

## Variability register

No new implementation-defined choice or presentation allowance. Restart and
shutdown budgets are explicit program inputs. Finite allocation, generated artifacts
and atom resources inherit the standing implementation-limit policy; remote
capacity and general scheduler reporting remain separately owned.

## Maintaining this index

Keep this complete inventory, authority, version registry, evidence and
traceability synchronized with changes to the contract.
