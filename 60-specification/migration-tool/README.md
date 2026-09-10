---
title: "Migration Tool"
kind: map
created: "2026-09-10"
tags: [specification, migration, tooling, diagnostics]
aliases: []
---

# Migration Tool (`60-specification/migration-tool`)

## Purpose

The normative retained-JSON migration transaction under
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).

## What belongs here

Rules for exact previews, explicit authorization, safe paths, staged writes,
retained backups, rollback, semantic rechecking, audit evidence, finite
resource outcomes, and the P109 public-source hold.

## Index

### Subdirectories

None yet.

### Documents

- [Transactional Retained-JSON Edits](transactional-retained-json-edits.md) — P125's revision 0.1.93 retained-input migration transaction and public-source hold.

## Variability register

No implementation-defined choice, normative recommendation, permission, or
bounded unspecified presentation is introduced. The fixed limits are 32 files,
16,777,216 aggregate decoded preimage bytes, 16,777,216 aggregate decoded
result bytes, and 1,024 edits per plan. Exceeding one produces the distinct
implementation-limit outcome defined by the chapter.

## Maintaining this index

Keep C008 repair applicability, P117 edit structure, C028 interface identity,
P116 provenance, package transactions, implementation limits, and P109 source
adoption aligned.
