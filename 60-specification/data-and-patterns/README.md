---
title: "Data and Pattern Specification"
kind: map
created: "2026-08-02"
tags:
  - algebraic-data-types
  - archive-navigation
  - directory-index
  - pattern-matching
  - specification
aliases:
  - "Catena data and pattern specification index"
---

# Data and Pattern Specification (`60-specification/data-and-patterns`)

## Purpose

These chapters define Catena 0.2 nominal algebraic data, construction,
patterns, matching, coverage, GADT refinement, module interfaces, BEAM
representation independence, and the initial generated fold.

The normative [Clause Condition Specification](../clause-conditions/README.md)
refines 0.2's conservative nonliteral-guard boundary without changing its
structural rules.

## What belongs here

Keep normative rules that connect datatype declarations to static typing,
ordered elimination, abstraction, separate compilation, and verified backend
lowering here. Structural row variants, programmable patterns, collection
syntax, stable foreign layouts, and categorical instance generation remain in
their own specification areas.

## Index

### Subdirectories

- None yet.

### Documents

- [Data and Pattern Overview](data-and-pattern-overview.md) — authority,
  profiles, guarantees, exclusions, and the C002 boundary.
- [Declarations and Nominal Identity](declarations-and-nominal-identity.md) —
  declaration grammar, recursive groups, constructor schemes, visibility,
  and names.
- [Construction and Pattern Typing](construction-and-pattern-typing.md) —
  construction order, the complete 0.2 pattern grammar, binding rules, and
  typed-pattern elaboration.
- [Match Semantics and Coverage](match-semantics-and-coverage.md) — ordered
  evaluation, guards, usefulness, inhabitedness, witnesses, redundancy, and
  deterministic limits.
- [GADT and Existential Patterns](gadt-and-existential-patterns.md) — refined
  results, required signatures, local equality evidence, and rigid scope.
- [Interfaces and Representation](interfaces-and-representation.md) — nominal
  module interfaces, constructor abstraction, integrity, and uniform versus
  compact BEAM layouts.
- [Derived Folds](derived-folds.md) — the one explicit compiler-generated
  eliminator, its signature, order, eligibility, and provenance.
- [Diagnostics and Conformance](diagnostics-and-conformance.md) — stable
  diagnostic families, required cases, differential testing, and promotion
  evidence.
- [Data and Pattern Metatheory](metatheory.md) — the formal judgments and
  current status of generativity, preservation, progress, usefulness, GADT
  scope, and representation independence.

## Executable evidence

The sibling [Catena compiler](https://github.com/pcharbon70/catena) implements
the 0.2 JSON-AST slice in Elixir on Erlang/OTP 29. It elaborates to verified
typed core and delegates `.beam` generation exclusively to
`compile:noenv_forms/2`. Reproduction commands and observed limits are in
[C002 Executable Data and Pattern Conformance](../../50-journal/2026-08-02-c002-executable-data-and-pattern-conformance.md).

## Maintaining this index

Version these chapters together. A semantic change requires corresponding
positive and negative conformance cases, updated typed-core verification, and
an explicit interface and representation-compatibility decision.
