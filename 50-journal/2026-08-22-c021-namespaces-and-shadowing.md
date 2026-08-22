---
title: "C021 Namespaces and Shadowing"
kind: journal
created: "2026-08-22"
tags:
  - catena
  - conformance
  - namespaces
  - specification
  - testing
aliases:
  - "C021 namespace evidence"
---

# C021 Namespaces and Shadowing

## Observations

Checklist item G021 is complete as C021 and normative source-only language
revision `0.1.17`. The completed boundary fixes the namespace category
inventory under the hard spelling-class partition, per-category uniqueness
domains with flat constructor uniqueness, silent innermost-wins shadowing
that never crosses categories, quantifier-scoped type variables that may
shadow type and trait names, local-over-imported precedence with
order-independent `NSP004` ambiguity rejection naming every origin,
governed-identity separation, and exactly-two-segment qualification.

Consolidation, not amendment: every rule generalizes the C010 kernel's
bounded namespace law, and the Haskell/SML evidence showed the adopted
shape is the mainstream model rather than an exotic choice. The
abstract-events discipline (C015/C020 pattern) again let the whole
contract become executable before P109's declaration grammar exists. One
representation decision emerged during testing: resolution scope depth
counts outward from the module scope (module = 0, deeper nesting = larger),
so identities carry a stable, comparable nesting measure rather than an
implementation-internal index.

The sibling compiler implementation is commit
[`b482b4cacc4017b8e479173fb3bd3c0ceac4f675`](https://github.com/pcharbon70/catena/commit/b482b4cacc4017b8e479173fb3bd3c0ceac4f675)
on branch `agent/c021-namespaces-shadowing`, prepared from the `rewrite`
integration line for coordinated publication.

## Evidence

The compiler adds `Catena.Namespace` with the
`Catena.build_namespace_environment/2` and `Catena.resolve_name/2`
boundaries, `NSP001`–`NSP005`, exact 0.1.17 registration with every
predecessor default pinned (identifiers 0.1.10 through file units 0.1.16),
and the `guides/language/namespaces.md` guide.

Focused verification:

```text
mix test test/catena/c021_namespaces_test.exs \
  test/catena/c021_traceability_coverage_test.exs
Result: 14 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 285 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration, pinned
predecessor defaults, and determinism; cross-category coexistence of one
spelling; the spelling-class violation matrix in both directions across
all eleven program categories; duplicates in every category, the typevar
quantifier domain, unbalanced scope events, and the legal shadowing
escape; governed-identity rejection and unknown categories; two-segment
qualification with deep chains and unknown modules; innermost resolution
with cross-category safety and post-close restoration; type-variable
scoping with type visibility, value separation, and quantifier expiry;
local-over-imported precedence with two-origin and order-flipped
ambiguity and single-import resolution; unbound references in every
category; and diagnostics carrying spelling, category, and all colliding
origins including a three-origin case.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit; 319 completed documents
were checked across 28 directories with 3,293 local links, 83
specification chapters, 445 traceability obligations, and all 26
validator unit tests passing.

## Version and boundary decision

C021 consumes `0.1.17` because it changes static meaning and diagnostics.
The source decoder now accepts cumulative source revisions through
0.1.17. Every predecessor API retains its exact selection; no new
implementation limit is introduced.

The retained JSON AST remains closed at 0.1.7, the exact kernel remains
0.1.8, and interface, artifact, signed-format, and compiler-package
versions do not change. The next unused semantic patch is `0.1.18`.

## Threads

- G022 must fix import and export syntax, visibility defaults, renaming,
  wildcard exclusion, and unused-import diagnostics over this precedence
  model.
- G024 must decide module recursion knowing resolution is
  order-independent; G025 must enforce package-level module uniqueness;
  G026 must design the prelude as one more origin; G066 must confirm no
  resolution becomes type-directed; P109 must emit the scope events this
  resolver consumes.

## Follow-ups

Plan G022 directly against the fixed precedence and collision rules; the
import-set abstraction this resolver consumes is the seam where concrete
import syntax plugs in.
