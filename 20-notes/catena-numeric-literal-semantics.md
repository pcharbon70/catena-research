---
title: "Catena Numeric Literal Semantics"
kind: note
created: "2026-08-21"
maturity: developing
tags:
  - catena
  - floats
  - integers
  - language-design
  - literals
aliases:
  - "Catena numeric literal model"
---

# Catena Numeric Literal Semantics

## Executive conclusion

Catena's first numeric semantics slice should assign meaning to the exact
components C017 already produces, and nothing more. An integer literal is a
value of an unbounded mathematical integer type `Int`. A decimal literal is a
value of a `Float` type whose domain is finite IEEE 754 binary64 with signed
zero; infinities and NaN are excluded from the 0.1.14 domain, so a decimal
whose magnitude rounds above the largest finite value is statically invalid.

Literals are monomorphic and admit no defaulting, no constraint-based typing,
and no implicit numeric coercion. A decimal literal's value is obtained by a
single correctly rounded conversion from its exact rational meaning, with
ties resolved to even significands, subnormal results admitted, and underflow
to zero valid. Numeric unary negation is defined as elaboration semantics —
total on `Int`, a sign flip producing `-0.0` from `0.0` on `Float` — while
operator spelling, precedence, and any negative pattern forms remain open.

This closes G018 as C018 without reopening C017 spelling, without amending
C001's no-defaulting contract, and without deciding G019 operators, G040
built-ins beyond the two numeric types, G061 numeric traits, G105 numeric
libraries, P035 primitive equality, or G036 runtime failure taxonomy.

## Scope and method

The operational target is independent agreement on the runtime meaning of
already-scanned numeric tokens: value domains, literal typing, conversion,
overflow and underflow outcomes, negation, diagnostics, and the one new
finite-resource boundary. The method separates source evidence from Catena
inference: primary standards and language references supply what binary64 and
typed literals mean elsewhere, local OTP experiments supply what the target
actually does, and this synthesis proposes what Catena fixes.

Primary evidence comes from
[IEEE Std 754-2019](../30-sources/ieee-2019-754-floating-point.md), the
re-read [Erlang/OTP expressions documentation](../30-sources/erlang-otp-expressions-and-guard-sequences.md),
the expanded [Haskell 2010 Report note](../30-sources/marlow-2010-haskell-language-report.md),
and the expanded [Rust literal reference note](../30-sources/rust-project-2026-literal-tokens.md).

## Relation to the current corpus

[C017 literals](../60-specification/literal-grammar/README.md) already return
a base, separator-free digits, and the exact mathematical value for integers,
and exact integral/fractional/exponent components with an exponent-sign class
for decimals. The scanner performs no rounding and selects no runtime type.
C018 consumes exactly those components; changing spelling is out of scope.

[C003 clause conditions](../60-specification/clause-conditions/syntax-and-safety.md)
and the [C010 kernel](../60-specification/formal-semantic-kernel/canonical-kernel-syntax.md)
already commit Catena's bounded fragments to an unbounded mathematical `Int`
with total arithmetic and no overflow. Making `Int` the integer literal's
type consolidates those decisions rather than adding a second integer notion,
and keeps the C012 `LIM002` digit floor an input limit rather than a value
range.

The [C001 type system](../60-specification/type-system/type-language-and-kinds.md)
normatively excludes numeric defaulting and implicit coercion, and
[C004 trait resolution](../60-specification/traits-and-categorical-operations/declarations-instances-and-coherence.md)
rejects ambiguous constraints rather than defaulting them. Monomorphic
literals are the only policy that adds numeric meaning without amending any
of those rules.

The [conformance vocabulary](../CONFORMANCE-VOCABULARY.md) requires that an
unrepresentable decimal be either invalid, an implementation limit, or an
explicit trap — never host-dependent or undefined — and the
[implementation limits policy](../IMPLEMENTATION-LIMITS.md) requires any new
finite-resource boundary to be classified, floored, and disclosed rather than
hidden in a parser.

## Comparative evidence and inference

### IEEE 754: adopt the finite core, not the exceptional encodings

The standard fixes binary64's parameters, signed zero, `roundTiesToEven` as
the default rounding, gradual underflow through subnormals, and correctly
rounded decimal conversion. These are stable obligations Catena can adopt
wholesale for the meaning of a decimal literal.

