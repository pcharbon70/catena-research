---
title: "Catena Exception Boundary"
kind: note
created: "2026-09-01"
maturity: developing
tags:
  - catena
  - failure
  - effects
  - language-design
aliases:
  - "the exception partition"
---

# Catena Exception Boundary

## Executive conclusion

Catena's answer to "what are exceptions?" is a partition into
three visibly distinct mechanisms — and no language exception
form. **Typed failure is a value** (`Option`/`Result`-shaped,
first-class, G103's contents). **Exception-style catching is the
effect pattern**: a request whose handler declines to resume is a
one-shot escape, visible in the effect row, catchable only by an
enclosing handler — sanctioned as an idiom, adding no rule to
C005. **Fatal failure is `trap(reason)`**: one terminal mechanism,
kinded, never catchable, with the programmer panic as its reserved
assertion/panic kind. Process exits, foreign failures, and
cancellation are routed to their owning gaps; C044's reopening
condition remains the only door for a language exception form.

## Scope, method, and definitions

This note synthesizes the archive's evidence for closing G081 at
revision `0.1.47`. It reads C036's failure taxonomy, C044's
exception-clause exclusion, C005's resumption discipline, C010's
process-local trap evidence, and C067's foreign visibility
routing; it invents no mechanism.

## Why a partition and not a mechanism

Every candidate answer to G081 already has a home. "An effect" —
yes, as the idiom: the calculus's affine resumptions make
declining to resume the natural one-shot escape, and its handler
nesting is the catching. "A value type" — yes: typed failure is
first-class. "A trap kind" — yes: panics and reserved faults are
kinded traps. What the corpus forbids is collapsing these into one
ambiguous `catch`: a site that cannot tell whether it is handling
a value, an abort, or a fatality loses the three-way partition
(C029/C036) that the whole failure architecture rests on.

## What each site can see

A caller sees a typed failure in a return type; an effect row
names what a handler may abort to; a trap is observed only as its
process's termination with a kinded reason. No construct blurs
the boundaries, and no construct converts one class into another
silently — converting a trap to a value is impossible (terminal),
and converting an effect abort to a trap is a handler's explicit
choice to trap instead of resume.

## Tradeoffs, limitations, falsification

The partition costs ergonomics: languages with a universal
`try` read shorter. The corpus prices honesty higher. Falsification:
any catchable trap, any language raise/catch form arriving without
reopening C036, any silent class conversion, or any panic that is
not a kinded trap voids this contract.

## Route to sources

- The Exception Boundary Specification (candidate, then normative
  at promotion, in `60-specification/exception-boundary/`) will
  define the contract this note argues for.
- [The Six Categories](../60-specification/runtime-failure-taxonomy/the-six-categories.md)
  — the taxonomy the partition preserves.
- [Context Rules and Reservations](../60-specification/pattern-contexts/context-rules-and-reservations.md)
  — C044's exception-clause exclusion with the reopening door.
- [Deep Handlers and Affine Resumptions](../60-specification/effects-and-handlers/deep-handlers-and-affine-resumptions.md)
  — the discipline that makes the pattern possible.
- The [resolved inquiry](../40-inquiries/are-exceptions-an-effect-a-trap-or-a-value.md)
  preserves the decision route.
