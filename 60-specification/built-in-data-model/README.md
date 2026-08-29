---
title: "Built-In Data Model Specification"
kind: map
created: "2026-08-29"
tags:
  - archive-navigation
  - directory-index
  - data-model
  - specification
aliases:
  - "Catena 0.1.35 data model specification"
---

# Built-In Data Model Specification (`60-specification/built-in-data-model`)

## Purpose

This directory contains the Catena 0.1.35 contract for the built-in
data model: the twelve-way classification, the Text, Character, and
Bytes types with their elaboration semantics, the content-based
comparability entries, the frontend-absence statement, the abstract
boundaries, and executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy governs resource disclosure; this area adds no new dimension.

## What belongs here

Put the classification, the three types' semantics, the comparability
entries, and C040 conformance obligations here. The literal grammar
remains C017's. The elaboration pattern remains C018's. The value
grammar and entry rule remain C029's. The comparable set remains
C035's. Coverage entries remain C033's. Collection declarations
remain G101's. Construction and update remain G042's. References
remain G084's. String libraries remain G105's. Spellings and the
compiled-program path for text literals remain P109's.

## Variability register

This area introduces no implementation-defined choice, recommendation,
bounded unspecified presentation, or implementation limit. Elaboration
and classification are deterministic; content semantics bind while
representation stays free per C037; no registry or tooling behavior
may vary.

## Index

### Subdirectories

- None yet.

### Documents

- [The Twelve-Way Classification](the-twelve-way-classification.md)
  — the per-type decision table and its consequences under each
  entry rule.
- [Text, Character, and Bytes](text-character-and-bytes.md) — the
  three new types' semantics, elaboration determinism, comparability
  entries, and the frontend-absence statement.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — the
  zero-new-families contract, the elaboration and classifier
  boundaries, `BM-OBL-001`–`BM-OBL-008`, evidence sets, and
  persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A
classification, type, or entry change requires an explicit later
semantic revision. Collections arrive as library nominal types at
G101; references stay excluded until gated. Keep the traceability
map, sibling compiler tests, source-language guides, and this
inventory synchronized.
