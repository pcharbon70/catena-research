---
title: "Catena Pattern Contexts"
kind: note
created: "2026-08-31"
maturity: developing
tags:
  - catena
  - patterns
  - refutability
  - language-design
aliases:
  - "pattern context classification"
---

# Catena Pattern Contexts

## Executive conclusion

Catena needs exactly three classes of pattern context, and only one
of them exists in the executable grammar today. Match is the
**exhaustive context**: patterns must cover the scrutinee type and
the C045 usefulness relation enforces it (`M001`/`M002`). Every
other current or future binding position is **irrefutable-only** —
a pattern must be proved total for the bound type or the form
rejects — or **explicit-failure** — the construct visibly names its
mismatch behavior, as a filtering generator's mismatch-as-skip
will. No context anywhere inherits an implicit runtime match
failure. That single principle, applied per context, is the whole
of P044; the grammar does not change.

## Scope, method, and definitions

This note synthesizes the archive's evidence for closing P044 (and
D046 with it) as a classification slice at revision `0.1.38`. It
reads C002's refutability boundary, C003's receive harness, C005's
handler clauses, C031's plain-name `let`, C036's failure taxonomy,
C045's usefulness relation, and the ADT and comprehension
syntheses; it invents no syntax.

- **Refutable pattern** — not proved total for its scrutinee type
  by the usefulness relation.
- **Context class** — exhaustive, irrefutable-only, or
  explicit-failure, as defined above.

## The context inventory

| Context | Exists today | Class | Rule |
| --- | --- | --- | --- |
| Match clauses | yes (JSON AST 0.1.2, kernel 0.1.8) | exhaustive | C045 unchanged: cover or `M001`; useless rows `M002` |
| `let` binders | plain names only (C031) | irrefutable-only on arrival | today pattern binding is not a `let` form; when specified, proved-total or explicit-failure |
| Function parameters | plain names only | irrefutable-only on arrival | C002's reservation codified |
| Comprehension generators | no (Section 6) | split | ordinary generators total; filtering generators explicit mismatch-as-skip — principle fixed here, grammar P051's |
| Public receives | no (C003 is a lowering harness) | reserved | on arrival: exhaustive over the message type or an explicit total fallback (timeout/default), in its own slice |
| Handler clauses | plain parameters + resumption binder (C005) | irrefutable-only on arrival | no patterns today; on arrival, proved-total or explicit-failure |
| Exception clauses | no — and never | excluded | C036: `trap` is terminal, failures are typed values or traps; no exception mechanism exists or is planned |

## Why irrefutable-only is the default

The corpus's own rules force it. C002 reserves it; the ADT
synthesis argues it (an accidental partial destructure must not
become an invisible filter or a hidden crash); C036 leaves no
exception to catch a mismatch with; and C031 made `let` a plain
name precisely so sequencing never hides selection. A refutable
pattern in a binding position has three honest spellings — prove
it total, make the failure a value (`Option`), or make the
selection visible (`match`, or an explicit filtering form) — and
each already has an owner.

## The D046 exclusion

View patterns, pattern synonyms, and active patterns are excluded.
C002 already excluded the forms without reserving hidden
conversion semantics; what D046 adds is the arrival condition
record: any future programmable pattern is its own slice and must
state its effects, totality, coverage obligations, evaluation
count, and cost before existing. Patterns stay pure — no calls, no
effects, no user-defined tests (C002).

## Tradeoffs, limitations, falsification

The slice's honesty rests on reservations being narrow: if P109 or
Section 6 ships a binding position whose mismatch behavior this
table did not name, the table is falsified and must be amended by
a new revision. The exclusion of exception clauses is a design
commitment, not a proof; it stands unless a future slice reopens
C036's taxonomy. Zero new diagnostics and zero new public API are
deliberate — nothing executable changes.

## Research priorities

Section 6 (P047–P056) consumes the generator principle; P109's
surface grammar will meet the irrefutable-only rule at every
binding it introduces; the open pattern-form question (list,
record, variant, binary, range literals in patterns) stays with
the data-model program.

## Route to sources

- [Pattern Contexts Specification](../60-specification/pattern-contexts/README.md)
  — the normative `0.1.38` contract.
- [Construction and Pattern Typing](../60-specification/data-and-patterns/construction-and-pattern-typing.md)
  — C002's refutability boundary this slice executes.
- [Match Semantics and Coverage](../60-specification/data-and-patterns/match-semantics-and-coverage.md)
  — the exhaustive context's authority.
- [Algebraic Data Types](algebraic-data-types.md) — the refutability
  conclusions (437–451) this slice codifies.
- [List Comprehensions](list-comprehensions.md) — the generator
  split this slice fixes as principle.
- [Resolved inquiry](../40-inquiries/which-pattern-contexts-admit-refutable-patterns.md)
  and the [topic map](pattern-contexts.md).
