---
title: "Collection Construction and Update Diagnostics and Conformance"
kind: specification
created: "2026-08-31"
status: normative
spec_version: "0.1.37"
tags:
  - conformance
  - diagnostics
  - collections
  - specification
  - testing
aliases:
  - "Catena 0.1.37 collections conformance"
---

# Collection Construction and Update Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.37 collections diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Six-Topic Decision](the-six-topic-decision.md) and
[Miss as Value and Complexity](miss-as-value-and-complexity.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`CO-OBL-001`,
`CO-OBL-008`). Construction is constructor application; recursion
and matching diagnostics are the shipped families; a non-comparable
key type is C035's `EQN001`; no new invalid input exists.

## Abstract public boundaries

Two shipped boundaries witness the contract; the bootstrap adds no
new public API (`CO-OBL-001`):

- **Reference evaluator and compiled BEAM (JSON-AST path)** — a
  declared nominal List exercised end-to-end: construction via
  constructors, head/tail via match, length by recursion, and a
  replace-head update, agreeing on both targets by returned values.
- **Value classification** — declared collections are values; their
  elements and keys compare under C035's structural recursion; the
  miss witness returns an Option-typed value, never a trap.

Implementations MUST NOT use these boundaries to claim collection
built-ins, dedicated update operators, complexity conformance, or
trapping lookups (`CO-OBL-008`).

## Determinism

Equal declarations, collections, and operations produce equal
values, traces, and miss answers on every target (`CO-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `CO-OBL-001` | apply collection behavior only at exact 0.1.37 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `CO-OBL-002` | fix the six-topic decision with shipped machinery and named owners | decision-shape tests |
| `CO-OBL-003` | keep construction and update as constructor application and match recursion, distinct from records | declared-List operation tests |
| `CO-OBL-004` | classify a lookup miss as typed failure as a value: total operations, never a trap | miss-as-value witness tests |
| `CO-OBL-005` | exclude complexity from the language layer, delegating documentation to G101 | absence tests |
| `CO-OBL-006` | fix duplicate-key behavior as a G101 declaration obligation, explicit in the declaring slice | classification tests |
| `CO-OBL-007` | ride C035 for ordering and key equality: keys must be comparable | key-equality witness tests |
| `CO-OBL-008` | keep the contract deterministic and outside G101/G105/P109 claims with zero new families | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `CO-OBL-*` set against unknown and
uncovered identifiers before C042 conformance is claimed.

## Required evidence sets

Positive evidence includes a nominal List declared in the JSON AST
and exercised — construction, head/tail match, length by recursion,
replace-head update — agreeing on evaluator and BEAM; a key-equality
witness (a Pair-keyed ADT with comparable Int keys inserting and
looking up); and a lookup miss returning an Option-typed value whose
terminal outcome is that value.

Negative evidence — in the definitional sense — includes no
collection built-in, update-operator, or complexity entry points;
no trapping lookup path; and no new family appearing.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities, records and collections remaining distinct, and
predecessor APIs retaining their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.37` adds the six-topic decision, the miss
classification, and the complexity exclusion; it adds no JSON AST
version, kernel S-expression version, interface version, artifact
version, signature domain, typing rule, runtime behavior, BEAM
representation, manifest field, public API name, or diagnostic
family, and amends no retained revision (`CO-OBL-001`, `CO-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.37`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.38`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[collections synthesis](../../20-notes/catena-collection-operations.md),
the [resolved inquiry](../../40-inquiries/how-do-collections-construct-and-update.md),
and the [topic map](../../10-maps/collection-construction-and-update.md).
The [C042 evidence record](../../50-journal/2026-08-31-c042-collections.md)
preserves the sibling-compiler commands
and archive validation.
