---
title: "Bindings and Sequencing Diagnostics and Conformance"
kind: specification
created: "2026-08-25"
status: candidate
spec_version: "0.1.27"
tags:
  - conformance
  - diagnostics
  - bindings
  - specification
  - testing
aliases:
  - "Catena 0.1.27 bindings conformance"
---

# Bindings and Sequencing Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.27 bindings diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Binding Structure and Scope](binding-structure-and-scope.md)
and [Unused Bindings and Sequencing](unused-bindings-and-sequencing.md).

## Stable diagnostics

This area introduces one warning family (`BS-OBL-001`, `BS-OBL-006`):

| ID | Severity | Required meaning |
| --- | --- | --- |
| `BS001` | warning | a non-`_`-prefixed binder never occurs in its binding's body |

`BS001` is deny-able through the manifest's `diagnostics.deny` list
exactly as `IMP001` is: denial promotes the warning to an error with
`promoted_from_warning`. All existing diagnostic families keep their
identities and meanings unchanged; the unbound-name rejection that
proves non-recursion remains `T001`.

## Abstract public boundaries

Three shipped boundaries witness the contract; the bootstrap adds the
warning walk (`BS-OBL-001`):

- **Check pipeline** — after inference and before verification, a
  let-tree walk collects binder usage per definition and emits `BS001`
  for each non-`_`-prefixed unused binder with its binding path; the
  existing `enforce_diagnostics` machinery performs deny promotion.
- **Reference and kernel machines** — the evaluator and stepper agree
  with compiled BEAM on values and effect traces for scope, shadowing,
  unused-preserves-effects, sequencing-idiom, and recursion-home
  programs (the C030 dual-agreement pattern, with the stepper as the
  third witness for kernel inputs).

Implementations MUST NOT use these boundaries to claim local recursive
forms, pattern binding, tail-call guarantees, or any excluded
machinery (`BS-OBL-008`).

## Determinism

Equal programs produce equal warnings, values, and traces; the warning
walk is order- and tool-independent (`BS-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `BS-OBL-001` | apply bindings behavior only at exact 0.1.27 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `BS-OBL-002` | keep local bindings strictly non-recursive: an RHS referencing its own binder is `T001` unbound | non-recursion rejection tests |
| `BS-OBL-003` | enforce sequential-lexical scope with silent innermost-wins shadowing of any in-scope name | shadowing witness tests |
| `BS-OBL-004` | keep recursion definitions-only with C024's SCC as mutual recursion's home | recursion-home and SCC witness tests |
| `BS-OBL-005` | keep unused bindings valid with RHS effects preserved on every target | unused-effects trace tests |
| `BS-OBL-006` | emit `BS001` exactly on non-`_`-prefixed unused binders with deny promotion | warning-matrix and deny tests |
| `BS-OBL-007` | fix the let idiom as sequencing: first to a value with effects, discard, then second | sequencing trace tests |
| `BS-OBL-008` | keep the contract deterministic and outside G032/G033/P034/P109 claims | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `BS-OBL-*` set against unknown and
uncovered identifiers before C031 conformance is claimed.

## Required evidence sets

Positive evidence includes scope and shadowing programs (inner shadows
outer, definition, and import silently) agreeing on values and traces
across evaluator and BEAM; unused-binding programs whose RHS performs
requests with those requests present in every trace; the sequencing
idiom ordering `e1`'s effects before `e2`'s; `BS001` firing on a
genuinely unused binder, silent on used and `_`-prefixed binders, and
denied to error through the manifest; a named recursive definition
running; and an SCC pair mutually recursing.

Negative evidence includes the self-referential let RHS rejecting as
`T001`; `BS001` absent when the binder occurs; and no new family
appearing for shadowing (it stays silent).

Exclusion evidence demonstrates no local recursive form, no pattern
binding, no tail-call claim, unchanged predecessor diagnostics, and
predecessor APIs retaining their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.27` adds the elevated binding account and the `BS001`
warning; it adds no JSON AST version, kernel S-expression version,
interface version, artifact version, signature domain, typing rule,
runtime behavior, BEAM representation, or manifest field (the deny
list already exists), and amends no retained revision (`BS-OBL-001`,
`BS-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.27`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.28`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[bindings synthesis](../../20-notes/catena-bindings-and-sequencing.md),
the [resolved inquiry](../../40-inquiries/how-should-catena-define-bindings-and-sequencing.md),
and the [topic map](../../10-maps/bindings-and-sequencing.md). The
C031 evidence record will preserve the sibling-compiler commands and
archive validation.
