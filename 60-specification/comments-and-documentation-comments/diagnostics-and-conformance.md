---
title: "Comments and Documentation Comments Diagnostics and Conformance"
kind: specification
created: "2026-08-18"
status: normative
spec_version: "0.1.12"
tags:
  - comments
  - conformance
  - diagnostics
  - documentation
  - specification
  - testing
aliases:
  - "Catena 0.1.12 comment conformance"
---

# Comments and Documentation Comments Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.12 comment diagnostic, abstract
frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Comment Lexing and Layout](comment-lexing-and-layout.md) and
[Documentation Attachment and Markdown](documentation-attachment-and-markdown.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `CMT001` | the supplied logical-unit index is invalid or does not begin a recognized comment |
| `CMT002` | EOF occurs before all nested block-comment openers are closed |
| `DOC001` | a documentation group is interrupted, lacks its one required LF, or reaches no documentable declaration target |

Every source-derived rejection includes the stable ID and primary original-byte
span when a source unit, delimiter, interruption, or target supplies one
(`CM-OBL-009`). `CMT001` distinguishes index range from a non-comment source
candidate. `CMT002` identifies the outer opener and remaining balance depth.
`DOC001` distinguishes missing LF, blank line, ordinary-comment interruption,
other significant interruption, and EOF; it also retains the first
documentation span.

Diagnostic prose and map-key presentation can improve only within the bounded
rules of the repository conformance vocabulary. Stable ID, source span,
meaning-bearing reason, severity class, and acceptance do not vary.

## Abstract public boundaries

A conforming implementation exposes an equivalent scan operation that accepts
C013 source bytes, an exact 0.1.12 selection, and a lexer-supplied logical-unit
index. It returns one complete comment plus the next unconsumed unit index, or
one diagnostic. A line comment's result index points at its terminating LF or
EOF (`CM-OBL-010`).

A conforming implementation also exposes an equivalent resolve operation over
ordered scanned comments, C015 layout events, and parser-supplied documentable
targets. It returns the lossless classified event stream, documentation
attachments, and exact selection, or one diagnostic.

The bootstrap evidence names these operations `Catena.scan_comment/2` and
`Catena.resolve_comments/2`. Its public records carry comment kind/form,
original units/span, normalized body units/text, internal line-break records,
next index, target identity/span, contributing comments, combined body,
Markdown profile, raw-HTML policy, doctest policy, and exact selection. These
Elixir names and structs are evidence API names, not required names for every
implementation.

C016 defines no whole-source lexer, parser, CLI, Markdown renderer, or doctest
runner (`CM-OBL-010`). Implementations MUST NOT infer comment starts inside
token-owned input or infer concrete declaration targets in this abstract
boundary.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `CM-OBL-001` | apply comment behavior only at 0.1.12 | exact selection and lifecycle tests |
| `CM-OBL-002` | recognize exact line/block/documentation prefix edges and leave line LF unconsumed | delimiter matrix and next-index tests |
| `CM-OBL-003` | balance every nested block opener without a language depth limit | mixed-kind, deep, and EOF-depth tests |
| `CM-OBL-004` | preserve C013 scalars, original spans, and every internal LF without normalization | Unicode, CRLF, unit, and span tests |
| `CM-OBL-005` | normalize documentation bodies by the exact delimiter, edge, and common-margin algorithm | line/block margin and decorative-star tests |
| `CM-OBL-006` | combine adjacent documentation and attach only across the permitted gap to the next target | positive grouping and all interruption tests |
| `CM-OBL-007` | classify every comment-internal LF through unchanged C015 rules | hard, soft, blank, and continued-frame tests |
| `CM-OBL-008` | pin CommonMark, preserve inert raw HTML, and expose exact explicit-only doctest metadata | profile, HTML, fence-label, and no-execution tests |
| `CM-OBL-009` | emit stable `CMT001`, `CMT002`, and `DOC001` failures with reasons and spans | every reason-family test |
| `CM-OBL-010` | keep the scanner/resolver abstract, lossless, and outside token/declaration guessing | supplied-index, target, and event-preservation tests |
| `CM-OBL-011` | make equal inputs and exact selections produce equal scan and resolve results | repeated-result tests |
| `CM-OBL-012` | preserve source-only and persisted-format separation | registry and forged-format tests |

Every obligation has at least one tagged passing test. The sibling compiler
gates the complete `CM-OBL-*` set against unknown and uncovered identifiers
before C016 conformance is claimed.

## Required evidence sets

Positive lexical evidence includes empty and nonempty line comments, EOF,
unconsumed LF, ordinary/documentation prefix edges, nested ordinary and
documentation-looking block openers, deep iterative nesting, Unicode scalar
preservation, LF, and CRLF spans. Negative lexical evidence includes
non-comment candidates, invalid unit indexes, and unterminated nested blocks.

Layout evidence includes no-LF block trivia and comment-internal soft, hard,
and repeated blank LFs. Documentation evidence includes line/block
normalization, exact SPACE/TAB common margin, decorative stars, multiple
adjacent comments, a valid target, missing LF, blank line, ordinary comment,
semicolon, significant token, non-documentable construct, and EOF.

Documentation-format evidence retains CommonMark source containing raw HTML,
records the exact profile and doctest info string, and demonstrates the absence
of rendered HTML or execution results at this boundary.

## Revision and persistence separation

Revision `0.1.12` is a compatible source-acceptance, static-meaning, and
diagnostic addition. Its static meaning includes documentation attachment and
metadata. It adds no JSON AST version,
kernel S-expression version, interface version, artifact version, signature
domain, typed-core form, runtime behavior, or BEAM representation
(`CM-OBL-001`, `CM-OBL-012`).

At the C016 boundary, source-text applicability is cumulative from `0.1.9`
through `0.1.12`; C017 subsequently adds source-only revision `0.1.13`.
The standalone C014 identifier APIs retain exact 0.1.10. The public C015 layout
resolver retains exact 0.1.11, including its default selection. Comment scanning
and resolution require exact 0.1.12. The next unused semantic patch is
`0.1.14` after C017's exact 0.1.13 atomic literal boundary.

## Rationale and evidence (non-normative)

The design route is preserved in the
[comment synthesis](../../20-notes/catena-comments-and-documentation-comments.md),
[resolved inquiry](../../40-inquiries/how-should-catena-handle-comments-and-documentation-comments.md),
and [topic map](../../10-maps/comments-and-documentation-comments.md). The
[C016 record](../../50-journal/2026-08-18-c016-comments-and-documentation-comments.md)
records the concrete sibling-compiler commands and archive validation.
