---
title: "C042 Collection Construction and Update"
kind: journal
created: "2026-08-31"
tags:
  - catena
  - conformance
  - collections
  - specification
  - testing
aliases:
  - "C042 collections evidence"
---

# C042 Collection Construction and Update

## Observations

Checklist item G042 is complete as C042 and normative source-only
language revision `0.1.37`, Section 5's third closure (5/8). The
completed boundary fixes the six topics: persistent update is
constructor application plus match-based recursion — no dedicated
operator exists; duplicate-key behavior is a G101 declaration
obligation fixed only as explicitness; ordering and key equality
ride C035's comparable set, so keys must be comparable; a
bounds-failure miss is typed failure as a value — total operations,
never a trap; and complexity promises are excluded from the language
layer because representation is invisible (C037) and nominal data
representation-independent (C002): a language cost bound would make
representation observable the moment a conforming implementation
chose a different one. Zero new diagnostic families and no new
public API.

Four implementation decisions worth recording. First, the **witness
path is the kernel S-expression boundary, like C041**: the frozen
JSON AST (0.1.1–0.1.7) carries no collection-relevant expression
tags beyond the C002 constructor machinery, and its definition
inference folds left-to-right so JSON value definitions cannot
self-recurse — the recursive List/PairMap witnesses therefore run on
`check_kernel`/`compile_kernel` plus the stepper and compiled BEAM.
Second, the **find witness needed a substitution fix**: the first
draft's `String.replace("(var entries)", …)` replaced the definition
scrutinee as well as main's argument, so `find` re-matched the same
constructed literal forever and exhausted the stepper budget; the
fix replaces only main's full call `(call (call (var find) (var
entries)) TARGET)`. Third, **kernel exhaustiveness does not refine
nested constructor sub-patterns** (the C010 `nested_partial`
precedent): `Cons(_, Nil)` leaves the tail position uncovered
(`M001`), so `second_of` destructures through a nested match on the
tail instead — exactly the idiom the chapters' "match recursion"
language describes. Fourth, the **miss witness asserts selected
values, not representations**: miss and hit project to `0`/`7`
through `present`, agreeing on stepper and BEAM, without pinning
`PairMap` value shapes — representation stays invisible by contract.

The sibling compiler implementation is commit
[`246019f`](https://github.com/pcharbon70/catena/commit/246019f),
merged into the `rewrite` integration line by compiler PR
[#117](https://github.com/pcharbon70/catena/pull/117) at merge commit
[`06f5584`](https://github.com/pcharbon70/catena/commit/06f5584abeaec64c695f4e975fd7864aed2bbeb3).
The merge retained the tested tree exactly (tree `09e2d9d`), and the
compiler PR was merged before this research promotion, following the
established publication order. The slice also repaired
a CONFORMANCE.md gap — per-slice profile sections had stopped after
C035 and the identity rows still said `0.1.22`; C036–C042 sections
and the exact-revision rows are restored to `0.1.37`.

## Evidence

The compiler registers revision `0.1.37` (`LanguageVersion` feature
`collection_construction_and_update`, static-meaning lifecycle
change with migration note) and adds the
`guides/language/collections.md` guide; the evidence is
`c042_collections_test.exs`.

Focused verification:

```text
mix test test/catena/c042_collections_test.exs \
  test/catena/c042_traceability_coverage_test.exs
Result: 8 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 478 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection with pinned predecessor
defaults (scan literal `0.1.13`, decode default `0.1.37`, float
value pin) and absent collection surfaces; the declared-List witness
(construction, head/tail match recursion, length, replace-head
update) agreeing on stepper and compiled BEAM by selected values
`{3, 3, 10, 2}`; the miss witness returning `0` (miss) and `7` (hit)
on both targets; key equality riding the comparable set (`9` on a
key hit, `Data.comparable_type?` accepting Int/tuple and rejecting
function types); the absence classification (no `lookup_bang`,
`update_at`, or complexity API); and determinism across repeated
stepper and BEAM runs.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

## Next

Section 5 continues with the pattern-context and representation
questions (P044 and successors); the next unused semantic patch is
`0.1.38`. The decision route is preserved by the
[collections topic map](../10-maps/collection-construction-and-update.md),
the [collections synthesis](../20-notes/catena-collection-operations.md),
and the [traceability registry's CO section](../10-maps/conformance-traceability.md).
