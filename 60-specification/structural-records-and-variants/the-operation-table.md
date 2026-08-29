---
title: "The Operation Table"
kind: specification
created: "2026-08-29"
status: candidate
spec_version: "0.1.36"
tags:
  - records
  - variants
  - specification
aliases:
  - "Catena record operations"
---

# The Operation Table

## Status and authority

This chapter is the normative Catena 0.1.36 operation-table contract
for structural records and variants. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elevates, without amending, the record and variant rules of
[Sequential Dynamics](../formal-semantic-kernel/sequential-dynamics.md),
the schedules of
[Ordered Forms and Entry Rule](../evaluation-order/ordered-forms-and-entry-rule.md),
and the dispatch of
[Branch Rules Consolidated](../branching/branch-rules-consolidated.md).

The rules apply only to source-language revision `0.1.36`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The operations

> **Normative definition.**

| Operation | Rule | Home |
| --- | --- | --- |
| `record { l = v }` | a closed literal: each label unique, each field a value; a duplicate label is static invalidity (`SR-OBL-002`) | kernel (this slice) |
| `select r l` | evaluates `r` to a record, extracts `l`; the label MUST be present — statically unreachable otherwise | kernel |
| `update r l v` | evaluates `r`, then the replacement value `v`, replaces `l`; the label MUST be present | kernel / C030 |
| `extend r l v` | evaluates `r`, then `v`, adds `l`; closed over a closed input | kernel |
| `restrict r l` | evaluates `r`, removes `l`; closed over a closed input | kernel |
| `inject l v` | a value once `v` is a value; the labeled payload is a value | kernel |
| match on a variant | tests the semantic label, then matches the payload (C033's row) | kernel / C033 |

Field order in a literal or update is an **effect-order fact only**:
written order controls evaluation order (C030) and never equality,
comparison, or row identity (C035/C037) (`SR-OBL-004`). Records are
comparable as semantic maps under C035's structural recursion
(`SR-OBL-005`).

## Duplicate labels

A record literal containing a duplicate label is static invalidity:
the record is a finite **unique-label** map by construction, and the
duplicate never becomes a runtime shape (`SR-OBL-003`). The kernel's
calculus rejects the duplicate at its parse boundary; the JSON AST
carries no record tags to duplicate (the frontend absence, below).

## The frontend absence

The retained frontends encode no record or variant expressions: the
JSON AST tags are frozen at 0.1.1–0.1.7 and the kernel S-expression
at 0.1.8 is the only input expressing them. The operations are
language-level rules over the kernel calculus, witnessed there, and
reach general frontends at P109's spelling era (`SR-OBL-006`) —
C040's frontend-absence pattern, restated for this area.

## Deliberately separate work

Nominal declarations remain C002's, without structural operations.
Collection construction and update remain G042's — records are not
collections. Aliases and newtypes remain G062's. Refutability by
context remains P044's. Spellings remain P109's.

## Rationale and evidence (non-normative)

The [records synthesis](../../20-notes/catena-structural-records.md)
records why consolidation states once what seven chapters scatter —
the C030/C033 pattern's Section 5 debut. The [resolved
inquiry](../../40-inquiries/what-are-structural-records-and-variants.md)
and [topic map](../../10-maps/structural-records.md) preserve the
decision route.
