---
title: "How Should Int and Float Relate Across Operators?"
kind: inquiry
created: "2026-08-31"
status: resolved
tags:
  - catena
  - numerics
  - language-design
aliases:
  - "G061 numeric relationships inquiry"
---

# How Should Int and Float Relate Across Operators?

## Purpose

G061 asks the checklist question: "Decide whether numeric overloading
uses traits, literal constraints, defaulting, coercions, or distinct
operators." C018 already rejected three of the five options — no
defaulting, no implicit coercion, no literal constraint generation
(`NM-OBL-005`/`NM-OBL-006`) — and C019 routed operator dispatch and
division here. What actually remained open: whether numeric operators
adopt trait dispatch or stay built-in forms, whether arithmetic joins
ordering and negation over `Float`, and where division and remainder
belong.

## Operational definitions

- **Numeric operator** — a built-in binary or unary primitive form
  with a fixed typing rule: `add`, `subtract`, `multiply`, the
  ordering operators, equality, negation.
- **Closed-set instantiation** — the operands unify with each other
  and the operator is defined for exactly the closed numeric set
  `{Int, Float}`; no instance search, no user extension.
- **Same-type rule** — both operands instantiate to the same numeric
  type; mixed `Int`/`Float` operands are ill-typed everywhere.

## Hypotheses

1. A new area `numeric-relationships` at `0.1.40` (code `NR`) carries
   the decision as a standard six-phase slice. *(Recommended.)*
2. **Closed-set monomorphic instantiation, no trait dispatch**:
   operators stay primitive forms whose operands unify with each
   other over exactly `{Int, Float}` — the pattern ordering and
   negation already use, made the rule for all numeric operators.
   Operators are never user-overloadable; a future numeric type
   joins the closed set by amending it in its own revision.
3. **Float arithmetic becomes checkable now, dormant by necessity**:
   extend `add`/`subtract`/`multiply` from Int-only to same-type
   `{Int, Float}` in the checker. Neither frozen frontend carries
   a float type or literal spelling, so the rule is
   correct-but-dormant — witnessed by driving the inference engine
   with float-typed operands, live with the first float-bearing
   frontend.
4. **Division and remainder route to G105** (checked and decimal
   arithmetic, the numeric library), matching C019's
   "G105/G061 with their own later revisions" split.
5. Zero new diagnostic families and no new public API: mixed-type
   rejection stays the unification error; nothing new exists to
   diagnose.

## Paths explored

- **Numeric trait dispatch** — rejected: makes operators
  user-overloadable in principle and adds dispatch evidence to
  operator sites, cutting against C001/C019 keeping operators
  fixed primitive forms.
- **Defer everything to P109** — rejected: strands the existing
  same-type ordering pattern half-justified and leaves G061's
  named question unanswered.
- **Fix division semantics now** — rejected: pre-empts G105's
  checked-arithmetic decisions (division-by-zero classification,
  truncation, remainder sign).
- **Keep arithmetic Int-only** — rejected: the annotation witness
  makes the extension nearly free, and the ordering/arithmetic
  asymmetry has no principled defender.

## Findings

All five hypotheses held; the developer chose the recommended
option on all four forks (no overrides). The decisive corpus facts:
C018's three rejections collapse the checklist's option list;
`infer.ex` already implements same-type instantiation for ordering;
the evaluator's `+`/`-`/`*` run Elixir floats natively, so only the
checkers pin arithmetic to Int.

## Outcome

Resolved as C061 at revision `0.1.40`: the contract will live in
`60-specification/numeric-relationships/`, the reasoning in
[Catena Numeric Relationships](../20-notes/catena-numeric-relationships.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). G105 keeps
explicit conversions, checked and decimal arithmetic, division and
remainder semantics, and the numeric library.
