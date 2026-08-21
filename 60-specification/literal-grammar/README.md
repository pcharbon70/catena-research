---
title: "Literal Grammar Specification"
kind: map
created: "2026-08-18"
tags:
  - archive-navigation
  - directory-index
  - literals
  - specification
  - syntax
aliases:
  - "Catena 0.1.13 literal specification"
---

# Literal Grammar Specification (`60-specification/literal-grammar`)

## Purpose

This directory contains the normative Catena 0.1.13 contract for atomic
Boolean, integer, decimal-float, text, character, and byte literal spelling;
decoded payloads and exact source provenance; literal-owned line breaks;
diagnostics; implementation limits; and executable conformance.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, diagnostic presentation, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy supplies the portable floors and common refusal contract for integer
magnitude and decoded literal payload size.

## What belongs here

Put atomic literal token spelling, delimiter and escape decoding, scalar and
octet restrictions, raw-token line ownership, source pieces, stable literal
diagnostics, and C017 conformance obligations here. Numeric runtime types,
defaulting, rounding, overflow, exceptional values, and negation are fixed by
the normative 0.1.14
[Numeric Literal Semantics](../numeric-literal-semantics/README.md) area.
Atoms/symbols and compound list, tuple, record, map, and binary construction
remain G040/G042/P093/G097. Concrete token composition, operators, and
punctuation remain G019/P109.

## Variability register

This area introduces no implementation-defined choice, recommendation, or
bounded unspecified presentation. It applies two implementation limits from
the repository policy: `LIM002` measures mathematical integer magnitude with
a 4,096-decimal-digit portable floor, and `LIM004` measures each decoded text
or byte payload with a 65,536-byte portable floor. No semantic hash-count,
escape-count, or source-line limit is introduced.

## Index

### Subdirectories

- None yet.

### Documents

- [Literal Forms and Boundaries](literal-forms-and-boundaries.md) — exact
  Boolean and numeric grammar, normalized components, atomic-token boundary,
  exclusions, and exact 0.1.13 applicability.
- [Text, Characters, and Bytes](text-characters-and-bytes.md) — cooked and raw
  delimiters, strict escapes, scalar and octet decoding, preservation,
  provenance pieces, and token-owned line breaks.
- [Diagnostics, Limits, and Conformance](diagnostics-limits-and-conformance.md)
  — stable `LIT001`–`LIT003`, active `LIM002`/`LIM004`, the abstract scan
  boundary, `LT-OBL-001`–`LT-OBL-012`, evidence sets, and persistence
  separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A literal spelling,
decoding, ownership, diagnostic, or limit change requires an explicit later
semantic or governance revision as applicable. Keep the traceability map,
sibling compiler tests, source-language guides, and this inventory
synchronized.
