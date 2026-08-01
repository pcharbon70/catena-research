---
title: "Warnings for Pattern Matching"
kind: source
created: "2026-07-31"
authors:
  - "Luc Maranget"
published: 2007
citation_key: "maranget2007WarningsPatternMatching"
container: "Journal of Functional Programming 17(3): 387–421"
edition: null
isbn: null
doi: "10.1017/S0956796807006223"
url: "https://www.cambridge.org/core/journals/journal-of-functional-programming/article/warnings-for-pattern-matching/3165B75113781E2431E3856972940347"
accessed: "2026-07-31"
tags:
  - algebraic-data-types
  - compilers
  - pattern-matching
aliases:
  - "Maranget on pattern-match warnings"
---

# Warnings for Pattern Matching

## Reference

Luc Maranget, “Warnings for Pattern Matching,” *Journal of Functional
Programming* 17, no. 3 (2007): 387–421.
[DOI](https://doi.org/10.1017/S0956796807006223),
[publisher record](https://www.cambridge.org/core/journals/journal-of-functional-programming/article/warnings-for-pattern-matching/3165B75113781E2431E3856972940347),
and [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3165B75113781E2431E3856972940347/S0956796807006223a.pdf/warnings-for-pattern-matching.pdf).

## Research question

Can non-exhaustive matches and useless clauses be detected directly from
pattern semantics, independently of the compiler's chosen match-code strategy,
with precise diagnostics and practical cost?

## Method

Maranget models constructor patterns as rows in a pattern matrix. The
usefulness predicate asks whether a candidate row matches some typed value not
already covered by preceding rows. Recursive specialization by constructors
defines the algorithm. The paper proves the analysis correct for strict,
generic lazy, and Haskell matching, extends it to or-patterns and missing-case
witnesses, implements it in Objective Caml, and measures pathological matrices
and real compilers.

## Findings

- Exhaustiveness and redundancy are dual uses of one semantic question. A
  match is exhaustive exactly when a wildcard candidate is not useful after
  all existing rows; an existing row is useless when it covers no new value.
- Typed constructor signatures make the search finite for ordinary finite
  ADTs. Products are single-constructor types; booleans are two nullary
  constructors; recursive payloads are analyzed structurally.
- A missing-case diagnostic can return a pattern witness representing values
  not covered, giving programmers more actionable information than a bare
  “non-exhaustive” warning.
- Coverage analysis does not need to reuse match compilation. Keeping the
  semantic checker separate permits either decision-tree or backtracking code
  generation.
- The same recursive core can support strict and non-strict matching after the
  value and matching semantics are made explicit.
- Naive analysis has exponential worst cases. Safeguards trade some ordinary
  overhead for protection against adversarial pattern matrices; measured cost
  on the studied real programs remained low.
- The formalization assumes types are inhabited. Empty types can therefore
  produce false uselessness or non-exhaustiveness conclusions unless the
  checker incorporates type-inhabitation knowledge.

## Relevance

Catena should make exhaustive `match` an error by default and produce concrete
missing-pattern witnesses. Coverage checking should consume the typed pattern
matrix after constructor resolution, but remain semantically separate from
decision-tree generation. Because Catena includes an empty type and may later
include GADTs, its checker cannot adopt the paper's inhabited-type assumption
without qualification.

## Limits

The core treatment does not solve guards, arbitrary extractors, view patterns,
GADT equalities, effectful patterns, or open variant rows. Its practical data
comes from the Objective Caml implementation and a small program set. The
algorithm and safeguards are a foundation, not a complete modern coverage
specification.

## Derived work

- [Algebraic Data Types](../20-notes/algebraic-data-types.md)
- [How Should Catena Specify Algebraic Data Types?](../40-inquiries/how-should-catena-specify-algebraic-data-types.md)
- [Algebraic Data Types map](../10-maps/algebraic-data-types.md)
