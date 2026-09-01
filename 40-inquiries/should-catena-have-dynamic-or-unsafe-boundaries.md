---
title: "Should Catena Have Dynamic or Unsafe Boundaries?"
kind: inquiry
created: "2026-09-01"
status: resolved
tags:
  - catena
  - type-system
  - language-design
aliases:
  - "G067 dynamic boundaries inquiry"
---

# Should Catena Have Dynamic or Unsafe Boundaries?

## Purpose

G067 asks the checklist question: "Define casts, runtime type
inspection, unchecked operations, compiler intrinsics, and how
unsafety is made visible — or explicitly exclude them." The corpus
had already excluded the vocabulary where it could bite (C003's
guard fragment rejects "a foreign call, dynamic test, reflection
operation, or unchecked cast"), erased all type and specification
material from runtime artifacts (C006/C113 — there is no RTTI to
inspect), and closed the failure taxonomy with no dynamic-type-check
kind (C036). What remained open was saying so for the whole
intralanguage surface and routing the visibility requirement to
the only edges where dynamic values can enter: the foreign
boundaries (G095/G096/G098).

## Operational definitions

- **Cast** — an operation asserting a type the checker did not
  prove, unchecked or checked at runtime.
- **Runtime type inspection** — any form whose behavior branches
  on a value's runtime type (typecase, reflection, `type_of`).
- **Unchecked operation** — an operation whose safety the language
  does not guarantee (raw pointer analogy: trusted escape from the
  proof).
- **Compiler intrinsic** — a compiler-internal primitive exposed
  as callable source surface.
- **Visible boundary** — an entry point whose checks, types, and
  failure classification are part of its declared interface.

## Hypotheses

1. A new area `dynamic-and-unsafe-boundaries` at `0.1.43` (code
   `DU`) carries the decision as an exclusion slice. *(Recommended:
   the C044/C066 shape.)*
2. **All five forms are excluded intralingually**: no casts, no
   runtime type inspection, no unchecked operations, no compiler
   intrinsics, no reflection — unsafety cannot be written in
   Catena source. Arrival conditions per form: a future
   cast/typecase/dyn must state its representation (amending
   C006/C113 erasure), its failure classification (amending
   C036's taxonomy), its visibility, and its evidence interaction.
3. **Visibility routes to the foreign owners**: any dynamic or
   unsafe value entering Catena must pass a visible, typed,
   failure-classified boundary owned by its arriving slice
   (G095 Erlang terms, G096 foreign calls, G098 NIFs); G067
   states the cross-edge requirement and adds no mechanism. The
   C036 foreign-raise-to-`trap(reason)` mapping is the standing
   precedent; the term format's refusal of non-finite floats
   (the probes journal) is an existing visible boundary in kind.
4. Zero new diagnostic families and no checker rule changes —
   witnesses run on existing machinery.

## Paths explored

- **Define a visible dyn boundary now** — rejected: the only
  consumers are foreign edges whose slices are undesigned;
  inventing representation ahead of need is the pattern C038
  rejected.
- **Reserve compiler intrinsics for tooling** — rejected: nothing
  needs them (the kernel and stepper are compiler-internal, not
  source-callable); a reservation without an owner is dead weight.
- **Define a generic visibility mechanism now** — rejected:
  pre-empts G096's effect-declaration design with machinery that
  has no consumers.
- **Defer to the foreign era** — rejected: leaves the named
  question open while the foreign edges get designed against an
  unstated rule.

## Findings

All four hypotheses held; the developer chose the recommended
option on all four forks (no overrides). The decisive corpus
facts: C003's guard vocabulary already names the forms, C006's
erasure rule leaves nothing to inspect at runtime, and C036's
taxonomy has no kind a cast failure could inhabit — three anchors
that make the exclusion a statement of fact rather than a new
rule.

## Outcome

Resolved as C067 at revision `0.1.43`: the contract lives in the
[Dynamic and Unsafe Boundaries Specification](../60-specification/dynamic-and-unsafe-boundaries/README.md),
the reasoning in
[Catena Dynamic and Unsafe Boundaries](../20-notes/catena-dynamic-and-unsafe-boundaries.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G095/G096/G098
implement the visibility requirement when their slices exist; D140
and P132 remain Section 7's open items.
