---
title: "Editor Protocol"
kind: map
created: "2026-09-12"
tags: [specification, tooling, diagnostics]
aliases: []
---

# Editor Protocol (`60-specification/editor-protocol`)

## Purpose

The normative grammar-independent language-service foundation under
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for retained-input snapshots, shared compiler analysis, result freshness,
cancellation, stable diagnostics, semantic queries, conservative rename
previews, fixed bounds, and the explicit P109 public-protocol hold.

## Index

### Subdirectories

None yet.

### Documents

- [Immutable Retained-Input Language Service](immutable-retained-input-language-service.md) — G123's revision 0.1.96 preparatory editor-service contract and public-source-protocol hold.

## Variability register

No implementation-defined choice, normative recommendation, permission, or
bounded unspecified presentation is introduced. The fixed bounds are
16,777,216 input bytes, 4,096 symbols, 256 cancelled request identities, 256
completion-prefix bytes, 1,024 rename edits, and 16,777,216 result bytes.

## Maintaining this index

Keep P109 public parsing and transport, P117 diagnostics, G118 formatting,
P119 semantic documentation, C066 name resolution, and P125 transactional
edits aligned with this service boundary.
