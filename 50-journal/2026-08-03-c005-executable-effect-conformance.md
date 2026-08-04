---
title: "C005 Executable Effect Conformance"
kind: journal
created: "2026-08-03"
tags:
  - algebraic-effects
  - beam-vm
  - compilers
  - effect-handlers
  - specification
aliases:
  - "C005 candidate implementation evidence"
  - "C005 executable implementation evidence"
---

# C005 Executable Effect Conformance

## Numbering amendment

This record predates the approved prototype-slice renumbering. Commit
`b24e58d587c830dbb9d8c87770105714745fcd1b` actually used the historical
`0.5` AST and interface values, which remain part of this record. The current
canonical C005 designation is `0.1.5`. See
[Prototype Slice Renumbering](2026-08-04-prototype-slice-renumbering.md) for
the complete mapping and pending cross-slice conformance identity.

## Observations

The sibling Catena compiler implementation is frozen on branch
`agent/c005-effects-handlers` at commit
[`b24e58d587c830dbb9d8c87770105714745fcd1b`](https://github.com/pcharbon70/catena/commit/b24e58d587c830dbb9d8c87770105714745fcd1b),
based on rewrite commit
`1b6b902b146a5539fc1a24f4303f9182fbe431fc`. The user explicitly authorized
the immutable compiler commit on 2026-08-03 before this archive recorded the
identity or promoted the
[version 0.5 effect specification](../60-specification/effects-and-handlers/README.md).
[Compiler PR #67](https://github.com/pcharbon70/catena/pull/67) publishes that
exact identity against `rewrite`; its eventual merge identity is not yet
known.

The Elixir implementation adds:

- JSON AST 0.5 declarations and expressions for nominal generic first-order
  effects, behavior-first `uses`, requests, named handlers, handling, and
  affine resume;
- identity-aware open effect rows, alpha-insensitive tails, exact capability
  subtraction, unique lexical selection, and missing, ambiguous, and escaping
  capability diagnostics;
- named module-level deep handlers with strict argument order, mandatory
  return and complete operation clauses, abort, deep reinstallation, and
  explicitly declared outer clause effects;
- path-sensitive affine resumption checking, non-escape verification, and a
  runtime consumed token that traps before a second continuation entry;
- a free-request reference evaluator whose handler folding is independent of
  the production dispatcher, sharing only the defensive token and trace
  recorder;
- effect-directed CPS workers behind ordinary direct wrappers, while pure
  definitions retain the direct lowering path;
- deterministic hidden BEAM entry points for public cross-module handlers;
- version 0.5 module interfaces that preserve effect and handler identity while
  retaining 0.2 through 0.4 decoding; and
- independent typed-core checks for row evidence, handler structure, and
  resumption discipline.

No Rust, Python compiler component, Core Erlang emitter, direct BEAM assembler,
runtime family-label search, or alternate target VM was introduced. Both the
direct and CPS paths lower through Erlang Abstract Format and OTP 29.

## Evidence

Environment observed in `/home/ducky/code/catena`:

```text
branch: agent/c005-effects-handlers
baseline rewrite commit: 1b6b902b146a5539fc1a24f4303f9182fbe431fc
implementation commit: b24e58d587c830dbb9d8c87770105714745fcd1b
compiler PR: https://github.com/pcharbon70/catena/pull/67
authorization date: 2026-08-03
Elixir: 1.20.2
Erlang/OTP: 29.0.4
target: BEAM only
```

Commands rerun after the immutable commit:

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
Compiling 40 files (.ex)
Generated catena app
Compiling 40 files (.ex)
Generated catena app
Running ExUnit
..........................................................................
Finished in 0.9 seconds
Result: 74 passed
Generated escript catena with MIX_ENV=dev
```

The focused command
`asdf exec mix test test/catena/c005_effects_test.exs --trace` reported 19
passing cases. Those cases cover deep resume and abort; static selection and
qualification; missing, ambiguous, malformed, and escaping effects; callback
purity; outer clause requests; forged typed-core evidence; direct versus CPS
lowering; generic effects and open rows; interface identity; cross-module
handler execution; affine branch use and dynamic double-resume defense; strict
handler argument order; distinct same-family capabilities; nested handler
order; and reference/BEAM value and trace agreement. The complete run keeps
the C001 through C004 corpus green.

Compiler PR #67 publishes the implementation commit without replacing the
tested identity. A later merge record must preserve that identity rather than
substituting the mutable branch head or an untested successor commit.

## Result

The bounded C005 implementation satisfies the version 0.5 promotion gate.
All six effect chapters are normative, and checklist items C005, C076, and
C079 are complete against this immutable identity. Existing normative
selection and resumption boundaries C077 and C078 remain intact.

This result is implementation evidence for the bounded first-order feature,
not a proof that the wider algebraic-effect design is complete. It does not
close resource cleanup, exception and host-effect boundaries, scoped or
higher-order operations, performance, or usability.

## Threads

The broader
[effect-semantics inquiry](../40-inquiries/which-algebraic-effect-semantics-should-catena-adopt.md)
remains open for metatheory, higher-order abstraction, resource safety,
measurement, and programmer comprehension. G080, G081, G082, and D083 retain
the boundaries deliberately excluded from 0.5.

## Follow-ups

1. Add the merge identity after compiler PR #67 is merged.
2. Preserve the implementation identity when a later language version
   supersedes 0.5.
3. Treat cleanup and cancellation as a separate resource-scope design, not an
   accidental consequence of aborting an affine resumption.
