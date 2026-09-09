---
title: "Checked Arithmetic and Explicit Rounding"
kind: specification
created: "2026-09-09"
status: normative
spec_version: "0.1.67"
tags: [specification, numerics, conformance]
aliases: []
---

# Checked Arithmetic and Explicit Rounding

## Status and authority

C105 applies to edition `0.1`, exact semantic revision `0.1.67`, without previews,
under [authority](../../SPECIFICATION-AUTHORITY.md),
[conformance vocabulary](../../CONFORMANCE-VOCABULARY.md) and
[implementation limits](../../IMPLEMENTATION-LIMITS.md). It executes the
[reviewed numeric plan](../../20-notes/language-completion-plan-delivery.md#item-105-numeric-library).
It adds checked numeric operations, an ordinary decimal package and an exact
numeric-program artifact. Public names, source syntax and automatic imports are
not adopted (`NL-OBL-001`).

The [closed primitive set](../numeric-relationships/the-closed-set-instantiation-rule.md#the-rule)
remains Int and Float; operands do not mix implicitly. The
[literal elaborator](../numeric-literal-semantics/numeric-types-and-literal-typing.md)
retains its historical grammar and static overflow behavior. Decimal is ordinary
nominal library data, not a new primitive or an implicit coercion target.

## Integer arithmetic and division

Checked integer addition, subtraction and multiplication return the exact
mathematical Int result, subject to resource limits. Euclidean division of a by
nonzero b returns the unique pair (q, r) satisfying a = b*q + r and
0 ≤ r < abs(b), including negative divisors. A zero divisor returns typed failure;
there is no truncating or floor-division ambiguity (`NL-OBL-002`).

## Finite binary64 arithmetic

Float contains only finite binary64 values. Checked addition, subtraction,
multiplication and division round the exact real result once to nearest,
with ties to even. Gradual underflow is preserved. A rounded result outside the
finite domain returns overflow failure; division by either signed zero returns
zero-divisor failure, including zero divided by zero. Non-finite bit-pattern
ingress returns nonfinite failure (`NL-OBL-003`).

Multiplication/division zero has the exclusive-or operand sign. Addition of two
negative zeros returns negative zero; other exact-zero sums return positive zero.
Subtraction follows addition with the second operand's sign inverted. A nonzero
exact result that rounds to zero retains its sign. No implicit Int/Float mixing
is admitted at either type checking or the checked library boundary.

## Primitive traps and typed answers

The new artifact admits explicit primitive-operation steps for same-type
addition/subtraction/multiplication, preserving the operand/result type. Finite
Float overflow is a trap whose reason is the closed structural variant
arithmetic containing overflow containing Unit. It is propagated through the
existing kernel `catena_trap` carrier. It is not an unclassified host badarith or
a new terminal class. This introduces the reserved arithmetic producer under
C036's [entry rule](../runtime-failure-taxonomy/the-six-categories.md#the-entry-rule).
The step uses the primitive result directly before the surrounding pipeline
wraps successful completion. It does not retroactively change retained artifacts
or make Float arithmetic expressions legal in the retained value-tree checker
(`NL-OBL-004`).

Explicit checked library operations instead return C103
[dependent outcomes](../outcome-contracts/values-sequencing-and-validation.md):
success contains the result, failure contains a closed variant whose alternatives
are zero_divisor, overflow, domain, inexact, decimal_precision, malformed_number
and nonfinite, each carrying Unit. Failure is an ordinary value and stops dependent
sequencing. Invalid operation/type/context descriptors and resource refusals
remain boundary errors. Existing explicit source traps propagate separately.

## Explicit conversions

Int-to-Float and decimal-to-Float select exact or nearest-even conversion.
Both perform one correctly rounded rational conversion; overflow is typed failure.
Exact conversion additionally fails with inexact when the finite result differs
mathematically from the input. Float-to-Int selects half-even, half-away,
toward-zero, floor, ceiling or exact. Exact rejects nonintegral values. Signed
Float zeros both convert to Int zero. Float-to-decimal uses the Float's exact
binary rational value and the supplied decimal context (`NL-OBL-005`).

Bit conversion accepts an unsigned 64-bit Int, preserving every finite encoding;
exponent-field-all-ones patterns return nonfinite. Values outside that unsigned
range are invalid inputs. The inverse returns the exact encoding as Int.

## Decimal package and contexts

The verified ordinary package defines one nominal Decimal with coefficient and
scale Int fields. Its mathematical value is coefficient × 10^(-scale). Scale is
retained as quantum: values with different coefficient/scale pairs can denote the
same rational without their structural nominal equality being changed. Zero has
no decimal sign. Compiled constructors and eliminators are ordinary declarations;
the checked numeric boundary verifies admitted coefficient/scale values again.

A context explicitly supplies exact revision, output scale, maximum number of
coefficient decimal digits, and rounding mode. Scale ranges from -1024 to 1024;
precision from 1 to 4096. Mode is half-even, half-away, toward-zero, floor, ceiling
or exact. Verification reconstructs the complete context and rejects extra fields.
There is no process-global, locale or ambient precision setting (`NL-OBL-006`).

Addition, subtraction, multiplication, division and rescaling first compute the
exact rational result, then round once to the context's output scale. Half-even
selects an even coefficient at a midpoint; half-away selects the coefficient
farther from zero. Directed modes have their mathematical direction for either
sign. Exact rejects a nonintegral scaled coefficient. A rounded coefficient
requiring more than the declared digits returns decimal_precision; it is not
silently rescaled. A zero divisor returns zero_divisor. Successful output retains
the requested scale. Operand coefficients admit at most 4096 decimal digits.
The ordinary constructor can represent unchecked input, but checked operations
refuse malformed or out-of-profile decimal values (`NL-OBL-007`).

## Parsing and formatting

Float printing returns the exact decimal expansion of its finite rational value,
with optional minus, at least one integral digit, a decimal point and at least one
fractional digit. It uses ASCII digits, no exponent and no grouping. Leading
integral zeros and trailing fractional zeros are removed except the single zero
needed on either side of the point. Both zeros print with their original sign.
The result is deterministic and round-trips bit-for-bit; shortest output is not
promised (`NL-OBL-008`).

Runtime parsing consumes the entire ASCII string: optional sign, one or more
digits, optional point followed by one or more digits, and optional e/E with
optional sign and one or more exponent digits. Whitespace, separators, trailing
text, non-finite words and malformed bytes are not accepted. Parsing rounds the
exact decimal value once; overflow fails, underflow preserves the mathematical
sign through signed zero. The parser admits at most 4096 input bytes. Larger text
is malformed_number under this fixed library admission contract. Huge exponent
magnitudes are classified before constructing powers of ten. This grammar is a
library data format and does not widen source literal grammar.

## Mathematical functions and admission

Square root is admitted for nonnegative finite Float values, with one correctly
rounded nearest-even result. It preserves either signed zero and returns domain
failure for negative nonzero values. The finite-domain result never overflows.
The implementation locates neighboring representable values and compares the
input against their exact squared midpoint; no host transcendental estimate
supplies a binding answer (`NL-OBL-009`).

The initial transcendental set is empty. Sine, cosine, exponential, logarithm and
power are unsupported operation roles. Follow-up gate NL-T01 requires a pinned
kernel, precise admitted domain/rounding specification, review of upstream proof
and hard-case evidence, independent local validation, and integration through
C098's native boundary if native code is used. Availability in CORE-MATH or an OTP
host function does not itself satisfy that gate. No ULP or bit-exact claim is made
for an absent function.

## Typed compiled and reference adoption

The exact `0.1.67` numeric artifact takes verified retained core, an exported pure
unary entry, a fixed typed operation pipeline and explicit C095 budgets. It admits
ordinary retained JSON core, kernel `0.1.8` core and C093's checked `0.1.58` pure
value-tree core. Input and the initial source result require C095 closed-data
schemas. Actual source computation runs before the numeric pipeline.

Each operation has a fixed transition: same-type numeric pairs to the corresponding
numeric result; integer pairs to Euclidean pairs; explicit scalar conversion,
format/parse and square-root transitions; a coefficient/scale pair to nominal
Decimal; explicit decimal rescaling/conversion/elimination; or four Int components
to a declared decimal-pair operation. No arbitrary native callback, effectful
entry or inferred conversion is admitted. Dependent failure skips later steps.
Pipelines admit at most 253 steps (`NL-OBL-010`).

The sidecar binds retained core, entry, operations, budgets, input/result/failure
schemas, numeric profile, full compiler identity, lowered forms and exact BEAM
bytes. Verification rebuilds the artifact. Invocation validates the native input,
serializes loading, reuses identical loaded bytes and rejects a conflicting
same-name module. The reference path independently executes source through its
existing evaluator and applies the checked operation semantics; primitive-step overflow
has the same arithmetic reason in either path. Ordinary decimal declarations
compile separately under the existing nominal system (`NL-OBL-011`).

## Bounds and costs

C095 [whole-carrier budgets](../erlang-type-boundary/typed-conversion-and-preservation.md)
apply to the complete operation/input carrier and returned outcome, including
error payloads. Decimal precision/scale, parser length and pipeline limits above
are fixed profile bounds. Existing source/literal, generated-code and runtime
allocation limits apply. A carrier refusal is not a numeric failure answer.

Integer/rational operations charge work proportional to their operand arithmetic
cost; exactness is not a constant-time promise. Basic Float inputs bound their
rational expansion by binary64 width. Square root performs at most 63 search
comparisons plus exact midpoint arithmetic. Exact printing can have 1074 fractional
places and scans/constructs its complete output. Decimal operations can create
intermediate integers larger than final precision before rounding; the bounded
scales and operand digits bound that expansion. General large Int operations
check complete results after computing them; budgets are admission/output limits,
not a promise to prevent every intermediate allocation. Source termination and
artifact rebuilding remain separate costs (`NL-OBL-012`).

## Variability register

Binary64 nearest-even arithmetic, signed-zero rules, exact decimal printing,
Euclidean division and the initial empty transcendental set are fixed. Rounding,
precision, scale and operation selection are explicit values. Decimal scale is
-1024..1024, coefficient precision 1..4096 digits, parser input 4096 bytes and
pipeline length 253. C095 node/byte/depth budgets are explicit and inherited source
and runtime bounds apply. There is no host-libm accuracy allowance.

## Rationale and evidence (non-normative)

The [journal](../../50-journal/2026-09-09-numeric-library.md) records all decisions,
independent rational vectors, midpoint tests and compiled/reference adoption.
The existing [IEEE source note](../../30-sources/ieee-2019-754-floating-point.md)
provides binary64 background. The [CORE-MATH source note](../../30-sources/core-math-correct-rounding-kernels.md)
records the upstream lead and why NL-T01 remains an explicit gate.
