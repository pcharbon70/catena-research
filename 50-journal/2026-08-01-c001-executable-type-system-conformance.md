---
title: "C001 Executable Type-System Conformance"
kind: journal
created: "2026-08-01"
tags:
  - beam-vm
  - catena
  - type-inference
aliases:
  - "C001 compiler experiment"
---

# C001 Executable Type-System Conformance

## Numbering amendment

This record predates the approved prototype-slice renumbering. The observed
compiler input and compile metadata at this historical run used `0.1`; those
observations are preserved rather than rewritten. The current canonical C001
designation is `0.1.1`. The complete mapping and the requirement for a fresh
cross-slice executable identity are recorded in
[Prototype Slice Renumbering](2026-08-04-prototype-slice-renumbering.md).

## Question

Can the C001 specification be exercised by a clean Elixir bootstrap compiler
that produces runnable BEAM code only through the supported OTP 29 language-
implementor boundary?

## Environment

- Repository: `pcharbon70/catena`, clean rewrite branch
  `agent/p001-type-system`
- Erlang/OTP: 29.0.4
- Elixir: 1.20.2 compiled for OTP 29
- Build input: versioned JSON AST `0.1`; no Catena source parser
- Backend: Erlang Abstract Format passed to `compile:noenv_forms/2`

The implementation was written from the new
[type-system specification](../60-specification/type-system/README.md), not
from the archived Catena proof of concept.

## Method

From the sibling compiler repository:

```bash
asdf current
asdf exec elixir --version
asdf exec mix format
asdf exec mix test
git diff --check
```

The tests exercise Algorithm W and `let` generalization, skolemized export
signatures, infinite-type rejection, a bounded independent declarative oracle,
unique and duplicate row behavior, trait ownership and non-overlap, associated
type lookup, rigid existential escape, affine token races, typed-core
verification, deterministic OTP compilation, BEAM loading, and execution.
The runtime cases include polymorphic `let` and a partially applied curried
top-level function used as a first-class value.

The backend test also inspects Erlang Abstract Format for the module and
original-source attributes and inspects the BEAM compile-info chunk for the
Catena specification and frontend versions.

## Result

The pinned OTP 29 run passed all 17 tests. Two compilations of the same typed
module produced identical binaries under deterministic mode. OTP loaded the
generated module and its exported `main/0` returned `{7, true}`. Eight
concurrent attempts to consume one resumption token produced exactly one
winner.

No production path constructs `.beam` content or invokes BEAM assembly. The
only binary generation call is `compile:noenv_forms/2` in the OTP adapter.

## Limits

The result is evidence for the C001 executable slice, not a complete language
implementation or an unbounded proof. The JSON AST supports only the pure
expression subset needed to exercise inference and backend integration. Rows,
traits, GADT scoping, and affine resumptions have executable contracts and
focused tests but are not yet integrated into Catena source programs. The
bounded declarative comparison cannot establish principality for all terms.

These limitations are reflected in
[Type-System Metatheory](../60-specification/type-system/metatheory.md) and the
[language completeness checklist](../00-inbox/language-specification-completeness-checklist.md).
