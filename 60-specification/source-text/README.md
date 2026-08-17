---
title: "Source Text Specification"
kind: map
created: "2026-08-17"
tags:
  - archive-navigation
  - directory-index
  - parsing
  - specification
  - unicode
aliases:
  - "Catena 0.1.9 source-text specification"
---

# Source Text Specification (`60-specification/source-text`)

## Purpose

This directory contains the normative Catena 0.1.9 contract for decoding
future ergonomic source files from bytes into a logical Unicode stream with
original-byte locations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, and content labels. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, variability, and diagnostic behavior.
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
controls any finite-resource refusal; this area introduces no new portable
minimum or implementation limit.

## What belongs here

Put only source encoding, BOM handling, logical newlines, normalization
boundaries, original-byte scalar locations, source-envelope diagnostics, and
their conformance gate here. Identifiers, whitespace and layout, comments,
literals, operators, complete grammar, formatter behavior, and file-to-module
rules remain later checklist work.

## Variability register

No 0.1.9 source-text rule introduces an implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation limit.
Conforming decoders accept and reject the same byte sequences and produce the
same logical scalar stream and language positions.

## Index

### Subdirectories

- None yet.

### Documents

- [Source-Text Envelope](source-text-envelope.md) — exact UTF-8, BOM, newline,
  normalization, preservation, position, applicability, and exclusion rules.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  diagnostics, public decoder and CLI results, obligation identifiers,
  adversarial evidence, and promotion boundary.

## Maintaining this index

Keep both chapters at one lifecycle status and version. Any widening of
accepted encodings, newline forms, normalization, source-coordinate units, or
frontend applicability requires an explicit later semantic revision and
migration record. Keep this inventory and the conformance traceability map in
sync with every rule change.
