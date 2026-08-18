---
title: "Comment Lexing and Layout"
kind: specification
created: "2026-08-18"
status: normative
spec_version: "0.1.12"
tags:
  - comments
  - layout
  - specification
  - syntax
aliases:
  - "Catena comment lexing"
---

# Comment Lexing and Layout

## Status and authority

This chapter is the normative Catena 0.1.12 ordinary-comment,
documentation-comment classification, and layout-integration contract. It is
governed by [Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes the logical source units from the
[Source-Text Envelope](../source-text/source-text-envelope.md) and delegates
line classification to
[Separators and Line Continuation](../whitespace-and-layout/separators-and-line-continuation.md).

The rules apply to source-only revision `0.1.12`. They do not reinterpret
retained JSON ASTs, the exact 0.1.8 kernel S-expression, interfaces, artifacts,
or signed formats.

## Comment forms

The exact comment forms are:

| Opener | Form | Classification | Terminator |
| --- | --- | --- | --- |
| `//` | line | ordinary unless the exact outer rule below applies | immediately before logical LF, or EOF |
| `///` | line | documentation when the next scalar is not `/` | immediately before logical LF, or EOF |
| `/*` | block | ordinary unless the exact outer rule below applies | matching balanced `*/` |
| `/**` | block | documentation when the next scalar is neither `*` nor `/` | matching balanced `*/` |

`////` begins an ordinary line comment. `/***` begins an ordinary block
comment. `/**/` is an empty ordinary block comment. `//!` and `/*!` are
ordinary comments; Catena defines no inner-documentation form
(`CM-OBL-002`). An implementation MUST apply these exact prefix distinctions
and MUST NOT choose the longest documentation-looking prefix by recovery.

A line comment consumes its opener and every following source unit through the
last unit before logical LF or EOF. The terminating logical LF is not part of
the comment and remains the next source event (`CM-OBL-002`).

Comment recognition occurs only at a lexer-supplied position outside any
already recognized token. This chapter does not reinterpret slash or asterisk
inside a literal, identifier, or another token. G019 owns the complete
maximal-token decision.

## Nested block comments

After the outer `/*`, each `/*` increments the block-comment nesting depth and
each `*/` decrements it. The comment ends when the depth first returns to zero.
Every nested opener participates, including `/**` and `/*!`; the outer opener
alone determines whether the completed comment is ordinary or documentation
(`CM-OBL-003`).

EOF at nonzero depth is malformed and produces `CMT002`. A conforming scanner
MUST balance nesting without recursion in the source language's semantics and
MUST NOT impose a Catena nesting-depth limit. An implementation resource
refusal, if one becomes necessary, is an implementation limit governed by the
repository limit policy and cannot be reported as a different comment grammar.

## Source units and body preservation

A comment record retains, in source order:

- its ordinary/documentation classification and line/block form;
- every original C013 source unit from the first opener unit through the last
  consumed unit;
- the half-open original-byte span covering those units;
- its body units and body text after only the documentation normalization
  defined in [Documentation Attachment and Markdown](documentation-attachment-and-markdown.md);
  and
- one line-break record for every logical LF inside the comment.

Ordinary comment bodies remove only their delimiters. Comment scanning performs
no escape interpretation, Unicode normalization, scalar replacement, or
line-ending conversion beyond the already completed C013 source decoding
(`CM-OBL-004`). Every scalar accepted by C013 is valid comment content unless
it participates in the ASCII delimiter pairs.

## Layout integration

For significant-token adjacency, a comment is trivia. Removing its non-LF
content does not create a significant token or satisfy a required left or
right expression.

For layout, every logical LF inside a comment is inserted at its original
ordered position in the C015 event stream. The line comment's unconsumed
terminating LF remains the ordinary surrounding event. A same-line block
comment contributes no LF. A block comment with multiple LFs contributes each
one separately; an implementation MUST NOT erase them, collapse them into one
synthetic LF, or move them outside the comment span (`CM-OBL-004`,
`CM-OBL-007`).

C015 classifies those LFs as `soft`, `separator`, or `blank` from the same
delimiter frames and adjacent significant-token capabilities used for
non-comment LFs. Comment kind, body text, indentation, and nesting depth do not
create a separate layout rule.

The resolved comment stream retains the original ordered comment, token,
horizontal-whitespace, logical-LF, semicolon, and declaration-target events.
Only line-break classification and documentation attachments are added.

## Rationale and evidence (non-normative)

The [comment synthesis](../../20-notes/catena-comments-and-documentation-comments.md)
compares Rust and Swift nesting with ECMAScript line preservation and explains
why Catena preserves every internal LF. The
[resolved inquiry](../../40-inquiries/how-should-catena-handle-comments-and-documentation-comments.md)
and [topic map](../../10-maps/comments-and-documentation-comments.md) preserve
the wider decision route.
