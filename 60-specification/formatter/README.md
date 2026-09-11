---
title: "Formatter"
kind: map
created: "2026-09-11"
tags: [specification, formatting, tooling, source-text]
aliases: []
---

# Formatter (`60-specification/formatter`)

## Purpose

The normative syntax-independent formatter foundation under
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for the document algebra, deterministic width-sensitive rendering,
verbatim token origins, source maps, canonical previews, fixed resource
bounds, and the explicit P109 public-source hold.

## Index

### Subdirectories

None yet.

### Documents

- [Syntax-Independent Document Algebra](syntax-independent-document-algebra.md) — G118's revision 0.1.94 preparatory printer contract and public-source hold.

## Variability register

No implementation-defined choice, normative recommendation, permission, or
bounded unspecified presentation is introduced. Width is measured in Unicode
scalar values. The default width is 100 and the maximum accepted width is 240.
The fixed bounds are 65,536 document nodes, depth 64, 16,777,216 input bytes,
16,777,216 output bytes, and 256 attachment bytes.

## Maintaining this index

Keep C013 source decoding, C015 layout, C016 comment attachment, C017 literal
preservation, C028 source compatibility, P117 diagnostics, P125 edit safety,
and P109 source adoption aligned.
