---
title: "Text, Characters, and Bytes"
kind: specification
created: "2026-08-18"
status: normative
spec_version: "0.1.13"
tags:
  - bytes
  - characters
  - literals
  - specification
  - text
aliases:
  - "Catena text and byte literals"
---

# Text, Characters, and Bytes

## Status and authority

This chapter is the normative Catena 0.1.13 text, character, byte, escape,
preservation, and literal-line-ownership contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It refines the atomic set in
[Literal Forms and Boundaries](literal-forms-and-boundaries.md).

## Text, character, and byte forms

> **Normative definition.**

```ebnf
cooked-text       = '"', { cooked-text-item }, '"' ;
character         = "'", { cooked-character-item }, "'" ;
cooked-bytes      = "b", '"', { cooked-byte-item }, '"' ;

raw-text-opener   = "r", { "#" }, '"' ;
raw-byte-opener   = "br", { "#" }, '"' ;
```

A raw opener records its number of `#` scalars. Its closer is a double quote
followed by exactly that many `#` scalars. A quote followed by fewer hashes is
content; the required closer can occur later. Hash count has no language-level
maximum and is matched iteratively (`LT-OBL-004`). Only lowercase `r`, `b`,
and `br` prefixes exist; `rb` is not a prefix.

Cooked text and byte literals use double quotes. A character literal uses
single quotes. Cooked forms cannot contain a C013 logical LF directly and
cannot use backslash-newline continuation. Raw forms can contain logical LF.

## Cooked escape decoding

The complete simple escape set is:

| Escape | Decoded scalar or octet |
| --- | --- |
| `\0` | zero |
| `\t` | tab |
| `\n` | line feed |
| `\r` | carriage return |
| `\\` | backslash |
| `\"` | double quote |
| `\'` | single quote |

`\xHH` contains exactly two hexadecimal digits. In text and character
literals its value is at most U+007F. In byte literals it contributes the
full octet range 0 through 255.

`\u{H...}` contains one through six hexadecimal digits and denotes one Unicode
scalar value. Values above U+10FFFF and surrogate code points U+D800 through
U+DFFF are malformed. Unicode escapes are not accepted in byte literals.
Unknown escapes and backslash followed by logical LF are malformed
(`LT-OBL-006`, `LT-OBL-009`).

## Text preservation

Direct text and character content consists of the already decoded C013
Unicode scalars other than the active delimiter, backslash, and cooked logical
LF. Escape decoding replaces only the explicit escape source units with their
defined contribution. Text decoding performs no NFC, NFD, NFKC, NFKD,
grapheme, case, or compatibility transformation (`LT-OBL-005`).

A character literal decodes to exactly one Unicode scalar, not one grapheme
cluster or one display cell. An empty character or a sequence such as `e`
followed by U+0301 is malformed; a single supplementary-plane scalar is valid
(`LT-OBL-006`).

## Byte content

Direct content in cooked and raw byte literals is ASCII U+0000 through
U+007F. A non-ASCII direct scalar is malformed even when its UTF-8 encoding
could be copied as several bytes. Cooked `\xHH` is the only escape that can
contribute an octet above 127. The decoded payload is an ordered byte sequence,
not necessarily UTF-8 text (`LT-OBL-006`).

## Decoded payload and provenance

Every successful text, character, or byte result retains:

- its kind and cooked or raw form, including raw hash count;
- the logical lexeme and every original C013 unit from opener through closer;
- one half-open original-byte span covering those units;
- its decoded payload;
- ordered provenance pieces classified as `verbatim` or `escape`, each with
  exact contributing source units, merged original-byte span, and decoded
  contribution; and
- every literal-owned logical LF in source order.

Delimiter units are retained by the literal but do not create decoded pieces.
Equal source bytes, exact selection, and unit index produce equal decoded
payloads and provenance (`LT-OBL-005`, `LT-OBL-010`, `LT-OBL-011`).

## Raw line-break ownership

Every logical LF between a raw opener and its exact closer belongs to the
literal token. It contributes U+000A to raw text or octet 10 to raw bytes and
appears in the literal-owned line-break list with its C013 original-byte span.
It is not a C015 layout line-break event and cannot separate, continue, or
blank an enclosing form (`LT-OBL-007`).

Cooked forms contain no source LF, although `\n` can contribute a decoded LF
without creating a source line event. This distinction prevents an escape
from manufacturing layout.

## Static text and future interpolation

Cooked and raw text defined by 0.1.13 are permanently non-interpolating.
Identifier-looking content and braces are ordinary literal content. A future
interpolated form uses a new opt-in prefix and later revision; it cannot
reinterpret an existing unprefixed or `r`-prefixed token (`LT-OBL-002`,
`LT-OBL-012`).

## Rationale and evidence (non-normative)

The [literal synthesis](../../20-notes/catena-literal-grammar.md) explains the
closed escape set, exact hash delimiters, static-text compatibility rule, and
separation between scalar text and byte payloads. The
[Rust literal source note](../../30-sources/rust-project-2026-literal-tokens.md),
updated [Python lexical note](../../30-sources/python-software-foundation-2026-python-lexical-analysis.md),
and updated [Swift lexical note](../../30-sources/swift-project-2026-lexical-structure.md)
preserve the comparative evidence.
