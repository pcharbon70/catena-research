---
title: "Text, Character, and Bytes"
kind: specification
created: "2026-08-29"
status: candidate
spec_version: "0.1.35"
tags:
  - data-model
  - text
  - specification
aliases:
  - "Catena text types"
---

# Text, Character, and Bytes

## Status and authority

This chapter is the normative Catena 0.1.35 Text, Character, and
Bytes contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It elaborates the scanner kinds of
[Text, Characters, and Bytes](../literal-grammar/text-characters-and-bytes.md)
under the pattern of
[Numeric Literal Semantics](../numeric-literal-semantics/README.md).

The rules apply only to source-language revision `0.1.35`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## The three types

> **Normative definition.**

```text
Text      ::= scalar-sequence       -- the decoded payload
Character ::= one Unicode scalar    -- its code point
Bytes     ::= byte-sequence
```

- **Text** is the sequence of Unicode scalars decoded from a text
  literal (cooked or raw); its identity is the decoded content —
  raw-hash counts, provenance, and source units remain scanner facts
  at 0.1.13 and never reach the value.
- **Character** is exactly one Unicode scalar, decoded to its code
  point; the scanner's one-scalar guarantee is trusted, not
  re-validated.
- **Bytes** is the sequence of decoded bytes.

## Elaboration

> **Normative definition.**

```text
elaborate : scanned-literal -> meaning
meaning   = { kind : text | character | bytes
            , type : Text | Character | Bytes
            , value : the decoded content }
```

Elaboration is **deterministic and total** over successfully scanned
literals: equal source bytes under exact selection produce equal
meanings (`BM-OBL-003`), riding C017's decoded-payload guarantee.
Cooked and raw forms of equal content elaborate to equal meanings —
form and hash count are scanner facts, not value facts.

## The frontend absence

The retained frontends encode no text, character, or bytes
expression: the JSON AST tags are frozen at 0.1.1–0.1.7 and the
kernel at 0.1.8. The three types therefore live at the **meaning and
classifier level** — values, comparisons, and orders are defined and
witnessed — and flow into compiled programs when a frontend can
encode their literals, at P109's spelling era (`BM-OBL-006`). This
is exactly Float's post-C018 status, stated as the witness-honesty
clause rather than left implicit.

## Comparability entries

Executing C035's rule (`BM-OBL-004`):

| Type | Equality | Order |
| --- | --- | --- |
| Text | structural: equal scalar sequences | lexicographic by code point |
| Character | equal scalars | by code point |
| Bytes | structural: equal byte sequences | lexicographic by byte |

The orders are total — no NaN-like special cases exist — and both
comparisons and orders observe content only, per C037's semantic
identity: representation (encoding, interning, chunking) is invisible.

## Determinism

Equal literals elaborate to equal meanings and compare equally on
every conforming target (`BM-OBL-008`); content semantics bind,
representation stays free.

## Deliberately separate work

Interpolation remains permanently excluded for unprefixed and `r`
forms (C017); string libraries remain G105's; the compiled-program
path and spellings remain P109's; byte-vs-text library conversions
remain G105.

## Rationale and evidence (non-normative)

The [data-model synthesis](../../20-notes/catena-built-in-data-model.md)
records why three types mirror the three scanner kinds and why the
content orders are the natural entries. The [topic
map](../../10-maps/built-in-data-model.md) routes the decision.
