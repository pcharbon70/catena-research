---
title: "Namespace Diagnostics and Conformance"
kind: specification
created: "2026-08-22"
status: candidate
spec_version: "0.1.17"
tags:
  - conformance
  - diagnostics
  - namespaces
  - specification
  - testing
aliases:
  - "Catena 0.1.17 namespace conformance"
---

# Namespace Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.17 namespace diagnostic, abstract
frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Namespace Inventory and Spelling](namespace-inventory-and-spelling.md)
and [Shadowing and Ambiguity](shadowing-and-ambiguity.md).

## Stable diagnostics

| ID | Required meaning |
| --- | --- |
| `NSP001` | a duplicate declaration of one spelling in one category within one scope |
| `NSP002` | a declaration event's spelling violates its category's spelling class |
| `NSP003` | a reference has no binding and no import in scope in its category |
| `NSP004` | an unqualified reference is ambiguous across two or more import origins |
| `NSP005` | a qualified reference has more than two segments |

An exact-selection mismatch remains `EDN001`. Every namespace rejection
carries the stable diagnostic ID, the offending spelling, its category,
and — for ambiguity — every colliding origin (`NS-OBL-011`).

Invalid events produce no resolution environment and no successful
reference resolution for the affected action. Diagnostic prose can improve
only within the bounded presentation rules of the repository conformance
vocabulary; identity, severity, reason, acceptance, and repair meaning do
not vary.

## Abstract public boundaries

A conforming implementation exposes two operations.

**Scope construction** accepts an ordered scope-event stream — declare
(category, spelling, span), open declaration/quantifier/expression scope,
close scope, and import set (origin, category, exported spellings) — and
returns one resolution environment, or exactly one diagnostic
(`NS-OBL-012`).

**Reference resolution** accepts one resolution environment and one
reference (category, spelling or two-segment qualified spelling, span)
and returns the resolved nominal identity — category, spelling, origin
(local, module, or import origin), and binding scope — or exactly one
diagnostic (`NS-OBL-012`).

Neither operation parses source, tokenizes, checks types, evaluates, or
compiles; the concrete grammar that emits scope events remains P109's,
and implementations MUST NOT use these boundaries to claim those later
phases (`NS-OBL-014`).

The bootstrap evidence names these operations
`Catena.Namespace.build_environment/1` and `Catena.Namespace.resolve/2`,
and the records `Catena.Namespace.Environment` and
`Catena.Namespace.Resolution`. These Elixir names are evidence API names,
not required names for every implementation.

## Determinism

Equal scope-event streams produce equal environments or equal
diagnostics; equal environments and references produce equal resolutions
or equal diagnostics (`NS-OBL-013`). Resolution is insensitive to the
order of independent import origins.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `NS-OBL-001` | apply namespace behavior only at exact 0.1.17 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `NS-OBL-002` | enforce disjoint categories where one spelling resolves in at most its requested category | cross-category coexistence tests |
| `NS-OBL-003` | enforce the hard spelling-class partition with `NSP002` | class-violation matrix tests |
| `NS-OBL-004` | reject same-scope duplicates per uniqueness domain as `NSP001` | duplicate matrix tests across categories and domains |
| `NS-OBL-005` | keep governed identities out of program resolution and vice versa | separation tests |
| `NS-OBL-006` | resolve exactly two-segment qualification and reject deeper chains as `NSP005` | qualification depth tests |
| `NS-OBL-007` | resolve innermost-visible bindings with silent deterministic shadowing | nesting and cross-category shadowing tests |
| `NS-OBL-008` | scope type variables per quantifier with type/trait shadowing and value separation | quantifier tests |
| `NS-OBL-009` | enforce local-over-imported precedence and order-independent `NSP004` ambiguity rejection | precedence, collision, and origin-order tests |
| `NS-OBL-010` | reject unbound references as `NSP003` | unbound tests per category |
| `NS-OBL-011` | emit stable diagnostics with spelling, category, and all colliding origins | every diagnostic family test |
| `NS-OBL-012` | expose the environment-building and reference-resolution boundaries as tree-or-diagnostic operations | boundary shape and no-partial-output tests |
| `NS-OBL-013` | produce deterministic environments and resolutions | repeated-result and origin-order tests |
| `NS-OBL-014` | preserve source-only and persisted-format separation and claim no later phase | registry, pinned-predecessor, forged-format, and absent-phase tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `NS-OBL-*` set against unknown and uncovered
identifiers before C021 conformance is claimed.

## Required evidence sets

Positive evidence includes same-spelling coexistence across categories;
nested scope shadowing in each direction; quantifier shadowing of types
and traits with restoration after the region; local-over-imported
precedence; two-segment qualification; and resolutions naming local,
module, and import origins.

Negative evidence includes duplicates in every category and domain;
spelling-class violations in both directions; unbound references in every
category; two-origin and three-origin ambiguities; origin-order
invariance of ambiguity; and three-segment chains.

Exclusion evidence demonstrates that neither boundary parses source,
tokenizes, type-checks, evaluates, or emits interfaces or BEAM, and that
predecessor APIs retain their exact 0.1.10 through 0.1.16 selections and
defaults.

## Revision and persistence separation

Revision `0.1.17` is a compatible static-meaning and diagnostic addition.
It adds no JSON AST version, kernel S-expression version, interface
version, artifact version, signature domain, typing rule, runtime
behavior, or BEAM representation (`NS-OBL-001`, `NS-OBL-014`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.17`. Standalone identifier, layout, comment, literal, numeric,
tokenization, operator-expression, and file-unit APIs retain their exact
0.1.10 through 0.1.16 selections and defaults. Namespace environment
construction requires exact `0.1.17`. The next unused semantic patch is
`0.1.18`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[namespaces synthesis](../../20-notes/catena-namespaces-and-shadowing.md),
the [open inquiry](../../40-inquiries/how-should-catena-organize-namespaces-and-shadowing.md),
and the [topic map](../../10-maps/namespaces-and-shadowing.md). The C021
evidence record will preserve the sibling-compiler commands and archive
validation.
