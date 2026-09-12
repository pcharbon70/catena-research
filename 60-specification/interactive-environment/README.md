---
title: "Interactive Environment"
kind: map
created: "2026-09-12"
tags: [specification, tooling, effects, resources]
aliases: []
---

# Interactive Environment (`60-specification/interactive-environment`)

## Purpose

The normative grammar-independent interactive-session foundation under
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for session ownership, admitted capabilities, retained checked inputs,
immutable module generations, bounded evaluation, interruption, history,
governance boundaries, cleanup, and the explicit P109 public-REPL hold.

## Index

### Subdirectories

None yet.

### Documents

- [Owned Retained-Input Sessions](owned-retained-input-sessions.md) — G120's revision 0.1.95 preparatory session contract and public-REPL hold.

## Variability register

No implementation-defined choice, normative recommendation, permission, or
bounded unspecified presentation is introduced. The fixed bounds are 16
capabilities, 32 retained generations per module, 256 history entries, a
default evaluation budget of 100,000 steps, a maximum evaluation budget of
10,000,000 steps, and 1,000 milliseconds for cleanup confirmation.

## Maintaining this index

Keep P109 public syntax, P117 diagnostics, C082 top-level effects, C080 resource
cleanup, P084 task ownership, C088 cancellation, C092 hot upgrade, C121 build
loading, and C131 secret handling aligned with this session boundary.
