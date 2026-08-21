---
title: "Numeric Literal Semantics"
kind: map
created: "2026-08-21"
tags:
  - archive-navigation
  - catena
  - floats
  - integers
  - literals
aliases:
  - "Catena numeric semantics map"
---

# Numeric Literal Semantics

## Scope

This map connects the C017 token components and C001/C003/C010 semantic
constraints that the adopted numeric meaning preserves, the primary evidence
about binary64 and typed literals, the C018 decision artifacts, and the
questions deliberately left to other owners.

## Start here

- [Catena Numeric Literal Semantics](../20-notes/catena-numeric-literal-semantics.md)
  develops the monomorphic `Int`/finite-`Float` model, correct rounding,
  static overflow refusal, negation semantics, and rejected alternatives.
- [Resolved numeric literal inquiry](../40-inquiries/how-should-catena-define-numeric-literal-semantics.md)
  records the operational question, hypotheses, and resolution.
- [Numeric Literal Semantics Specification](../60-specification/numeric-literal-semantics/README.md)
  is the normative version 0.1.14 contract.
- [C018 evidence record](../50-journal/2026-08-21-c018-numeric-literal-semantics.md)
  records the executable elaborator and verification.
- [Literal Grammar map](literal-grammar.md) fixes the spelling and exact
  components this route gives meaning to.

## Trails

### Foundations that constrain any answer

- [Literal Grammar Specification](../60-specification/literal-grammar/README.md)
  supplies exact numeric components without rounding or type selection.
- [Type System Specification](../60-specification/type-system/README.md)
  excludes numeric defaulting and implicit coercion.
- [Clause Conditions](../60-specification/clause-conditions/syntax-and-safety.md)
  and the [Formal Semantic Kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
  commit the bounded fragments to an unbounded mathematical `Int`.
- [Catena Conformance Vocabulary](../CONFORMANCE-VOCABULARY.md) and
  [Implementation Limits and Portability](../IMPLEMENTATION-LIMITS.md)
  require the overflow outcome and any new digit bound to be classified
  invalidity, limits, or traps — never host-dependent.

### Primary evidence

- [IEEE Std 754-2019](../30-sources/ieee-2019-754-floating-point.md) fixes
  the binary64 domain, `roundTiesToEven`, subnormals, and correctly rounded
  decimal conversion.
- [Erlang/OTP expressions documentation](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
  records the target's `badarith` exceptional arithmetic, host-parser
  refusal of out-of-range decimals, and mixed-type comparison behavior.
- [Haskell 2010 Report](../30-sources/marlow-2010-haskell-language-report.md)
  shows overloaded literals coupled with defaulting and undefined
  exceptional conditions.
- [Rust literal reference](../30-sources/rust-project-2026-literal-tokens.md)
  shows typed-literal resolution with `i32`/`f64` defaults and static
  out-of-range rejection.

### Limits and traceability

- [Implementation Limits and Portability map](implementation-limits-and-portability.md)
  carries the `LIM002` integer floor that the proposed decimal-component
  bound extends.
- [Conformance Traceability](conformance-traceability.md) registers
  `NM-OBL-001` through `NM-OBL-014` against normative anchors and sibling
  compiler tests.

## Open questions

C018 is complete at revision `0.1.14`. G019 retains negation spelling and all
operator tokens;
G040 retains the wider built-in data model; G061 retains numeric trait
relationships; G105 retains explicit conversions and the numeric library;
P035 retains primitive equality and ordering including signed zero; G036
retains the runtime failure taxonomy for arithmetic outside this domain.
