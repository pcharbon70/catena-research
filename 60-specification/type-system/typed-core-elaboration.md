---
title: "Typed-Core Elaboration"
kind: specification
created: "2026-08-01"
status: normative
spec_version: "0.1.1"
tags:
  - beam-vm
  - catena
  - specification
  - type-inference
aliases:
  - "Catena 0.1.1 elaboration contract"
---

# Typed-Core Elaboration

## Explicit core

Every accepted term MUST elaborate to a typed core that records:

- the monotype and evaluation effect of every expression;
- type abstraction and application at generalized bindings;
- explicit trait evidence parameters and selected instance dictionaries;
- explicit lexical capability identities and handler boundaries;
- GADT coercion evidence scoped to the selected branch; and
- affine resumption creation, consumption, or abandonment.

Surface conveniences may disappear, but source spans MUST remain attached to
core nodes. Evidence and coercions have no runtime representation unless
executable code consumes them.

The relevant typed-core forms are:

> **Normative definition.**

```text
term ::= x | literal | fn (x:t) -> term | term term
       | type_fn a -> term | term @t
       | evidence_fn d:q -> term | term {{evidence}}
       | capability c:Effect in term | perform c.operation term
       | handle c with clauses in term
       | coerce equality term
       | resume_once token continuation value
```

Each node carries its result type, evaluation effect, and original source
span. Type, evidence, and equality forms are verification-only unless lowering
identifies an executable dependency.

## Core verifier

A verifier independent of surface inference MUST check the elaborated core.
It trusts declared nominal identities and imported signed interfaces, but it
MUST recheck types, effects, evidence applications, coercion scope, and affine
use. Backend lowering MUST accept only verified core. A verifier failure after
successful surface checking is an implementation defect and MUST NOT be
reported as a source-program type error.

## BEAM-only backend boundary

Catena targets only the BEAM VM. The bootstrap compiler is implemented in
Elixir and is intended to self-host after the language can express its own
toolchain.

The required Catena 0.1.1 lowering path is:

> **Normative definition.**

```text
Catena source or versioned JSON AST
  -> typed core
  -> verified typed core
  -> Erlang Abstract Format
  -> OTP 29 compile:noenv_forms/2
  -> .beam
```

The bootstrap phase accepts a versioned JSON AST so parser design cannot
silently determine type semantics. This format is a toolchain interface, not
Catena source syntax.

A conforming backend MUST use OTP's supported Erlang source or Erlang Abstract
Format route. It MUST NOT directly emit BEAM assembly or construct `.beam`
files. Core Erlang is not the normative interchange because its compiler
interface and primitive operations are not a stable language-implementor
contract. Source annotations and compiler metadata SHOULD preserve original
Catena locations and toolchain version.

The primary platform evidence is recorded in
[Erlang/OTP 29 Compiler Recommendations for Language Implementors](../../30-sources/erlang-otp-29-compiler-recommendations-language-implementors.md).
