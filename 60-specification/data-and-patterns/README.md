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

These chapters define Catena 0.1.2 nominal algebraic data, construction,
patterns, matching, coverage, GADT refinement, module interfaces, BEAM
representation independence, and the initial generated fold.

The normative [Clause Condition Specification](../clause-conditions/README.md)
refines 0.1.2's conservative nonliteral-guard boundary without changing its
structural rules.

## What belongs here

Keep normative rules that connect datatype declarations to static typing,
ordered elimination, abstraction, separate compilation, and verified backend
lowering here. Structural row variants, programmable patterns, collection
syntax, stable foreign layouts, and categorical instance generation remain in
their own specification areas.

Document authority and rendered content labels follow the repository
[Specification Authority](../../SPECIFICATION-AUTHORITY.md).
Requirement words, behavior classes, permitted variation, limits, and profile
disclosure follow the repository
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md).

Every chapter is `normative`. The historical C002 commit exercised these
semantics under retired `0.1` and `0.2` protocol identifiers. It remains
semantic evidence, but it is not evidence for the exact `0.1.1` and `0.1.2`
wire identities. The hard cutover and fresh cross-slice evidence requirement
are recorded in
[Prototype Slice Renumbering](../../50-journal/2026-08-04-prototype-slice-renumbering.md).

## Variability register

| Governing rule | Classification and bound |
| --- | --- |
| [GADT and Existential Patterns — Explicit advanced declarations](gadt-and-existential-patterns.md#explicit-advanced-declarations) | `MAY` permits an explicitly bound existential variable in constructor fields; the datatype result prohibition and rigid non-escape rules still apply. |
| [Construction and Pattern Typing — Construction](construction-and-pattern-typing.md#construction) | `MAY` permits source authors to write named fields in any order and permits a selected physical layout only while written evaluation order and declaration-order payload semantics remain fixed. |
| [Interfaces and Representation — Deterministic module interface](interfaces-and-representation.md#deterministic-module-interface) | Checking `MAY` consume interfaces but writes no artifact. The bootstrap profile records that interface consumption is enabled. |
| [Match Semantics and Coverage — Usefulness model](match-semantics-and-coverage.md#usefulness-model) | Shared pattern matrices are a `SHOULD` performance technique; usefulness results cannot vary. The current deviation is tracked by G138. |
| [GADT and Existential Patterns — Typed-core evidence](gadt-and-existential-patterns.md#typed-core-evidence) | GADT coverage `MAY` use local equalities to exclude impossible constructors, but coverage precision cannot justify an unsound branch. The bootstrap profile records that this path is enabled. |
| [Derived Folds — Generated evidence](derived-folds.md#generated-evidence) | Direct verified fold lowering is permitted when observations match both required layouts. The bootstrap instead uses the verified ordinary lowering path. |
| [Match Semantics and Coverage — Deterministic implementation limit](match-semantics-and-coverage.md#deterministic-implementation-limit) | Coverage supports at least 20,000 usefulness steps and reports `M004` on exhaustion; a limit cannot masquerade as non-exhaustiveness or redundancy. |

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
  construction order, the complete 0.1.2 pattern grammar, binding rules, and
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
the renumbered `0.1.2` JSON-AST slice in its current working tree. It
elaborates to verified typed core and delegates `.beam` generation exclusively
to `compile:noenv_forms/2`. Historical reproduction commands and observed
limits are in
[C002 Executable Data and Pattern Conformance](../../50-journal/2026-08-02-c002-executable-data-and-pattern-conformance.md).

## Maintaining this index

Version these chapters together. A semantic change requires corresponding
positive and negative conformance cases, updated typed-core verification, and
an explicit interface and representation-compatibility decision.
