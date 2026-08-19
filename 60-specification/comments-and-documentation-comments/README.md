---
title: "Comments and Documentation Comments Specification"
kind: map
created: "2026-08-18"
tags:
  - archive-navigation
  - comments
  - directory-index
  - documentation
  - specification
  - syntax
aliases:
  - "Catena 0.1.12 comments specification"
---

# Comments and Documentation Comments Specification (`60-specification/comments-and-documentation-comments`)

## Purpose

This directory contains the normative Catena 0.1.12 contract for ordinary
comments, nested block balancing, comment-owned line breaks, documentation
comment normalization and attachment, Markdown and doctest policy, diagnostics,
and executable conformance.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, diagnostic presentation, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy applies generally; this area creates no numeric implementation limit.

## What belongs here

Put slash-comment delimiters and balancing, their C013 source-unit and C015
layout behavior, outer documentation classification, body normalization,
forward declaration attachment, CommonMark/raw-HTML/doctest policy, stable
diagnostics, and C016 conformance obligations here. Atomic literal bodies are
defined by C017; concrete operator/punctuation tokenization remains G019; complete
documentable declarations remain P109; file/module ownership remains G020;
rendering and formatting remain G110/G118; executable doctest semantics remain
G119.

## Variability register

No 0.1.12 comment rule introduces an implementation-defined choice,
recommendation, bounded unspecified presentation, or implementation limit.
Conforming implementations recognize the same comment forms and nesting,
preserve the same line events and source spans, produce the same normalized
documentation bodies and attachments, apply the same CommonMark and doctest
metadata, and reject the same malformed or unattached inputs.

## Index

### Subdirectories

- None yet.

### Documents

- [Comment Lexing and Layout](comment-lexing-and-layout.md) — exact line/block
  forms, documentation prefix edges, balanced nesting, source preservation,
  token ownership, and C015 LF integration.
- [Documentation Attachment and Markdown](documentation-attachment-and-markdown.md)
  — body normalization, adjacent grouping, forward declaration attachment,
  CommonMark 0.31.2, raw-HTML safety, and explicit doctest opt-in.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  `CMT001`, `CMT002`, and `DOC001` failures, abstract public operations,
  `CM-OBL-001`–`CM-OBL-012`, evidence sets, and revision separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A delimiter, nesting,
layout, normalization, attachment, Markdown, doctest-policy, or diagnostic
change requires an explicit later semantic revision. Keep the traceability
map, sibling compiler tests, source-language guides, and this inventory
synchronized.
