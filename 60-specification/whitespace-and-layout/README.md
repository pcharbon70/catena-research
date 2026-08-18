---
title: "Whitespace and Layout Specification"
kind: map
created: "2026-08-17"
tags:
  - archive-navigation
  - directory-index
  - layout
  - specification
  - syntax
  - whitespace
aliases:
  - "Catena 0.1.11 whitespace and layout specification"
---

# Whitespace and Layout Specification (`60-specification/whitespace-and-layout`)

## Purpose

This directory contains the normative Catena 0.1.11 contract for layout
whitespace, indentation invariance, expression separators, line continuation,
delimiter frames, diagnostics, and executable conformance.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, diagnostic presentation, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy applies generally; this area creates no numeric implementation limit.

## What belongs here

Put only whitespace repertoire, indentation meaning, hard and soft line
breaks, semicolon separation, token continuation capabilities, delimiter-frame
line policy, stable layout diagnostics, and C015 conformance obligations here.
Comment syntax and attachment are now defined by the adjacent
[C016 specification](../comments-and-documentation-comments/README.md).
Literal-contained whitespace remains G017; concrete operators, punctuation,
precedence, associativity, and recovery remain G019; complete surface
productions remain P109.

## Variability register

No 0.1.11 layout rule introduces an implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation limit.
Conforming implementations recognize the same layout whitespace, ignore
indentation semantically, classify the same token-event stream identically,
and reject the same interrupted or malformed continuation contexts.

## Index

### Subdirectories

- None yet.

### Documents

- [Whitespace and Indentation](whitespace-and-indentation.md) — applicability,
  inherited logical source, exact whitespace repertoire, token separation,
  indentation invariance, tabs, blank lines, and ownership boundaries.
- [Separators and Line Continuation](separators-and-line-continuation.md) — hard
  LF and semicolon separators, token join capabilities, continued and block
  delimiter frames, EOF, and the lossless classification algorithm.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `LAY001`–`LAY003` failures, the public layout-engine boundary,
  `LY-OBL-001`–`LY-OBL-011`, evidence sets, and revision separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A whitespace-repertoire,
indentation, separator, continuation, delimiter-frame, or diagnostic change
requires an explicit later semantic revision. Keep the traceability map,
sibling compiler tests, source-language guides, and this inventory synchronized.