The standard also defines infinities and NaNs, with overflow producing
infinity under the default attribute. That part Catena does not adopt for
0.1.4-domain reasons: the BEAM target raises `badarith` on float overflow and
division by zero rather than producing infinities, Catena literals have no
`inf`/`NaN` spelling (C017), and C009 forbids leaving the outcome
unspecified. A domain that excludes the exceptional encodings makes the
arithmetic operations that would produce them someone else's explicit
decision (G036) instead of an accidental infinity.

### Erlang/OTP: the target is already a finite-float machine

Local OTP 29 verification confirms `1.0e308 * 1.0e308` raises `badarith`,
`1.0/0.0` raises `badarith`, and `list_to_float("1.0e400")` raises `badarg`.
The bit-pattern-constructed largest finite binary64 is
`1.7976931348623157e308`. A finite `Float` domain with raising exceptional
arithmetic therefore describes the target; an infinity-producing domain would
require emulating a machine Catena does not run on.

Erlang's comparison rules are the counter-evidence: `1 == 1.0` is `true`
through mixed-type conversion, and `=:=` distinguishes `0` from `0.0` and
`0.0` from `-0.0`. Catena's no-implicit-coercion boundary and P035's open
primitive-equality question exist precisely so these behaviors are decided,
not inherited through lowering.

### Haskell: overloaded literals purchase defaulting and undefined overflow

Haskell's literals are `fromInteger`/`fromRational` applications with
overloaded typings, usable only together with default declarations, and the
report leaves fixed-precision overflow and underflow undefined. Both halves
are incompatible with Catena: C001 has no defaulting, and C009 prohibits
undefined behavior. Haskell is retained as the evidence that constrained
literals and defaulting are one design, not two separable features.

### Rust: static rejection without defaults

Rust resolves unsuffixed literals by context, defaulting to `i32`/`f64` when
under-constrained, statically erroring when over-constrained, converting
integer values through a fixed-width intermediate with `overflowing_literals`
(deny by default), rejecting literals that would be infinite, and treating
`-` as an operator applied to a positive literal. Catena adopts the static
out-of-range rejection, the absence of exceptional spellings, and the
negation separation, and rejects the defaults because C001 already has.

## Selected model

### Value domains

`Int` is the set of mathematical integers. `Float` is the set of finite IEEE
754 binary64 values: zero, subnormal, and normal magnitudes with either sign,
bounded above by (2 − 2⁻⁵²) × 2¹⁰²³. `+0.0` and `-0.0` are distinct
encodings of the same arithmetic zero; their equality, ordering, and matching
behavior is owned by P035, not this slice. Infinities and NaNs are not
members of `Float` in 0.1.14, and no 0.1.14 operation constructs them.

### Literal typing

An integer token elaborates to an `Int` literal with exactly the C017
mathematical value. A decimal token elaborates to a `Float` literal with the
correctly rounded value below. Both typings are fixed and monomorphic: an
unconstrained literal is as typed as a constrained one, no numeric class or
constraint is generated, and no expected-type or inferred-type adaptation
occurs. Mixed integer/decimal arithmetic and comparison is ill-typed without
coercions; explicit conversions are library work owned by G105.

### Decimal conversion

A decimal token's exact meaning is the rational
`integral.fractional × 10^exponent` built from its C017 components. Its
`Float` value is that rational rounded once to nearest binary64 with ties to
even significands. Rounding may produce any finite magnitude including the
smallest subnormal; an exact value too small to round up to the smallest
subnormal rounds to signed zero and is valid. The largest finite value
itself is a valid literal; any magnitude that would round above it is
statically invalid with a stable `NUM001` diagnostic, independent of any
host parser. Conversion happens once at elaboration; runtime semantics do
not reinterpret the spelling.

### Negation

Numeric unary negation is fixed as elaboration semantics: on `Int` it yields
the additive inverse (total, no overflow); on `Float` it flips the sign bit,
so `- 0.0` is `-0.0` and `- x` otherwise preserves magnitude. The operator's
surface spelling, precedence, and fixity remain G019's; pattern grammar
remains unsigned per C002, so `-1` matches nothing and any negative pattern
extension is future pattern work with its own coverage story.

