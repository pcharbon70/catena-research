---
title: "What Are Structural Records and Variants?"
kind: inquiry
created: "2026-08-29"
status: resolved
tags:
  - catena
  - records
  - variants
  - rows
  - language-design
aliases:
  - "P041 structural records inquiry"
---

# What Are Structural Records and Variants?

## Purpose

P041 asks the checklist question: "Specify literal, selection, update
syntax, duplicate labels, and row-polymorphic typing... and runtime
representation" (with extension and restriction from the program
doc). The kernel's calculus already implements the complete
operation set — record literals with unique-label rejection, select,
update, extend, restrict, variant injection and matching, row types
with tails — frozen at 0.1.8 and exercised end-to-end by the C010
fixture. This inquiry elevates that calculus to language-level
rules, the Section 4 pattern's Section 5 debut.

## Operational definitions

- **Structural record** — a finite unique-label-to-value map whose
  identity is its field set and contents, not a nominal declaration.
- **Structural variant** — an injection of one labeled payload into
  an open variant row.
- **Closed row** — a record or variant whose field set is complete
  at the literal.
- **Open tail** — a type-position row variable composing row
  polymorphism through signatures.

## Hypotheses

1. A new area `structural-records-and-variants` at `0.1.36` (code
   `SR`) carries the contract, elevating the kernel calculus. C010
   stays frozen; C002's nominal exclusions stay. *(Recommended:
   one-version-per-area.)*
2. **Full kernel consolidation** in one cited table — literal,
   select, update, extend, restrict, inject, match — with duplicate
   labels rejected, field order controlling effects but never
   equality, and missing-label operations statically unreachable.
3. The row typing is **kernel rows verbatim**: literals closed;
   extend/restrict closed over closed inputs; open tails only in
   type positions; select requires the label present. No open-record
   expressions, no widening.
4. The representation is **semantic maps verbatim**: written order
   controls effects, never equality or row identity (C030/C037);
   representation invisible; BEAM rides maps as the kernel backend
   already does.
5. The deliverable is kernel-path witnesses with zero new diagnostic
   families — the C036/C037 target pair (stepper + compiled BEAM),
   the fixture's operation round-trip, duplicate-label rejection,
   variant dispatch, and the JSON-AST absence stated.

## Paths explored

- **Partial elevation** (literal/select/update only) — rejected: the
  kernel fixture exercises extend/restrict today; partial would be
  knowingly incomplete.
- **Open-record literals** — rejected: new machinery the kernel never
  fixed, the invented-form pattern.
- **Deferring tail composition** — rejected: the kernel's type module
  already substitutes tails; deferring leaves shipped facts
  unclassified.
- **Stable layout or field-order guarantee** — rejected: amends
  C023 and C037.
- **Frontend integration / normative-only** — rejected patterns.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (five of five, no overrides). The witness-target pair
is the C036/C037 precedent: the frozen JSON AST carries no record
or variant expression tags, so all evidence runs on the kernel
S-expression path, with BEAM-side assertions checking selected values
(not map shapes) since representation is invisible by contract.

## Outcome

Resolved as C041 at revision `0.1.36`: the contract will live in
`60-specification/structural-records-and-variants/`, the reasoning
in [Catena Structural Records](../20-notes/catena-structural-records.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). P109 spellings
and the frontend path, G042 collection semantics, G062 aliases, and
P044 refutability remain open with their owners.
