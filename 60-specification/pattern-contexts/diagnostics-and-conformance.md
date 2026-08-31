---
title: "Pattern Contexts Diagnostics and Conformance"
kind: specification
created: "2026-08-31"
status: normative
spec_version: "0.1.38"
tags:
  - conformance
  - diagnostics
  - patterns
  - specification
  - testing
aliases:
  - "Catena 0.1.38 pattern contexts conformance"
---

# Pattern Contexts Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.38 pattern-contexts
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Three Context Classes](the-three-context-classes.md) and
[Context Rules and Reservations](context-rules-and-reservations.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`PC-OBL-001`,
`PC-OBL-003`). Match keeps `M001`/`M002`; unsupported pattern forms
keep `M005`; malformed binders keep the structural diagnostics of
their owning frontends. No accepted 0.1.37 program changes meaning.

## Abstract public boundaries

The shipped boundaries witness the contract; the bootstrap adds no
new public API (`PC-OBL-001`):

- **Kernel S-expression boundary** — a `let` whose binder is not a
  plain value name rejects, and no parameter-position pattern form
  exists; match programs elaborate, check, and run unchanged.
- **JSON-AST boundary** — `let` keeps its name binder; definitions
  keep plain parameters; no view, synonym, active, or
  pattern-binding tag exists.

Implementations MUST NOT use these boundaries to claim pattern
`let`, parameter patterns, generator grammar, public receive
grammar, exception clauses, or any programmable pattern form
(`PC-OBL-003`).

## Determinism

Unchanged programs produce identical values, traces, and
diagnostics on every conforming target (`PC-OBL-003`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `PC-OBL-001` | apply pattern-context rules only at exact 0.1.38 and register the stable lifecycle addition with zero new families | exact selection, registry, and lifecycle tests |
| `PC-OBL-002` | fix the three context classes with exactly one exhaustive context | classification-shape tests |
| `PC-OBL-003` | keep match's C045 authority and the no-implicit-runtime-match property with unchanged diagnostics | regression-pin tests |
| `PC-OBL-004` | keep `let` and parameters plain-named today with the irrefutable-only default reserved for arrivals | negative boundary tests |
| `PC-OBL-005` | fix the generator principle: ordinary total, filtering explicitly mismatch-as-skip, grammar deferred | classification tests |
| `PC-OBL-006` | reserve public receives as exhaustive-or-explicit-fallback in their own slice | absence tests |
| `PC-OBL-007` | keep handler clauses on plain binders with irrefutable-only arrival | absence tests |
| `PC-OBL-008` | exclude exception clauses under C036's terminal trap taxonomy | absence tests |
| `PC-OBL-009` | exclude programmable patterns with recorded arrival conditions | absence tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `PC-OBL-*` set against unknown and
uncovered identifiers before C044 conformance is claimed.

## Required evidence sets

Positive evidence includes a match program agreeing on the
reference evaluator and compiled BEAM with 0.1.37 semantics
unchanged, and the lifecycle registration of 0.1.38.

Negative evidence — in the definitional sense — includes a
pattern-position `let` binder and a parameter-position pattern
rejecting at the kernel and JSON-AST boundaries, and no entry
points for generator grammar, public receives, exception clauses,
or programmable pattern forms.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities (`M001`, `M002`, `M005`, structural binder diagnostics)
and predecessor APIs retaining their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.38` adds the classification, the per-context rules
and reservations, and the D046 exclusion; it adds no JSON AST
version, kernel S-expression version, interface version, artifact
version, signature domain, typing rule, runtime behavior, BEAM
representation, manifest field, public API name, or diagnostic
family, and amends no retained revision (`PC-OBL-001`, `PC-OBL-003`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.38`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.39`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[pattern-contexts synthesis](../../20-notes/catena-pattern-contexts.md),
the [resolved inquiry](../../40-inquiries/which-pattern-contexts-admit-refutable-patterns.md),
and the [topic map](../../10-maps/pattern-contexts.md). The C044
evidence record will preserve the sibling-compiler commands and
archive validation.
