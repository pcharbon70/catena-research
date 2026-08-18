---
title: "How Should Catena Handle Comments and Documentation Comments?"
kind: inquiry
created: "2026-08-18"
status: resolved
tags:
  - catena
  - comments
  - documentation
  - language-design
  - syntax
aliases:
  - "Catena comments inquiry"
---

# How Should Catena Handle Comments and Documentation Comments?

## Why this matters

C013 fixed the logical scalar stream and C015 fixed layout, but a comment could
still erase or manufacture a separator depending on an implementation's
unstated lexer behavior. The language also lacked a durable distinction
between source-maintainer notes and user-facing declaration documentation.

These choices affect parser agreement, formatter preservation, generated API
documentation, stale-comment detection, HTML safety, and whether examples can
execute during builds.

## Operational question

Choose a model in which independent implementations agree on:

- line and block delimiters, nesting, prefix edge cases, and EOF;
- which comment-owned logical LFs reach C015 and with which source spans;
- documentation classification, body normalization, grouping, and target;
- the Markdown profile and raw-HTML safety boundary;
- the exact opt-in for future executable documentation; and
- the stable failure when documentation has no valid target.

The answer must compose with C013 and C015 without claiming G019's complete
tokenizer, P109's declaration grammar, G020's file/module rule, or G119's
doctest runner.

## Paths explored

- [Rust comments](../30-sources/rust-project-2026-rust-comments.md) provide
  nested slash comments, exact outer-documentation prefixes, and attachment
  edge cases.
- [Swift lexical structure](../30-sources/swift-project-2026-lexical-structure.md)
  independently supports balanced nested multiline comments.
- [ECMAScript comments](../30-sources/ecma-international-2026-ecmascript-comments.md)
  demonstrate why line-comment terminators and multiline-comment line breaks
  must remain visible to syntax.
- [Elixir documentation](../30-sources/elixir-project-2026-writing-documentation.md)
  separates API documentation from code comments and makes doctest execution
  an explicit test action.
- [CommonMark 0.31.2](../30-sources/macfarlane-2024-commonmark-specification.md)
  supplies a versioned document grammar while exposing raw-HTML and info-string
  boundaries that Catena must secure separately.

## Findings

The slash family gives a small familiar lexical surface, but only if edge
prefixes are fixed. Nested block comments materially improve source editing
and can be scanned iteratively without defining a language nesting ceiling.

Treating comments as featureless spaces is incompatible with C015. A line
comment must stop before LF, and block comments must contribute every internal
logical LF in source order. This is the only lossless choice that preserves
hard, soft, and blank classifications.

Forward-only documentation attachment avoids importing Rust's unresolved
enclosing-item model. Requiring one line before the parser-supplied declaration
and rejecting blank or significant intervening events makes stale
documentation visible.

CommonMark must be versioned. Raw HTML preservation and safe rendering are
different obligations. Doctest execution must also be separate from Markdown
parsing and explicitly selected per fence.

## Outcome

Resolved as C016 and source-only language revision `0.1.12`. Catena uses `//`,
nested `/* ... */`, `///`, and `/** ... */`; the Rust-style inner forms have no
special meaning. Every C013 logical LF inside comments enters C015 layout.
Documentation normalizes through exact delimiter/edge/common-margin rules,
combines adjacent comments, and attaches only to the next parser-supplied
declaration after exactly one LF. Invalid attachment is `DOC001`.

Documentation bodies use `commonmark-0.31.2`; raw HTML never executes
unsanitized. Only exact trimmed `catena doctest` fences opt into the future G119
runner. The [synthesis](../20-notes/catena-comments-and-documentation-comments.md)
develops the design, the
[normative specification](../60-specification/comments-and-documentation-comments/README.md)
defines the exact contract, and the
[C016 journal](../50-journal/2026-08-18-c016-comments-and-documentation-comments.md)
records executable evidence.
