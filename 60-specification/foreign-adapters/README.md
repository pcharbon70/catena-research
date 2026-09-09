---
title: "Foreign Adapters"
kind: map
created: "2026-09-09"
tags: [specification, foreign-boundary]
aliases: []
---

# Foreign Adapters (`60-specification/foreign-adapters`)

## Purpose

The normative `0.1.61` executed adapter milestone of P096, following the
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Explicit trusted host declarations, effect-bound requests, scope ownership,
cooperative cancellation, pure compiled callbacks, and their conformance evidence.
Public syntax, environmental provisioning and general effectful callbacks retain
their separately identified completion work.

## Index

### Subdirectories

None yet.

### Documents

- [Authority, Calls and Callback Lifetime](authority-calls-and-callback-lifetime.md) —
  normative declaration, execution, cancellation and bounded cleanup contract.

## Variability register

All capacity and wait bounds are explicit adapter inputs. The default operation
and callback-registration bounds are each 1,024; default release grace is one
billion nanoseconds. Concurrent completion, cancellation and callback ingress
follow the event-order rules of the contract. The standing allocation and
code-generation limits continue to apply.

## Maintaining this index

Keep this inventory, the implementation journal, conformance map and checklist
synchronized. P096 stays partial until its public-surface gate and remaining
callback authority work are fulfilled.
