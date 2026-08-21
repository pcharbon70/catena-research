---
title: "Numeric Literal Semantics Specification"
kind: map
created: "2026-08-21"
tags:
  - archive-navigation
  - directory-index
  - floats
  - integers
  - literals
  - specification
aliases:
  - "Catena 0.1.14 numeric literal specification"
---

# Numeric Literal Semantics Specification (`60-specification/numeric-literal-semantics`)

## Purpose

This directory contains the Catena 0.1.14 contract for numeric literal
meaning: the `Int` and `Float` value domains, monomorphic literal typing
without defaulting or coercion, exact decimal-to-binary64 conversion with
correct rounding, static overflow invalidity, numeric unary negation
elaboration, stable diagnostics, the active implementation limit, and
executable conformance obligations.

The repository-level [Specification Authority](../../SPECIFICATION-AUTHORITY.md)
controls status, applicability, rendered labels, and conflicts. The
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md) controls
requirement force, invalidity, diagnostic presentation, and variability. The
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md)
policy supplies the portable floor and common refusal contract for the
decimal-component digit limit activated by this area.

## What belongs here

Put the runtime meaning of already-scanned C017 numeric tokens here:
value domains, literal typing, conversion, rounding, overflow and underflow
outcomes, negation elaboration, diagnostics, limits, and C018 conformance
obligations. Numeric token spelling and components remain the exact
0.1.13 [Literal Grammar](../literal-grammar/README.md) contract. Operator
spelling, precedence, and token composition remain G019/P109. The wider
built-in data model remains G040, numeric trait relationships remain G061,
explicit conversions and the numeric library remain G105, primitive equality
and ordering remain P035, and the runtime failure taxonomy for arithmetic
outside this domain remains G036.

## Variability register

This area introduces no implementation-defined choice, recommendation, or
bounded unspecified presentation. It applies one implementation limit from
the repository policy: `LIM005` measures the total decimal digits of a
decimal literal's exact components with a 4,096-digit portable floor. The
existing `LIM002` integer-magnitude floor continues to apply to integer
tokens under the literal-grammar area. Static overflow refusal is semantic
invalidity (`NUM001`), not a limit.

## Index

### Subdirectories

- None yet.

### Documents

- [Numeric Types and Literal Typing](numeric-types-and-literal-typing.md) —
  the `Int` and finite binary64 `Float` domains, signed zero, monomorphic
  literal typing, the no-defaulting and no-coercion boundary, negation
  elaboration, and the unsigned pattern boundary.
- [Decimal Conversion and Overflow](decimal-conversion-and-overflow.md) —
  exact rational meaning of C017 decimal components, single correct rounding
  with ties to even, subnormal and underflow results, static overflow
  invalidity, and exact integer literal values.
- [Diagnostics, Limits, and Conformance](diagnostics-limits-and-conformance.md)
  — stable `NUM001`, active `LIM005`, the abstract elaboration boundary, the
  BEAM representation, `NM-OBL-001`–`NM-OBL-014`, evidence sets, and
  persistence separation.

## Maintaining this index

Keep all chapters at one lifecycle status and version. A numeric meaning,
typing, conversion, negation, diagnostic, or limit change requires an
explicit later semantic revision. Keep the traceability map, sibling compiler
tests, source-language guides, and this inventory synchronized.
