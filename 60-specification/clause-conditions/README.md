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

These normative chapters define Catena 0.3 clause conditions: their surface
placement, safe expression language, reusable predicates, ordered selection,
coverage facts, module evidence, BEAM lowering, and restricted receive use.

## What belongs here

Keep rules that connect a successful structural pattern to conditional clause
selection here. General effects, unrestricted recursion, trait-defined
operators, public process protocols, receive timeouts, pattern guards, handler
guards, and programmable patterns remain in their own specification areas.

Every chapter is `normative`. Published compiler commit
[`165fc4837f101d01016248e62479ef4caa0f20ce`](https://github.com/pcharbon70/catena/commit/165fc4837f101d01016248e62479ef4caa0f20ce)
provides the executable promotion evidence, and checklist item C003 records the
completed specification slice.

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
published 0.3 implementation at commit
[`165fc4837f101d01016248e62479ef4caa0f20ce`](https://github.com/pcharbon70/catena/commit/165fc4837f101d01016248e62479ef4caa0f20ce),
merged through [compiler PR #65](https://github.com/pcharbon70/catena/pull/65).
The reproducible commands and observed test count are recorded in
[C003 Executable Clause Condition Conformance](../../50-journal/2026-08-02-c003-executable-clause-condition-conformance.md).

## Maintaining this index

Version these chapters together. A future lifecycle change must update the
compiler evidence, C003 checklist entry, journal, conformance chapter, maps,
and affected cross-version rules atomically.
