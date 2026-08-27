---
title: "Float Equality and Semantics"
kind: specification
created: "2026-08-26"
status: candidate
spec_version: "0.1.30"
tags:
  - equality
  - ordering
  - float
  - specification
aliases:
  - "Catena float comparison"
---

# Float Equality and Semantics

## Status and authority

This chapter is the normative Catena 0.1.30 float-comparison contract.
It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies the finite-binary64 contract of
[Numeric Literal Semantics](../numeric-literal-semantics/README.md)
to the comparison operators.

The rules apply only to source-language revision `0.1.30`. They do not
reinterpret retained manifests, interfaces, artifacts, or signed formats.

## Bit-exact equality

Float equality is **bit-exact** (`EQ-OBL-002`):

> **Normative definition.**

```text
x equal y   ⟺   bits64(x) == bits64(y)
```

- The two signed zeros are **distinct**: `−0.0 ≠ 0.0` — consistent
  with C029's grammar, which admits them as distinct values, and with
  no other value pair being equal-but-distinct.
- Reference and compiled implementations compare the 64-bit patterns
  directly; a conforming implementation MUST NOT equate the signed
  zeros.

## Total ordering

Float ordering is **total** with no ties (`EQ-OBL-003`):

> **Normative definition.**

```text
−0.0 < 0.0 < positive-denormals < ... < largest-finite
```

- The order extends the numeric order with `−0.0` immediately below
  `0.0`; every two distinct floats are ordered, and equal floats
  (bit-exact) are unordered-with-respect-to-strict-comparisons exactly
  as integers are.

## No NaN exists

There is no NaN semantics to define (`EQ-OBL-002`): C018 fixes
`Float` as finite binary64 with no NaN-producing operation in the
closed inventory — literals are finite (`NUM001` rejects overflow),
and no division-like operator exists. The checklist's "floats
including NaN" clause therefore resolves as an **elevation of C018's
finite-only guarantee**: no NaN exists in the value space, equality is
total, and no comparison traps. Should a future slice introduce a
NaN-producing operation, its slice owns the NaN semantics through the
entry rule.

## Target precedent (non-normative)

The [OTP compatibility analysis](../../30-sources/erlang-otp-compatibility-and-upgrading.md)
records OTP 27 moving `0.0 =:= -0.0` from `true` to `false` — the
target runtime's own direction — and the compiler already lowers
`equal` to `=:=`, which distinguishes the signed zeros on OTP 27+.
Catena's rule follows the target rather than fighting it.

## Determinism

Comparison is deterministic and observable only through its `Bool`
result (`EQ-OBL-008`): no traps, no effects, total over the closed
set.

## Deliberately separate work

NaN-producing operations and their failure modes remain their
introducing slices'; the runtime failure taxonomy remains G036's
(nothing here can trap); IEEE-semantics switches remain gated behind
an edition record (observable, breaking).

## Rationale and evidence (non-normative)

The [equality synthesis](../../20-notes/catena-equality-and-ordering.md)
records the three forces converging on bit-exactness: C029's distinct
signed zeros, no NaN to accommodate, and the target's existing
behavior. The [topic map](../../10-maps/equality-and-ordering.md)
routes the decision.
