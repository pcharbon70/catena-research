---
title: "Source-Text Diagnostics and Conformance"
kind: specification
created: "2026-08-17"
status: normative
spec_version: "0.1.9"
tags:
  - conformance
  - diagnostics
  - parsing
  - specification
  - unicode
aliases:
  - "Catena 0.1.9 source conformance"
---

# Source-Text Diagnostics and Conformance

## Stable diagnostics

Source-envelope failure uses these stable diagnostic identities:

| ID | Meaning |
| --- | --- |
| `SRC001` | malformed UTF-8 or a detected unsupported UTF-16/UTF-32 encoding signature |
| `SRC002` | prohibited leading UTF-8 byte-order mark |
| `SRC003` | carriage return not immediately followed by line feed |

Each diagnostic is an error with a primary original-byte span and a stable
machine-readable `reason`. `SRC001` for a detected alternate signature also
records the detected encoding. Diagnostic prose can improve, but the ID,
classification, repair, span boundary, and meaning-bearing details remain
stable under the corpus-wide presentation rules.

Failure returns no logical source-text result. Source validation writes no
interface, BEAM module, or other successful final artifact, consistently with
the invalid-input rule in the
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md#invalid-input-and-actions).

## Revision and frontend separation

The source-text decoder accepts exact selection edition `0.1`, revision
`0.1.9`, and no preview. An absent standalone selection resolves to that
current source-text selection. Another selected revision reports `EDN001` and
does not reinterpret the bytes through a different frontend.

Revision 0.1.9 adds no JSON AST version, kernel S-expression version,
interface version, artifact version, signature domain, typed-core form, or
BEAM representation. JSON compilation remains bounded by its retained input
formats and compilation-capable revisions; the kernel remains exactly 0.1.8.

The 0.1.9 lifecycle entry is a compatible addition affecting source
acceptance and diagnostics. Its migration text does not convert or
reinterpret a 0.1.8 kernel input.

## Public decoder result

A conforming source-text decoder returns the original bytes, logical text,
ordered scalar units with their original-byte spans, a zero-width end-of-input
span, and the resolved selection. Returning counts or other derived metadata
does not replace those required fields in an API that supplies input to a
later lexer.

The bootstrap compiler exposes this contract as `Catena.decode_source_text/2`
returning `Catena.SourceText`, with `Catena.SourceText.Unit` for scalar/span
pairs.

## Command-line validation

The bootstrap command `catena check-source-text FILE` reads one file and uses
the same decoder. On success it emits one deterministic JSON object with
status, edition, language revision, original byte count, logical scalar count,
and logical newline count. It emits no source contents and creates no output
files.

> **Normative conformance example.**

```json
{
  "byte_count": 4,
  "edition": "0.1",
  "language_revision": "0.1.9",
  "newline_count": 1,
  "scalar_count": 2,
  "status": "ok"
}
```

This decoded example corresponds to the UTF-8 bytes for `é` followed by CRLF.
JSON object-key order is not semantic; the decoded fields and values are
deterministic.

## Required executable evidence

Conformance evidence covers:

- ASCII plus valid two-, three-, and four-byte scalar encodings;
- unassigned scalars, noncharacters, combining marks, U+FFFD, and embedded
  U+FEFF;
- LF, CRLF, mixed endings, absent and present final newlines, and exact
  original-byte spans;
- composed and decomposed spellings accepted and preserved distinctly;
- scalar columns for tabs, combining marks, multibyte scalars, and
  supplementary-plane scalars;
- every UTF-8 malformed-sequence class, detected UTF-16/UTF-32 signatures,
  leading UTF-8 BOM, and lone CR;
- invalid input after a valid multibyte prefix and precise prefix-derived
  positions;
- empty input and its end-of-input span;
- exact source revision selection, deterministic API and CLI results, and
  absence of successful files; and
- regression protection against treating 0.1.9 as a JSON, kernel, interface,
  or compiled-artifact version.

## Conformance obligations

- **ST-OBL-001 — Exact applicability.** A source-text implementation MUST
  apply this envelope only to revision 0.1.9 and MUST preserve all older
  frontend and persisted-format boundaries.
- **ST-OBL-002 — Strict UTF-8.** It MUST accept every otherwise permitted
  well-formed UTF-8 scalar sequence and MUST reject malformed or alternate-
  encoded input without guessing.
- **ST-OBL-003 — No replacement.** It MUST NOT replace, skip, or reinterpret
  malformed bytes as Unicode scalars.
- **ST-OBL-004 — BOM distinction.** It MUST reject a leading UTF-8 BOM as
  `SRC002` and MUST preserve U+FEFF away from the beginning.
- **ST-OBL-005 — Logical newlines.** It MUST map LF and CRLF to one logical LF,
  MUST reject lone CR as `SRC003`, and MUST NOT treat NEL, LINE SEPARATOR, or
  PARAGRAPH SEPARATOR as a 0.1.9 newline.
- **ST-OBL-006 — Normalization preservation.** It MUST NOT normalize or
  normalization-check the source scalar sequence.
- **ST-OBL-007 — Original-byte mapping.** It MUST retain original bytes and a
  source unit for every logical scalar with its original half-open span.
- **ST-OBL-008 — Coordinate model.** It MUST use zero-based byte offsets,
  one-based lines and scalar columns, one newline transition per LF or CRLF,
  and a zero-width end-of-input span.
- **ST-OBL-009 — Stable failure.** It MUST report `SRC001`, `SRC002`, or
  `SRC003` with the specified span and details and MUST publish no successful
  result for invalid input.
- **ST-OBL-010 — Deterministic discovery.** Its public decoder and validation
  command MUST agree on revision, decoded counts, and deterministic result
  fields without creating a compile artifact.

## Implementation limits

This slice introduces no new finite resource dimension or portable floor.
Malformed byte, BOM, and newline rejection are semantic invalidity rather than
implementation-limit exhaustion. Aggregate source size, memory accounting,
cancellation, and hostile-input performance remain outside C013 and cannot be
invented by an implementation profile without a future normative owner under
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md#evolution-and-version-axes).

## Evidence route (non-normative)

The [resolved inquiry](../../40-inquiries/how-should-catena-decode-and-normalize-source-text.md)
records the decision. The [source-text map](../../10-maps/source-text-encoding-and-normalization.md)
connects normative rules, primary evidence, implementation behavior, and the
[C013 verification record](../../50-journal/2026-08-17-c013-source-text-encoding-and-normalization.md).
