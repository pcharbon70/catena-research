---
title: "How Do the Excluded Advanced Type Forms Stay Excluded?"
kind: inquiry
created: "2026-09-01"
status: resolved
tags:
  - catena
  - type-system
  - language-design
aliases:
  - "D140 advanced exclusions inquiry"
---

# How Do the Excluded Advanced Type Forms Stay Excluded?

## Purpose

D140 defers the advanced type features: "Impredicativity, inferred
higher rank, general linear and dependent types, unrestricted
type-level computation, and higher-kinded polymorphism over
arbitrary kinds stay outside version 0.1.1." The exclusions
themselves are already normative — C001's advanced-type-checking
chapter lists seven excluded forms with a profile-boundary
diagnostic rule, and C068 closed the positive complement (the
checked advanced profile) at the annotation boundary. What the
corpus lacked is a normative home for the **arrival gate**: the
discipline a future slice must discharge before any excluded form
exists. That discipline already exists in prose — remaining-areas'
seven-point list.

## Operational definitions

- **Excluded form** — one of the seven advanced type features C001
  excludes for edition 0.1.
- **Arrival gate** — the seven statements a future slice must make:
  an independent problem statement, evidence of repeated use, an
  interaction audit, a formal semantics, an operational contract,
  a diagnostic story, and a comparison with an ordinary library or
  explicit core mechanism.
- **Checked profile** — C068's positive complement: predicative
  explicit higher rank, signature-directed GADTs, branch-local
  equalities, and explicit rigid constructor existentials, behind
  an annotation boundary.

## Hypotheses

1. A new area `excluded-advanced-type-features` at `0.1.44` (code
   `EA`) carries the decision as a small confirmation slice.
   *(Recommended: the C046 precedent — D046 closed when C044
   recorded its exclusion with arrival conditions.)*
2. **The exclusion table covers the full C001 list** — the seven
   forms including first-class existential packages beyond
   declared constructors and unrestricted GADT inference, not only
   the five D140 names — one boundary, one table, no second slice.
3. **The seven-point gate is adopted verbatim** as the per-form
   amendment route; each arriving slice states all seven for the
   form it admits.
4. Zero new diagnostic families (C001's rule that rejection
   identifies the profile boundary stands) and no checker rule
   changes; the checked profile stays unchanged.

## Paths explored

- **Pointer-only closure** — rejected: leaves the arrival gate as
  inbox prose rather than normative text, weaker than every other
  closure of the era.
- **D140's forms only** — rejected: existentials and GADT
  inference would lack recorded arrival conditions.
- **Bespoke per-form conditions** — rejected: invents per-form
  analysis a confirmation slice has no evidence for; the
  seven-point gate already generalizes.
- **Fold into P132** — rejected: unrelated subjects.

## Findings

All four hypotheses held; the developer chose the recommended
option on all four forks (no overrides). The decisive fact: C001
and C068 already partition the space — the negative side
(exclusions) and the positive side (checked profile) both stand at
`0.1.1`; D140's completion only writes the gate between them.

## Outcome

Resolved as C140 at revision `0.1.44`: the contract will live in
`60-specification/excluded-advanced-type-features/`, the reasoning
in [Catena Excluded Advanced Types](../20-notes/catena-excluded-advanced-types.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). Section 7
completes at 10/10; P132 and Section 9's resource half remain the
next era's work.
