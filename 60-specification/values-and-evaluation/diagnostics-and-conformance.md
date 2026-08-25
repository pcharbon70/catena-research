---
title: "Values and Evaluation Diagnostics and Conformance"
kind: specification
created: "2026-08-24"
status: normative
spec_version: "0.1.25"
tags:
  - conformance
  - diagnostics
  - values
  - evaluation
  - specification
  - testing
aliases:
  - "Catena 0.1.25 values conformance"
---

# Values and Evaluation Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.25 values diagnostic,
abstract frontend, and conformance contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [Value Forms and First-Classness](value-forms-and-first-classness.md)
and [Strictness and Terminal Outcomes](strictness-and-terminal-outcomes.md).

## Stable diagnostics

This area introduces **zero new diagnostic families** (`VA-OBL-001`,
`VA-OBL-008`). It is definitional: it accepts no new input forms and
rejects nothing existing, so no new invalid input exists to diagnose.
Every existing diagnostic family keeps its identity and meaning
unchanged; nothing in this area alters any failure's classification.

## Abstract public boundaries

Two boundaries gain values wiring (`VA-OBL-001`):

- **Value classification** — a total classification operation over
  typed-core expression forms and kernel terms implements the closed
  grammar: it reports value or non-value for every decodable form,
  never crashes on well-formed input, and gives the reason for each
  non-value classification against the closed non-value list.
- **Stepper terminals** — the shipped kernel stepper's terminal
  contract (`{:value, expression}` or `{:trap, reason, result}`)
  witnesses the terminal-outcome rule: every terminal it produces
  carries a value or a trap, and nothing else.

Implementations MUST NOT use these boundaries to claim equality,
ordering, rendering, observability, lazy forms, or any excluded
machinery (`VA-OBL-008`). The bootstrap evidence adds no new public
API names beyond the classification operation.

## Determinism

Equal forms classify equally; classification is order-, locale-, and
tool-independent (`VA-OBL-008`). The classifier is total over decodable
typed-core and kernel input.

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `VA-OBL-001` | apply values behavior only at exact 0.1.25 and register the stable lifecycle addition | exact selection, registry, and lifecycle tests |
| `VA-OBL-002` | fix the closed value grammar and the closed non-value list with kernel rules unchanged | classification matrix tests |
| `VA-OBL-003` | admit Float as the tenth value form with C018 semantics unchanged | float classification tests |
| `VA-OBL-004` | guarantee uniform first-classness: bindable, passable, returnable, storable, with exclusions named not tiered | storage-and-return witness tests |
| `VA-OBL-005` | keep value membership closed: no form outside the grammar classifies as a value | closed-set tests |
| `VA-OBL-006` | enforce the strictness invariant with the two named exceptions and the value-or-trap terminal contract | stepper terminal and exception tests |
| `VA-OBL-007` | gate every future lazy or multi-evaluation form behind an edition record | absence and registry-shape tests |
| `VA-OBL-008` | keep classification deterministic and outside P035/G036/G037/P109 claims | repeated-result and exclusion tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `VA-OBL-*` set against unknown and
uncovered identifiers before C029 conformance is claimed.

## Required evidence sets

Positive evidence includes every value form classifying as a value —
integer, Boolean, Unit, Float (including both signed zeros), nested
tuples of values, closures, constructor values, records, injections
carrying values, and opaque handles; structural forms with nested
non-values classifying as non-values; every non-value classifying with
its reason — evidence, handler declaration, capability name,
resumption, trap, effect row, signature; stepper terminals always
carrying a value or a trap across a corpus including trap-producing
programs; `and`/`or` skip witnesses; Float classification through the
C018 boundary; and determinism across repeated classification.

Negative evidence — in the definitional sense of non-membership —
includes every closed-grammar miss classifying as a non-value and no
crash on any decodable form.

Exclusion evidence demonstrates that classification claims no equality,
ordering, rendering, or observability, that no lazy form is admitted,
that no existing diagnostic identity changes, and that predecessor
APIs retain their exact selections and defaults.

## Revision and persistence separation

Revision `0.1.25` adds the value grammar, the non-value list,
first-classness, the strictness invariant, the terminal contract, and
the classification operation; it adds no JSON AST version, kernel
S-expression version, interface version, artifact version, signature
domain, typing rule, runtime behavior, BEAM representation, manifest
field, or diagnostic family (`VA-OBL-001`, `VA-OBL-008`). No retained
revision is amended: the 0.1.8 kernel chapters keep their exact-input
boundary, and this area elevates rather than extends them.

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.25`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.26`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[values synthesis](../../20-notes/catena-values-and-evaluation.md), the
[resolved inquiry](../../40-inquiries/what-are-catenas-values-and-strictness.md),
and the [topic map](../../10-maps/values-and-evaluation.md). The C029
evidence record will preserve the sibling-compiler commands and archive
validation.
