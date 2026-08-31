---
title: "List Comprehensions Diagnostics and Conformance"
kind: specification
created: "2026-08-31"
status: candidate
spec_version: "0.1.39"
tags:
  - conformance
  - diagnostics
  - comprehensions
  - specification
  - testing
aliases:
  - "Catena 0.1.39 comprehension conformance"
---

# List Comprehensions Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.39 comprehension
diagnostic, abstract frontend, and conformance contract. It is
governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies the four preceding chapters.

## Stable diagnostics

This area introduces **three new diagnostic families**
(`LC-OBL-001`), with vocabulary that prefers task words over
category words:

| Family | Meaning |
| --- | --- |
| `LCP001` | a name is rebound in the same comprehension |
| `LCP002` | a filtering generator's pattern can never match |
| `LCP003` | a filtering marker is unnecessary: the pattern is already total |

Every other comprehension diagnostic reuses an existing family by
role (`LC-OBL-006`, `LC-OBL-007`): a non-total ordinary generator
pattern or refutable `let` binding is the non-exhaustive-match
family (`M001`); a non-list source or non-`Bool` filter is the
typing-error family; an unused binding is the `BS001` family.
Implementations MUST NOT add comprehension-specific duplicates of
reused families (`LC-OBL-014`).

## Abstract public boundaries

The shipped boundary is the dormant elaboration API
(`LC-OBL-001`): a qualifier tree elaborates to a kernel
S-expression module — with its fused worker — that checks, runs on
the reference stepper, and compiles to BEAM. This is the area's
one new public API surface. No frontend accepts comprehension
expressions; adoption is the surface-grammar capstone's.

Implementations MUST NOT use this boundary to claim surface
syntax, non-list sources, lazy production, parallel traversal, or
non-list targets (`LC-OBL-014`).

## Determinism

Equal qualifier trees and sources produce equal results, traces,
and failures on every conforming target (`LC-OBL-014`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `LC-OBL-001` | apply comprehension rules only at exact 0.1.39, register the lifecycle addition, and declare the `LCP` families and the elaboration API | exact selection, registry, and lifecycle tests |
| `LC-OBL-002` | fix the grammar's semantic roles and keywords with the adoption boundary at the surface capstone | grammar-shape tests |
| `LC-OBL-003` | require `List A` sources with the excluded-source boundary | elaboration typing tests |
| `LC-OBL-004` | fix left-to-right depth-first traversal with dependency, once-per-prefix source evaluation, and empty-input behavior | desugaring-equivalence tests |
| `LC-OBL-005` | fix `when` filter semantics: visible effects, false-as-skip, all other failures propagate, no guard fragment | filter witnesses |
| `LC-OBL-006` | consume C044's split: total ordinary generators, `case` mismatch-as-skip, `LCP002`/`LCP003` markers, `M001` reuse | coverage and marker diagnostics tests |
| `LC-OBL-007` | fix left-to-right scope, non-escaping non-recursive bindings, `LCP001` rebinding, `BS001` reuse | scope and rebinding tests |
| `LC-OBL-008` | fix exact order, multiplicity, non-short-circuiting filters, and failure timing with visible effect rows | trace-agreement tests |
| `LC-OBL-009` | fix eager ordered production with lazy and infinite inputs excluded | eager-production witnesses |
| `LC-OBL-010` | fix the typed qualifier-tree target, the extensional equations, and the no-dispatch rule | elaboration-shape tests |
| `LC-OBL-011` | fix `List B` results with all other targets excluded | result-type tests |
| `LC-OBL-012` | make sequential execution normative and parallel forms excluded | trace and absence tests |
| `LC-OBL-013` | produce the fused tail-recursive worker with linear allocation, source-faithful diagnostics, and cost honesty | worker-shape and stack-safety tests |
| `LC-OBL-014` | keep the contract deterministic and outside unowned claims with the reuse map enforced | determinism and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `LC-OBL-*` set against unknown and
uncovered identifiers before C047 conformance is claimed.

## Required evidence sets

Positive evidence includes desugaring-equivalence on the kernel
stepper and compiled BEAM for a single generator, a two-generator
Cartesian traversal, a `case` filtering generator skipping
mismatches, a `when` filter skipping `false`, and an exhaustive
`let` binding — agreeing on values with a hand-written recursive
program; an effect-bearing comprehension whose trace order is
source order; the fused-worker shape (one recursive worker, no
intermediate definitions); stack-safe deep-input production on
BEAM; and the three `LCP` diagnostics firing with the `M001` and
typing-family reuse.

Negative evidence — in the definitional sense — includes
rebinding, never-matching `case` patterns, unnecessary markers,
non-total ordinary generators, and refutable `let` patterns
rejecting; and no surface-syntax, non-list-source, lazy, parallel,
or non-list-target entry points existing.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities and predecessor APIs retaining their exact selections
and defaults.

## Revision and persistence separation

Revision `0.1.39` adds the comprehension contract and the `LCP`
families; it adds no JSON AST version, kernel S-expression version,
interface version, artifact version, signature domain, runtime
behavior, BEAM representation, manifest field, or surface syntax,
and amends no retained revision (`LC-OBL-001`, `LC-OBL-014`). The
one new public API is the dormant elaboration boundary.

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.39`; every predecessor API retains its exact selection. The
next unused semantic patch is `0.1.40`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[list-comprehensions synthesis](../../20-notes/list-comprehensions.md),
the [resolved inquiry](../../40-inquiries/how-should-catena-specify-list-comprehensions.md),
and the [topic map](../../10-maps/list-comprehensions.md). The C047
evidence record will preserve the sibling-compiler commands and
archive validation.
