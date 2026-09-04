---
title: "The Six Categories"
kind: specification
created: "2026-08-26"
status: normative
spec_version: "0.1.32"
tags:
  - failure
  - taxonomy
  - specification
aliases:
  - "Catena failure category mapping"
---

# The Six Categories

## Status and authority

This chapter is the normative Catena 0.1.32 category mapping and entry
rule. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It applies [The Single Outcome](the-single-outcome.md) over the
deferred boundaries of C005, C018, and C034.

The rules apply only to source-language revision `0.1.32`.

## The mapping

The checklist's six categories classify as (`FT-OBL-005`):

> **Normative definition.**

| Category | Classification at 0.1.32 |
| --- | --- |
| Explicit panic or crash | the kernel's `trap` expression — the only user-invoked failure; its surface spelling is P109's |
| Typed failure (`Option`/`Result`) | ordinary **values**, non-failures: G105's library types return domain values; a "no answer" is normal termination |
| Arithmetic faults | **reserved** — no faulting operator exists in the closed inventory; the kind enters with its producer |
| Failed assertions | **reserved** — no assert form exists; the kind enters with its producer |
| Foreign exceptions | **reserved** — foreign calls (G095/G096) do not exist; a foreign raise will map to `trap(reason)` (the 0.1.47 [Exception Boundary](../exception-boundary/README.md) restates this mapping as its routing row) |
| VM termination | **operational**, outside program semantics — G084/G092/G121's machinery, never an outcome class |

## The entry rule

> **Normative definition.**

A failure producer — the first faulting arithmetic operator, the
first assert form, the foreign boundary (G095/G096), or any successor
whose evaluation can terminate abnormally — enters the language
**only through a slice that classifies its failures as
`trap(reason)` in the same change** (`FT-OBL-006`). No producer may
add a second outcome class, and no producer may arrive with its
failures unclassified. An implementation MUST NOT use this area's
boundary to claim an unclassified failure kind.

## Typed failure is not failure

The mapping's most consequential row deserves its statement: typed
failure returns; it does not trap. An `Option`-typed function that
answers "none" has terminated normally with a value — comparable,
storable, returnable like any value. Classifying domain answers as
failures would make ordinary total functions abnormal; G105 builds
its types on this separation (`FT-OBL-007`).

## Determinism

Equal programs trap identically or terminate identically on every
conforming target; the mapping and gate are classifications, not
behaviors (`FT-OBL-008`).

## Deliberately separate work

G105 owns library contents; G095/G096 the foreign boundary; G084
process death and signals; G092/G121 VM termination; G088
cancellation; P109 assert/panic spellings; G037 failure-path
allocation observability.

## Rationale and evidence (non-normative)

The [failure synthesis](../../20-notes/catena-runtime-failure-taxonomy.md)
records why the mapping is honest about absent producers and why
typed failure is the taxonomy's sharpest distinction. The [topic
map](../../10-maps/runtime-failure-taxonomy.md) routes the decision.
