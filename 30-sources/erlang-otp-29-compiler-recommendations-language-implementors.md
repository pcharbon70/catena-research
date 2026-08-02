---
title: "Erlang/OTP 29 Compiler Recommendations for Language Implementors"
kind: source
created: "2026-08-01"
tags:
  - beam-vm
  - catena
  - compiler
  - erlang
aliases:
  - "OTP 29 language implementor path"
authors:
  - "Ericsson AB"
published: "OTP 29"
citation_key: "erlang-otp-2026-compile-language-implementors"
container: "Erlang/OTP System Documentation"
edition: "29.0.4"
isbn: null
doi: null
url: "https://www.erlang.org/doc/apps/compiler/compile.html#recommendations-for-language-implementors"
accessed: "2026-08-01"
---

# Erlang/OTP 29 Compiler Recommendations for Language Implementors

## Reference

Ericsson AB. “Compiler (`compile`) — Recommendations for Language
Implementors.” *Erlang/OTP System Documentation*, OTP 29. Canonical
[compiler documentation](https://www.erlang.org/doc/apps/compiler/compile.html#recommendations-for-language-implementors),
accessed 2026-08-01.

## Research question

Which supported OTP boundary should a new BEAM-only language use, and which
lower-level routes should Catena avoid treating as stable contracts?

## Findings

OTP recommends generating Erlang source or Erlang Abstract Format. Abstract
forms can retain original source locations through line annotations and can be
compiled with `compile:forms/2` or `compile:noenv_forms/2`.

The documentation warns language implementors away from Core Erlang as a
general interchange because compiler-internal primitive operations are
unstable and malformed input can reach backend assumptions. It more strongly
discourages BEAM assembly, which is an internal format and can produce unsafe
results. Compiler options support binary output, deterministic compilation,
source identity, compile metadata, and custom debug information.

## Relevance

Catena therefore uses verified typed core internally, lowers to Erlang
Abstract Format, and delegates `.beam` production to OTP 29. This is the
normative backend boundary in
[Typed-Core Elaboration](../60-specification/type-system/typed-core-elaboration.md).

## Limits

This documentation specifies compiler interfaces, not Catena's semantics. The
abstract-form data model can evolve with OTP, so Catena must pin and test its
supported OTP release rather than copy internal compiler assumptions.

## Derived work

- [Type-System Diagnostics and Conformance](../60-specification/type-system/diagnostics-and-conformance.md)
  requires an actual OTP 29 compile/load/execute test.
- [Catena Language Overview](../language-overview.md) places the adapter after
  typed-core verification rather than treating Abstract Format as a semantic
  core.
