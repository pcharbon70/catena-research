---
title: "How Should Catena Define Numeric Literal Semantics?"
kind: inquiry
created: "2026-08-21"
status: open
tags:
  - catena
  - floats
  - integers
  - language-design
  - literals
aliases:
  - "Catena numeric literal inquiry"
---

# How Should Catena Define Numeric Literal Semantics?

## Why this matters

C017 closed numeric spelling: every integer token carries its base and exact
mathematical value, and every decimal token carries exact integral,
fractional, and exponent components. Those components still have no runtime
meaning. Until numeric literal semantics are fixed, independent
implementations could disagree about the default types of `1` and `1.0`,
whether `0.1` is the nearest binary64 value or something else, whether
`1.0e400` is a value, an error, or host-dependent, what `-` applied to a
literal means, and which conversions happen silently. Every one of those
disagreements would leak into pattern matching, conditions, serialization,
BEAM lowering, and future numeric libraries.

## Operational question

Choose a bounded 0.1.14 boundary in which independent implementations agree
on:

- the value domains of `Int` and `Float` and the status of infinities, NaN,
  and signed zero;
- the types assigned to unsuffixed integer and decimal literals, with or
  without constraints, defaulting, or expected-type adaptation;
- whether implicit `Int`/`Float` coercions exist anywhere;
- the exact conversion from C017 decimal components to a `Float` value,
  including rounding of ties, subnormal results, underflow to zero, and
  overflow past the largest finite value;
- the elaboration of numeric unary negation, including negative zero, without
  deciding operator spelling or precedence;
- the failure classes and stable diagnostics of refused conversions, and any
  new implementation limit that bounds hostile numeric input; and
- explicit exclusions left to their existing owners.

The answer must compose with C001's no-defaulting and no-implicit-coercion
inference contract, C003/C010's mathematical `Int`, C017's exact components,
C009's behavior classes, and C012's limit contract without silently deciding
G019 operator syntax, G040 built-ins, G061 numeric traits, G105 numeric
libraries, P035 primitive equality, or G036 runtime failure taxonomy.

## Working hypotheses

- `Int` is the unbounded mathematical integer already used by C003 and C010;
  an integer literal denotes exactly the C017 mathematical value.
- `Float` is finite IEEE 754 binary64 with signed zero. Infinities and NaN
  are excluded from the 0.1.14 value domain, aligning with a BEAM target
  whose arithmetic raises rather than producing them.
- Literals are monomorphic: integer tokens have type `Int`, decimal tokens
  have type `Float`. No numeric defaulting and no constraint-based literal
  typing are introduced.
- No implicit numeric coercions exist; mixed arithmetic is ill-typed, and
  explicit conversions are future library work owned by G105.
- A decimal literal's `Float` value is its exact rational value rounded once
  by `roundTiesToEven`; subnormal results and underflow to zero are valid,
  and a magnitude that rounds above the largest finite value is statically
  invalid with a stable diagnostic.
- Numeric unary negation is an elaboration operation: total on `Int`, and a
  sign flip on `Float` that produces `-0.0` from `0.0`. Spelling and
  precedence remain G019's; pattern grammar stays unsigned.
- A new implementation limit bounds the total digits of a decimal literal's
  exact components, mirroring the C012 integer floor.

## Paths to explore

- [IEEE Std 754-2019](../30-sources/ieee-2019-754-floating-point.md) fixes
  the binary64 domain, `roundTiesToEven`, subnormals, and correct rounding.
- [Erlang/OTP expressions documentation](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
  supplies target behavior: `badarith` on float overflow and division by
  zero, `badarg` from the host float parser on out-of-range decimals, and
  mixed-type comparison behavior Catena should not inherit.
- [The Haskell 2010 Report](../30-sources/marlow-2010-haskell-language-report.md)
  shows the alternative: overloaded `fromInteger`/`fromRational` literals,
  defaulting, and undefined fixed-precision exceptional conditions.
- [The Rust Reference](../30-sources/rust-project-2026-literal-tokens.md)
  shows typed-literal resolution with `i32`/`f64` defaults and static
  out-of-range rejection.
- [C017 literal specification](../60-specification/literal-grammar/README.md)
  supplies the exact components this question consumes.
- [C001 type language](../60-specification/type-system/type-language-and-kinds.md),
  [C003 condition safety](../60-specification/clause-conditions/syntax-and-safety.md),
  [C010 kernel syntax](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md),
  and the [implementation limits policy](../IMPLEMENTATION-LIMITS.md) supply
  the constraints any answer must preserve.

## Findings

- Local OTP 29 verification (2026-08-21) confirms the trap-aligned target:
  `1.0e308 * 1.0e308` and `1.0/0.0` raise `badarith`, and
  `list_to_float("1.0e400")` raises `badarg`; the largest finite binary64 is
  `1.7976931348623157e308` by bit-pattern construction. A finite `Float`
  domain therefore describes the target rather than fighting it.
- IEEE 754-2019 makes correctly rounded decimal conversion and gradual
  underflow normative obligations of the format, so exact-component
  conversion with a single rounding is an adoptable requirement rather than
  a local invention.
- Haskell couples overloaded literals with defaulting and leaves
  fixed-precision exceptional conditions undefined; Catena's C001 contract
  excludes the first and C009 forbids the second, so monomorphic literals
  with statically decided overflow follow from already-normative rules.
- Rust demonstrates that static out-of-range rejection and no `inf`/`NaN`
  spellings are implementable, while its `i32`/`f64` defaults are precisely
  the numeric defaulting Catena excludes.
- The synthesis
  [Catena Numeric Literal Semantics](../20-notes/catena-numeric-literal-semantics.md)
  develops the full model, rejected alternatives, and falsification
  criteria; the [topic map](../10-maps/numeric-literal-semantics.md) routes
  the evidence.

## Outcome

Open. Resolution requires candidate normative chapters covering domains,
typing, conversion, negation, diagnostics, and limits; a sibling compiler
implementation with exact decimal-to-binary64 conversion independent of host
float parsing; and tagged executable evidence, following the C013–C017
promotion workflow.
