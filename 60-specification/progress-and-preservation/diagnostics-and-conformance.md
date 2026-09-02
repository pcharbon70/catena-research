---
title: "Progress and Preservation Diagnostics and Conformance"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.45"
tags:
  - conformance
  - diagnostics
  - metatheory
  - specification
  - testing
aliases:
  - "Catena 0.1.45 metatheory conformance"
---

# Progress and Preservation Diagnostics and Conformance

## Status and authority

This chapter is the normative Catena 0.1.45 progress-and-
preservation diagnostic, abstract frontend, and conformance
contract. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Effects and Failure Targets](the-effects-and-failure-targets.md) and
[The Integrated Theorem](the-integrated-theorem.md).

## Stable diagnostics

This area introduces **zero new diagnostic families**
(`PP-OBL-001`, `PP-OBL-002`). Targets state properties; the
rejections that guard them (affine-resumption duplication,
handler-row mismatches, unhandled requests) keep their C005
identities.

## Abstract public boundaries

The shipped boundaries witness the contract on existing machinery;
the bootstrap adds no new public API (`PP-OBL-001`):

- **Reference stepper and compiled BEAM** — handler programs
  agreeing on values and traces (installation, resume-once,
  return clause); the trap fixture (trapping child, spared
  spawner) agreeing on terminal states.
- **Kernel metatheory corpus** — sequential and mailbox
  preservation evidence (C010), unchanged.

Implementations MUST NOT use these boundaries to claim the
composition lemma, the public-process extension, or any
unconditional whole-language theorem (`PP-OBL-006`,
`PP-OBL-007`).

## Determinism

Unchanged programs produce identical values, traces, and
diagnostics on every conforming target (`PP-OBL-002`).

## Conformance obligations

| ID | Obligation | Required executable evidence |
| --- | --- | --- |
| `PP-OBL-001` | apply target rules only at exact 0.1.45 and register the stable lifecycle addition with zero new families and no new API | exact selection, registry, and lifecycle tests |
| `PP-OBL-002` | state the effects-and-failure targets over the shipped calculus only | handler and trap witnesses |
| `PP-OBL-003` | keep effect progress and trap terminality as stated with kernel-verbatim reasons | trace-agreement witnesses |
| `PP-OBL-004` | carry each target's evidence obligation with the C030 dual-agreement discipline | agreement witnesses |
| `PP-OBL-005` | keep the integrated theorem as a composed statement with the conditional summary | composition-part pinning |
| `PP-OBL-006` | keep the composition lemma a routed proof obligation, never a claim | absence and wording tests |
| `PP-OBL-007` | keep the process and foreign extensions conditional and routed to their owners | routing witnesses |
| `PP-OBL-008` | keep the contract deterministic with the component corpora unchanged | determinism tests |

Every obligation has at least one tagged passing test. The sibling
compiler gates the complete `PP-OBL-*` set against unknown and
uncovered identifiers before C132 conformance is claimed.

## Required evidence sets

Positive evidence includes handler programs agreeing on stepper
and BEAM for installation, resume-once, and return-clause
completion; the trap fixture's terminal states; the kernel
metatheory corpus re-pinned; and the lifecycle registration of
0.1.45.

Negative evidence — in the definitional sense — includes no
claimed composition proof, no public-process or foreign-value
claims beyond the conditionals, and no extension of any component
target beyond its stated calculus.

Exclusion evidence demonstrates unchanged predecessor diagnostic
identities and predecessor APIs retaining their exact selections
and defaults.

## Revision and persistence separation

Revision `0.1.45` adds the effects-and-failure targets, the
composed integrated theorem, and the conditional extensions; it
adds no JSON AST version, kernel S-expression version, interface
version, artifact version, signature domain, typing rule, runtime
behavior, BEAM representation, manifest field, public API name, or
diagnostic family, and amends no retained revision (`PP-OBL-001`,
`PP-OBL-002`).

The source-text decoder accepts cumulative revisions `0.1.9` through
`0.1.45`; every predecessor API retains its exact selection. The next
unused semantic patch is `0.1.46`.

## Rationale and evidence (non-normative)

The design route is preserved in the
[synthesis](../../20-notes/catena-progress-and-preservation.md),
the [resolved inquiry](../../40-inquiries/what-progress-and-preservation-targets-remain.md),
and the [topic map](../../10-maps/progress-and-preservation.md).
The [C132 evidence
record](../../50-journal/2026-09-01-c132-metatheory.md)
preserves the sibling-compiler commands and archive validation.
