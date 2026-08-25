---
title: "C030 Evaluation Order"
kind: journal
created: "2026-08-25"
tags:
  - catena
  - conformance
  - evaluation-order
  - specification
  - testing
aliases:
  - "C030 evaluation order evidence"
---

# C030 Evaluation Order

## Observations

Checklist item P030 is complete as C030 and normative source-only
language revision `0.1.26`, completing Section 4's evaluation core
alongside C029. The completed boundary fixes the closed ordered-forms
table — the kernel's list elevated verbatim plus the typed-core
completions (curried multi-argument application as repeated unary
left-to-right, trait-call subject then arguments, handler installation
before body, annotate transparency) — the future-form entry rule
(collections, interpolation, and G040 compounds declare their order in
their own slices), the order-versus-structure boundary against
G031/G032, and trace observability: a conforming implementation's
effect-request trace equals the declared order's trace, generalizing
C004's traversal and C005's handler-order rules. The slice is
definitional: no new public API and zero new diagnostic families.

Three implementation decisions worth recording. First, the evidence
oracle is the **operation name, not the argument value**: the runtime
trace event is `{:request, family, capability, operation}` — argument
values are not traced — so the corpus uses one effect with three
operations (`first`, `second`, `third`) as order discriminators, and
each handler clause resumes its argument unchanged so values stay
meaningful for the `and`/`or` skip witnesses (a false left operand is
built from `first 1 ≠ first 2`). Second, the reference target is the
**JSON-AST reference evaluator** (`Catena.Reference.Evaluator`), not
the kernel stepper: the dual-agreement evidence needs both targets to
run the *same* program, and the compiled path consumes the JSON AST —
so the C005 pattern is instantiated on the evaluator/BEAM pair. The
kernel stepper remains the definitional machine for the S-expression
calculus, whose own trace labels already agree. Third, the JSON AST
has no `sequence` tag (that form is kernel-only): the sequence row's
language-level witness uses the analogous `let` schedule —
right-hand-side to a value, then the body — and the table's sequence
row stays kernel-elevated, exactly the elevation-not-amendment split.

Also recorded: full-field 0.1.5 programs (type_exports, types, traits,
instances, templates, imports) and extra definitions placed *before*
`main` — the environment builds in definition order, so a helper must
precede its consumer; and module names arrive as strings while
`compile_json` returns atoms, so `dual_trace` normalizes once.

The sibling compiler implementation is commit
[`5e1e8948249701a45029379e604b7aa0e8376e92`](https://github.com/pcharbon70/catena/commit/5e1e8948249701a45029379e604b7aa0e8376e92),
merged into the `rewrite` integration line by compiler PR
[#106](https://github.com/pcharbon70/catena/pull/106) at merge commit
[`55f58a7`](https://github.com/pcharbon70/catena/commit/55f58a790669593beef5a7dcc6c95158243a969a).
The merge retained the tested tree exactly (tree `ef2dbef`), and the
compiler PR was merged before this research promotion, following the
established publication order.

## Evidence

The compiler registers revision `0.1.26` (`LanguageVersion` feature
`evaluation_order`, static-meaning lifecycle change with migration
note) and adds the
`guides/language/evaluation-order.md` guide; the evidence is
`c030_evaluation_order_test.exs` — no production semantics module, per
the definitional stance (the traces are the oracle).

Focused verification:

```text
mix test test/catena/c030_evaluation_order_test.exs \
  test/catena/c030_traceability_coverage_test.exs
Result: 11 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 377 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration, and
pinned predecessor defaults (the namespace resolver stays pinned at
`0.1.22`, `decode_source_text` advances to `0.1.26`); call arguments
after the callee (`first`, `second`); tuple fields plus the `let`
schedule (`first`, `second`, `third`); the `and` skip (left false:
`[:first, :first]` only) and the forced `or` (left false:
`[:first, :first, :second, :third]`); curried application as repeated
unary; handler installation preceding body (`:handle` first in every
trace); binary left-then-right; fragment trace shapes unchanged; the
closed-set absence (no collection or interpolation order entry
points); and dual-target determinism across repeated runs — every
program asserting `reference == beam`.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit.

## Version and boundary decision

C030 consumes `0.1.26` for the ordered-forms table, the typed-core
completions, the entry rule, and trace observability; it adds no JSON
AST version, kernel S-expression version, interface version, artifact
version, signature domain, typing rule, runtime behavior, BEAM
representation, manifest field, public API name, or diagnostic
family, and amends no retained revision. Every predecessor API retains
its exact selection. The next unused semantic patch is `0.1.27`.

## Threads

- G031 owns binding structure; G032 arity and currying as typing; G033
  branch forms; P035 equality; G036 failure taxonomy; G037
  observability beyond the trace; G040 each new compound's table
  entry; G088 cancellation mid-order; P109 surface syntax.

## Follow-ups

Section 4 continues with G031 (bindings and sequencing) — the trilogy's
third member — then G032/G033. G040 plus G061 unlock the
standard-library era.
