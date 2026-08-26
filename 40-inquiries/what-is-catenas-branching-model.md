---
title: "What Is Catena's Branching Model?"
kind: inquiry
created: "2026-08-25"
status: resolved
tags:
  - catena
  - branching
  - conditionals
  - match
  - language-design
aliases:
  - "G033 branching inquiry"
---

# What Is Catena's Branching Model?

## Purpose

G033 asks the checklist question: "Specify Boolean conditions, match
expressions, branch typing, missing alternatives, and whether any
statement-like control forms exist." The substance is shipped — C002
fixes match expressions with exhaustive coverage and branch typing,
C003 fixes Boolean conditions in the clause form, the kernel fixes
commitment dynamics, and C029–C032 fixed the surrounding model — but
scattered across five areas. This inquiry consolidates the
language-level account and resolves the two genuinely open questions:
the general conditional and statement forms.

## Operational definitions

- **Branch form** — the single expression form that selects among
  clause bodies by pattern (and condition) testing.
- **Branch typing** — clause bodies unify with the match's type.
- **Missing alternative** — a scrutinee value matching no clause;
  `M001` with a witness.
- **Statement-like control form** — any construct that sequences or
  exits without producing a value.
- **Conditional sugar promise** — the fixed desugaring any future
  conditional surface spelling receives.

## Hypotheses

1. A new area `branching` at `0.1.29` (code `BR`) completes the
   Section 4 sibling run; C002 and C003 stay frozen and are cited.
   *(Recommended: the one-version-per-area invariant forbids
   extending them.)*
2. **Match is the only branch form**, with the sugar promise: any
   future conditional spelling P109 introduces desugars to a match on
   a `Bool` scrutinee with `true`/`false` patterns (or C003's clause
   conditions), with shipped semantics as its meaning — the C032
   multi-param-sugar pattern. No new expression form exists on any
   retained input (frozen AST tags). *(Recommended: an `if` form is
   impossible now and forever redundant with match.)*
3. **Statement-like control forms do not exist**, declared
   normatively: every construct is an expression; branching yields
   values through clause bodies; effects sequence through C031's let
   idiom; no early return, no break, no statement tier.
4. One consolidated chapter elevates the scattered rules with
   citations — scrutinee-once, source-order clauses,
   pattern-before-condition, one condition evaluation, false
   fallthrough, irreversible commitment, branch typing, `M001`
   missing alternatives, `and`/`or` composition under C029's skips,
   and match-dispatched tails keeping C032's guarantee.
5. C032-style witnesses with zero new diagnostic families are the
   deliverable: Boolean-pattern dispatch as the conditional,
   fallthrough ordering with observable effects, branch-typing
   agreement, `M001` and redundancy unchanged, commitment
   irreversibility, and the no-statement absence.

## Paths explored

- **New `if` expression form now** — rejected: impossible on retained
  inputs (frozen tags) and redundant with match.
- **Match-only without the sugar promise** — rejected: weaker; invites
  the P109 exercise to reinvent conditional semantics instead of
  consuming fixed ones.
- **Reserve a statement tier** — rejected: pre-decides against the
  everything-is-an-expression architecture the kernel fixed.
- **Defer the statement question to P109** — rejected: leaves the
  checklist's explicit clause undelivered.
- **Extend C002/C003 chapters** — rejected: amends retained areas.
- **Minimal residuals-only chapter** — rejected: loses the one-place
  answer G033 asks for.
- **New branch warnings / normative-only** — rejected: duplicates
  C002's redundancy family; rejected pattern.

## Findings

All five hypotheses held; the developer chose the recommended option
on every fork (five of five, no overrides). One evidence-shape
refinement: C003's conditions are the *pure* fragment, so the
fallthrough witness cannot observe condition effects — the observable
comes from scrutinee and chosen-body effects, with fallthrough proven
by *which* body's effects appear. Condition purity is itself part of
the shipped answer and is consolidated, not changed.

## Outcome

Resolved as C033 at revision `0.1.29`: the contract will live in
`60-specification/branching/`, the reasoning in
[Catena Branching](../20-notes/catena-branching.md), and the forks in
the [design decision
register](../20-notes/design-decision-register.md). P034 termination,
G036 failure taxonomy, G040 future scrutinee types' coverage entries,
P109 surface spellings, and G088 cancellation mid-branch remain open
with their owners.
