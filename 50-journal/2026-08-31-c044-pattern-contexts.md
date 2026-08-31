---
title: "C044 Pattern Contexts"
kind: journal
created: "2026-08-31"
tags:
  - catena
  - conformance
  - patterns
  - specification
  - testing
aliases:
  - "C044 pattern contexts evidence"
---

# C044 Pattern Contexts

## Observations

Checklist items P044 and D046 are complete as C044 and C046,
normative source-only language revision `0.1.38`, Section 5's
fourth closure (6/8). The completed boundary fixes three context
classes — match the only exhaustive context, irrefutable-only the
default for binding positions, explicit-failure the only honest
refutability — with the no-implicit-runtime-match property holding
in every context. Per-context rules: `let` binders and function
parameters stay plain-named today (irrefutable-only on arrival);
the generator principle is fixed (ordinary total, filtering
explicitly mismatch-as-skip) with grammar deferred to Section 6;
public receives are reserved as exhaustive-or-explicit-fallback;
handler clauses keep plain binders; exception clauses are
permanently excluded under C036's terminal trap; and D046's
programmable patterns are excluded with arrival conditions
recorded. Zero new diagnostic families and no new public API.

Three implementation decisions worth recording. First, the
**redundancy witness runs on the JSON-AST path, not the kernel**:
the kernel checker's coverage check is a simplified head-coverage
exhaustiveness test, while the usefulness-based useless-row
detection (`M002`) runs in the inference pipeline — so the
unchanged-diagnostics witness pins `M001` through `check_kernel`
and `M002` through `check_json`. Second, the **handler witness is
the C010 fixture, not an invented program**: a hand-written handler
module risks failing for invented-syntax reasons rather than
pattern reasons, so the plain-binder regression re-checks and
re-runs the existing fixture that carries a real handler with
plain parameters and a resumption binder. Third, the **negative
boundary witnesses fail for verified reasons**: the pattern-position
`let` binder rejects as `SYN002` ("let binding must be an unquoted
name") — confirmed by direct inspection, not assumed — and the
JSON-AST `let` keeps its `"name"` binder with a `"pattern"` key
rejecting at decode.

The sibling compiler implementation is commit
[`00bd04c`](https://github.com/pcharbon70/catena/commit/00bd04c)
on branch `agent/c044-pattern-contexts`, publication pending: the
compiler PR merges into `rewrite` first, then this research
promotion merges, following the established publication order.

## Evidence

The compiler registers revision `0.1.38` (`LanguageVersion` feature
`pattern_contexts`, static-meaning lifecycle change with migration
note) and adds the `guides/language/pattern-contexts.md` guide;
the evidence is `c044_pattern_contexts_test.exs`.

Focused verification:

```text
mix test test/catena/c044_pattern_contexts_test.exs \
  test/catena/c044_traceability_coverage_test.exs
Result: 10 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 488 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection with pinned predecessor
defaults (scan literal `0.1.13`, decode default `0.1.38`, float
value pin) and absent reserved/excluded entry points; the match
regression pin agreeing on stepper and compiled BEAM (`12`) with
unchanged `M001` (kernel) and `M002` (JSON AST) identities; the
pattern-position `let` binder rejecting `SYN002` at the kernel
boundary and the JSON-AST `let` rejecting a `"pattern"` binder;
the C010 fixture's handler clauses re-checked with plain binders;
and determinism across repeated runs.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

## Next

Section 5 continues with the later pattern-form question (list,
record, variant, binary, range) and the representation boundary;
Section 6 (comprehensions) consumes the generator principle. The
next unused semantic patch is `0.1.39`. The decision route is
preserved by the [pattern-contexts topic
map](../10-maps/pattern-contexts.md), the [pattern-contexts
synthesis](../20-notes/catena-pattern-contexts.md), and the
[traceability registry's PC
section](../10-maps/conformance-traceability.md).