### Limits and diagnostics

Static overflow refusal is semantic invalidity (`NUM001`), not a limit: the
input has no `Float` value, unlike `LIM002` where a valid value is merely
large. One new implementation limit `LIM005` bounds the total digits of a
decimal token's exact components (integral, fractional, and exponent
magnitude), with a 4,096-digit portable floor mirroring `LIM002`, so a
hostile exponent cannot force unbounded exact-rational work while the
conversion remains exact below the floor.

### Lowering and persistence

`Int` maps to the Erlang integer and `Float` to the Erlang float, consistent
with C010's fixed representation. The wider primitive-to-BEAM model remains
P093's. C017 scanning stays pinned to exact `0.1.13`; the numeric meaning
APIs select exact `0.1.14`; retained JSON, kernel, interface, artifact, and
signed-format versions do not change.

## Rejected alternatives

- **Full IEEE 754 domain (infinities and NaN):** contradicts the target's
  raising arithmetic, has no literal spelling to construct the values, and
  forces the NaN/`Equatable`-reflexivity conflict into P035 now.
- **Exact rational or decimal `Float`:** rounding-free but unrepresentable on
  the target without a library numeric tower that G105 has not designed.
- **Constrained literals with defaulting (Haskell model):** requires
  amending C001's no-defaulting rule and C004's ambiguity rejection before it
  could mean anything.
- **`i32`/`f64`-style inference defaults (Rust model):** same C001 conflict,
  plus fixed-width integers contradict the normative mathematical `Int`.
- **Literal-only or general `Int`→`Float` widening:** an implicit coercion in
  exchange for convenience, needing C001 replacement records and creating
  `1`-in-`Float`-context ambiguity for no measured usability gain.
- **Overflow as a runtime-trapping value or an implementation limit:** a
  literal that cannot denote a value should fail statically as invalid;
  relabeling it a limit would misclassify semantic unrepresentability, and a
  trap-at-runtime constant is a value no program could ever observe.

## What C018 adds to the design

Every later surface, elaborator, and backend inherits one numeric meaning:
two monomorphic types, exact integer values, once-rounded finite decimals,
static overflow refusal, and a sign-flip negation whose syntax is still free.
Conditions, patterns, serialization, and the standard library can then refer
to stable numeric facts instead of per-feature conventions, and the
host-parser boundary is testable: below `LIM005`, conversion is exact and
implementation-independent; above it, refusal is a disclosed limit.

## Remaining questions and falsification criteria

G019 must fix negation spelling and precedence; G040 must place `Int` and
`Float` in the full built-in data model; G061 must relate any future numeric
traits to these monomorphic types; G105 must design explicit conversions and
the numeric library; P035 must decide primitive equality and ordering
including signed zero; G036 must classify the runtime failures of arithmetic
that cannot produce values in this domain.

The model should be revisited if the BEAM target changes its
exceptional-float behavior, if evidence from G105 shows that monomorphic
literals materially damage real numeric code, or if exact-component
conversion below `LIM005` proves non-portable across independent
implementations. Convenience arguments alone do not reopen C001.

## Connections

- The [open numeric literal inquiry](../40-inquiries/how-should-catena-define-numeric-literal-semantics.md)
  records the operational question and evidence trail.
- The [Numeric Literal Semantics map](../10-maps/numeric-literal-semantics.md)
  routes through evidence, constraints, and remaining owners.
- [Catena Literal Grammar](catena-literal-grammar.md) fixes the spelling this
  synthesis gives meaning to.
- [Catena Implementation Limits and Portability](catena-implementation-limits-and-portability.md)
  supplies the limit model `LIM005` extends.

## Sources

- [IEEE Std 754-2019: Floating-Point Arithmetic](../30-sources/ieee-2019-754-floating-point.md)
- [Erlang/OTP Expressions and Guard Sequences](../30-sources/erlang-otp-expressions-and-guard-sequences.md)
- [Haskell 2010 Language Report](../30-sources/marlow-2010-haskell-language-report.md)
- [The Rust Reference: Literal Tokens and Expressions](../30-sources/rust-project-2026-literal-tokens.md)
