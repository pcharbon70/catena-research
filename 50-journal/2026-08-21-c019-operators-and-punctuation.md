---
title: "C019 Operators and Punctuation"
kind: journal
created: "2026-08-21"
tags:
  - catena
  - conformance
  - operators
  - specification
  - syntax
  - testing
aliases:
  - "C019 operator evidence"
---

# C019 Operators and Punctuation

## Observations

Checklist item G019 is complete as C019 and normative source-only language
revision `0.1.15`. The completed boundary fixes the closed semantic-mapped
operator and punctuation inventory with maximal munch and reserved-spelling
rejection, the concrete C015 continuation capabilities and delimiter frames,
the fixed precedence ladder with non-associative comparisons and the
left-associative `|>` pipe, and the first whole-source token stream plus a
bounded operator-expression layer.

The semantic-mapped discipline held: every operator token denotes an
already-normative meaning (`+ - *`, comparisons, equalities from C003/C010;
prefix `-` from C018; `!` Boolean not) or is structural, so completing G019
required no new semantics and no amendment to C001 through C018. A useful
consequence surfaced during testing: sequences like `<<`, `++`, and `--`
tokenize into shorter valid tokens and fail at the expression layer
(`a -- b` is validly `a - (- b)`), while no-match positions like `/`, `%`,
and `=` fail at tokenization — the `OPR001`/`OPR002` split follows the
layer boundary exactly.

The sibling compiler implementation is commit
[`6e13bdf72547c4b363d794461c3f875fd0a16119`](https://github.com/pcharbon70/catena/commit/6e13bdf72547c4b363d794461c3f875fd0a16119),
merged into the `rewrite` integration line by compiler PR
[#95](https://github.com/pcharbon70/catena/pull/95) at merge commit
[`3f2ef5b`](https://github.com/pcharbon70/catena/commit/3f2ef5b6680a4984dc30c01847cd7dc9a71f56ea).
The merge retained the tested tree exactly (tree `bcb78c4`), and the compiler
PR was merged before this research promotion, following the established
publication order.

## Evidence

The compiler adds `Catena.Tokenizer` — the whole-source maximal-munch lexer
composing the C014 identifier/qualified-name, C016 comment, and C017
literal scanners over the C013 unit stream, emitting tokens with
original-byte spans, capability pairs, and delimiter frame events — and
`Catena.Operator`, the fixed-ladder expression layer with prefix operators,
rejected comparison chains, groupings, and the pipe. The public boundary is
`Catena.tokenize_source/2` and `Catena.parse_operator_expression/1`, with
`OPR001`–`OPR002` and exact 0.1.15 registration pinning every predecessor
default (identifiers 0.1.10, layout 0.1.11, comments 0.1.12, literal
scanning 0.1.13, numeric elaboration 0.1.14).

Focused verification:

```text
mix test test/catena/c019_operators_test.exs \
  test/catena/c019_traceability_coverage_test.exs
Result: 14 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 260 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration, pinned
predecessor defaults, and determinism; the full inventory and every reserved
no-match spelling; maximal munch against `1.0e3`, `1.`, `x.y.z`, `1.x`,
`->x`, `|>x`, `!!a`, and the four spacing variants of `a-1`; the exact
capability pairs including balanced opener/closer contexts; frame families,
modes, innermost closing, `LAY002` integration, and multiline continued
contents; ladder grouping and associativity; chain rejection and
parenthesized regroupings; prefix nesting, `-1` as negation, and the
unsigned pattern boundary; pipe grouping and precedence; `->` and `.`
exclusions with qualified names as atomic operands; token-text/span
round-trip slices; and transactional single-diagnostic rejection with no
recovery.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit; 302 completed documents were
checked across 26 directories with 3,070 local links, 77 specification
chapters, 419 traceability obligations, and all 26 validator unit tests
passing.

## Version and boundary decision

C019 consumes `0.1.15` because it changes source acceptance and static
expression structure. The source decoder now accepts cumulative source
revisions through 0.1.15. Every predecessor API retains its exact
selection; no new implementation limit is introduced, and aggregate
token-count limits remain with the G129 owner.

The retained JSON AST remains closed at 0.1.7, the exact kernel remains
0.1.8, and interface, artifact, signed-format, and compiler-package versions
do not change. The next unused semantic patch is `0.1.16`.

## Threads

- P109 must fix application and declaration grammar and the `->` clause
  structure over this token stream; G020 must relate token streams to files
  and modules.
- G021/G022 must give `.`-separated qualified names their resolution
  meaning; G040 must decide whether field-like access reuses `.`; G061 must
  decide operator trait dispatch; G066 retains type-directed resolution
  questions.
- G118 formatter tolerance and G123 editor recovery consume the lossless
  stream but remain open owners.

## Follow-ups

Plan P109's application syntax from the now-fixed pipe structure without
reopening the C019 inventory or ladder, and fold the `->` clause grammar
into the same declaration decision.
