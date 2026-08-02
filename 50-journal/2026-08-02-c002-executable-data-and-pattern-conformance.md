---
title: "C002 Executable Data and Pattern Conformance"
kind: journal
created: "2026-08-02"
tags:
  - algebraic-data-types
  - beam-vm
  - pattern-matching
aliases:
  - "C002 compiler experiment"
---

# C002 Executable Data and Pattern Conformance

## Question

Can the C002 data and pattern rules be implemented as an extension of the
clean C001 Elixir bootstrap, verified before lowering, and executed on OTP 29
with two representation strategies that preserve source observations?

## Environment

- Repository: `pcharbon70/catena`
- Branch: `rewrite`
- Implementation commit: `ae311604ef587a022ce2b7b46599200fcb96a7ab`,
  published on `origin/rewrite`
- Erlang/OTP: 29.0.4, ERTS 17.0.4
- Elixir: 1.20.2 compiled for OTP 29
- Input: JSON AST 0.1 compatibility plus normalized JSON AST 0.2
- Backend: Erlang Abstract Format passed only to `compile:noenv_forms/2`

## Method

The implementation adds declaration elaboration, nominal types, pattern
checking, usefulness coverage, GADT refinements, rigid existentials,
typed-core verification, deterministic module interfaces, generated folds,
uniform and compact layout lowering, and a layout-independent reference
evaluator.

The verification commands were:

```bash
asdf current
asdf exec elixir --version
asdf exec mix format --check-formatted
asdf exec mix compile --warnings-as-errors
asdf exec mix test
asdf exec mix escript.build
git diff --check
```

The 39 passing tests include all 17 C001 regressions and C002 cases for:

- AST 0.1 normalization and AST 0.2 declarations;
- empty, negative, and mutually recursive types;
- positional and named construction with source-order evaluation metadata;
- match exhaustiveness, witnesses, redundancy, guards, and `or` patterns;
- a deterministic coverage-budget failure and bounded Boolean corpus;
- transparent, abstract, imported, aliased, and tampered interfaces;
- annotated GADT evaluation and existential escape rejection;
- compiler-generated fold checking and execution;
- corrupted constructor and decision-tree evidence; and
- deterministic compile, load, and execution under both layouts.

The durable fixture is
`test/fixtures/c002-option.catena.json` in the compiler repository. The layout
observation command compiled it under each layout, loaded its module, observed
`make/0`, ran `main/0` 10,000 times, and inspected BEAM and interface sizes.

## Result

Both layouts compiled to 900-byte deterministic BEAM files and produced the
same 1,820-byte layout-free `.cati.json` interface. Their BEAM hashes differed,
as expected:

| Layout | BEAM SHA-256 | `make/0` term words | 10,000 `main/0` calls |
| --- | --- | ---: | ---: |
| uniform | `0614fe5816396ff4e891feaa88553cb49bcd90cbc3b02c27fc6d791982f69a9a` | 7 | 5,576 µs |
| compact | `0cd4f804af4fab3b118eb31b891ef327683550d52fae65d70748c356ce5c6ee3` | 3 | 5,411 µs |

The timing is one local sample, not a performance claim. Term size confirms
only that the chosen example makes the reference wrapper larger than the
compact tuple. The interface bytes were identical because layout information
is intentionally absent.

The reference evaluator and both BEAM layouts returned `7` for the fixture's
typed match. Generated `Option.fold` selected the correct handler. Abstract
interfaces omitted constructors; transparent imported construction worked;
tampering changed the digest and was rejected.

A separate escript smoke test ran `compile-ir --layout uniform` against a copy
of the durable fixture. It reported success and wrote both the 900-byte
`C002Fixture.beam` and 1,820-byte `C002Fixture.cati.json` beside the input.

## Limits

This is executable and differential evidence, not a mechanized proof. The
bootstrap still has no Catena source parser. Its primitive expression set is
small, and the coverage witness language currently exercises integers,
Booleans, tuples, and nominal constructors rather than future strings, lists,
binaries, or structural variants.

The ordered decision representation is deliberately simple. Guard
classification proves only literal `true` and `false`; other typed Boolean
guards remain unknown for coverage. Foreign-term validation, stable ABI,
categorical derivation, programmable patterns, and full effectful evaluation
remain outside C002.

The normative boundary and proof status are in the
[Data and Pattern Specification](../60-specification/data-and-patterns/README.md).
