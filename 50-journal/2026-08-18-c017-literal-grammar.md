---
title: "C017 Literal Grammar"
kind: journal
created: "2026-08-18"
tags:
  - catena
  - conformance
  - literals
  - specification
  - testing
aliases:
  - "C017 literal evidence"
---

# C017 Literal Grammar

## Observations

Checklist item G017 is complete as C017 and normative source-only language
revision `0.1.13`. The completed boundary scans exactly one atomic Boolean,
integer, decimal-float, text, character, or byte literal from a caller-supplied
C013 logical-unit index. It retains decoded payload, exact numeric components,
original units/spans, provenance pieces, and raw token-owned line breaks.

The deliberately narrow boundary was essential. Pulling lists, tuples,
records, maps, atoms, or symbols into an “all literals” milestone would also
have chosen primitive types, evaluation order, duplicate handling, patterns,
and BEAM representation. Those forms remain with their existing data and
grammar owners. G018 likewise retains numeric runtime meaning; C017 returns
exact components and mathematical integers without rounding.

The sibling compiler implementation is commit
[`d51b3079c87f84b560e009ac9fc00e0077d11b05`](https://github.com/pcharbon70/catena/commit/d51b3079c87f84b560e009ac9fc00e0077d11b05)
on compiler PR [#93](https://github.com/pcharbon70/catena/pull/93), prepared
from the `rewrite` integration line. The research bundle was prepared on the
matching `agent/c017-literal-grammar` branch from `main` for coordinated
publication.

## Evidence

The compiler adds `Catena.scan_literal/2`, `Catena.Literal` and its
`Numeric`, `Piece`, and `ScanResult` records, exact revision/lifecycle
registration, `LIT001`–`LIT003`, active `LIM004`, source spans, and explicit
pinning of the older comment default to 0.1.12.

Focused verification:

```text
mix test test/catena/c017_literal_grammar_test.exs \
  test/catena/c017_traceability_coverage_test.exs
Result: 12 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 233 passed
mix escript.build
git diff --check
```

The clean warnings-as-errors build compiles 74 Elixir files, formatting is
clean, escript generation succeeds, and the compiler diff check emits no
output.

The focused corpus covers exact selection and persistence separation;
Booleans; every numeric base; dotted and exponent floats; normalized numeric
metadata; leading-zero, separator, exponent, digit, suffix, and sign failures;
all cooked escapes; Unicode preservation; arbitrary raw hashes; one-scalar
characters; ASCII and escaped bytes; raw LF ownership; CRLF/multibyte spans;
exact `LIM002` and `LIM004` boundaries; explicit excluded forms; determinism;
and the absence of whole-source parser/compiler claims. The coverage gate
requires all `LT-OBL-001` through `LT-OBL-012` tags.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
Archive validation passed: 283 completed documents, 24 directories,
2796 local links, and 111 source notes checked; 70 specification chapters and
69 classified fenced blocks checked; 388 traceability obligations
(290 traced, 77 partial, 21 untraced).

python3 -m unittest test_validate_archive.py
Ran 26 tests — OK

git diff --check
No output.
```

## Version and boundary decision

C017 consumes `0.1.13` because it changes accepted ergonomic source forms and
diagnostics. The source decoder now accepts cumulative source revisions
through 0.1.13. Identifier, layout, and comment APIs retain their exact 0.1.10,
0.1.11, and 0.1.12 selections and defaults.

The retained JSON AST remains closed at 0.1.7, the exact kernel remains 0.1.8,
and interface, artifact, signed-format, and compiler-package versions do not
change. The next unused semantic patch is `0.1.14`.

## Threads

- G018 now owns numeric default types, coercions, rounding, overflow,
  exceptional values, and negative-expression elaboration; bases and
  separators are complete in C017.
- G019/P109 must compose identifiers, literals, comments, layout, operators,
  punctuation, and recovery into one maximal whole-file token and grammar
  model.
- G040/G042/P093/G097 retain compound collections, atoms/symbols, binaries,
  maps, and the wider BEAM value model.
- A future interpolating text form needs a new opt-in prefix and lifecycle
  record; existing cooked and raw text remain static.

## Follow-ups

Plan G018 from the now-fixed numeric token components, without reopening C017
spelling or folding unary negation into the literal token.
