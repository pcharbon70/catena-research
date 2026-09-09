---
title: "2026-09-09 Numeric Library"
kind: journal
created: "2026-09-09"
tags: [numerics, specification, conformance]
aliases: []
---

# 2026-09-09 Numeric Library

## Scope and outcome

Executes [P105](../20-notes/language-completion-plan-delivery.md#item-105-numeric-library)
at approved semantic revision 0.1.67. The [contract](../60-specification/numeric-library/checked-arithmetic-and-explicit-rounding.md)
defines executable checked arithmetic, conversions, decimal contexts and formatting.
Public vocabulary remains held. Original CP-105-1..6 recommendations are retained.

## Implementation decisions

Every fork below records at least four alternatives before its implementation is
committed. Role labels are implementation identifiers, not adopted user vocabulary.

| Decision | Question | Alternatives | Recommended | Selected | Reason |
| --- | --- | --- | --- | --- | --- |
| NL-I01 | Finite arithmetic engine | A host operations; B exact-rational operations with one binary64 rounding; C decimal approximation; D saturating arithmetic | B | B | Exact integers make rounding, overflow and signed-zero policy independent of libm. |
| NL-I02 | Square root kernel | A unchecked host sqrt; B port a native libm; C binary-search representable roots and compare exact squared midpoints; D omit roots | C | C | A bounded 63-step search admits an independently testable correctly rounded algebraic function without native integration. |
| NL-I03 | Transcendental admission | A expose all host functions; B measured host whitelist; C retain an empty initial transcendental set pending per-kernel validation; D label ordinary host results exact | C | C | CP-105-6 permits unsupported functions to remain absent with named follow-up work; current upstream availability alone is not local validation. |
| NL-I04 | Float printing | A host shortest printer; B fixed 17 digits; C exact decimal expansion with canonical zero/trailing-zero rules; D locale display | C | C | Exact finite expansion guarantees deterministic round trips without promising shortest or attractive display. |
| NL-I05 | Runtime numeric parser | A reuse source token syntax; B explicit bounded ASCII decimal grammar; C host parsing with trailing text; D evaluated text | B | B | The library grammar can round exact decimal ratios without widening source syntax or accepting non-finite values. |
| NL-I06 | Conversion loss | A implicit promotion; B silent truncation; C explicit exact/nearest Float conversion and declared integer rounding modes; D universal rationals | C | C | Keep C061's primitive closed set and make loss a typed decision. |
| NL-I07 | Decimal representation | A new primitive type; B ordinary coefficient/scale nominal value; C binary Float wrapper; D formatted Text | B | B | A library value preserves decimal quantum and composes with existing nominal data and typed outcomes. |
| NL-I08 | Decimal context | A ambient thread settings; B global precision; C explicit output scale, coefficient-digit precision and rounding; D infer scale from operands | C | C | A pure operation rounds once to a context carried in its verified descriptor. |
| NL-I09 | Rounding modes | A truncation only; B host defaults; C half-even/half-away/toward-zero/floor/ceiling/exact; D stochastic rounding | C | C | The closed explicit set covers common directions and checked exactness without hidden state. |
| NL-I10 | Decimal limits | A unbounded scale; B fixed cents; C scale -1024..1024 and 1..4096 coefficient digits; D silently clamp | C | C | Fixed declared bounds prevent attacker-selected exponent allocations; exhaustion and invalid setup remain distinct. |
| NL-I11 | Integer division | A host truncating quotient; B floor quotient; C Euclidean quotient/remainder; D implicit host semantics | C | C | The selected CP-105-5 law holds for either divisor sign; zero division returns a typed library failure. |
| NL-I12 | Primitive fault adoption | A mutate retained backends globally; B new-artifact primitive steps classify overflow as an arithmetic trap; C change primitive result types; D swallow badarith | B | B | Exact 0.1.67 adoption supplies the missing producer classification while preserving old artifact interpretation. |
| NL-I13 | Compiled library adoption | A host-only facade; B new source vocabulary now; C rebuilt typed operation pipeline over retained core; D arbitrary remote calls | C | C | The program executes real source computation before fixed numeric operations and binds exact compiler/forms/binary identity. |
| NL-I14 | Decimal transport into pipelines | A reinterpret arbitrary tuples as decimals; B typed four-Int pair construction and explicit nominal elimination; C add implicit nominal schema exceptions; D raw host callback | B | B | The initial source boundary stays C095 closed data; declared transitions produce ordinary nominal decimals internally. |
| NL-I15 | Failure algebra | A host exceptions everywhere; B strings; C closed C103 dependent failure variants, with primitive traps separate; D nullable values | C | C | Zero divisor, overflow, domain, inexactness, precision, malformed text and non-finite ingress compose without exception recovery. |
| NL-I16 | Evidence model | A examples only; B host differential alone; C Python Fraction vectors plus exact root inequalities and compiled/reference witnesses; D decimal-output snapshots only | C | C | Independent rational rounding exercises basic operations; source execution and provenance checks exercise adoption. |
| NL-I17 | Resource checks | A output only; B input only; C complete operation/input and returned-outcome budgets plus fixed scalar bounds; D implicit defaults | C | C | Carrier limits remain observable setup/resource refusals rather than numeric answers; output work is charged honestly. |
| NL-I18 | Module identity | A overwrite loaded code; B trust module name; C serialize exact-byte reuse and reject conflicts; D random names per invocation | C | C | The artifact cannot silently execute different same-name code and does not leak unbounded generated atoms per call. |
| NL-I19 | Retained Float expression boundary | A widen the historical checker silently; B invent accepted source spelling; C explicit typed primitive steps after retained source computation; D omit the overflow witness | C | C | The checked 0.1.58 tree rejects Float arithmetic expressions. Respect that evidence while making the producer executable in the exact new artifact. |

## Local implementation and evidence

`Standard.Numeric.Binary64` decodes exact bit-pattern rationals, computes basic
operations with integer arithmetic, and rounds once. Its root search uses ordered
positive binary64 encodings and squared rational midpoints. Exact printing
constructs finite decimal expansions; the separate bounded parser does not reuse
or widen the source grammar.

`Standard.Numeric.Decimal` uses an ordinary nominal coefficient/scale pair.
Context precision counts output coefficient digits at the requested scale, not an
ambient significant-digit setting. Arithmetic computes the exact ratio before
one rounding. `Package` verifies complete ordinary declarations and hierarchy
identity. This adds no built-in type or implicit numeric coercion.

`Program` verifies retained core, checks fixed operation transitions and compiles
an exact 0.1.67 wrapper. It executes source computation first and binds compiler,
forms, operation/limit/profile data and BEAM bytes. Module reuse requires identical
loaded bytes. The reference path separately executes retained source, then uses
the same numeric semantics; independent arithmetic oracles cover that shared layer.

A proposed source-overflow witness first used unsupported `mul` spelling, then
revealed that retained 0.1.58 checks arithmetic operands as Int. Neither fixture
failure justifies changing historical grammar. The final witness uses an explicit
typed primitive operation in the new pipeline and distinguishes its arithmetic
trap from the checked operation's dependent failure value. No claim is made that
this session made Float arithmetic expressions legal in the old checker.

The C105 tests exercise signed Euclidean identities over small ranges and a
5,001-digit integer, signed zeros, subnormal midpoint ties, maximum finite values,
non-finite ingress, exact conversion loss, very large integer overflow, decimal
modes and bounds, complete-carrier refusals, compiled ordinary/tree execution,
ordinary nominal declarations, sidecar tampering, module conflicts and pipeline
limits. Float print/parse covers more than 2,000 finite patterns. Square-root
results satisfy exact neighboring midpoint inequalities and agree with the host
oracle on over 300 boundary/deterministic patterns.

`scripts/build_numeric_vectors.py` uses Python `fractions.Fraction`, deterministic
seed 105 and a single Python binary64 conversion of each exact rational result.
It generated 6,688 add/subtract/multiply/divide vectors, including zero and overflow
classifications, stored in `test/fixtures/numeric-rational-vectors.json`. This is
independent of the Elixir rounding implementation. Regeneration is deterministic.
The existing full compiler suite covers retained literal semantics and mixed-type
rejection as well as the new library. Measured evidence is for this host's installed
OTP/Elixir toolchain; the specification is a target obligation, not a claim that
unavailable architectures were tested.

## Follow-up NL-T01

The [CORE-MATH reading](../30-sources/core-math-correct-rounding-kernels.md) verifies
the current primary project lead. Initial transcendentals remain absent as the
reviewed plan permits. Admission of each future sine/cosine/exp/log/power kernel
requires a pinned implementation, explicit finite-domain/rounding behavior,
upstream proof/hard-case review, independent local checks and any necessary C098
native-service integration. No ULP promise is inferred from the project overview.

## Verification and provenance

Commands: `python3 scripts/build_numeric_vectors.py`, `mix test`,
`MIX_ENV=prod mix compile --warnings-as-errors`, `MIX_ENV=prod mix escript.build`,
`python3 validate_archive.py` and `git diff --check`. Final results and implementation
provenance are recorded after the full checks complete.

The checklist audit also repaired stale per-section table totals and its next-patch
field. Recounting all 141 actual item rows yields **105 complete, 22 partial,
12 gaps and 2 deferred**; the table and headline now agree.

Final verification: **948 compiler tests passed**, production compilation passed
with warnings as errors, and the production escript built. Regenerating all
6,688 rational vectors preserved SHA-256
`274035d3b9c3fd88bb66e884c18937b0b52e08abfbaa22f43d1fcccbb7929b4b`.
The archive validator passed **642 documents, 79 directories, 123 sources and
193 specification chapters**, with **886 obligations** (791 traced, 74 partial,
21 untraced). Both repositories passed `git diff --check`.

Compiler implementation commit `3c9339a3383f763d6f993e1c5870020b28cc27fb`
merged through [compiler PR 149](https://github.com/pcharbon70/catena/pull/149)
as `0b219bfdb62ddc3fe625b60a954dce54261b4868`. The compiler `rewrite`
branch was synchronized with origin before deleting the feature branch.
