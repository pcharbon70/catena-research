---
title: "C024 Module Dependency Cycles"
kind: journal
created: "2026-08-24"
tags:
  - catena
  - conformance
  - modules
  - separate-compilation
  - specification
  - testing
aliases:
  - "C024 cycles evidence"
---

# C024 Module Dependency Cycles

## Observations

Checklist item G024 is complete as C024 and normative source-only
language revision `0.1.20`. The completed boundary admits module
dependency cycles: maximal strongly-connected components are the units of
checking, resolution, and caching; intra-component references resolve
against companions' declared signatures with no digests circulating
inside the component; cross-component imports stay digest-bound exactly
as C022 fixed them; components receive one deterministic joint digest;
initialization is definition-only with per-component loading; and the
dependency-inversion alternative is the sanctioned non-cyclic
restructuring. `CYC001` reports intra-component regime mixing and
signature gaps at the closing transaction.

This is the corpus's first cycle-*admitting* slice and its largest
compiler slice since C019. Three implementation decisions emerged. First,
provisional interfaces are built from *definitions-stripped* member cores
checked against header-only companion seeds — because the seeds' unknown
inhabitation made the coverage checker expand mutually-recursive domains
without memoization, the seeds now compute *true* inhabitation from the
merged raw constructor graph (a fixed point over declared constructor
shapes). Second, the joint digest is a SHA-256 over sorted
`module:digest` entries, making it invariant to member order and —
verified directly — to the uniform/compact layout choice, extending
C002's representation independence from modules to components. Third, a
pre-existing coverage boundary was isolated and recorded rather than
worked around: exhaustive matching over mutually-recursive types exhausts
the `M004` budget *even within a single module* (verified with a
single-module `Nat` probe before any component work), so the component
corpus proves execution through cross-module construction and per-member
functions, and wider recursive matching is bounded by the same existing
limit rather than by this slice.

The sibling compiler implementation is commit
[`ca2be792e3f5fe081c67ec7ca9e845d40a5087c0`](https://github.com/pcharbon70/catena/commit/ca2be792e3f5fe081c67ec7ca9e845d40a5087c0),
merged into the `rewrite` integration line by compiler PR
[#100](https://github.com/pcharbon70/catena/pull/100) at merge commit
[`336a271`](https://github.com/pcharbon70/catena/commit/336a2710385992fdd5a4f3f0de470511b2c33f4c).
The merge retained the tested tree exactly (tree `6db5169`), and the
compiler PR was merged before this research promotion, following the
established publication order.

## Evidence

The compiler adds the abstract SCC layer in `Catena.Namespace` — a
fourth in-place grammar extension of the environment builder to
`0.1.20`, with provide-module events gaining optional `dependencies`
and `signatures` fields, a `current_module` option attaching import
edges to the consumer, reachability-based component partitioning, and
both `CYC001` rejections at the closing transaction — and the concrete
`Catena.Scc` / `Catena.compile_scc/2` boundary with the
`Catena.Scc.Result` record, plus the `guides/language/module-cycles.md`
guide.

Focused verification:

```text
mix test test/catena/c024_module_cycles_test.exs \
  test/catena/c024_traceability_coverage_test.exs
Result: 9 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 312 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration, and
pinned predecessor defaults (with the resolver's required revision
advanced to 0.1.20 accepting both event shapes); abstract grouping of
pairs, self-loops, and three-module rings with digest-free intra-
component admission and cross-component digest imports; both `CYC001`
reasons with full details plus `T008` on the concrete path; the acyclic
regression (environment sccs degenerate, member interface digest equal
to ordinary compilation's); joint-digest determinism across member
permutations and rebuilds with divergence on member change; the
inversion shape compiling without a component; two-module component
execution in both layouts — cross-module construction yielding the
layout-correct term plus per-member integer functions — and a
three-module ring compiling with a stable digest; and an outsider
importing a component member through its digest-bound interface while
the uninterfaced import fails `A004`.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit; 343 completed documents
were checked across 31 directories with 3,589 local links, 91
specification chapters, 475 traceability obligations, and all 26
validator unit tests passing.

## Version and boundary decision

C024 consumes `0.1.20` because it admits cyclic event graphs, adds the
`CYC001` diagnostic family, and adds the joint digest as a new
deterministic field of the component result. Member interfaces remain
ordinary digest-bound interfaces; the retained JSON AST stays closed at
0.1.7, the kernel at 0.1.8, and interface, artifact, signed-format, and
compiler-package versions do not change. Every predecessor API retains
its exact selection. The next unused semantic patch is `0.1.21`.

## Threads

- G025 must assemble packages over component units and represent joint
  digests in lockfiles; P109 must fix the concrete recursive `use`
  surface; G028 must treat joint digests as compatibility boundaries;
  the `M004`-over-recursive-types coverage boundary joins G138's
  performance envelope and the coverage-checker's own limits as recorded
  evidence, not an SCC defect.

## Follow-ups

Plan G025 next: components are now its assembly input, and the Hex
publishing hypothesis note is waiting there. The true-inhabitation
seeding and provisional-interface mechanism should be revisited if
coverage memoization over recursive types ever lands — the seeding stays
correct but could then inherit real elaborated metadata directly.
