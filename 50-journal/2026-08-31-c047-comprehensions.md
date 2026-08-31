---
title: "C047 List Comprehensions"
kind: journal
created: "2026-08-31"
tags:
  - catena
  - conformance
  - comprehensions
  - specification
  - testing
aliases:
  - "C047 comprehensions evidence"
---

# C047 List Comprehensions

## Observations

Checklist items P047–P058 are complete as C047–C058, normative
source-only language revision `0.1.39`, Section 6's closure — the
largest slice so far at twelve items (80/141 total). The completed
boundary: an eager, ordered, `List A → List B` `for ... yield`
expression with total generators, `case ... in` mismatch-as-skip
filtering generators, typed `when` filters, exhaustive local `let`
bindings, visible effects, sequential depth-first traversal, and a
qualifier-tree elaboration to a fused tail-recursive worker chain.
Implementation is dormant by the frozen-frontend constraint:
`Catena.Comprehension.elaborate/1` maps a caller-built qualifier
tree to a kernel module — recursive workers are expressible in the
kernel but not in the JSON AST, whose definitions fold
left-to-right and cannot self-recurse (the C042 finding). Surface
tokens adopt with P109. Three new `LCP` diagnostic families
(rebinding, never-matching filtering pattern, unnecessary marker);
`M001`, `T002`, and `BS001` reused by role.

Five implementation decisions worth recording. First, the **fused
worker is a chain, not a single definition**: one tail-recursive
definition per generator depth sharing one accumulator, with the
outer worker advancing around each inner completion — the chapter
wording was refined at candidate stage to match what is honestly
generatable. Second, the **first hand-counted emitter was replaced
by balanced form builders**: string templates with manual closing
parentheses failed on filter/let nesting, so every generated form
now wraps exactly once (`call_form`, `match_form`, `clause_form`,
`fn_form`) and balance is structural. Third, **type checking and
coverage ride the kernel checker**: the elaborator threads
caller-declared binder types through worker signatures and lets
`check_kernel` be the authority — non-list sources surface as
`T002`, non-total ordinary generators and refutable `let` bindings
as `M001`, non-`Bool` filters as `T002`. Fourth, **`LCP003` uses a
probe**: a case generator whose ordinary-generator variant checks
clean is provably total, so the elaborator elaborates the probe
and asks the real checker. Fifth, **the deep-input witness honors
the published parser nesting limit**: 2000 nested `construct`
forms reject as `SYN003` (1024-level limit), so the stack-safety
witness runs 900 elements on BEAM. One process slip recurred and
was caught: the lifecycle `feature/2` registration for
`list-comprehensions` was lost in a multi-edit and restored before
publication.

The sibling compiler implementation is commit
[`3216831`](https://github.com/pcharbon70/catena/commit/3216831)
(implementation `500859d` plus the warning fix), merged into the
`rewrite` integration line by compiler PR
[#119](https://github.com/pcharbon70/catena/pull/119) at merge
commit
[`7b0591d`](https://github.com/pcharbon70/catena/commit/7b0591d417117cb2ca3d94c5779239f3f6a70a5d).
The merge retained the tested tree exactly (tree `ab84e6d`), and
the compiler PR was merged before this research promotion,
following the established publication order.

## Evidence

The compiler registers revision `0.1.39` (`LanguageVersion` feature
`list_comprehensions`, static-meaning lifecycle change with
migration note), adds `lib/catena/comprehension.ex` (the dormant
elaboration boundary, this area's one new public API), and adds
the `guides/language/list-comprehensions.md` guide; the evidence
is `c047_list_comprehensions_test.exs`.

Focused verification:

```text
mix test test/catena/c047_list_comprehensions_test.exs \
  test/catena/c047_traceability_coverage_test.exs
Result: 14 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 502 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection with pinned predecessor
defaults and the elaboration API declared; the grammar's semantic
roles (first-qualifier-must-be-generator raises; role fragments
present); non-list sources rejecting `T002`; the Cartesian
traversal `[14, 15, 24, 25]` with dependency and empty-input
behavior; `when` filters skipping `false` (`[30, 40]` through a
`let` binding) with non-`Bool` rejecting `T002`; the
pattern-generator split (`case` skipping `None` to `[1, 3]`,
non-total rejecting `M001`, `LCP002`, `LCP003`); scope
(`LCP001` rebinding, `BS001` unused); effect rows threading
`(uses Ask)` with parallel entry points absent; the fused-worker
shape (exactly workers + reverse + main + context definitions, no
dispatch) with desugaring-equivalence against the hand-written
recursive map on both targets; `List B` results with no other
target entry points; stack-safe 900-element production on BEAM;
and determinism with the exclusion boundary (no surface, lazy,
stream, or iterator entry points).

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

## Next

Section 6 is closed except D059's deferred neighbors (ranges, zip,
streams, binary and map comprehensions, generic collectors), which
remain independently researched. The next unchecked items begin
Section 7 (traits, combinators, derivation, standard library). The
next unused semantic patch is `0.1.40`. The decision route is
preserved by the [list-comprehensions map](../10-maps/list-comprehensions.md),
the [list-comprehensions synthesis](../20-notes/list-comprehensions.md),
and the [traceability registry](../10-maps/conformance-traceability.md).
