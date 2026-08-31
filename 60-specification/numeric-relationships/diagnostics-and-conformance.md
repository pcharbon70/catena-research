---
title: "Numeric Relationships Diagnostics and Conformance"
kind: specification
created: "2026-08-31"
status: normative
spec_version: "0.1.40"
tags:
  - conformance
  - diagnostics
  - numerics
  - specification
  - testing
aliases:
  - "Catena 0.1.40 numeric relationships conformance"
---

# Numeric Relationships Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.40 numeric-relationships
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Closed-Set Instantiation Rule](the-closed-set-instantiation-rule.md) and
[Exclusions and Routings](exclusions-and-routings.md).

## Stable diagnostics

This area introduces **zero new diagnostic families**
(`NR-OBL-001`, `NR-OBL-006`). Mixed-type rejection stays the
unification error of the typing families; a non-numeric operand is
the existing operand error; no new invalid input exists.

## Abstract public boundaries

The shipped boundaries witness the contract; the bootstrap adds no
new public API (`NR-OBL-001`):

- **Inference engine** — the same-type arithmetic instantiation is
  witnessed by driving the checker's inference directly with
  float-typed operands: float `add` infers `Float`, Int `add`
  infers `Int` unchanged, and mixed operands reject. The rule is
  correct-but-dormant: no frozen frontend carries a float type or
  literal spelling, so the rule becomes input-reachable with the
  first float-bearing frontend.
- **Evaluator and BEAM lowering** — arithmetic on Elixir floats
  computes natively (`+`/`-`/`*`), dormant until float operands
  can reach them.
- **Value classification** — `Int` and `Float` remain the closed
  set's members (`Catena.Values`, unchanged from C040/C035).

Implementations MUST NOT use these boundaries to claim operator
dispatch, user overloadability, mixed-type acceptance, division,
remainder, implicit conversion, or any frontend float spelling
(`NR-OBL-006`).

## Determinism

Equal operands produce equal results, failures, and traces on
every conforming target (`NR-OBL-006`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `NR-OBL-001` | apply numeric-relationship rules only at exact 0.1.40 and register the stable lifecycle addition with zero new families and no new API | exact selection, registry, and lifecycle tests |
| `NR-OBL-002` | fix the closed-set instantiation rule: operands unify with each other over exactly {Int, Float} | rule-shape tests |
| `NR-OBL-003` | keep operators free of dispatch, evidence, and user overloadability | absence tests |
| `NR-OBL-004` | re-affirm no defaulting, no implicit coercion, no literal constraints; mixed operands ill-typed | mixed-type rejection tests |
| `NR-OBL-005` | make arithmetic same-type over {Int, Float}: the rule accepts float operands, witnessed on the inference engine, dormant until a float-bearing frontend | inference-engine witnesses |
| `NR-OBL-006` | keep the contract deterministic with zero new families and the reuse boundary enforced | determinism and exclusion tests |
| `NR-OBL-007` | route division, remainder, and reserved spellings to G105 with no divide or remainder operator existing | absence tests |
| `NR-OBL-008` | keep the closed set amendable only by a new revision amending the enumeration | exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `NR-OBL-*` set against unknown and
uncovered identifiers before C061 conformance is claimed.

## Required evidence sets

Positive evidence includes the inference engine typing float `add`
as `Float` and Int `add` as `Int` unchanged; ordering and negation
unchanged over both members; Int arithmetic programs running
unchanged on the reference evaluator and compiled BEAM; and the
lifecycle registration of 0.1.40.

Negative evidence — in the definitional sense — includes mixed
`Int`/`Float` operands rejecting in the inference engine, no
dispatch or overloadability entry points, and no divide or
remainder operator existing.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities and predecessor APIs retaining their exact selections
and defaults.

## Revision and persistence separation

Revision `0.1.40` extends arithmetic typing to same-type `Float`
operands and fixes the instantiation rule; it adds no JSON AST
version, kernel S-expression version, interface version, artifact
version, signature domain, runtime behavior for existing programs,
BEAM representation, manifest field, public API name, or diagnostic
family, and amends no retained revision — Int-only programs are
unchanged (`NR-OBL-001`, `NR-OBL-006`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.40`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.41`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[numeric-relationships synthesis](../../20-notes/catena-numeric-relationships.md),
the [resolved inquiry](../../40-inquiries/how-should-int-and-float-relate-across-operators.md),
and the [topic map](../../10-maps/numeric-relationships.md). The [C061
evidence record](../../50-journal/2026-08-31-c061-numerics.md)
preserves the sibling-compiler commands and
archive validation.
