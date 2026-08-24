---
title: "C026 Prelude Policy"
kind: journal
created: "2026-08-24"
tags:
  - catena
  - conformance
  - prelude
  - specification
  - testing
aliases:
  - "C026 prelude evidence"
---

# C026 Prelude Policy

## Observations

Checklist item G026 is complete as C026 and normative source-only
language revision `0.1.22`. The completed boundary fixes the manifest
`prelude` field (one package, one requirement, absent/`null` = no
origin); admission as an ordinary import-class origin under unchanged
C021 precedence (locals win; prelude-import collisions reject as
`NSP004` naming both origins; no tier); the zero-implicit-names edition
guarantee with a lifecycle-record path for any future default; and
prelude selections resolving and locking as ordinary C025 dependencies.

This slice is the purest wiring of the corpus so far: every rule was
already promised in shipped prose (C021's "never a silent default",
C022's declined implicit Prelude), and the implementation simply
connected three shipped boundaries — manifest decoder, environment
builder, dependency resolver — with one injection point. One
implementation decision worth recording: the prelude origin enters at
the environment builder's base case (after all provided modules are
known), not as a pre-event, because the export set to inject is only
knowable after the provide_module event for the prelude package has
been processed. This also means an unknown prelude package is `PKG004`
— the same family as an unknown import target, from the same
environment-miss fact.

The sibling compiler implementation is commit
[`484d797a33eaf580f2c43ddd0776c6675078c4f9`](https://github.com/pcharbon70/catena/commit/484d797a33eaf580f2c43ddd0776c6675078c4f9),
merged into the `rewrite` integration line by compiler PR
[#102](https://github.com/pcharbon70/catena/pull/102) at merge commit
[`e7fea0b`](https://github.com/pcharbon70/catena/commit/e7fea0bda483f377e90ec911b1a54020766e13c8).
The merge retained the tested tree exactly (tree `c3cd077`), and the
compiler PR was merged before this research promotion, following the
established publication order.

## Evidence

The compiler adds the `prelude:` option to
`Catena.build_namespace_environment/2` (fifth in-place grammar
extension to `0.1.22`, both event shapes accepted), the `prelude`
injection in the builder's base case with `PKG004` rejection for
unknown packages, `PRE001` validation for malformed selections at the
option layer, the optional `prelude` field in the 0.1.7 manifest
decoder with `PRE001` shape rejection, and `merge_prelude` in
`Catena.Package.Deps.resolve/2` treating the selection as an implicit
root dependency, plus the `guides/language/prelude.md` guide.

Focused verification:

```text
mix test test/catena/c026_prelude_policy_test.exs \
  test/catena/c026_traceability_coverage_test.exs
Result: 9 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 332 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration, and
pinned predecessor defaults (with the resolver's grammar advancing to
0.1.22 and the C021–C024 EDN001 required-version pins updated); the
zero-implicit-names guarantee (absent and `null` both resolve nothing,
with `PKG004` for unknown prelude names); every `PRE001` shape
(non-object, missing fields, invalid requirement grammar) at the option
and manifest layers; prelude-origin admission and unqualified resolution
with `Core` origin; local-beats-prelude shadowing; prelude-import
`NSP004` collisions with both origins sorted, resolved by
qualification; prelude resolution through `Package.Deps` with `PKG003`
for bad requirements and `PKG004` for unknown names; lock generation,
byte-determinism, and exact-pin replay including the prelude; manifest
decode round trips with the `prelude` field present, absent, and
malformed; and determinism with no phase expansion beyond existing
boundaries.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit; 361 completed documents
were checked across 33 directories with 3,819 local links, 97
specification chapters, 497 traceability obligations, and all 26
validator unit tests passing.

## Version and boundary decision

C026 consumes `0.1.22` for the prelude field, origin injection, and
`PRE001`. The manifest extension is optional and backward-compatible;
no kernel, retained-JSON, interface, artifact, or signed-format version
changes. Every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.23`.

## Threads

- G101 must freeze prelude contents and decide whether any future
  edition names a default prelude through a lifecycle record; P102 owns
  collection protocols the prelude may re-export; G121 may scaffold the
  field but never imply selection; G028/G136 own compatibility
  meanings of prelude version bumps.

## Follow-ups

Section 3's remainder: G027 (entry points) and G028 (API/ABI
compatibility, now also owning re-export facades). P109 remains the
surface capstone.
