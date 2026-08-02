---
title: "C004 Executable Trait Conformance"
kind: journal
created: "2026-08-02"
tags:
  - beam-vm
  - category-theory
  - compilers
  - specification
  - trait-constraints
aliases:
  - "C004 candidate implementation evidence"
  - "C004 executable implementation evidence"
---

# C004 Executable Trait Conformance

## Observations

The sibling Catena compiler implementation is frozen at commit
[`b69f6f7e3da6015bf9b3385152ca3f3687422472`](https://github.com/pcharbon70/catena/commit/b69f6f7e3da6015bf9b3385152ca3f3687422472),
based on rewrite commit `a4c4a053c02dc13411afde9a2c462aae989ddff3`.
[Compiler PR #66](https://github.com/pcharbon70/catena/pull/66) incorporated it
into `rewrite` as merge commit
[`1b6b902b146a5539fc1a24f4303f9182fbe431fc`](https://github.com/pcharbon70/catena/commit/1b6b902b146a5539fc1a24f4303f9182fbe431fc).
The complete verification sequence was rerun from the immutable implementation
commit, supplying the executable identity for the
[normative 0.4 specification](../60-specification/traits-and-categorical-operations/README.md).

The Elixir implementation adds:

- rigid kinds through binary type-constructor kinds;
- a parameterized trait and instance registry with ownership, non-overlap,
  exact methods, decreasing contexts, functional-dependency consistency,
  associated types, parent cycles, coherent parent substitution, memoized
  evidence, and deterministic budgets;
- a SHA-256-bound ordinary-library interface containing the seventeen
  behavior-first capabilities, their formal reference names, minimal ABI,
  direct parents, laws, and operational metadata;
- JSON AST and module interface version 0.4 with preserved older decoding;
- promised, tested, and derived law tiers plus explicit-Equatable and bounded
  extensional test helpers;
- six explicit-target derivation plans, implicit derived instances,
  type-qualified operations, reference evaluation, BEAM lowering, and
  verifier provenance checks for the prototype's whole-field structural
  profile; `CollectingMapper` is a verified template that selects contextual
  mapping, multi-mapping, and value-embedding evidence rather than collapsing
  to pure mapping;
- verified specialization templates and helper closure;
- a strict toolchain-only package manifest;
- deterministic specialization keys binding template content, concrete types,
  evidence digests, compiler/specification versions, and the standard digest;
- one companion BEAM containing direct remote calls after evidence erasure;
  and
- tested standard `List` `Mapper` and `Reducible` instances whose ordinary
  library implementations use stack-safe reverse accumulation and iterative
  reduction.

No Rust, Python compiler component, Core Erlang emitter, direct BEAM assembler,
runtime dictionary library, package manager, network dependency resolution,
or alternate target VM was introduced.

## Evidence

Environment observed in `/home/ducky/code/catena`:

```text
branch: agent/c004-traits-categories
baseline rewrite commit: a4c4a053c02dc13411afde9a2c462aae989ddff3
implementation commit: b69f6f7e3da6015bf9b3385152ca3f3687422472
compiler PR: https://github.com/pcharbon70/catena/pull/66
merge commit: 1b6b902b146a5539fc1a24f4303f9182fbe431fc
Elixir: 1.20.2
Erlang/OTP: 29.0.4
target: BEAM only
```

Commands run:

```bash
asdf exec mix format --check-formatted
asdf exec mix clean
asdf exec mix compile --warnings-as-errors
asdf exec mix test
asdf exec mix escript.build
git diff --check
```

Observed result:

```text
Compiling 36 files (.ex)
Generated catena app
Compiling 36 files (.ex)
Generated catena app
Running ExUnit
.......................................................
Finished in 0.6 seconds
Result: 55 passed
Generated escript catena with MIX_ENV=dev
```

The new C004 conformance module checks all seventeen public/formal mappings,
all parent evidence, two witnesses for each unitless capability, two Workflow
witnesses, both `TwoSlotMapper` positions, callback visitation order,
structural operations in the reference evaluator and BEAM, explicit equality
evidence, bounded function samples, contextual collection across two fields,
rejected reserved law trust, rejected incomplete helper closure, higher-kinded
type-term round trips, deterministic repeat specialization, direct generated
calls, and absence of dictionary or instance payload in generated forms. The
standard `List` checks resolve interface evidence and execute mapping and
reduction over 250,000 elements without stack exhaustion. The same run keeps
all 46 C001–C003 tests green.

The targeted C004 run also reported nine passing cases by name, including
deterministic specialization to a direct call, companion-BEAM production, and
the 250,000-element standard `List` stress case. This is the repeat-build and
artifact-inspection evidence required by the promotion gate.

## Result

The implementation and chapters make the C004 family complete for version
0.4. All seven chapters are normative and share the immutable compiler identity
recorded above.

The implementation currently enforces a conservative whole-field profile for
mapping, two-slot mapping, reduction, and collection derivation. Its collection
template now selects `Mapper`, `MultiMapper`, and `ValueEmbedder`, preserves
left-to-right field order, rebuilds through layout-private helpers, and erases
that evidence to direct calls. The tested standard `List` implementations now
close the recursive collection stack-safety promotion check. The immutable
publication and verification requirements are now satisfied.

## Threads

Public parser punctuation remains unfrozen because JSON AST 0.4 is the
bootstrap boundary. P107 also remains partial: the public vocabulary is fixed
for the normative ABI, but comprehension and usability have not been measured
independently.

Cryptographic publisher signing remains outside 0.4. The standard and module
interfaces are content-digest-bound; that fact must not be described as a
publisher signature.

## Follow-ups

1. Preserve the implementation and merge identities when later versions
   supersede 0.4.
2. Evaluate comprehension and usability independently before completing P107.
