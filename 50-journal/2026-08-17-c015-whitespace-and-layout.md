---
title: "C015 Whitespace and Layout"
kind: journal
created: "2026-08-17"
tags:
  - conformance
  - layout
  - specification
  - syntax
  - testing
  - whitespace
aliases:
  - "C015 layout evidence"
---

# C015 Whitespace and Layout

## Observations

Checklist item G015 is complete as C015 and normative source-only language
revision `0.1.11`. The
[Whitespace and Layout Specification](../60-specification/whitespace-and-layout/README.md)
makes indentation non-semantic, limits layout whitespace to ASCII space, tab,
and C013 logical LF, uses hard LF and semicolon separators, and resolves soft
lines from token capabilities and delimiter-frame modes.

The decision was developed in the
[synthesis](../20-notes/catena-whitespace-layout-and-line-continuation.md) and
[resolved inquiry](../40-inquiries/how-should-catena-treat-whitespace-and-line-breaks.md).
The [topic map](../10-maps/whitespace-layout-and-line-continuation.md) routes
through Elixir, Python, Haskell, Rust, C013, and C014.

The result remains deliberately pre-lexer. Comments, literal bodies, concrete
operators, punctuation, precedence, associativity, and complete surface
productions remain G016–G019 and P109. The executable engine consumes opaque
lexer-supplied token events instead of guessing those unresolved forms.

## Compiler evidence

The coordinated sibling-compiler implementation targets the `rewrite` line
from branch `agent/c015-whitespace-layout` and adds:

- cumulative source-text selection through `0.1.11` without widening persisted
  or compilable formats;
- `Catena.Layout` token, whitespace, line-break, semicolon, and result events;
- `Catena.resolve_layout/2` with lossless classifications and exact selection;
- `LAY001`–`LAY003` with original-byte spans and stable reasons;
- continued and block delimiter frames plus before/after token joins; and
- tagged `LY-OBL-001` through `LY-OBL-011` tests and a complete coverage gate.

The exact 0.1.10 standalone identifier frontend retains its default selection
even though the source-text decoder now defaults to 0.1.11. The language-info
and conformance-info registries report 0.1.11 as current.

No whole-source layout CLI was added. Such a command would falsely imply that
comments, literals, and concrete tokenization were already defined.

The implementation is immutable at compiler commit
[`5d08925ce92f57e78018e0ab81c008a7d917dfbc`](https://github.com/pcharbon70/catena/commit/5d08925ce92f57e78018e0ab81c008a7d917dfbc)
on draft compiler PR [#91](https://github.com/pcharbon70/catena/pull/91).

## Evidence

The implementation verification records these required commands:

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

All commands passed on 2026-08-17. The clean compiler build compiled 72 Elixir
files with warnings treated as errors; ExUnit passed 210 tests; and escript
generation succeeded. Archive validation passed 261 completed documents in 22
directories, 2,546 local links, 105 source notes, 64 specification chapters,
67 classified fenced blocks, and 364 traceability obligations (266 traced, 77
partial, and 21 untraced). The archive validator's 26 unit tests also passed.

## Result

C015 consumes `0.1.11` because it changes how ergonomic source whitespace and
line boundaries are classified and exposes a stable frontend engine and
diagnostic family. It does not change the compiler package release, retained
JSON AST, exact 0.1.8 kernel, interfaces, signature domains, typed core,
runtime semantics, or BEAM representation.

## Threads

- G016 must define comment nesting, line termination, documentation
  attachment, Markdown, and doctests.
- G017 must define which whitespace and newlines belong inside literals.
- G019 must assign concrete tokens to continuation and delimiter capabilities
  while defining operators, precedence, associativity, and recovery.
- P109 must integrate the layout event stream into the complete grammar and
  concrete syntax tree.

## Follow-ups

Integrate G016 comments, G017 literals, and G019 concrete token capabilities
through the published event boundary without reinterpreting C015 layout.
