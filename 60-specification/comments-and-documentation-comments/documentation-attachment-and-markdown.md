---
title: "Documentation Attachment and Markdown"
kind: specification
created: "2026-08-18"
status: normative
spec_version: "0.1.12"
tags:
  - comments
  - documentation
  - markdown
  - specification
  - syntax
aliases:
  - "Catena documentation comments"
---

# Documentation Attachment and Markdown

## Status and authority

This chapter is the normative Catena 0.1.12 documentation-body, attachment,
Markdown, raw-HTML, and doctest-selection contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It consumes documentation comments recognized by
[Comment Lexing and Layout](comment-lexing-and-layout.md).

## Documentation body normalization

A line documentation body is formed by removing the exact `///` opener and
then removing one immediately adjacent U+0020 SPACE when present. No tab or
second space is removed.

A block documentation body is formed in this order (`CM-OBL-005`):

1. remove the outer `/**` opener and matching `*/` closer;
2. remove one immediately adjacent U+0020 SPACE at the beginning and one at
   the end when present;
3. remove every leading or trailing line whose remaining content is only
   U+0020 SPACE and U+0009 TAB, including the logical LF separating that edge
   line from retained content;
4. calculate the longest exact SPACE/TAB prefix shared by every nonblank
   retained line; and
5. remove that prefix from each retained line that has it.

Blank interior lines remain. Every scalar and source span not removed by these
steps remains in order. Tabs and spaces are compared as distinct scalars; no
tab width or display column participates. A leading `*` is content and MUST NOT
be stripped as a decorative margin convention.

Normalization neither parses Markdown nor changes Unicode normalization. It
produces normalized body units and their corresponding UTF-8 text.

## Grouping and declaration attachment

One or more adjacent documentation comments form a documentation group. Between
two comments in the group, only horizontal C015 whitespace and zero or one
logical LF can occur. Their normalized bodies combine in source order with one
logical LF between bodies.

A group attaches only to the next parser-supplied documentable declaration
target. Between the final comment and that target, only horizontal whitespace
and exactly one logical LF can occur. The target contributes a stable
declaration identity and source span to the attachment (`CM-OBL-006`).

An ordinary comment, blank line, semicolon, significant token,
non-documentable construct, absent required LF, or EOF before a valid target
breaks attachment. The group is then ill-formed and produces `DOC001`; an
implementation MUST NOT silently discard it, attach it across the interruption,
or reinterpret it as inner/enclosing documentation (`CM-OBL-006`,
`CM-OBL-009`).

P109 enumerates concrete documentable declaration productions. C016's
executable boundary uses parser-supplied abstract targets so it does not guess
that future grammar. G020 separately defines file/module relationships.

## Markdown profile

Each attachment carries the exact profile label `commonmark-0.31.2`. A
documentation consumer parses the combined normalized body according to
[CommonMark Specification 0.31.2](../../30-sources/macfarlane-2024-commonmark-specification.md).
Unversioned “Markdown,” another CommonMark version, GitHub-flavored Markdown,
or a renderer's ambient default is not an equivalent profile
(`CM-OBL-008`).

C016 requires preservation of the normalized Markdown source and does not
require the compiler frontend to render it. Symbol links, generated-document
containers, navigation, and output formats remain G110.

## Raw HTML safety

CommonMark raw HTML remains present in the normalized source and parse result.
A tool can display it as escaped text or sanitize it under a separately
documented policy. A renderer MUST NOT place raw documentation HTML into an
executable context without sanitization and MUST NOT execute scripts, event
handlers, active URLs, or equivalent active content directly from the
documentation source (`CM-OBL-008`).

This safety obligation does not authorize the compiler to delete or normalize
the original Markdown source stored in the attachment.

## Doctest selection

Fenced code is non-executable documentation by default. After CommonMark
extracts a fence info string, trimming its leading and trailing whitespace
opts the block into future doctest processing only when the complete remaining
string is exactly `catena doctest` (`CM-OBL-008`). Case differs; additional
words differ; `catena` alone and `doctest` alone differ.

C016 records `explicit_only` doctest policy and the exact info string but
executes no documentation. An implementation claiming only 0.1.12 MUST NOT
evaluate a documentation block, publish an execution result, or reject a
program because a prospective doctest result differs. G119 owns the future
runner, language selection, environment, effects, expected-output syntax,
budgets, isolation, and build consequences.

## Rationale and evidence (non-normative)

The [Elixir documentation note](../../30-sources/elixir-project-2026-writing-documentation.md)
supports separating documentation from source comments and doctest execution
from documentation storage. The
[Rust comments note](../../30-sources/rust-project-2026-rust-comments.md)
supports forward outer documentation; Catena deliberately omits its inner
variant. The [CommonMark note](../../30-sources/macfarlane-2024-commonmark-specification.md)
explains the version and raw-HTML boundary.
