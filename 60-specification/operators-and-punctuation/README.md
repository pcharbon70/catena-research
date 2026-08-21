---
title: "Operators and Punctuation Specification"
kind: map
created: "2026-08-21"
tags:
  - archive-navigation
  - directory-index
  - operators
  - specification
  - syntax
aliases:
  - "Catena 0.1.15 operator specification"
---

# Operators and Punctuation Specification (`60-specification/operators-and-punctuation`)

## Purpose

This directory contains the Catena 0.1.15 contract for operator and
punctuation tokens: the closed semantic-mapped inventory with maximal-munch
boundaries, reserved-spelling rejection, the concrete C015 continuation
capabilities and delimiter-frame assignments, the fixed precedence ladder
and associativity rules, the whole-source token stream and bounded
operator-expression layer, stable diagnostics, and executable conformance
obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, diagnostic presentation, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs aggregate-input disclosure; this area adds no new resource
dimension and defers aggregate token-count limits to the G129 owner.

## What belongs here

Put operator and punctuation spelling, munching boundaries against the
C014–C018 atoms, reserved spellings, per-token continuation capabilities,
delimiter families and frame modes, the precedence ladder and
associativity, pipe elaboration structure, operator-expression diagnostics,
and C019 conformance obligations here. Application and declaration grammar
and the `->` clause structure remain P109. File-to-module relations remain
G020. Qualified-name resolution remains G021/G022. Field-like access and the
wider built-in data model remain G040. Operator trait dispatch remains G061.
Type-directed resolution questions remain G066. Editor recovery remains
G123.

## Variability register

This area introduces no implementation-defined choice, recommendation, or
bounded unspecified presentation. It introduces no implementation limit. The
whole-source token stream consumes the existing C013–C018 per-token limits;
aggregate file and token-count limits remain with the G129 owner and are not
created here.

## Index

### Subdirectories

- None yet.

### Documents

- [Token Inventory and Maximal Munch](token-inventory-and-maximal-munch.md)
  — the closed operator and punctuation set, exact spellings, munch
  boundaries against identifiers, literals, and numeric components,
  reserved spellings, and the ASCII rule.
- [Capabilities and Delimiter Frames](capabilities-and-delimiter-frames.md)
  — the concrete `join_before`/`join_after` assignments, delimiter families
  and frame modes, separator roles, and the `.` interaction with C014
  qualified names.
- [Precedence and Associativity](precedence-and-associativity.md) — the
  fixed ladder, per-level associativity, non-associative comparisons,
  prefix negation and not, the pipe elaboration relation, and the declared
  absence of fixity declarations.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `OPR001`–`OPR002`, the abstract tokenize and parse boundaries,
  `OP-OBL-001`–`OP-OBL-016`, evidence sets, and persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A token spelling,
capability, frame, ladder level, associativity, or diagnostic change
requires an explicit later semantic revision. Keep the traceability map,
sibling compiler tests, source-language guides, and this inventory
synchronized.
