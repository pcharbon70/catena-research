---
title: "C016 Comments and Documentation Comments"
kind: journal
created: "2026-08-18"
tags:
  - comments
  - conformance
  - documentation
  - specification
  - syntax
  - testing
aliases:
  - "C016 comment evidence"
---

# C016 Comments and Documentation Comments

## Observations

Checklist item G016 is complete as C016 and normative source-only language
revision `0.1.12`. The
[Comments and Documentation Comments Specification](../60-specification/comments-and-documentation-comments/README.md)
defines slash comments, iterative nested block balancing, comment-internal
layout, forward declaration documentation, CommonMark 0.31.2, inert raw HTML,
and explicit-only future doctests.

The decision was developed in the
[synthesis](../20-notes/catena-comments-and-documentation-comments.md) and
[resolved inquiry](../40-inquiries/how-should-catena-handle-comments-and-documentation-comments.md).
The [topic map](../10-maps/comments-and-documentation-comments.md) connects the
Rust, Swift, ECMAScript, Elixir, CommonMark, C013, and C015 evidence.

The result remains deliberately pre-lexer and pre-parser. The implementation
scans one comment at a lexer-supplied unit index and resolves an abstract event
stream containing parser-supplied documentable targets. It does not recognize
whole files, render Markdown, execute doctests, or decide file/module ownership.

## Compiler evidence

The coordinated sibling-compiler working tree targets the `rewrite` line from
branch `agent/c016-comments-documentation` and adds:

- cumulative source-text selection through `0.1.12` without widening retained
  or persisted formats;
- exact 0.1.11 default behavior for `Catena.resolve_layout/2` after the current
  revision advances;
- `Catena.scan_comment/2` with lossless source units, normalized body units,
  line-comment terminator preservation, iterative nested blocks, and
  `CMT001`/`CMT002`;
- `Catena.resolve_comments/2` with comment-transparent token adjacency, C015
  classification for every internal LF, parser-supplied targets, normalized
  documentation attachments, CommonMark/raw-HTML/doctest metadata, and
  `DOC001`; and
- tagged `CM-OBL-001` through `CM-OBL-012` tests plus a complete coverage gate.

The exact 0.1.10 identifier frontend and exact 0.1.11 layout frontend retain
their selection boundaries. No CLI, Markdown dependency, renderer, or doctest
runner was added.

## Evidence

The coordinated verification set is:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
mix escript.build
git diff --check
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
```

The compiler's focused and full ExUnit runs pass 221 tests on 2026-08-18.
The clean warnings-as-errors build compiles 73 Elixir files, formatting is
clean, and escript generation succeeds.
Archive validation passes 274 completed documents in 23 directories, 2,677
local links, 110 source notes, 67 specification chapters, 67 classified fenced
blocks, and 376 traceability obligations (278 traced, 77 partial, and 21
untraced). The archive validator's 26 focused unit tests also pass. Both
repositories pass `git diff --check` in the complete cross-repository audit.

## Result

C016 consumes `0.1.12` because it changes accepted ergonomic source forms,
layout observations, documentation metadata, and stable diagnostics. It does
not change the compiler package release, retained JSON AST, exact 0.1.8 kernel,
interfaces, signature domains, typed core, runtime semantics, or BEAM
representation.

## Threads

- C017 now defines atomic literal bodies, escapes, static text, and raw newline
  ownership; any future interpolation requires a new opt-in prefix.
- G019 must integrate comment recognition with concrete punctuation and
  maximal tokenization.
- G020 and P109 must define file/module and complete declaration-target rules.
- G110 and G118 must render and format documentation without weakening raw-HTML
  or lossless-source rules.
- G119 must define isolated doctest execution, expected results, effects,
  budgets, and build integration.

## Follow-ups

Carry the lossless comment events and parser-supplied documentation targets
into the complete lexer/parser without replacing the C013 unit stream or C015
layout classifier.
