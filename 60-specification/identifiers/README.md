---
title: "Identifier Specification"
kind: map
created: "2026-08-17"
tags:
  - archive-navigation
  - directory-index
  - identifiers
  - security
  - specification
  - unicode
aliases:
  - "Catena 0.1.10 identifier specification"
---

# Identifier Specification (`60-specification/identifiers`)

## Purpose

This directory contains the normative Catena 0.1.10 contract for standalone
ergonomic identifiers, qualified names, keyword escapes, Unicode security, and
confusable-name diagnostics.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, diagnostic promotion, and variability.
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
controls finite-resource refusal; this area adds no implementation limit.

## What belongs here

Put only identifier repertoire, normalization, case equality, qualification,
reserved-word escaping, Unicode security filtering, confusable comparison,
stable diagnostics, and C014 conformance obligations here. Whole-source token
boundaries remain later work, while whitespace and layout now live in the
normative [0.1.11 area](../whitespace-and-layout/README.md). Comments, literals,
concrete operators, namespace membership, shadowing, name resolution, imports,
exports, and file/module relations remain later checklist work.

## Variability register

No 0.1.10 identifier rule introduces an implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation limit.
Conforming implementations use the same pinned Unicode data, accept and reject
the same standalone names, and produce the same canonical segments and stable
diagnostic families. Project policy can promote `IDN007` using the already
normative diagnostic-denial mechanism; that explicit input is not hidden
implementation variability.

## Index

### Subdirectories

- None yet.

### Documents

- [Identifier Syntax and Equivalence](identifier-syntax-and-equivalence.md) —
  Unicode version, XID production, NFC spelling, case, identity, source spans,
  applicability, and exclusion rules.
- [Qualification, Keywords, and Security](qualification-keywords-and-security.md)
  — dot-separated paths, backtick escapes, the closed word set, General
  Security Profile, Highly Restrictive scripts, and confusable comparison.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `IDN001`–`IDN007` outcomes, public API and CLI results, obligation
  identifiers, executable evidence, and promotion boundary.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A Unicode-data change,
repertoire change, normalization change, keyword addition, identity change, or
security-policy change requires an explicit later semantic revision. Keep the
traceability map, compiler data manifest, source guide, and this inventory in
sync with every rule change.
