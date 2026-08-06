---
title: "Clause Condition Specification"
kind: map
created: "2026-08-02"
tags:
  - archive-navigation
  - directory-index
  - pattern-matching
  - specification
aliases:
  - "Catena clause condition specification index"
---

# Clause Condition Specification (`60-specification/clause-conditions`)

## Purpose

These normative chapters define Catena 0.1.3 clause conditions: their surface
placement, safe expression language, reusable predicates, ordered selection,
coverage facts, module evidence, BEAM lowering, and restricted receive use.

## What belongs here

Keep rules that connect a successful structural pattern to conditional clause
selection here. General effects, unrestricted recursion, trait-defined
operators, public process protocols, receive timeouts, pattern guards, handler
guards, and programmable patterns remain in their own specification areas.

Document authority and rendered content labels follow the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md).
Requirement words, behavior classes, permitted variation, limits, and profile
disclosure follow the repository
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md).

Every chapter is `normative`. Published compiler commit
[`165fc4837f101d01016248e62479ef4caa0f20ce`](https://github.com/pcharbon70/catena/commit/165fc4837f101d01016248e62479ef4caa0f20ce)
provides historical semantic evidence under the retired `0.1` through `0.3`
protocol identifiers, and checklist item C003 records the completed semantic
slice. It is not evidence for the exact renumbered wire identities. The hard
cutover and fresh cross-slice evidence requirement are recorded in
[Prototype Slice Renumbering](../../50-journal/2026-08-04-prototype-slice-renumbering.md).

## Variability register

| Governing rule | Classification and bound |
| --- | --- |
| [Guard Tree Semantics — Guard-tree core](guard-tree-semantics.md#guard-tree-core) | Structural tests and continuations can be shared only when selection order, multiplicity, bindings, values, and effects remain identical. |
| [BEAM Lowering — Ordinary lowering](beam-lowering.md#ordinary-lowering) | `auto`, `native`, and `ordinary` are explicit lowering selections, not unreported implementation variation; all applicable paths preserve the same typed observations. |
| [Diagnostics and Conformance — Stable diagnostics](diagnostics-and-conformance.md#stable-diagnostics) | Task-facing “clause condition” wording is a `SHOULD` diagnostic-quality recommendation. The current compiler deviation is disclosed and tracked by P117. |
| [Condition Predicates and Interfaces — Budget](condition-predicates-and-interfaces.md#budget) | Normalization and transitive inlining support at least 20,000 nodes and report `CND007` as an implementation limit. |
| [Coverage and Fact Evidence — Budgets and diagnostics](coverage-and-fact-evidence.md#budgets-and-diagnostics) | Structural analysis inherits the 20,000-step `M004` minimum; fact-analysis exhaustion is an implementation limit or conservative unknown, never a semantic proof. |

## Index

### Subdirectories

- None yet.

### Documents

- [Clause Condition Overview](clause-condition-overview.md) — authority,
  guarantees, profiles, implementation boundary, and exclusions.
- [Syntax and Safety](syntax-and-safety.md) — clause syntax, the exact initial
  operation set, typing, evaluation order, and rejected forms.
- [Condition Predicates and Interfaces](condition-predicates-and-interfaces.md)
  — reusable declarations, acyclic dependencies, explicit imports, normalized
  interface bodies, and evidence digests.
- [Guard Tree Semantics](guard-tree-semantics.md) — structural success,
  one-time condition evaluation, fallthrough, commitment, and or-pattern
  sharing.
- [Coverage and Fact Evidence](coverage-and-fact-evidence.md) — structural
  usefulness, the integer difference-constraint theory, conservative unknowns,
  redundancy, exhaustiveness, budgets, and rechecking.
- [Clause Contexts and Receive](clause-contexts-and-receive.md) — ordinary
  matches, multi-clause functions, the typed selective-receive harness, and
  context-specific terminal behavior.
- [BEAM Lowering](beam-lowering.md) — native and ordinary lowering, OTP 29
  Abstract Format, imported predicate inlining, and erased analysis evidence.
- [Clause Condition Diagnostics and Conformance](diagnostics-and-conformance.md)
  — stable diagnostic IDs, required positive and negative cases, differential
  tests, and promotion requirements.
- [Clause Condition Metatheory](metatheory.md) — judgments, semantic claims,
  evidence status, and falsification criteria.

## Executable evidence

The sibling [Catena compiler](https://github.com/pcharbon70/catena) contains the
historical C003 implementation at commit
[`165fc4837f101d01016248e62479ef4caa0f20ce`](https://github.com/pcharbon70/catena/commit/165fc4837f101d01016248e62479ef4caa0f20ce),
merged through [compiler PR #65](https://github.com/pcharbon70/catena/pull/65).
That commit used the retired `0.3` identifier. The reproducible commands and
observed test count are recorded in
[C003 Executable Clause Condition Conformance](../../50-journal/2026-08-02-c003-executable-clause-condition-conformance.md).

## Maintaining this index

Version these chapters together. A future lifecycle change must update the
compiler evidence, C003 checklist entry, journal, conformance chapter, maps,
and affected cross-version rules atomically.
