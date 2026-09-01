---
title: "Catena Dynamic and Unsafe Boundaries"
kind: note
created: "2026-09-01"
maturity: developing
tags:
  - catena
  - type-system
  - erasure
  - language-design
aliases:
  - "Catena unsafe exclusion"
---

# Catena Dynamic and Unsafe Boundaries

## Executive conclusion

Unsafety cannot be written in Catena source. Edition `0.1` has no
casts, no runtime type inspection, no unchecked operations, no
compiler intrinsics, and no reflection — and the corpus's own
architecture made this a statement of fact rather than a fresh
renunciation: the guard fragment already rejects the vocabulary,
erasure leaves no runtime type material to inspect, and the
failure taxonomy has no kind a cast failure could inhabit. The
only dynamic edges are foreign (G095/G096/G098), and the one rule
G067 adds for them is a requirement, not a mechanism: whatever
enters must pass a visible, typed, failure-classified boundary
owned by its arriving slice.

## Scope, method, and definitions

This note synthesizes the archive's evidence for closing G067 at
revision `0.1.43`. It reads C003's guard fragment, C006's erasure
rule, C036's failure taxonomy, C035's comparable set, and the
foreign-gap texts (G095/G096/G098); it invents no mechanism.

## Three anchors that decided the question

1. **The guard vocabulary (C003)**: the checker already rejects
   "a foreign call, dynamic test, reflection operation, or
   unchecked cast" — the checklist's categories are named
   exclusions in the one fragment where they were ever tempted.
2. **Erasure (C006/C113)**: no specification, governance, or type
   material survives into runtime artifacts — there is no runtime
   type information for a typecase to branch on. Admitting
   inspection means amending erasure itself.
3. **The failure taxonomy (C036)**: `trap(reason)` with kinded
   reasons has no dynamic-type-check kind; foreign raises map to
   `trap(reason)` already. A checked cast needs a failure
   classification that does not exist and cannot arrive silently.

## The foreign visibility requirement

Dynamic values can only enter at three edges: Erlang terms
(G095), foreign calls (G096), and NIFs (G098). G067's one
addition is the cross-edge rule: every entry must be visible —
declared, typed, and failure-classified in its owning slice. The
standing precedents: C036's foreign-raise mapping, and the BEAM's
own term-format refusal of non-finite floats (the probes journal)
— a host boundary that is visible by refusing rather than by
coercing. The requirement binds the foreign slices' designs; it
does not build anything now.

## Tradeoffs, limitations, falsification

The exclusion costs ergonomics at the seams: until the foreign
slices exist, there is simply no way to bring an untyped value in
— which is the point. If any form (cast, typecase, intrinsic,
reflection) appears without first amending erasure and the failure
taxonomy per its arrival conditions, this contract is falsified
and must be amended by a new revision.

## Route to sources

- The [Dynamic and Unsafe Boundaries Specification](../60-specification/dynamic-and-unsafe-boundaries/README.md)
  defines the normative `0.1.43` contract this note argues for.
- [Syntax and Safety](../60-specification/clause-conditions/syntax-and-safety.md)
  — the guard vocabulary (anchor one).
- [Artifacts, Erasure, and CLI](../60-specification/specifications-and-governance/artifacts-erasure-and-cli.md)
  — the erasure rule (anchor two).
- [The Six Categories](../60-specification/runtime-failure-taxonomy/the-six-categories.md)
  — the taxonomy with no cast kind (anchor three).
- [BEAM float host-boundary probes](../50-journal/2026-08-31-beam-float-boundary-probes.md)
  — a visible host boundary in kind.
- The [resolved inquiry](../40-inquiries/should-catena-have-dynamic-or-unsafe-boundaries.md)
  preserves the decision route.
