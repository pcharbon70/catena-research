---
title: "Which Pattern Contexts Admit Refutable Patterns?"
kind: inquiry
created: "2026-08-31"
status: resolved
tags:
  - catena
  - patterns
  - language-design
aliases:
  - "P044 refutability by context inquiry"
---

# Which Pattern Contexts Admit Refutable Patterns?

## Purpose

P044 asks the checklist question: "Local bindings, generators,
public receives, handlers, and exception clauses still need their
own admissibility and failure rules." C002 completed match-clause
refutability and explicitly reserved the rest; its refutability
boundary says future contexts "MUST either admit only patterns
proven irrefutable or define an explicit failure construct" and
"MUST NOT inherit an implicit runtime match exception." This
inquiry turns that reservation into per-context rules.

## Operational definitions

- **Refutable pattern** — a pattern not proved total for its
  scrutinee type by the C045 usefulness relation.
- **Pattern context** — any syntactic position that binds by
  pattern: match clauses, `let` binders, function parameters,
  comprehension generators, receive clauses, handler clauses,
  exception clauses.
- **Implicit runtime match failure** — a context whose pattern
  mismatch becomes an unspecified dynamic failure no source rule
  names; the property the corpus forbids.

## Hypotheses

1. A new area `pattern-contexts` at `0.1.38` (code `PC`) carries
   the contract as a **classification slice**: three context
   classes — exhaustive, irrefutable-only, explicit-failure — with
   per-context rules and reservations, no grammar changes.
   *(Recommended: C037's deferred-exclusion sweep shape.)*
2. **Match is the only exhaustive context**; C045's usefulness
   relation and `M001`/`M002` stay authoritative and unchanged.
3. **let binders and function parameters are irrefutable-only on
   arrival**: C031's plain-name binder stands today; when pattern
   binding arrives it must be proved total or carry an explicit
   failure construct — never a hidden runtime match.
4. **Generators get the principle, not the grammar**: ordinary
   generators require total patterns; filtering generators
   explicitly request mismatch-as-skip (the ADT synthesis
   proposal); grammar, effects, and lowering stay P051's.
5. **Public receives are reserved** (any future public receive is
   exhaustive over its message type or carries an explicit total
   fallback in its own slice; C003 stays a lowering harness);
   **handler clauses keep plain binders** (irrefutable-only on
   arrival); **exception clauses are permanently excluded** (C036's
   trap is terminal; failures are typed values or traps); and
   **D046's programmable patterns are excluded** with arrival
   conditions recorded (effects, totality, coverage, evaluation
   count, cost).

## Paths explored

- **Admit let-patterns now** (irrefutable-only, implemented) —
  rejected: touches both frontends ahead of P109's surface work
  with no user demand recorded.
- **Pointer-only closure** (cite C002's reservation, no new
  revision) — rejected: the reservation states a requirement on
  future slices, not rules for the five contexts P044 names.
- **Specify public receive or generator grammar now** — rejected:
  invents forms before their owning slices (the C038
  invented-form pattern).
- **Reserve exception clauses for a future mechanism** — rejected:
  contradicts C036's closed failure taxonomy; no such mechanism is
  planned.
- **Leave D046 deferred** — rejected: its exclusion is one table
  row here; a separate later slice adds ceremony without content.

## Findings

All five hypotheses held; the developer chose the recommended
option on all five forks (no overrides). The ADT synthesis's
refutability conclusions (lines 437–451) carried directly:
refutable patterns are rejected in `let`, parameters, and ordinary
generators; explicit filtering generators may request
mismatch-as-skip; other contexts use total results; no ordinary
expression hides a runtime Match failure.

## Outcome

Resolved as C044 at revision `0.1.38`: the contract will live in
`60-specification/pattern-contexts/`, the reasoning in
[Catena Pattern Contexts](../20-notes/catena-pattern-contexts.md),
and the forks in the [design decision
register](../20-notes/design-decision-register.md). D046 closes as
C046 in the same change. Generator grammar (P051), public receive
grammar, later pattern forms (list, record, variant, binary,
range), and P109 spellings remain with their owners.
