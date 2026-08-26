---
title: "Branching Diagnostics and Conformance"
kind: specification
created: "2026-08-25"
status: normative
spec_version: "0.1.29"
tags:
  - conformance
  - diagnostics
  - branching
  - specification
  - testing
aliases:
  - "Catena 0.1.29 branching conformance"
---

# Branching Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.29 branching diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Branch Form and Its Desugaring](the-branch-form-and-its-desugaring.md)
and [Branch Rules Consolidated](branch-rules-consolidated.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`BR-OBL-001`,
`BR-OBL-008`). Every branch failure already has a stable home: a
non-exhaustive match is C002's `M001` with its witness; redundancy is
C002's coverage rejection; condition violations are C003's families;
nothing new becomes invalid here. Every existing family keeps its
identity and meaning unchanged.

## Abstract public boundaries

Three shipped boundaries witness the contract; the bootstrap adds no
new public API (`BR-OBL-001`):

- **Reference evaluator** — Boolean-pattern dispatch, fallthrough
  selection, and commitment, agreeing with compiled BEAM.
- **Kernel stepper** — the definitional commitment dynamics for the
  S-expression calculus.
- **Coverage checking** — `M001` and redundancy rejection unchanged,
  on the C002 calculus.

Implementations MUST NOT use these boundaries to claim a
non-desugaring conditional, a statement tier, or any excluded
machinery (`BR-OBL-008`).

## Determinism

Equal matches select equal bodies with equal traces on every target;
witnesses are order- and tool-independent (`BR-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `BR-OBL-001` | apply branching behavior only at exact 0.1.29 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `BR-OBL-002` | keep match the single branch form with no other form existing on any retained input | form-absence tests |
| `BR-OBL-003` | fix the conditional sugar promise: Bool-pattern match desugaring, `true`/`false` exhaustive dispatch | conditional witness tests |
| `BR-OBL-004` | keep every consolidated rule exactly as its citing area fixed it | cited-rule regression tests |
| `BR-OBL-005` | keep statement-like control forms absent, sequenced through the let idiom, gated behind edition records | absence and idiom tests |
| `BR-OBL-006` | preserve commitment irreversibility: only the selected body's effects are observable | commitment trace tests |
| `BR-OBL-007` | preserve condition fallthrough: a false condition continues with later clauses | fallthrough witness tests |
| `BR-OBL-008` | keep the contract deterministic and outside P034/G036/G040/P109/G088 claims with zero new diagnostic families | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `BR-OBL-*` set against unknown and
uncovered identifiers before C033 conformance is claimed.

## Required evidence sets

Positive evidence includes a `Bool`-pattern match dispatching `true`
and `false` with evaluator/BEAM trace agreement; fallthrough proven by
which body's effects appear — a first clause whose condition is false
after structural success, a second clause taken; scrutinee effects
preceding clause effects; branch typing agreeing across targets
(bodies unifying with the match's type); and commitment irreversibility
(only the chosen body's request appears).

Negative evidence — in the definitional sense — includes a
non-exhaustive match rejecting as `M001` with a witness (C002
unchanged), a redundant clause rejecting per the coverage calculus,
and no new family appearing for any branch shape.

Exclusion evidence demonstrates no conditional entry point beyond
match, no statement or control entry points, unchanged C002/C003
diagnostic identities, and predecessor APIs retaining their exact
selections and defaults.

## Revision and persistence separation

Revision `0.1.29` adds the branch-form statement, the sugar promise,
the consolidated table, and the statement-form absence; it adds no
JSON AST version, kernel S-expression version, interface version,
artifact version, signature domain, typing rule, runtime behavior,
BEAM representation, manifest field, public API name, or diagnostic
family, and amends no retained revision (`BR-OBL-001`, `BR-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.29`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.30`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[branching synthesis](../../20-notes/catena-branching.md), the
[resolved inquiry](../../40-inquiries/what-is-catenas-branching-model.md),
and the [topic map](../../10-maps/branching.md). The C033 evidence
record will preserve the sibling-compiler commands and archive
validation.
