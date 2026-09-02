---
title: "The Exclusion Table and Gate"
kind: specification
created: "2026-09-01"
status: normative
spec_version: "0.1.44"
tags:
  - type-system
  - specification
aliases:
  - "Catena advanced exclusion gate"
---

# The Exclusion Table and Gate

## Status and authority

This chapter is the normative Catena 0.1.44 exclusion table and
arrival gate. It is governed by
[Specification Authority](../../SPECIFICATION-AUTHORITY.md),
[Catena Conformance Vocabulary](../../CONFORMANCE-VOCABULARY.md), and
[Catena Implementation Limits and Portability](../../IMPLEMENTATION-LIMITS.md).
It restates as routing rows the exclusions and checked profile of
[Advanced Type Checking](../type-system/advanced-type-checking.md)
(C001/C068, unchanged) and adopts the arrival discipline the
[remaining research areas](../../00-inbox/remaining-catena-research-areas.md)
fix in prose.

The rules apply only to source-language revision `0.1.44`. They do
not reinterpret retained manifests, interfaces, artifacts, or
signed formats.

## The exclusion table

> **Normative definition.**

The following forms are excluded from edition `0.1` (`EA-OBL-002`),
each exclusion standing unchanged from `0.1.1` (C001):

| Form | What it would admit |
| --- | --- |
| Impredicative instantiation | quantification over arbitrary types, breaking the predicative boundary |
| Inferred higher rank | rank-2+ types arising without the annotation boundary |
| First-class existential packages beyond declared constructors | existentials outside C002's declared, rigid surface |
| General linear types | usage-counted values beyond C005's affine, branch-scoped resumptions |
| Dependent types | types indexing on values |
| Unrestricted type families | computation at the type level |
| Higher-kinded polymorphism over arbitrary kinds | abstraction over type constructors beyond the declared kind discipline |
| Unrestricted GADT inference | equalities arising without signature direction (`EA-OBL-002`) |

Rejection of one of these forms MUST identify the profile boundary
rather than report an unrelated unification failure (C001's rule,
unchanged) (`EA-OBL-004`). The **checked profile** — predicative
explicit higher rank, signature-directed GADTs, branch-local
equalities, and explicit rigid constructor existentials, behind an
annotation boundary — is the positive complement and stays
unchanged (C068) (`EA-OBL-005`).

## The arrival gate

> **Normative definition.**

A slice that admits any excluded form MUST, in its own normative
revision, state for that form (`EA-OBL-003`):

1. an **independent problem statement** — what problem the form
   solves that no shipped mechanism solves;
2. **evidence of repeated use** — programs or domains that hit the
   problem more than once;
3. an **interaction audit** — effects on principality (C063),
   coherence (C065), erasure (C006), resolution
   (C021/C066), and the failure taxonomy (C036);
4. a **formal semantics** — typing and dynamics with the form's
   proofs or proof obligations;
5. an **operational contract** — evaluation order, cost honesty,
   and representation stance under invisibility;
6. a **diagnostic story** — how rejections identify the boundary
   and how errors read; and
7. a **comparison with an ordinary library or explicit core
   mechanism** — why the form beats the non-advanced alternative
   (`EA-OBL-003`).

Until all seven are stated with witnesses, the exclusion binds.
Forms arrive independently or not at all: no omnibus
advanced-features revision is admitted (`EA-OBL-006`).

## Rationale and evidence (non-normative)

The [excluded-advanced-types synthesis](../../20-notes/catena-excluded-advanced-types.md)
argues the gate-not-ban reading — each exclusion guards a priced
guarantee, and the gate prices admission. The [resolved
inquiry](../../40-inquiries/how-do-the-excluded-advanced-type-forms-stay-excluded.md)
preserves the decision route.
