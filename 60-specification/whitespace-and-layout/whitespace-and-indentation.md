---
title: "Whitespace and Indentation"
kind: specification
created: "2026-08-17"
status: normative
spec_version: "0.1.11"
tags:
  - layout
  - specification
  - syntax
  - whitespace
aliases:
  - "Catena whitespace repertoire"
---

# Whitespace and Indentation

## Status and authority

This chapter is the normative Catena 0.1.11 whitespace and indentation
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the logical scalar stream and original-byte spans defined by the
[Source-Text Envelope](../source-text/source-text-envelope.md) and preserves
the name rules in the
[Identifier Specification](../identifiers/README.md).

The rules apply to the source-only revision `0.1.11`. They do not reinterpret
retained JSON ASTs, the exact 0.1.8 kernel S-expression, interfaces, artifacts,
or signed formats.

## Layout whitespace

Outside a token, comment, or literal, a layout-whitespace scalar is exactly one
of:

- U+0020 SPACE;
- U+0009 CHARACTER TABULATION; or
- the logical U+000A LINE FEED produced by C013.

No other scalar is layout whitespace (`LY-OBL-002`). U+000B, U+000C, U+0085,
U+00A0, U+200E, U+200F, U+2028, U+2029, U+3000, and every other Unicode space
or line-separator scalar are invalid outside a later token class that
explicitly admits them. They produce `LAY001` over the offending original-byte
span.

C013 remains the sole owner of byte decoding and physical line formation.
CRLF supplies one logical LF with a two-byte span; LF supplies one logical LF
with a one-byte span; lone CR is rejected as `SRC003` before layout processing
(`LY-OBL-009`).

## Horizontal whitespace and token separation

A nonempty run of SPACE or TAB is horizontal whitespace. Horizontal whitespace
is trivia after it has separated adjacent tokens where concatenating their
spellings would otherwise produce a different tokenization. The concrete token
grammar owns that maximal-token decision.

The layout result retains each horizontal-whitespace run and its ordered source
units. A parser can ignore the run; a formatter, diagnostic renderer, or
concrete-syntax tree can preserve it (`LY-OBL-010`).

## Indentation has no semantic effect

Leading horizontal whitespace is governed by the same rule as horizontal
whitespace elsewhere. An implementation MUST NOT emit indentation or
dedentation tokens, open or close a block, insert a separator, choose a
delimiter mode, or change token capabilities because of a line's indentation
(`LY-OBL-003`).

Replacing one leading SPACE/TAB run with another legal SPACE/TAB run leaves
the significant token sequence, separator classification, and continuation
classification unchanged. This rule applies to empty indentation, mixed spaces
and tabs, and tabs at any scalar column.

TAB advances the C013 language column by one scalar. Catena defines no tab
stop, tab expansion, indentation width, display-cell width, or mixed-indentation
error. Presentation tools can recommend or normalize indentation only when
their edits preserve the classified token-event stream.

## Blank layout

A logical LF before any significant token is blank. After a hard separator,
additional logical LFs before the next significant token are blank. Blank LFs
remain in the lossless result but do not create empty expressions
(`LY-OBL-005`).

End of file can terminate a complete final form without a final LF. Horizontal
whitespace and blank logical LFs are also valid after the final hard separator.

## Token ownership boundary

The whole-source lexer applies this chapter only after recognizing token-owned
regions. A string, character, documentation body, or comment can contain a
scalar that is not layout whitespace when its own later specification admits
that scalar. Such content reaches the layout engine as part of one opaque token
or comment event, not as layout whitespace (`LY-OBL-011`).

G016 defines whether a comment terminator contributes a logical line break to
the surrounding layout stream. G017 defines literal-contained newlines and
spaces. G019 defines concrete punctuation and operators. Until those owners
are complete, the C015 executable boundary accepts lexer-supplied abstract
token events rather than claiming a whole-source lexer.

## Rationale and evidence (non-normative)

The selected model and rejected alternatives are developed in
[Catena Whitespace, Layout, and Line Continuation](../../20-notes/catena-whitespace-layout-and-line-continuation.md).
The [resolved inquiry](../../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md)
and [topic map](../../10-maps/whitespace-layout-and-line-continuation.md) route
through the Elixir, Python, Haskell, and Rust comparisons.
