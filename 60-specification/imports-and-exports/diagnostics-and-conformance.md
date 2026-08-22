---
title: "Import Diagnostics and Conformance"
kind: specification
created: "2026-08-22"
status: normative
spec_version: "0.1.18"
tags:
  - conformance
  - diagnostics
  - imports
  - specification
  - testing
aliases:
  - "Catena 0.1.18 import conformance"
---

# Import Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.18 import/export diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Export Declarations and Visibility](export-declarations-and-visibility.md)
and [Import Declarations and Admission](import-declarations-and-admission.md).

## Stable diagnostics

| ID | Class | Required meaning |
| --- | --- | --- |
| `IMP001` | warning | an admitted unqualified name never referenced in its category, or an imported module with no qualified or unqualified use |
| `IMP002` | error | a listed import name is absent from the module's exported set |
| `IMP003` | error | an imported module is not known to the resolution context |
| `EXP001` | error | an export declaration names a name the module does not declare in that category |

Duplicate imports and exports reuse C021 `NSP001`; qualification against
an unadmitted module is C021 `NSP003`; import collisions are C021
`NSP004`. An exact-selection mismatch remains `EDN001`
(`IM-OBL-009`).

`IMP001` is deny-able through the C008 warning machinery and MUST NOT
affect acceptance, resolution, or any successful output
(`IM-OBL-010`). Error diagnostics carry the offending spelling,
category, and module. Invalid events produce no environment for the
affected action; diagnostic prose can improve only within the bounded
presentation rules of the repository conformance vocabulary.

## Abstract public boundaries

A conforming implementation extends the C021 environment builder to
consume export and import events alongside declaration and scope events,
validating them against known export sets, and exposes one additional
operation (`IM-OBL-011`):

**Unused-import analysis** accepts the built environment and the set of
referenced identities — each a (category, spelling, qualified-module)
triple — and returns zero or more `IMP001` warnings and nothing else:
never errors, never resolutions.

Neither operation parses source, tokenizes, checks types, evaluates, or
compiles; the concrete `use`/`export` grammar remains P109's, and
implementations MUST NOT use these boundaries to claim those later
phases (`IM-OBL-013`).

The bootstrap evidence names these operations
`Catena.build_namespace_environment/2` (extended event grammar),
`Catena.Namespace.check_unused_imports/2`, and the record
`Catena.Namespace.ImportWarning`. These Elixir names are evidence API
names, not required names for every implementation.

## Determinism

Equal scope, export, and import events and equal known export sets
produce equal environments or equal diagnostics; equal environments and
reference sets produce equal warning lists in a stable order
(`IM-OBL-012`). Warning order follows import-event order then name-list
order.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `IM-OBL-001` | apply import/export behavior only at exact 0.1.18 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `IM-OBL-002` | export nothing without an explicit export declaration; private names never resolve elsewhere | private-by-default and leak tests |
| `IM-OBL-003` | enforce export events with categories, spelling classes, and type transparency modes | export event matrix and abstract-constructor tests |
| `IM-OBL-004` | reject exports of undeclared names as `EXP001` | undeclared export tests |
| `IM-OBL-005` | enforce two-effect admission: qualification against the export set plus listed unqualified admission with the empty qualified-only form | admission and empty-list tests |
| `IM-OBL-006` | reject unexported listed names as `IMP002` and unknown modules as `IMP003` | validation tests |
| `IM-OBL-007` | admit no wildcard, hiding, renaming, alias, or re-export form | exclusion tests |
| `IM-OBL-008` | feed imported names into C021 precedence and reference-time `NSP004` unchanged | precedence and collision interaction tests |
| `IM-OBL-009` | emit stable import/export diagnostics with spelling, category, and module | every diagnostic family test |
| `IM-OBL-010` | keep `IMP001` a deny-able warning that never affects acceptance | warning-only and denial tests |
| `IM-OBL-011` | expose the unused-import analysis returning warnings only | analysis-shape tests |
| `IM-OBL-012` | produce deterministic environments, diagnostics, and warning order | repeated-result and order tests |
| `IM-OBL-013` | preserve source-only and persisted-format separation and claim no later phase | registry, pinned-predecessor, forged-format, and absent-phase tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `IM-OBL-*` set against unknown and uncovered
identifiers before C022 conformance is claimed.

## Required evidence sets

Positive evidence includes exports in every category; transparent and
abstract type exports; qualified resolution through admitted modules;
listed unqualified admission; empty-list qualified-only imports;
cumulative multi-imports; unused-import warnings for unused names and
wholly unused modules with stable order; and denial of `IMP001`.

Negative evidence includes exports of undeclared names; imports of
unexported names and unknown modules; duplicate imports reusing
`NSP001`; unadmitted qualification as `NSP003`; and collision references
as `NSP004`.

Exclusion evidence demonstrates that no wildcard, hiding, renaming,
alias, or re-export event shape is accepted, that the analysis never
errors, and that predecessor APIs retain their exact 0.1.10 through
0.1.17 selections and defaults.

## Revision and persistence separation

Revision `0.1.18` is a compatible static-meaning and diagnostic addition.
It adds no JSON AST version, kernel S-expression version, interface
version, artifact version, signature domain, typing rule, runtime
behavior, or BEAM representation (`IM-OBL-001`, `IM-OBL-013`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.18`. Standalone identifier through file-unit APIs retain their
exact 0.1.10 through 0.1.16 selections and defaults; namespace
environment construction requires exact `0.1.17` with the extended
import/export event grammar accepted at exact `0.1.18`. The next unused
semantic patch is `0.1.19`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[imports synthesis](../../20-notes/catena-imports-and-exports.md), the
[resolved inquiry](../../40-inquiries/how-should-catena-handle-imports-and-exports.md),
and the [topic map](../../10-maps/imports-and-exports.md). The C022
evidence record will preserve the sibling-compiler commands and archive
validation.
