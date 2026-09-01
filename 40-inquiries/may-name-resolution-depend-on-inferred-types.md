---
title: "May Name Resolution Depend on Inferred Types?"
kind: inquiry
created: "2026-09-01"
status: resolved
tags:
  - catena
  - name-resolution
  - type-system
  - language-design
aliases:
  - "G066 resolution inquiry"
---

# May Name Resolution Depend on Inferred Types?

## Purpose

G066 asks the checklist question: "State whether field, method,
constructor, literal, and operator resolution may depend on
inferred types." C021 already made resolution a function of scope
structure alone, C018 banned expected-type adaptation, C065
rejects trait ambiguity at the instance rather than the call site,
and C061 eliminated the last name-choice candidate by fixing
closed-set operator instantiation. What remained open was saying
so: one invariant, one five-way classification, and the
evidence-selection carve-out that keeps trait dispatch honest.

## Operational definitions

- **Name resolution** — choosing which declaration a written name
  denotes.
- **Type-directed resolution** — allowing that choice to depend on
  inferred or expected types (overloading by type).
- **Evidence selection** — choosing which instance dictionary runs
  for an already-resolved trait method name, governed by coherence.

## Hypotheses

1. A new area `name-resolution` at `0.1.42` (code `NMR`) carries
   the decision as a classification slice. *(Recommended: the
   C062 shape.)*
2. **Resolution is type-independent**: every name resolves as a
   function of scope structure alone; adding, removing, or
   changing annotations never changes a name's target. The
   five-way table: field labels are not resolved names (`select`
   is a typed operation); trait method names resolve normally with
   **instance selection classified as evidence selection, not
   resolution**; constructors are declaration-scoped by
   visibility; literals self-describe by spelling; operators
   instantiate over the closed set with no name choice.
3. Nothing arrives silently: overloaded-by-type names,
   expected-type-adapted literals, call-site ambiguity deferral,
   and field-access-by-inference are excluded, each amendable only
   by a revision that amends the table explicitly.
4. Zero new diagnostic families and no checker rule changes —
   witnesses run on existing machinery.

## Paths explored

- **Admit type-directed resolution per class** — rejected: the
  order-dependence hazard C021 explicitly rejected (the OCaml
  open-re-shadowing model), reopening the determinism discipline.
- **Classify trait instance selection as resolution** — rejected:
  makes the invariant false for methods and contradicts C065's
  instance-level ambiguity rejection.
- **Merge with G067** — rejected: unrelated subjects, and the
  corpus already expects the confirmation (the operators synthesis
  names G066 as the confirmation owner).
- **Defer** — rejected: every input is in hand.

## Findings

All four hypotheses held; the developer chose the recommended
option on all four forks (no overrides). The decisive corpus
facts: C021's scope-structural resolution with rejection on import
collision, `NM-OBL-005`'s no-adaptation clause, C065's
"not a deferred call-site ambiguity," and C061's closed-set
instantiation — each pillar already stands; G066 states the roof.

## Outcome

Resolved as C066 at revision `0.1.42`: the contract lives in the
[Name Resolution Specification](../60-specification/name-resolution/README.md),
the reasoning in
[Catena Name Resolution](../20-notes/catena-name-resolution.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G067 and D140
remain Section 7's open items; P109 owns any future surface
spellings.
