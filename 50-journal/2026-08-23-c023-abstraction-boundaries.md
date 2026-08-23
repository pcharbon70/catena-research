---
title: "C023 Abstraction Boundaries"
kind: journal
created: "2026-08-23"
tags:
  - catena
  - abstraction
  - conformance
  - specification
  - testing
aliases:
  - "C023 abstraction evidence"
---

# C023 Abstraction Boundaries

## Observations

Checklist item P023 is complete as C023 and normative source-only language
revision `0.1.19`. The completed boundary confirms the transparent/abstract
pair as the complete constructor-authority vocabulary, declares that no
stable-layout form exists on any frontend (both-layout conformance stays
mandatory and `L001` unchanged, with G028 owning any future
layout-stability contract together with the foreign boundaries), and
sanctions the abstract-type-plus-validating-constructor-plus-observer
invariant idiom with its wildcard-plus-observers coverage consequence.

This is the corpus's first *exclusion-proof* slice: the shipped contracts
already implied the answers, so the compiler work proves the boundary
holds on real paths rather than adding behavior. One production tightening
emerged: export events are now key-whitelisted like imports, so an event
carrying a `layout:` attribute is `invalid_event` rather than silently
ignored — the declared exclusion is executable. The idiom corpus also
recorded two JSON-AST usage facts worth keeping: qualified constructor
references are three segments (`Wrapper.Email.Email` for constructor
`Email` of type `Email` in module `Wrapper`), and parameterized
definitions pair a `parameters` list with a function-typed signature
(closures as definition bodies remain valid but call sites lower
differently).

A pre-existing compiler documentation defect was repaired in the same
change: the CONFORMANCE header rows had stalled at `0.1.17` when C022's
header edit script failed mid-run; they now read through `0.1.19`.

The sibling compiler implementation is commit
[`bbce0ee25fe6f8b64204a4ec757dc6d281d63f9f`](https://github.com/pcharbon70/catena/commit/bbce0ee25fe6f8b64204a4ec757dc6d281d63f9f),
merged into the `rewrite` integration line by compiler PR
[#99](https://github.com/pcharbon70/catena/pull/99) at merge commit
[`4bc2629`](https://github.com/pcharbon70/catena/commit/4bc26290d0476438478e3d67ab4f4b0e0dd72730).
The merge retained the tested tree exactly (tree `7abbfbf`), and the
compiler PR was merged before this research promotion, following the
established publication order.

## Evidence

The compiler adds the `c023_abstraction_test.exs` exclusion and idiom
corpus with `AB-OBL-001`–`AB-OBL-007` tags and its coverage gate, the
0.1.19 lifecycle registration pinning every predecessor default, the
export-event key whitelist, and the `guides/language/abstraction.md`
guide.

Focused verification:

```text
mix test test/catena/c023_abstraction_test.exs \
  test/catena/c023_traceability_coverage_test.exs
Result: 8 passed
```

Complete compiler verification during implementation:

```text
mix format --check-formatted
mix clean
mix compile --warnings-as-errors
mix test
Result: 303 passed
mix escript.build
git diff --check
```

The focused corpus covers exact selection, lifecycle registration, pinned
predecessor defaults, and the absence of new surface functions; the
transparency-enum closure across export events (six invalid modes
including string spellings) and persisted interfaces (four invalid
visibility strings through the retained JSON AST); stable-layout
rejection on export events (`invalid_event` through key whitelisting)
with idiom execution under both layouts asserting `metadata.layout`,
interface shape without layout fields, and loaded-module results; the
smart-constructor idiom compiling and executing in both layouts with
typed-failure validation (`parse 0` rejected, `parse 42` observed) and
the public-wrapper contrast where a transparent wrapper compiles and a
bypass module still constructs through it — demonstrating that wrapper
"invariants" are advisory; wildcard coverage over abstract scrutinees
inside the definer contrasted with constructor visibility there; and
abstract constructors unconstructible and unmatchable through
digest-bound interfaces (`A004` both ways) while transparent
`EmailResult` construction from a client succeeds.

Archive verification after the complete connected bundle and indexes:

```text
python3 validate_archive.py
python3 -m unittest test_validate_archive.py
git diff --check
```

Results are recorded in the promotion commit; 335 completed documents
were checked across 30 directories with 3,484 local links, 88
specification chapters, 465 traceability obligations, and all 26
validator unit tests passing.

## Version and boundary decision

C023 consumes `0.1.19` although it accepts no new input: the revision
carries the exclusion contract, the sanctioned idiom, and its executable
proof, keeping the every-area-one-version invariant. Every predecessor
API retains its exact selection; no new implementation limit, diagnostic
family, or persisted format appears.

The retained JSON AST remains closed at 0.1.7, the exact kernel remains
0.1.8, and interface, artifact, signed-format, and compiler-package
versions do not change. The next unused semantic patch is `0.1.20`.

## Threads

- G028 must design any layout-stability or ABI contract; D046/G040 must
  design views or selective exposure if ever admitted; P093 must map
  representations to BEAM under the same non-observability; G095 must
  keep foreign terms from becoming typed values by shape; G101+ consumes
  the sanctioned idiom in the standard library.

## Follow-ups

Plan G024 or G025 next; P109's declaration grammar can now emit the
complete C020–C022 event vocabulary, and the smart-constructor idiom
gives the standard library its invariant pattern pre-approved.
