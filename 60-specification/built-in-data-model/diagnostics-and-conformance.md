---
title: "Built-In Data Model Diagnostics and Conformance"
kind: specification
created: "2026-08-29"
status: normative
spec_version: "0.1.35"
tags:
  - conformance
  - diagnostics
  - data-model
  - specification
  - testing
aliases:
  - "Catena 0.1.35 data model conformance"
---

# Built-In Data Model Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.35 data-model diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Twelve-Way Classification](the-twelve-way-classification.md)
and [Text, Character, and Bytes](text-character-and-bytes.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`BM-OBL-001`,
`BM-OBL-008`). Scanned-literal rejections are C017's `LT` families;
no new invalid input exists — elaboration is total over scanned
literals, and the classification accepts nothing new into any
frontend.

## Abstract public boundaries

Three boundaries gain data-model wiring; the bootstrap adds the
elaboration module (`BM-OBL-001`):

- **Elaboration** — `Catena.Text.elaborate/2` turns a scanned text,
  character, or bytes literal into its typed meaning
  (`Text.Meaning`), the `Numeric.Meaning` shape, deterministic and
  total.
- **Value classification** — `Catena.Values` admits Text, Character,
  and Bytes in both carriers, comparable and orderable per the
  entries; kind-carrying meanings classify by kind, and bare binaries
  classify conservatively by content.
- **Type classification** — `Catena.Data.comparable_type?/2` admits
  the three new type atoms with their orderability.

Implementations MUST NOT use these boundaries to claim collection
built-ins, references, interpolation, or any excluded machinery
(`BM-OBL-008`).

## Determinism

Equal literals produce equal meanings, comparisons, and orders on
every target (`BM-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `BM-OBL-001` | apply data-model behavior only at exact 0.1.35 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `BM-OBL-002` | fix the twelve-way classification with the seven shipped types restated unchanged | classification-shape tests |
| `BM-OBL-003` | elaborate the three scanner kinds deterministically and totally, cooked/raw form-irrelevant over equal content | elaboration determinism tests |
| `BM-OBL-004` | execute the content-based comparability entries: three new comparable-and-orderable types with total orders | classifier and order tests |
| `BM-OBL-005` | keep collections as library territory and references excluded, both gated | absence tests |
| `BM-OBL-006` | state the frontend absence honestly: no compiled-program text literals; coverage entries at P109 | absence tests |
| `BM-OBL-007` | keep the Character one-scalar invariant and Text/Bytes content identity | invariant tests |
| `BM-OBL-008` | keep the model deterministic and outside G042/G084/G101/G105/P109 claims with zero new families | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `BM-OBL-*` set against unknown and
uncovered identifiers before C040 conformance is claimed.

## Required evidence sets

Positive evidence includes cooked text, raw text, character, and bytes
literals elaborating to their typed meanings with determinism;
cooked and raw forms of equal content elaborating to equal meanings;
the one-scalar character invariant; the classifier matrix (three new
value forms, comparable, orderable; Unit still non-comparable;
handles and closures still never); and the content orders (code-point
and byte sequences at the comparison level).

Negative evidence — in the definitional sense — includes no
collection built-in, reference, or interpolation entry points; no
frontend encoding of text literals; and no new family appearing.

Exclusion evidence demonstrates unchanged C017 `LT` identities,
unchanged predecessor diagnostic identities, and predecessor APIs
retaining their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.35` adds the classification, the three types, the
elaboration operation, and the comparability entries; it adds no
JSON AST version, kernel S-expression version, interface version,
artifact version, signature domain, typing rule, runtime behavior,
BEAM representation, manifest field, or diagnostic family, and
amends no retained revision (`BM-OBL-001`, `BM-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.35`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.36`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[data-model synthesis](../../20-notes/catena-built-in-data-model.md),
the [resolved inquiry](../../40-inquiries/which-types-are-built-in.md),
and the [topic map](../../10-maps/built-in-data-model.md). The C040
evidence record will preserve the sibling-compiler commands and
archive validation.
