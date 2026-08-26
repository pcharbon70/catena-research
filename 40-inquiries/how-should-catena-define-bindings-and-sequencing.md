---
title: "How Should Catena Define Bindings and Sequencing?"
kind: inquiry
created: "2026-08-25"
status: resolved
tags:
  - catena
  - bindings
  - sequencing
  - language-design
aliases:
  - "G031 bindings and sequencing inquiry"
---

# How Should Catena Define Bindings and Sequencing?

## Purpose

G031 asks the checklist question: "Define `let`-like syntax, scope,
recursive bindings, mutual recursion, unused values, and sequencing of
effectful expressions." The kernel fixes the core facts — substitute
after value, unused bindings stay valid with effects preserved, named
recursion through the signed environment — but they are frozen at
0.1.8, the sequencing form is kernel-only, and nothing states scope or
shadowing at the bindings level. This inquiry resolves the language
account.

## Operational definitions

- **Local binding** — a `let`-shaped binding: one plain value name,
  one right-hand-side expression, one body evaluated after
  substitution.
- **Non-recursive** — the RHS's environment does not contain the name
  being bound.
- **Sequencing idiom** — `let _ = e1; e2`: evaluate e1 to a value,
  discard it, then evaluate e2.
- **Unused binding** — a binder whose name never occurs in the body.
- **Definitions-only recursion** — recursion lives in named
  definitions via the signed environment; C024's SCC is the
  mutual-recursion statement at module level.

## Hypotheses

1. A new area `bindings-and-sequencing` at `0.1.27` (code `BS`)
   completes the trilogy — values (C029, *what*), order (C030,
   *when*), bindings (C031, *structure*). *(Recommended: the
   one-version-per-area invariant forbids extending the week-old
   evaluation-order area.)*
2. Local `let` is strictly non-recursive; recursion is definitions-only
   with C024's SCC as the mutual-recursion home; local recursive forms
   belong to G032's named local functions and P034's termination work.
   *(Recommended: the kernel's substitute-after-value rule already
   implies non-recursion.)*
3. Unused bindings stay valid with RHS effects preserved (kernel rule
   elevated), plus an IMP001-style deny-able `BS001` warning with a
   `_`-prefix exemption as the deliberate-discard escape hatch.
   *(Recommended: matches the corpus's only warning precedent and adds
   real lint value.)*
4. Sequencing of effectful expressions is the let-with-unused-binder
   idiom, elevated and normative — the only sequencing the retained
   JSON AST can express without amending frozen tags; P109 may surface
   dedicated punctuation later.
5. Local bindings shadow anything in scope, C021 verbatim — innermost
   wins, no new collision diagnostics.
6. C030-style witnesses on stepper, evaluator, and BEAM plus the
   `BS001` compiler wiring are the executable deliverable.

## Paths explored

- **Local recursive `let` / letrec-and** — rejected: folds G032's
  named-local-function question in prematurely and duplicates C024's
  module-level answer at the wrong layer.
- **Unused bindings as hard error** — rejected: contradicts the
  kernel's explicit "remains valid" rule; would amend retained
  semantics.
- **Silent only, no warning** — workable but declines the one ergonomic
  the IMP001 precedent makes cheap.
- **Distinct language sequence form** — rejected: creates a form the
  retained input cannot express; a conformance gap for the compiled
  path.
- **Restricting import/prelude shadowing** — rejected: contradicts
  C021's fixed precedence table.
- **Descriptive `Catena.Bindings` module / normative-only** — rejected
  patterns from C030's deliberation.

## Findings

All six hypotheses held; the developer chose the recommended option on
every fork (six of six, no overrides). Two refinements emerged during
fork resolution: the `_`-prefix exemption (a warning that fires on the
normative sequencing idiom itself would be self-defeating — the idiom's
binder is deliberately unused), and the proof shape for non-recursion
(a let RHS referencing its own binder is `T001` unbound, which the
compiler already enforces — the witness demonstrates it).

## Outcome

Resolved as C031 at revision `0.1.27`: the contract lives in the
[Bindings and Sequencing Specification](../60-specification/bindings-and-sequencing/README.md),
the reasoning in
[Catena Bindings and Sequencing](../20-notes/catena-bindings-and-sequencing.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G032 functions and
calls, G033 branching, P034 termination, P035 equality, P109 syntax,
and G088 cancellation mid-sequence remain open with their owners.
