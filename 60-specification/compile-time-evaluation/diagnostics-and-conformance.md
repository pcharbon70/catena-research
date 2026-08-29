---
title: "Compile-Time Evaluation Diagnostics and Conformance"
kind: specification
created: "2026-08-26"
status: normative
spec_version: "0.1.34"
tags:
  - conformance
  - diagnostics
  - compile-time-evaluation
  - specification
  - testing
aliases:
  - "Catena 0.1.34 compile-time conformance"
---

# Compile-Time Evaluation Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.34 compile-time diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Compile-Time Stance](the-compile-time-stance.md) and
[Totality and Determinism Restrictions](totality-and-determinism-restrictions.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`CE-OBL-001`,
`CE-OBL-008`). The stance accepts nothing new and rejects nothing
existing; the cited budgets keep their owning areas' families
(`CND007`, `EVD003`, the law verdicts). Nothing new becomes invalid
here.

## Abstract public boundaries

Three shipped boundaries witness the contract; the bootstrap adds no
new public API (`CE-OBL-001`):

- **Derivation engine** — `Catena.Derive` emits folds and
  capabilities with `compiler_derived` provenance and the generated
  marker; recompilation of equal declarations yields byte-identical
  binaries.
- **The three meta-evaluators** — condition normalization, the
  specification checker, and law checking, each under its cited
  budget, unchanged.
- **The compiler pipeline** — checking plus generation only: no
  const-eval, macro, or attribute evaluation stage exists anywhere
  in the public surface.

Implementations MUST NOT use these boundaries to claim an unbounded
evaluator, a macro expander, or any excluded machinery (`CE-OBL-008`).

## Determinism

Equal compilations produce equal derived definitions, verdicts, and
bytes on every target (`CE-OBL-008`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `CE-OBL-001` | apply compile-time behavior only at exact 0.1.34 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `CE-OBL-002` | fix the four-form decision: constants never execute; attributes and macros absent; derivations are generation | stance-shape tests |
| `CE-OBL-003` | keep the gate inherited: no evaluator arrives total-or-bounded-free; none is claimed | absence tests |
| `CE-OBL-004` | keep derivations compiler-internal: no user code evaluated, provenance marked, output checked | derivation provenance tests |
| `CE-OBL-005` | keep the restriction table exact: the gate plus the three cited budgets, complete at 0.1.34 | budget regression tests |
| `CE-OBL-006` | keep compilation deterministic: equal declarations, equal derived output, equal bytes | byte-identity tests |
| `CE-OBL-007` | keep the three meta-evaluators under their unchanged regimes | regime regression tests |
| `CE-OBL-008` | keep the classification deterministic and outside P109/G040/G005/G116/G121 claims with zero new families | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `CE-OBL-*` set against unknown and
uncovered identifiers before C038 conformance is claimed.

## Required evidence sets

Positive evidence includes a datatype with `fold` and capability
derivations compiling with `compiler_derived` provenance and the
generated marker on its derived definitions; recompilation yielding
byte-identical binaries; and the derived definition flowing through
checking and verification like any definition.

Negative evidence — in the definitional sense — includes no
const-eval, macro-expander, or attribute-evaluation entry points
anywhere in the public surface; no evaluator stage in the pipeline;
and no new family appearing.

Exclusion evidence demonstrates the three cited budgets unchanged
(the condition normalization budget rejection, the configured
specification-example limit, the bounded-law shapes), unchanged
predecessor diagnostic identities, and predecessor APIs retaining
their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.34` adds the stance, the classification, and the
restriction table; it adds no JSON AST version, kernel S-expression
version, interface version, artifact version, signature domain,
typing rule, runtime behavior, BEAM representation, manifest field,
public API name, or diagnostic family, and amends no retained
revision (`CE-OBL-001`, `CE-OBL-008`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.34`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.35`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[compile-time synthesis](../../20-notes/catena-compile-time-evaluation.md),
the [resolved inquiry](../../40-inquiries/what-executes-during-compilation.md),
and the [topic map](../../10-maps/compile-time-evaluation.md). The
C038 evidence record will preserve the sibling-compiler commands and
archive validation.
