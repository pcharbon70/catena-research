---
title: "Erlang Type Boundary"
kind: map
created: "2026-09-09"
tags:
  - specification
  - foreign-boundary
aliases: []
---

# Erlang Type Boundary (`60-specification/erlang-type-boundary`)

## Purpose

C095's exact `0.1.60` typed conversion contract under the
[authority policy](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[implementation limits](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Explicit codecs, whole-carrier budgets, nominal constructor provenance,
foreign/native representation distinctions, expected conversion refusal,
Float ingress evidence and preservation obligations. General foreign execution
belongs to P096 and native authority/handle roles to P097/G098.

## Index

### Subdirectories

None yet.

### Documents

- [Typed Conversion and Preservation](typed-conversion-and-preservation.md) —
  admitted codec relations, budgets, failure classification and obligations.

## Variability register

The contract is deterministic. Node, byte and depth bounds are explicit adapter
inputs. Finite allocation and emitted-code limits inherit the standing policy;
no new compiler-configured threshold or presentation allowance is added.

## Maintaining this index

Keep the exhaustive inventory, authority, conformance map, compiler tests,
source provenance and checklist synchronized. Extend an admission relation
only through an explicit later semantic revision with preservation evidence.
