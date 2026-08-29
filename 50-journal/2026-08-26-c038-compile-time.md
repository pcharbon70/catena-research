---
title: "C038 Compile-Time Evaluation"
kind: journal
created: "2026-08-26"
tags:
  - catena
  - conformance
  - compile-time-evaluation
  - specification
  - testing
aliases:
  - "C038 compile-time evidence"
---

# C038 Compile-Time Evaluation

## Observations

Checklist item G038 is complete as C038 and normative source-only
language revision `0.1.34`, the fifth and final Section 4 partial to
close — the section is complete except for P041's edge. The completed
boundary fixes: constants never execute (definitions compile, not
run); no attribute system and no macro system exist, each arriving —
if ever — through its own slice under C034's gate; generated
derivations classify as compiler-internal template generation
executing no user code, with `compiler_derived` provenance,
deterministic and total by construction; and the cited restriction
table (the gate plus condition normalization, the 20,000-step
specification checker, and bounded law samples) is the complete
totality and determinism regime. Zero new diagnostic families and no
new public API.

Three implementation decisions worth recording. First, the **answer
is a decision, not a design**: nothing exists to design — no constant
form, no attribute syntax, no macro spelling (all P109-era surface)
— and designing semantics for forms that cannot be written would
invert the corpus's own method. The stance protects the compiler:
no const-eval, macro, or attribute evaluator can arrive as a
compatible addition. Second, the **derivation witness rides the C002
vocabulary**: a datatype declaring `derivations: ["fold"]` compiles
with the derived `Option.fold` carrying `generated?: true` and
`provenance: :compiler_derived` on its `:derived_fold` expression,
recompiles byte-identically, and runs (fold over `Some 7` yields 7) —
the existing test territory reasserted, with two encoding traps
re-learned from C002's helpers: constructor declarations take raw
positional type fields while constructor *patterns* use
`"arguments"` (not `"fields"`). Third, the **budget regressions
assert configuration, not pathology**: the three limits
(`condition_normalization_nodes`, `specification_example_steps`,
`kernel_reference_steps`) are configured integers, and the recursive
condition rejection re-runs the CND-family shape — the regimes are
their owning areas' frozen facts, witnessed as unchanged.

The sibling compiler implementation is commit
[`30426d558f79498f791a398a5ff01c7590b18cad`](https://github.com/pcharbon70/catena/commit/30426d558f79498f791a398a5ff01c7590b18cad)
on branch `agent/c038-compile-time`, pending compiler PR and research
promotion following the established publication order (the PR links
are backfilled at publication).

## Evidence

The compiler registers revision `0.1.34` (`LanguageVersion` feature
`compile_time_evaluation`, static-meaning lifecycle change with
migration note) and adds the `guides/language/compile-time.md` guide;
the evidence is `c038_compile_time_test.exs`.

Focused verification:

```text
mix test test/catena/c038_compile_time_test.exs \
  test/catena/c038_traceability_coverage_test.exs
Result: 7 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 451 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration, and
pinned predecessor defaults; the derivation provenance regression
(`generated?: true`, `provenance: :compiler_derived`, byte-identical
recompilation, and the derived fold executing correctly on BEAM); the
three budget regressions (configured integers plus the recursive-
condition `CND` rejection); the absence matrix (no `const_eval`,
`expand_macro`, `eval_attribute`, or `Derive.evaluate` entry points);
and determinism across repeated compilation with identical interface
bytes and definition counts.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit.

## Version and boundary decision

C038 consumes `0.1.34` for the stance, the derivations
classification, and the restriction table; it adds no JSON AST
version, kernel S-expression version, interface version, artifact
version, signature domain, typing rule, runtime behavior, BEAM
representation, manifest field, public API name, or diagnostic
family, and amends no retained revision. Every predecessor API
retains its exact selection. The next unused semantic patch is
`0.1.35`.

## Threads

- P109 owns spellings for any future const/macro/attribute surface;
  G040 owns deriving extensions, classified under this area's rules
  on arrival; G005/G116 own code-generation programs; G121 owns
  build tooling.

## Follow-ups

Section 4 is complete except for P041 (structural records and
variants — Section 5's edge item, listed in Section 5). Section 5's
data program (G040 anchor) is the next era. The decision route is
preserved in the
[compile-time synthesis](../20-notes/catena-compile-time-evaluation.md)
and the [topic map](../10-maps/compile-time-evaluation.md).
