---
title: "What Progress and Preservation Targets Remain?"
kind: inquiry
created: "2026-09-01"
status: resolved
tags:
  - catena
  - metatheory
  - language-design
aliases:
  - "P132 metatheory targets inquiry"
---

# What Progress and Preservation Targets Remain?

## Purpose

P132 asks the checklist question: "C002 states the nominal and
structural claims; C003 adds condition typing, closed safety,
predicate expansion, fallthrough, commitment, guarded exhaustive
progress, fact soundness, lowering equivalence, receive
preservation, and evidence-erasure targets. Effects, public
processes, foreign values, and the integrated theorem remain
open." The completion bar is the one C002 and C003 set: normative
target statements with executable evidence, full proofs routed as
future obligations.

## Operational definitions

- **Target** — a normatively stated metatheory claim (progress,
  preservation, or an allied property) with named executable
  evidence; not a machine-checked proof.
- **Composed statement** — an integrated theorem written as its
  component theorems plus an explicit composition lemma, with the
  lemma's proof obligation routed to an owner.
- **Conditional extension** — a target stated for machinery that
  does not exist yet, holding iff the owning slice's arrival rules
  are discharged.

## Hypotheses

1. A new area `progress-and-preservation` at `0.1.45` (code `PP`)
   carries the completion as a targets slice. *(Recommended: the
   era precedent.)*
2. **Effects and failure targets** state preservation and progress
   for the shipped handler calculus — handler installation,
   affine resume-once, the return clause, and `trap` as the
   failure terminal — witnessed on existing machinery (C005
   corpus shapes, C036's process-context fixture, C030 trace
   agreement).
3. **The integrated theorem is a composed statement**: the
   component theorems (C002 data, C003 conditions, C010 kernel
   sequential and mailbox, this slice's effects targets) named as
   parts, plus a composition lemma whose proof obligation routes
   to the type-system inquiry and Section 16's formal-validation
   era. Checkable in parts now, provable later.
4. **Conditional, routed extensions** for the remainder: process
   targets restate C010's mailbox results as standing evidence and
   condition the public-process extension on G084/G085; foreign
   targets condition the theorem on G095/G096's visible boundary,
   where C067's rule makes entering values already-typed and
   preservation holds by construction.

## Paths explored

- **Prove the theorems now** — rejected: the open inquiry names
  exactly these proofs as incomplete; no proof infrastructure
  exists.
- **Defer the integrated theorem to Section 16** — rejected: fails
  P132's named remainder; the composed statement is the honest
  middle.
- **Claim the whole-language theorem** — rejected: dishonest
  without the composition proof.
- **Unconditional process/foreign statements** — rejected: claims
  theorems about machinery that does not exist.

## Findings

All four hypotheses held; the developer chose the recommended
option on all four forks (no overrides). The decisive corpus
facts: C002/C003's era precedent fixes the bar; C010 already holds
sequential and mailbox preservation as standing evidence; and
C067's boundary rule makes the foreign conditional nearly free.

## Outcome

Resolved as C132 at revision `0.1.45`: the contract lives in the
[Progress and Preservation Specification](../60-specification/progress-and-preservation/README.md),
the reasoning in
[Catena Progress and Preservation](../20-notes/catena-progress-and-preservation.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). Section 16
opens with its first closure; the composition proof and Section
16's remaining gates follow.
