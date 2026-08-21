---
title: "C018 Numeric Literal Semantics"
kind: journal
created: "2026-08-21"
tags:
  - catena
  - conformance
  - floats
  - integers
  - literals
  - specification
  - testing
aliases:
  - "C018 numeric evidence"
---

# C018 Numeric Literal Semantics

## Observations

Checklist item G018 is complete as C018 and normative source-only language
revision `0.1.14`. The completed boundary elaborates exactly one C017-scanned
numeric token into its typed meaning: an exact mathematical `Int` value or a
correctly rounded finite binary64 `Float` value, with total negation, no
defaulting, no implicit coercions, `NUM001` static overflow invalidity, and
the active `LIM005` decimal-component digit limit.

The narrow boundary stayed essential. Operator spelling, numeric traits,
explicit conversions, primitive equality, arithmetic failure, and the wider
data model all remain with their existing owners, so completing G018 required
no amendment to C001's no-defaulting contract or C017's spelling.

The sibling compiler implementation is commit
[`6fb2ad89a5cc5518528106f73d60b5adc9387d74`](https://github.com/pcharbon70/catena/commit/6fb2ad89a5cc5518528106f73d60b5adc9387d74)
on branch `agent/c018-numeric-literal-semantics`, prepared from the `rewrite`
integration line for coordinated publication.

## Evidence

The compiler adds `Catena.Numeric` and `Catena.elaborate_numeric_literal/2`,
exact integer-arithmetic decimal-to-binary64 conversion with a single
`roundTiesToEven` step, `NUM001`, active `LIM005`, exact 0.1.14 revision and
lifecycle registration, explicit pinning of literal scanning to exact
`0.1.13`, and predecessor test and guide updates.

Boundary constants were verified before being fixed in text. Local OTP 29
checks: the largest finite binary64 is `1.7976931348623157e308`
(bit pattern `0x7FEFFFFFFFFFFFFF`); `1.0e308 * 1.0e308` and `1.0/0.0` raise
`badarith`; `list_to_float("1.0e400")` raises `badarg`; the minimum normal is
`2.2250738585072014e-308` and the minimum subnormal decodes from
`<<0,0,0,0,0,0,0,1>>`. The halfway overflow boundary 2¹⁰²⁴ − 2⁹⁷⁰, the
max-subnormal/min-normal halfway tie, the exact half-subnormal tie at
2⁻¹⁰⁷⁵, and the shortest-vs-exact max-finite decimals were all checked with
exact integer arithmetic before being encoded as test expectations.

Focused verification:

```text
mix test test/catena/c018_numeric_literal_semantics_test.exs \
  test/catena/c018_traceability_coverage_test.exs
Result: 13 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 246 passed
mix escript.build
git diff --check
```

The clean warnings-as-errors build compiles 75 Elixir files, formatting is
clean, escript generation succeeds, and the compiler diff check emits no
output.

The focused corpus covers exact selection, revision pinning, lifecycle
registration, and determinism; every integer base with exact values;
monomorphic typing without constraint, defaulting, or coercion surface;
domain exclusions and signed zero; total negation including `-0.0`; correct
rounding of ties to even significands; subnormal, exact-tie, and
underflow-to-zero results; the largest-finite and halfway overflow
boundaries including the exact 309-digit max-finite decimal; the `LIM005`
4,096/4,097 boundary; and the absence of whole-source phases. The coverage
gate requires all `NM-OBL-001` through `NM-OBL-014` tags.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit; 292 completed documents were
checked across 25 directories with 2933 local links, 73 specification
chapters, 403 traceability obligations, and all 26 validator unit tests
passing.

## Version and boundary decision

C018 consumes `0.1.14` because it changes static meaning and diagnostics.
The source decoder now accepts cumulative source revisions through 0.1.14.
Identifier, layout, comment, and literal APIs retain their exact 0.1.10,
0.1.11, 0.1.12, and 0.1.13 selections and defaults; `LIM005` joins the C012
portable-minimum registry without changing any existing classification.

The retained JSON AST remains closed at 0.1.7, the exact kernel remains
0.1.8, and interface, artifact, signed-format, and compiler-package versions
do not change. The next unused semantic patch is `0.1.15`.

## Threads

- G019/P109 must fix negation spelling, precedence, and operator tokens and
  compose identifiers, literals, comments, and layout into one whole-file
  token stream.
- G061 owns numeric trait relationships over the now-fixed monomorphic
  types; G105 owns explicit `Int`/`Float` conversions and the numeric
  library; P035 owns primitive equality and ordering including the two zero
  encodings; G036 owns the runtime failure taxonomy for arithmetic outside
  the finite domain.
- G040 owns placing `Int` and `Float` inside the complete built-in data
  model, including sendability of `Float`.
- The canonical archive version registry now covers 0.1.9 through 0.1.14;
  C014 and C016 immutable publication identities remain to be backfilled in
  their journals.

## Follow-ups

Plan G019 from the now-fixed numeric meaning without reopening C018 typing
or conversion, and fold unary negation's spelling into the same token and
precedence decision.
